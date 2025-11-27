import pandas as pd
from pathlib import Path
# import os

# forma con libreria OS, método anterior
# materials_data = os.path.join('..', 'data', 'materiales_db.csv')
# materials_df = pd.read_csv(materials_data)


def cargar_materiales():
    ruta_actual = Path(__file__).resolve().parent
    ruta_data = ruta_actual.parent / 'data'
    ruta_csv = ruta_data / 'materiales_db.csv'
    try:
        materiales_df = pd.read_csv(ruta_csv)
        return materiales_df
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_csv} no se encontró.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {ruta_csv} está vacío.")
        return pd.DataFrame()


def agregar_materiales():
    return


# Prueba de la función
print(cargar_materiales())
