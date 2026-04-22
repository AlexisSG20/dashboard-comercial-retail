USE dashboard_comercial_retail;
GO

-- 1. KPIs generales del negocio
SELECT
    SUM(venta_neta) AS ventas_totales,
    SUM(utilidad) AS utilidad_total,
    ROUND(SUM(utilidad) / NULLIF(SUM(venta_neta), 0) * 100, 2) AS margen_utilidad_porcentaje,
    COUNT(DISTINCT venta_id) AS cantidad_ordenes,
    ROUND(SUM(venta_neta) / NULLIF(COUNT(DISTINCT venta_id), 0), 2) AS ticket_promedio
FROM ventas;


-- 2. Ventas y utilidad por mes
SELECT
    YEAR(fecha) AS anio,
    MONTH(fecha) AS mes,
    SUM(venta_neta) AS ventas_totales,
    SUM(utilidad) AS utilidad_total
FROM ventas
GROUP BY YEAR(fecha), MONTH(fecha)
ORDER BY anio, mes;

-- 3. Ventas y utilidad por tienda
SELECT
    t.tienda,
    t.ciudad,
    SUM(v.venta_neta) AS ventas_totales,
    SUM(v.utilidad) AS utilidad_total,
    COUNT(DISTINCT v.venta_id) AS cantidad_ordenes
FROM ventas v
INNER JOIN tiendas t
    ON v.tienda_id = t.tienda_id
GROUP BY t.tienda, t.ciudad
ORDER BY ventas_totales DESC;

-- 4. Ventas y utilidad por categoría
SELECT
    p.categoria,
    SUM(v.venta_neta) AS ventas_totales,
    SUM(v.utilidad) AS utilidad_total,
    ROUND(SUM(v.utilidad) / NULLIF(SUM(v.venta_neta), 0) * 100, 2) AS margen_utilidad_porcentaje,
    SUM(v.cantidad) AS unidades_vendidas
FROM ventas v
INNER JOIN productos p
    ON v.producto_id = p.producto_id
GROUP BY p.categoria
ORDER BY utilidad_total DESC;

-- 5. Top 10 productos por ventas
SELECT TOP 10
    p.producto,
    p.categoria,
    SUM(v.venta_neta) AS ventas_totales,
    SUM(v.utilidad) AS utilidad_total,
    SUM(v.cantidad) AS unidades_vendidas
FROM ventas v
INNER JOIN productos p
    ON v.producto_id = p.producto_id
GROUP BY p.producto, p.categoria
ORDER BY ventas_totales DESC;

-- 6. Cumplimiento de metas por tienda y mes
SELECT
    YEAR(v.fecha) AS anio,
    MONTH(v.fecha) AS mes,
    t.tienda,
    SUM(v.venta_neta) AS ventas_reales,
    m.meta_ventas,
    ROUND(SUM(v.venta_neta) / NULLIF(m.meta_ventas, 0) * 100, 2) AS cumplimiento_porcentaje
FROM ventas v
INNER JOIN tiendas t
    ON v.tienda_id = t.tienda_id
INNER JOIN metas m
    ON m.tienda_id = v.tienda_id
    AND m.anio = YEAR(v.fecha)
    AND m.mes = MONTH(v.fecha)
GROUP BY
    YEAR(v.fecha),
    MONTH(v.fecha),
    t.tienda,
    m.meta_ventas
ORDER BY anio, mes, tienda;

-- 7. Validación de registros cargados
SELECT 'clientes' AS tabla, COUNT(*) AS registros FROM clientes
UNION ALL
SELECT 'productos', COUNT(*) FROM productos
UNION ALL
SELECT 'tiendas', COUNT(*) FROM tiendas
UNION ALL
SELECT 'vendedores', COUNT(*) FROM vendedores
UNION ALL
SELECT 'ventas', COUNT(*) FROM ventas
UNION ALL
SELECT 'metas', COUNT(*) FROM metas
UNION ALL
SELECT 'dim_fecha', COUNT(*) FROM dim_fecha;