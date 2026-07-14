with open('number.txt','r') as f:
    sum=0
    for data in f:#dataの中に一つづつ数を入れていく
        num = int(data)#numはdataをint型にしたやつ
        sum += num#取り出した整数をsumに足していく
    print(sum)
"""実行結果 55
テキストの中は、１から１０が書いてある
"""
