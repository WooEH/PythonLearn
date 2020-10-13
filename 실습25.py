a = [5, 2, 4, 1, 3]
print(a)
#a.sort()
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)