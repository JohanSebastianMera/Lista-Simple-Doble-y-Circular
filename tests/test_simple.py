# Pruebas de la lista simple.
# Se ejecutan desde la carpeta del proyecto con:
#   python -m unittest discover -s tests -v

# unittest es la herramienta de Python para hacer pruebas
import unittest

# Estas 3 líneas le dicen a Python dónde están los archivos de las listas
# (la carpeta de arriba de tests), así la prueba funciona desde cualquier lado,
# también con el botón "Run" del editor.
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lista_simple import ListaSimple


# Cada método que empieza con "test_" es una prueba.
# assertEqual(a, b) revisa que a y b sean iguales; si no, la prueba falla.
# assertTrue / assertFalse revisan que algo sea True o False.
class TestListaSimple(unittest.TestCase):

    # ---------------- LISTA VACÍA ----------------

    def test_lista_vacia(self):
        lista = ListaSimple()
        self.assertTrue(lista.esta_vacia())
        self.assertEqual(len(lista), 0)
        self.assertEqual(str(lista), "None")
        # en una lista vacía no hay nada que borrar ni encontrar
        self.assertFalse(lista.eliminar("Arroz"))
        self.assertEqual(lista.buscar("Arroz"), -1)

    def test_invertir_lista_vacia(self):
        lista = ListaSimple()
        lista.invertir()
        # invertir una lista vacía no debe dañar nada
        self.assertTrue(lista.esta_vacia())

    # ---------------- UN SOLO NODO ----------------

    def test_un_nodo(self):
        lista = ListaSimple()
        lista.insertar_inicio("Arroz")
        self.assertFalse(lista.esta_vacia())
        self.assertEqual(len(lista), 1)
        self.assertEqual(str(lista), "Arroz,None")
        self.assertEqual(lista.buscar("Arroz"), 0)

    def test_un_nodo_eliminar(self):
        lista = ListaSimple()
        lista.insertar_final("Arroz")
        self.assertTrue(lista.eliminar("Arroz"))
        # al borrar el único nodo la lista vuelve a quedar vacía
        self.assertTrue(lista.esta_vacia())
        self.assertIsNone(lista.cabeza)    # assertIsNone revisa que sea None
        self.assertEqual(len(lista), 0)

    def test_un_nodo_invertir(self):
        lista = ListaSimple()
        lista.insertar_inicio("Arroz")
        lista.invertir()
        # con un solo dato, invertir deja todo igual
        self.assertEqual(str(lista), "Arroz,None")

    # ---------------- VARIOS NODOS ----------------

    def test_insertar_inicio(self):
        lista = ListaSimple()
        # cada dato nuevo queda de primero, por eso salen al revés
        lista.insertar_inicio(3)
        lista.insertar_inicio(2)
        lista.insertar_inicio(1)
        self.assertEqual(str(lista), "1,2,3,None")
        self.assertEqual(len(lista), 3)

    def test_insertar_final(self):
        lista = ListaSimple()
        lista.insertar_final("Arroz")
        lista.insertar_final("Leche")
        lista.insertar_final("Huevos")
        self.assertEqual(str(lista), "Arroz,Leche,Huevos,None")
        self.assertEqual(len(lista), 3)

    def test_insertar_en_posicion(self):
        lista = ListaSimple()
        lista.insertar_final("Arroz")
        lista.insertar_final("Huevos")
        lista.insertar_en(1, "Leche")    # la posición 1 es la segunda
        self.assertEqual(str(lista), "Arroz,Leche,Huevos,None")
        self.assertEqual(len(lista), 3)

    def test_eliminar_varios(self):
        lista = ListaSimple()
        for producto in ("Arroz", "Leche", "Huevos", "Pan"):
            lista.insertar_final(producto)
        lista.eliminar("Arroz")    # el primero (la cabeza)
        self.assertEqual(str(lista), "Leche,Huevos,Pan,None")
        lista.eliminar("Huevos")   # uno del medio
        self.assertEqual(str(lista), "Leche,Pan,None")
        lista.eliminar("Pan")      # el último
        self.assertEqual(str(lista), "Leche,None")
        self.assertEqual(len(lista), 1)
        # si el dato no está, devuelve False y no cambia nada
        self.assertFalse(lista.eliminar("Queso"))
        self.assertEqual(len(lista), 1)

    def test_buscar_varios(self):
        lista = ListaSimple()
        for producto in ("Arroz", "Leche", "Huevos"):
            lista.insertar_final(producto)
        self.assertEqual(lista.buscar("Arroz"), 0)
        self.assertEqual(lista.buscar("Huevos"), 2)
        self.assertEqual(lista.buscar("Queso"), -1)

    def test_invertir_varios(self):
        lista = ListaSimple()
        for numero in (1, 2, 3, 4):
            lista.insertar_final(numero)
        lista.invertir()
        self.assertEqual(str(lista), "4,3,2,1,None")

    def test_recorrer_inverso(self):
        lista = ListaSimple()
        for numero in (1, 2, 3):
            lista.insertar_final(numero)
        self.assertEqual(lista.recorrer_inverso(), "3,2,1")
        # recorrer al revés solo muestra, no cambia la lista
        self.assertEqual(str(lista), "1,2,3,None")

    # ---------------- POSICIÓN INVÁLIDA ----------------

    def test_posicion_invalida(self):
        lista = ListaSimple()
        lista.insertar_final("Arroz")
        # assertRaises revisa que el código de adentro lance ese error
        with self.assertRaises(IndexError):
            lista.insertar_en(5, "Leche")
        with self.assertRaises(IndexError):
            lista.insertar_en(-1, "Leche")


# Permite correr este archivo solo
if __name__ == "__main__":
    unittest.main()
