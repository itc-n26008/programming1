A = {a for a in range(21)}
B = {b for b in range(21) if b % 2 == 0}
C = A-B#偶数を引くと、奇数だけが表示されるね
print(C)
'''実行結果
{1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
'''
