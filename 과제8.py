n = int(input())
a = list()
b = list()
c = list()

for i in range(n):
    num = int(input())
    a.append(num)

    num = int(input())
    b.append(num)

for i in range(n):
    c.append(a[i] + b[n - i - 1])

print("c =", c)