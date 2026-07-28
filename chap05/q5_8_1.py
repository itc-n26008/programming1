country_code={
        'Iceland':{'code':'354','capital':'Reykjavik'},
        'Ireland':{'code':'353','capital':'Dublin'},
        'Azervaidjan':{'code':'984','capital':'Bakua'}
        }

def getstr_keyval(x):
    if not isinstance(x,dict):#isinstanceは型を調べる機能、dictは辞書、
        #辞書じゃなかったらそのまま外に返す
        return x

    my_str = ''
    for key, val in x.items():#セットで取り出す、items
        my_str +=(' '+ str(key) + ' ' + getstr_keyval(val))
    return my_str#作った文字列を返す

for key1, val1 in country_code.items():
    print(key1, getstr_keyval(val1))
''' 実行結果
Iceland  code 354 capital Reykjavik
Ireland  code 353 capital Dublin
Azervaidjan  code 984 capital Bakua
'''
