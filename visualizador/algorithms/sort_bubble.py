# sort_bubble.py
# Bubble Sort paso a paso

items = []
i = 0
j = 0
n = 0

def init(vals):
    global items, i, j, n
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, i, j, n

    if i >= n - 1:
        return {"done": True}

    a = j
    b = j + 1
    swapped = False

    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swapped = True

    j += 1
    if j >= n - i - 1:
        j = 0
        i += 1

    return {
        "a": a,
        "b": b,
        "swap": swapped,
        "done": False
    }
