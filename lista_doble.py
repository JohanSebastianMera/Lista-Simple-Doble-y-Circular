# ============================================================
# lista_doble.py
# Lista doblemente enlazada: cada nodo conoce al SIGUIENTE y al ANTERIOR.
# Guarda la cabeza (inicio) y la cola (final).
# Ejemplo cotidiano: un reproductor de música (canción siguiente / anterior).
#
# Para ejecutar el menú:  python lista_doble.py
#
# Asignatura: Estructuras de la Información
# Autores: [NOMBRE 1], [NOMBRE 2], [NOMBRE 3], [NOMBRE 4]
# ============================================================

from nodos import NodoDoble


class ListaDoble:

    # Crea la lista vacía: sin cabeza, sin cola y tamaño 0.
    def __init__(self):
        self.cabeza = None    # primer nodo
        self.cola = None      # último nodo
        self.tamano = 0       # cuántos nodos hay

    # ¿La lista está vacía?  ->  O(1)
    def esta_vacia(self):
        return self.cabeza is None

    # Permite usar len(lista).  ->  O(1)
    def __len__(self):
        return self.tamano

    # Borra todo.  ->  O(1)
    def vaciar(self):
        self.cabeza = None
        self.cola = None
        self.tamano = 0

    # ---------------- MÉTODOS DE APOYO (privados) ----------------

    # Devuelve el nodo de la posición pos, entrando por el extremo más cercano.
    # Si pos está en la primera mitad avanza desde la cabeza,
    # si no, retrocede desde la cola.  ->  O(n), máximo n/2 pasos
    def _nodo_en(self, pos):
        if pos < self.tamano // 2:
            actual = self.cabeza
            for _ in range(pos):
                actual = actual.siguiente      # avanzamos
        else:
            actual = self.cola
            for _ in range(self.tamano - 1 - pos):
                actual = actual.anterior       # retrocedemos
        return actual

    # Quita de la lista un nodo que ya tenemos ubicado y devuelve su dato.
    # Arregla cabeza y cola si el nodo era un extremo.  ->  O(1)
    def _desenlazar(self, nodo):
        ant = nodo.anterior
        sig = nodo.siguiente

        if ant is None:
            # era la cabeza: la cabeza pasa a ser el siguiente
            self.cabeza = sig
        else:
            # el anterior salta el nodo y apunta al siguiente
            ant.siguiente = sig

        if sig is None:
            # era la cola: la cola pasa a ser el anterior
            self.cola = ant
        else:
            # el siguiente salta el nodo y apunta hacia atrás al anterior
            sig.anterior = ant

        # (si era el único nodo, cabeza y cola quedaron en None)

        # el nodo quitado ya no apunta a nadie
        nodo.anterior = None
        nodo.siguiente = None
        self.tamano -= 1
        return nodo.dato

    # ---------------- INSERTAR ----------------

    # Agrega un dato al inicio.  ->  O(1)
    def insertar_inicio(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            # lista vacía: el nuevo es cabeza y cola a la vez
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            # 1. el nuevo apunta hacia adelante a la cabeza
            nuevo.siguiente = self.cabeza
            # 2. la cabeza apunta hacia atrás al nuevo
            self.cabeza.anterior = nuevo
            # 3. la cabeza ahora es el nuevo
            self.cabeza = nuevo
        self.tamano += 1

    # Agrega un dato al final.  ->  O(1) gracias a la cola
    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            # lista vacía: el nuevo es cabeza y cola a la vez
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            # 1. el nuevo apunta hacia atrás a la cola
            nuevo.anterior = self.cola
            # 2. la cola apunta hacia adelante al nuevo
            self.cola.siguiente = nuevo
            # 3. la cola ahora es el nuevo
            self.cola = nuevo
        self.tamano += 1

    # Agrega un dato en la posición pos (empieza en 0).  ->  O(n)
    def insertar_en(self, pos, dato):
        if pos < 0 or pos > self.tamano:
            raise IndexError(f"Posición inválida: {pos}. Debe estar entre 0 y {self.tamano}.")

        if pos == 0:
            self.insertar_inicio(dato)
            return
        if pos == self.tamano:
            self.insertar_final(dato)
            return

        # caso del medio: el nuevo va entre 'ant' y 'sig'
        sig = self._nodo_en(pos)    # el que hoy está en la posición
        ant = sig.anterior          # el que está antes
        nuevo = NodoDoble(dato)
        # 1. el nuevo apunta hacia atrás al anterior
        nuevo.anterior = ant
        # 2. el nuevo apunta hacia adelante al siguiente
        nuevo.siguiente = sig
        # 3. el anterior apunta hacia adelante al nuevo
        ant.siguiente = nuevo
        # 4. el siguiente apunta hacia atrás al nuevo
        sig.anterior = nuevo
        self.tamano += 1

    # ---------------- ELIMINAR Y BUSCAR ----------------

    # Elimina la primera vez que aparece el dato.
    # Devuelve True si lo eliminó, False si no estaba.  ->  O(n)
    def eliminar(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.dato == dato:
                self._desenlazar(actual)    # se encarga de cabeza, cola y único nodo
                return True
            actual = actual.siguiente
        return False

    # Devuelve la posición del dato (desde 0) o -1 si no está.  ->  O(n)
    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual is not None:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    # ---------------- RECORRER ----------------

    # Devuelve el mismo texto que print(lista).
    def recorrer(self):
        return str(self)

    # Texto de la lista:  None <- 1 <-> 2 <-> 3 -> None   ->  O(n)
    def __str__(self):
        if self.esta_vacia():
            return "None"
        partes = []    # lista temporal SOLO de textos
        actual = self.cabeza
        while actual is not None:
            partes.append(str(actual.dato))
            actual = actual.siguiente
        return "None <- " + " <-> ".join(partes) + " -> None"

    # Recorre desde la cola hacia atrás:  3 <-> 2 <-> 1   ->  O(n)
    def recorrer_inverso(self):
        if self.esta_vacia():
            return "None"
        partes = []    # lista temporal SOLO de textos
        actual = self.cola
        while actual is not None:
            partes.append(str(actual.dato))
            actual = actual.anterior    # usamos el enlace hacia atrás
        return " <-> ".join(partes)

    # ---------------- OPERACIÓN ESPECIAL ----------------

    # Elimina el nodo de la posición pos y devuelve su dato.
    # Llega al nodo desde el extremo más cercano (ver _nodo_en).  ->  O(n)
    def eliminar_en(self, pos):
        if self.esta_vacia():
            raise IndexError(f"Posición inválida: {pos}. La lista está vacía.")
        if pos < 0 or pos >= self.tamano:
            raise IndexError(f"Posición inválida: {pos}. Debe estar entre 0 y {self.tamano - 1}.")
        nodo = self._nodo_en(pos)
        return self._desenlazar(nodo)


# ============================================================
# MENÚ: REPRODUCTOR DE MÚSICA
# Cada canción es un nodo doble. Con 'siguiente' y 'anterior'
# podemos pasar de canción hacia adelante y hacia atrás.
# ============================================================

def menu():
    playlist = ListaDoble()
    sonando = None    # nodo de la canción que está sonando

    while True:
        print("\n------ REPRODUCTOR DE MÚSICA (Lista doble) ------")
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

        # el try evita que el programa se cierre si escriben algo mal
        try:
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

        except ValueError:
            print("Error: debes escribir un número.")
        except IndexError:
            # la clase usa posiciones desde 0; aquí el usuario cuenta desde 1
            print("Error: ese puesto no existe en la lista.")

        # Si no sonaba nada, o si quitaron la canción que sonaba
        # (quedó sin enlace anterior y ya no es la cabeza), volvemos a la primera.
        if sonando is None or (sonando is not playlist.cabeza and sonando.anterior is None):
            sonando = playlist.cabeza

        # después de cada acción mostramos la playlist
        print("Playlist:", playlist)
        if sonando is not None:
            print("Sonando ahora:", sonando.dato)


# Esto solo se ejecuta si corremos este archivo directamente
if __name__ == "__main__":
    menu()
