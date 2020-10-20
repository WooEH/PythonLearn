kor_score = list()
sum = 0

while True:
    kor_sco = int(input())

    if kor_sco == 0:
        break

    kor_score.append(kor_sco)

print(kor_score)

for i in kor_score:
    sum += i

avg = sum / len(kor_score)

print("Avg = %.2f" % avg)