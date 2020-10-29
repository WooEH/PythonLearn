def selection_sort(a):
    n = len(a)

    for i in range(0, n-1):
        max_ind = i

        for j in range(i+1, n):
            if a[max_ind] < a[j]:
                max_ind = j

        temp = a[i]
        a[i] = a[max_ind]
        a[max_ind] = temp