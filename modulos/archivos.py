import csv
import json

# CARGAR DATOS DESDE CSV
def cargar_datos_csv(ruta):
    datos = []

    try:
        with open(ruta, "r", encoding="latin-1") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                datos.append(fila)

        print(f"
Datos cargados correctamente: {len(datos)} registros
")
        return datos

    except FileNotFoundError:
        print("Error: archivo no encontrado")
        return []

# GUARDAR RESUMEN EN JSON

def guardar_resumen_json(resumen, nombre_archivo="resumen_dataset.json"):

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(resumen, archivo, indent=4, ensure_ascii=False)

    print(f"
Resumen guardado en {nombre_archivo}
")
