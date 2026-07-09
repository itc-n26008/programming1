import random

numbers = ['0','1','2','3','4','5','6','7','8','9']
answer = ''.join(random.sample(numbers, 3))

while True:
    guess = input("3桁の数字を入力: ")

    strike = 0
    ball = 0

    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1

    if strike == 3:
        print("正解！")
        break
    else:
        print(f"{strike}ストライク {ball}ボール")
