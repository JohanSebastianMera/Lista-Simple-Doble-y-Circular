# Lista circular – Turnos para lavar los platos

Programa en Python que usa una lista circular para manejar los turnos de
lavar los platos en la casa desde un menú en la consola.

## ¿Qué es una lista circular?

Es una cadena de nodos donde el **último nodo (la cola) apunta otra vez al
primero**, formando un círculo. Así, cuando le toca al último, el turno
vuelve a empezar.

```
        cabeza                     cola
          ↓                         ↓
       [Ana] → [Luis] → [Sofía] → [Carlos]
          ↑                         │
          └─────────────────────────┘
```

- **cola:** el último nodo. Es lo único que guarda la lista.
- **cabeza:** no se guarda, siempre es `cola.siguiente`. En el menú es a quien le toca **hoy**.
- **tamano:** cuántos nodos hay.

> Como ningún nodo apunta a `None`, la lista se recorre con
> `for _ in range(self.tamano)`, que da exactamente una vuelta. Un
> `while actual:` nunca terminaría.

## Archivos

| Archivo | ¿Para qué sirve? |
|---|---|
| `nodos.py` | Tiene la clase `Nodo` (el dato y la flecha al siguiente). |
| `lista_simple.py` | La usa `josefo()` para devolver el orden de salida. |
| `lista_circular.py` | Tiene la clase `ListaCircular` y el menú. |

Los tres archivos deben estar en la misma carpeta.

## ¿Cómo se ejecuta?

Se necesita Python 3.10 o superior.
En la terminal o consola ejecutar:

```bash
python lista_circular.py
```

## Métodos de la clase `ListaCircular`

### `cabeza`
Devuelve el primer nodo (`cola.siguiente`). Se escribe sin paréntesis
(`lista.cabeza`) gracias a `@property`.

### `esta_vacia()`
`True` si la lista está vacía, `False` si tiene algo.

### `len(lista)`
Dice cuántos datos hay.

### `vaciar()`
Borra toda la lista.

### `insertar_inicio(dato)`
Agrega el dato de primero, entre la cola y la cabeza. Si es el único nodo,
se apunta a sí mismo para cerrar el círculo.

### `insertar_final(dato)`
Agrega el dato de último **sin recorrer la lista**: lo inserta al inicio y
luego mueve la cola un paso adelante.

### `insertar_en(pos, dato)`
Agrega el dato en una posición. Si la posición no existe, da error.

### `eliminar(dato)`
Borra el dato. Devuelve `True` si lo borró y `False` si no estaba.

### `buscar(dato)`
Dice la posición del dato, o `-1` si no está.

### `print(lista)` / `recorrer()`
Muestra la lista dando una sola vuelta:
`Ana -> Luis -> Sofía -> (vuelve a Ana)`

### `rotar(n)`
Mueve el círculo `n` posiciones **sin mover los datos**: solo avanza la
cola, y la cabeza avanza con ella. Usa `n % tamano`, así que con 7 personas
rotar 12 es lo mismo que rotar 5.
Ejemplo: `rotar(2)` en `1, 2, 3, 4, 5` deja `3, 4, 5, 1, 2`.

### `josefo(k)`
Cuenta de `k` en `k` alrededor del círculo y saca al que cae en `k`, hasta
que no quede nadie. Devuelve una **lista simple** con el orden en que fueron
saliendo; el último es el "sobreviviente". Si `k` es menor que 1, da error.
**Ojo:** la lista circular queda vacía al terminar.

### Método de apoyo: `_eliminar_siguiente(anterior)`
Lo usa la clase por dentro (`eliminar` y `josefo`). Saca el nodo que está
**después** de `anterior`, porque en esta lista no hay flecha hacia atrás.
Si el nodo quitado era la cola, el anterior pasa a ser la nueva cola.

> Nota: **Posiciones:** la lista cuenta desde **0**, pero el menú pide el puesto desde **1**.

## Menú

| Opción | ¿Qué hace? |
|---|---|
| 1 | Dice a quién le toca hoy y a quién mañana. |
| 2 | Agrega una persona a la que le toca hoy. |
| 3 | Agrega una persona al final de la ronda. |
| 4 | Agrega una persona en un puesto. |
| 5 | Saca a una persona de la ronda. |
| 6 | Dice en cuántos días le toca a una persona. |
| 7 | Pasa al día siguiente (`rotar(1)`). |
| 8 | Adelanta varios días (`rotar(n)`). |
| 9 | **Papa caliente:** decide quién lava en Navidad usando Josefo. Se juega con una copia, así la ronda real no se borra. |
| 10 | Carga una casa de ejemplo: Ana, Luis, Sofía, Carlos, Valentina, Mateo y Laura. |
| 0 | Salir. |

## Ejemplo

```
Elige una opción: 10
Se cargó la casa de ejemplo.

Elige una opción: 1
Hoy lava los platos: Ana
Mañana le toca a: Luis

Elige una opción: 7
Pasó un día. Ahora le toca a Luis

Elige una opción: 8
¿Cuántos días pasaron?: 12
Ahora le toca a Laura

Elige una opción: 6
¿Para quién?: Mateo
A Mateo le toca dentro de 6 día(s).

Elige una opción: 9
¿De cuánto en cuánto se cuenta? (k >= 1): 3
Orden en que van saliendo: Luis,Valentina,Ana,Mateo,Carlos,Laura,Sofía,None
Pierde y lava los platos en Navidad: Sofía

Elige una opción: 0
¡Que nadie se salte su turno!
```
