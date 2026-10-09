# ============================================================
# nodos.py
# Clases Nodo y NodoDoble: las "cajitas" que forman las listas.
#
# Asignatura: Estructuras de la Información
# Autores: [NOMBRE 1], [NOMBRE 2], [NOMBRE 3], [NOMBRE 4]
# ============================================================


# Nodo para la lista simple y la lista circular.
# Guarda un dato y la referencia al nodo que sigue.
class Nodo:
    def __init__(self, dato):
        self.dato = dato          # el valor que guarda el nodo
        self.siguiente = None     # al crearse no apunta a nadie


# Nodo para la lista doble.
# Hereda de Nodo (dato y siguiente) y agrega el enlace al anterior.
class NodoDoble(Nodo):
    def __init__(self, dato):
        super().__init__(dato)    # crea dato y siguiente como en Nodo
        self.anterior = None      # al crearse no apunta a nadie
