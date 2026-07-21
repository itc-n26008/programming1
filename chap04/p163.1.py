# グローバル変数を定義します
animal = 'cat'#関数の外で作られてるからグローバル変数
# グローバル変数をプリントします
print("animal:", animal)

def my_func():#コレ関数だから、ここで作った関数↓
    animal = 'dog'#こいつは外で使えない、ローカル変数　returnしたら多分使える
    print("animal in my_func:", animal)

my_func()

print("animal global after my_func", animal)
"""実行結果
animal: cat ←　グローバル変数が使われている
animal in my_func: dog ←　実行した関数の中のローカル変数が出力
animal global after my_func cat ←　グローバル変数が使われている

"""
