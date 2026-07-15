def my_func(x):
    x.append(1)#1を追加する

my_list = [1, 2, 3]
my_func(my_list)

print(my_list)
"""実行結果
[1, 2, 3, 1]
"""
