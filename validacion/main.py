from fastapi import FastAPI, HTTPException
from models import DatosGenerador
from database import coleccion_datos

app = FastAPI()

@app.post("/datos/")
async def recibir_datos(datos: DatosGenerador):
    # Validar que los datos no contengan errores
    for campo, valor in datos.dict().items():
        if valor == "ERROR":
            return {"mensaje": "Datos con error", "status": "rechazado"}

    # Guardar datos en MongoDB
    coleccion_datos.insert_one(datos.dict())

    return {"mensaje": "Datos recibidos correctamente", "status": "aceptado"}

@app.get("/datos/")
async def obtener_datos():
    """Devuelve todos los datos almacenados en la base de datos."""
    datos = list(coleccion_datos.find({}, {"_id": 0}))  # No mostrar el campo _id
    return {"datos": datos}


@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}

@app.get("/media_produccion/")
async def media_produccion():
    """Calcula la media de potencia_kw de todos los generadores."""
    resultado = coleccion_datos.aggregate([
        {"$group": {"_id": None, "media_potencia": {"$avg": "$potencia_kw"}}}
    ])
    
    resultado = list(resultado)
    
    if resultado:
        return {"media_potencia_kw": resultado[0]["media_potencia"]}
    else:
        return {"mensaje": "No hay datos disponibles"}

