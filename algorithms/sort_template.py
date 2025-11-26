# Plantilla mínima para crear un algoritmo nuevo

items = []
n = 0

def init(vals):
    global items, n
    items = list(vals)
    n = len(items)

def step():
    return {"done": True}
