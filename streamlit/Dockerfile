# Use a imagem oficial do Python como base
FROM python:3.8-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do aplicativo para o diretório de trabalho
COPY . .

# Exponha a porta em que o Streamlit estará em execução
EXPOSE 8501

# Comando para iniciar o aplicativo Streamlit
CMD ["streamlit", "run", "app.py"]
