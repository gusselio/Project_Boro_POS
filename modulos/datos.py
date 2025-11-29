import json
import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))  # Ruta raíz del proyecto
DB_PATH = os.path.join(BASE_PATH, "database")


# -------------------- FUNCIONES DE ARCHIVOS JSON --------------------

def cargar_json(nombre_archivo):
    ruta = os.path.join(DB_PATH, nombre_archivo)
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def guardar_json(nombre_archivo, data):
    ruta = os.path.join(DB_PATH, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# -------------------- CARGA INICIAL DE DATOS --------------------

inventario = cargar_json("inventario.json")
recetas = cargar_json("recetas.json")
historial_ventas = cargar_json("historial_ventas.json")


# Si faltan archivos, créalos vacíos automáticamente
if inventario == {}:
    guardar_json("inventario.json", {})
if recetas == {}:
    guardar_json("recetas.json", {})
if historial_ventas == {}:
    guardar_json("historial_ventas.json", {})

# Stock inicial para detectar porcentajes
stock_inicial = inventario.copy()

# Diccionario compartido para notificaciones
notificaciones_compra = {}


# -------------------- FUNCIONES PARA GUARDAR CAMBIOS --------------------

def guardar_inventario():
    guardar_json("inventario.json", inventario)


def guardar_recetas():
    guardar_json("recetas.json", recetas)


def guardar_historial():
    guardar_json("historial_ventas.json", historial_ventas)
