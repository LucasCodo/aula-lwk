FROM python:3.11
LABEL authors="luss1"

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

CMD ["maturin", "develop"]
# Comando para rodar o script Python
CMD ["python", "main.py"]
