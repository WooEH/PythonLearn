# 10 - 20대의 체력을 측정하려고 한다. 체력 측정의 종목은 팔굽혀펴기, 윗몸일으키기 두 개이며,
# 이 두 종목을 합산하여 등급을 매길 예정이다.
# 총점 합산에 있어서 반영 비는 다음과 같다.
# 남성(팔굽-60%, 윗몸-40%)
# 여성(팔굽-40%, 윗몸-60%)
# 총점을 바탕으로 등급을 매기는데, 연령대에 따라 다른 기준을 적용한다.
# (20대의 경우 70 이상 : A, 50 이상 70 미만 : B, 50 미만 : C,
# 10대의 경우 60 이상 : A, 40 이상 60 미만 : B, 40미만 : C)
# 총점과 등급을 출력하는 프로그램을 작성하라.

age = int(input())
push_up = int(input())
sit_up = int(input())
gender = input()
total = 0
grade = ""

if gender == "F":
    total = push_up * 0.4 + sit_up * 0.6
    if 20 <= age <= 29:
        if total >= 70:
            grade = "A"
        elif total >= 50:
            grade = "B"
        else:
            grade = "C"
    elif 10 <= age <= 19:
        if total >= 60:
            grade = "A"
        elif total >= 40:
            grade = "B"
        else:
            grade = "C"
elif gender == "M":
    total = push_up * 0.6 + sit_up * 0.4
    if 20 <= age <= 29:
        if total >= 70:
            grade = "A"
        elif total >= 50:
            grade = "B"
        else:
            grade = "C"
    elif 10 <= age <= 19:
        if total >= 60:
            grade = "A"
        elif total >= 40:
            grade = "B"
        else:
            grade = "C"

print("total = %d" % total)
print(grade)