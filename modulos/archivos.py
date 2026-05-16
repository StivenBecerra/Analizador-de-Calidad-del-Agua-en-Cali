import json
import os 

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
