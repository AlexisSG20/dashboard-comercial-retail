USE dashboard_comercial_retail;
GO

CREATE TABLE productos (
    producto_id INT PRIMARY KEY,
    producto VARCHAR(100),
    categoria VARCHAR(50),
    costo_unitario DECIMAL(10,2),
    precio_unitario DECIMAL(10,2)
);

CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY,
    cliente VARCHAR(100),
    ciudad VARCHAR(50),
    segmento VARCHAR(30)
);

CREATE TABLE tiendas (
    tienda_id INT PRIMARY KEY,
    tienda VARCHAR(100),
    ciudad VARCHAR(50),
    region VARCHAR(50)
);

CREATE TABLE vendedores (
    vendedor_id INT PRIMARY KEY,
    vendedor VARCHAR(100),
    tienda_id INT
);

CREATE TABLE ventas (
    venta_id INT PRIMARY KEY,
    fecha DATE,
    producto_id INT,
    cliente_id INT,
    tienda_id INT,
    vendedor_id INT,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    costo_unitario DECIMAL(10,2),
    descuento_porcentaje INT,
    venta_neta DECIMAL(10,2),
    costo_total DECIMAL(10,2),
    utilidad DECIMAL(10,2)
);

CREATE TABLE metas (
    meta_id INT PRIMARY KEY,
    anio INT,
    mes INT,
    tienda_id INT,
    meta_ventas DECIMAL(10,2)
);

CREATE TABLE dim_fecha (
    fecha DATE PRIMARY KEY,
    anio INT,
    mes INT,
    nombre_mes VARCHAR(20),
    trimestre INT,
    dia INT,
    dia_semana VARCHAR(20),
    periodo VARCHAR(7)
);