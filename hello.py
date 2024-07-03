import random

answer_number = random.randint(1,100)
print(answer_number)

count = 0

while True:
    count = count +1
    print(f"{count}번째 시도입니다!")

    my_guess = int(input('1~100 사이의 숫자를 입력하세요.'))
    if answer_number == my_guess:
        print("정답입니다.")
        print(f"{count}번 만에 맞췄습니다!")
        break
    elif answer_number > my_guess:
        print("UP")
    else:
        print("DOWN")