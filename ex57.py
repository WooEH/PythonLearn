def get_gcd(n1, n2):

    min = n1
    if n2 < min:
        min = n2

    for i in range(1, min + 1):
        if n1 % i == 0 and n2 % i == 0:
            ans = i

    return ans


n1 = int(input())
n2 = int(input())

result = get_gcd(n1, n2)
print(result)