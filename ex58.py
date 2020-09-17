n1 = int(input())
n2 = int(input())

def count_zero(n1, n2):
    count = 0

    for i in range(n1, n2+1):
        while i > 0:
            if i % 10 == 0:
                count += 1

            i = int(i / 10)

    return count


result = count_zero(n1, n2)
print(result)