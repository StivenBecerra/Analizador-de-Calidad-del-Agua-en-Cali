import os
from modulos.funciones import cargar_datos

base = os.path.dirname(__file__)
ruta = os.path.join(base, "data", "Agua_cali_2012_2018_completo.csv")

#print("Ruta actual:", base)
#print("Ruta del archivo:", ruta)
#print("Contenido data:", os.listdir(os.path.join(base, "data")))   

datos = cargar_datos(ruta)


for i in range(1, len(datos)):
    try:
        datos[i][5] = float(datos[i][5]) / 100
    except:
        datos[i][5] = '' 

for i in range(1, len(datos)):
    try:
        datos[i][5] =str(datos[i][5]) 
    except:
        datos[i][5] = '' 


from modulos.funciones import buscar


termino = input("Ingrese el término a buscar: ")    
print(f"Buscando el término '{termino}' en el dataset...")
buscar(datos, termino)
print("\nBúsqueda finalizada.")
print("======================================================")
print("\nEstadisicas basicas")
from modulos.funciones import estadisticas
from modulos.funciones import pedir_parametro
print("\npH[-](Potencial de hidrogeno)\nDQO [mg/L](Demanda Química de Oxígeno)\nCE [µS/cm](Conductividad Eléctrica)\nSST [mg/L](Sólidos Suspendidos Totales)")


indice_columna = pedir_parametro()
estadisticas(datos, indice_columna)



