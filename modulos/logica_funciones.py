import unicodedata
from modulos import historial
import math

# LIMPIAR TEXTO
def limpiar_texto(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto


# CARGAR DATOS
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

        return datos

    except FileNotFoundError:

        return []


# VALIDAR COLUMNA
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

    return equivalencias.get(columna)


# COLUMNAS DISPONIBLES
def mostrar_columnas(datos):

    if not datos:
        return []

    return list(datos[0].keys())


# BUSCAR
def buscar(datos, termino):

    termino = limpiar_texto(termino)

    resultados = []

    for registro in datos:

        texto = " ".join(str(v) for v in registro.values())
        texto = limpiar_texto(texto)

        if termino in texto:

            resultados.append(registro)

    consulta = f"Búsqueda general: {termino}"

    historial.guardar_historial(
        consulta,
        len(resultados)
    )

    return resultados


# FILTRAR
def filtrar(datos, columna, valor):

    columna_real = columna_valida(
        datos,
        columna
    )

    if columna_real is None:
        return []

    resultados = []

    for registro in datos:

        try:

            if float(registro[columna_real]) > float(valor):

                resultados.append(registro)

        except:

            continue

    consulta = f"Filtro {columna_real} > {valor}"

    historial.guardar_historial(
        consulta,
        len(resultados)
    )

    return resultados


# AGRUPAR
def agrupar(datos, columna):

    columna_real = columna_valida(
        datos,
        columna
    )

    if columna_real is None:
        return []

    conteo = {}

    for registro in datos:

        valor = registro[columna_real]

        conteo[valor] = conteo.get(
            valor,
            0
        ) + 1

    ordenado = sorted(
        conteo.items(),
        key=lambda x: x[1],
        reverse=True
    )

    resultados = []

    for valor, cantidad in ordenado:

        resultados.append({
            columna_real: valor,
            "Cantidad": cantidad
        })

    consulta = f"Agrupar por {columna_real}"

    historial.guardar_historial(
        consulta,
        len(resultados)
    )

    return resultados


# ESTADÍSTICAS
def estadisticas(datos, columna):

    columna_real = columna_valida(
        datos,
        columna
    )

    if columna_real is None:
        return None

    valores = []

    for registro in datos:

        try:

            numero = float(
                registro[columna_real]
            )

            if not math.isnan(numero):

                valores.append(numero)

        except:

            continue

    if not valores:

        return None

    resultado = {

        "cantidad": len(valores),

        "maximo": max(valores),

        "minimo": min(valores),

        "promedio": (
            sum(valores) / len(valores)
        )
    }

    consulta = f"Estadísticas de {columna_real}"

    historial.guardar_historial(
        consulta,
        len(valores)
    )

    return resultado