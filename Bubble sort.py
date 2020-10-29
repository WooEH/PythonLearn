def bubble_sort(a):
    n = len(a)

    for i in range(n):
        for j in range(n):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
