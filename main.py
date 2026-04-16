import unicodedata
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
            encabezados = archivo.readline().strip().split(",")

            for linea in archivo:
                valores = linea.strip().split(",")

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
    if columna in datos[0]:
        return True
    else:
        print("Error: columna no válida")
        return False


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

    if resultados:
        for r in resultados:
            mostrar_registro(r)
    else:
        print("No se encontraron coincidencias")


#ESTADÍSTICAS
def estadisticas(datos):
    columna = input("\nIngrese nombre de la columna: ")

    if not columna_valida(datos, columna):
        return

    valores = []

    for registro in datos:
        try:
            valores.append(float(registro[columna]))
        except:
            continue

    if valores:
        print("\n--- Estadísticas ---")
        print(f"Cantidad de datos: {len(valores)}")
        print(f"Máximo: {max(valores)}")
        print(f"Mínimo: {min(valores)}")
        print(f"Promedio: {sum(valores)/len(valores):.2f}")
    else:
        print("No hay datos numéricos en esa columna")


#FILTRAR
def filtrar(datos):
    columna = input("\nIngrese columna: ")

    if not columna_valida(datos, columna):
        return

    try:
        valor = float(input("Ingrese valor mínimo: "))
    except:
        print("Error: debe ingresar un número válido")
        return

    resultados = []

    for registro in datos:
        try:
            if float(registro[columna]) > valor:
                resultados.append(registro)
        except:
            continue

    print(f"\nSe encontraron {len(resultados)} registros\n")

    if resultados:
        for r in resultados:
            mostrar_registro(r)
    else:
        print("No hay resultados")


#AGRUPAR
def agrupar(datos):
    columna = input("\nIngrese la columna para agrupar: ")

    if not columna_valida(datos, columna):
        return

    conteo = {}

    for registro in datos:
        valor = registro[columna]

        if valor in conteo:
            conteo[valor] += 1
        else:
            conteo[valor] = 1

    print("\n--- Conteo por categoría ---\n")

    ordenado = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

    for valor, cantidad in ordenado:
        print(f"{valor}: {cantidad}")


#MENÚ PRINCIPAL
def menu():
    datos = cargar_datos("Agua_cali_2012_2018_Pequeño.csv")

    if not datos:
        return

    while True:
        print("\n========== DATALAB ==========")
        print("1. Buscar registros")
        print("2. Ver estadísticas")
        print("3. Filtrar registros")
        print("4. Agrupar por categoría")
        print("5. Ver columnas disponibles")
        print("6. Salir")
        print("=============================")

        opcion = input("Seleccione una opción: ")

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
            print("\nSaliendo del programa...\n")
            break

        else:
            print("Opción inválida")


# 
menu()