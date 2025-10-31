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
            "Cafe": 10, "Agua": 200, "Vasos Calientes": 1
        },
        "Cafe Capuccino": {
            "Cafe": 10, "Leche": 50, "Agua": 150, "Vasos Calientes": 1
        },
        "Cafe Moka": {
            "Cafe": 60, "Leche": 120, "Chocolate": 20, "Vasos Calientes": 1
        },
        "Tisana Frutos Rojos": {
            "Tisana Roja": 50, "Agua": 360, "Vasos Calientes": 1
        }

    },
    "Bebidas Frias": {
        "Frappuccino Moka": {
            "Cafe": 10, "Leche": 100, "Hielo": 70, "Vasos Frios": 1
        },
        "Frappuccino Chocolate Blanco":{
            "Chocolate Blanco": 80, "Leche": 180, "Hielo": 180, "Vasos Frios": 1
        },
        "Frapuccino Matcha": {
            "Polvo Matcha": 15,"Agua": 60, "Leche": 240, "Hielo": 60, "Vasos Frios": 1
        },
        "Iced Latte": {
            "Cafe": 45, "Leche": 150, "Hielo": 60, "Vasos Frios": 1
        }
    },
    "Postres": {
        "Pan de Muerto": 10
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
    "Chocolate": 1000 # Gramos
    "Vasos Frios": 300, #Unidades
    "Vasos Calientes": 500, #Unidades
    "Tisana Roja": 500, #Gramos
    "Hielo": 20000, #Gamos
    "Polvo Matcha": 150
}
def punto_de_venta():
    print("\nPUNTO DE VENTA")

def ventas():
    print("Ventas")

#SUBFUNCIONES DE INVENTARIOS
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
                print("Cargando Inventario")
                print("\n==============================")
                print("      INVENTARIO ACTUAL")
                print("==============================")
                print(f"{'Nombre':<15} | {'Cantidad'}")
                print("-" * 30)
                for producto, cantidad in inventario.items():
                    print(f"{producto:<15}: {cantidad}")
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