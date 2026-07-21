# グローバル変数を定義します
animal = 'cat'
# グローバル変数をプリントします
print("animal:", animal)

def my_func():
    # ローカル変数を定義します
    vegetable = 'carrot'
    # 関数の中でグローバル変数の値をプリントします
    print("animal in my_func:", animal)
    # ローカル変数の値をプリントします。
    print("vegetable in_the_func:", vegetable)

my_func()

#print("vegetable:", vegetable)
"""
printするとき
animal: cat
animal in my_func: cat
vegetable in_the_func: carrot
Traceback (most recent call last):
  File "/vagrant/programming1/chap04/p162.1.py", line 16, in <module>
    print("vegetable:", vegetable)
                        ^^^^^^^^^
NameError: name 'vegetable' is not defined
　
printしないとき
animal: cat
animal in my_func: cat
vegetable in_the_func: carrot

できるだけローカル変数を使いたいそうです
"""
