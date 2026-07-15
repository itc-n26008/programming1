import random

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
#print(alphabet)
ch = random.choice(alphabet)#こいつが正解
print(ch)#何故か正解を表示
while True:
    val = input()#ターミナルで入れたやつと、正解があっているか？を検証する
    if ch == val:
       print('OK')
       break
    else:
         print('NG')
"""実行結果
1回目
w
w
OK
２回目
z
r
NG
z
OK
"""
