from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"

archivos = [
    "clientes.csv",
    "productos.csv",
    "tiendas.csv",
    "vendedores.csv",
    "ventas.csv",
    "metas.csv",
]

for archivo in archivos:
    ruta = RAW_DIR / archivo
    df = pd.read_csv(ruta, sep=";")

    print("\n==============================")
    print(f"Archivo: {archivo}")
    print("==============================")
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")
    print("\nColumnas:")
    print(list(df.columns))
    print("\nValores nulos:")
    print(df.isnull().sum())