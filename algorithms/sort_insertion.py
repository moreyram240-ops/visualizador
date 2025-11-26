# sort_insertion.py
# Insertion Sort - paso-a-paso para el visualizador

items = []
n = 0
i = 1            # índice del elemento "key" que vamos a insertar
j = None         # índice para desplazar elementos (j se mueve a la izquierda)
key = None
state = "load_key"  # "load_key", "compare_shift", "place_key"
comparisons = 0
swaps = 0        # para insertion contaremos como "swap" cuando movemos dos índices visualmente

def init(vals):
    global items, n, i, j, key, state, comparisons, swaps
    items = list(vals)
    n = len(items)
    i = 1
    j = None
    key = None
    state = "load_key"
    comparisons = 0
    swaps = 0

def step():
    global items, n, i, j, key, state, comparisons, swaps

    if n <= 1 or i >= n:
        return {"done": True}

    # cargar la clave para insertar
    if state == "load_key":
        key = items[i]
        j = i - 1
        state = "compare_shift"
        # resaltar la posición clave frente a j
        return {"a": i, "b": j, "swap": False, "done": False}

    # comparar y posiblemente desplazar items[j] -> items[j+1]
    if state == "compare_shift":
        if j >= 0:
            comparisons += 1
            a = j
            b = j + 1
            if items[j] > key:
                # desplazar un elemento a la derecha (esto es un movimiento visible)
                items[j + 1] = items[j]
                swaps += 1  # contamos como swap visual (movimiento de columnas)
                j -= 1
                return {"a": a, "b": b, "swap": True, "done": False}
            else:
                # posición encontrada
                state = "place_key"
                return {"a": j, "b": j + 1, "swap": False, "done": False}
        else:
            # j < 0 -> colocamos la key en items[0]
            state = "place_key"
            return {"a": 0, "b": 0, "swap": False, "done": False}

    # colocar la key en j+1
    if state == "place_key":
        dest = j + 1
        items[dest] = key
        # avanzar i y resetear estado
        i += 1
        state = "load_key"
        return {"a": dest, "b": dest, "swap": True, "done": False}

    return {"done": True}
