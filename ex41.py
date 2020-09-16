print("1. Orange juice")
print("2. Soda")
print("3. Cola")

price = 0
money = 0

choice = int(input("What do you want? = "))

if choice == 1:
    price = 600
elif choice == 2:
    price = 700
elif choice == 3:
    price = 900

price_check = price
money_check = 0

while True:
    print("Please insert coin = %d" % price_check)
    money = int(input("coin = "))

    price_check -= money
    money_check += money

    if price_check <= 0:
        change = money_check - price

        print("Click!!! Here is your drink!")
        print("Change = %d" % change)
        break

    if money == 0:
        print()
        print("Cancel")
        break
