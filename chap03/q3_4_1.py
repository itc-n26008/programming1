for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(10):
    if i % 2 == 0:
        break
    print(i)
    
"""実行結果 
1
3
5
7
9
↑　これは、continueだけの結果、breakのやつは表示されない
continue 偶数だったらスルーして、それ以外が表示される
breakだったら　i=0ですでにif条件に当てはまってて、即break、ループ終了だから何も表示されない　"""
