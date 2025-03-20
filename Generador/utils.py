import random
import numpy as np

def generar_datos_sinteticos(id_generador, probabilidad_error=0.1):
    """
    Genera datos de producción de un generador e introduce errores con una probabilidad dada.
    """
    datos = {
        "id_generador": id_generador,
        "potencia_kw": round(np.random.uniform(0, 5000), 2),  # Potencia entre 0 y 5000 kW
        "velocidad_viento": round(np.random.uniform(2, 25), 2),  # Velocidad entre 2 y 25 m/s
        "temperatura": round(np.random.uniform(-10, 50), 2),  # Temperatura entre -10 y 50 °C
        "timestamp": np.datetime64('now').astype(str)  # Timestamp actual
    }

    # Introducir error aleatorio con probabilidad N
    if random.random() < probabilidad_error:
        clave_erronea = random.choice(["potencia_kw", "velocidad_viento", "temperatura"])
        datos[clave_erronea] = "ERROR"  # Insertar un valor inválido

    return datos
