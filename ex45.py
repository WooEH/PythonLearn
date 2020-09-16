num = int(input("num = "))
sum = 0
count = 0

for i in range(3, num+1, 3):
    sum += i
    count += 1

print("Count = %d" % count)
print("Sum = %d" % sum)
