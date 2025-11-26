# sort_insertion.py
# Insertion Sort paso a paso

items = []
i = 1
j = 1
key = None
n = 0

def init(vals):
    global items, i, j, key, n
    items = list(vals)
    n = len(items)
    i = 1
    j = 1
    key = items[1] if n > 1 else None

def step():
    global items, i, j, key, n

    if i >= n:
        return {"done": True}

    a = j - 1
    b = j
    swapped = False

    if j > 0 and items[a] > key:
        items[b] = items[a]
        j -= 1
        swapped = True
    else:
        items[j] = key
        i += 1
        if i < n:
            key = items[i]
            j = i

    return {
        "a": a if a >= 0 else 0,
        "b": b if b < n else n-1,
        "swap": swapped,
        "done": False
    }
