n = int(input())

for hour in range(n+1):
    for min in range(60):
        print("%02d:%02d" % (hour, min))

