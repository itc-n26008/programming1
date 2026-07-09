import random
numbers=['0','1','2','3','4','5','6','7','8','9']
num4 =''.join(random.sample(numbers, k=4))
while True:
    val= input()
    if val == num4:
        print('正解です！')
        break
    if len(val) != 4:#文字数が４じゃなかったら
        print('数字４ついれなさいね')
        continue
    answer =''
    for i in range(4):#文字一つずつ確認
        if num4[i]==val[i]:#その１文字があってたら、
            answer += num4[i]#answer二追加
        else:
            answer += 'X'#あってなかったら、Xを追加
    print('->'+ answer)
"""実行結果　    
7777 途中から
->X7XX
8888
->XXXX
9999
->XXXX
4725
"""
"""先生が書いたやつ
import random
numbers = [chr(i) for i in range(ord('0'), ord('9') + 1)]
chr→　数字から文字に変換
ord→　文字コードから数字に変換
rangeは、最後のやつを含まないから、＋１を入れている
１，２，３，４，５，６，７，８，９
#print(numbers)
sample4 = random.sample(numbers, k=4)
num4 = ''.join(sample4)
print(num4)
while True:
    val = input()
    if val == num4:
        print('OK')
        break
    if len(val) != 4:
        print('input 4 numbers.')
        continue
    answer = ''
    for i in range(4):
        if num4[i] == val[i]:
            answer += num4[i]
        else:
            answer += 'X'
    print('-> ' + answer)
