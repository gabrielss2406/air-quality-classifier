import streamlit as st
import joblib
import pandas as pd
import os

model_path = os.getenv("MODEL_PATH", "model.pkl")
model = joblib.load(model_path)

st.set_page_config(page_title="Monitor da Poluição", page_icon="🌬️")

if 'history' not in st.session_state:
    st.session_state.history = []

st.markdown("""
<style>
    .main {
        background-color: #e6e6e6;
    }
    div.stButton > button {
        background-color: #ff4d4d !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 0.6rem 1rem !important;
        font-size: 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🏭 Monitor da Qualidade do Ar")

st.markdown("### Insira os Índices de Qualidade do Ar (AQI):")

location_name = st.text_input("Nome da Localização", placeholder="Ex: Centro da Cidade")

col1, col2 = st.columns(2)

with col1:
    O3 = st.number_input("Ozônio (O3)", min_value=0.0, value=50.0)
    CO = st.number_input("Monóxido de Carbono (CO)", min_value=0.0, value=0.9)
    NO2 = st.number_input("Dióxido de Nitrogênio (NO2)", min_value=0.0, value=40.0)

with col2:
    PM10 = st.number_input("Partículas Inaláveis (PM10)", min_value=0.0, value=72.0)
    PM25 = st.number_input("Partículas Finas (PM2.5)", min_value=0.0, value=32.0)
    SO2 = st.number_input("Dióxido de Enxofre (SO2)", min_value=0.0, value=4.0)

if st.button("🚨 Verificar Nível de Poluição"):
    try:
        feature_names = ['O3_aqi', 'CO_aqi', 'NO2_aqi', 'PM10_aqi', 'PM2_5_aqi', 'SO2_aqi']
        data = [[O3, CO, NO2, PM10, PM25, SO2]]
        df_pred = pd.DataFrame(data, columns=feature_names)
        result = model.predict(df_pred)[0]
        print(result)

        if result == 1:
            st.error(f"Ambiente poluído 👎")
        else:
            st.success(f"Ambiente não poluído 👍")
        
        result_label = "poluído" if result == 1 else "não poluído"
        st.session_state.history.append({
            "Localização": location_name,
            "Resultado": result_label,
            "O3": O3, "CO": CO, "NO2": NO2, 
            "PM10": PM10, "PM2.5": PM25, "SO2": SO2
        })
            
    except Exception as e:
        st.error(f"Erro ao classificar: {e}")

if st.session_state.history:
    st.markdown("---")
    st.markdown("### Histórico de Medições")
    
    # Inverte a ordem do histórico para mostrar o mais recente primeiro
    reversed_history = st.session_state.history[::-1]
    
    df = pd.DataFrame(reversed_history)
    st.dataframe(df)