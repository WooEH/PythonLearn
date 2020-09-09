# card game

card1 = int(input("2~10: "))
card2 = int(input("2~10: "))

sum = card1 + card2
sum %= 10

print(sum)