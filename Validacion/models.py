from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Union


class DatosGenerador(BaseModel):
    id_generador: int = Field(..., example=1)
    potencia_kw: Union[float, str] = Field(..., example=3000.5)
    velocidad_viento: Union[float, str] = Field(..., example=12.5)
    temperatura: Union[float, str] = Field(..., example=25.2)
    timestamp: str = Field(..., example="2024-03-17T12:00:00Z")

    @field_validator("potencia_kw")
    @classmethod
    def validar_potencia(cls, v):
        if isinstance(v, (int, float)):  # Verifica si es un número
            if v >= 4000:
                raise ValueError("La potencia debe ser menor que 4000 kW")
        return v
