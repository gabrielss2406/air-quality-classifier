import streamlit as st
import joblib
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.aqi import aqi_calc

model_path = os.getenv("MODEL_PATH", "research/model.pkl")
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"Arquivo do modelo não encontrado em: {model_path}")
    st.stop()

st.set_page_config(page_title="Calcular Poluição", page_icon="🏭")

st.title("🏭 Calcular Nível de Poluição")

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("### Insira as concentrações de poluentes (em µg/m³):")

with st.expander("ℹ️ O que fazemos com esses valores?"):
    st.markdown("""
    Convertemos esses valores para a medida de Índice de Qualidade do Ar (AQI), uma medida diária da limpeza ou poluição do ar, para classificar o ambiente e possibilitar a análise.
    """)

location_name = st.text_input("Nome da Localização", placeholder="Ex: Centro da Cidade")

col1, col2 = st.columns(2)

with col1:
    O3_ug = st.number_input("Ozônio (O3 [µg/m³])", min_value=0.0, value=55.0)
    CO_ug = st.number_input(
        "Monóxido de Carbono (CO [µg/m³])", min_value=0.0, value=115.0
    )
    NO2_ug = st.number_input(
        "Dióxido de Nitrogênio (NO2 [µg/m³])", min_value=0.0, value=1.0
    )

with col2:
    PM10_ug = st.number_input(
        "Partículas Inaláveis (PM10 [µg/m³])", min_value=0.0, value=5.0
    )
    PM25_ug = st.number_input(
        "Partículas Finas (PM2.5 [µg/m³])", min_value=0.0, value=4.0
    )
    SO2_ug = st.number_input(
        "Dióxido de Enxofre (SO2 [µg/m³])", min_value=0.0, value=1.0
    )

if st.button("🚨 Verificar Nível de Poluição"):
    if not location_name:
        st.warning("Por favor, insira um nome para a localização.")
    else:
        try:
            aqi_results = aqi_calc(
                pm25=PM25_ug, pm10=PM10_ug, o3=O3_ug, no2=NO2_ug, so2=SO2_ug, co=CO_ug
            )

            feature_names = [
                "O3_aqi",
                "CO_aqi",
                "NO2_aqi",
                "PM10_aqi",
                "PM2_5_aqi",
                "SO2_aqi",
            ]

            data = [
                [
                    aqi_results["O3"],
                    aqi_results["CO"],
                    aqi_results["NO2"],
                    aqi_results["PM10"],
                    aqi_results["PM2.5"],
                    aqi_results["SO2"],
                ]
            ]

            df_pred = pd.DataFrame(data, columns=feature_names)

            result = model.predict(df_pred)[0]

            if result == 1:
                st.error("Ambiente poluído 👎")
            else:
                st.success("Ambiente não poluído 👍")

            with st.expander("Ver detalhes da medição"):
                col1, col2, col3 = st.columns(3)
                col1.metric("O3 AQI", f"{aqi_results['O3']}", f"{O3_ug} µg/m³", delta_color="off")
                col2.metric("CO AQI", f"{aqi_results['CO']}", f"{CO_ug} µg/m³", delta_color="off")
                col3.metric("NO2 AQI", f"{aqi_results['NO2']}", f"{NO2_ug} µg/m³", delta_color="off")
                col1.metric("PM10 AQI", f"{aqi_results['PM10']}", f"{PM10_ug} µg/m³", delta_color="off")
                col2.metric("PM2.5 AQI", f"{aqi_results['PM2.5']}", f"{PM25_ug} µg/m³", delta_color="off")
                col3.metric("SO2 AQI", f"{aqi_results['SO2']}", f"{SO2_ug} µg/m³", delta_color="off")

            result_label = "poluído" if result == 1 else "não poluído"

            st.session_state.history.append(
                {
                    "Localização": location_name,
                    "Resultado": result_label,
                    "O3 (µg/m³)": O3_ug,
                    "CO (µg/m³)": CO_ug,
                    "NO2 (µg/m³)": NO2_ug,
                    "PM10 (µg/m³)": PM10_ug,
                    "PM2.5 (µg/m³)": PM25_ug,
                    "SO2 (µg/m³)": SO2_ug,
                }
            )

        except Exception as e:
            st.error(f"Erro ao classificar: {e}")

if st.session_state.history:
    st.markdown("---")
    st.markdown("### Histórico de Medições")

    reversed_history = st.session_state.history[::-1]

    df = pd.DataFrame(reversed_history)
    st.dataframe(df)
