# Monitor da Qualidade do Ar

Este é um aplicativo Streamlit para monitorar a qualidade do ar, permitindo a entrada manual de dados para classificação e o acompanhamento de um histórico de medições.

## Estrutura do Projeto

-   `app.py`: Página principal da aplicação. Contém informações de boas-vindas e inicializa o estado global da sessão.
-   `pages/`: Diretório que contém as diferentes páginas da aplicação.
    -   `Calcular_Poluicao.py`: Página onde o usuário pode inserir os índices de qualidade do ar (AQI) para prever o nível de poluição e visualizar o histórico de medições.
    -   `Calcular_por_Localizacao.py`: Página reservada para futuras implementações, onde será possível calcular a poluição baseada em uma localização específica.
    -   `Análise_Detalhada.py`: Página com conteúdo estático, que pode ser expandida no futuro para exibir análises mais aprofundadas.
-   `model.pkl`: O modelo de machine learning utilizado para classificar a qualidade do ar.
-   `requirements.txt`: Lista as dependências Python necessárias para rodar o projeto.

## Como Rodar o Projeto

Siga os passos abaixo para configurar e executar a aplicação em sua máquina local:

### 1. Pré-requisitos

Certifique-se de ter o Python 3.8 ou superior instalado.

### 2. Clonar o Repositório (se aplicável)

Se este projeto estiver em um repositório Git, clone-o:

```bash
git clone <url_do_repositorio>
cd air-quality-classifier
```

### 3. Criar e Ativar um Ambiente Virtual

É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No macOS/Linux:
source .venv/bin/activate
```

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas Python necessárias:

```bash
pip install -r requirements.txt
```

### 5. Executar a Aplicação Streamlit

Para iniciar a aplicação, **sempre execute o arquivo principal `Tela_inicial.py`**. Isso garante que o estado da sessão (`st.session_state`) seja inicializado corretamente para todas as páginas.

```bash
streamlit run Tela_inicial.py
```

Após executar o comando, o Streamlit abrirá automaticamente a aplicação em seu navegador padrão. Você poderá navegar entre as diferentes páginas usando o menu lateral.

### 6. Desativar o Ambiente Virtual

Quando terminar de usar a aplicação, você pode desativar o ambiente virtual:

```bash
deactivate
```

# 🌿 Conceitos de Poluição

## 🧪 1. Concentrações Reais de Poluentes (`*_medida`)

As colunas que terminam com **`_medida`** representam a **concentração real** de um poluente na atmosfera, medida por sensores ou estações de monitoramento.

- `pm25_medida` — partículas finas PM2.5  
- `pm10_medida` — partículas maiores PM10  
- `co_medida` — monóxido de carbono  
- `no2_medida` — dióxido de nitrogênio  
- `o3_medida` — ozônio  

Esses valores são geralmente medidos em µg/m³ ou ppm, dependendo do poluente.

---

## 📊 2. AQI – Índice de Qualidade do Ar (`*_aqi`)

As colunas que terminam com **`*_aqi`** representam o **Air Quality Index (AQI)**, um índice padronizado que converte concentrações reais em uma escala comum de risco.

Funções do AQI:
- Facilitar a interpretação sobre a qualidade do ar  
- Indicar riscos à saúde  
- Padronizar diferentes poluentes na mesma escala  

- **0–50:** Qualidade boa  
- **51–100:** Moderada  
- **101+ :** Nociva à saúde  

---

## 🏭 3. Relação entre Concentração Real e AQI

O código compara graficamente:
- `*_medida` → concentração real  
- `*_aqi` → impacto padronizado na saúde  

Isso permite observar:
- A força da relação entre concentração e risco  
- Se o aumento na concentração aumenta o AQI proporcionalmente  
- Quais poluentes causam mais impacto mesmo em baixas quantidades  

---

## 🔥 4. Correlação entre Poluentes e a Poluição Geral

Medido o quanto cada poluente contribui para a variável final `polluted` (indicador de poluição).

Isso permite responder:
- Quais poluentes têm maior impacto na poluição geral  
- Se há poluentes que normalmente aparecem juntos  
- Como diferentes medidas se relacionam entre si  

---

## 🌬 5. Poluentes Trabalhados

Os dados incluem diferentes poluentes atmosféricos, cada um com características próprias.

### **PM2.5 e PM10 (Material Particulado)**
- Mistura de partículas sólidas e líquidas suspensas no ar  
- PM2.5: partículas finas que penetram profundamente nos pulmões  
- Fortemente associadas a doenças cardiovasculares e respiratórias  

### **NO₂ (Dióxido de Nitrogênio)**
- Principalmente emitido por veículos e indústrias  
- Irritante para o sistema respiratório  

### **O₃ (Ozônio Troposférico)**
- Formado por reações químicas entre outros poluentes  
- Pode piorar doenças respiratórias  

### **CO (Monóxido de Carbono)**
- Resultado da combustão incompleta de combustíveis  
- Altamente tóxico em concentrações elevadas  

---

## 🧭 6. Variável-Alvo: `polluted`

O conjunto possui a coluna **`polluted`**, que indica se a qualidade do ar está:

- **1:** Poluída  
- **0:** Não poluída  

Ela ajuda a identificar quais poluentes são determinantes no estado final de poluição.

---

## 📈 7. Conceito de Correlação Aplicado à Poluição

- Como os poluentes se relacionam entre si  
- Quais deles têm maior influência sobre a poluição  
- Estruturas de dependência entre variáveis ambientais  

---

## 🧭 Resumo

- Medir poluentes  
- Padronizar impacto via AQI  
- Explorar o comportamento dos poluentes  
- Entender como eles se relacionam com a poluição geral  

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

---

Espero que este README ajude a esclarecer como rodar o projeto e entender sua estrutura.
