dice1 = int(input())
dice2 = int(input())

sum = dice1 + dice2

if sum % 4 == 0:
    print("%d is multiple of 2 and 4." % sum)
elif sum % 2 == 0:
    print("%d is multiple of 2." % sum)
else :
    print("%d is not multiple of 2 or 4." % sum)