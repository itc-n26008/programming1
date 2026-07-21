def func_square(*args):#*ってつけたときは自動でリストになる
    results=[]
    for n in args:
        results.append(n*n)#入れていく数字同士を掛ける
    return results#結果を外投げてる感じ

numbers = [1,2,3,4]
print(func_square(*numbers))
#many_numbers=list(range(100))
#print(many_numbers)
many_numbers=list(range(100))
print(func_square(*many_numbers))#キャッチできなかったらNoneになる
"""実行結果
[1, 4, 9, 16]
"""

"""ヒントを書いたやつ
numbers=[1,2,3,4]
def func_hint(*args):
    print("args:",args)
    print("len(args):",len(args))

func_hint(*numbers)
実行結果
args: (1, 2, 3, 4)
len(args): 4
"""
