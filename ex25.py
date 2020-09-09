n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
n3 = int(input("n3 = "))

min = n1

if n2 < min:
    min = n2

if n3 < min:
    min = n3

print("Min =",min)