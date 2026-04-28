import pandas as pd #type: ignore


def limpiar_dataframe(df, columnas_texto, columnas_obligatorias):

    dataFrameCopia = df.copy()

    #  B. Textos
    for columna in columnas_texto:
        dataFrameCopia[columna] = dataFrameCopia[columna].astype(str).str.strip()

    dataFrameCopia["producto"] = dataFrameCopia["producto"].str.title()
    dataFrameCopia["vendedor"] = dataFrameCopia["vendedor"].str.title()
    dataFrameCopia["talla"]    = dataFrameCopia["talla"].str.upper()
    
    tallas_validas = {"XS", "S", "M", "L", "XL", "XXL"}
    dataFrameCopia = dataFrameCopia[dataFrameCopia["talla"].isin(tallas_validas)]    
    # C. Nulos
    dataFrameCopia.replace(["", "none", "nan", "-"], pd.NA, inplace=True)

    #  E. Tipos de datos
    dataFrameCopia["precio_unitario"] = pd.to_numeric(dataFrameCopia["precio_unitario"], errors="coerce").astype("Int64")
    dataFrameCopia["cantidad"]        = pd.to_numeric(dataFrameCopia["cantidad"],        errors="coerce").astype("Int64")
    dataFrameCopia["total"]           = pd.to_numeric(dataFrameCopia["total"],           errors="coerce")
    dataFrameCopia["fecha"]           = pd.to_datetime(dataFrameCopia["fecha"],          errors="coerce", dayfirst=True)

    # D. Duplicados 
    dataFrameCopia = dataFrameCopia.drop_duplicates()

    # F. Reglas de negocio
    dataFrameCopia = dataFrameCopia.dropna(subset=columnas_obligatorias)

    dataFrameCopia = dataFrameCopia[dataFrameCopia["cantidad"] > 0]

    dataFrameCopia = dataFrameCopia[
    dataFrameCopia["total"] == dataFrameCopia["precio_unitario"] * dataFrameCopia["cantidad"]
    ]

    return dataFrameCopia