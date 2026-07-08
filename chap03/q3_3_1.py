my_list=['tokyo','osaka','fukuoka','aichi','kyoto','chiba','saitama','gunma']
my_list_6 = []
for s in my_list:
    if len(s) >= 6:
        my_list_6.append(s)
print(my_list_6)
"""実行結果['fukuoka', 'saitama']
sに１つずつリストの中身を入れて、len(文字数)が６以上だったら、
my_list_6に、append追加して、表示している　"""
