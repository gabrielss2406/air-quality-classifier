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

## Contribuição

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

---

Espero que este README ajude a esclarecer como rodar o projeto e entender sua estrutura.
