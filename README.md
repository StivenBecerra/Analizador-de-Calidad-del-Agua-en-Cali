# Analizador-de-Calidad-del-Agua-en-Cali
Descripción

DATALAB es un programa desarrollado en Python que permite cargar, consultar y analizar información almacenada en un archivo CSV desde la consola.

El sistema trabaja con el archivo:

Agua_cali_2012_2018_Pequeño.csv

Su objetivo es facilitar la exploración de datos mediante un menú interactivo.

Funciones principales

**Buscar registros**

Permite buscar palabras o valores dentro de todos los registros del archivo.

**Ver estadísticas**

Calcula estadísticas básicas de una columna numérica:

-Cantidad de datos

-Valor máximo

-Valor mínimo

-Promedio

**Filtrar registros**

Muestra los registros cuyo valor sea mayor al número ingresado por el usuario.

**Agrupar por categoría**

Cuenta cuántas veces aparece cada valor dentro de una columna.

**Ver columnas disponibles**

Muestra los nombres de todas las columnas del archivo CSV.

**Salir**

Cierra el programa.

**Requisitos**

Python 3 o superior

**Cómo ejecutar el programa**

1. Guardar el código en un archivo llamado:
datalab.py

2. Tener el archivo CSV en la misma carpeta:
Agua_cali_2012_2018_Pequeño.csv

3. Ejecutar en la terminal:
python datalab.py

**Estructura del programa**

El programa está dividido en funciones:

-limpiar_texto(): normaliza texto para búsquedas

-cargar_datos(): carga el archivo CSV

-mostrar_registro(): imprime registros

-columna_valida(): valida columnas

-mostrar_columnas(): muestra encabezados

-buscar(): busca coincidencias

-estadisticas(): calcula estadísticas

-filtrar(): filtra valores numéricos

-agrupar(): cuenta categorías

-menu(): menú principal

**Tecnologías utilizadas**

-Python

-Manejo de archivos

-Listas

-Diccionarios

-Funciones

**Autores**

-Jaider Becerra

-Nicolas Serrano

-María Bermudez

-Francisco Martínez

-Juan Tucuma

-David Lopez

-Guillermo Avila

-Nicole Lara
