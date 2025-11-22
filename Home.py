import streamlit as st

st.set_page_config(
    page_title="Monitor da Qualidade do Ar", page_icon="🌬️", layout="wide"
)

if "history" not in st.session_state:
    st.session_state.history = []

st.markdown(
    """
<style>
    .main {
        background-color: #f0f2f6;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ff4d4d;
    }
    .stButton > button {
        background-color: #ff4d4d;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        font-size: 1rem;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #e60000;
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
        transform: translateY(-2px);
    }
</style>
""",
    unsafe_allow_html=True,
)

st.title("🌬️ Bem-vindo ao Monitor da Qualidade do Ar")

st.markdown("---")

st.header("Sobre a Aplicação")
st.write(
    """
    Este aplicativo foi desenvolvido para fornecer uma análise simples e rápida da qualidade do ar 
    com base nos principais poluentes. Utilize o menu lateral para navegar entre as funcionalidades.
    """
)

st.subheader("Funcionalidades:")
st.markdown(
    """
    - **Calcular Poluição:** Insira manualmente os valores dos poluentes para obter uma classificação instantânea.
    - **Calcular por Localização:** (Em breve) Obtenha a qualidade do ar para uma localização específica.
    - **Análise Detalhada:** Visualize o histórico de todas as medições realizadas.
    """
)

st.info("👈 Selecione uma opção no menu lateral para começar.")
