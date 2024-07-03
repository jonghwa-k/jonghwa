import random

rsp = ['Rock', 'Scissor', 'Paper']
computer_pick = random.choice(rsp)
player = input("가위,바위,보 중에 하나를 선택하세요.")

if player == computer_pick:
    print('비겼습니다.')
elif (player == 'Rock'and computer_pick == 'Paper') or (player == 'Scissor' and computer_pick == 'Rock') or (player == 'Paper' and computer_pick == 'Scissor'):
    print('졌습니다.')
else:
    print('이겼습니다.')