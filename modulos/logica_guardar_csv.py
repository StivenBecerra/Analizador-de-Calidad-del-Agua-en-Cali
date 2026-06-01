import csv
import os
def guardar_resultados(resultados, nombre):

    if not resultados:
        return

    if not nombre.endswith(".csv"):
        nombre += ".csv"

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    data_dir = os.path.join(
        base_dir,
        "Data"
    )

    os.makedirs(
        data_dir,
        exist_ok=True
    )

    ruta_archivo = os.path.join(
        data_dir,
        nombre
    )

    with open(
        ruta_archivo,
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.DictWriter(
            archivo,
            fieldnames=resultados[0].keys()
        )

        escritor.writeheader()
        escritor.writerows(resultados)


def obtener_archivos_guardados():

    archivos = []

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    data_dir = os.path.join(
        base_dir,
        "Data"
    )

    os.makedirs(
        data_dir,
        exist_ok=True
    )

    for archivo in os.listdir(data_dir):

        if archivo.endswith(".csv"):

            archivos.append(archivo)

    return archivos

def cargar_resultados(nombre_archivo):

    resultados = []

    base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    data_dir = os.path.join(
        base_dir,
        "Data"
    )

    ruta_archivo = os.path.join(
        data_dir,
        nombre_archivo
    )

    try:

        with open(
            ruta_archivo,
            "r",
            encoding="utf-8"
        ) as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:
                resultados.append(fila)

    except FileNotFoundError:
        return []

    return resultados