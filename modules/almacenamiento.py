import pandas as pd
from pathlib import Path
# import os
# import time

# inicio = time.time()


def estructurar_lista(lista):
    try:
        lista_est = {item["material"]: {
            "precio": item["precio"], "unidad": item["unidad"]} for item in lista}
        return lista_est
    except:
        return {}

# forma con libreria OS
# materials_data = os.path.join('..', 'data', 'materiales_db.csv')
# materials_df = pd.read_csv(materials_data)


def cargar_materiales():
    ruta_actual = Path(__file__).resolve().parent
    ruta_data = ruta_actual.parent / 'data'
    ruta_csv = ruta_data / 'materiales_db.csv'
    try:
        materiales_df = pd.read_csv(ruta_csv, sep=';')
        materiales_dic = materiales_df.to_dict(orient="records")
        materiales_est = estructurar_lista(materiales_dic)
        return materiales_est
    except FileNotFoundError:
        print(
            f"Error: No se encontró el directorio o archivo en la ruta: {ruta_csv}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {ruta_csv} está vacío.")
        return pd.DataFrame()


def agregar_materiales(material, precio, unidad):
    ruta_actual = Path(__file__).resolve().parent
    ruta_data = ruta_actual.parent / 'data'
    ruta_csv = ruta_data / 'materiales_db.csv'
    try:
        n_material = {"material": material, "precio": precio, "unidad": unidad}
        nuevo_material_df = pd.DataFrame([n_material])
        nuevo_material_df.to_csv(
            ruta_csv, mode="a", index=False, header=False, sep=";")
        return
    except FileNotFoundError:
        print(
            f"Error: No se encontró el directorio o archivo en la ruta: {ruta_csv}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Ocurrió un error al intentar escribir el archivo: {e}")


def editar_material(nombre_material_a_buscar, columna_a_editar, nuevo_valor):
    ruta_actual = Path(__file__).resolve().parent
    ruta_data = ruta_actual.parent / 'data'
    ruta_csv = ruta_data / 'materiales_db.csv'
    try:
        lista_a_editar = pd.read_csv(ruta_csv, sep=";")
        # busca el material a editar en la columna material
        filtro = lista_a_editar["material"] == nombre_material_a_buscar
        if lista_a_editar[filtro].empty:
            print(
                f"Error: No se encontró ningún material con el nombre '{nombre_material_a_buscar}'.")
            return False
        lista_a_editar.loc[filtro, columna_a_editar] = nuevo_valor
        lista_a_editar.to_csv(ruta_csv, index=False, sep=";")
        return
    except FileNotFoundError:
        print(
            f"Error: No se encontró el directorio o archivo en la ruta: {ruta_csv}")
        return pd.DataFrame()
    except KeyError:
        print(
            f"Error: La columna '{columna_a_editar}' o 'material' no existe en el CSV.")
        return False
    except Exception as e:
        print(f"Ocurrió un error al intentar escribir el archivo: {e}")


def cargar_proyecto(nombre):
    return


def guardar_proyecto(nombre, datos):
    return


# Prueba de la función
# agregar_materiales("Tubo PVC 10 cm", 5.0, "m")
lista = cargar_materiales()
print(lista)
editar_material("cemento", "precio", 0.19)
lista = cargar_materiales()
print(lista)


# fin = time.time()
# tiempo_ejecucion = fin - inicio
# print(f"El tiempo de ejecución fue de: {tiempo_ejecucion} segundos")
