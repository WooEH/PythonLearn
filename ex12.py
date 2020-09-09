# 구구단 n 단 출력.

n = int(input("2~9 입력: "))

for i in range(1, 10):
    print("%d x %d = %d"%(n, i, n*i))