# Usar imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de requisitos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Crear directorio para la base de datos SQLite
RUN mkdir -p /app/data

# Exponer el puerto 7700
EXPOSE 7700

# Variable de entorno para la API key de Google (debe configurarse al ejecutar el contenedor)
ENV GOOGLE_API_KEY=""

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7700"]
