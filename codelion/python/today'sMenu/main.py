import random
import time

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

# 메뉴 추가
while True:
    print(lunch)
    item = input("음식을 추가해주세요 : ")
    if (item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)

# 메뉴 삭제
set_lunch = set(lunch)
while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")
    if (item == "q"):
        break
    set_lunch = set_lunch - set([item])
print(set_lunch, "중에서 선택합니다.")

# 5초 카운트 다운
for a in range(5, 0, -1):   # range(start, stop, step)
    print(a)
    time.sleep(1)

# 결과 출력
print(random.choice(list(set_lunch)))