alias lc='ls src/'
#テストを簡単に======ここから問題集の関数===================
#仮想環境の起動
activate() {
        cd /vagrant/prog1.py || return
        source test/bin/activate
        cd quiz/ || return

        ls
        if [ -f .lastdir ]; then
                last=$(cat .lastdir)
        else
                last=""
        fi
        echo "問題集の名前を入力 or ENTERで前回: $last"
        read dir

        if [ -z "$dir" ]; then
                dir="$last"
        fi

        cd "$dir" || return

        echo "$dir" > ../.lastdir

        ls src/

        echo ==================
        echo sv ファイル名 pt ファイル名 lc →　ls src/
        echo 今やっているところ
        cat .memo

}
pt() {
    pytest tests/test_$1
}

#svの設定
sv(){
        vi src/$@
}

