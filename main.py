# =========================================
# Universidad Tecmilenio
# Proyecto: Sistema de Inventario - Café BORO
# Versión: Avance lineal (sin clases)
# Nombre: Gustavo Salvador Leal Dominguez
# Fecha: 26 de Octubre de 2025
# =========================================
import time

recetas = {
    "Bebidas Calientes": {
        "Cafe Americano": {
            "Cafe": 10, "Agua": 200, "Vasos Calientes": 1, "Precio": 45
        },
        "Cafe Capuccino": {
            "Cafe": 10, "Leche": 50, "Agua": 150, "Vasos Calientes": 1, "Precio": 65
        },
        "Cafe Moka": {
            "Cafe": 60, "Leche": 120, "Chocolate": 20, "Vasos Calientes": 1, "Precio": 65
        },
        "Tisana Frutos Rojos": {
            "Tisana Roja": 50, "Agua": 360, "Vasos Calientes": 1, "Precio": 50
        }

    },
    "Bebidas Frias": {
        "Frappuccino Moka": {
            "Cafe": 10, "Leche": 100, "Hielo": 70, "Vasos Frios": 1, "Precio": 85
        },
        "Frappuccino Chocolate Blanco":{
            "Chocolate Blanco": 80, "Leche": 180, "Hielo": 180, "Vasos Frios": 1, "Precio": 80
        },
        "Frapuccino Matcha": {
            "Polvo Matcha": 15,"Agua": 60, "Leche": 240, "Hielo": 60, "Vasos Frios": 1, "Precio": 85
        },
        "Iced Latte": {
            "Cafe": 45, "Leche": 150, "Hielo": 60, "Vasos Frios": 1, "Precio": 65
        }

    },
    "Postres": {
        "Pan de Muerto": {
            "Unidades": 10, "Precio": 40
        },
        "Galleta": {
            "Unidades": 16, "Precio": 20
        }
    }
}

inventario = {
    "Cafe": 10,     #Kilos
    "Leche": 5000,  #Mililitros
    "Azucar": 2000, #Gramos
    "Vasos": 100,   #Unidades
    "Agua": 40000, #Mililitros
    "Tapas": 100,    #Unidades
    "Chocolate Blanco":1000, #Gramos
    "Chocolate": 1000, # Gramos
    "Vasos Frios": 300, #Unidades
    "Vasos Calientes": 500, #Unidades
    "Tisana Roja": 500, #Gramos
    "Hielo": 20000, #Gamos
    "Polvo Matcha": 150
}


# SUBFUNCIÓN DE REALIZAR VENTA
def finalizar_venta(pedido_actual):
    total = 0
    print("\n--- RESUMEN DE VENTA ---")
    for producto, cantidad in pedido_actual.items():
        # Buscar a qué categoría pertenece
        for categoria in recetas.values():
            if producto in categoria:
                precio_unitario = categoria[producto]["Precio"]
                total_producto = precio_unitario * cantidad
                total += total_producto
                print(f"{producto} x{cantidad} = ${total_producto}")
                break
    print(f"\n💰 TOTAL A PAGAR: ${total}")


# SUBFUNCIÓN DE REALIZAR VENTA
def seleccionar_producto(categoria, pedido_actual):
    print(f"\n--- {categoria.replace('_', ' ').title()} ---")
    productos = recetas[categoria]

    for i, producto in enumerate(productos.keys(), start=1):
        print(f"{i}. {producto} - ${productos[producto]['Precio']}")

    opcion = int(input("Seleccione un producto: "))
    producto_seleccionado = list(productos.keys())[opcion - 1]
    cantidad = int(input("Ingrese la cantidad: "))

    # Se guarda o acumula
    pedido_actual[producto_seleccionado] = pedido_actual.get(producto_seleccionado, 0) + cantidad
    print(f"✅ {cantidad}x {producto_seleccionado} agregado(s) al pedido.")

    # Mostrar el pedido actual completo
    print("\n🧾 PEDIDO ACTUAL:")
    for producto, cantidad in pedido_actual.items():
        print(f"- {producto}: {cantidad}")
    print()  # Línea vacía para separar


# SUBFUNCIONES DE PUNTO DE VENTA
def realizar_venta():
    pedido_actual = {}
    while True:
        print("1. Bebidas Calientes")
        print("2. Bebidas Frias")
        print("3. Postres")
        print("4. Salir - Ver Total")
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


