import json
import os 
import csv
# GUARDAR RESUMEN EN JSON
def guardar_resumen_json(
    resumen,
    nombre_archivo="resumen_dataset.json"
):

    # Ruta de la carpeta principal del proyecto
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Ruta de la carpeta Data
    data_dir = os.path.join(base_dir, "Data")

    # Crear la carpeta si no existe
    os.makedirs(data_dir, exist_ok=True)

    # Ruta completa del archivo JSON
    ruta_archivo = os.path.join(data_dir, nombre_archivo)

    with open(
        ruta_archivo,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            resumen,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    print(
        f"\nResumen guardado en {nombre_archivo}\n"
    )

# EXPORTAR RESULTADOS CSV
def exportar_resultados_csv(
    datos,
    ruta_archivo
):

    if not datos:
        print("No hay datos para exportar")
        return

    columnas = datos[0].keys()

    with open(
        ruta_archivo,
        mode="w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        escritor = csv.DictWriter(
            archivo,
            fieldnames=columnas
        )

        escritor.writeheader()

        for fila in datos:
            escritor.writerow(fila)

    print("Archivo CSV exportado correctamente")
