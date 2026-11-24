# -*- coding: utf-8 -*-
"""DAYANE FAUSTINO — suíte (quarto e banheiro), três cenários  [24/11/2026]

⭐ [Jonathan, 24/11/2026] "vamos fazer esse orçamento no mesmo formato do anterior": o caderno de 4 páginas da
  Jessica Fernandes (capa · os móveis e a ferragem · três cenários · condições), mesma designer (Rubia Nascimento).
⭐ Cenários de `dayane-faustino/cenarios.py`: Hettich com palha · básica com palha · básica com MDF Tela.
⚠ Condições das últimas propostas (BH, 90 dias, 40% + 20% a 30/60/90, validade 5 dias) — confirmar.
⛔ Nenhum número digitado · sem metragem e sem contagem.
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'dayane-faustino'
sys.path.insert(0, str(R))
with contextlib.redirect_stdout(io.StringIO()):
    import precos as PR
    import cenarios as CN
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')

CLIENTE, DESIGNER, OBRA, DATA = 'Dayane Faustino', 'Rubia Nascimento', 'Suíte, quarto e banheiro · Belo Horizonte', 'Novembro de 2026'
PRAZO, VALIDADE = '90 dias corridos', '5 dias'
PAGTO = [('Entrada, na assinatura do contrato', 0.40), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.20)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
IMG = {p.stem: 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
       for p in (P / 'img-dayane-faustino').glob('*.jpg')}
VALORES = []
TOTAL = sum(v for *_, v in VALORES)

S, N = [], [0]
def folha(corpo, dark=False, rodape=True):
    N[0] += 1
    f = (f'<div class="foot"><span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span><span>{N[0]:02d} / 04</span></div>'
         if rodape else '')
    S.append(f'<div class="slide{" dark" if dark else ""}">{corpo}{f}</div>')

# ── 01 · capa e o projeto ───────────────────────────────────────────────
PIL = [('Do corte à montagem', 'Fábrica e equipe próprias: uma só empresa responde por tudo o que está nestas folhas.'),
       ('Executivo nosso', 'Cada móvel é detalhado por nós e aprovado por você e pela designer antes do corte.'),
       ('Conferido na fábrica', 'Cada peça é montada e regulada aqui antes de ser embalada.')]
folha(f'''<div class="p1">
 <div class="p1-l">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="p1-nome">Dayane<br>Faustino</div>
  <div class="p1-s">A marcenaria da suíte: o quarto e o banheiro.</div>
  <p class="p1-t">No projeto da designer <b>{E(DESIGNER)}</b>, a Nogueira Âmbar aquece a suíte inteira: o
   roupeiro com palha sextavada, a cabeceira em painéis frisados com o estofado listrado, a escrivaninha e as
   mesas sobre pés dourados. No banheiro, a bancada com o quadriculado vazado em corte a laser.</p>
  <div class="p1-pil">{''.join(f'<div><b>{E(t)}</b><span>{E(d)}</span></div>' for t, d in PIL)}</div>
  <div class="p1-meta">
   <div><div class="k">Projeto</div><div class="v">{E(DESIGNER)}</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Ferragem</div><div class="v">Hettich</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="p1-r"><img class="g1" src="{IMG['quarto']}" alt=""><img class="g2" src="{IMG['quarto-b']}" alt="">
  <img class="g3" src="{IMG['banho']}" alt=""></div>
</div>''', dark=True, rodape=False)

# ── 02 · os móveis e a ferragem ─────────────────────────────────────────
MOV = [
 ('01', 'Roupeiro', 'quarto',
  'Em Nogueira Âmbar, com palha sextavada nas portas de baixo, puxador ponto dourado e interior com gavetas, '
  'cabideiros e sapateiras deslizantes.'),
 ('02', 'Cabeceira e mesas', 'quarto-b',
  'Cabeceira em painéis frisados com o estofado listrado, e as mesas laterais com palha nas gavetas e pés dourados.'),
 ('03', 'Escrivaninha e prateleira', 'quarto-b',
  'Escrivaninha suspensa com gavetas de puxador cava, e a prateleira de ponta arredondada sobre a TV.'),
 ('04', 'Banheiro', 'banho',
  'Bancada suspensa com portas e as gavetas em quadriculado vazado, cortado a laser.'),
]
POS = {'03': '85%'}
mov = ''.join(f'''<div class="mv2"><div class="mi"><img src="{IMG[img]}" alt="" style="object-position:{POS.get(n, '50%')} 50%"><span>{n}</span></div>
  <div class="mt"><b>{E(t)}</b><p>{E(d)}</p></div></div>''' for n, t, img, d in MOV)
folha(f'''<div class="pad p2">
 <div class="eyebrow">O projeto</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">Uma suíte, uma só linguagem.</h1>
 <div class="p2g">
  <div class="movs">{mov}</div>
  <div class="het">
   <div class="hf"><img src="{IMG['fer-sensys']}" alt=""><img src="{IMG['fer-hettich-gaveta']}" alt=""></div>
   <div class="hk">A ferragem · duas linhas</div>
   <div class="ht">Hettich, alemã, ou a linha básica.</div>
   <p><b>Hettich:</b> corrediça oculta e dobradiça Novisys com amortecimento integrado — a porta fecha suave,
    sem bater, e se regula nos três sentidos. <b>Básica:</b> corrediça telescópica e dobradiça nacional.
    A linha vale para o projeto inteiro.</p>
   <div class="hs"><div class="sl"><b>10</b><span>anos</span></div>
    <div><div class="hk">Garantia Valvic</div><div class="hx">Dez anos na Hettich e dois na básica, sobre a
     marcenaria e a ferragem. Termo assinado na entrega.</div></div></div>
  </div>
 </div>
 <div class="acab"><b>Acabamentos:</b> MDF Nogueira Âmbar, Guararapes · palha sextavada ou MDF Tela, conforme o
  cenário · estofado listrado · pés em perfil dourado · quadriculado em corte a laser · puxador ponto dourado.</div>
</div>''')

# ── 03 · os três cenários  [24/11/2026] ─────────────────────────────────
# ⭐ devolutiva da Rubia: ferragem básica mantendo a palha, e básica trocando a palha por MDF Tela (Guararapes)
CEN = CN.valores()
SHORT = {
 'Roupeiro com palha nas portas de baixo': 'Roupeiro',
 'Cabeceira em painéis frisados e cabeceira estofada': 'Cabeceira em painéis e cabeceira estofada',
 'Escrivaninha suspensa e prateleira': 'Escrivaninha suspensa e prateleira',
 'Mesas laterais com palha e pés dourados': 'Mesas laterais com pés dourados',
 'Bancada com portas e gavetas em quadriculado vazado': 'Bancada do banheiro, quadriculado vazado',
}
assert set(SHORT) == set(CEN[0]['itens'])
hd = ''.join(f'<th class="c{k}">Cenário {k + 1}</th>' for k in range(3))
rows = ''.join(f'<tr><td class="l">{E(SHORT[m])}</td>' + ''.join(f'<td class="c{k}">{brs(c["itens"][m])}</td>' for k, c in enumerate(CEN))
               + '</tr>' for m in SHORT)
tots = ''.join(f'<td class="c{k}">{brs(c["total"])}</td>' for k, c in enumerate(CEN))
DIZ = ['Ferragem alemã e palha natural nas portas do roupeiro e nas gavetas das mesas.',
       'Mesma palha natural, com corrediça telescópica e dobradiça nacional.',
       'Ferragem básica, e a palha trocada por MDF Tela, Guararapes.']
cards = ''.join(f'''<div class="cn c{k}"><div class="n">Cenário {k + 1}</div>
   <div class="t">{E(c["nome"])}</div><p>{E(DIZ[k])}</p>
   <div class="tg"><span>Ferragem</span><b>{E("Hettich" if k == 0 else "Básica")}</b></div>
   <div class="tg"><span>Portas e gavetas</span><b>{E(c["acab"])}</b></div>
   <div class="tg"><span>Garantia</span><b>{c["garantia"]} anos</b></div>
   <div class="v">{br(c["total"])}</div>
   <div class="e">Entrada {br(c["total"] * PAGTO[0][1])}</div>
   {"<div class=\'dif\'>" + br(CEN[0]["total"] - c["total"]) + " a menos que o cenário 1</div>" if k else "<div class=\'dif\'>Recomendado</div>"}</div>'''
                for k, c in enumerate(CEN))
folha(f'''<div class="pad p3">
 <div class="eyebrow">Investimento · três cenários</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O mesmo projeto, em três cenários.</h1>
 <div class="cns">{cards}</div>
 <table class="inv cmp3"><tr><th class="l">Móvel</th>{hd}</tr>{rows}
  <tr class="tt"><td class="l">O projeto completo</td>{tots}</tr></table>
</div>''')

# ── 04 · condições ──────────────────────────────────────────────────────
pay = ''.join(f'<tr><td>{E(r)}</td><td class="d">{p*100:.0f}%</td>' + ''.join(f'<td class="d">{br(c["total"] * p)}</td>' for c in CEN) + '</tr>'
              for r, p in PAGTO)
folha(f'''<div class="pad p3">
 <div class="eyebrow">Condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">Prazo, pagamento e garantia.</h1>
 <table class="inv pg4"><tr><th class="l">Pagamento</th><th></th>{''.join(f'<th>Cenário {k + 1}</th>' for k in range(3))}</tr>{pay}</table>
 <div class="ob" style="font-size:7.2pt;color:var(--mut);margin-top:2mm">Todas as parcelas por transferência bancária.</div>
 <div class="cd" style="grid-template-columns:repeat(4,1fr);margin-top:7mm">
  <div><div class="k">Prazo</div><div class="v">{E(PRAZO)}</div><div class="s">Contados a partir da medição técnica no local.</div></div>
  <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div><div class="s">A partir desta data.</div></div>
  <div><div class="k">Garantia</div><div class="v">10 ou 2 anos</div><div class="s">Dez na Hettich, dois na básica. Instalação e regulagem, dois anos.</div></div>
  <div><div class="k">Incluso</div><div class="v">Do projeto à instalação</div><div class="s">Executivo, material, ferragem do cenário, estofado, pés metálicos, transporte, montagem.</div></div>
 </div>
 <div class="fora" style="margin-top:7mm"><div class="eyebrow" style="margin-bottom:2mm">Não estão nesta proposta</div>
  Bancada em granito, cuba, torneira, box, espelhos, revestimentos, pintura, luminárias, cadeira, tapete,
  cabideiros e objetos de decoração.</div>
 <div class="sig" style="margin-top:auto"><div class="ln">{E(CLIENTE)} · cenário escolhido: ____</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

EXTRA = '''
:root{--paper:#FCFAF5}
.slide{background:var(--paper)}
.slide.dark{background:var(--deep)}
.p1{display:grid;grid-template-columns:118mm 1fr;height:100%}
.p1-l{padding:16mm 12mm 12mm 16mm;display:flex;flex-direction:column;color:#F6F1E7}
.p1-nome{font-family:'Cormorant Garamond',Georgia,serif;font-size:40pt;line-height:.98;margin-top:9mm}
.p1-s{color:var(--gold-lt);font-size:9pt;letter-spacing:.06em;margin-top:3mm}
.p1-t{font-size:9pt;line-height:1.6;color:#D9D2C4;margin-top:7mm}
.p1-t b{color:#F6F1E7}
.p1-pil{display:grid;gap:2.6mm;margin-top:6mm}
.p1-pil div{border-left:2px solid var(--gold);padding-left:3mm}
.p1-pil b{display:block;font-size:8.2pt;color:#F6F1E7;letter-spacing:.04em}
.p1-pil span{font-size:7.6pt;color:#BDB5A6;line-height:1.45}
.p1-meta{display:grid;grid-template-columns:1fr 1fr;gap:3mm 6mm;margin-top:auto;padding-top:4mm;border-top:1px solid rgba(255,255,255,.14)}
.p1-meta .k{font-size:6.2pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-lt)}
.p1-meta .v{font-size:8.4pt;margin-top:.6mm}
.p1-r{display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:1fr 1fr;gap:2mm;padding:2mm 2mm 2mm 0}
.p1-r img{width:100%;height:100%;object-fit:cover;display:block;min-height:0}
.p1-r .g1{grid-row:1 / span 2}
.p2g{display:grid;grid-template-columns:1.55fr 1fr;gap:8mm;flex:1;min-height:0}
.movs{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:5mm;min-height:0}
.mv2{display:flex;flex-direction:column;min-height:0}
.mv2 .mi{position:relative;flex:1;min-height:0;overflow:hidden}
.mv2 .mi img{width:100%;height:100%;object-fit:cover;display:block}
.mv2 .mi span{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);font-family:'Cormorant Garamond',Georgia,serif;
  font-size:13pt;padding:1mm 4mm}
.mv2 .mt{padding-top:2.4mm}
.mv2 .mt b{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;font-weight:600}
.mv2 .mt p{font-size:7.7pt;color:var(--soft);line-height:1.45;margin-top:.6mm}
.het{background:var(--deep);color:#F6F1E7;border-radius:4px;padding:5mm;display:flex;flex-direction:column}
.het .hf{display:grid;grid-template-columns:1fr 1fr;gap:2mm;height:44mm}
.het .hf img{width:100%;height:100%;object-fit:cover;border-radius:2px;background:#fff}
.het .hk{font-size:6.4pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-lt);font-weight:600;margin-top:4mm}
.het .ht{font-family:'Cormorant Garamond',Georgia,serif;font-size:16pt;line-height:1.15;margin-top:1mm}
.het p{font-size:8pt;line-height:1.5;color:#D9D2C4;margin-top:2mm}
.het p b{color:#F6F1E7}
.het .hs{display:flex;gap:4mm;align-items:center;margin-top:auto;padding-top:4mm;border-top:1px solid rgba(226,201,142,.3)}
.het .sl{width:22mm;height:22mm;border-radius:50%;border:1.4px solid var(--gold-lt);display:flex;flex-direction:column;
  align-items:center;justify-content:center;flex:none}
.het .sl b{font-family:'Cormorant Garamond',Georgia,serif;font-size:27pt;line-height:.9;color:var(--gold-lt);font-weight:600}
.het .sl span{font-size:5.8pt;letter-spacing:.24em;text-transform:uppercase}
.het .hs .hk{margin-top:0}
.het .hx{font-size:7.6pt;color:#D9D2C4;line-height:1.45;margin-top:.8mm}
.acab{margin-top:4mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);font-size:7.8pt;color:var(--soft)}
.acab b{color:var(--ink)}
.p2,.p3{padding-bottom:18mm}
.p3g{display:grid;grid-template-columns:1.2fr 1fr;gap:9mm;flex:1;min-height:0}
.inv3 td,.inv3 th{padding-top:1.3mm !important;padding-bottom:1.3mm !important;font-size:9pt}
.inv3 td .sub{font-size:6.8pt;color:var(--mut);font-weight:400;margin-top:.2mm}
.fora{margin-top:6mm;font-size:7.8pt;color:var(--soft);line-height:1.5}
.cx{display:flex;flex-direction:column;gap:5mm}
.tot{background:var(--deep);color:#F6F1E7;border-radius:4px;padding:5mm 6mm}
.tot .k{font-size:6.4pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-lt);font-weight:600}
.tot .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;line-height:1.05;margin-top:1mm}
.tot .sp{height:1px;background:rgba(226,201,142,.35);margin:3.6mm 0}
.tot .pg{width:100%;border-collapse:collapse;font-size:8.2pt}
.tot .pg td{padding:1.4mm 0;border-bottom:1px solid rgba(255,255,255,.1)}
.tot .pg td.d{text-align:right;color:var(--gold-lt);white-space:nowrap;padding-left:3mm}
.tot .ob{font-size:6.8pt;color:#BDB5A6;margin-top:2mm}
.cd{display:grid;grid-template-columns:1fr 1fr;gap:3.6mm 6mm}
.cd .k{font-size:6.4pt;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);font-weight:700}
.cd .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;margin-top:.6mm}
.cd .s{font-size:7.2pt;color:var(--soft);line-height:1.4;margin-top:.4mm}
.cns{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.cn{border:1.2px solid var(--line);border-radius:4px;padding:4mm 4.6mm;background:#fff;display:flex;flex-direction:column}
.cn.c0{background:var(--deep);color:#F6F1E7;border-color:var(--deep)}
.cn .n{font-size:6.4pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700}
.cn.c0 .n{color:var(--gold-lt)}
.cn .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;line-height:1.1;margin-top:1mm}
.cn p{font-size:7.4pt;line-height:1.4;color:var(--soft);margin:1.2mm 0 1.4mm;min-height:8mm}
.cn.c0 p{color:#D9D2C4}
.cn .tg{display:flex;justify-content:space-between;font-size:7.4pt;border-top:1px solid var(--hair);padding:1.1mm 0}
.cn.c0 .tg{border-top-color:rgba(255,255,255,.12)}
.cn .tg span{color:var(--mut)}.cn.c0 .tg span{color:#BDB5A6}
.cn .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:20pt;line-height:1.05;margin-top:1.6mm}
.cn .e{font-size:7.6pt;color:var(--soft)}.cn.c0 .e{color:#D9D2C4}
.cn .dif{margin-top:1.6mm;font-size:6.8pt;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);font-weight:700}
.cn.c0 .dif{color:var(--gold-lt)}
.cmp3{margin-top:4mm}
.cmp3 tr.tt td{border-top:1.5px solid var(--ink);font-weight:700;font-size:9.4pt}
.pg4 td:first-child{text-align:left}
.cmp3 td,.cmp3 th{padding-top:.75mm !important;padding-bottom:.75mm !important;font-size:8pt}
.cmp3 th.c0,.cmp3 td.c0{background:var(--gold-pale);font-weight:700;padding-left:3mm;padding-right:3mm}
.pg4 td,.pg4 th{font-size:9pt;padding-top:2mm !important;padding-bottom:2mm !important}
.pg4 td.d{text-align:right}
.sig{display:grid;grid-template-columns:1fr 1fr;gap:14mm;margin-top:6mm}
.sig .ln{border-top:1px solid var(--ink);padding-top:1.6mm;font-size:7.4pt;color:var(--soft)}
'''
HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Proposta · {E(CLIENTE)}</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&'
        'family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
        f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S) + '</body></html>')

# ── as travas ───────────────────────────────────────────────────────────
_t = re.sub(r'<[^>]+>', ' ', re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S)))
assert 'R$' not in ''.join(S[:2]), '⛔ preço antes da folha de valor'
assert not [c for c in '⭐⛔⚠' if c in _t]
for _p in ('cartão', 'desconto', 'margem', 'blum', 'sensys', 'mariana', 'odiney', 'luiza', 'cristaleira', 'jessica', 'lixeira', 'alecrim', 'nada corta'):
    assert _p not in _t.lower(), _p
assert not re.search(r'\d+\s*(cm|mm|m²)', re.sub(r'<[^>]+>', ' ', S[1])), '⛔ medida na descrição'
OUT = R / 'proposta-dayane-faustino.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-dayane-faustino.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
npg = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(PDF)], capture_output=True, text=True).stdout).group(1))
assert npg == 4, f'⛔ a proposta tem de ter 4 páginas: saiu com {npg}'
print(f'{PDF.name} · {npg} folhas · ' + ' · '.join(f"{c['nome']} {br(c['total'])}" for c in CEN))
