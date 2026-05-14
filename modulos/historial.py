import csv
import os
from datetime import datetime

# Ruta de la carpeta del proyecto
base = os.path.dirname(os.path.dirname(__file__))

# Ruta del archivo historial
ruta_historial = os.path.join(base, "data", "historial_de_consultas.csv")

# GUARDAR HISTORIAL
def guardar_historial(consulta, cantidad_resultados):

    archivo_existe = os.path.isfile(ruta_historial)

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ruta_historial, "a", newline="", encoding="utf-8") as archivo:

        escritor = csv.writer(archivo)

        if not archivo_existe:
            escritor.writerow([
                "fecha",
                "consulta",
                "resultados"
            ])

        escritor.writerow([
            fecha_hora,
            consulta,
            cantidad_resultados
        ])

# MOSTRAR HISTORIAL

def mostrar_historial():

    try:

        with open(ruta_historial, "r", encoding="utf-8") as archivo:

            lector = csv.reader(archivo)

            print("\n========== HISTORIAL ==========\n")

            next(lector, None)  

            for fila in lector:

                fecha = fila[0]
                consulta = fila[1]
                resultados = fila[2]

                print(f"{fecha} | {consulta} | {resultados} resultados")

    except FileNotFoundError:

        print("\nNo existe historial todavía.")