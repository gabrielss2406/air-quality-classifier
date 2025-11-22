FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
CMD ["streamlit", "run", "Tela_Inicial.py"]
