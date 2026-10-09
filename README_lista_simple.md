# Lista simple: lista de compras del mercado

## ¿Qué es una lista simple?

Es una fila de "cajitas" (nodos). Cada cajita guarda **un dato** y una
**flecha al siguiente**. La última cajita apunta a `None`, que significa "ya no hay más".

```
cabeza
  ↓
[Arroz] → [Leche] → [Huevos] → None
```

- **cabeza**: es la primera cajita. Desde ella se recorre toda la lista.
- **tamano**: cuenta cuántas cajitas hay.
- Solo se puede caminar **hacia adelante**.

## ¿Cómo se ejecuta?

Desde la carpeta `listas-enlazadas` se abre la terminal y se escribe:

```bash
python lista_simple.py
```

Se necesita Python 3.10 o más nuevo. No hay que instalar nada más.

> El archivo `nodos.py` tiene que estar en la misma carpeta, porque de ahí sale la clase `Nodo`.

## ¿Qué hace cada método?

| Método | ¿Qué hace? |
|---|---|
| `esta_vacia()` | Dice `True` si la lista no tiene nada y `False` si tiene algo. |
| `len(lista)` | Dice cuántos datos hay. |
| `vaciar()` | Borra toda la lista. |
| `insertar_inicio(dato)` | Pone el dato de primero. |
| `insertar_final(dato)` | Pone el dato de último (camina hasta el final). |
| `insertar_en(pos, dato)` | Pone el dato en una posición. Si la posición no existe, da error. |
| `eliminar(dato)` | Borra el dato. Devuelve `True` si lo borró y `False` si no estaba. |
| `buscar(dato)` | Dice en qué posición está el dato, o `-1` si no está. |
| `print(lista)` / `recorrer()` | Muestra la lista así: `Arroz -> Leche -> None`. |
| `recorrer_inverso()` | Muestra la lista del último al primero (usa una función que se llama a sí misma). |
| `invertir()` | Le da la vuelta a la lista cambiando las flechas. **Ahora está comentado en el código** (ver la nota de abajo). |

> **Ojo con las posiciones:** por dentro la lista cuenta desde **0**, pero el
> menú le pide al usuario los puestos desde **1**, como en una lista de papel.
> Por eso el código resta o suma 1.

## Opciones del menú

| Opción | Qué hace en la lista de compras |
|---|---|
| 1 | **Compra urgente**: el producto queda de primero. |
| 2 | **Anotar producto** al final. |
| 3 | **Anotar en un puesto** específico. |
| 4 | **Tachar** un producto que ya se compró. |
| 5 | **¿Ya lo anoté?**: busca un producto y dice su puesto. |
| 6 | **Ver lista**: dice cuántos productos faltan. |
| 7 | **Leer de abajo hacia arriba**. |
| 8 | **Darle la vuelta** a la lista (usa `invertir`). |
| 9 | **Cargar ejemplo**: Arroz, Leche, Huevos, Pan, Café, Panela y Queso. |
| 0 | Salir. |

Después de cada opción el programa muestra cómo quedó la lista.
Si se escribe algo mal (por ejemplo letras donde va un número), sale un
mensaje de error y el programa **no se cierra**.

> **Nota:** el método `invertir()` está comentado (entre `'''`). Mientras siga
> así, la **opción 8 cierra el programa** con un error. Para que funcione hay que
> quitar las `'''` que lo rodean.

## Ejemplo de uso

```
Elige una opción: 9
Se cargó el mercado de ejemplo.
Lista: Arroz -> Leche -> Huevos -> Pan -> Café -> Panela -> Queso -> None

Elige una opción: 4
Producto que ya compraste: Leche
Leche tachado de la lista.
Lista: Arroz -> Huevos -> Pan -> Café -> Panela -> Queso -> None

Elige una opción: 5
Producto a buscar: Café
Café está en el puesto 4
Lista: Arroz -> Huevos -> Pan -> Café -> Panela -> Queso -> None

Elige una opción: 7
De abajo hacia arriba: Queso -> Panela -> Café -> Pan -> Huevos -> Arroz
```
