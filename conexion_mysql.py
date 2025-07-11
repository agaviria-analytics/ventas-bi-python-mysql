import mysql.connector
import pandas as pd

#conexion a la bd mysql
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ventas_bi"
)

query = """
SELECT
    v.id_venta,
    v.fecha,
    c.nombre_cliente,
    c.zona,
    p.nombre_producto,
    p.categoria,
    v.cantidad,
    v.precio_unitario,
    v.costo_unitario
FROM ventas v
JOIN clientes c ON v.id_cliente = c.id_cliente
JOIN productos p ON v.id_producto = p.id_producto
WHERE v.fecha BETWEEN '2023-01-01' AND '2024-12-31'
ORDER BY v.id_venta;
"""
df=pd.read_sql(query,conexion)
conexion.close()

df.to_excel("ventas_combinadas.xlsx",index=False)
print("Archivo excel generado:ventas_combinadas.xlsx")
print(df)