import pandas as pd


def generar_archivo_json(lista_ventas, nombre_archivo):
    dataframe_ventas = pd.DataFrame(lista_ventas)
    dataframe_ventas.to_json(nombre_archivo, orient="records", indent=4)
    print(f"Archivo JSON generado: {nombre_archivo}")