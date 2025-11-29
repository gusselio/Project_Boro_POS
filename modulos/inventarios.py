# inventarios.py

from modulos.notificaciones import refresh_notificaciones
from modulos.datos import inventario, stock_inicial, guardar_inventario, notificaciones_compra, recetas

def descontar_insumos(producto, cantidad):
    ingredientes = recetas.get(producto, {})

    for insumo, cantidad_necesaria in ingredientes.items():
        inventario[insumo] -= cantidad * cantidad_necesaria

def visualizar_inventario():
    """Muestra el inventario actual."""
    print("\n==============================")
    print("      INVENTARIO ACTUAL")
    print("==============================")
    print(f"{'Nombre':<15} | {'Cantidad'}")
    print("-" * 30)
    for producto, cantidad in inventario.items():
        print(f"{producto:<15}: {cantidad}")


def agregar_producto():
    """Agrega un nuevo artículo al inventario."""
    nombre_articulo_nuevo = input("Ingrese el nombre del nuevo artículo: ")
    cantidad_nuevo_articulo = int(input("Ingrese la cantidad: "))

    if nombre_articulo_nuevo in inventario:
        print("❌ El artículo ya existe.")
    else:
        inventario[nombre_articulo_nuevo] = cantidad_nuevo_articulo
        stock_inicial[nombre_articulo_nuevo] = cantidad_nuevo_articulo
        refresh_notificaciones()
        print(f"✅ Artículo '{nombre_articulo_nuevo}' agregado con {cantidad_nuevo_articulo} unidades.")

    guardar_inventario()
    refresh_notificaciones()

def editar_producto():
    """Edita nombre o cantidad de un artículo existente."""
    articulo_editar = input("¿Qué artículo quieres editar?: ")

    if articulo_editar not in inventario:
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

            valor_actual = inventario[articulo_editar]

            # Renombrar en inventario
            inventario[nuevo_nombre] = valor_actual
            del inventario[articulo_editar]

            # Renombrar en stock inicial
            if articulo_editar in stock_inicial:
                stock_inicial[nuevo_nombre] = stock_inicial.pop(articulo_editar)

            # Renombrar en notificaciones si existiera
            if articulo_editar in notificaciones_compra:
                notificaciones_compra[nuevo_nombre] = notificaciones_compra.pop(articulo_editar)

            refresh_notificaciones()
            print("✅ Nombre actualizado correctamente.")
            break

        elif opcion == 2:
            nueva_cantidad = int(input("Nueva cantidad: "))
            inventario[articulo_editar] = nueva_cantidad
            stock_inicial[articulo_editar] = nueva_cantidad
            refresh_notificaciones()
            print("✅ Cantidad actualizada.")
            break

        elif opcion == 3:
            print("Edición cancelada.")
            break

        else:
            print("❌ Opción inválida.")
    guardar_inventario()
    refresh_notificaciones()

def eliminar_producto():
    """Elimina un artículo del inventario."""
    producto_eliminar = input("¿Qué producto deseas eliminar?: ")

    if producto_eliminar not in inventario:
        print("❌ El producto no existe.")
        return

    print("¿Seguro que deseas eliminarlo?")
    print("1. Sí, eliminar")
    print("2. No, cancelar")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        del inventario[producto_eliminar]
        stock_inicial.pop(producto_eliminar, None)
        notificaciones_compra.pop(producto_eliminar, None)
        refresh_notificaciones()
        print("🗑️ Producto eliminado correctamente.")
    else:
        print("Cancelado.")
    guardar_inventario()
    refresh_notificaciones()

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
