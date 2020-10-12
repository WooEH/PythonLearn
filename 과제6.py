N = int(input())
num = 9

for i in range(N):
    for j in range(N-i):
        print(num, end="")

        num -= 1
        if num == 0:
            num = 9
    print()