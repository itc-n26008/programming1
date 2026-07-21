def is_even(x):
    '''偶数なら True'''
    return x % 2 == 0


# 偶数だけで取得します
for e in filter(is_even, range(1, 11)):
    print(e, end=" ")
"""実行結果
2 4 6 8 10
"""
