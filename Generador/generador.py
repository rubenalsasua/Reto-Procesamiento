import requests
import random
import time
import json
from multiprocessing import Process
from utils import generar_datos_sinteticos

API_URL = "http://validacion:8000/datos/"  # URL de la API
PROBABILIDAD_ERROR = 0.1  # 10% de probabilidad de error
INTERVALO_ENVIO = 5  # Enviar datos cada 5 segundos


def generador(id_generador):
    """Simula un generador eólico que envía datos a la API cada 5 segundos."""
    while True:
        datos = generar_datos_sinteticos(id_generador, PROBABILIDAD_ERROR)
        print(f"Generador {id_generador} enviando datos: {datos}")  # Agrega esto

        try:
            respuesta = requests.post(API_URL, json=datos)
            print(f"Respuesta del servidor: {respuesta.json()}")
        except Exception as e:
            print(f"Error en el Generador {id_generador}: {e}")

        time.sleep(INTERVALO_ENVIO)


if __name__ == "__main__":
    # Crear 10 procesos para los generadores
    procesos = [Process(target=generador, args=(i,)) for i in range(1, 11)]

    # Iniciar los procesos en paralelo
    for p in procesos:
        p.start()

    # Mantener los procesos corriendo
    for p in procesos:
        p.join()
