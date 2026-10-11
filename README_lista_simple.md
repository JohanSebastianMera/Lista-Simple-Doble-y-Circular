# Lista simple – Lista de compras del mercado

Programa en Python que usa una lista enlazada simple para manejar una
lista de compras desde un menú en la consola.

## ¿Qué es una lista simple?

Es una cadena de nodos. Cada nodo guarda un dato y una flecha al
siguiente nodo. El último apunta a `None` (no hay más).
cabeza
  ↓
[Arroz] → [Leche] → [Huevos] → None

## Archivos

¿Para que sirven?

| `nodos.py` | Tiene la clase `Nodo` (el dato y la flecha al siguiente). |
| `lista_simple.py` | Tiene la clase `ListaSimple` y el menú. |

Los dos archivos deben estar en la misma carpeta.

## ¿Cómo se ejecuta?

Se necesita Python: 3.10 o superior. 
Terminal o consola ejecutar: python lista_simple.py

## Métodos de la clase `ListaSimple`

¿Qué hace?
| `esta_vacia()` | `True` si la lista está vacía, `False` si tiene algo. 
| `len(lista)` | Cuántos datos hay. 
| `vaciar()` | Borra toda la lista. 
| `insertar_inicio(dato)` | Agrega el dato de primero. 
| `insertar_final(dato)` | Agrega el dato de último. 
| `insertar_en(pos, dato)` | Agrega el dato en una posición. Si no existe, da error. 
| `eliminar(dato)` | Borra el dato. `True` si lo borró, `False` si no estaba. 
| `buscar(dato)` | Dice la posición del dato, o `-1` si no está. 
| `print(lista)` / `recorrer()` | Muestra la lista: `Arroz,Leche,Huevos,None` 
| `recorrer_inverso()` | Muestra la lista del último al primero (de forma recursiva). 
| `invertir()` | Le da la vuelta a la lista cambiando las flechas. 

> Nota:**Posiciones:** la lista cuenta desde **0**, pero el menú pide el puesto desde **1**.

## Menú

| Opción | ¿Qué hace? |
|---|---|
| 1 | Compra urgente: agrega el producto al inicio. |
| 2 | Anota un producto al final. |
| 3 | Anota un producto en un puesto. |
| 4 | Tacha (elimina) un producto ya comprado. |
| 5 | Busca un producto y dice su puesto. |
| 6 | Dice cuántos productos faltan. |
| 7 | Muestra la lista de abajo hacia arriba. |
| 8 | Le da la vuelta a la lista. |
| 9 | Carga un mercado de ejemplo: Arroz, Leche, Huevos, Pan, Café, Panela y Queso. |
| 0 | Salir. |

## Ejemplo

Elige una opción: 9
Se cargó el mercado de ejemplo.

Elige una opción: 6
Faltan 7 producto(s) por comprar.

Elige una opción: 7
De abajo hacia arriba: Queso,Panela,Café,Pan,Huevos,Leche,Arroz

Elige una opción: 8
Lista invertida: ahora el último va primero.

Elige una opción: 0
¡Buen mercado!