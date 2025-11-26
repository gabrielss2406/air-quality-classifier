import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Análise Detalhada", page_icon="📊")

st.title("📊 Análise Detalhada dos dados")

st.info("O objetivo central desse trabalho é a detecção e análise de ambientes poluídos. O conteúdo está estruturado em seções que incluem contextualização do problema, " \
"preparação dos dados, exploração inicial, modelagem e avaliação. A seguir, apresenta-se uma análise detalhada dos dados utilizados.")

st.write(
    """
    Utilizamos pandas e numpy para manipulação de dados, matplotlib e seaborn para visualização, scikit-learn para modelagem (com forte presença de Pipeline, StandardScaler, 
    RandomForestClassifier e métricas), entre outros elementos utilizados para pré-processamento e avaliação.
    """
)

st.info("Primeiro é feito o carregamento dos dados, foram importados dados em 22 colunas: city, timestamp, temperature, wind, humidity, dew_point, pressure	uv_index, O3_aqi, CO_medida, NO2_aqi, NO2_medida, PM10_aqi, PM10_medida, PM2_5_aqi, PM2_5_medida, SO2_aqi, SO2_medida e polluted")

st.write(
    """
   Os componentes de poluição são:
    - O3: Ozônio
    - CO: Monóxido de Carbono
    - NO2: Dióxido de Nitrogênio
    - PM10: Material Particulado
    - PM2.5: Material Particulado Fino
    - SO2: Dióxido de Enxofre
    """
)

st.write(
    """Analisando a estrutura dos dados, temos a cidade onde os sensores estão situados, a data da medida e diversas metricas da condição do meio ambiente. Podemos ver que todas as metricas sobre concentração de algum elemento tem uma coluna aqi e outra medida. Buscando entender um pouco melhor, e para esclarecer a diferença:
- **Medida**: Valor medido bruto, ou seja, o dado obtido direto do sensor.
- **AQI**: Dado padronizado dentro de intervalos, que mostram o nivel de poluição que isso pode trazer, como dois elementos possuem medidas diferentes, são colocados nessa forma para trazer uma melhor comparação e relação entre eles."""
)

st.info("Não foi necessário realizar tratamento de dados faltantes, pois o dataset apresentava dados completos.")

st.info("Então realizamos a EDA para entender e visualizar os dados antes de treinar modelos.")

st.write(
    """ Foram feitos gráficos para comparar o valor medido e AQI de cada poluente, obtendo os seguintes gráficos:"""
)

col1, col2 = st.columns(2)
with col1:
    st.image("images/o3_aqi_vs_medida.png", caption="Distribuição do O3", width=550)
with col2:
    st.image("images/co_aqi_vs_medido.png", caption="Distribuição do CO", width=550)

col3, col4 = st.columns(2)
with col3:
    st.image("images/no2_aqi_vs_medido.png", caption="Distribuição do NO2", width=550)
with col4:
    st.image("images/pm10_aqi_vs_medido.png", caption="Distribuição do PM10", width=550)

col5, col6 = st.columns(2)
with col5:
    st.image("images/pm2_aqi_vs_medido.png", caption="Distribuição do PM2", width=550)
with col6:
    st.image("images/so2_aqi_vs_medido.png", caption="Distribuição do SO2", width=550)

st.info(" As colunas AQI possuem os dados mais padronizados e normalizado, mas observando os gráficos, surge a reflexão, qual das duas métricas (AQI ou medida) é mais relevante para a análise de poluição?")

st.write(
    """ Então plotamos gráficos para as análises dos valores e definir qual o melhor para o estudo:"""
)

st.image("images/distribuicao_vars.png", caption="Distribuição das variáveis")

col1, col2 = st.columns(2)
with col1:
    st.image("images/boxplot_o3_aqi.png", width=550)
with col2:
    st.image("images/boxplot_o3.png",  width=550)

col3, col4 = st.columns(2)
with col3:
    st.image("images/boxplot_co_aqi.png",  width=550)
with col4:
    st.image("images/boxplot_co_medida.png", width=550)

col5, col6 = st.columns(2)
with col5:
    st.image("images/boxplot_no2_aqi.png", width=550)
with col6:
    st.image("images/boxplot_no2_medida.png", width=550)

col7, col8 = st.columns(2)
with col7:
    st.image("images/boxplot_pm10_aqi.png", width=550)
with col8:
    st.image("images/boxplot_pm10_medida.png", width=550)

