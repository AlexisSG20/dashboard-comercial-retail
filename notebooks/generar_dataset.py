from pathlib import Path
import csv
import random
from datetime import date, timedelta

random.seed(20)

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

ciudades = ["Huancayo", "Lima", "Arequipa", "Trujillo", "Cusco"]

tiendas = [
    [1, "Tienda Huancayo Centro", "Huancayo", "Junín"],
    [2, "Tienda Lima Norte", "Lima", "Lima"],
    [3, "Tienda Arequipa Mall", "Arequipa", "Arequipa"],
    [4, "Tienda Trujillo Real", "Trujillo", "La Libertad"],
    [5, "Tienda Cusco Plaza", "Cusco", "Cusco"],
]

categorias = {
    "Tecnología": ["Audífonos", "Mouse", "Teclado", "Monitor", "Smartwatch", "Parlante"],
    "Hogar": ["Lámpara", "Organizador", "Silla", "Mesa auxiliar", "Juego de sábanas"],
    "Moda": ["Casaca", "Polo", "Jean", "Zapatillas", "Mochila"],
    "Deportes": ["Pelota", "Mancuernas", "Mat yoga", "Tomatodo", "Bicicleta estática"],
    "Belleza": ["Perfume", "Crema facial", "Shampoo", "Plancha cabello", "Set maquillaje"],
}

nombres = ["Alex", "María", "Luis", "Valeria", "Carlos", "Ana", "Diego", "Lucía", "Jorge", "Camila"]
apellidos = ["Quispe", "Flores", "Rojas", "Torres", "Ramírez", "García", "Mendoza", "Castro"]

vendedores_nombres = ["Rosa", "Miguel", "Andrea", "Fernando", "Patricia", "José", "Gabriela", "Renato"]

def guardar_csv(nombre_archivo, encabezados, filas):
    ruta = RAW_DIR / nombre_archivo
    with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
        writer = csv.writer(archivo, delimiter=";")
        writer.writerow(encabezados)
        writer.writerows(filas)

productos = []
producto_id = 1

for categoria, lista_productos in categorias.items():
    for nombre in lista_productos:
        costo = random.randint(20, 700)
        precio = round(costo * random.uniform(1.25, 1.80), 2)
        productos.append([producto_id, nombre, categoria, costo, precio])
        producto_id += 1

clientes = []
for cliente_id in range(1, 501):
    nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
    ciudad = random.choice(ciudades)
    segmento = random.choice(["Nuevo", "Frecuente", "Premium"])
    clientes.append([cliente_id, nombre, ciudad, segmento])

vendedores = []
for vendedor_id in range(1, 16):
    nombre = f"{random.choice(vendedores_nombres)} {random.choice(apellidos)}"
    tienda_id = ((vendedor_id - 1) % len(tiendas)) + 1
    vendedores.append([vendedor_id, nombre, tienda_id])

ventas = []
fecha_inicio = date(2023, 1, 1)
fecha_fin = date(2025, 12, 31)
dias = (fecha_fin - fecha_inicio).days

for venta_id in range(1, 5001):
    fecha = fecha_inicio + timedelta(days=random.randint(0, dias))
    producto = random.choice(productos)
    cliente = random.choice(clientes)
    tienda = random.choice(tiendas)
    vendedor = random.choice([v for v in vendedores if v[2] == tienda[0]])

    cantidad = random.randint(1, 5)
    precio_unitario = producto[4]
    costo_unitario = producto[3]
    descuento = random.choice([0, 0, 0, 5, 10, 15])

    venta_bruta = cantidad * precio_unitario
    venta_neta = round(venta_bruta * (1 - descuento / 100), 2)
    costo_total = round(cantidad * costo_unitario, 2)
    utilidad = round(venta_neta - costo_total, 2)

    ventas.append([
        venta_id,
        fecha.isoformat(),
        producto[0],
        cliente[0],
        tienda[0],
        vendedor[0],
        cantidad,
        precio_unitario,
        costo_unitario,
        descuento,
        venta_neta,
        costo_total,
        utilidad
    ])

metas = []
meta_id = 1

for anio in [2023, 2024, 2025]:
    for mes in range(1, 13):
        for tienda in tiendas:
            meta_ventas = random.randint(30000, 65000)
            metas.append([meta_id, anio, mes, tienda[0], meta_ventas])
            meta_id += 1

guardar_csv(
    "productos.csv",
    ["producto_id", "producto", "categoria", "costo_unitario", "precio_unitario"],
    productos
)

guardar_csv(
    "clientes.csv",
    ["cliente_id", "cliente", "ciudad", "segmento"],
    clientes
)

guardar_csv(
    "tiendas.csv",
    ["tienda_id", "tienda", "ciudad", "region"],
    tiendas
)

guardar_csv(
    "vendedores.csv",
    ["vendedor_id", "vendedor", "tienda_id"],
    vendedores
)

guardar_csv(
    "ventas.csv",
    [
        "venta_id",
        "fecha",
        "producto_id",
        "cliente_id",
        "tienda_id",
        "vendedor_id",
        "cantidad",
        "precio_unitario",
        "costo_unitario",
        "descuento_porcentaje",
        "venta_neta",
        "costo_total",
        "utilidad"
    ],
    ventas
)

guardar_csv(
    "metas.csv",
    ["meta_id", "anio", "mes", "tienda_id", "meta_ventas"],
    metas
)

print("Dataset generado correctamente en data/raw/")