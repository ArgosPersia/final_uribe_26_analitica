from data.simuladorEmpleados import crear_empleados
from data.simuladorVentas import generar_ventas
from utils.generarCSV import generar_archivo_csv
from utils.generarJSON import generar_archivo_json
from utils.limpiarDatos import limpiar_dataframe
import pandas as pd


empleados = crear_empleados(10)
ventas = generar_ventas(50, empleados)

print("\nVENTAS ")
for venta in ventas:
    print(f"Fecha: {venta['fecha']} | Vendedor: {venta['vendedor']} | Producto: {venta['producto']} | Cantidad: {venta['cantidad']}")

dataframe_ventas = pd.DataFrame(ventas)

generar_archivo_csv(ventas, "data/ventas_sucias.csv")
generar_archivo_json(ventas, "data/json_ventas_sucias.json")


# print(dataframe_ventas.head(7))
# print(dataframe_ventas.tail())
# print(dataframe_ventas.shape)
# print(dataframe_ventas.columns)
# print(dataframe_ventas.dtypes)
# print(dataframe_ventas.info())
# print(dataframe_ventas.describe())

df_limpio = limpiar_dataframe(
    df=dataframe_ventas,
    columnas_texto=["producto", "talla", "vendedor"],
    columnas_obligatorias=["producto", "precio_unitario", "cantidad", "total"],
)

generar_archivo_csv(df_limpio.to_dict("records"), "data/ventas_limpias.csv")
generar_archivo_json(df_limpio.to_dict("records"), "data/json_ventas_limpias.json")
