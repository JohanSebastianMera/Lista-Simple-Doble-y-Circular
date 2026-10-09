"""Pruebas unitarias de la clase ListaCircular.

Ejecutar desde la raíz del proyecto con:
    python -m unittest discover -s tests -v

Asignatura: Estructuras de la Información.
Autores: [NOMBRE 1], [NOMBRE 2], [NOMBRE 3], [NOMBRE 4].
"""

import unittest

from lista_circular import ListaCircular
from lista_simple import ListaSimple


def crear_lista(*datos: object) -> ListaCircular:
    """Crea una ListaCircular con los datos dados, en el mismo orden.

    Args:
        *datos: valores que se insertan al final, uno por uno.

    Returns:
        ListaCircular: la lista ya cargada.
    """
    lista = ListaCircular()
    for dato in datos:
        lista.insertar_final(dato)
    return lista


class TestListaCircularBase(unittest.TestCase):
    """Clase base con una verificación de integridad del ciclo."""

    def verificar_ciclo(self, lista: ListaCircular) -> None:
        """Comprueba que el ciclo esté bien cerrado.

        Verifica que, partiendo de la cabeza y avanzando exactamente
        tamano pasos, se vuelva a la cabeza; que el nodo anterior a ese
        regreso sea la cola; y que cola.siguiente sea la cabeza.
        """
        if lista.esta_vacia():
            self.assertIsNone(lista.cola)
            self.assertEqual(len(lista), 0)
            return
        cabeza = lista.cola.siguiente
        self.assertIs(lista.cabeza, cabeza)
        actual = cabeza
        for paso in range(len(lista)):
            if paso < len(lista) - 1:
                # antes de la última vuelta no se debe regresar a la cabeza
                self.assertIsNot(actual.siguiente, cabeza)
            ultimo = actual
            actual = actual.siguiente
        self.assertIs(ultimo, lista.cola)
        self.assertIs(actual, cabeza)


class TestListaCircularVacia(TestListaCircularBase):
    """Comportamiento de una lista circular sin nodos."""

    def setUp(self):
        """Crea una lista vacía antes de cada prueba."""
        self.lista = ListaCircular()

    def test_esta_vacia(self):
        """Una lista nueva está vacía, sin cola y con len 0."""
        self.assertTrue(self.lista.esta_vacia())
        self.assertEqual(len(self.lista), 0)
        self.assertIsNone(self.lista.cola)
        self.assertIsNone(self.lista.cabeza)

    def test_eliminar_en_vacia(self):
        """Eliminar en una lista vacía devuelve False."""
        self.assertFalse(self.lista.eliminar(1))

    def test_buscar_en_vacia(self):
        """Buscar en una lista vacía devuelve -1."""
        self.assertEqual(self.lista.buscar(1), -1)

    def test_str_vacia(self):
        """La representación de una lista vacía es '(vacía)'."""
        self.assertEqual(str(self.lista), "(vacía)")
        self.assertEqual(self.lista.recorrer(), "(vacía)")

    def test_rotar_vacia(self):
        """Rotar una lista vacía no falla y la deja vacía."""
        self.lista.rotar(3)
        self.assertTrue(self.lista.esta_vacia())

    def test_josefo_vacia(self):
        """Josefo en una lista vacía devuelve una ListaSimple vacía."""
        orden = self.lista.josefo(3)
        self.assertIsInstance(orden, ListaSimple)
        self.assertTrue(orden.esta_vacia())


class TestListaCircularUnNodo(TestListaCircularBase):
    """Casos límite con un solo nodo."""

    def test_nodo_se_apunta_a_si_mismo(self):
        """Con un solo nodo, cola.siguiente es la propia cola."""
        lista = ListaCircular()
        lista.insertar_inicio(7)
        self.assertIs(lista.cola.siguiente, lista.cola)
        self.assertEqual(str(lista), "7 -> (vuelve a 7)")
        self.verificar_ciclo(lista)

    def test_insertar_y_eliminar_unico(self):
        """Insertar un nodo y eliminarlo deja la cola en None."""
        lista = ListaCircular()
        lista.insertar_final(7)
        self.assertTrue(lista.eliminar(7))
        self.assertIsNone(lista.cola)
        self.assertTrue(lista.esta_vacia())
        self.assertEqual(len(lista), 0)


