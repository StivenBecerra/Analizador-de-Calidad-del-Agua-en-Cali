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

        # GUARDAR SOLO NÚMEROS VÁLIDOS
        numeros = []

        for v in valores:

            if es_numero(v):
                numeros.append(float(v))

        # COLUMNAS NUMÉRICAS
        if len(numeros) > 0:

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
