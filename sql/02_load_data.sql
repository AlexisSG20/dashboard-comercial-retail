USE dashboard_comercial_retail;
GO

-- Ajusta las rutas de los archivos CSV según tu entorno local antes de ejecutar este script.
-- Ejemplo:
-- RUTA_LOCAL\dashboard-comercial-retail\data\raw\productos.csv

BULK INSERT productos
FROM 'RUTA_LOCAL\\dashboard-comercial-retail\\data\\raw\\productos.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);

BULK INSERT clientes
FROM 'RUTA_LOCAL\\dashboard-comercial-retail\\data\\raw\\clientes.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);

BULK INSERT tiendas
FROM 'RUTA_LOCAL\\dashboard-comercial-retail\\data\\raw\\tiendas.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);

BULK INSERT vendedores
FROM 'RUTA_LOCAL\\dashboard-comercial-retail\\data\\raw\\vendedores.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);

BULK INSERT ventas
FROM 'RUTA_LOCAL\\dashboard-comercial-retail\\data\\raw\\ventas.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);

BULK INSERT metas
FROM 'RUTA_LOCAL\\dashboard-comercial-retail\\data\\raw\\metas.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);

BULK INSERT dim_fecha
FROM 'RUTA_LOCAL\\dashboard-comercial-retail\\data\\processed\\dim_fecha.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ';',
    ROWTERMINATOR = '0x0a',
    CODEPAGE = '65001',
    TABLOCK
);