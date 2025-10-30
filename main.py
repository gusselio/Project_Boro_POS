# =========================================
# Universidad Tecmilenio
# Proyecto: Sistema de Inventario - Café BORO
# Versión: Avance lineal (sin clases)
# Nombre: Gustavo Salvador Leal Dominguez
# Fecha: 26 de Octubre de 2025
# =========================================
import time

inventario = {
    "Cafe": 10,     #Kilos
    "Leche": 5000,  #Mililitros
    "Azucar": 2000, #Gramos
    "Vasos": 100,   #Unidades
    "Tapas": 100    #Unidades
}
def punto_de_venta():
    print("\nPUNTO DE VENTA")

def ventas():
    print("Ventas")

def agregar_articulo():
    nombre_artirulo_nuevo = input("Ingrese el nombre del nuevo articulo: ")
    cantidad_nuevo_articulo = int(input("Ingrese la cantidad: "))

    if nombre_artirulo_nuevo in inventario:
        print("El nuevo articulo ya existe")
    else:
        inventario[nombre_artirulo_nuevo] = cantidad_nuevo_articulo
        print(f"El articulo {nombre_artirulo_nuevo} ha sido agregado correctamente, con {cantidad_nuevo_articulo}")

def editar_articulo():
    articulo_editar = input("Cual articulo quieres editar?: ")
    while True:
        if articulo_editar in inventario:
            print("Que quieres editar?\n 1. Nombre de Articulo\n 2. Cantidad del Articulo")
            opcion_editar_articulo = int(input("Ingrese su opcion: "))
            if opcion_editar_articulo == 1:
                nuevo_nombre_articulo = input("Ingrese el nuevo nombre del articulo: ")
                valor_actual = inventario[articulo_editar]
                inventario[nuevo_nombre_articulo] = valor_actual
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

def inventarios():
    print("\n==============================")
    print("        INVENTARIOS")
    print("==============================")
    while True:
        print("\nQue accion quiere realizar?")
        print("1. Ver Inventario Actual")
        print("2. Añadir Producto")
        print("3. Editar Producto")
        print("4. Salir")
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
                agregar_articulo()

            case 3:
                editar_articulo()



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