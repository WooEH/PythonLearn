# Intersection set by list

def intersection(a, b):
    res = []

    for i in a:
        if i in b:
            res.append(i)
    res = set(res)
    return res