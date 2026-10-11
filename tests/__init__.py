# Este archivo convierte la carpeta tests en un "paquete" de Python.
# Las líneas de abajo agregan la carpeta del proyecto a la ruta de búsqueda,
# para que las pruebas encuentren lista_simple.py, lista_doble.py, etc.
import os
import sys

carpeta_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if carpeta_proyecto not in sys.path:
    sys.path.insert(0, carpeta_proyecto)
