mon = int(input())
tra = input()


if tra == "A":
    food = mon * 0.1
    area = mon * 0.1
    hotel = mon * 0.4
    trans = mon * 0.4
elif tra == "B":
    food = mon * 0.35
    area = mon * 0.35
    hotel = mon * 0.15
    trans = mon * 0.15

print("My choice is %s type." % tra)
print("food = %d" % food)
print("area = %d" % area)
print("hotel = %d" % hotel)
print("trans = %d" % trans)
