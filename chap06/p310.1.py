# def reverse(data):
#     '''引数に受け取ったシーケンスを逆向きに返す'''
#     ret = []
#     for index in range(len(data)-1, -1, -1):
#         ret.append(data[index])
#     return ret

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

# リストをforループのinに添える(forループで反復子が作られる)
# ジェネレータをforループのinに添える
for char in reverse("golf"):
    print(char, end=" ")
