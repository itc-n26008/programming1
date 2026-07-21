import os
import sys
MAX = 2
print(sys.getdefaultencoding())
print(os.path.basename(os.getcwd()))
for i in range(3):
    print(i, end=' ')
    if MAX > i:
        print(MAX)
    else:
        print('#')


"""実行結果
utf-8
chap04
0 2
1 2
2 #
"""
