import pickle
with open('sample.pkl', 'rb') as f:#バイナリで読み込む
    load_num = pickle.load(f)#loadは、復元、dumpの対義語？元の形で取り出す
    print(load_num)#それを表示
"""実行結果
100
"""
