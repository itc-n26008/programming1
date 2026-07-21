# 偶数だけ取得します。
for e in filter(lambda i: i%2 == 0, range(1, 11)):
    print(e, end=" ")
"""実行結果
2 4 6 8 10
"""
