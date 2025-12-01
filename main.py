"""
Universidad Tecmilenio

Proyecto: Sistema de Punto de Venta e Inventario - Café BORO
Versión: Proyecto Final

Nombre: Ing. Gustavo Salvador Leal Dominguez
Matrícula: 7225668

Materia:   Fundamentos de Programación
Profesor:  Ing. Carlos A. Sánchez Rivera
Fecha:     22 de octubre de 2025
"""

import time

# Importar funciones principales de cada módulo
from modulos.inventarios import inventarios
from modulos.punto_venta import punto_de_venta
from modulos.notificaciones import ver_notificaciones
from modulos.gestion_archivos import gestion_archivos
from modulos.ventas import menu_ventas

# Cargar datos globales
from modulos.datos import inventario, stock_inicial, notificaciones_compra


# ------------------------------- MENÚ PRINCIPAL -------------------------------

def menu_principal():
    while True:
        print("\n===================================")
        print("      CAFE BORO - SISTEMA POS")
        print("===================================")
        print("1. Punto de Venta")
        print("2. Ventas")
        print("3. Inventario")
        print("4. Notificaciones")
        print("5. Gestión de Archivos (Actividad)")
        print("6. Salir")

        try:
            opcion = int(input("\nIngrese su opción: "))
        except ValueError:
            print("❌ Opción inválida, ingrese un número.")
            continue

        match opcion:
            case 1:
                print("Ingresando a Punto de Venta...")
                time.sleep(0.5)
                punto_de_venta()

            case 2:
                print("Ingresando a Ventas...")
                time.sleep(0.5)
                menu_ventas()

            case 3:
                print("\nIngresando a Inventarios...")
                time.sleep(0.5)
                inventarios()

            case 4:
                ver_notificaciones()

            case 5:
                print("Gestión de Archivos (Actividad)")
                gestion_archivos()

            case 6:
                print("Programa Finalizado")
                break

            case _:
                print("Opción inválida, intentelo nuevamente.")


# ------------------------------- PROGRAMA -------------------------------

if __name__ == "__main__":
    menu_principal()
