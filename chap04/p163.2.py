# グローバル変数を定義します
animal = 'cat'
# グローバル変数をプリントします
print("animal:", animal)

def my_func_alter():
    global animal
    animal = 'dog'
    print("animal in my_func:", animal)

my_func_alter()

print("animal global after my_func", animal)
"""実行結果
animal: cat
animal in my_func: dog
animal global after my_func dog
"""
