# Difference set / A - B

def difference(a, b):
    res = []

    for i in a:
        if i not in b:
            res.append(i)
    res = set(res)
    return res