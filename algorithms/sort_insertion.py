# Insertion Sort paso-a-paso

items = []
n = 0
i = 1
j = None
key = None
state = "load_key"
comparisons = 0
swaps = 0

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

    if i >= n:
        return {"done": True}

    if state == "load_key":
        key = items[i]
        j = i - 1
        state = "compare_shift"
        return {"a": i, "b": j, "swap": False, "done": False}

    if state == "compare_shift":
        if j >= 0:
            comparisons += 1
            if items[j] > key:
                items[j + 1] = items[j]
                swaps += 1
                j -= 1
                return {"a": j+1, "b": j+2, "swap": True, "done": False}
            else:
                state = "place_key"
        else:
            state = "place_key"

        return {"a": j, "b": j + 1, "swap": False, "done": False}

    if state == "place_key":
        items[j + 1] = key
        i += 1
        state = "load_key"
        return {"a": j + 1, "b": j + 1, "swap": True, "done": False}
