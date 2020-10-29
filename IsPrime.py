# Prime number judge

def IsPrime(a):
    cnt = 0

    for i in range(1, a+1):
        if a % i ==0:
            cnt += 1

    if cnt == 2:
        return True

    return False
