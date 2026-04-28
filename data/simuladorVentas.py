from datetime import datetime, timedelta
import random


def generar_ventas(numero_facturas, lista_empleados):
    catalogo_productos = [
        {"nombre": "Camisa Polo Slim Fit Algodon",  "precio": 200000},
        {"nombre": "Jeans Classic Blue Denim",       "precio": 180000},
        {"nombre": "Chaqueta Bomber Impermeable",    "precio": 350000},
        {"nombre": "Camiseta Basica Cuello V",       "precio":  85000},
        {"nombre": "Bermuda Cargo Beige",            "precio": 120000},
        {"nombre": "Saco Cuello Tortuga Lana",       "precio": 220000},
    ]

    tallas_disponibles = ["XS", "S", "M", "L", "XL", "XXL"]
    fecha_inicio = datetime(2026, 1, 2)
    ventas = []

    for _ in range(numero_facturas):
        empleado_vendedor = random.choice(lista_empleados)
        nombre_vendedor = empleado_vendedor["nombres_apellidos"]

        cantidad_productos_distintos = random.randint(1, 4)
        fecha_transaccion = fecha_inicio + timedelta(days=random.randint(0, 60))

        for _ in range(cantidad_productos_distintos):
            producto_seleccionado = random.choice(catalogo_productos)
            cantidad_unidades = random.randint(1, 3)

            venta = {
                "producto":        producto_seleccionado["nombre"],
                "precio_unitario": producto_seleccionado["precio"],
                "talla":           random.choice(tallas_disponibles),
                "cantidad":        cantidad_unidades,
                "vendedor":        nombre_vendedor,
                "total":           cantidad_unidades * producto_seleccionado["precio"],
                "fecha":           fecha_transaccion.strftime("%Y-%m-%d"),
            }

            probabilidad_error = random.random()

            if probabilidad_error < 0.15:
                venta["producto"] = " " + venta["producto"] + " "
            elif probabilidad_error < 0.30:
                venta["vendedor"] = venta["vendedor"].upper()
            elif probabilidad_error < 0.40:
                venta["talla"] = "medio"
            elif probabilidad_error < 0.50:
                venta["cantidad"] = random.choice([0, -1, None])
            elif probabilidad_error < 0.60:
                venta["precio_unitario"] = None
            elif probabilidad_error < 0.70:
                venta["fecha"] = fecha_transaccion.strftime("%d/%m/%Y")
            elif probabilidad_error < 0.80:
                venta["total"] = random.randint(5000, 15000)
            elif probabilidad_error < 0.90:
                venta["producto"] = venta["producto"].lower()

            ventas.append(venta)

    if len(ventas) >= 3:
        ventas.append(ventas[0].copy())
        ventas.append(ventas[1].copy())

    return ventas