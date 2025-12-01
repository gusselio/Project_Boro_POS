import json
from modulos.notificaciones import refresh_notificaciones
from modulos.datos import (
    cargar_inventario,
    cargar_recetas,
    guardar_inventario,
    notificaciones_compra,
    stock_inicial,
)


def visualizar_inventario():
    inventario = cargar_inventario()

    print("\n==============================")
    print("      INVENTARIO ACTUAL")
    print("==============================")
    print(f"{'Nombre':<15} | {'Cantidad'}")
    print("-" * 30)

    for producto, cantidad in inventario.items():
        print(f"{producto:<15}: {cantidad}")


def agregar_producto():
    inventario = cargar_inventario()  # cargar estado actual

    nombre = input("Ingrese el nombre del nuevo artículo: ")
    cantidad = int(input("Ingrese la cantidad: "))

    if nombre in inventario:
        print("❌ El artículo ya existe.")
        return

    inventario[nombre] = cantidad
    stock_inicial[nombre] = cantidad

    guardar_inventario()
    refresh_notificaciones()
    print(f"✅ Artículo '{nombre}' agregado.")


def editar_producto():
    inventario = cargar_inventario()

    articulo = input("¿Qué artículo deseas editar?: ")

    if articulo not in inventario:
        print("❌ El artículo no existe.")
        return

    while True:
        print("\n¿Qué deseas editar?")
        print("1. Nombre del artículo")
        print("2. Cantidad del artículo")
        print("3. Cancelar")

        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            nuevo_nombre = input("Nuevo nombre: ")

            valor_actual = inventario[articulo]
            inventario[nuevo_nombre] = valor_actual
            del inventario[articulo]

            # actualizar stock inicial
            if articulo in stock_inicial:
                stock_inicial[nuevo_nombre] = stock_inicial.pop(articulo)

            # actualizar notificaciones
            if articulo in notificaciones_compra:
                notificaciones_compra[nuevo_nombre] = notificaciones_compra.pop(articulo)

            print("✅ Nombre actualizado correctamente.")
            break

        elif opcion == 2:
            nueva_cantidad = int(input("Nueva cantidad: "))
            inventario[articulo] = nueva_cantidad
            stock_inicial[articulo] = nueva_cantidad
            print("✅ Cantidad actualizada.")
            break

        elif opcion == 3:
            print("Edición cancelada.")
            return

        else:
            print("❌ Opción inválida.")

    guardar_inventario()
    refresh_notificaciones()


def eliminar_producto():
    inventario = cargar_inventario()

    producto = input("¿Qué producto deseas eliminar?: ")

    if producto not in inventario:
        print("❌ El producto no existe.")
        return

    print("¿Seguro que deseas eliminarlo?")
    print("1. Sí, eliminar")
    print("2. No, cancelar")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        del inventario[producto]
        stock_inicial.pop(producto, None)
        notificaciones_compra.pop(producto, None)

        guardar_inventario()
        refresh_notificaciones()

        print("🗑️ Producto eliminado correctamente.")
    else:
        print("Cancelado.")


def inventarios():
    """Menú principal del módulo de inventarios."""
    while True:
        print("\n==============================")
        print("        INVENTARIOS")
        print("==============================")
        print("1. Ver Inventario Actual")
        print("2. Añadir Producto")
        print("3. Editar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")

        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            visualizar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            editar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            break
        else:
            print("❌ Opción inválida.")
