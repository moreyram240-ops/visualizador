# sort_template.py
# Plantilla mínima para crear un algoritmo nuevo

items = []
n = 0

def init(vals):
    global items, n
    items = list(vals)
    n = len(items)
    # inicializar punteros/estado

def step():
    # implementar un micro-paso y devolver:
    # {"a": int, "b": int, "swap": bool, "done": bool}
    return {"done": True}
