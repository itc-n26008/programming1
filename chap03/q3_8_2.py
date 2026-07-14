import pickle
with open('test.pkl','rb') as f:
    result=pickle.load(f)#機械語から元の形式に戻す
    print(result)#戻した形をprint
"""実行結果
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
復元されている
xxdでみると、なんかめっちゃ複雑
7/14
"""
