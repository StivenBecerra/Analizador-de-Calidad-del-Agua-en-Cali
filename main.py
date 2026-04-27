from modulos import funciones
import os

base = os.path.dirname(__file__)
ruta = os.path.join(base, "data", "Agua_cali_2012_2018_Pequeño.csv")

if __name__ == "__main__":
    funciones.menu()
