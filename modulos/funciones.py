import unicodedata
from modulos import historial
from modulos.analisis import generar_resumen
from modulos.archivos import guardar_resumen_json
from modulos import guardar_csv 
import math


#LIMPIAR TEXTO
def limpiar_texto(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

#CARGAR DATOS
def cargar_datos(ruta):
    datos = []
    try:
        with open(ruta, "r", encoding="latin-1") as archivo:
            encabezados = archivo.readline().strip().split(";")

            for linea in archivo:
                valores = linea.strip().split(";")

                if len(valores) == len(encabezados):
                    registro = dict(zip(encabezados, valores))
                    datos.append(registro)

        print(f"\nDatos cargados correctamente: {len(datos)} registros\n")
        return datos

    except FileNotFoundError:
        print("Error: archivo no encontrado")
        return []

#MOSTRAR REGISTRO
def mostrar_registro(registro):
    for clave, valor in registro.items():
        print(f"{clave}: {valor}")
    print("=" * 30)

#VALIDAR COLUMNA
def columna_valida(datos, columna):

    equivalencias = {
        "ano": "Ano",
        "año": "Ano",
        "fecha": "Fecha",
        "punto": "Punto de muestreo",
        "punto de muestreo": "Punto de muestreo",
        "rio": "Rio",
        "od": "OD (%)",
        "ph": "pH",
        "dqo": "DQO (mg/L)",
        "ce": "CE (microS/cm)",
        "sst": "SST (mg/L)"
    }

    columna = columna.lower().strip()

    if columna in equivalencias:
        return equivalencias[columna]

    print("Error: columna no válida")
    return None

#MOSTRAR COLUMNAS
def mostrar_columnas(datos):
    print("\nColumnas disponibles:")
    for col in datos[0].keys():
        print(f"- {col}")

#BUSCAR
def buscar(datos):  
    termino = limpiar_texto(input("\nIngrese término de búsqueda: "))
    resultados = []

    for registro in datos:
        texto = " ".join(str(v) for v in registro.values())
        texto = limpiar_texto(texto)

        if termino in texto:
            resultados.append(registro)

    print(f"\nSe encontraron {len(resultados)} registros\n")
    
    consulta = f"Búsqueda general: {termino}"
    historial.guardar_historial(consulta, len(resultados))

    if resultados:
        for r in resultados:
            mostrar_registro(r)
        guardar = input("\n¿Desea guardar resultados? (s/n): ")
        if guardar.lower() == "s":
            guardar_csv.guardar_resultados(resultados)
    else:
        print("No se encontraron coincidencias")

#ESTADÍSTICAS
def estadisticas(datos):
    columna = input("\nIngrese nombre de la columna: ")

    columna_real = columna_valida(datos, columna)

    if columna_real is None:
        return

    valores = []

    for registro in datos:
        try:
            if not math.isnan(float(registro[columna_real])):
                valores.append(float(registro[columna_real]))
        except:
            continue

    if valores:
        print(f"\n--- Estadísticas de {columna_real} ---")
        print(f"Cantidad de datos: {len(valores)}")
        print(f"Máximo: {max(valores)}")
        print(f"Mínimo: {min(valores)}")
        print(f"Promedio: {sum(valores)/len(valores):.2f}")
        consulta = f"Estadísticas de {columna_real}"
        historial.guardar_historial(consulta, len(valores))
    else:
        print("No hay datos numéricos en esa columna")

#FILTRAR
def filtrar(datos):
    columna = input("\nIngrese columna: ")

    columna_real = columna_valida(datos, columna)

    if columna_real is None:
        return

    try:
        valor = float(input("Ingrese valor mínimo: "))
    except:
        print("Error: debe ingresar un número válido")
        return

    resultados = []

    for registro in datos:
        try:
            if float(registro[columna_real]) > valor:
                resultados.append(registro)
        except:
            continue

    print(f"\nSe encontraron {len(resultados)} registros\n")
    consulta = f"Filtro {columna_real} > {valor}"
    historial.guardar_historial(consulta, len(resultados))

    if resultados:
        for r in resultados:
            mostrar_registro(r)
        guardar = input("\n¿Desea guardar resultados? (s/n): ")
        if guardar.lower() == "s":
            guardar_csv.guardar_resultados(resultados)
    else:
        print("No hay resultados")

#AGRUPAR
def agrupar(datos):
    columna = input("\nIngrese la columna para agrupar: ")

    columna_real = columna_valida(datos, columna)

    if columna_real is None:
        return

    conteo = {}

    for registro in datos:
        valor = registro[columna_real]

        if valor in conteo:
            conteo[valor] += 1
        else:
            conteo[valor] = 1

    print("\n--- Conteo por categoría ---\n")

    consulta = f"Agrupar por {columna_real}"
    historial.guardar_historial(consulta, len(conteo))
   
    ordenado = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

    for valor, cantidad in ordenado:
        print(f"{valor}: {cantidad}")
    historial.guardar_historial(consulta,len(conteo))

    guardar = input("\n¿Desea guardar resultados? (s/n): ")

    if guardar.lower() == "s":

        resultados = []

        for valor, cantidad in ordenado:

            resultados.append({columna_real: valor, "Cantidad": cantidad})
        guardar_csv.guardar_resultados(resultados)
        
#MENÚ PRINCIPAL
def menu(ruta):
    datos = cargar_datos(ruta)
    # RESUMEN AUTOMÁTICO DEL DATASET
    resumen = generar_resumen(datos)

    guardar_resumen_json(resumen)

    print("Resumen del dataset generado correctamente")

    if not datos:
        return

    while True:
        print("\n========== DATALAB ==========")
        print("1. Buscar registros")
        print("2. Ver estadísticas")
        print("3. Filtrar registros")
        print("4. Agrupar por categoría")
        print("5. Ver columnas disponibles")
        print("6. Ver historial")
        print("7. Ver archivos guardados")
        print("8. Salir")
        print("=============================")

        opcion = input("Seleccione una opción (ejm: 1): ")

        if opcion == "1":
            buscar(datos)

        elif opcion == "2":
            mostrar_columnas(datos)
            estadisticas(datos)

        elif opcion == "3":
            mostrar_columnas(datos)
            filtrar(datos)

        elif opcion == "4":
            mostrar_columnas(datos)
            agrupar(datos)

        elif opcion == "5":
            mostrar_columnas(datos)

        elif opcion == "6":
            historial.mostrar_historial()

        elif opcion == "7":
            guardar_csv.ver_archivos_guardados()

        elif opcion == "8":
            print("\nSaliendo del programa...\n")
            break

        else:
            print("Opción inválida")
