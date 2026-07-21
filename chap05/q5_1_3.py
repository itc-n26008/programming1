queue = []
queue.append(1)#1を追加して
print('queue:', queue)
queue.append(2)#2を追加して
print('queue:', queue)
print('pop from queue 1st value:', queue.pop(0))#取り出して消える
print('pop from queue 2nd value:', queue.pop(0))#またまた取り出して消える
print('queue:', queue)
"""実行結果
queue: [1]
queue: [1, 2]
pop from queue 1st value: 1 だからここと、
pop from queue 2nd value: 2　ここで数字が違うのよ
queue: []　ぜんぶpopされたから何もなくなっている
"""
