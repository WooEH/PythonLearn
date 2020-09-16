num = int(input("num = "))
res = 0

while num > 0:
    res += num % 10
    num = int(num/10)
    res *= 10

res /= 10
print("Result = %d" % res)