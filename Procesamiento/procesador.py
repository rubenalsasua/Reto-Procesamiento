import time
import pandas as pd
from database import coleccion_datos, coleccion_aggregados

def calcular_agregados():
    """Lee los datos desde MongoDB, calcula agregaciones y los guarda."""
    
    # Leer todos los datos de MongoDB
    datos = list(coleccion_datos.find({}, {"_id": 0}))

    if not datos:
        print("No hay datos para procesar.")
        return

    # Convertir a DataFrame
    df = pd.DataFrame(datos)

    # Convertir timestamp a formato datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Agrupar por minuto y calcular promedios
    agregados = df.resample("1T", on="timestamp").mean()

    # Convertir a diccionarios para MongoDB
    registros_aggregados = agregados.reset_index().to_dict(orient="records")

    # Guardar en MongoDB
    if registros_aggregados:
        coleccion_aggregados.insert_many(registros_aggregados)
        print(f"Guardados {len(registros_aggregados)} registros agregados en MongoDB.")

# Ejecutar cada 60 segundos
while True:
    calcular_agregados()
    time.sleep(60)
