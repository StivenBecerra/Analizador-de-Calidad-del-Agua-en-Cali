import csv
import os

#GUARDAR RESULTADOS
def guardar_resultados(resultados):
    if not resultados:
        print("No hay resultados para guardar")
        return

    nombre=input("\nIngrese nombre del archivo: ")

    if not nombre.endswith(".csv"):
        nombre+=".csv"

    try:
        with open(nombre,"w",newline="",encoding="utf-8") as archivo:
            escritor=csv.DictWriter(
                archivo,
                fieldnames=resultados[0].keys()
            )

            escritor.writeheader()
            escritor.writerows(resultados)

        print(f"\nResultados guardados en {nombre}")

    except:
        print("Error al guardar archivo")

#CARGAR RESULTADOS
def cargar_resultados(nombre_archivo):
    resultados=[]

    try:
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:
            lector=csv.DictReader(archivo)

            for fila in lector:
                resultados.append(fila)

        print(f"\nArchivo cargado correctamente")
        print(f"Registros encontrados: {len(resultados)}\n")

        for r in resultados:
            for clave,valor in r.items():
                print(f"{clave}: {valor}")

            print("="*30)

    except FileNotFoundError:
        print("Archivo no encontrado")

# ARCHIVOS
def ver_archivos_guardados():
    archivos=[]

    for archivo in os.listdir():
        if archivo.endswith(".csv"):
            archivos.append(archivo)

    if not archivos:
        print("\nNo hay archivos guardados")
        return

    print("\n ARCHIVOS GUARDADOS \n")

    for i,archivo in enumerate(archivos,start=1):
        print(f"{i}. {archivo}")

    try:
        opcion=int(input("\nSeleccione archivo: "))
        archivo_seleccionado=archivos[opcion-1]

        cargar_resultados(archivo_seleccionado)

    except:
        print("Opción inválida")
