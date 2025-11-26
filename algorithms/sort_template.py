# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
# Agregá acá tus punteros/estado, p.ej.:
# i = 0; j = 0; fase = "x"; stack = []

def init(vals):
    global items, n
    items = list(vals)
    n = len(items)
    # TODO: inicializar punteros/estado

def step():
    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    return {"done": True}
