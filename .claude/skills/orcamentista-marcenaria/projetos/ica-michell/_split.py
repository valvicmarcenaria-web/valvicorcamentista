import json, sys, math, pathlib
P = pathlib.Path(__file__).resolve().parent
nome, lim = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 19000
Q = json.load(open(P/f'_req-{nome}.json'))
ch, cur, n = [], [], 0
for r in Q:
    s = len(json.dumps(r, ensure_ascii=False, separators=(',', ':')))
    if n + s > lim and cur: ch.append(cur); cur, n = [], 0
    cur.append(r); n += s
if cur: ch.append(cur)
for i, c in enumerate(ch, 1):
    s = json.dumps(c, ensure_ascii=False, separators=(',', ':'))
    open(P/f'_c{i}.txt', 'w').write(s)
    print(i, len(c), len(s))
