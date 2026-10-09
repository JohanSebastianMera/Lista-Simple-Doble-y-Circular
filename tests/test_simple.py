"""Pruebas unitarias de la clase ListaSimple.

Ejecutar desde la raíz del proyecto con:
    python -m unittest discover -s tests -v

Asignatura: Estructuras de la Información.
Autores: [NOMBRE 1], [NOMBRE 2], [NOMBRE 3], [NOMBRE 4].
"""

import unittest

from lista_simple import ListaSimple


def crear_lista(*datos: object) -> ListaSimple:
    """Crea una ListaSimple con los datos dados, en el mismo orden.

    Args:
        *datos: valores que se insertan al final, uno por uno.

    Returns:
        ListaSimple: la lista ya cargada.
    """
    lista = ListaSimple()
    for dato in datos:
        lista.insertar_final(dato)
    return lista


class TestListaSimpleVacia(unittest.TestCase):
    """Comportamiento de una lista simple sin nodos."""

    def setUp(self):
        """Crea una lista vacía antes de cada prueba."""
        self.lista = ListaSimple()

    def test_esta_vacia(self):
        """Una lista nueva está vacía y su longitud es 0."""
        self.assertTrue(self.lista.esta_vacia())
        self.assertEqual(len(self.lista), 0)
        self.assertIsNone(self.lista.cabeza)

    def test_eliminar_en_vacia(self):
        """Eliminar en una lista vacía devuelve False y no cambia el tamaño."""
        self.assertFalse(self.lista.eliminar(1))
        self.assertEqual(len(self.lista), 0)

    def test_buscar_en_vacia(self):
        """Buscar en una lista vacía devuelve -1."""
        self.assertEqual(self.lista.buscar(1), -1)

    def test_str_vacia(self):
        """La representación de una lista vacía es 'None'."""
        self.assertEqual(str(self.lista), "None")
        self.assertEqual(self.lista.recorrer(), "None")


class TestListaSimpleUnNodo(unittest.TestCase):
    """Casos límite con un solo nodo."""

    def test_insertar_y_eliminar_unico(self):
        """Insertar un nodo y eliminarlo deja la lista vacía."""
        lista = ListaSimple()
        lista.insertar_inicio(7)
        self.assertEqual(str(lista), "7 -> None")
        self.assertEqual(len(lista), 1)
        self.assertTrue(lista.eliminar(7))
        self.assertTrue(lista.esta_vacia())
        self.assertIsNone(lista.cabeza)
        self.assertEqual(len(lista), 0)

    def test_insertar_final_en_vacia(self):
        """insertar_final en una lista vacía deja el nodo como cabeza."""
        lista = ListaSimple()
        lista.insertar_final(5)
        self.assertEqual(lista.cabeza.dato, 5)
        self.assertEqual(str(lista), "5 -> None")


