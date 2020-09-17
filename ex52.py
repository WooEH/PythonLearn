def enlarge(n: int):
    if n > 0:
        n += 1
    elif n < 0:
        n -= 1

    return n


print(enlarge(3))
print(enlarge(-3))
