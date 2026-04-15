import csv

def parsear_linea(linea):
    return next(csv.reader([linea], delimiter=','))


def reparar_si_esta_mal(fila):
    if len(fila) == 1:
        return next(csv.reader([fila[0]], delimiter=','))
    return fila


def cargar_datos(ruta):
    datos = []

    with open(ruta, encoding="utf-8") as f:

        for linea in f:

            linea = linea.strip()

            if not linea:
                continue

            try:
                fila = parsear_linea(linea)
            except:
                continue

            fila = reparar_si_esta_mal(fila)

            # limpiar comillas
            fila = [c.strip().replace('"', '') for c in fila]

            # conservar vacíos
            fila = [c if c != '' else '' for c in fila]

            datos.append(fila)

    return datos
#=====================================================================

# FUNCION: BUSCAR
def buscar(datos, termino):
    resultados = []
    for fila in datos:
        if termino.lower() in ",".join(fila).lower():
            resultados.append(fila)

    print(f"\nSe encontraron {len(resultados)} registros:\n")
    for r in resultados:
        print(r)
# =====================================================================

# FUNCION: PEDIR PARAMETRO


def pedir_parametro():
   
    while True:
        parametro = input("Ingrese el parámetro [pH/DQO/CE/SST]: ")
        parametro = parametro.strip().upper()   
        if parametro in ["PH", "DQO", "CE", "SST"]:
            if parametro == "PH":
             indice_columna = 5
            elif parametro == "DQO":
             indice_columna = 6
            elif parametro == "CE":
             indice_columna = 7
            elif parametro== "SST":
             indice_columna = 8
            return indice_columna  
        else:
            print("Parámetro inválido, intenta de nuevo")

            
# FUNCION: ESTADISTICAS
# =====================================================================

def estadisticas(datos, indice_columna):
    valores = []
    filas = []

    for i in range(1, len(datos)):  
        valor = datos[i][indice_columna]

       
        if valor != "" :
            try:
                valor = float(valor)
                valores.append(valor)
                filas.append(i)
            except:
                pass

    maximo = max(valores)
    minimo = min(valores)

    fila_max = filas[valores.index(maximo)]
    fila_min = filas[valores.index(minimo)]

    promedio = sum(valores) / len(valores)

    if indice_columna == 5:
        print("\nEstadísticas para pH:")
    elif indice_columna == 6:
        print("\nEstadísticas para DQO:")
    elif indice_columna == 7:
        print("\nEstadísticas para CE:")
    elif indice_columna == 8:
        print("\nEstadísticas para SST:")

    print(f"\nMáximo: {maximo}")# (fila {fila_max})")
    print(f"Mínimo: {minimo}")# (fila {fila_min})")
    print(f"Promedio: {promedio}")

    