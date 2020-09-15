n = int(input())

num = 1
fac = 1

while fac < n:
    num += 1
    fac *= num

print("Num = %d" % num)
print("Total = %d" % fac)