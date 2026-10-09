# ============================================================
# lista_circular.py
# Lista circular: el último nodo (la cola) apunta de nuevo al primero.
# Solo guardamos la cola; la cabeza es cola.siguiente.
# Ejemplo cotidiano: turnos para lavar los platos en la casa.
#
# IMPORTANTE: aquí ningún nodo apunta a None, así que un
# "while actual:" NUNCA terminaría (ciclo infinito).
# Por eso todos los recorridos usan  for _ in range(self.tamano):
# así visitamos exactamente 'tamano' nodos y paramos.
#
# Para ejecutar el menú:  python lista_circular.py
#
# Asignatura: Estructuras de la Información
# Autores: [NOMBRE 1], [NOMBRE 2], [NOMBRE 3], [NOMBRE 4]
# ============================================================

from nodos import Nodo
from lista_simple import ListaSimple


class ListaCircular:

    # Crea la lista vacía.
    def __init__(self):
        self.cola = None   # cola.siguiente es la cabeza
        self.tamano = 0    # cuántos nodos hay

    # La cabeza no se guarda: se calcula como cola.siguiente.
    # Con @property se puede escribir lista.cabeza sin paréntesis.
    @property
    def cabeza(self):
        if self.cola is None:
            return None
        return self.cola.siguiente

    # ¿La lista está vacía?  ->  O(1)
    def esta_vacia(self):
        return self.cola is None

    # Permite usar len(lista).  ->  O(1)
    def __len__(self):
        return self.tamano

    # Borra todo.  ->  O(1)
    def vaciar(self):
        self.cola = None
        self.tamano = 0

    # ---------------- MÉTODO DE APOYO (privado) ----------------

    # Quita el nodo que está DESPUÉS de 'anterior' y devuelve su dato.
    # Lo usan eliminar() y josefo().  ->  O(1)
    def _eliminar_siguiente(self, anterior):
        eliminado = anterior.siguiente
        if self.tamano == 1:
            # era el único nodo: la lista queda vacía
            self.cola = None
        else:
            # el anterior salta el nodo y apunta al que sigue
            anterior.siguiente = eliminado.siguiente
            if eliminado is self.cola:
                # si quitamos la cola, la nueva cola es el anterior
                self.cola = anterior
        # el nodo quitado ya no apunta a nadie
        eliminado.siguiente = None
        self.tamano -= 1
        return eliminado.dato

    # ---------------- INSERTAR ----------------

    # Agrega un dato al inicio (entre la cola y la cabeza).  ->  O(1)
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            # 1. único nodo: se apunta a sí mismo para cerrar el círculo
            nuevo.siguiente = nuevo
            # 2. ese nodo es la cola (y también la cabeza)
            self.cola = nuevo
        else:
            # 1. el nuevo apunta a la cabeza actual
            nuevo.siguiente = self.cola.siguiente
            # 2. la cola apunta al nuevo, que pasa a ser la cabeza
            self.cola.siguiente = nuevo
        self.tamano += 1

    # Agrega un dato al final.  ->  O(1)
    # Truco: lo insertamos al inicio y movemos la cola un paso adelante.
    def insertar_final(self, dato):
        self.insertar_inicio(dato)
        # la cola avanza al nuevo nodo, que ahora es el último
        self.cola = self.cola.siguiente

    # Agrega un dato en la posición pos (la cabeza es la 0).  ->  O(n)
    def insertar_en(self, pos, dato):
        if pos < 0 or pos > self.tamano:
            raise IndexError(f"Posición inválida: {pos}. Debe estar entre 0 y {self.tamano}.")

        if pos == 0:
            self.insertar_inicio(dato)
            return
        if pos == self.tamano:
            self.insertar_final(dato)
            return

        # buscamos el nodo anterior a la posición, desde la cabeza
        anterior = self.cola.siguiente
        for _ in range(pos - 1):
            anterior = anterior.siguiente

        nuevo = Nodo(dato)
        # 1. el nuevo apunta al que estaba en la posición
        nuevo.siguiente = anterior.siguiente
        # 2. el anterior apunta al nuevo
        anterior.siguiente = nuevo
        self.tamano += 1

    # ---------------- ELIMINAR Y BUSCAR ----------------

    # Elimina la primera vez que aparece el dato.
    # Devuelve True si lo eliminó, False si no estaba.  ->  O(n)
    def eliminar(self, dato):
        if self.esta_vacia():
            return False

        # empezamos en la cola, así anterior.siguiente es la cabeza
        anterior = self.cola
        # for con range(tamano): damos UNA sola vuelta (sin ciclo infinito)
        for _ in range(self.tamano):
            actual = anterior.siguiente
            if actual.dato == dato:
                self._eliminar_siguiente(anterior)   # se encarga de los casos especiales
                return True
            anterior = actual
        return False

    # Devuelve la posición del dato (desde 0) o -1 si no está.  ->  O(n)
    def buscar(self, dato):
        if self.esta_vacia():
            return -1
        actual = self.cola.siguiente
        # for con range(tamano): una sola vuelta
        for posicion in range(self.tamano):
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
        return -1

    # ---------------- RECORRER ----------------

    # Devuelve el mismo texto que print(lista).
    def recorrer(self):
        return str(self)

    # Texto de la lista:  1 -> 2 -> 3 -> (vuelve a 1)   ->  O(n)
    def __str__(self):
        if self.esta_vacia():
            return "(vacía)"
        partes = []    # lista temporal SOLO de textos
        actual = self.cola.siguiente
        # for con range(tamano): exactamente una vuelta
        for _ in range(self.tamano):
            partes.append(str(actual.dato))
            actual = actual.siguiente
        # al terminar la vuelta, 'actual' es otra vez la cabeza
        partes.append(f"(vuelve a {actual.dato})")
        return " -> ".join(partes)

    # ---------------- OPERACIONES ESPECIALES ----------------

    # Rota la lista n posiciones a la izquierda SIN mover los datos:
    # solo avanzamos la cola (y la cabeza avanza con ella).
    # Ejemplo: rotar(2) en 1..5 deja 3 -> 4 -> 5 -> 1 -> 2.
    # Usamos n % tamano para no dar vueltas completas de más.  ->  O(n)
    def rotar(self, n):
        if self.tamano <= 1:
            return    # vacía o con un nodo: no cambia nada
        for _ in range(n % self.tamano):
            self.cola = self.cola.siguiente

    # Problema de Josefo: eliminamos cada k-ésimo nodo hasta vaciar la lista.
    # Devuelve una ListaSimple con el orden en que salieron.
    # OJO: la lista circular queda vacía.  ->  O(n·k)
    def josefo(self, k):
        if k < 1:
            raise ValueError(f"k debe ser mayor o igual a 1 (se recibió {k}).")

        orden = ListaSimple()
        # empezamos en la cola para que el conteo arranque en la cabeza
        anterior = self.cola
        # una vuelta del for por cada nodo que hay que eliminar
        for _ in range(self.tamano):
            # avanzamos k - 1 nodos; el k-ésimo queda en anterior.siguiente
            for _ in range(k - 1):
                anterior = anterior.siguiente
            dato = self._eliminar_siguiente(anterior)
            # insertamos al inicio (O(1)) y al final invertimos una sola vez
            orden.insertar_inicio(dato)
        orden.invertir()
        return orden


