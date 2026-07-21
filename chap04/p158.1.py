def show_args(*args):
    '''与えられた複数の位置引数をタプルにまとめて受け取りそのタプルを表示して返す'''
    print('Positional arguments:', args)
    return args

positional_args = (4, 5, 6,  'ya')
#positional_args = [4, 5, 6,  'ya']
print(show_args(*positional_args))
"""実行結果
Positional arguments: (4, 5, 6, 'ya')
(4, 5, 6, 'ya')
"""
