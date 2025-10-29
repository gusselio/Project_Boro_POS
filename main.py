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
                print("Cargando Inventario", time.sleep(0.1),".",time.sleep(0.1),".",time.sleep(0.1),".\n")
                print("\n==============================")
                print("      INVENTARIO ACTUAL")
                print("==============================")
                print(f"{'Nombre':<15} | {'Cantidad'}")
                print("-" * 30)
                for producto, cantidad in inventario.items():
                    print(f"{producto:<15}: {cantidad}")
            case 2:
                agregar_articulo()



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