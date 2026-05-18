# Analizador-de-Calidad-del-Agua-en-Cali
**Descripción**

DATALAB es un programa desarrollado en Python que permite cargar, consultar y analizar información almacenada en un archivo CSV desde la consola.

El sistema trabaja con el archivo: 
Agua_cali_2012_2018_Pequeño.csv

Su objetivo es facilitar la exploración de datos mediante un menú interactivo.

**Funciones principales**

Buscar registros

Permite buscar palabras o valores dentro de todos los registros del archivo y da la opción de guardar los resultados en un archivo CSV.

Ver estadísticas

Muestra las columnas y calcula estadísticas básicas de una columna numérica:

-Cantidad de datos

-Valor máximo

-Valor mínimo

-Promedio

Filtrar registros

Muestra los registros cuyo valor sea mayor al número ingresado por el usuario y permite guardar los resultados.

Agrupar por categoría

Cuenta cuántas veces aparece cada valor dentro de una columna de forma ordenada de mayor a menor y permite guardar los resultados.

Ver columnas disponibles

Muestra los nombres de todas las columnas del archivo CSV.

Ver historial

Permite ver el historial de las consultas realizadas durante la ejecución.

Ver archivos guardados

Muestra una lista de los archivos CSV guardados en la carpeta Data y permite cargar y ver su contenido.

Salir

Cierra el programa.

**Requisitos**

Python 3 o superior

Módulos nativos: json, os, csv, math, unicodedata

**Cómo ejecutar el programa**

Guardar el código en un archivo llamado: datalab.py

Tener el archivo CSV en la misma carpeta: Agua_cali_2012_2018_Pequeño.csv

Ejecutar en la terminal: python datalab.py

**Estructura del programa**

El programa está dividido en funciones:

-es_numero(): verifica si un valor es numérico

-generar_resumen(): genera un resumen automático del dataset con mínimos, máximos, promedios o valores únicos

-guardar_resumen_json(): guarda el resumen automáticamente en un archivo JSON dentro de la carpeta Data

-limpiar_texto(): normaliza texto eliminando acentos y mayúsculas para búsquedas

-cargar_datos(): carga el archivo CSV con codificación latin-1 y separador punto y coma

-mostrar_registro(): imprime registros con un formato legible

-columna_valida(): valida las columnas ingresadas y maneja equivalencias de nombres

-mostrar_columnas(): muestra los encabezados disponibles

-buscar(): busca coincidencias de texto en los registros y permite exportar a CSV

-estadisticas(): calcula las estadísticas de una columna numérica validada

-filtrar(): filtra registros por valores mayores al ingresado y permite exportar a CSV

-agrupar(): cuenta categorías de forma ordenada y permite guardar los resultados en un CSV

-guardar_resultados(): exporta listas de diccionarios a un archivo CSV en la carpeta Data

-cargar_resultados(): lee y muestra por consola un archivo guardado previamente

-ver_archivos_guardados(): indexa la carpeta Data, lista los archivos CSV y permite seleccionar uno para leerlo

-menu(): maneja el flujo del menú interactivo principal

**Tecnologías utilizadas**

-Python

-Manejo de archivos (CSV y JSON)

-Manejo de rutas del sistema (os)

-Listas, diccionarios y conjuntos (set)

-Funciones y modularización

**Autores**

-Jaider Stiven Becerra Muñoz

-Nicolas Serrano Cipriam

-María Alejandra Bermudez Poveda

-Francisco David Martínez Romero

-Juan Sebastian Tacuma Jimenez

-David Sebastian Lopez Tisoy

-Guillermo Andres Avila Barrera

-Nicole Andrea Lara Escorcia
