import pickle
sample_num = 100
with open('sample.pkl', 'wb') as f:
    pickle.dump(sample_num, f)
"""
変数をそのまま保存するpickle
バイナリ型を指定ファイルに書き込むのを、ｆと名付ける
ファイルにpickleしたデータを入れる、pickle.dump
"""
