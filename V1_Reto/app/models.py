from pydantic import BaseModel, Field
from typing import List

class GeneradorDatos(BaseModel):
    """Modelo Pydantic para validar los datos de un generador eólico"""
    id: int = Field(..., ge=0)  # ID del generador (≥ 0)
    potencia_kw: float = Field(..., gt=0, lt=5000, description="Potencia en kW entre 0 y 5000")
    viento_mps: float = Field(..., gt=0, lt=30, description="Velocidad del viento en m/s entre 0 y 30")

class AgregadosResponse(BaseModel):
    """Modelo de respuesta para las estadísticas del parque eólico"""
    promedio_kw: float
    maximo_kw: float
    minimo_kw: float
