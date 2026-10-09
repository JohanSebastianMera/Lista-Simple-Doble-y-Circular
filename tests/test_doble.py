"""Pruebas unitarias de la clase ListaDoble.

Ejecutar desde la raíz del proyecto con:
    python -m unittest discover -s tests -v

Asignatura: Estructuras de la Información.
Autores: [NOMBRE 1], [NOMBRE 2], [NOMBRE 3], [NOMBRE 4].
"""

import unittest

from lista_doble import ListaDoble


def crear_lista(*datos: object) -> ListaDoble:
    """Crea una ListaDoble con los datos dados, en el mismo orden.

    Args:
        *datos: valores que se insertan al final, uno por uno.

    Returns:
        ListaDoble: la lista ya cargada.
    """
    lista = ListaDoble()
    for dato in datos:
        lista.insertar_final(dato)
    return lista


class TestListaDobleBase(unittest.TestCase):
    """Clase base con una verificación de integridad de enlaces."""

    def verificar_enlaces(self, lista: ListaDoble) -> None:
        """Comprueba que los enlaces de ida y vuelta sean coherentes.

        Verifica que cabeza.anterior y cola.siguiente sean None, que cada
        nodo.siguiente.anterior sea el propio nodo y que el conteo de
        nodos coincida con len().
        """
        if lista.esta_vacia():
            self.assertIsNone(lista.cabeza)
            self.assertIsNone(lista.cola)
            self.assertEqual(len(lista), 0)
            return
        self.assertIsNone(lista.cabeza.anterior)
        self.assertIsNone(lista.cola.siguiente)
        contador = 0
        actual = lista.cabeza
        while actual is not None:
            contador += 1
            if actual.siguiente is not None:
                self.assertIs(actual.siguiente.anterior, actual)
            else:
                self.assertIs(actual, lista.cola)
            actual = actual.siguiente
        self.assertEqual(contador, len(lista))


class TestListaDobleVacia(TestListaDobleBase):
    """Comportamiento de una lista doble sin nodos."""

    def setUp(self):
        """Crea una lista vacía antes de cada prueba."""
        self.lista = ListaDoble()

    def test_esta_vacia(self):
        """Una lista nueva está vacía, sin cabeza ni cola y con len 0."""
        self.assertTrue(self.lista.esta_vacia())
        self.assertEqual(len(self.lista), 0)
        self.verificar_enlaces(self.lista)

    def test_eliminar_en_vacia(self):
        """Eliminar en una lista vacía devuelve False."""
        self.assertFalse(self.lista.eliminar(1))
        self.assertEqual(len(self.lista), 0)

    def test_buscar_en_vacia(self):
        """Buscar en una lista vacía devuelve -1."""
        self.assertEqual(self.lista.buscar(1), -1)

    def test_str_vacia(self):
        """La representación de una lista vacía es 'None'."""
        self.assertEqual(str(self.lista), "None")
        self.assertEqual(self.lista.recorrer(), "None")
        self.assertEqual(self.lista.recorrer_inverso(), "None")


class TestListaDobleUnNodo(TestListaDobleBase):
    """Casos límite con un solo nodo."""

    def test_insertar_inicio_y_eliminar_unico(self):
        """Insertar un nodo y eliminarlo deja cabeza y cola en None."""
        lista = ListaDoble()
        lista.insertar_inicio(7)
        self.assertIs(lista.cabeza, lista.cola)
        self.assertEqual(str(lista), "None <- 7 -> None")
        self.assertTrue(lista.eliminar(7))
        self.assertIsNone(lista.cabeza)
        self.assertIsNone(lista.cola)
        self.assertEqual(len(lista), 0)

    def test_insertar_final_y_eliminar_en_unico(self):
        """eliminar_en(0) sobre el único nodo deja cabeza y cola en None."""
        lista = ListaDoble()
        lista.insertar_final(7)
        self.assertIs(lista.cabeza, lista.cola)
        self.assertEqual(lista.eliminar_en(0), 7)
        self.assertIsNone(lista.cabeza)
        self.assertIsNone(lista.cola)
        self.assertTrue(lista.esta_vacia())


