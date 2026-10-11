# Pruebas de la lista circular.
# Se ejecutan desde la carpeta del proyecto con:
#   python -m unittest discover -s tests -v

import unittest

# Estas 3 líneas le dicen a Python dónde están los archivos de las listas
# (la carpeta de arriba de tests), así la prueba funciona desde cualquier lado,
# también con el botón "Run" del editor.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lista_circular import ListaCircular


# Función de ayuda: crea una lista circular con los datos que le pasemos.
# El * permite pasarle cualquier cantidad de datos: crear_lista(1, 2, 3)
def crear_lista(*datos):
    lista = ListaCircular()
    for dato in datos:
        lista.insertar_final(dato)
    return lista


class TestListaCircular(unittest.TestCase):

    # ---------------- LISTA VACÍA ----------------

    def test_lista_vacia(self):
        lista = ListaCircular()
        self.assertTrue(lista.esta_vacia())
        self.assertEqual(len(lista), 0)
        self.assertEqual(str(lista), "(vacía)")
        self.assertIsNone(lista.cola)
        self.assertFalse(lista.eliminar("Ana"))
        self.assertEqual(lista.buscar("Ana"), -1)

    def test_rotar_y_josefo_lista_vacia(self):
        lista = ListaCircular()
        lista.rotar(3)    # rotar una lista vacía no debe fallar
        self.assertTrue(lista.esta_vacia())
        orden = lista.josefo(3)
        self.assertTrue(orden.esta_vacia())

    # ---------------- UN SOLO NODO ----------------

    def test_un_nodo(self):
        lista = ListaCircular()
        lista.insertar_inicio("Ana")
        self.assertEqual(len(lista), 1)
        self.assertEqual(str(lista), "Ana -> (vuelve a Ana)")
        # con un solo nodo, el nodo se apunta a sí mismo
        self.assertIs(lista.cola.siguiente, lista.cola)

    def test_un_nodo_eliminar(self):
        lista = ListaCircular()
        lista.insertar_final("Ana")
        self.assertTrue(lista.eliminar("Ana"))
        # al borrar el único nodo, la cola queda en None
        self.assertIsNone(lista.cola)
        self.assertTrue(lista.esta_vacia())

    # ---------------- VARIOS NODOS ----------------

    def test_insertar_inicio_y_final(self):
        lista = ListaCircular()
        lista.insertar_final("Luis")
        lista.insertar_final("Sofía")
        lista.insertar_inicio("Ana")
        self.assertEqual(str(lista), "Ana -> Luis -> Sofía -> (vuelve a Ana)")
        self.assertEqual(lista.cola.dato, "Sofía")
        # lo más importante: la cola apunta otra vez a la cabeza
        self.assertEqual(lista.cola.siguiente.dato, "Ana")

    def test_insertar_en_posicion(self):
        lista = crear_lista("Ana", "Sofía")
        lista.insertar_en(1, "Luis")
        self.assertEqual(str(lista), "Ana -> Luis -> Sofía -> (vuelve a Ana)")
        self.assertEqual(len(lista), 3)

    def test_eliminar_varios(self):
        lista = crear_lista("Ana", "Luis", "Sofía", "Carlos")
        lista.eliminar("Ana")       # la cabeza
        self.assertEqual(lista.cola.siguiente.dato, "Luis")
        lista.eliminar("Carlos")    # la cola
        self.assertEqual(lista.cola.dato, "Sofía")
        self.assertEqual(str(lista), "Luis -> Sofía -> (vuelve a Luis)")
        # si no está, devuelve False (y no se queda dando vueltas para siempre)
        self.assertFalse(lista.eliminar("Pedro"))

    def test_buscar_varios(self):
        lista = crear_lista("Ana", "Luis", "Sofía")
        self.assertEqual(lista.buscar("Ana"), 0)
        self.assertEqual(lista.buscar("Sofía"), 2)
        self.assertEqual(lista.buscar("Pedro"), -1)

    def test_rotar(self):
        lista = crear_lista(1, 2, 3, 4, 5)
        lista.rotar(2)
        # la cabeza ahora es el 3
        self.assertEqual(lista.cabeza.dato, 3)
        self.assertEqual(str(lista), "3 -> 4 -> 5 -> 1 -> 2 -> (vuelve a 3)")

    def test_rotar_mas_que_el_tamano(self):
        lista = crear_lista(1, 2, 3, 4, 5)
        lista.rotar(12)    # 12 % 5 = 2, es igual que rotar 2
        self.assertEqual(lista.cabeza.dato, 3)

    def test_josefo(self):
        lista = crear_lista(1, 2, 3, 4, 5, 6, 7)
        orden = lista.josefo(3)
        # contando de 3 en 3, salen en este orden (el resultado es una lista simple)
        self.assertEqual(str(orden), "3,6,2,7,5,1,4,None")
        # josefo deja la lista circular vacía
        self.assertTrue(lista.esta_vacia())

    def test_josefo_k_invalido(self):
        lista = crear_lista(1, 2, 3)
        with self.assertRaises(ValueError):
            lista.josefo(0)

    # ---------------- POSICIÓN INVÁLIDA ----------------

    def test_posicion_invalida(self):
        lista = crear_lista("Ana", "Luis")
        with self.assertRaises(IndexError):
            lista.insertar_en(5, "Pedro")
        with self.assertRaises(IndexError):
            lista.insertar_en(-1, "Pedro")


if __name__ == "__main__":
    unittest.main()
