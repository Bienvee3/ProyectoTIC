FROM python:3.10-slim

# Instala utilidades y dependencias
RUN apt update && apt install -y curl procps

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el resto del código
COPY scripts /app/scripts

# Establece el nuevo directorio de trabajo
WORKDIR /app/scripts

# Expone el puerto para Flask
EXPOSE 5000

# Comando por defecto
CMD ["python3", "scripts/web_snake_game/run_snake_server.py"]
