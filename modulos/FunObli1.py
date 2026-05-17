import os
import csv

#GUARDAR RESULTADOS
def guardar_resultados(resultados):
    if not resultados:
        print("No hay resultados para guardar")
        return
    
    nombre=input("\nIngrese nombre del archivo: ")
    
    if not nombre.endswith(".csv"):
        nombre+=".csv"
     # Ruta de la carpeta del proyecto
    base = os.path.dirname(os.path.dirname(__file__))
    # Ruta del nuevo archivo resultados
    ruta_resultados = os.path.join(base, "data","Resultados_guardados", nombre)
    try:
      #Escribir csv
        with open(ruta_resultados,"x",newline="",encoding="utf-8") as archivo:
            escritor=csv.DictWriter(
                archivo,
                fieldnames=resultados[0].keys()
                delimiter=";"
            )

            escritor.writeheader()
            escritor.writerows(resultados)

        print(f"\nResultados guardados en {nombre}")
#No sobreescribir archivos existentes
    except FileExistsError:
        print("El archivo ya existe, porfavor ingrese otro nombre")
        guardar_resultados(resultados)
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
    #Ruta base
    base = os.path.dirname(os.path.dirname(__file__))
    # Ruta de la carpeta de resultados guardados
    ruta_resultadosguar = os.path.join(base, "data","Resultados_guardados")
    for archivo in os.listdir(ruta_resultadosguar):
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
#función que se llama para saber si el usuario guardara los datos o no
def ConfirmarGuard():
    Rta=limpiar_texto(input("¿Desea guardar resultados?"))
    if Rta=="si":
        return True
    elif Rta=="no":
        return False
    else:
       return -1