class TestListaDobleVariosNodos(TestListaDobleBase):
    """Inserciones y eliminaciones con varios nodos."""

    def test_insertar_inicio(self):
        """insertar_inicio agrega delante de la cabeza."""
        lista = ListaDoble()
        for x in (3, 2, 1):
            lista.insertar_inicio(x)
        self.assertEqual(str(lista), "None <- 1 <-> 2 <-> 3 -> None")
        self.assertEqual(len(lista), 3)
        self.verificar_enlaces(lista)

    def test_insertar_final(self):
        """insertar_final agrega después de la cola."""
        lista = crear_lista(1, 2, 3)
        self.assertEqual(str(lista), "None <- 1 <-> 2 <-> 3 -> None")
        self.assertEqual(lista.cola.dato, 3)
        self.assertEqual(len(lista), 3)
        self.verificar_enlaces(lista)

    def test_insertar_en_primera_mitad(self):
        """insertar_en en la primera mitad enlaza los cuatro punteros."""
        lista = crear_lista(1, 3, 4, 5, 6)
        lista.insertar_en(1, 2)
        self.assertEqual(
            str(lista), "None <- 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 -> None"
        )
        self.assertEqual(len(lista), 6)
        self.verificar_enlaces(lista)

    def test_insertar_en_segunda_mitad(self):
        """insertar_en en la segunda mitad (llega desde la cola)."""
        lista = crear_lista(1, 2, 3, 4, 6)
        lista.insertar_en(4, 5)
        self.assertEqual(
            str(lista), "None <- 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 -> None"
        )
        self.verificar_enlaces(lista)

    def test_insertar_en_extremos(self):
        """insertar_en con 0 y con tamano actualiza cabeza y cola."""
        lista = crear_lista(2, 3)
        lista.insertar_en(0, 1)
        lista.insertar_en(len(lista), 4)
        self.assertEqual(str(lista), "None <- 1 <-> 2 <-> 3 <-> 4 -> None")
        self.assertEqual(lista.cabeza.dato, 1)
        self.assertEqual(lista.cola.dato, 4)
        self.verificar_enlaces(lista)

    def test_eliminar_cabeza(self):
        """Eliminar la cabeza deja al segundo como cabeza con anterior None."""
        lista = crear_lista(1, 2, 3)
        self.assertTrue(lista.eliminar(1))
        self.assertEqual(str(lista), "None <- 2 <-> 3 -> None")
        self.assertIsNone(lista.cabeza.anterior)
        self.assertEqual(len(lista), 2)
        self.verificar_enlaces(lista)

    def test_eliminar_medio(self):
        """Eliminar un dato del medio reenlaza a sus dos vecinos."""
        lista = crear_lista(1, 2, 3)
        self.assertTrue(lista.eliminar(2))
        self.assertEqual(str(lista), "None <- 1 <-> 3 -> None")
        self.assertEqual(len(lista), 2)
        self.verificar_enlaces(lista)

    def test_eliminar_cola(self):
        """Eliminar la cola actualiza la cola y su siguiente queda en None."""
        lista = crear_lista(1, 2, 3)
        self.assertTrue(lista.eliminar(3))
        self.assertEqual(str(lista), "None <- 1 <-> 2 -> None")
        self.assertEqual(lista.cola.dato, 2)
        self.assertIsNone(lista.cola.siguiente)
        self.assertEqual(len(lista), 2)
        self.verificar_enlaces(lista)

    def test_eliminar_inexistente(self):
        """Eliminar un dato que no está devuelve False y no cambia nada."""
        lista = crear_lista(1, 2, 3)
        self.assertFalse(lista.eliminar(9))
        self.assertEqual(len(lista), 3)
        self.verificar_enlaces(lista)

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
        """vaciar() deja cabeza y cola en None y tamaño 0."""
        lista = crear_lista(1, 2, 3)
        lista.vaciar()
        self.verificar_enlaces(lista)


