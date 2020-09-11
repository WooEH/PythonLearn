dice1 = int(input("dice1 = "))
dice2 = int(input("dice2 = "))

sum = dice1 + dice2

if sum % 2 == 0:
    if sum % 4 == 0:
        print(sum , "is multiple of 4")
    else :
        print(sum , "is multiple of 2")
else :
    print(sum , "is not multiple of 2 or 4")