# Use a imagem oficial do Python
FROM python:3.9

# Configuração do diretório de trabalho
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie todo o código da aplicação para o contêiner
COPY . .

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