col9, col10 = st.columns(2)
with col9:
    st.image("images/boxplot_pm2_aqi.png",  width=550)
with col10:
    st.image("images/boxplot_pm2_medida.png",  width=550)

col11, col12 = st.columns(2)
with col11:
    st.image("images/boxplot_so2_aqi.png", width=550)
with col12:
    st.image("images/boxplot_so2_medida.png", width=550)

st.info("Pudemos observar:")

st.write(
    """- **O3_medida / O3_aqi**
    + Distribuição levemente assimétrica.
    + Grande concentração entre 20–60.
    + Cauda curta de valores mais altos.
    +  *Interpretação*: O ozônio costuma ter picos ocasionais, mas de forma geral é relativamente estável. Pode ser um indicativo moderado de poluição.

- **CO_medida / CO_aqi**
    + Extremamente assimétricos.
    + Muitos valores próximos de zero.
    + Cauda longa atingindo valores bem altos.
    + *Interpretação*: CO é claramente uma variável com muitos valores muito baixos e alguns picos isolados (talvez áreas industriais, tráfego intenso, ou falhas pontuais de medição).

- **NO2_medida / NO2_aqi**
    + Muito concentrado perto de zero.
    + Poucos valores mais altos (>60).
    + *Interpretação*: NO₂ está fortemente associado a poluição por tráfego e combustão. Mesmo com baixa ocorrência de picos, os valores altos podem discriminar bem locais poluídos.

- **PM10_medida / PM10_aqi**
    + Assimetria muito forte.
    + Grande concentração perto de zero.
    + Cauda longa.
    + *Interpretação*: PM10 é uma das métricas mais importantes para classificar poluição e aqui ela parece ter vários valores extremos. É uma variável com comportamento ideal para ser usada como feature principal no modelo.

- **PM2_5_medida / PM2_5_aqi**
    + Distribuição semelhante ao PM10, mas menos extrema.
    + Valores médios variam entre 10–50 com cauda até >100.
    + *Interpretação*: PM2.5 é extremamente correlacionado com riscos para saúde e é um excelente indicador de poluição. Precisará de transformação por causa da cauda longa.

- **SO2_medida / SO2_aqi**
    + Muito concentrado abaixo de 5.
    + Pouquíssimos valores altos.
    + *Interpretação*: SO₂ costuma ser baixo em muitos lugares e só sobe em regiões industriais ou queima de carvão. Pode ajudar a identificar locais específicos fortemente poluídos, mas não será tão útil para generalização.
"""
)

st.info("Plotando um gráfico com a relação das variáveis e a poluição:")

st.image("images/relacao_com_poluted.png", width=700)

st.info("Mostrando a nossa matriz de correlação:")

st.image("images/matriz_correlacao.png", width=1000)

st.info("Conclusão final:")

st.write(
    """ - *Forte correlação entre “medida” e “aqi” de cada poluente*: Essa relação é esperada, pois o AQI é um índice derivado diretamente da concentração medida.
Isso reforça que usar ao mesmo tempo medidas e AQI no modelo introduziria multicolinearidade.

- *Poluentes apresentam forte correlação entre si*: As concentrações medidas de poluentes apresentam correlação positiva moderada a alta entre si, especialmente ->
(PM10_medida, PM2_5_medida e NO2_medida)
(CO_medida e NO2_medida)
(PM10_aqi, PM2_5_aqi e NO2_aqi)
Isso sugere que ambientes com alta concentração de um poluente geralmente têm níveis elevados de outros poluentes também.

- *Correlação dos poluentes com a variável-alvo polluted* A variável polluted apresenta maior correlação com:
    + PM10_medida
    + PM2_5_medida
    + NO2_medida
    + CO_medida

    Esses são os poluentes mais influentes na determinação de ambientes poluídos, segundo a estrutura do dataset.
    Eles tendem a subir juntos quando o ambiente encontra-se em condição considerada poluída.

    Por outro lado, variáveis climáticas como temperatura, umidade, pressão e vento possuem correlação fraca ou neutra com polluted, indicando que fatores meteorológicos têm impacto bem menor no rótulo final.

- *Variáveis climáticas possuem pouca influência*: Temperatura, vento, umidade e ponto de orvalho apresentam correlações baixas com os níveis de poluição. Isso mostra que, no dataset, as condições meteorológicas não são determinantes diretas na classificação do ambiente como poluído ou não."""
)