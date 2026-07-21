def multi_func(number):
    if number == 0:
        print('min', end=" ")
        return min
    elif number == 1:
        print('max', end=" ")
        return max
    else:
        print('sum', end=" ")
        return sum
    
num_list = [1, 2, 3, 4]
for i in [0, 1, 2]:
    func = multi_func(i)
    print(func(num_list))
"""実行結果
min 1
max 4
sum 10
"""
