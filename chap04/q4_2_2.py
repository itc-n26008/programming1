def fib2(n):
    '''nより小さなフィボナッチ数列をリストで返す'''
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result
print(fib2(1000))
"""実行結果
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
[]を作っているからリストになるのかもしれぬな
"""