class TestListaSimpleVariosNodos(unittest.TestCase):
    """Inserciones y eliminaciones con varios nodos."""

    def test_ejemplo_del_enunciado(self):
        """El ejemplo del enunciado imprime 1 -> 2 -> 3 -> None."""
        lista = ListaSimple()
        for x in (3, 2, 1):
            lista.insertar_inicio(x)
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> None")
        self.assertEqual(len(lista), 3)

    def test_insertar_final(self):
        """insertar_final agrega en orden al final."""
        lista = crear_lista(1, 2, 3)
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> None")
        self.assertEqual(len(lista), 3)

    def test_insertar_en_medio(self):
        """insertar_en coloca el dato en la posición del medio."""
        lista = crear_lista(1, 2, 4)
        lista.insertar_en(2, 3)
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> 4 -> None")
        self.assertEqual(len(lista), 4)

    def test_insertar_en_extremos(self):
        """insertar_en con 0 y con tamano inserta al inicio y al final."""
        lista = crear_lista(2, 3)
        lista.insertar_en(0, 1)
        lista.insertar_en(len(lista), 4)
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> 4 -> None")
        self.assertEqual(len(lista), 4)

    def test_eliminar_cabeza(self):
        """Eliminar el dato de la cabeza mueve la cabeza al segundo nodo."""
        lista = crear_lista(1, 2, 3)
        self.assertTrue(lista.eliminar(1))
        self.assertEqual(str(lista), "2 -> 3 -> None")
        self.assertEqual(len(lista), 2)

    def test_eliminar_medio(self):
        """Eliminar un dato del medio salta ese nodo."""
        lista = crear_lista(1, 2, 3)
        self.assertTrue(lista.eliminar(2))
        self.assertEqual(str(lista), "1 -> 3 -> None")
        self.assertEqual(len(lista), 2)

    def test_eliminar_cola(self):
        """Eliminar el último dato deja al penúltimo apuntando a None."""
        lista = crear_lista(1, 2, 3)
        self.assertTrue(lista.eliminar(3))
        self.assertEqual(str(lista), "1 -> 2 -> None")
        self.assertEqual(len(lista), 2)

    def test_eliminar_inexistente(self):
        """Eliminar un dato que no está devuelve False y no cambia nada."""
        lista = crear_lista(1, 2, 3)
        self.assertFalse(lista.eliminar(9))
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> None")
        self.assertEqual(len(lista), 3)

    def test_eliminar_solo_primera_aparicion(self):
        """Con datos repetidos, eliminar quita solo la primera aparición."""
        lista = crear_lista(1, 2, 1)
        self.assertTrue(lista.eliminar(1))
        self.assertEqual(str(lista), "2 -> 1 -> None")

    def test_buscar(self):
        """buscar devuelve la posición del dato o -1 si no está."""
        lista = crear_lista(10, 20, 30)
        self.assertEqual(lista.buscar(10), 0)
        self.assertEqual(lista.buscar(30), 2)
        self.assertEqual(lista.buscar(99), -1)

    def test_recorrer_igual_a_str(self):
        """recorrer() devuelve el mismo texto que str()."""
        lista = crear_lista(1, 2, 3)
        self.assertEqual(lista.recorrer(), str(lista))

    def test_vaciar(self):
        """vaciar() deja la lista sin nodos y con tamaño 0."""
        lista = crear_lista(1, 2, 3)
        lista.vaciar()
        self.assertTrue(lista.esta_vacia())
        self.assertEqual(len(lista), 0)


class TestListaSimplePosicionInvalida(unittest.TestCase):
    """Validación de posiciones en insertar_en."""

    def test_insertar_en_negativa(self):
        """Una posición negativa lanza IndexError."""
        lista = crear_lista(1, 2)
        with self.assertRaises(IndexError):
            lista.insertar_en(-1, 0)

    def test_insertar_en_mayor_que_tamano(self):
        """Una posición mayor que tamano lanza IndexError."""
        lista = crear_lista(1, 2)
        with self.assertRaises(IndexError):
            lista.insertar_en(3, 0)
        self.assertEqual(len(lista), 2)


class TestListaSimpleEspecial(unittest.TestCase):
    """Operación especial invertir() y recorrer_inverso()."""

    def test_invertir_vacia(self):
        """Invertir una lista vacía la deja vacía."""
        lista = ListaSimple()
        lista.invertir()
        self.assertTrue(lista.esta_vacia())
        self.assertEqual(str(lista), "None")

    def test_invertir_un_nodo(self):
        """Invertir una lista de un nodo no la cambia."""
        lista = crear_lista(1)
        lista.invertir()
        self.assertEqual(str(lista), "1 -> None")
        self.assertEqual(len(lista), 1)

    def test_invertir_varios(self):
        """Invertir varios nodos los deja en orden contrario."""
        lista = crear_lista(1, 2, 3, 4)
        lista.invertir()
        self.assertEqual(str(lista), "4 -> 3 -> 2 -> 1 -> None")
        self.assertEqual(len(lista), 4)

    def test_invertir_dos_veces(self):
        """Invertir dos veces devuelve la lista original."""
        lista = crear_lista(1, 2, 3)
        lista.invertir()
        lista.invertir()
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> None")

    def test_recorrer_inverso(self):
        """recorrer_inverso muestra los datos del final a la cabeza."""
        lista = crear_lista(1, 2, 3)
        self.assertEqual(lista.recorrer_inverso(), "3 -> 2 -> 1")
        # no debe modificar la lista
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> None")

    def test_recorrer_inverso_vacia_y_un_nodo(self):
        """recorrer_inverso en vacía devuelve 'None' y con un nodo su dato."""
        self.assertEqual(ListaSimple().recorrer_inverso(), "None")
        self.assertEqual(crear_lista(5).recorrer_inverso(), "5")


if __name__ == "__main__":
    unittest.main()
