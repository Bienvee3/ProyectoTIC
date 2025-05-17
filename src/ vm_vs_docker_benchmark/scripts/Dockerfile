FROM python:3.10-slim

RUN apt update && apt install -y curl procps && \
    pip install --upgrade pip && \
    pip install flask requests psutil \
    pip install -r requirements.txt

WORKDIR /app
COPY scripts /app/scripts
WORKDIR /app/scripts

EXPOSE 5000

CMD ["python3", "scripts/web_snake_game/run_snake_server.py"]
