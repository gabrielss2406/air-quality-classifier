import streamlit as st
import requests
import joblib
import pandas as pd
import os
import sys
import folium
from streamlit_folium import st_folium

# Adiciona o diretório raiz ao sys.path para encontrar o módulo utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.aqi import aqi_calc

# Carrega o modelo
model_path = os.getenv("MODEL_PATH", "research/model.pkl")
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"Arquivo do modelo não encontrado em: {model_path}")
    st.stop()

st.set_page_config(page_title="Calcular por Localização", page_icon="📍")

st.title("📍 Calcular por Localização")

# Inicializa o estado da sessão para histórico e coordenadas
if "history_location" not in st.session_state:
    st.session_state.history_location = []
if "map_center" not in st.session_state:
    st.session_state.map_center = [-14.235, -51.925]  # Centro do Brasil
if "map_zoom" not in st.session_state:
    st.session_state.map_zoom = 4
if "lat_input" not in st.session_state:
    st.session_state.lat_input = -23.55  # Padrão: São Paulo
if "lon_input" not in st.session_state:
    st.session_state.lon_input = -46.63  # Padrão: São Paulo

st.markdown("### Clique no mapa ou insira as coordenadas:")

# Criação do mapa
m = folium.Map(
    location=st.session_state.map_center, zoom_start=st.session_state.map_zoom
)
folium.Marker(
    [st.session_state.lat_input, st.session_state.lon_input],
    popup="Localização Selecionada",
).add_to(m)

# Exibe o mapa e captura a interação
map_data = st_folium(m, width=700, height=500, key="folium_map")

# Atualiza as coordenadas com base no clique do mapa
if map_data and map_data["last_clicked"]:
    lat, lon = map_data["last_clicked"]["lat"], map_data["last_clicked"]["lng"]
    # Atualiza tanto os inputs quanto o centro do mapa
    if st.session_state.lat_input != lat or st.session_state.lon_input != lon:
        st.session_state.lat_input = lat
        st.session_state.lon_input = lon
        st.session_state.map_center = [lat, lon]
        st.rerun()


# Função callback para atualizar o mapa quando os inputs mudarem
def update_map_center():
    st.session_state.map_center = [
        st.session_state.lat_input,
        st.session_state.lon_input,
    ]


# Inputs para latitude e longitude
latitude = st.number_input(
    "Latitude",
    min_value=-90.0,
    max_value=90.0,
    value=st.session_state.lat_input,
    key="lat_input",
    on_change=update_map_center,
)
longitude = st.number_input(
    "Longitude",
    min_value=-180.0,
    max_value=180.0,
    value=st.session_state.lon_input,
    key="lon_input",
    on_change=update_map_center,
)

if st.button("🚨 Verificar Qualidade do Ar na Localização"):
    if not (latitude is not None and longitude is not None):
        st.warning("Por favor, insira valores válidos para Latitude e Longitude.")
    else:
        try:
            api_url = (
                f"https://air-quality-api.open-meteo.com/v1/air-quality?"
                f"latitude={latitude}&longitude={longitude}&"
                f"current=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone&"
                f"timezone=auto"
            )
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()

            if "current" in data:
                current_data = data["current"]

                o3_ug = current_data.get("ozone")
                co_ug = current_data.get("carbon_monoxide")
                no2_ug = current_data.get("nitrogen_dioxide")
                pm10_ug = current_data.get("pm10")
                pm25_ug = current_data.get("pm2_5")
                so2_ug = current_data.get("sulphur_dioxide")

                aqi_results = aqi_calc(
                    pm25=pm25_ug,
                    pm10=pm10_ug,
                    o3=o3_ug,
                    no2=no2_ug,
                    so2=so2_ug,
                    co=co_ug,
                )

                feature_names = [
                    "O3_aqi",
                    "CO_aqi",
                    "NO2_aqi",
                    "PM10_aqi",
                    "PM2_5_aqi",
                    "SO2_aqi",
                ]

                data_for_pred = [
                    [
                        aqi_results["O3"],
                        aqi_results["CO"],
                        aqi_results["NO2"],
                        aqi_results["PM10"],
                        aqi_results["PM2.5"],
                        aqi_results["SO2"],
                    ]
                ]

                df_pred = pd.DataFrame(data_for_pred, columns=feature_names)
                result = model.predict(df_pred)[0]

                if result == 1:
                    st.error("Ambiente poluído 👎")
                else:
                    st.success("Ambiente não poluído 👍")

                result_label = "poluído" if result == 1 else "não poluído"

                st.session_state.history_location.append(
                    {
                        "Latitude": latitude,
                        "Longitude": longitude,
                        "Resultado": result_label,
                        "O3 (µg/m³)": o3_ug,
                        "CO (µg/m³)": co_ug,
                        "NO2 (µg/m³)": no2_ug,
                        "PM10 (µg/m³)": pm10_ug,
                        "PM2.5 (µg/m³)": pm25_ug,
                        "SO2 (µg/m³)": so2_ug,
                    }
                )
            else:
                st.warning(
                    "Não foi possível obter dados de qualidade do ar para esta localização."
                )

        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao conectar com a API: {e}")
        except Exception as e:
            st.error(f"Erro ao processar dados ou classificar: {e}")

if st.session_state.history_location:
    st.markdown("---")
    st.markdown("### Histórico de Medições por Localização")
    reversed_history_location = st.session_state.history_location[::-1]
    df_history = pd.DataFrame(reversed_history_location)
    st.dataframe(df_history)
