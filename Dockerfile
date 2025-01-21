# Use uma imagem base Python
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt /app/requirements.txt
COPY src /app/src
COPY modelos_deploy_src /app/modelos_deploy_src

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exposição da porta do Flask
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "src/app.py"]
