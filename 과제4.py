N = int(input())
M = int(input())

ans = [1]
sum = 1

for i in range(1, M):
    ans.append(ans[i-1] + N)
    sum += ans[i]

for i in ans:
    print(i)
print("Total = %d" % sum)
