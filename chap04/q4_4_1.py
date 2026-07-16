vote_num=0#出力を見るためのグローバル変数

def vote():#表追加する関数
    print("投票します")
    global vote_num
    vote_num +=1#+1している

def reset_box():#表を空にする関数
    global vote_num
    print("箱を空にします")
    vote_num =0

def check_box():#表を発表する関数
    global vote_num
    print("表の数は{}です".format(vote_num))#変数の数を{}の中に入れている
vote()#追加
check_box()#開票
vote()
check_box()
for i in range(3):
    vote()
check_box()
reset_box()#表リセット
check_box()


