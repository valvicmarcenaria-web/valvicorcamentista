set -e
gera () { # nome sid blk0_hoje fim_hoje
  python3 planilha.py $1 >/dev/null
  python3 aba.py $1 $2 $3 $4 5 | tail -3
  python3 merge.py $1 | tail -1
  python3 _txt.py $1
  python3 _slim.py $1
  python3 _split.py $1 19000
  cp _c1.txt _c1-$1.txt; cp _c2.txt _c2-$1.txt 2>/dev/null || true
  cp _blk.txt _blk-$1.txt
}
gera "$@"
