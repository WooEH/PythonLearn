n = int(input())
score = list()

for i in range(3):
    subject = list()

    for j in range(n):
        subject.append(int(input()))

    score.append(subject)

for i in range(3):
    sum = 0
    avg = 0
    for j in score[i]:
        sum += j
    avg = sum / len(score[i])

    if i == 0:
        print("Kor) sum: %d, avg: %.1f" % (sum, avg))
    elif i == 1:
        print("Eng) sum: %d, avg: %.1f" % (sum, avg))
    elif i == 2:
        print("Math) sum: %d, avg: %.1f" % (sum, avg))