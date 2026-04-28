import pandas as pd #type: ignore
import os


def generar_archivo_csv(lista_ventas, nombre_archivo):
    dataframe_ventas = pd.DataFrame(lista_ventas)
    dataframe_ventas.to_csv(nombre_archivo, index=False)
    print(f"Archivo CSV generado: {nombre_archivo}")