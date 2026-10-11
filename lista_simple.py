from nodos import Nodo

class ListaSimple:
    def __init__(self):
        self.cabeza = None    
        self.tamano = 0       

    def esta_vacia(self):
        return self.cabeza is None
    #True si no hay nodos/False si hay alguno

    # Permite saber el tamaño de la lista con len
    def __len__(self):
        return self.tamano

    # Borra todo: soltamos la cabeza y Python libera los nodos.
    def vaciar(self):
        self.cabeza = None
        self.tamano = 0

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        #El nuevo apunta al que era la cabeza y la cabeza ahora es el nuevo
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1 #Aumentamos 1 el tamaño de la lista

    def insertar_final(self, dato):
        # si está vacía, el nuevo es la cabeza
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None: #Recorremos la lista hasta que el siguiente sea None (último nodo)
                actual = actual.siguiente  
            # el último ahora apunta al nuevo
            actual.siguiente = nuevo
        self.tamano += 1

    def insertar_en(self, pos, dato):
        # la posición debe estar entre 0 y el tamaño de la lista
        if pos < 0 or pos > self.tamano:
            # raise "envia" un error para avisar que la posición no sirve
            raise IndexError(f"Posición inválida: {pos}. Debe estar entre 0 y {self.tamano}.")
        if pos == 0:
            self.insertar_inicio(dato)
            return  
        # buscamos el nodo ANTERIOR a la posición
        anterior = self.cabeza
        # for _ in range(n): repetir n veces; el _ es porque no usamos el número
        for _ in range(pos - 1):
            anterior = anterior.siguiente
        nuevo = Nodo(dato)
        nuevo.siguiente = anterior.siguiente    
        anterior.siguiente = nuevo
        self.tamano += 1

    # Devuelve True si lo borró y False si no lo encontró
    def eliminar(self, dato):
        # Si la lista esta vacía
        if self.esta_vacia():
            return False

        # Si el dato está en la cabeza
        if self.cabeza.dato == dato:
            # la cabeza pasa a ser el segundo nodo
            self.cabeza = self.cabeza.siguiente
            self.tamano -= 1 
            return True

        # Si no estaba en la cabeza
        anterior = self.cabeza
        while anterior.siguiente is not None:
            if anterior.siguiente.dato == dato:
                # el anterior "salta" el nodo y apunta al que sigue
                anterior.siguiente = anterior.siguiente.siguiente
                self.tamano -= 1
                return True
            anterior = anterior.siguiente
        # no se encontró
        return False

    # Devuelve la posición del dato
    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual is not None:    # mientras haya nodo que revisar
            if actual.dato == dato:
                return posicion 
            actual = actual.siguiente
            posicion += 1
        return -1

    def recorrer(self):
        return str(self) 

    def __str__(self):
        partes = []    # lista temporal SOLO de textos, no de nodos
        actual = self.cabeza
        while actual is not None:
            partes.append(str(actual.dato)) 
            actual = actual.siguiente
        partes.append("None")
        # join pega todos los textos poniendo "," entre cada uno
        return ",".join(partes)

    # Recorre del final al inicio
    def recorrer_inverso(self):
        if self.esta_vacia():
            return "None"
        partes = []    # lista temporal SOLO de textos
        self._recorrer_inverso_rec(self.cabeza, partes)
        return ",".join(partes)
    #Funcion de apoyo a recorrer_inverso() 
    def _recorrer_inverso_rec(self, nodo, partes):
        if nodo is None:    # si ya no hay más nodos,paramos
            return
        # primero vamos hasta el final y al regresar guardamos el dato, por eso sale al revés
        self._recorrer_inverso_rec(nodo.siguiente, partes)
        partes.append(str(nodo.dato))

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual is not None:
            # Guardamos el siguiente para no perderlo
            siguiente = actual.siguiente
            # El actual ahora apunta hacia atrás
            actual.siguiente = anterior
            # Anterior avanza al actual
            anterior = actual
            # Actual avanza al siguiente que guardamos
            actual = siguiente
        # el último nodo quedó en 'anterior': es la nueva cabeza
        self.cabeza = anterior

# ============================================================
# MENÚ: LISTA DE COMPRAS DEL MERCADO
# ============================================================

def menu():
    compras = ListaSimple()

    while True:    
        print("\n------ LISTA DE COMPRAS ------")
        print("1. Compra urgente (agregar al inicio)")
        print("2. Anotar producto (agregar al final)")
        print("3. Anotar producto en un puesto")
        print("4. Tachar producto ya comprado (eliminar)")
        print("5. ¿Ya anoté este producto? (buscar)")
        print("6. Ver lista")
        print("7. Leer de abajo hacia arriba (recorrer inverso)")
        print("8. Darle la vuelta a la lista (invertir)")
        print("9. Cargar mercado de ejemplo")
        print("0. Salir")
        opcion = input("Elige una opción: ")   

        if opcion == "1":
                producto = input("Producto urgente: ")
                compras.insertar_inicio(producto)
                print(producto, "quedó de primero.")

        elif opcion == "2":
                producto = input("Producto: ")
                compras.insertar_final(producto)
                print(producto, "se anotó al final.")

        elif opcion == "3":
                # el usuario cuenta desde 1, la lista desde 0: restamos 1
                # int() convierte el texto escrito en número
                puesto = int(input(f"Puesto (1 a {len(compras) + 1}): "))
                producto = input("Producto: ")
                compras.insertar_en(puesto - 1, producto)
                print(producto, "quedó en el puesto", puesto)

        elif opcion == "4":
                producto = input("Producto que ya compraste: ")
                if compras.eliminar(producto):    # entra aquí si eliminar devolvió True
                    print(producto, "tachado de la lista.")
                else:
                    print(producto, "no estaba en la lista.")

        elif opcion == "5":
                producto = input("Producto a buscar: ")
                pos = compras.buscar(producto)
                if pos == -1:
                    print(producto, "NO está anotado. ¡Que no se te olvide!")
                else:
                    # sumamos 1 para mostrar el puesto como lo cuenta una persona
                    print(producto, "está en el puesto", pos + 1)

        elif opcion == "6":
                print("Faltan", len(compras), "producto(s) por comprar.")

        elif opcion == "7":
                print("De abajo hacia arriba:", compras.recorrer_inverso())

        elif opcion == "8":
                compras.invertir()
                print("Lista invertida: ahora el último va primero.")

        elif opcion == "9":
                compras.vaciar()    # primero borramos lo que hubiera
                # recorremos cada producto del grupo y lo agregamos al final
                for producto in ("Arroz", "Leche", "Huevos", "Pan", "Café", "Panela", "Queso"):
                    compras.insertar_final(producto)
                print("Se cargó el mercado de ejemplo.")

        elif opcion == "0":
                print("¡Buen mercado!")
                break 
        else:
                print("Opción no válida.")

    print("Error: ese puesto no existe en la lista.")

    # después de cada acción mostramos la lista
    print("Lista:", compras)

#Lo ejecutamos solo si se llama directamente a este archivo, no si se importa
if __name__ == "__main__":
   menu()
