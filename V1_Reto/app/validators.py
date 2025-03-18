import pandas as pd
from pydantic import ValidationError
from models import GeneradorDatos  # Importamos el modelo Pydantic

# Cargar CSV
df = pd.read_csv("data/datos.csv")

# Validar cada fila
for _, row in df.iterrows():
    try:
        GeneradorDatos(**row.to_dict())
        print(f"✅ Válido: {row.to_dict()}")
    except ValidationError as e:
        print(f"❌ Error en {row.to_dict()}: {e}")
