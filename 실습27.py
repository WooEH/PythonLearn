def getMax(n):
    max = n[0]
    for i in range(4):
        if n[i] > max:
            max = n[i]

        print(i, max)
    print("Max = %d" % max);



a = [2, 3, 1, 4]
print("a =", a)
getMax(a)
