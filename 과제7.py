a = list()
cnt = 0
flag = False

while True:
    flag = False
    num = int(input())

    if cnt == 0:
        a.append(num)
        cnt += 1
    else:
        for i in a:
            if i == num:
                flag = True

        if flag:
            continue
        else:
            a.append(num)
            cnt += 1

    if cnt == 5:
        break

print(a)