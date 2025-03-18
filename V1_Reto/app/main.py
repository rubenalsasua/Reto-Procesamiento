from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import random
import statistics

app = FastAPI()

# Modelo de datos de un generador eólico
class GeneradorDatos(BaseModel):
    id: int
    potencia_kw: float = Field(..., gt=0, lt=5000)  # Potencia entre 0 y 5000 kW
    viento_mps: float = Field(..., gt=0, lt=30)  # Viento entre 0 y 30 m/s

# Base de datos temporal en memoria
datos_generadores = []

@app.post("/datos/")
def recibir_datos(datos: GeneradorDatos):
    """Recibe y almacena datos de un generador eólico"""
    datos_generadores.append(datos)
    return {"message": "Datos recibidos correctamente"}

@app.get("/agregados/")
def obtener_agregados():
    """Calcula estadísticas básicas de producción"""
    if not datos_generadores:
        raise HTTPException(status_code=400, detail="No hay datos registrados")
    
    potencias = [d.potencia_kw for d in datos_generadores]
    return {
        "promedio_kw": statistics.mean(potencias),
        "maximo_kw": max(potencias),
        "minimo_kw": min(potencias),
    }
