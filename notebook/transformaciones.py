import pandas as pd #type: ignore
import random
from data.simuladorVentas import generar_ventas

# Generar empleados aleatorios
nombres = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martínez", "Luis Rodriguez"]
lista_empleados = [{"nombres_apellidos": random.choice(nombres)} for _ in range(10)]

datos = generar_ventas(50, lista_empleados)
datosOrdenados = pd.DataFrame(datos)

# Query 1
resultado = datosOrdenados.query("total > 500000")
print("Ventas > 500k")
print(resultado) 

# Query 2
ventas_300_tallaM = datosOrdenados.query("total > 300000 and talla == 'M'")
print("Ventas > 300k y talla M")
print(ventas_300_tallaM)

#queries con valores especificos de una columna
#me gustaria ver las ventas de dos empleados especificos, Maria garcia o de Juan Perez
ventas_vendedores = datosOrdenados.query("vendedor == 'Maria Garcia' or vendedor == 'Juan Perez'")
print(ventas_vendedores)