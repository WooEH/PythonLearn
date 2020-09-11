p1 = int(input("Color(1, 2): "))
p2 = int(input("Color(1. 2): "))

print("1 = Red")
print("2 = Blue")

if p1 == 2:
    p1 = int(input("dice1 = "))
else :
    p1 = 0

if p2 == 2:
    p2 = int(input("dice2 = "))
else :
    p2 = 0

if p1 > p2 :
    print("P1 Win")
elif p2 > p1 :
    print("P2 win")
else :
    print("Draw")