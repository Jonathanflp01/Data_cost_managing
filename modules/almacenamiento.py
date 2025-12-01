import pandas as pd
from pathlib import Path
# import os
# import time
# import json

# inicio = time.time()


def estructurar_lista(lista):
    try:
        lista_est = {item["material"]: {
            "precio": item["precio"], "unidad": item["unidad"]} for item in lista}
        return lista_est
    except:
        return {}


def _obtener_rutas():
    """
    Función auxiliar para centralizar la configuración de rutas.
    Retorna una tupla con las rutas necesarias.
    """
    ruta_actual = Path(__file__).resolve().parent
    ruta_data = ruta_actual.parent / 'data'
    ruta_csv = ruta_data / 'materiales_db.csv'
    ruta_proyectos = ruta_data / 'proyectos'

    ruta_data.mkdir(exist_ok=True)
    ruta_proyectos.mkdir(parents=True, exist_ok=True)

    return ruta_csv, ruta_proyectos

# forma con libreria OS
# materials_data = os.path.join('..', 'data', 'materiales_db.csv')
# materials_df = pd.read_csv(materials_data)


def cargar_materiales():
    ruta_csv, _ = _obtener_rutas()
    try:
        if not ruta_csv.exists():
            print(f"Error: El archivo {ruta_csv} no existe.")
            return {}
        materiales_df = pd.read_csv(ruta_csv, sep=';')
        materiales_dic = materiales_df.to_dict(orient="records")
        return estructurar_lista(materiales_dic)
    except Exception as e:
        print(f"Ocurrió un error al intentar leer el archivo: {e}")
        return {}


def agregar_materiales(material, precio, unidad):
    if material in cargar_materiales():
        print(f"El material '{material}' ya existe en la base de datos.")
        return

    ruta_csv, _ = _obtener_rutas()

    try:
        n_material = {"material": material, "precio": precio, "unidad": unidad}
        nuevo_material_df = pd.DataFrame([n_material])

        modo = 'a' if ruta_csv.exists() else 'w'
        header = not ruta_csv.exists()

        nuevo_material_df.to_csv(
            ruta_csv, mode=modo, index=False, header=header, sep=";")
        return
    except Exception as e:
        print(f"Ocurrió un error al intentar escribir el archivo: {e}")


def editar_material(nombre_material_a_buscar, columna_a_editar, nuevo_valor):

    ruta_csv, _ = _obtener_rutas()

    try:
        lista_a_editar = pd.read_csv(ruta_csv, sep=";")
        if nombre_material_a_buscar not in lista_a_editar['material'].values:
            print(
                f"Error: No se encontró ningún material con el nombre '{nombre_material_a_buscar}'.")
            return False

        # busca el material a editar en la columna material
        filtro = lista_a_editar["material"] == nombre_material_a_buscar
        lista_a_editar.loc[filtro, columna_a_editar] = nuevo_valor
        lista_a_editar.to_csv(ruta_csv, index=False, sep=";")
        return
    except Exception as e:
        print(f"Ocurrió un error al intentar escribir el archivo: {e}")


def guardar_proyecto(nombre, datos):
    nombre_archivo = str(nombre+'.json')
    try:
        _, ruta_proyectos = _obtener_rutas()
        ruta_json = ruta_proyectos / nombre_archivo

        # Para trabajarlo con json puro
        # with open(ruta_json, 'w', encoding='utf-8') as archivo:
        # json.dump(datos, archivo, ensure_ascii=False, indent=4)

        # Con Pandas
        datos_pd = pd.DataFrame(datos)
        datos_pd.to_json(ruta_json, orient='records', indent=4)
        print(f'Se ha guardado satisfactoriamente el proyecto {nombre}')
    except Exception as e:
        print(f'Ha ocurrido un error al guardar el archivo: {e}')


def cargar_proyecto(nombre):
    _, ruta_proyectos = _obtener_rutas()
    ruta_proyecto = ruta_proyectos / (nombre + '.json')
    try:
        if not ruta_proyecto.exists():
            print("El proyecto no existe.")
            return []

        # Para trabajarlo con json puro
        # with open(ruta_proyecto, 'r', encoding='utf-8') as archivo:
        # datos = json.load(archivo)
        # return datos

        # Con Pandas
        proyecto_guardado = pd.read_json(
            ruta_proyecto, orient='records', encoding='utf-8')
        return proyecto_guardado.to_dict(orient='records')

    except Exception as e:
        print(f"Ocurrió un error al intentar escribir el archivo: {e}")


# Prueba de la función
# agregar_materiales("Tubo PVC 10 cm", 5.0, "m")
# lista = cargar_materiales()
# print(lista)
# editar_material("cemento", "precio", 0.19)
# lista = cargar_materiales()
# print(lista)

# fin = time.time()
# tiempo_ejecucion = fin - inicio
# print(f"El tiempo de ejecución fue de: {tiempo_ejecucion} segundos")
