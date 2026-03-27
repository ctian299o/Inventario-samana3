# Sistema de Inventario en Python

## Descripción

Este programa es un sistema de inventario básico desarrollado en Python que permite gestionar productos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), además de generar estadísticas y guardar/cargar datos desde archivos CSV.

---

## ¿Cómo funciona el programa?

El sistema utiliza una **lista de diccionarios** para almacenar los productos.
Cada producto tiene la siguiente estructura:

```python
{
  "nombre": "Producto",
  "precio": 1000,
  "cantidad": 10
}
```

---

##  Explicación paso a paso

### 1. Importación de librería

```python
import csv
```

Se importa la librería `csv` para poder guardar y leer archivos en formato CSV.

---

### 2.  Creación del inventario

```python
inventario = []
```

Se inicializa una lista vacía donde se almacenarán los productos.

---

## FUNCIONES CRUD

### 3.  Agregar producto

```python
def agregar_producto(inventario, nombre, precio, cantidad):
```

* Crea un diccionario con los datos del producto.
* Lo agrega a la lista `inventario`.

---

### 4.  Mostrar inventario

```python
def mostrar_inventario(inventario):
```

* Si el inventario está vacío → muestra "Inventario vacío".
* Si no → recorre la lista y muestra cada producto.

---

### 5.  Buscar producto

```python
def buscar_producto(inventario, nombre):
```

* Recorre el inventario.
* Si encuentra el producto → lo devuelve.
* Si no → retorna `None`.

---

### 6. Actualizar producto

```python
def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
```

* Busca el producto.
* Si existe:

  * Actualiza el precio (si se proporciona).
  * Actualiza la cantidad (si se proporciona).
* Retorna `True` si lo actualiza, `False` si no lo encuentra.

---

### 7. Eliminar producto

```python
def eliminar_producto(inventario, nombre):
```

* Busca el producto.
* Si existe → lo elimina de la lista.
* Retorna `True` o `False`.

---

##  ESTADÍSTICAS

### 8. Calcular estadísticas

```python
def calcular_estadisticas(inventario):
```

Calcula:

* Total de unidades
* Valor total del inventario
* Producto más caro
* Producto con mayor stock

Retorna un diccionario con estos datos.

---

## ARCHIVOS CSV

### 9. Guardar inventario

```python
def guardar_csv(inventario, ruta):
```

* Guarda los datos en un archivo CSV.
* Escribe encabezados: nombre, precio, cantidad.
* Maneja errores con `try/except`.

---

##  MENÚ INTERACTIVO

El programa usa un `while True` para ejecutar un menú continuo:

```text
1. Agregar
2. Mostrar
3. Buscar
4. Actualizar
5. Eliminar
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
```

###  Flujo del programa:

* El usuario elige una opción.
* El programa ejecuta la función correspondiente.
* Se repite hasta que el usuario elija salir.

---

##  Características principales

✅ CRUD completo
✅ Validación de datos
✅ Manejo de errores
✅ Persistencia con archivos CSV
✅ Estadísticas del inventario
✅ Menú interactivo

---

##  Ejemplo de uso

```text
Elige una opción: 1
Nombre: Laptop
Precio: 2500
Cantidad: 5
```

---

##  Posibles mejoras

* Agregar interfaz gráfica (GUI)
* Usar base de datos (SQLite)
* Validar entradas del usuario más estrictamente
* Mejorar formato de impresión

---

## Autor

Proyecto educativo para aprender:

* Listas y diccionarios
* Funciones
* Archivos CSV
* Lógica de programación

---
