N = int(input())

for i in range(N):
    for j in range(N):
        if i == j:
            print("O", end="")
        else:
            print("X", end="")
    print()