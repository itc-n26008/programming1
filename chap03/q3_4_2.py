numbers = [1,1,2,3,5,8,13,21]
x=0
for n in numbers:
    if n > 10:
        break
    x += n
print(x)
"""出力結果　20
10より小さい数の合計を求めるから。10超えるとループ破壊"""
