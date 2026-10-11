
# Guarda un dato y la referencia al nodo que sigue.
class Nodo:
    def __init__(self, dato):
        self.dato = dato 
        self.siguiente = None   

# Hereda de Nodo (dato y siguiente) y agrega el enlace al anterior.
class NodoDoble(Nodo):
    def __init__(self, dato):
        super().__init__(dato)    # crea dato y siguiente como en Nodo
        self.anterior = None 
