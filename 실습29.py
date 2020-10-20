n = int(input())
score = list()

for i in range(n):
    s = int(input())
    score.append(s)

max = score[0]
min = score[0]

for i in score:
    if i > max:
        max = i

    if i < min:
        min = i

print("max = %d" % max)
print("min = %d" % min)