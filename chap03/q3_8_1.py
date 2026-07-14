import pickle#pythonのデータをそのまま保存復元できる仕組み

with open('test.pkl','wb') as f:#ｆという名前をつける,書き込みｗ、バイナリ形式で保存ｂ（機械語ってことらしい）
    my_list=list(range(1,11))#1~10までのファイル作るってことみたい
    pickle.dump(my_list, f)#dumpはデータをファイルに書き込むということらしい

"""実行結果
保存されるだけ
見ると、意味不明な機械語が書いてある
"""
