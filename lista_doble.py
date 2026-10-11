from nodos import NodoDoble

class ListaDoble:

    # Creamos la lista vacía
    def __init__(self):
        self.cabeza = None  
        self.cola = None   
        self.tamano = 0 

    # ¿La lista está vacía?
    def esta_vacia(self):
        return self.cabeza is None

    # Permite usar len(lista) para saber el tamaño
    def __len__(self):
        return self.tamano

    # Borra todo
    def vaciar(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    # ---------------- MÉTODOS DE APOYO ----------------
    def _nodo_en(self, pos):
        if pos < self.tamano // 2:
            actual = self.cabeza
            for _ in range(pos):
                actual = actual.siguiente
        else:
            actual = self.cola
            for _ in range(self.tamano - 1 - pos):
                actual = actual.anterior
        return actual

    # Quita de la lista un nodo que ya tenemos ubicado y devuelve su dato.
    def _desenlazar(self, nodo):
        ant = nodo.anterior
        sig = nodo.siguiente

        if ant is None:
            # Si era la cabeza, la cabeza pasa a ser el siguiente
            self.cabeza = sig
        else:
            # el anterior salta el nodo y apunta al siguiente
            ant.siguiente = sig

        if sig is None:
            # Si era la cola, la cola pasa a ser el anterior
            self.cola = ant
        else:
            sig.anterior = ant
        nodo.anterior = None
        nodo.siguiente = None
        self.tamano -= 1
        return nodo.dato

    # Agrega un dato al inicio.
    def insertar_inicio(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamano += 1

    # Agrega un dato al final. 
    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamano += 1

    # Agrega un dato en la posición pos
    def insertar_en(self, pos, dato):
        if pos < 0 or pos > self.tamano:
            raise IndexError(f"Posición inválida: {pos}. Debe estar entre 0 y {self.tamano}.")

        if pos == 0:
            self.insertar_inicio(dato)
            return
        if pos == self.tamano:
            self.insertar_final(dato)
            return
        sig = self._nodo_en(pos)  
        ant = sig.anterior    
        nuevo = NodoDoble(dato)
        nuevo.anterior = ant
        nuevo.siguiente = sig
        ant.siguiente = nuevo
        sig.anterior = nuevo
        self.tamano += 1

    def eliminar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                self._desenlazar(actual)
                return True
            actual = actual.siguiente
        return False

    # Devuelve la posición del dato
    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual is not None:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    # Devuelve el mismo texto que print(lista).
    def recorrer(self):
        return str(self)

    # Texto de la lista
    def __str__(self):
        if self.esta_vacia():
            return "None"
        partes = []    # lista temporal SOLO de textos
        actual = self.cabeza
        while actual is not None:
            partes.append(str(actual.dato))
            actual = actual.siguiente
        return "None <- " + " <-> ".join(partes) + " -> None"

    # Recorre desde la cola hacia atrás
    def recorrer_inverso(self):
        if self.esta_vacia():
            return "None"
        partes = [] 
        actual = self.cola
        while actual is not None:
            partes.append(str(actual.dato))
            actual = actual.anterior    # usamos el enlace hacia atrás
        return " <-> ".join(partes)

    # ---------------- OPERACIÓN ESPECIAL ----------------

    # Elimina el nodo de la posición pos y devuelve su dato.
    def eliminar_en(self, pos):
        if self.esta_vacia():
            raise IndexError(f"Posición inválida: {pos}. La lista está vacía.")
        if pos < 0 or pos >= self.tamano:
            raise IndexError(f"Posición inválida: {pos}. Debe estar entre 0 y {self.tamano - 1}.")
        nodo = self._nodo_en(pos)
        return self._desenlazar(nodo)

# ============================================================
# MENÚ: REPRODUCTOR DE MÚSICA
# ============================================================

def menu():
    playlist = ListaDoble()
    sonando = None

    while True:
        print("\n------ REPRODUCTOR DE MÚSICA ------")
        print("1. Agregar canción al inicio")
        print("2. Agregar canción al final")
        print("3. Agregar canción en un puesto")
        print("4. Quitar canción por nombre (eliminar)")
        print("5. Quitar canción por puesto (eliminar_en)")
        print("6. Buscar canción")
        print("7. >> Siguiente canción")
        print("8. << Canción anterior")
        print("9. Ver playlist al revés (recorrer inverso)")
        print("10. Cargar playlist de ejemplo")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
                cancion = input("Canción: ")
                playlist.insertar_inicio(cancion)
                print(cancion, "agregada al inicio.")

        elif opcion == "2":
                cancion = input("Canción: ")
                playlist.insertar_final(cancion)
                print(cancion, "agregada al final.")

        elif opcion == "3":
                # el usuario cuenta desde 1, la lista desde 0: restamos 1
                puesto = int(input(f"Puesto (1 a {len(playlist) + 1}): "))
                cancion = input("Canción: ")
                playlist.insertar_en(puesto - 1, cancion)
                print(cancion, "quedó en el puesto", puesto)

        elif opcion == "4":
                cancion = input("Canción a quitar: ")
                if playlist.eliminar(cancion):
                    print(cancion, "salió de la playlist.")
                else:
                    print(cancion, "no está en la playlist.")

        elif opcion == "5":
                puesto = int(input(f"Puesto a quitar (1 a {len(playlist)}): "))
                cancion = playlist.eliminar_en(puesto - 1)
                print(cancion, "salió de la playlist.")

        elif opcion == "6":
                cancion = input("Canción a buscar: ")
                pos = playlist.buscar(cancion)
                if pos == -1:
                    print(cancion, "no está en la playlist.")
                else:
                    print(cancion, "está en el puesto", pos + 1)

        elif opcion == "7":
                if sonando is None:
                    print("La playlist está vacía.")
                elif sonando.siguiente is None:
                    print("Ya estás en la última canción.")
                else:
                    sonando = sonando.siguiente    # avanzamos con 'siguiente'

        elif opcion == "8":
                if sonando is None:
                    print("La playlist está vacía.")
                elif sonando.anterior is None:
                    print("Ya estás en la primera canción.")
                else:
                    sonando = sonando.anterior     # retrocedemos con 'anterior'
        elif opcion == "9":
                print("Al revés:", playlist.recorrer_inverso())

        elif opcion == "10":
                playlist.vaciar()
                for cancion in ("La Bicicleta", "Colombia Tierra Querida", "Despacito",
                                "La Gota Fría", "Tusa", "Me Gustas Tú", "Hips Don't Lie"):
                    playlist.insertar_final(cancion)
                sonando = playlist.cabeza
                print("Se cargó la playlist de ejemplo.")

        elif opcion == "0":
                print("¡Hasta la próxima canción!")
                break
        else:
                print("Opción no válida.")

        
        # Si no sonaba nada, o si quitaron la canción que sonaba
        if sonando is None or (sonando is not playlist.cabeza and sonando.anterior is None):
            sonando = playlist.cabeza
        print("Playlist:", playlist)
        if sonando is not None:
            print("Sonando ahora:", sonando.dato)


# Esto solo se ejecuta si corremos este archivo directamente
if __name__ == "__main__":
    menu()
