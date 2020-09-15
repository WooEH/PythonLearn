total = 0
cnt = 0

while total < 20:

    dice = int(input())

    cnt += 1
    if dice == 4:
        break

    total += dice

print("Count = %d" % cnt)
print("Total = %d" % total)