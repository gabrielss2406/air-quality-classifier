import streamlit as st
import joblib
import pandas as pd
import os

# Carrega o modelo
model_path = os.getenv("MODEL_PATH", "research/model.pkl")
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    st.error(f"Arquivo do modelo não encontrado em: {model_path}")
    st.stop()

st.set_page_config(page_title="Calcular Poluição", page_icon="🏭")

st.title("🏭 Calcular Nível de Poluição")

# Inicializa o histórico na session_state se não existir
if "history" not in st.session_state:
    st.session_state.history = []

st.markdown("### Insira os Índices de Qualidade do Ar (AQI):")

with st.expander("ℹ️ O que é o AQI e como ele é calculado?"):
    st.markdown("""
    #### 1. O que é o AQI?
    O **Índice de Qualidade do Ar (AQI)** funciona como um "termômetro" da poluição. Quanto maior o número, maior o risco para a saúde.

    #### 2. Como a conta é feita?
    O cálculo **não é uma linha reta única**. Ele funciona em **degraus**, usando uma técnica chamada *Interpolação Linear Segmentada*.

    * **O Conceito:** A fórmula muda dependendo da gravidade.
    * **Na Prática:** Primeiro, identificamos em qual "faixa" a poluição se encontra (ex: faixa boa ou ruim). Depois, aplicamos uma regra de três específica para aquele pedaço.
    
    É por isso que o índice sobe mais rápido em algumas faixas (como quando o ar começa a ficar perigoso) do que em outras. O valor final do AQI do dia é sempre determinado pelo **pior poluente** medido no momento.
    """)

location_name = st.text_input("Nome da Localização", placeholder="Ex: Centro da Cidade")

col1, col2 = st.columns(2)

with col1:
    O3 = st.number_input("Ozônio (O3 [AQI])", min_value=0.0, value=28.0)
    CO = st.number_input("Monóxido de Carbono (CO [AQI])", min_value=0.0, value=1.0)
    NO2 = st.number_input("Dióxido de Nitrogênio (NO2 [AQI])", min_value=0.0, value=1.0)

with col2:
    PM10 = st.number_input(
        "Partículas Inaláveis (PM10 [AQI])", min_value=0.0, value=5.0
    )
    PM25 = st.number_input("Partículas Finas (PM2.5 [AQI])", min_value=0.0, value=15.0)
    SO2 = st.number_input("Dióxido de Enxofre (SO2 [AQI])", min_value=0.0, value=1.0)

if st.button("🚨 Verificar Nível de Poluição"):
    if not location_name:
        st.warning("Por favor, insira um nome para a localização.")
    else:
        try:
            feature_names = [
                "O3_aqi",
                "CO_aqi",
                "NO2_aqi",
                "PM10_aqi",
                "PM2_5_aqi",
                "SO2_aqi",
            ]
            data = [[O3, CO, NO2, PM10, PM25, SO2]]
            df_pred = pd.DataFrame(data, columns=feature_names)

            result = model.predict(df_pred)[0]

            if result == 1:
                st.error("Ambiente poluído 👎")
            else:
                st.success("Ambiente não poluído 👍")

            result_label = "poluído" if result == 1 else "não poluído"
            st.session_state.history.append(
                {
                    "Localização": location_name,
                    "Resultado": result_label,
                    "O3": O3,
                    "CO": CO,
                    "NO2": NO2,
                    "PM10": PM10,
                    "PM2.5": PM25,
                    "SO2": SO2,
                }
            )

        except Exception as e:
            st.error(f"Erro ao classificar: {e}")

# Exibe o histórico de medições
if st.session_state.history:
    st.markdown("---")
    st.markdown("### Histórico de Medições")

    # Inverte a ordem do histórico para mostrar o mais recente primeiro
    reversed_history = st.session_state.history[::-1]

    df = pd.DataFrame(reversed_history)
    st.dataframe(df)
