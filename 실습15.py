num = int(input())

sum1 = 0
sum2 = 0

for i in range(1, num+1):
    if i % 2 == 0:
        sum2 += i
    else:
        sum1 += i

print("Sum1 = %d" % sum1)
print("Sum2 = %d" % sum2)
