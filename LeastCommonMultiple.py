# Least Common Multiple

def lcm(a, b):
    max = 1

    if a >= b:
        max = a
    else:
        max = b

    while True:
        if max % a == 0 and max % b == 0:
            res = max
            return res
        else:
            max += 1
