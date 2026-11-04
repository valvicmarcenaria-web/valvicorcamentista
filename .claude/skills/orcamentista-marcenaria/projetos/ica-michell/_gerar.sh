set -e
gera () { # nome sid blk0_hoje fim_hoje
  python3 planilha.py $1 >/dev/null
  python3 aba.py $1 $2 $3 $4 5 | tail -3
  python3 merge.py $1 | tail -1
  python3 _txt.py $1
  python3 _slim.py $1
  python3 _split.py $1 19000
  rm -f _c?-$1.txt
  for n in 1 2 3 4 5 6; do [ -f _c$n.txt ] && cp _c$n.txt _c$n-$1.txt; done
  cp _blk.txt _blk-$1.txt
}
gera "$@"
