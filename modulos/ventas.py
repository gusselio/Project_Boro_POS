import os
from datetime import datetime
from modulos.datos import historial_ventas

# Carpeta donde se guardan los reportes
RUTA_REPORTES = "reportes"

# Crear carpeta si no existe
if not os.path.exists(RUTA_REPORTES):
    os.makedirs(RUTA_REPORTES)


# =========================
#   MENU PRINCIPAL
# =========================
def menu_ventas():
    while True:
        print("\n===== MENÚ DE VENTAS =====")
        print("1. Generar reporte del día")
        print("2. Exportar reporte a TXT")
        print("3. Mostrar historial en pantalla")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            generar_reporte_dia()

        elif opcion == "2":
            exportar_reporte_txt()

        elif opcion == "3":
            mostrar_historial()

        elif opcion == "0":
            break

        else:
            print("❌ Opción inválida.\n")


# =========================
#   FUNCIONES DE REPORTE
# =========================

def generar_reporte_dia():
    print("\n===== REPORTE DEL DÍA =====\n")

    if not historial_ventas:
        print("No hay ventas registradas hoy.\n")
        return

    for i, venta in enumerate(historial_ventas, 1):

        # Validación robusta
        if not isinstance(venta, dict) or "detalle" not in venta:
            print(f"⚠️ Advertencia: Registro de venta #{i} está corrupto y se omitió.")
            continue

        print(f"Venta #{i} - Hora: {venta['hora']}")

        # Validar que el detalle sea una lista
        detalle = venta["detalle"]
        if not isinstance(detalle, list):
            print("⚠️ Error: 'detalle' no es una lista, registro omitido.")
            continue

        for item in detalle:
            if not isinstance(item, dict):
                print("⚠️ Error: un item no es diccionario.")
                continue

            print(f" - {item['producto']} x{item['cantidad']} = ${item['subtotal']}")

        print()




def exportar_reporte_txt():
    from modulos.datos import historial_ventas
    import os
    from datetime import datetime

    if not historial_ventas:
        print("No hay ventas para exportar.\n")
        return

    # Crear carpeta si no existe
    os.makedirs("reportes", exist_ok=True)

    # Crear nombre con fecha y hora
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"reporte_{timestamp}.txt"
    ruta_archivo = os.path.join("reportes", nombre_archivo)

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("===== REPORTE DEL DÍA =====\n\n")

        for i, venta in enumerate(historial_ventas, 1):

            # Validar estructura de la venta
            if not isinstance(venta, dict) or "detalle" not in venta:
                archivo.write(f"⚠️ Registro #{i} corrupto — omitido.\n\n")
                continue

            archivo.write(f"Venta #{i} - Hora: {venta['hora']}\n")

            detalle = venta["detalle"]

            # Validar tipo del detalle
            if not isinstance(detalle, list):
                archivo.write("⚠️ Error: 'detalle' no es una lista — omitido.\n\n")
                continue

            for item in detalle:
                if not isinstance(item, dict):
                    archivo.write("⚠️ Error: item no es diccionario — omitido.\n")
                    continue

                archivo.write(f" - {item['producto']} x{item['cantidad']} = ${item['subtotal']}\n")

            archivo.write("\n")

    print(f"Reporte exportado correctamente: {ruta_archivo}\n")
    input("Presione ENTER para continuar...")


def mostrar_historial():
    from modulos.datos import historial_ventas

    if not historial_ventas:
        print("No hay ventas registradas.\n")
        return

    print("\n===== HISTORIAL COMPLETO =====\n")

    for i, venta in enumerate(historial_ventas, 1):

        # Validar estructura
        if not isinstance(venta, dict) or "detalle" not in venta:
            print(f"⚠️ Registro #{i} corrupto — omitido.\n")
            continue

        print(f"Venta #{i} - Hora: {venta['hora']}")

        detalle = venta["detalle"]

        if not isinstance(detalle, list):
            print("⚠️ Error: 'detalle' no es una lista — omitido.\n")
            continue

        for item in detalle:
            if not isinstance(item, dict):
                print("⚠️ Error: item no es diccionario — omitido.")
                continue

            print(f" - {item['producto']} x{item['cantidad']} = ${item['subtotal']}")

        print()

    input("Presione ENTER para continuar...")

