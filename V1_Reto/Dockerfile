# Usar imagen de Python
FROM python:3.10

# Definir directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando para iniciar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
