n1 = int(input("n1 = "))
n2 = int(input("n2 = "))

if n1 > n2:
    tmp = n1
    n1 = n2
    n2 = tmp

print("n1 = %d n2 = %d"%(n1,n2))