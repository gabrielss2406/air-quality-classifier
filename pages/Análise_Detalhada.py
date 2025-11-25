import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Análise Detalhada", page_icon="📊")

st.title("📊 Análise Detalhada")

st.markdown("""
Esta página apresenta uma análise exploratória detalhada dos dados de poluição do ar no Brasil, 
incluindo distribuições de variáveis e correlações entre poluentes.
""")

with st.spinner("Carregando análise..."):
    sns.set_theme(style="whitegrid", palette="viridis")
    plt.rcParams["figure.figsize"] = (12, 6)


    @st.cache_data
    def load_data():
        path = os.path.join("research", "pollution_data_brazil.csv")
        df = pd.read_csv(path)
        return df


    df = load_data()

    cols_poluentes = [
        "O3_medida",
        "O3_aqi",
        "CO_medida",
        "CO_aqi",
        "NO2_medida",
        "NO2_aqi",
        "PM10_medida",
        "PM10_aqi",
        "PM2_5_medida",
        "PM2_5_aqi",
        "SO2_medida",
        "SO2_aqi",
    ]

    st.header("📈 Distribuição das Variáveis Numéricas")

    st.markdown("""
    Os gráficos abaixo mostram a distribuição dos principais poluentes atmosféricos medidos no Brasil.
    Analisamos tanto os valores brutos medidos pelos sensores quanto os índices AQI (Air Quality Index) padronizados.
    """)

    axes = df[cols_poluentes].hist(bins=30, figsize=(15, 12))
    fig = axes.flatten()[0].figure
    plt.suptitle("Distribuição das Variáveis Numéricas dos Poluentes")
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

    st.subheader("🔍 Análise das Distribuições")

    with st.expander("**O3 (Ozônio) - medida / aqi**"):
        st.markdown("""
        - Distribuição levemente assimétrica
        - Grande concentração entre 20–60
        - Cauda curta de valores mais altos
        - **Interpretação**: O ozônio costuma ter picos ocasionais, mas de forma geral é relativamente estável. 
          Pode ser um indicativo moderado de poluição.
        """)

    with st.expander("**CO (Monóxido de Carbono) - medida / aqi**"):
        st.markdown("""
        - Extremamente assimétricos
        - Muitos valores próximos de zero
        - Cauda longa atingindo valores bem altos
        - **Interpretação**: CO é claramente uma variável com muitos valores muito baixos e alguns picos isolados 
          (talvez áreas industriais, tráfego intenso, ou falhas pontuais de medição).
        """)

    with st.expander("**NO2 (Dióxido de Nitrogênio) - medida / aqi**"):
        st.markdown("""
        - Muito concentrado perto de zero
        - Poucos valores mais altos (>60)
        - **Interpretação**: NO₂ está fortemente associado a poluição por tráfego e combustão. 
          Mesmo com baixa ocorrência de picos, os valores altos podem discriminar bem locais poluídos.
        """)

    with st.expander("**PM10 (Material Particulado ≤10μm) - medida / aqi**"):
        st.markdown("""
        - Assimetria muito forte
        - Grande concentração perto de zero
        - Cauda longa
        - **Interpretação**: PM10 é uma das métricas mais importantes para classificar poluição e aqui ela 
          parece ter vários valores extremos. É uma variável com comportamento ideal para ser usada como 
          feature principal no modelo.
        """)

    with st.expander("**PM2.5 (Material Particulado ≤2.5μm) - medida / aqi**"):
        st.markdown("""
        - Distribuição semelhante ao PM10, mas menos extrema
        - Valores médios variam entre 10–50 com cauda até >100
        - **Interpretação**: PM2.5 é extremamente correlacionado com riscos para saúde e é um excelente 
          indicador de poluição. Precisará de transformação por causa da cauda longa.
        """)

    with st.expander("**SO2 (Dióxido de Enxofre) - medida / aqi**"):
        st.markdown("""
        - Muito concentrado abaixo de 5
        - Pouquíssimos valores altos
        - **Interpretação**: SO₂ costuma ser baixo em muitos lugares e só sobe em regiões industriais ou 
          queima de carvão. Pode ajudar a identificar locais específicos fortemente poluídos, mas não será 
          tão útil para generalização.
        """)

    st.header("🔗 Análise de Correlações")

    st.markdown("""
    As correlações entre variáveis nos ajudam a entender como os diferentes poluentes e fatores ambientais 
    se relacionam entre si e com a classificação de ambientes poluídos.
    """)

    st.subheader("Matriz de Correlação Completa")

    numeric_df = df.select_dtypes(include=np.number)
    corr = numeric_df.corr()

    fig_corr, ax_corr = plt.subplots(figsize=(14, 10))
    sns.heatmap(corr, annot=False, cmap="viridis", linewidths=0.5, ax=ax_corr)
    ax_corr.set_title("Matriz de Correlação", fontsize=16)
    plt.tight_layout()
    st.pyplot(fig_corr)
    plt.close()

    st.subheader("Correlação com a Variável 'polluted'")

    st.markdown("""
    O gráfico abaixo mostra quais variáveis têm maior correlação com a classificação de ambientes poluídos.
    """)

    corrs = numeric_df.corr()["polluted"].sort_values(ascending=False)

    fig_target, ax_target = plt.subplots(figsize=(8, 5))
    sns.barplot(x=corrs.index, y=corrs.values, ax=ax_target, palette="viridis", hue=corrs.index, legend=False)
    ax_target.set_xticks(range(len(corrs.index)))
    ax_target.set_xticklabels(corrs.index, rotation=90)
    ax_target.set_ylabel("Correlação")
    ax_target.set_title("Correlação de cada variável com 'polluted'", fontsize=14)
    plt.tight_layout()
    st.pyplot(fig_target)
    plt.close()

    st.subheader("🔍 Principais Insights das Correlações")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**✅ Correlações Fortes Identificadas**")
        st.markdown("""
        - **Forte correlação entre "medida" e "aqi"** de cada poluente: Essa relação é esperada, 
          pois o AQI é um índice derivado diretamente da concentração medida.
        
        - **Poluentes apresentam forte correlação entre si**: As concentrações medidas de poluentes 
          apresentam correlação positiva moderada a alta entre si, especialmente:
          - PM10_medida, PM2_5_medida e NO2_medida
          - CO_medida e NO2_medida
          - PM10_aqi, PM2_5_aqi e NO2_aqi
        
        - Isso sugere que ambientes com alta concentração de um poluente geralmente têm níveis 
          elevados de outros poluentes também.
        """)

    with col2:
        st.markdown("**📊 Variáveis Mais Influentes**")
        st.markdown("""
        A variável **polluted** apresenta maior correlação com:
        - **PM10_medida** (Material Particulado)
        - **PM2_5_medida** (Material Particulado Fino)
        - **NO2_medida** (Dióxido de Nitrogênio)
        - **CO_medida** (Monóxido de Carbono)
        
        Esses são os poluentes mais influentes na determinação de ambientes poluídos, 
        segundo a estrutura do dataset.
        """)

    st.info("""
    **💡 Observação Importante**: Variáveis climáticas como temperatura, umidade, pressão e vento 
    possuem correlação fraca ou neutra com 'polluted', indicando que fatores meteorológicos têm 
    impacto bem menor na classificação de ambientes poluídos.
    """)

    st.header("📝 Conclusões da Análise")

    st.success("""
    **Principais descobertas:**

    1. **PM10 e PM2.5** são os indicadores mais fortes de poluição, com distribuições que mostram 
       claramente ambientes extremamente poluídos.

    2. **NO2 e CO** também são importantes, especialmente em áreas urbanas com tráfego intenso.

    3. Os **índices AQI** são mais adequados para modelagem por serem padronizados e permitirem 
       melhor comparação entre diferentes poluentes.

    4. **Fatores climáticos** têm baixa influência na classificação de poluição, sugerindo que 
       os níveis de poluentes são determinados principalmente por atividades humanas e industriais.

    5. A **multicolinearidade** entre medidas e AQI exige escolha estratégica de features para 
       evitar redundância no modelo.
    """)
