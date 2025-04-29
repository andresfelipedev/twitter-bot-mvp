# Utilizar una imagen oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos al contenedor
COPY . .

# Establecer PYTHONPATH para que reconozca los módulos
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para correr la app
CMD ["python", "scripts/run_bot.py"]
