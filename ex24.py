n1 = int(input("n1 = "))
n2 = int(input("n2 = "))
n3 = int(input("n3 = "))

max = n1
if n2 > max:
    max = n2

if n3 > max:
    max = n3

print("Max =",max)