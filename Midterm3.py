A = int(input())
B = int(input())
oper = input()

if oper == "-":
    res = A-B
    print("%d %s %d = %d" %(A, oper, B, res))
    if res < 0:
        print("MINUS")
    else :
        print("PLUS")
elif oper == "+":
    res = A+B
    print("%d %s %d = %d" %(A, oper, B, res))
    if res < 0:
        print("MINUS")
    else :
        print("PLUS")
elif oper == "*":
    res = A*B
    print("%d %s %d = %d" %(A, oper, B, res))
    if res < 0:
        print("MINUS")
    else :
        print("PLUS")
else :
    print("error")