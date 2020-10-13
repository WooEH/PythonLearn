def get_gcd(n1, n2):
    res = 1
    if n1 >= n2:
        small = n2
    else :
        small = n1

    for i in range(1, small+1):
        if n1 % i == 0 and n2 % i == 0 :
            res = i
    return res

n1 = int(input())
n2 = int(input())
print(get_gcd(n1, n2))