# ============================================================
# MENÚ: TURNOS PARA LAVAR LOS PLATOS
# Cada persona de la casa es un nodo. Cuando le toca al último,
# el turno vuelve al primero: ¡es un círculo!
# La cabeza (cola.siguiente) es a quien le toca HOY.
# ============================================================

def menu():
    turnos = ListaCircular()

    while True:
        print("\n------ TURNOS PARA LAVAR LOS PLATOS (Lista circular) ------")
        print("1. ¿A quién le toca hoy?")
        print("2. Agregar persona (le toca hoy)")
        print("3. Agregar persona al final de la ronda")
        print("4. Agregar persona en un puesto")
        print("5. Sacar persona de la ronda (eliminar)")
        print("6. ¿Cuándo me toca? (buscar)")
        print("7. Pasar al día siguiente (rotar 1)")
        print("8. Adelantar varios días (rotar n)")
        print("9. Papa caliente: ¿quién lava en Navidad? (Josefo)")
        print("10. Cargar casa de ejemplo")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        # el try evita que el programa se cierre si escriben algo mal
        try:
            if opcion == "1":
                if turnos.esta_vacia():
                    print("No hay nadie en la ronda.")
                else:
                    print("Hoy lava los platos:", turnos.cabeza.dato)
                    print("Mañana le toca a:", turnos.cabeza.siguiente.dato)

            elif opcion == "2":
                nombre = input("Nombre: ")
                turnos.insertar_inicio(nombre)
                print("A", nombre, "le toca hoy.")

            elif opcion == "3":
                nombre = input("Nombre: ")
                turnos.insertar_final(nombre)
                print(nombre, "entra al final de la ronda.")

            elif opcion == "4":
                # el usuario cuenta desde 1, la lista desde 0: restamos 1
                puesto = int(input(f"Puesto (1 a {len(turnos) + 1}): "))
                nombre = input("Nombre: ")
                turnos.insertar_en(puesto - 1, nombre)
                print(nombre, "quedó en el puesto", puesto)

            elif opcion == "5":
                nombre = input("¿Quién sale de la ronda?: ")
                if turnos.eliminar(nombre):
                    print(nombre, "ya no está en la ronda.")
                else:
                    print(nombre, "no estaba en la ronda.")

            elif opcion == "6":
                nombre = input("¿Para quién?: ")
                pos = turnos.buscar(nombre)
                if pos == -1:
                    print(nombre, "no está en la ronda.")
                elif pos == 0:
                    print("¡A", nombre, "le toca HOY!")
                else:
                    print("A", nombre, "le toca dentro de", pos, "día(s).")

            elif opcion == "7":
                turnos.rotar(1)
                if not turnos.esta_vacia():
                    print("Pasó un día. Ahora le toca a", turnos.cabeza.dato)

            elif opcion == "8":
                dias = int(input("¿Cuántos días pasaron?: "))
                turnos.rotar(dias)
                if not turnos.esta_vacia():
                    print("Ahora le toca a", turnos.cabeza.dato)

            elif opcion == "9":
                if turnos.esta_vacia():
                    print("No hay nadie para jugar.")
                else:
                    k = int(input("¿De cuánto en cuánto se cuenta? (k >= 1): "))
                    # josefo vacía la lista, así que jugamos con una COPIA
                    copia = ListaCircular()
                    actual = turnos.cabeza
                    for _ in range(len(turnos)):
                        copia.insertar_final(actual.dato)
                        actual = actual.siguiente
                    orden = copia.josefo(k)
                    print("Orden en que van saliendo:", orden)
                    # el último en salir es quien pierde
                    ultimo = orden.cabeza
                    for _ in range(len(orden) - 1):
                        ultimo = ultimo.siguiente
                    print("Pierde y lava los platos en Navidad:", ultimo.dato)

            elif opcion == "10":
                turnos.vaciar()
                for nombre in ("Ana", "Luis", "Sofía", "Carlos", "Valentina", "Mateo", "Laura"):
                    turnos.insertar_final(nombre)
                print("Se cargó la casa de ejemplo.")

            elif opcion == "0":
                print("¡Que nadie se salte su turno!")
                break

            else:
                print("Opción no válida.")

        except ValueError:
            print("Error: debes escribir un número entero (en Josefo, k >= 1).")
        except IndexError:
            # la clase usa posiciones desde 0; aquí el usuario cuenta desde 1
            print("Error: ese puesto no existe en la lista.")

        # después de cada acción mostramos la ronda
        print("Ronda:", turnos)


# Esto solo se ejecuta si corremos este archivo directamente
if __name__ == "__main__":
    menu()
