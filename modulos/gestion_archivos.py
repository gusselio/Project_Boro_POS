# modulos/gestion_archivos.py
import time
import os
import threading
import json
import queue
from datetime import datetime

# -----------------------------
#  Pedir usuario y bienvenida
# -----------------------------
def solicitar_usuario():
    usuario = input("Ingrese su nombre o nickname: ").strip()
    print(f"\nBienvenido al sistema, {usuario.upper()} \n")
    return usuario


# -----------------------------
#  Función con espera de carga
# -----------------------------
def mostrar_carga():
    print("Cargando sistema, por favor espere...")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\n")


# -----------------------------
#  Solicitar fecha y almacenarla
# -----------------------------
def pedir_fecha():
    while True:
        fecha_txt = input("Ingrese la fecha en formato DD/MM/AAAA: ").strip()
        try:
            dia, mes, anio = fecha_txt.split("/")
            fecha = (int(dia), int(mes), int(anio))
            return fecha
        except ValueError:
            print("⚠️ Formato incorrecto. Ejemplo: 12/06/2023")


def input_with_timeout(prompt: str, timeout: float):
    """
    Muestra prompt y espera input del usuario. Si el usuario no responde antes
    de `timeout` segundos, retorna None.
    """
    q = queue.Queue()

    def worker():
        try:
            s = input(prompt)
            q.put(s)
        except Exception:
            q.put(None)

    t = threading.Thread(target=worker, daemon=True)
    t.start()

    try:
        return q.get(timeout=timeout)
    except queue.Empty:
        return None


# -----------------------------
#  Leer archivo
# -----------------------------
def leer_archivo():
    print("\nArchivos disponibles en /database:")

    # Ruta a la carpeta database
    carpeta_db = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database")

    # Listar archivos json y txt dentro de /database
    archivos = [f for f in os.listdir(carpeta_db)
                if f.endswith(".txt") or f.endswith(".json")]

    if not archivos:
        print("No hay archivos .txt o .json disponibles en /database.")
        return

    # Mostrar archivos encontrados
    for i, nombre in enumerate(archivos, 1):
        print(f"{i}. {nombre}")

    try:
        opcion = int(input("Seleccione un archivo para abrir: "))
        archivo = archivos[opcion - 1]

        ruta_archivo = os.path.join(carpeta_db, archivo)

        print("\n--- CONTENIDO ---")

        # JSON → se imprime bonito
        if archivo.endswith(".json"):
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                contenido = json.load(f)
                print(json.dumps(contenido, indent=4, ensure_ascii=False))

        # TXT → se imprime normal
        else:
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                print(f.read())

        print("-----------------\n")

    except (IndexError, ValueError):
        print("⚠️ Opción inválida.")
    except FileNotFoundError:
        print("⚠️ Archivo no encontrado.")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")



# -----------------------------
#  Crear archivo
# -----------------------------
def crear_archivo(fecha):
    nombre_raw = input("Ingrese nombre del nuevo archivo (sin extensión): ").strip()
    if not nombre_raw:
        print("⚠️ Nombre vacío. Cancelando.")
        input("Presione Enter para volver al menú...")
        return

    nombre = f"{nombre_raw}.txt"
    if os.path.exists(nombre):
        print("⚠️ Ya existe un archivo con ese nombre.")
        opcion = input("¿Desea sobrescribirlo? (si/no): ").strip().lower()
        if opcion != "si":
            print("Operación cancelada.")
            input("Presione Enter para volver al menú...")
            return

    contenido = input("Escriba el contenido inicial: ")

    try:
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(f"Fecha: {fecha}\n")
            f.write(contenido)
        print(f"✔ Archivo '{nombre}' creado correctamente.\n")
    except Exception as e:
        print(f"⚠️ Error al crear el archivo: {e}")

    input("Presione Enter para volver al menú...")


# -----------------------------
#  Escribir en archivo existente
# -----------------------------
def escribir_archivo(fecha):
    nombre = input("Nombre del archivo a modificar (incluya .txt): ").strip()

    if not os.path.exists(nombre):
        print("⚠️ Ese archivo no existe.")
        opcion = input("¿Deseas crearlo? (si/no): ").strip().lower()
        if opcion == "si":
            crear_archivo(fecha)
        else:
            input("Presione Enter para volver al menú...")
        return

    try:
        with open(nombre, "a", encoding="utf-8") as f:
            texto = input("Ingrese el texto a agregar: ")
            f.write(f"\n[{fecha}] {texto}")
        print("✔ Se agregó texto correctamente.")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

    input("Presione Enter para volver al menú...")


# -----------------------------
#  Menú en forma de MATRIZ
# -----------------------------
def mostrar_menu_matriz():
    print("""
====== GESTIÓN DE ARCHIVOS ======

    [1] Leer archivo          |    [2] Crear archivo
    [3] Escribir archivo      |    [4] Cambiar usuario
    [5] Editar inventario     |    [6] Editar recetas
    [7] Salir al menú

""")

