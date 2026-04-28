from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os

app = FastAPI()

FILE_SUCIAS = "data/ventas_sucias.csv"
FILE_LIMPIAS = "data/ventas_limpias.csv"

class VentaRequest(BaseModel):
    producto: str
    talla: str
    cantidad: float
    vendedor: str
    precioUnitario: float
    total: float
    fecha: str

def guardar_csv(datos, ruta):
    df = pd.DataFrame([datos])
    df.to_csv(ruta, mode='a', header=not os.path.exists(ruta), index=False, encoding='utf-8')

@app.post("/analizar-venta")
def analizar(venta: VentaRequest):
    original = venta.model_dump()
    
    # Proceso de Limpieza
    vendedor_L = " ".join(original['vendedor'].split()).title()
    talla_L = str(original['talla']).upper().strip().replace("MEDIO", "M")
    producto_L = original['producto'].strip().capitalize()
    cantidad_L = int(original['cantidad'])
    
    total_esperado = original['precioUnitario'] * cantidad_L
    calculo_ok = abs(original['total'] - total_esperado) < 0.1
    
    venia_sucia = (original['vendedor'] != vendedor_L or 
                original['talla'] != talla_L or 
                original['cantidad'] != cantidad_L or 
                not calculo_ok)

    datos_limpios = {
        "producto": producto_L, "precio_unitario": original['precioUnitario'],
        "talla": talla_L, "cantidad": cantidad_L,
        "vendedor": vendedor_L, "total": original['total'], "fecha": original['fecha']
    }

    if venia_sucia:
        guardar_csv(original, FILE_SUCIAS)
    
    if calculo_ok and cantidad_L > 0:
        guardar_csv(datos_limpios, FILE_LIMPIAS)
        estado = "LIMPIA"
    else:
        estado = "SUCIA"

    return {"estado": estado, **datos_limpios}

if __name__ == "__main__":
    import uvicorn #type: ignore
    uvicorn.run(app, host="127.0.0.1", port=8000)