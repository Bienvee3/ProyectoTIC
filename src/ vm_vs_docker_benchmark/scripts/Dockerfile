FROM python:3.10-slim

RUN apt update && apt install -y curl procps

WORKDIR /app

# Copiar requirements.txt (está en ../requirements.txt desde scripts/)
COPY ../requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar todo el contenido de web_snake_game dentro de /app/web_snake_game
COPY web_snake_game /app/web_snake_game

WORKDIR /app/web_snake_game

EXPOSE 5000

CMD ["python3", "run_snake_server.py"]
