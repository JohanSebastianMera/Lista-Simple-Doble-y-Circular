# En la lista circular el último nodo (la cola) apunta otra vez al primero.
from nodos import Nodo
from lista_simple import ListaSimple 

class ListaCircular:

    def __init__(self):
        self.cola = None
        self.tamano = 0

    @property
    # @property permite escribir lista.cabeza sin paréntesis, como si fuera un dato.

    def cabeza(self):
        if self.cola is None:
            return None
        return self.cola.siguiente

    def esta_vacia(self):
        return self.cola is None

    # Permite usar len(lista) para saber el tamaño
    def __len__(self):
        return self.tamano

    def vaciar(self):
        self.cola = None
        self.tamano = 0

    # ---------------- MÉTODO DE APOYO ----------------
    # Quita el nodo que está DESPUÉS de 'anterior' y devuelve su dato.
    def _eliminar_siguiente(self, anterior):
        eliminado = anterior.siguiente
        if self.tamano == 1:
            # Era el único nodo (se apuntaba a sí mismo): la lista queda vacía
            self.cola = None
        else:
            # El anterior salta el nodo y apunta al que sigue
            anterior.siguiente = eliminado.siguiente
            # "is" compara si es el MISMO nodo, no solo el mismo dato
            if eliminado is self.cola:
                # Si quitamos la cola, el anterior pasa a ser la nueva cola
                self.cola = anterior
        eliminado.siguiente = None
        self.tamano -= 1
        return eliminado.dato

    # Agrega un dato al inicio: el nuevo queda entre la cola y la cabeza.
    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            nuevo.siguiente = nuevo
            self.cola = nuevo
        else:
            # El nuevo apunta a la cabeza actual y la cola apunta al nuevo
            nuevo.siguiente = self.cola.siguiente
            self.cola.siguiente = nuevo
        self.tamano += 1

    # Agrega un dato al final sin recorrer la lista, se inserta al inicio y la cola avanza un paso,
    def insertar_final(self, dato):
        self.insertar_inicio(dato)
        self.cola = self.cola.siguiente

    # Agrega un dato en la posición pos
    def insertar_en(self, pos, dato):
        if pos < 0 or pos > self.tamano:
            # raise envía un error para avisar que la posición no sirve
            raise IndexError(f"Posición inválida: {pos}. Debe estar entre 0 y {self.tamano}.")

        if pos == 0:
            self.insertar_inicio(dato)
            return
        if pos == self.tamano:
            self.insertar_final(dato)
            return

        # Buscamos el nodo ANTERIOR a la posición, empezando en la cabeza
        anterior = self.cola.siguiente
        for _ in range(pos - 1):
            anterior = anterior.siguiente

        nuevo = Nodo(dato)
        nuevo.siguiente = anterior.siguiente
        anterior.siguiente = nuevo
        self.tamano += 1

    # Devuelve True si lo borró y False si no lo encontró
    def eliminar(self, dato):
        if self.esta_vacia():
            return False

        # Empezamos en la cola para que anterior.siguiente sea la cabeza
        anterior = self.cola
        # range(tamano): revisamos cada nodo una sola vez y paramos
        for _ in range(self.tamano):
            actual = anterior.siguiente
            if actual.dato == dato:
                self._eliminar_siguiente(anterior)
                return True
            anterior = actual
        return False

    # Devuelve la posición del dato o -1 si no está
    def buscar(self, dato):
        if self.esta_vacia():
            return -1
        actual = self.cola.siguiente
        # El for da una sola vuelta y además nos va dando la posición
        for posicion in range(self.tamano):
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
        return -1

    def recorrer(self):
        return str(self)

    # Texto de la lista
    def __str__(self):
        if self.esta_vacia():
            return "(vacía)"
        partes = []    
        actual = self.cola.siguiente
        for _ in range(self.tamano):
            partes.append(str(actual.dato))
            actual = actual.siguiente
        # Después de una vuelta completa, 'actual' llegó otra vez a la cabeza
        partes.append(f"(vuelve a {actual.dato})")
        return " -> ".join(partes)


    # Rota la lista n posiciones SIN mover los datos: solo avanza la cola,
    def rotar(self, n):
        if self.tamano <= 1:
            return
        for _ in range(n % self.tamano):
            self.cola = self.cola.siguiente

    # Josefo cuenta de k en k alrededor del círculo y se elimina al que cae en k, 
    # hasta que no quede nadie.(Devuelve una ListaSimple con el orden en que fueron saliendo)
    def josefo(self, k):
        if k < 1:
            raise ValueError(f"k debe ser mayor o igual a 1 (se recibió {k}).")

        orden = ListaSimple()
        # Empezamos en la cola para que el conteo arranque en la cabeza
        anterior = self.cola
        # El range se calcula una sola vez al inicio: una vuelta por cada persona
        for _ in range(self.tamano):
            # Avanzamos k - 1 pasos; el que sigue (el k-ésimo) es el que sale
            for _ in range(k - 1):
                anterior = anterior.siguiente
            dato = self._eliminar_siguiente(anterior)
            # Se agrega al inicio porque es más rápido que al final en la lista simple;
            # al terminar se invierte una vez y queda en el orden correcto
            orden.insertar_inicio(dato)
        orden.invertir()
        return orden

# ============================================================
# MENÚ: TURNOS PARA LAVAR LOS PLATOS
# ============================================================

def menu():
    turnos = ListaCircular()

    while True:
        print("\n------ TURNOS PARA LAVAR LOS PLATOS ------")
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
                # El usuario cuenta desde 1 y la lista desde 0: restamos 1
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
                # La posición coincide con los días que faltan (0 = hoy)
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
                    # josefo() vacía la lista, por eso jugamos con una COPIA
                    # y la ronda real de turnos no se pierde
                    copia = ListaCircular()
                    actual = turnos.cabeza
                    for _ in range(len(turnos)):
                        copia.insertar_final(actual.dato)
                        actual = actual.siguiente
                    orden = copia.josefo(k)
                    print("Orden en que van saliendo:", orden)
                    # El último en salir es quien pierde: avanzamos hasta él
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

# Lo ejecutamos solo si se llama directamente a este archivo, no si se importa
if __name__ == "__main__":
    menu()
