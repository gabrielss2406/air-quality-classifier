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

st.header("Contexto")

st.markdown("""
O Brasil enfrenta uma crise sanitária silenciosa de grandes proporções impulsionada pela poluição atmosférica, que se consolidou como um dos maiores riscos ambientais à saúde pública nacional. Dados recentes indicam que, apenas entre 2019 e 2021, a má qualidade do ar foi responsável por mais de 326 mil óbitos no país. A exposição contínua a poluentes, especialmente o material particulado fino (MP2,5), está diretamente associada ao agravamento de doenças isquêmicas do coração, acidentes vasculares cerebrais e câncer de pulmão, afetando de forma desproporcional crianças e idosos.

A gravidade do cenário tornou-se inegável durante a crise ambiental de 2024, quando a combinação de seca extrema e queimadas expôs milhões de brasileiros a níveis tóxicos de fumaça. Na região Amazônica, localidades como Boca do Acre (AM) chegaram a registrar concentrações de poluentes 653% acima do limite diário seguro estipulado pela Organização Mundial da Saúde (OMS). O impacto transbordou as fronteiras regionais, fazendo com que a cidade de São Paulo fosse momentaneamente classificada, em setembro de 2024, como a metrópole com a pior qualidade de ar do mundo em rankings internacionais, evidenciando que o problema é sistêmico e afeta todo o território nacional.

Além do custo humano, a poluição impõe um fardo econômico insustentável ao Estado, transformando a questão ambiental em um problema de responsabilidade fiscal. Estima-se que o Sistema Único de Saúde (SUS) tenha um dispêndio médio anual de aproximadamente R$ 2,5 bilhões apenas com internações por doenças cardiorrespiratórias atribuíveis à queima de biomassa na Amazônia e no Cerrado. Essa sangria de recursos demonstra que a inação no controle de emissões resulta em prejuízo direto aos cofres públicos, drenando verbas que poderiam ser investidas na promoção da saúde primária.

A motivação para novos estudos é reforçada pela fragilidade do atual arcabouço regulatório e pela insuficiência de dados. Embora o Conselho Nacional do Meio Ambiente (CONAMA) tenha atualizado as normas através da Resolução nº 506/2024, os prazos de transição são longos e permitem que o país opere com metas de poluição muito acima das recomendações da OMS por décadas. Somado a isso, o Brasil opera com um déficit crítico de monitoramento: relatórios do IEMA apontam a necessidade imediata de mais de 100 novas estações para cobrir adequadamente a população, visto que diversas capitais e grandes centros urbanos ainda carecem de sensores automáticos.

Portanto, a realização deste estudo justifica-se pela urgência em confrontar a "cegueira institucional" sobre a real dimensão da qualidade do ar no Brasil. A discrepância entre a severidade dos dados epidemiológicos e a leniência das políticas de controle exige a produção de evidências científicas robustas. Apenas através de uma análise detalhada será possível subsidiar políticas públicas capazes de reverter esse quadro de morbimortalidade e garantir o direito fundamental da população a um ambiente respirável e seguro.
""")

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
    - **Análise Detalhada:** Visualize insights e como foi o desenvolvimento do modelo desse projeto.
    """
)

st.info("👈 Selecione uma opção no menu lateral para começar.")