class TestListaDoblePosicionInvalida(unittest.TestCase):
    """Validación de posiciones en insertar_en y eliminar_en."""

    def test_insertar_en_invalida(self):
        """insertar_en con posición negativa o mayor que tamano lanza IndexError."""
        lista = crear_lista(1, 2)
        with self.assertRaises(IndexError):
            lista.insertar_en(-1, 0)
        with self.assertRaises(IndexError):
            lista.insertar_en(3, 0)
        self.assertEqual(len(lista), 2)

    def test_eliminar_en_invalida(self):
        """eliminar_en con posición negativa o igual a tamano lanza IndexError."""
        lista = crear_lista(1, 2)
        with self.assertRaises(IndexError):
            lista.eliminar_en(-1)
        with self.assertRaises(IndexError):
            lista.eliminar_en(2)
        self.assertEqual(len(lista), 2)

    def test_eliminar_en_vacia(self):
        """eliminar_en en una lista vacía lanza IndexError."""
        with self.assertRaises(IndexError):
            ListaDoble().eliminar_en(0)


class TestListaDobleEspecial(TestListaDobleBase):
    """Operación especial eliminar_en() y recorrer_inverso()."""

    def test_eliminar_en_primera_mitad(self):
        """eliminar_en en la primera mitad devuelve el dato correcto."""
        lista = crear_lista(1, 2, 3, 4, 5, 6)
        self.assertEqual(lista.eliminar_en(1), 2)
        self.assertEqual(str(lista), "None <- 1 <-> 3 <-> 4 <-> 5 <-> 6 -> None")
        self.assertEqual(len(lista), 5)
        self.verificar_enlaces(lista)

    def test_eliminar_en_segunda_mitad(self):
        """eliminar_en en la segunda mitad (llega desde la cola)."""
        lista = crear_lista(1, 2, 3, 4, 5, 6)
        self.assertEqual(lista.eliminar_en(4), 5)
        self.assertEqual(str(lista), "None <- 1 <-> 2 <-> 3 <-> 4 <-> 6 -> None")
        self.assertEqual(len(lista), 5)
        self.verificar_enlaces(lista)

    def test_eliminar_en_cabeza(self):
        """eliminar_en(0) quita la cabeza."""
        lista = crear_lista(1, 2, 3)
        self.assertEqual(lista.eliminar_en(0), 1)
        self.assertEqual(lista.cabeza.dato, 2)
        self.assertIsNone(lista.cabeza.anterior)
        self.verificar_enlaces(lista)

    def test_eliminar_en_cola(self):
        """eliminar_en(tamano - 1) quita la cola y cola.siguiente es None."""
        lista = crear_lista(1, 2, 3)
        self.assertEqual(lista.eliminar_en(len(lista) - 1), 3)
        self.assertEqual(lista.cola.dato, 2)
        self.assertIsNone(lista.cola.siguiente)
        self.verificar_enlaces(lista)

    def test_eliminar_en_hasta_vaciar(self):
        """Eliminar siempre la posición 0 hasta vaciar deja cabeza y cola en None."""
        lista = crear_lista(1, 2, 3)
        for esperado in (1, 2, 3):
            self.assertEqual(lista.eliminar_en(0), esperado)
            self.verificar_enlaces(lista)
        self.assertIsNone(lista.cabeza)
        self.assertIsNone(lista.cola)

    def test_recorrer_inverso(self):
        """recorrer_inverso muestra los datos de la cola a la cabeza."""
        lista = crear_lista(1, 2, 3)
        self.assertEqual(lista.recorrer_inverso(), "3 <-> 2 <-> 1")
        self.assertEqual(crear_lista(5).recorrer_inverso(), "5")


if __name__ == "__main__":
    unittest.main()
