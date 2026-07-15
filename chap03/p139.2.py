with open('test.dat', 'rb') as f:
    data = f.read(6)
    print(data)
"""
bバイナリとして、r読み込むのを、fと名付ける
６バイトだけ読み込む
それを表示する"""
