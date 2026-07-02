answer = '''◯　●　●　●
●　◯　●　●
●　●　◯　●
●　●　●　◯
'''
print(answer)

w = '◯ '
b = '● '
#answer = w + b*3 = '\n'+b + w + b*2 + w+ b + '\n' + b*3 + w
#print(answer)下がもっと賢いやり方

answer = ''
for i in range(4):
    for j in range(4):
        if j == i:
            answer += w#白丸が入る
        else:
            answer += b#黒丸が入る
    answer += '\n'#多分改行 
print(answer)
"""実行結果
◯　●　●　●
●　◯　●　●
●　●　◯　●
●　●　●　◯

◯ ● ● ●
● ◯ ● ●
● ● ◯ ●
● ● ● ◯
"""
