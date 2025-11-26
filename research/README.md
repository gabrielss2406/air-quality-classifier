#  Conceitos de Poluição

##  1. Concentrações Reais de Poluentes (`*_medida`)

As colunas que terminam com **`_medida`** representam a **concentração real** de um poluente na atmosfera, medida por sensores ou estações de monitoramento.

- `pm25_medida` — partículas finas PM2.5  
- `pm10_medida` — partículas maiores PM10  
- `co_medida` — monóxido de carbono  
- `no2_medida` — dióxido de nitrogênio  
- `o3_medida` — ozônio  

Esses valores são geralmente medidos em µg/m³ ou ppm, dependendo do poluente.

---

##  2. AQI – Índice de Qualidade do Ar (`*_aqi`)

As colunas que terminam com **`*_aqi`** representam o **Air Quality Index (AQI)**, um índice padronizado que converte concentrações reais em uma escala comum de risco.

Funções do AQI:
- Facilitar a interpretação sobre a qualidade do ar  
- Indicar riscos à saúde  
- Padronizar diferentes poluentes na mesma escala  

- **0–50:** Qualidade boa  
- **51–100:** Moderada  
- **101+ :** Nociva à saúde  

---

##  3. Relação entre Concentração Real e AQI

O código compara graficamente:
- `*_medida` → concentração real  
- `*_aqi` → impacto padronizado na saúde  

Isso permite observar:
- A força da relação entre concentração e risco  
- Se o aumento na concentração aumenta o AQI proporcionalmente  
- Quais poluentes causam mais impacto mesmo em baixas quantidades  

---

##  4. Correlação entre Poluentes e a Poluição Geral

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

##  6. Variável-Alvo: `polluted`

O conjunto possui a coluna **`polluted`**, que indica se a qualidade do ar está:

- **1:** Poluída  
- **0:** Não poluída  

Ela ajuda a identificar quais poluentes são determinantes no estado final de poluição.

---

##  7. Conceito de Correlação Aplicado à Poluição

- Como os poluentes se relacionam entre si  
- Quais deles têm maior influência sobre a poluição  
- Estruturas de dependência entre variáveis ambientais  

---

##  Resumo

- Medir poluentes  
- Padronizar impacto via AQI  
- Explorar o comportamento dos poluentes  
- Entender como eles se relacionam com a poluição geral  