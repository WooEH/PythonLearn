n = int(input())
sum = 0
sco = list()

for i in range(n):
    score = int(input())
    sco.append(score)

for i in sco:
    sum += i

avg = sum / len(sco)

print(sco)
print("Avg = %.2f" % avg)