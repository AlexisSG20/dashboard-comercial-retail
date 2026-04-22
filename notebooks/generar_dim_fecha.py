from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

ventas_detalle = pd.read_csv(PROCESSED_DIR / "ventas_detalle.csv", sep=";")
ventas_detalle["fecha"] = pd.to_datetime(ventas_detalle["fecha"])

fecha_min = ventas_detalle["fecha"].min()
fecha_max = ventas_detalle["fecha"].max()

dim_fecha = pd.DataFrame({
    "fecha": pd.date_range(start=fecha_min, end=fecha_max, freq="D")
})

dim_fecha["anio"] = dim_fecha["fecha"].dt.year
dim_fecha["mes"] = dim_fecha["fecha"].dt.month
dim_fecha["nombre_mes"] = dim_fecha["fecha"].dt.month_name()
dim_fecha["trimestre"] = dim_fecha["fecha"].dt.quarter
dim_fecha["dia"] = dim_fecha["fecha"].dt.day
dim_fecha["dia_semana"] = dim_fecha["fecha"].dt.day_name()
dim_fecha["periodo"] = dim_fecha["fecha"].dt.to_period("M").astype(str)

dim_fecha.to_csv(
    PROCESSED_DIR / "dim_fecha.csv",
    sep=";",
    index=False,
    encoding="utf-8-sig"
)

print("Archivo creado correctamente:")
print(PROCESSED_DIR / "dim_fecha.csv")
print(f"Filas: {dim_fecha.shape[0]}")
print(f"Columnas: {dim_fecha.shape[1]}")