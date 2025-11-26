# sort_selection.py
# Selection Sort paso a paso

items = []
i = 0
j = 0
min_index = 0
n = 0

def init(vals):
    global items, i, j, min_index, n
    items = list(vals)
    n = len(items)
    i = 0
    j = 1
    min_index = 0

def step():
    global items, i, j, min_index, n

    if i >= n - 1:
        return {"done": True}

    a = min_index
    b = j
    swapped = False

    # Comparar
    if items[j] < items[min_index]:
        min_index = j

    j += 1

    # Si terminó la búsqueda del mínimo, hacer swap
    if j >= n:
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
            swapped = True

        i += 1
        min_index = i
        j = i + 1

    return {
        "a": a,
        "b": b,
        "swap": swapped,
        "done": False
    }
