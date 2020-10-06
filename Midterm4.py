num = int(input())
sumHei = 0
flag = 0

for i in range(num):
    hei = int(input())

    if hei > 100:
        sumHei += hei
    else :
        flag += 1

avg = sumHei / (num - flag)

print("Avg = %d cm" % avg)
