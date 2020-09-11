print("상품 종류\t상품 번호\t판매 가격(원/개)")
print("배추\t1\t5000")
print("무\t2\t2000")
print("상추\t3\t3000")

cho = int(input("1~3 : "))
num = int(input("0 이상 : "))

if cho == 1:
    price = num * 5000
elif cho == 2:
    price = num * 2000
else :
    price = num * 3000

print(price)