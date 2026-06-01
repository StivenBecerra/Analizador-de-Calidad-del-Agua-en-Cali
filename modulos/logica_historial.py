import csv
import os
from datetime import datetime

# Ruta de la carpeta del proyecto
base = os.path.dirname(os.path.dirname(__file__))

# Ruta del archivo historial
ruta_historial = os.path.join(base, "data", "historial_de_consultas.csv")

def obtener_historial():

    datos = []

    try:

        with open(
            ruta_historial,
            "r",
            encoding="utf-8"
        ) as archivo:

            lector = csv.DictReader(
                archivo
            )

            for fila in lector:
                datos.append(fila)

    except FileNotFoundError:
        pass

    return datos