class TestListaCircularVariosNodos(TestListaCircularBase):
    """Inserciones y eliminaciones con varios nodos."""

    def test_insertar_inicio(self):
        """insertar_inicio agrega antes de la cabeza sin mover la cola."""
        lista = ListaCircular()
        for x in (3, 2, 1):
            lista.insertar_inicio(x)
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> (vuelve a 1)")
        self.assertEqual(lista.cola.dato, 3)
        self.assertEqual(len(lista), 3)
        self.verificar_ciclo(lista)

    def test_insertar_final(self):
        """insertar_final agrega después de la cola y la actualiza."""
        lista = crear_lista(1, 2, 3)
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> (vuelve a 1)")
        self.assertEqual(lista.cola.dato, 3)
        self.assertEqual(len(lista), 3)
        self.verificar_ciclo(lista)

    def test_insertar_en_medio(self):
        """insertar_en coloca el dato en una posición intermedia."""
        lista = crear_lista(1, 2, 4)
        lista.insertar_en(2, 3)
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> 4 -> (vuelve a 1)")
        self.assertEqual(len(lista), 4)
        self.verificar_ciclo(lista)

    def test_insertar_en_extremos(self):
        """insertar_en con 0 y con tamano actualiza cabeza y cola."""
        lista = crear_lista(2, 3)
        lista.insertar_en(0, 1)
        lista.insertar_en(len(lista), 4)
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> 4 -> (vuelve a 1)")
        self.assertEqual(lista.cola.dato, 4)
        self.verificar_ciclo(lista)

    def test_eliminar_cabeza(self):
        """Eliminar la cabeza hace que la cola apunte al segundo nodo."""
        lista = crear_lista(1, 2, 3)
        self.assertTrue(lista.eliminar(1))
        self.assertEqual(str(lista), "2 -> 3 -> (vuelve a 2)")
        self.assertEqual(lista.cola.siguiente.dato, 2)
        self.assertEqual(len(lista), 2)
        self.verificar_ciclo(lista)

    def test_eliminar_medio(self):
        """Eliminar un dato del medio salta ese nodo."""
        lista = crear_lista(1, 2, 3)
        self.assertTrue(lista.eliminar(2))
        self.assertEqual(str(lista), "1 -> 3 -> (vuelve a 1)")
        self.assertEqual(len(lista), 2)
        self.verificar_ciclo(lista)

    def test_eliminar_cola(self):
        """Eliminar la cola hace que el anterior sea la nueva cola."""
        lista = crear_lista(1, 2, 3)
        self.assertTrue(lista.eliminar(3))
        self.assertEqual(str(lista), "1 -> 2 -> (vuelve a 1)")
        self.assertEqual(lista.cola.dato, 2)
        self.assertEqual(len(lista), 2)
        self.verificar_ciclo(lista)

    def test_eliminar_inexistente(self):
        """Eliminar un dato que no está devuelve False sin ciclo infinito."""
        lista = crear_lista(1, 2, 3)
        self.assertFalse(lista.eliminar(9))
        self.assertEqual(len(lista), 3)
        self.verificar_ciclo(lista)

    def test_buscar(self):
        """buscar devuelve la posición del dato o -1 sin ciclo infinito."""
        lista = crear_lista(10, 20, 30)
        self.assertEqual(lista.buscar(10), 0)
        self.assertEqual(lista.buscar(30), 2)
        self.assertEqual(lista.buscar(99), -1)

    def test_recorrer_igual_a_str(self):
        """recorrer() devuelve el mismo texto que str()."""
        lista = crear_lista(1, 2, 3)
        self.assertEqual(lista.recorrer(), str(lista))

    def test_vaciar(self):
        """vaciar() deja la cola en None y tamaño 0."""
        lista = crear_lista(1, 2, 3)
        lista.vaciar()
        self.verificar_ciclo(lista)
        self.assertEqual(str(lista), "(vacía)")


