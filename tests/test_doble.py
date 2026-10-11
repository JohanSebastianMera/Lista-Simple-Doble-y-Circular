# Pruebas de la lista doble.
# Se ejecutan desde la carpeta del proyecto con:
#   python -m unittest discover -s tests -v

import unittest

# Estas 3 líneas le dicen a Python dónde están los archivos de las listas
# (la carpeta de arriba de tests), así la prueba funciona desde cualquier lado,
# también con el botón "Run" del editor.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lista_doble import ListaDoble


class TestListaDoble(unittest.TestCase):

    # ---------------- LISTA VACÍA ----------------

    def test_lista_vacia(self):
        lista = ListaDoble()
        self.assertTrue(lista.esta_vacia())
        self.assertEqual(len(lista), 0)
        self.assertEqual(str(lista), "None")
        self.assertEqual(lista.recorrer_inverso(), "None")
        # en una lista vacía no hay cabeza ni cola
        self.assertIsNone(lista.cabeza)
        self.assertIsNone(lista.cola)
        self.assertFalse(lista.eliminar("Tusa"))
        self.assertEqual(lista.buscar("Tusa"), -1)

    def test_eliminar_en_lista_vacia(self):
        lista = ListaDoble()
        # no se puede borrar una posición si no hay nada
        with self.assertRaises(IndexError):
            lista.eliminar_en(0)

    # ---------------- UN SOLO NODO ----------------

    def test_un_nodo(self):
        lista = ListaDoble()
        lista.insertar_inicio("Tusa")
        self.assertEqual(len(lista), 1)
        self.assertEqual(str(lista), "None <- Tusa -> None")
        # con un solo nodo, la cabeza y la cola son el MISMO nodo
        # (assertIs revisa que sean el mismo objeto)
        self.assertIs(lista.cabeza, lista.cola)

    def test_un_nodo_eliminar(self):
        lista = ListaDoble()
        lista.insertar_final("Tusa")
        self.assertTrue(lista.eliminar("Tusa"))
        # caso importante: al borrar el único nodo, cabeza Y cola quedan en None
        self.assertIsNone(lista.cabeza)
        self.assertIsNone(lista.cola)
        self.assertEqual(len(lista), 0)

    def test_un_nodo_eliminar_en(self):
        lista = ListaDoble()
        lista.insertar_final("Tusa")
        # eliminar_en devuelve el dato que borró
        self.assertEqual(lista.eliminar_en(0), "Tusa")
        self.assertIsNone(lista.cabeza)
        self.assertIsNone(lista.cola)

    # ---------------- VARIOS NODOS ----------------

    def test_insertar_inicio_y_final(self):
        lista = ListaDoble()
        lista.insertar_final("B")
        lista.insertar_final("C")
        lista.insertar_inicio("A")
        self.assertEqual(str(lista), "None <- A <-> B <-> C -> None")
        self.assertEqual(lista.cabeza.dato, "A")
        self.assertEqual(lista.cola.dato, "C")
        self.assertEqual(len(lista), 3)

    def test_insertar_en_posicion(self):
        lista = ListaDoble()
        for letra in ("A", "B", "D", "E"):
            lista.insertar_final(letra)
        lista.insertar_en(2, "C")
        self.assertEqual(str(lista), "None <- A <-> B <-> C <-> D <-> E -> None")
        self.assertEqual(len(lista), 5)

    def test_flechas_de_ida_y_vuelta(self):
        lista = ListaDoble()
        for letra in ("A", "B", "C"):
            lista.insertar_final(letra)
        # desde B se puede ir hacia adelante (C) y hacia atrás (A)
        b = lista.cabeza.siguiente
        self.assertEqual(b.siguiente.dato, "C")
        self.assertEqual(b.anterior.dato, "A")
        # la cabeza no tiene anterior y la cola no tiene siguiente
        self.assertIsNone(lista.cabeza.anterior)
        self.assertIsNone(lista.cola.siguiente)

    def test_eliminar_varios(self):
        lista = ListaDoble()
        for letra in ("A", "B", "C", "D"):
            lista.insertar_final(letra)
        lista.eliminar("A")    # la cabeza
        self.assertEqual(lista.cabeza.dato, "B")
        lista.eliminar("C")    # uno del medio
        self.assertEqual(str(lista), "None <- B <-> D -> None")
        lista.eliminar("D")    # la cola
        self.assertEqual(lista.cola.dato, "B")
        self.assertIsNone(lista.cola.siguiente)
        self.assertEqual(len(lista), 1)

    def test_eliminar_en_varios(self):
        lista = ListaDoble()
        for numero in (1, 2, 3, 4, 5, 6):
            lista.insertar_final(numero)
        # posición en la primera mitad: se llega desde la cabeza
        self.assertEqual(lista.eliminar_en(1), 2)
        # posición en la segunda mitad: se llega desde la cola
        self.assertEqual(lista.eliminar_en(3), 5)
        self.assertEqual(str(lista), "None <- 1 <-> 3 <-> 4 <-> 6 -> None")
        # borrar la última posición actualiza la cola
        self.assertEqual(lista.eliminar_en(len(lista) - 1), 6)
        self.assertEqual(lista.cola.dato, 4)
        self.assertIsNone(lista.cola.siguiente)

    def test_buscar_varios(self):
        lista = ListaDoble()
        for letra in ("A", "B", "C"):
            lista.insertar_final(letra)
        self.assertEqual(lista.buscar("A"), 0)
        self.assertEqual(lista.buscar("C"), 2)
        self.assertEqual(lista.buscar("Z"), -1)

    def test_recorrer_inverso(self):
        lista = ListaDoble()
        for numero in (1, 2, 3):
            lista.insertar_final(numero)
        # va desde la cola hacia atrás usando la flecha "anterior"
        self.assertEqual(lista.recorrer_inverso(), "3 <-> 2 <-> 1")

    # ---------------- POSICIÓN INVÁLIDA ----------------

    def test_posicion_invalida(self):
        lista = ListaDoble()
        lista.insertar_final("A")
        lista.insertar_final("B")
        with self.assertRaises(IndexError):
            lista.insertar_en(5, "X")
        with self.assertRaises(IndexError):
            lista.eliminar_en(2)    # solo existen las posiciones 0 y 1
        with self.assertRaises(IndexError):
            lista.eliminar_en(-1)


if __name__ == "__main__":
    unittest.main()
