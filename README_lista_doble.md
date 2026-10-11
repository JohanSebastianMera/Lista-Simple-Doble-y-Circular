# Lista doble – Reproductor de música

Programa en Python que usa una lista doblemente enlazada para manejar una
playlist desde un menú en la consola.

## ¿Qué es una lista doble?

Es una cadena de nodos. Cada nodo guarda un dato y dos flechas: una al
nodo siguiente y otra al nodo anterior. Por eso se puede avanzar
y también retroceder.

```
        cabeza                                   cola
          ↓                                        ↓
None ← [La Bicicleta] ⇄ [Despacito] ⇄ [Tusa] → None
```

## Archivos

¿Para qué sirve? 

| `nodos.py` | Tiene la clase `NodoDoble` (el dato, la flecha al siguiente y la flecha al anterior). |
| `lista_doble.py` | Tiene la clase `ListaDoble` y el menú. |

Los dos archivos deben estar en la misma carpeta.

## ¿Cómo se ejecuta?

Se necesita Python: 3.10 o superior.
En la terminal o consola ejecutar: python lista_doble.py

## Métodos de la clase `ListaDoble`

 ¿Qué hace? 
|---|---|
| `esta_vacia()` | `True` si la lista está vacía, `False` si tiene algo. 
| `len(lista)` | Cuántos datos hay. 
| `vaciar()` | Borra toda la lista. 
| `insertar_inicio(dato)` | Agrega el dato de primero. 
| `insertar_final(dato)` | Agrega el dato de último (usa la cola, no recorre). 
| `insertar_en(pos, dato)` | Agrega el dato en una posición. Si no existe, da error. 
| `eliminar(dato)` | Borra el dato. `True` si lo borró, `False` si no estaba. 
| `eliminar_en(pos)` | Borra el dato de una posición y lo devuelve. Si no existe, da error. 
| `buscar(dato)` | Dice la posición del dato, o `-1` si no está. 
| `print(lista)` / `recorrer()` | Muestra la lista: `None <- A <-> B <-> C -> None` 
| `recorrer_inverso()` | Muestra la lista del último al primero, usando la flecha "anterior": `C <-> B <-> A` 

**Métodos de apoyo** (los usa la clase por dentro):

| Método | ¿Qué hace? |
|---|---|
| `_nodo_en(pos)` | Busca el nodo de una posición. Si está en la primera mitad empieza desde la cabeza; si está en la segunda mitad, desde la cola. Así optimiza el recorrido. |
| `_desenlazar(nodo)` | Saca un nodo de la lista uniendo a su vecino de atrás con su vecino de adelante. Si era la cabeza o la cola, las actualiza. |

> Nota: **Posiciones:** la lista cuenta desde **0**, pero el menú pide el puesto desde **1**.

## Menú

| Opción | ¿Qué hace? |
|---|---|
| 1 | Agrega una canción al inicio. |
| 2 | Agrega una canción al final. |
| 3 | Agrega una canción en un puesto. |
| 4 | Quita una canción por su nombre. |
| 5 | Quita la canción de un puesto. |
| 6 | Busca una canción y dice su puesto. |
| 7 | Pasa a la **siguiente** canción. |
| 8 | Vuelve a la canción **anterior**. |
| 9 | Muestra la playlist al revés. |
| 10 | Carga una playlist de ejemplo de 7 canciones. |
| 0 | Salir. |

Después de cada opción el programa muestra la playlist y la canción que está
sonando. Si se quita la canción que sonaba, vuelve a sonar la primera.

## Ejemplo

```
Elige una opción: 10
Se cargó la playlist de ejemplo.
Playlist: None <- La Bicicleta <-> Colombia Tierra Querida <-> Despacito <-> La Gota Fría <-> Tusa <-> Me Gustas Tú <-> Hips Don't Lie -> None
Sonando ahora: La Bicicleta

Elige una opción: 7
Sonando ahora: Colombia Tierra Querida

Elige una opción: 8
Sonando ahora: La Bicicleta

Elige una opción: 8
Ya estás en la primera canción.

Elige una opción: 5
Puesto a quitar (1 a 7): 7
Hips Don't Lie salió de la playlist.

Elige una opción: 9
Al revés: Me Gustas Tú <-> Tusa <-> La Gota Fría <-> Despacito <-> Colombia Tierra Querida <-> La Bicicleta

Elige una opción: 0
¡Hasta la próxima canción!
```