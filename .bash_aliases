# 変更点があるとき、git statusにじどうついかされるのか検証
# Vagrantログイン時に自動実行
cd /vagrant/programming1

if [ -d .git ]; then
  git branch && git status
  
echo ========
echo "fv,fp"
fi
#仮想環境の起動
activate() {
	source test/bin/activate
	cd quiz/01.Warmup-1 || return
	ls
	ls src/
	echo ==================
	echo sv ファイル名 pt ファイル名 lc →　ls src/
}
#alias設定場所
alias fv='f vi'
alias fp='f python3'
alias py='python3'
alias lc='ls src/'
#alias sv='vi /src'
#alias activate='source test/bin/activate

#git switchの設定
git() {
    if [ "$1" = "switch" ]; then
        command git "$@" && command git branch
    else
        command git "$@"
    fi
}

#面倒だから作る
f() {
  chap=$(basename "$PWD")
  num=${chap#chap0}
  $1 q${num}_$2_$3.py
}
#テストを簡単に======ここから問題集の関数===================
pt() {
    pytest tests/test_$1
}

#svの設定
sv(){
	vi src/$@
}

#実験　コピーする
# aliases を各 Git リポジトリにコピーするコマンド
sync-aliases() {
    # ディレクトリが存在するか確認してコピー
    cp /home/vagrant/.bash_aliases /vagrant/programming1/.bash_aliases
    cp /home/vagrant/.bash_aliases /vagrant/prog1.py/.bash_aliases

    echo "✅ /home/vagrant/.bash_aliases を各 Git ディレクトリにコピーしました！"
}
