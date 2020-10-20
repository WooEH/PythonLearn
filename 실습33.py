p = [0, 0, 0]

n = int(input())

for i in range(n):
    for j in range(3):
        temp = int(input())

        if p[j] < temp:
            p[j] = temp
    print(p)

max = max(p)

if max == p[0]:
    print("Person1 Win")
elif max == p[1]:
    print("Person2 Win")
else :
    print("Person3 Win")