# sort_bubble.py
# Bubble Sort - implementación paso-a-paso para el visualizador

items = []
n = 0
i = 0      # cantidad de pasadas completas
j = 0      # índice actual dentro de la pasada
comparisons = 0
swaps = 0

def init(vals):
    global items, n, i, j, comparisons, swaps
    items = list(vals)
    n = len(items)
    i = 0
    j = 0
    comparisons = 0
    swaps = 0

def step():
    global items, n, i, j, comparisons, swaps

    if n <= 1 or i >= n - 1:
        # terminado
        return {"done": True}

    a = j
    b = j + 1

    # seguridad: índices válidos
    if b >= n:
        # avanzar fase si por alguna razón j quedó fuera
        j = 0
        i += 1
        return {"a": 0, "b": 0, "swap": False, "done": False}

    comparisons += 1
    if items[a] > items[b]:
        # hacer swap en la lista primero
        items[a], items[b] = items[b], items[a]
        swaps += 1
        swapped = True
    else:
        swapped = False

    # avanzar j; si fin de pasada, reiniciar j y aumentar i
    j += 1
    if j >= n - i - 1:
        j = 0
        i += 1

    return {"a": a, "b": b, "swap": swapped, "done": False}
