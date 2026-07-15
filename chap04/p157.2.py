def show_kwargs(**kwargs):
    '''与えられた複数のキーワード引数を辞書にまとめてうけとりその辞書を表示して返す'''
    print('Keyword arguments:', kwargs)
    return kwargs

print(show_kwargs(pasta='ペンネ', drink='赤ワイン', main_dish='肉料理', n_customers=3))
"""実行結果
Keyword arguments: {'pasta': 'ペンネ', 'drink': '赤ワイン', 'main_dish': '肉料理', 'n_customers': 3}
{'pasta': 'ペンネ', 'drink': '赤ワイン', 'main_dish': '肉料理', 'n_customers': 3}
`
"""
