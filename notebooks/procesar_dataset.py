from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

ventas = pd.read_csv(RAW_DIR / "ventas.csv", sep=";")
productos = pd.read_csv(RAW_DIR / "productos.csv", sep=";")
clientes = pd.read_csv(RAW_DIR / "clientes.csv", sep=";")
tiendas = pd.read_csv(RAW_DIR / "tiendas.csv", sep=";")
vendedores = pd.read_csv(RAW_DIR / "vendedores.csv", sep=";")

ventas_detalle = ventas.merge(productos, on="producto_id", how="left")
ventas_detalle = ventas_detalle.merge(clientes, on="cliente_id", how="left")
ventas_detalle = ventas_detalle.merge(tiendas, on="tienda_id", how="left")
ventas_detalle = ventas_detalle.merge(vendedores, on="vendedor_id", how="left", suffixes=("", "_vendedor"))

ventas_detalle["fecha"] = pd.to_datetime(ventas_detalle["fecha"])
ventas_detalle["anio"] = ventas_detalle["fecha"].dt.year
ventas_detalle["mes"] = ventas_detalle["fecha"].dt.month
ventas_detalle["nombre_mes"] = ventas_detalle["fecha"].dt.month_name()
ventas_detalle["periodo"] = ventas_detalle["fecha"].dt.to_period("M").astype(str)

ventas_detalle = ventas_detalle.rename(columns={
    "ciudad_x": "ciudad_cliente",
    "ciudad_y": "ciudad_tienda"
})

ventas_detalle.to_csv(
    PROCESSED_DIR / "ventas_detalle.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("Archivo procesado creado correctamente:")
print(PROCESSED_DIR / "ventas_detalle.csv")
print(f"Filas: {ventas_detalle.shape[0]}")
print(f"Columnas: {ventas_detalle.shape[1]}")