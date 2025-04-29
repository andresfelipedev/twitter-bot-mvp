# Utilizar una imagen oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar todos los archivos del proyecto al contenedor
COPY . .

# Establecer PYTHONPATH para que reconozca correctamente la carpeta /app
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para correr la aplicación
CMD ["python", "scripts/run_bot.py"]
