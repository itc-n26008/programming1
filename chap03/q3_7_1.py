with open('sample.txt','r') as f:
    line = f.readline()
    print(line)
"""実行結果
sample.txtが１行だけ表示される
with⇒　使い終わったファイルを自動で閉じる設定
自動で閉じないと、他のファイルが開けなくなるみたい
open→　ファイルを開く関数
as→　名前をつけるらしい　
"""
