import random
numbers=['0','1','2','3','4','5','6','7','8','9']
sample4=random.sample(numbers, k=4)
num4=''.join(sample4)
while True:
    val = input()
    if val == num4:
        print('OK')
        break
    else:
        print(val,':NG')
"""実行結果 入れた数字があってたらOK、間違ってたらNGが出る、当たるまで
sampleは、重複無しで一部を取り出す　randomがついてるから、ランダムに取る
数字の中からランダムで重複せず、４つ数字を取るk=4のとこkはしていされてて、
他の英語じゃだめ。取り出すという意味らしい？
リストの数字をくっつける　''.joinのとこ
joinは、リストの中身をくっつけるという意味　''の中に何もないから、完全に連結する
"""
