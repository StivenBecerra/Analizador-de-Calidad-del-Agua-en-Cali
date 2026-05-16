
# VERIFICAR SI UN VALOR ES NUMÉRICO

def es_numero(valor):
    try:
        float(valor)
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

        if len(valores) > 0 and all(es_numero(v) for v in valores):
    return resumen
