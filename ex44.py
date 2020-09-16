num = int(input("num = "))
sum_odd = 0
sum_even = 0

for i in range(1, num+1):
    if i % 2 == 0:
        sum_even += i
    else :
        sum_odd += i

print("Sum1 = %d" % sum_odd)
print("Sum2 = %d" % sum_even)