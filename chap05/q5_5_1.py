a = {x for x in 'abcabcabc' if x not in 'ab'}
print(a)
'''実行結果
{'c'}
{}だったら集合の表記らしい
aとbが入ってなかったら、aに入れるってことかな？
そのまま考えたら、ccc?になるけど、
集合は重複を自動で消すから、
答えはｃのみ
for x in 'abcabcabc'
    if x not in ab:
        ここなんだろう、ｘに入れるとか？
        a.add(x)ってなるらしい
'''
