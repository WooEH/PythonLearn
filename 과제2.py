#상품의 가격을 입력받는다.
# 만일 상품의 가격이 10000원 이상이면 10%의 할인율을 적용한 값과 “expensive”를 출력한다.
# 다음으로 상품이 10000원 미만 5000원 이상일 경우 20%의 할인율을 적용하고 “appropriate”을 출력하고,
# 5000원 미만 일 경우 50%의 할인율을 적용한 후 “cheap“을 출력하는 프로그램을 작성하라.

price = int(input())
message = "cheap"

if price >= 10000:
    price *= 0.9
    message = "expensive"
elif price >= 5000:
    price *= 0.8
    message = "appropriate"
else :
    price *= 0.5

print("price : %d"%price)
print(message)