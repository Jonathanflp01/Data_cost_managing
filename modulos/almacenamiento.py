import pandas as pd
from pathlib import Path
# import os
import time

# forma con libreria OS, método anterior
# materials_data = os.path.join('..', 'data', 'materiales_db.csv')
# materials_df = pd.read_csv(materials_data)
inicio = time.time()


def estructurar_lista(lista):
    try:
        lista_est = {item["material"]: {
            "precio": item["precio"], "unidad": item["unidad"]} for item in lista}
        return lista_est
    except:
        return {}


def cargar_materiales():
    ruta_actual = Path(__file__).resolve().parent
    ruta_data = ruta_actual.parent / 'data'
    ruta_csv = ruta_data / 'materiales_db.csv'
    try:
        materiales_df = pd.read_csv(ruta_csv, sep=';')
        materiales_dic = materiales_df.to_dict(orient="records")

        return materiales_dic
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_csv} no se encontró.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {ruta_csv} está vacío.")
        return pd.DataFrame()


def agregar_materiales():
    return


def cargar_proyecto(nombre):
    return


def guardar_proyecto(nombre, datos):
    return


# Prueba de la función

lista = cargar_materiales()

print(estructurar_lista(lista))


fin = time.time()
tiempo_ejecucion = fin - inicio
print(f"El tiempo de ejecución fue de: {tiempo_ejecucion} segundos")
