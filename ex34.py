sum = 0
count = 0

while sum < 20:
    dice = int(input("dice = "))
    count += 1
    sum += dice

print("Count = %d" % count)
print("Total = %d" % sum)
