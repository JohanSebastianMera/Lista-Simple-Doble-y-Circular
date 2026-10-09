# Traemos la clase Nodo del archivo nodos.py para poder crear nodos aquí
from nodos import Nodo

class ListaSimple:
    # Crea la lista vacía: no hay cabeza y el tamaño es 0.
    # __init__ se ejecuta solo cuando escribimos ListaSimple()
    def __init__(self):
        self.cabeza = None    # None = "nada", todavía no hay primer nodo
        self.tamano = 0       # contador de cuántos productos hay

    # ¿La lista está vacía?
    def esta_vacia(self):
        return self.cabeza is None
    #True si no hay nodos/False si hay alguno

    # Permite saber el tamaño de la lista con len
    # (gracias a este método podemos escribir len(compras))
    def __len__(self):
        return self.tamano

    # Borra todo: soltamos la cabeza y Python libera los nodos.
    def vaciar(self):
        self.cabeza = None
        self.tamano = 0

    # Agrega un dato al inicio
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)    # creamos la "cajita" con el dato
        # 1. el nuevo apunta al que era la cabeza y la cabeza ahora es el nuevo
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamano += 1      # += 1 es lo mismo que tamano = tamano + 1

    # Agrega un dato al final
    def insertar_final(self, dato):
        # si está vacía, el nuevo es la cabeza
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza    # empezamos a caminar desde el primero
            # avanzamos hasta el último (el que apunta a None)
            while actual.siguiente is not None:
                actual = actual.siguiente    # pasamos al siguiente nodo
            # el último ahora apunta al nuevo
            actual.siguiente = nuevo
        self.tamano += 1

    # Agrega un dato en la posición pos
    def insertar_en(self, pos, dato):
        # la posición debe estar entre 0 y el tamaño de la lista
        if pos < 0 or pos > self.tamano:
            # raise "lanza" un error a propósito para avisar que la posición no sirve
            # la f antes de las comillas permite meter variables dentro de { }
            raise IndexError(f"Posición inválida: {pos}. Debe estar entre 0 y {self.tamano}.")
        if pos == 0:
            self.insertar_inicio(dato)
            return    # return sin nada: salimos del método aquí mismo
        # buscamos el nodo ANTERIOR a la posición (avanzamos pos - 1 veces)
        anterior = self.cabeza
        # for _ in range(n): repetir n veces; el _ es porque no usamos el número
        for _ in range(pos - 1):
            anterior = anterior.siguiente
        nuevo = Nodo(dato)
        nuevo.siguiente = anterior.siguiente    # el nuevo se engancha al que seguía
        anterior.siguiente = nuevo              # el anterior se engancha al nuevo
        self.tamano += 1

    #Eliminar
    # Devuelve True si lo borró y False si no lo encontró
    def eliminar(self, dato):
        # Si la lista esta vacía
        if self.esta_vacia():
            return False

        # Si el dato está en la cabeza
        if self.cabeza.dato == dato:
            # la cabeza pasa a ser el segundo nodo
            self.cabeza = self.cabeza.siguiente
            self.tamano -= 1    # -= 1 es lo mismo que tamano = tamano - 1
            return True

        # Si no estaba en la cabeza, lo buscamos mirando "un paso adelante"
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
    # (empieza a contar en 0; si no lo encuentra devuelve -1)
    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual is not None:    # mientras haya nodo que revisar
            if actual.dato == dato:
                return posicion      # lo encontramos: decimos dónde está
            actual = actual.siguiente
            posicion += 1
        return -1

    # Devuelve el mismo texto que print(lista).
    def recorrer(self):
        return str(self)    # str(self) usa el método __str__ de abajo

    # Texto de la lista:  1 -> 2 -> 3 -> None   ->  O(n)
    # __str__ es lo que Python muestra cuando hacemos print(lista)
    def __str__(self):
        partes = []    # lista temporal SOLO de textos, no de nodos
        actual = self.cabeza
        while actual is not None:
            partes.append(str(actual.dato))    # append = agregar al final; str() = volver texto
            actual = actual.siguiente
        partes.append("None")
        # join pega todos los textos poniendo " -> " entre cada uno
        return " -> ".join(partes)

    # Recorre del final al inicio
    def recorrer_inverso(self):
        if self.esta_vacia():
            return "None"
        partes = []    # lista temporal SOLO de textos
        self._recorrer_inverso_rec(self.cabeza, partes)
        return " -> ".join(partes)

    # Función recursiva de apoyo.
    # Recursiva = la función se llama a sí misma, nodo por nodo
    # El _ al inicio del nombre indica que es de uso interno de la clase
    def _recorrer_inverso_rec(self, nodo, partes):
        if nodo is None:    # ya no hay más nodos: aquí paramos
            return
        # primero vamos hasta el final y al regresar guardamos el dato, por eso sale al revés
        self._recorrer_inverso_rec(nodo.siguiente, partes)
        partes.append(str(nodo.dato))

    # ---------------- OPERACIÓN ESPECIAL ----------------

    # Invierte la lista cambiando los enlaces (no crea nodos nuevos).
    # Usa tres punteros: anterior, actual y siguiente.  ->  O(n)
    '''def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual is not None:
            # 1. guardamos el siguiente para no perderlo
            siguiente = actual.siguiente
            # 2. el actual ahora apunta hacia atrás
            actual.siguiente = anterior
            # 3. anterior avanza al actual
            anterior = actual
            # 4. actual avanza al siguiente que guardamos
            actual = siguiente
        # el último nodo quedó en 'anterior': es la nueva cabeza
        self.cabeza = anterior

'''
# ============================================================
# MENÚ: LISTA DE COMPRAS DEL MERCADO
# Cada producto es un nodo de la lista simple.
# ============================================================

def menu():
    compras = ListaSimple()    # creamos la lista de compras vacía

    while True:    # repite el menú para siempre, hasta que alguien elija 0
        # \n hace un salto de línea para que el menú no salga pegado
        print("\n------ LISTA DE COMPRAS (Lista simple) ------")
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
        opcion = input("Elige una opción: ")    # input lee lo que escribe el usuario (como texto)

        # el try evita que el programa se cierre si escriben algo mal
        try:
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
                break    # break rompe el while True y se acaba el menú

            else:
                print("Opción no válida.")

        # except atrapa el error para mostrar un mensaje en vez de cerrarse
        except ValueError:
            # pasa cuando int() recibe letras en vez de un número
            print("Error: debes escribir un número.")
        except IndexError:
            # la clase usa posiciones desde 0; aquí el usuario cuenta desde 1
            print("Error: ese puesto no existe en la lista.")

        # después de cada acción mostramos la lista
        print("Lista:", compras)


# Esto solo se ejecuta si corremos este archivo directamente
# (python lista_simple.py); si otro archivo lo importa, el menú no arranca
if __name__ == "__main__":
    menu()
