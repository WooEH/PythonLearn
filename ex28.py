dice1 = int(input("dice1 = "))
dice2 = int(input("dice2 = "))

if dice1 % 2 == 0 :
    if dice2 % 2 ==0 :
        print("All dices are even")
else :
    if dice2 % 2 == 1 :
        print("All dices are odd")