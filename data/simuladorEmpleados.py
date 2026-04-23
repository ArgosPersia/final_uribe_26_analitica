import random
from datetime import datetime

def crear_empleados(N):
    nombres = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Elena", "Jorge"]
    apellidos = ["Zapata", "Cano", "Giraldo", "Valencia", "Rios", "Gomez", "Perez"]
    
    lista_empleados = []
    for i in range(N):
        nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"
        empleado = {
            "id": i + 1,
            "nombres_apellidos": nombre_completo,
            "salario_base": 1300000,
            "documento": random.randint(1000000, 9999999),
            "fecha_ingreso": datetime(2026, 1, 1).strftime("%Y-%m-%d")
        }
        lista_empleados.append(empleado)
    return lista_empleados