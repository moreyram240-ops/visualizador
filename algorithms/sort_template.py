items = []
n = 0
i = 0
j = 0
fase = ""
done_flag = False

def init(vals):
    global items, n, i, j, fase, done_flag
    items = list(vals)
    n = len(items)
    i = 0
    j = 0
    fase = ""
    done_flag = (n <= 1)

def step():
    global items, n, i, j, fase, done_flag

    if done_flag or n <= 1:
        return {"done": True}

    return {"done": True}