class TestListaCircularPosicionInvalida(unittest.TestCase):
    """Validación de posiciones en insertar_en."""

    def test_insertar_en_invalida(self):
        """insertar_en con posición negativa o mayor que tamano lanza IndexError."""
        lista = crear_lista(1, 2)
        with self.assertRaises(IndexError):
            lista.insertar_en(-1, 0)
        with self.assertRaises(IndexError):
            lista.insertar_en(3, 0)
        self.assertEqual(len(lista), 2)


class TestListaCircularEspecial(TestListaCircularBase):
    """Operaciones especiales josefo() y rotar()."""

    def test_josefo_1_a_7_con_k_3(self):
        """josefo(3) con 1..7 elimina en el orden 3, 6, 2, 7, 5, 1, 4."""
        lista = crear_lista(1, 2, 3, 4, 5, 6, 7)
        orden = lista.josefo(3)
        self.assertIsInstance(orden, ListaSimple)
        self.assertEqual(str(orden), "3 -> 6 -> 2 -> 7 -> 5 -> 1 -> 4 -> None")
        self.assertEqual(len(orden), 7)
        # la circular queda vacía
        self.assertTrue(lista.esta_vacia())
        self.assertIsNone(lista.cola)

    def test_josefo_k_1(self):
        """josefo(1) elimina en el mismo orden de la lista."""
        lista = crear_lista(1, 2, 3)
        self.assertEqual(str(lista.josefo(1)), "1 -> 2 -> 3 -> None")

    def test_josefo_k_invalido(self):
        """josefo con k menor que 1 lanza ValueError y no modifica la lista."""
        lista = crear_lista(1, 2, 3)
        with self.assertRaises(ValueError):
            lista.josefo(0)
        self.assertEqual(len(lista), 3)
        self.verificar_ciclo(lista)

    def test_rotar_2(self):
        """rotar(2) sobre 1..5 deja la cabeza en 3."""
        lista = crear_lista(1, 2, 3, 4, 5)
        lista.rotar(2)
        self.assertEqual(lista.cabeza.dato, 3)
        self.assertEqual(lista.cola.dato, 2)
        self.assertEqual(str(lista), "3 -> 4 -> 5 -> 1 -> 2 -> (vuelve a 3)")
        self.assertEqual(len(lista), 5)
        self.verificar_ciclo(lista)

    def test_rotar_mayor_que_tamano(self):
        """rotar(n) con n mayor que el tamaño equivale a rotar(n % tamano)."""
        lista = crear_lista(1, 2, 3, 4, 5)
        lista.rotar(12)  # 12 % 5 = 2
        self.assertEqual(lista.cabeza.dato, 3)
        self.verificar_ciclo(lista)

    def test_rotar_multiplo_del_tamano(self):
        """rotar(tamano) deja la lista igual."""
        lista = crear_lista(1, 2, 3)
        lista.rotar(3)
        self.assertEqual(str(lista), "1 -> 2 -> 3 -> (vuelve a 1)")
        self.verificar_ciclo(lista)

    def test_rotar_negativo(self):
        """rotar(-1) rota una posición hacia la derecha."""
        lista = crear_lista(1, 2, 3, 4)
        lista.rotar(-1)
        self.assertEqual(lista.cabeza.dato, 4)
        self.verificar_ciclo(lista)

    def test_cola_apunta_a_cabeza_tras_cada_operacion(self):
        """cola.siguiente sigue siendo la cabeza después de cada operación."""
        lista = ListaCircular()
        operaciones = [
            lambda: lista.insertar_final(1),
            lambda: lista.insertar_inicio(0),
            lambda: lista.insertar_final(3),
            lambda: lista.insertar_en(2, 2),
            lambda: lista.rotar(1),
            lambda: lista.eliminar(0),
            lambda: lista.eliminar(3),
            lambda: lista.rotar(5),
            lambda: lista.eliminar(1),
            lambda: lista.eliminar(2),
        ]
        for operacion in operaciones:
            operacion()
            self.verificar_ciclo(lista)
        self.assertTrue(lista.esta_vacia())


if __name__ == "__main__":
    unittest.main()
