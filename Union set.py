# Union set

def union(a, b):
    res = []

    for i in a:
        res.append(i)
    for i in b:
        res.append(i)

    res = set(res)
    return res