# -----------------------------
#  Editar inventario función
# -----------------------------
def editar_inventario():
    from modulos.datos import cargar_json, guardar_json

    inventario = cargar_json("inventario.json")

    print("\n=== INVENTARIO ACTUAL ===")
    for item, cantidad in inventario.items():
        print(f"- {item}: {cantidad}")

    producto = input("\nIngrese el producto a modificar: ")

    if producto not in inventario:
        print("❌ Ese producto no existe.")
        return

    try:
        nueva_cantidad = int(input("Nueva cantidad: "))
        inventario[producto] = nueva_cantidad
        guardar_json("inventario.json", inventario)
        print("✔ Inventario actualizado correctamente.")
    except ValueError:
        print("❌ Debe ingresar un número.")


# -----------------------------
#  Editar Recetas función
# -----------------------------
def editar_recetas():
    from modulos.datos import cargar_json, guardar_json

    recetas = cargar_json("recetas.json")

    print("\n=== RECETAS ===")
    for categoria, items in recetas.items():
        print(f"\n[{categoria}]")
        for producto, data in items.items():
            precio = data.get("Precio", "N/D")
            insumos = data.get("Insumos", "No definidos")
            print(f" - {producto}: Precio ${precio}, Insumos: {insumos}")

    producto = input("\nIngrese el nombre del producto a modificar: ")

    # Buscar producto en la estructura
    encontrado = None
    for categoria, items in recetas.items():
        if producto in items:
            encontrado = (categoria, items[producto])
            break

    if not encontrado:
        print("❌ Producto no encontrado.")
        return

    categoria, info = encontrado

    print("\n¿Qué desea modificar?")
    print("[1] Precio")
    print("[2] Insumos")
    opcion = input("Seleccione: ")

    if opcion == "1":
        try:
            nuevo_precio = float(input("Nuevo precio: "))
            recetas[categoria][producto]["Precio"] = nuevo_precio
        except ValueError:
            print("❌ Precio inválido.")
            return

    elif opcion == "2":
        print("Formato: insumo1:10, insumo2:5")
        texto = input("Nuevos insumos: ")
        try:
            nuevos_insumos = {}
            pares = texto.split(",")
            for par in pares:
                nombre, cantidad = par.split(":")
                nuevos_insumos[nombre.strip()] = int(cantidad.strip())

            recetas[categoria][producto]["Insumos"] = nuevos_insumos
        except:
            print("❌ Error en formato de insumos.")
            return
    else:
        print("❌ Opción inválida.")
        return

    guardar_json("recetas.json", recetas)
    print("✔ Receta actualizada correctamente.")


# -----------------------------
#  Esperar opción (usa timeout real)
# -----------------------------
def esperar_opcion(timeout_seconds: int = 600):
    """
    Devuelve la cadena ingresada por el usuario antes del timeout.
    Si no responde en `timeout_seconds`, retorna None.
    """
    print(f"⏳ Tienes {timeout_seconds//60} minutos para elegir una opción...")
    respuesta = input_with_timeout("Ingrese opción (o presione Enter para mostrar prompt directo): ", timeout_seconds)
    return respuesta


# -----------------------------
#  FUNCIÓN PRINCIPAL DEL MÓDULO
# -----------------------------
def gestion_archivos():
    usuario = solicitar_usuario()
    mostrar_carga()
    fecha = pedir_fecha()

    while True:
        mostrar_menu_matriz()

        respuesta = esperar_opcion(600)  # 600 seg = 10 min

        # Si retorna None => timeout expiró
        if respuesta is None:
            seguir = input("\nNo hubo respuesta en 10 minutos. ¿Deseas continuar? (si/no): ").strip().lower()
            if seguir != "si":
                print("Regresando a la pantalla inicial...\n")
                return
            # si desea continuar, simplemente volver al inicio del while (se muestra menú)
            continue

        # Si el usuario escribió algo, usamos esa respuesta
        respuesta = respuesta.strip()
        if respuesta == "":
            # si presionó Enter en el input_with_timeout, pedimos ahora la opción normal
            try:
                opcion = int(input("Seleccione una opción (número): ").strip())
            except ValueError:
                print("⚠️ Debes escribir un número.\n")
                continue
        else:
            # la respuesta ya trae lo que tecleó el usuario
            if not respuesta.isdigit():
                print("⚠️ Debes escribir un número.\n")
                continue
            opcion = int(respuesta)

        match opcion:
            case 1:
                leer_archivo()
            case 2:
                crear_archivo(fecha)
            case 3:
                escribir_archivo(fecha)
            case 4:
                usuario = solicitar_usuario()
            case 5:
                editar_inventario()
            case 6:
                editar_recetas()
            case 7:
                print("Saliendo del módulo…\n")
                return
            case _:
                print("⚠️ Opción inválida.\n")
