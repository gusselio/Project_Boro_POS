from modulos.datos import inventario, recetas, stock_inicial, guardar_inventario, historial_ventas, guardar_historial
from modulos.notificaciones import refresh_notificaciones, notificaciones_compra
from modulos.inventarios import visualizar_inventario, descontar_insumos
from datetime import datetime


# ----------------------------------
#   Verificar existencia
# ----------------------------------
def verificar_existencia(producto, cantidad):
    for categoria in recetas.values():
        if producto in categoria:
            receta = categoria[producto]
            for insumo, cantidad_necesaria in receta.items():
                if insumo == "Precio":
                    continue
                total_requerido = cantidad_necesaria * cantidad
                disponible = inventario.get(insumo, 0)
                if disponible < total_requerido:
                    print(f"❌ No hay suficiente '{insumo}' para preparar {cantidad}x {producto}.")
                    print(f"Disponible: {disponible}\n")
                    return False
            return True
    return False


# ----------------------------------
#   Descontar inventario
# ----------------------------------
def descontar_inventario(producto, cantidad):
    for categoria in recetas.values():
        if producto in categoria:
            receta = categoria[producto]
            for insumo, cantidad_necesaria in receta.items():
                if insumo == "Precio":
                    continue
                total_requerido = cantidad_necesaria * cantidad
                inventario[insumo] -= total_requerido
                if inventario[insumo] < 0:
                    inventario[insumo] = 0
    guardar_inventario()
    refresh_notificaciones()

# ----------------------------------
#   Finalizar venta
# ----------------------------------
def finalizar_venta(pedido_actual):
    from modulos.datos import historial_ventas
    total = 0
    venta_realizada = []

    print("\n--- RESUMEN DE VENTA ---")

    for producto, cantidad in pedido_actual.items():

        # BUSCAR EL PRECIO EN RECETAS
        precio = None
        for categoria, items in recetas.items():
            if producto in items:
                precio = items[producto]["Precio"]
                break

        if precio is None:
            print(f"❌ ERROR: No se encontró precio de {producto}.")
            continue

        subtotal = precio * cantidad

        print(f"{producto} x{cantidad} = ${subtotal}")
        total += subtotal

        # Descontar inventario
        descontar_insumos(producto, cantidad)

        # Registrar en historial
        venta_realizada.append({
            "producto": producto,
            "cantidad": cantidad,
            "subtotal": subtotal
        })

    historial_ventas.append(venta_realizada)

    print(f"\n💰 TOTAL A PAGAR: ${total}")
    input("\nPresione Enter para continuar...")

# ----------------------------------
#   Seleccionar producto
# ----------------------------------
def seleccionar_producto(categoria, pedido_actual):
    print(f"\n--- {categoria} ---")
    productos = recetas[categoria]

    for i, producto in enumerate(productos.keys(), 1):
        print(f"{i}. {producto} - ${productos[producto]['Precio']}")

    opcion = int(input("Seleccione un producto: "))
    producto_seleccionado = list(productos.keys())[opcion - 1]
    cantidad = int(input("Ingrese la cantidad: "))

    if not verificar_existencia(producto_seleccionado, cantidad):
        print("⚠️ No se agregó al pedido por falta de insumos.\n")
        return

    pedido_actual[producto_seleccionado] = pedido_actual.get(producto_seleccionado, 0) + cantidad

    print("\n🧾 PEDIDO ACTUAL:")
    for prod, cant in pedido_actual.items():
        print(f"- {prod}: {cant}")


# ----------------------------------
#   Realizar venta
# ----------------------------------
def realizar_venta():
    pedido_actual = {}

    while True:
        print("\n1. Bebidas Calientes")
        print("2. Bebidas Frias")
        print("3. Postres")
        print("4. Finalizar venta")
        opcion = int(input("Ingrese su opción: "))

        match opcion:
            case 1:
                seleccionar_producto("Bebidas Calientes", pedido_actual)
            case 2:
                seleccionar_producto("Bebidas Frias", pedido_actual)
            case 3:
                seleccionar_producto("Postres", pedido_actual)
            case 4:
                finalizar_venta(pedido_actual)
                break
            case _:
                print("Opción inválida.")


# ----------------------------------
#   Menú del punto de venta
# ----------------------------------
def punto_de_venta():
    print("\n=========== PUNTO DE VENTA ===========")

    while True:
        print("\n1. Realizar una venta")
        print("2. Ver inventario")
        print("3. Salir")
        opcion = int(input("Ingrese su opción: "))

        match opcion:
            case 1:
                realizar_venta()
            case 2:
                visualizar_inventario()
            case 3:
                return
