# =========================================
# Universidad Tecmilenio
# Proyecto: Sistema de Inventario - Café BORO
# Versión: Avance lineal (sin clases)
# Nombre: Gustavo Salvador Leal Dominguez
# Fecha: 26 de Octubre de 2025
# =========================================

inventario = {
    "Cafe": 10,     #Kilos
    "Leche": 5000,  #Mililitros
    "Azucar": 2000, #Gramos
    "Vasos": 100,   #Unidades
    "Tapas": 100    #Unidades
}
def punto_de_venta():
    print("Punto de venta")

def ventas():
    print("Ventas")

def inventarios():
    print("Inventarios")


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
                punto_de_venta()
            case 2:
                print("Ingresando a Ventas")
            case 3:
                print("Ingresando a Inventarios")
            case _:
                print("Opcion invalida, intentelo nuevamente")

menu_principal()