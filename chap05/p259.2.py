I = 3
J = 3
multiplicated_xy_dict = {i: {j: i * j for j in range(J)} for i in range(I)}
#↑　辞書の中に辞書がある
print('key1', 'key2', 'value', sep='\t')#タブ区切りをするらしい
for i, v1 in multiplicated_xy_dict.items():
    for j, v2 in v1.items():
        print(i, j, v2, sep='\t')
'''出力結果
key1	key2	value
0	0	0
0	1	0
0	2	0
1	0	0
1	1	1
1	2	2
2	0	0
2	1	2
2	2	4
'''
