functions=[sum,min,max]#sumは足し算、minは一番小さい数字、maxは一番大きい数字を計算
number_list = range(1,11)
for func in functions:
    print("Function: {}, Result: {}".format(func.__name__, func(number_list)))
"""実行結果
Function: sum, Result: 55 1から10までの合計
Function: min, Result: 1 1から１０までで一番小さいの
Function: max, Result: 10 ↑　一番大きいの
"""
