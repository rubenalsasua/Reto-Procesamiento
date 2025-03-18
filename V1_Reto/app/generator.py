import requests
import random
import time

URL = "http://localhost:8000/datos/"

def generar_dato(id):
    """Genera datos sintéticos con errores aleatorios"""
    error_probabilidad = 0.2  # 20% de error en los datos

    potencia_kw = round(random.uniform(0, 6000), 2)  # Error si >5000
    viento_mps = round(random.uniform(-5, 35), 2)  # Error si <0 o >30

    if random.random() < error_probabilidad:
        potencia_kw *= 2  # Introduce un error en la potencia

    dato = {"id": id, "potencia_kw": potencia_kw, "viento_mps": viento_mps}
    return dato

# Simulación de los 10 generadores
while True:
    for i in range(10):
        dato = generar_dato(i)
        response = requests.post(URL, json=dato)
        print(f"Generador {i}: {dato} -> {response.status_code}")
    time.sleep(5)
