a = {x for x in 'abcabcabc' if x not in 'ab'}
b = {y for y in 'abcabcabc' if y not in 'bc'}
print(a|b)#重複除いて全部の文字表示

'''実行結果
{'c', 'a'}
b はどっちにも入ってないことがわかるけど、aとｃは互いに片方には入ってるから表示される

コレって表示されるのはランダムなのかな？
'''
