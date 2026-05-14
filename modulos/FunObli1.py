import os
def Guardarresults():
    Rta=limpiar_texto(input("¿Desea guardar resultados?"))
    if Rta=="si":
        # Ruta de la carpeta del proyecto
        base = os.path.dirname(os.path.dirname(__file__))
        nombre=input("¿Cómo se llamará el archivo?")
        # Ruta del nuevo archivo resultados
        ruta_resultados = os.path.join(base, "data", nombre, ".csv")
        try:
            with open(ruta_resultados, "x", newline="", encoding="utf-8") as archivo:
        except:
            

    elif Rta=="no":
        return 0
    else:
       return -1
