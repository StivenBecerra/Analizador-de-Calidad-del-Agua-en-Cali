import math
# VERIFICAR SI ES NÚMERO
def es_numero(valor):

    try:
        numero = float(valor)
        if math.isnan(numero):
            return False
        return True

    except:
        return False

# GENERAR RESUMEN DEL DATASET
def generar_resumen(datos):

    resumen = {}

    # TOTAL DE REGISTROS
    resumen["total_registros"] = len(datos)
    # VALIDAR DATOS
    if len(datos) == 0:
        return resumen

    columnas = datos[0].keys()

    # RECORRER COLUMNAS

    for columna in columnas:

        valores = []

        for fila in datos:

            valor = fila[columna]

            if valor != "":
                valores.append(valor)
        # COLUMNAS NUMÉRICAS
        if (
            len(valores) > 0
            and all(es_numero(v) for v in valores)
        ):

            numeros = []

            for v in valores:
                numeros.append(float(v))

            resumen[columna] = {

                "minimo": min(numeros),

                "maximo": max(numeros),

                "promedio": round(
                    sum(numeros) / len(numeros),
                    2
                )
            }

        # COLUMNAS DE TEXTO

        else:

            unicos = set(valores)

            resumen[columna] = {

                "valores_unicos": len(unicos)

            }

    return resumen
