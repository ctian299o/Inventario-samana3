# Inventario (lista de diccionarios) 
# FUNCIONES CRUD 
# ESTADÍSTICAS 

import csv

inventario = []


def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)


def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacío")
    else:
        for p in inventario:
            print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"] == nombre:
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False


def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False



def calcular_estadisticas(inventario):
    if not inventario:
        return None

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }


# GUARDAR CSV

def guardar_csv(inventario, ruta):
    if not inventario:
        print("No hay datos para guardar")
        return

    try:
        with open(ruta, mode="w", newline="") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except Exception:
        print("Error al guardar archivo")


# CARGAR CSV

def cargar_csv(ruta):
    inventario_cargado = []
    errores = 0

    try:
        with open(ruta, mode="r") as archivo:
            reader = csv.reader(archivo)
            encabezado = next(reader)

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido")
                return []

            for fila in reader:
                try:
                    if len(fila) != 3:
                        errores += 1
                        continue

                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    inventario_cargado.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })

                except:
                    errores += 1

        print(f"Archivo cargado. Filas inválidas: {errores}")
        return inventario_cargado

    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception:
        print("Error al leer archivo")

    return []


# ================= MENÚ PRINCIPAL =================

while True:
    print("\n===== MENÚ =====")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        agregar_producto(inventario, nombre, precio, cantidad)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        p = buscar_producto(inventario, nombre)
        print(p if p else "No encontrado")

    elif opcion == "4":
        nombre = input("Nombre: ")
        precio = input("Nuevo precio (Enter para omitir): ")
        cantidad = input("Nueva cantidad (Enter para omitir): ")

        precio = float(precio) if precio else None
        cantidad = int(cantidad) if cantidad else None

        if not actualizar_producto(inventario, nombre, precio, cantidad):
            print("Producto no encontrado")

    elif opcion == "5":
        nombre = input("Nombre: ")
        if not eliminar_producto(inventario, nombre):
            print("Producto no encontrado")

    elif opcion == "6":
        stats = calcular_estadisticas(inventario)
        if stats:
            print(stats)
        else:
            print("Inventario vacío")

    elif opcion == "7":
        ruta = input("Ruta del archivo: ")
        guardar_csv(inventario, ruta)

    elif opcion == "8":
        ruta = input("Ruta del archivo: ")
        nuevos = cargar_csv(ruta)

        if nuevos:
            decision = input("¿Sobrescribir inventario? (S/N): ")
            if decision.upper() == "S":
                inventario = nuevos
            else:
                inventario.extend(nuevos)

    elif opcion == "9":
        print("Fin del programa")
        break

    else:
        print("Opción inválida")