from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:admin@mongodb:27017")

client = MongoClient(MONGO_URI)
db = client["parque_eolico"]  # Base de datos
coleccion_datos = db["datos_generadores"]  # Colección donde guardamos datos