def punto_de_venta():
    print("\n==============================")
    print("        PUNTO DE VENTA")
    print("==============================")
    while True:
        print("\n¿Qué acción quiere realizar?")
        print("1. Realizar una Venta")
        print("2. Ver inventario")
        print("3. Salir")
        opcion = int(input("Ingrese su opción: "))
        match opcion:
            case 1:
                realizar_venta()
            case 2:
                visualizar_inventario()
            case 3:
                break


def ventas():
    print("Ventas")

#SUBFUNCIONES DE INVENTARIOS
def visualizar_inventario():
    print("Cargando Inventario")
    print("\n==============================")
    print("      INVENTARIO ACTUAL")
    print("==============================")
    print(f"{'Nombre':<15} | {'Cantidad'}")
    print("-" * 30)
    for producto, cantidad in inventario.items():
        print(f"{producto:<15}: {cantidad}")

def agregar_producto():
    nombre_articulo_nuevo = input("Ingrese el nombre del nuevo articulo: ")
    cantidad_nuevo_articulo = int(input("Ingrese la cantidad: "))

    if nombre_articulo_nuevo in inventario:
        print("El nuevo articulo ya existe")
    else:
        inventario[nombre_articulo_nuevo] = cantidad_nuevo_articulo
        print(f"El articulo {nombre_articulo_nuevo} ha sido agregado correctamente, con {cantidad_nuevo_articulo}")

def editar_producto():
    articulo_editar = input("Cual articulo quieres editar?: ")
    while True:
        if articulo_editar in inventario:
            print("Que quieres editar?\n 1. Nombre de Articulo\n 2. Cantidad del Articulo")
            opcion_editar_articulo = int(input("Ingrese su opcion: "))
            if opcion_editar_articulo == 1:
                nuevo_nombre_articulo = input("Ingrese el nuevo nombre del articulo: ")

                #Se copia el valor de la clave vieja
                valor_actual = inventario[articulo_editar]

                #Se crea la nueva clave y se le asigna la copia de valor de la clave vieja
                inventario[nuevo_nombre_articulo] = valor_actual

                #Se elimina la clave vieja
                del inventario[articulo_editar]
                print(f"El cambio ha sido realizado correctamente")
                print(f"Nombre cambiado correctamente a {nuevo_nombre_articulo}")
            elif opcion_editar_articulo == 2:
                nueva_cantidad_articulo = int(input("Ingrese su nuevo cantidad: "))
                inventario[articulo_editar] = nueva_cantidad_articulo
            else:
                break
        else:
            print("Este articulo no existe, revise el nombre ingresado")
        break

def eliminar_producto():
    producto_eliminar = input("Cual producto quieres eliminar?: ")
    while True:
        if producto_eliminar in inventario:
            print("Seguro que quieres eliminar este articulo?\n1. Si\n2. No")
            opcion_eliminar_articulo = int(input("Ingrese su opcion: "))
            if opcion_eliminar_articulo == 1:
                del inventario[producto_eliminar]
                print("\nProducto eliminado correctamente")
                break
            else:
                break
        else:
            print("El producto no existe, revise el nombre ingresado")
            break


def inventarios():
    print("\n==============================")
    print("        INVENTARIOS")
    print("==============================")
    while True:
        print("\nQue accion quiere realizar?")
        print("1. Ver Inventario Actual")
        print("2. Añadir Producto")
        print("3. Editar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")
        opcion = int(input("\nIngrese su opcion: "))
        match opcion:
            case 1:
                visualizar_inventario()
            case 2:
                agregar_producto()
            case 3:
                editar_producto()
            case 4:
                eliminar_producto()
            case 5:
                break



#Declaracion de la funcion Menu principal
def menu_principal():
    while True:
        print("CAFE BORO - SISTEMA DE CONTROL")
        print("1. Punto de Venta")
        print("2. Ventas")
        print("3. Inventario")
        print("4. Salir")

        opcion = int(input("Ingrese su opcion: "))
        match opcion:
            case 1:
                print("Ingresando a Punto de Venta")
                time.sleep(0.5)
                punto_de_venta()
            case 2:
                print("Ingresando a Ventas")
                time.sleep(0.3)
                ventas()
            case 3:
                print("\nIngresando a Inventarios")
                time.sleep(0.8)
                inventarios()
            case _:
                print("Opcion invalida, intentelo nuevamente")

menu_principal()