card1 = int(input("card1(2~10) = "))
card2 = int(input("card2(2~10) = "))

p1 = (card1 + card2) % 10

card1 = int(input("card1(2~10) = "))
card2 = int(input("card2(2~10) = "))

p2 = (card1 + card2) % 10

print("1st User score:",p1)
print("2nd User score:",p2)

if p1 > p2:
    print("1st User Win")
elif p1 < p2:
    print("2nd User Win")
else :
    print("Draw")
