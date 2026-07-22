str_num_list = map(lambda x: "{:34}".format(x), range(1,8))
str_num_list

print(list(str_num_list))

"""実行結果
['0001', '0002', '0003', '0004', '0005', '0006', '0007']
{:04}４桁で埋めるってことらしい
"{:x>4}".format(1)→　コレで好きな文字で埋めれるらしい　xのところを変える
"""
