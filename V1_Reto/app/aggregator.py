import statistics
from typing import List
from models import GeneradorDatos, AgregadosResponse

def calcular_agregados(datos: List[GeneradorDatos]) -> AgregadosResponse:
    """
    Calcula estadísticas de producción del parque eólico.

    Args:
        datos (List[GeneradorDatos]): Lista de datos recibidos de los generadores.

    Returns:
        AgregadosResponse: Resumen con promedio, máximo y mínimo de producción.
    """
    if not datos:
        return AgregadosResponse(promedio_kw=0, maximo_kw=0, minimo_kw=0)

    potencias = [d.potencia_kw for d in datos]

    return AgregadosResponse(
        promedio_kw=statistics.mean(potencias),
        maximo_kw=max(potencias),
        minimo_kw=min(potencias),
    )
