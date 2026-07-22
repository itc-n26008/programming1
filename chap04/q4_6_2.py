import random

def generate_students_data(num_students):
    '''生徒名、身長、体重からなるデータをランダムに生成する

    引数：num_students:生徒の人数を取る
    戻り：num_students個のタプル（生徒名、身長、体重）からなるリスト

    データの内容
    　生徒名　'nXX'XXは10から５０の番号
    　身長　150-190cm からランダムに選んだ値
    　体重　50-80kg からランダムに選んだ値
    '''
    students_data=[]
    for i in range(num_students):
        name='n'+ str(random.randint(10,50))
        height = random.randint(150,190)
        weight = random.randint(50,80)
        students_data.append((name,height,weight))
        if i == 0: print('i, name, height, weight')
        if i < 2 or i == num_students -1:
            print(i,name,height, weight)
        elif i == 2:
            print('...')
    return students_data

students_data = generate_students_data(10)

students_by_height=sorted(students_data, key=lambda s: s[1])
students_by_weight=sorted(students_data, key=lambda s: s[2])

print('\nSort bu height')
for student in students_by_height:
    print(student)
'''実行結果
i, name, height, weight
0 n45 156 65
1 n48 162 75
...
9 n18 174 62

Sort bu height
('n33', 150, 72)
('n14', 152, 69)
('n45', 156, 65)
('n21', 157, 62)
('n48', 162, 75)
('n28', 164, 77)
('n18', 174, 62)
('n31', 175, 50)
('n44', 184, 67)
('n48', 187, 73)

'''
