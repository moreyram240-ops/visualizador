# Selection Sort - paso-a-paso

items = []
n = 0
i = 0
j = 1
min_index = 0
comparisons = 0
swaps = 0

def init(vals):
    global items, n, i, j, min_index, comparisons, swaps
    items = list(vals)
    n = len(items)
    i = 0
    j = 1
    min_index = 0
    comparisons = 0
    swaps = 0

def step():
    global items, n, i, j, min_index, comparisons, swaps

    if i >= n - 1:
        return {"done": True}

    comparisons += 1

    if items[j] < items[min_index]:
        min_index = j

    j += 1

    if j >= n:
        items[i], items[min_index] = items[min_index], items[i]
        swaps += 1

        i += 1
        min_index = i
        j = i + 1

        return {"a": i, "b": min_index, "swap": True, "done": False}

    return {"a": j, "b": min_index, "swap": False, "done": False}
  
