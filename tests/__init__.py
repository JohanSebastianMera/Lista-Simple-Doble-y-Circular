"""Paquete de pruebas unitarias del proyecto de listas enlazadas.

Agrega la carpeta raíz del proyecto al ``sys.path`` para que las pruebas
puedan importar ``nodos``, ``lista_simple``, ``lista_doble`` y
``lista_circular`` sin importar desde dónde se ejecuten.

Asignatura: Estructuras de la Información.
Autores: [NOMBRE 1], [NOMBRE 2], [NOMBRE 3], [NOMBRE 4].
"""

import os
import sys

RAIZ_PROYECTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if RAIZ_PROYECTO not in sys.path:
    sys.path.insert(0, RAIZ_PROYECTO)
