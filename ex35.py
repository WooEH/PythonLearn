dice = int(input("dice = "))
sum = dice
count = 1

while dice != 4:
    dice = int(input("dice = "))
    sum += dice
    count += 1

print("Count = %d" % count)
print("Total = %d" % sum)
