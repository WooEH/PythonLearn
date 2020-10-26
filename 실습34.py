n = int(input())
li = list()
totalSum = 0

for i in range(n):
    s = int(input())

    if s >= 0:
        totalSum += s
    else:
        s = -s

    li.append(s)

li.sort()
print(li)
print("Sum = %d" % totalSum)
