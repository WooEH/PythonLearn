def sum_digit(n):
    sum = 0

    while True:
        sum += n % 10
        n /= 10

        if n == 0:
            return sum

n = int(input())
result = sum_digit(n)
print(result)