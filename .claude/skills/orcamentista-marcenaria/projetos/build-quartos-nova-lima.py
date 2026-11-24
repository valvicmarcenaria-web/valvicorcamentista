# -*- coding: utf-8 -*-
"""QUARTOS LUCIA, MARCELA E MARCELO · NOVA LIMA — proposta em três páginas, linha Hettich  [24/11/2026]

⭐ [Jonathan, 24/11/2026] "pode montar a proposta · deixe claro as definições que foram consideradas que não
  estão expostas nos projetos". Valores de `quartos-lucia-marcela-marcelo/precos.py` (MC 32%, comissão de
  vendedor 10%, nota 9%; Marcela num item só; mesa do Marcelo fechada em 2.400).
⭐ Sem renders: a capa usa a referência que o cliente enviou. Página 2 = os móveis + as DEFINIÇÕES CONSIDERADAS
  (tudo o que não estava no desenho e foi definido pelo Jonathan) + a ferragem Hettich. Página 3 = investimento.
⚠ Nome do cliente não informado: a proposta sai pelos quartos. Validade das últimas propostas (5 dias).
⛔ Nenhum número digitado · sem metragem nas descrições dos móveis (as medidas aparecem só nas definições).
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'quartos-lucia-marcela-marcelo'
sys.path.insert(0, str(R))
with contextlib.redirect_stdout(io.StringIO()):
    import precos as PR
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')

CLIENTE, OBRA, DATA = 'Quartos Lucia, Marcela e Marcelo', 'Nova Lima', 'Novembro de 2026'
PRAZO, VALIDADE = '120 dias corridos', '5 dias'
PAGTO = [('Entrada, na assinatura do contrato', 0.40), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.20)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
IMG = {p.stem: 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
       for p in (P / 'img-quartos-nova-lima').glob('*.jpg')}

NOME = {
 'Roupeiro de correr, folha central com espelho': ('Quarto da Lucia', 'Roupeiro de correr'),
 'Roupeiro de correr com ponta curva, coluna de prateleiras e bancada suspensa': ('Quarto da Marcela', 'Roupeiro com ponta curva, coluna e bancada'),
 'Mesa de cabeceira com ponta curva, nicho e prateleira suspensa': ('Quarto do Marcelo', 'Mesa de cabeceira e prateleira'),
}
VALORES = [(NOME[m][0], NOME[m][1], round(v['pv'])) for (_a, m), v in PR.TAB['Hettich'].items()]
TOTAL = sum(v for *_, v in VALORES)
assert abs(TOTAL - PR.total('Hettich')) <= 3

S, N = [], [0]
def folha(corpo, dark=False, rodape=True):
    N[0] += 1
    f = (f'<div class="foot"><span>Valvic&nbsp;·&nbsp;{E(OBRA)}</span><span>{N[0]:02d} / 03</span></div>'
         if rodape else '')
    S.append(f'<div class="slide{" dark" if dark else ""}">{corpo}{f}</div>')

# ── 01 · capa ───────────────────────────────────────────────────────────
PIL = [('Do corte à montagem', 'Fábrica e equipe próprias: uma só empresa responde por tudo o que está nestas folhas.'),
       ('Executivo nosso', 'Cada móvel é detalhado por nós e aprovado por vocês antes do corte.'),
       ('Conferido na fábrica', 'Cada peça é montada e regulada aqui antes de ser embalada.')]
folha(f'''<div class="p1">
 <div class="p1-l">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="p1-nome">Lucia, Marcela<br>e Marcelo</div>
  <div class="p1-s">A marcenaria dos três quartos.</div>
  <p class="p1-t">Roupeiros de correr em madeirado fosco, com a ponta de prateleiras abertas arredondada que
   vocês trouxeram como referência, a bancada suspensa da Marcela e a mesa de cabeceira de ponta curva do
   Marcelo — tudo no mesmo desenho, do corte à instalação.</p>
  <div class="p1-pil">{''.join(f'<div><b>{E(t)}</b><span>{E(d)}</span></div>' for t, d in PIL)}</div>
  <div class="p1-meta">
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Ferragem</div><div class="v">Hettich</div></div>
   <div><div class="k">Acabamento</div><div class="v">Madeirado fosco</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="p1-r"><img src="{IMG['referencia']}" alt=""><div class="tag">A referência de vocês</div></div>
</div>''', dark=True, rodape=False)

# ── 02 · os móveis, as definições e a ferragem ──────────────────────────
MOV = [
 ('Quarto da Lucia', 'Roupeiro de correr',
  'Três portas de correr com puxador em perfil slim, a central em espelho com quadro de alumínio. Por dentro, '
  'maleiro, cabideiros, prateleiras, gavetas e sapateiras.'),
 ('Quarto da Marcela', 'Roupeiro com ponta curva, coluna e bancada',
  'O mesmo roupeiro de correr, com a ponta de prateleiras abertas arredondada, a coluna de prateleiras e a '
  'bancada suspensa de ponta arredondada.'),
 ('Quarto do Marcelo', 'Mesa de cabeceira e prateleira',
  'Mesa com portas de puxador cava, a ponta curva com nichos e uma prateleira suspensa.'),
]
mov = ''.join(f'<div class="mv3"><div class="k">{E(a)}</div><div class="t">{E(t)}</div><p>{E(d)}</p></div>'
              for a, t, d in MOV)
# ⭐ [Jonathan, 24/11/2026] "deixe claro as definições que foram consideradas que não estão expostas nos projetos"
DEF = [
 ('Material', 'MDF <b>madeirado fosco</b>, 18 mm, em caixas, portas e prateleiras; interior das gavetas em Branco TX. '
  'O padrão exato é escolhido com vocês antes da compra.'),
 ('Espessura', 'Prateleiras e estrutura em <b>18 mm</b> (o desenho indicava 2,5).'),
 ('Profundidade', 'Roupeiros com <b>60 cm</b> de profundidade.'),
 ('Portas de correr', 'Puxador em <b>perfil slim</b>; a folha central da Lucia em <b>espelho com quadro de alumínio</b>.'),
 ('Quarto da Lucia', 'O espaço ao lado do roupeiro <b>fica livre</b>, sem marcenaria.'),
 ('Quarto da Marcela', 'Ponta curva com <b>cinco prateleiras</b>; coluna de prateleiras do piso ao teto; '
  '<b>bancada suspensa a 80 cm</b> do piso, com ponta arredondada.'),
 ('Quarto do Marcelo', 'O hachurado do desenho é a <b>curva da peça</b>, não ripado. Portas com <b>puxador cava</b> e '
  '<b>uma prateleira suspensa</b> sobre a mesa.'),
 ('Iluminação', '<b>Sem LED</b> nos móveis.'),
]
defs = ''.join(f'<li><span>{E(k)}</span><p>{d}</p></li>' for k, d in DEF)
folha(f'''<div class="pad p2">
 <div class="eyebrow">O projeto</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">Três quartos, um só desenho.</h1>
 <div class="p2g">
  <div>
   <div class="mvs">{mov}</div>
   <div class="dfs"><div class="dk">Definições consideradas nesta proposta</div>
    <div class="ds">O projeto não traz estes pontos; eles foram definidos com vocês e estão nos valores.</div>
    <ul>{defs}</ul></div>
  </div>
  <div class="het">
   <div class="hf"><img src="{IMG['fer-sensys']}" alt=""><img src="{IMG['fer-hettich-gaveta']}" alt=""></div>
   <div class="hk">A ferragem · linha Hettich</div>
   <div class="ht">Alemã, testada para dezenas de milhares de ciclos.</div>
   <p>Corrediças ocultas com amortecimento nas gavetas e dobradiça <b>Hettich Novisys</b>: fecham suave, sem bater,
    e se regulam na obra ou anos depois.</p>
   <div class="hs"><div class="sl"><b>10</b><span>anos</span></div>
    <div><div class="hk">Garantia Valvic</div><div class="hx">Dez anos sobre a marcenaria e a ferragem.
     Instalação e regulagem, dois anos. Termo assinado na entrega.</div></div></div>
  </div>
 </div>
</div>''')

# ── 03 · investimento e condições ───────────────────────────────────────
rows = ''.join(f'<tr><td class="l">{E(a)}<div class="sub">{E(t)}</div></td><td class="hi">{brs(v)}</td></tr>'
               for a, t, v in VALORES)
pay = ''.join(f'<tr><td>{E(r)}</td><td class="d">{p*100:.0f}%</td><td class="d">{br(TOTAL * p)}</td></tr>'
              for r, p in PAGTO)
folha(f'''<div class="pad p3">
 <div class="eyebrow">Investimento e condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">O projeto completo, na linha Hettich.</h1>
 <div class="p3g">
  <div>
   <table class="inv inv3"><tr><th class="l">Quarto</th><th class="hi">Hettich</th></tr>{rows}</table>
   <div class="fora"><div class="eyebrow" style="margin-bottom:2mm">Não estão nesta proposta</div>
    Camas, colchões, iluminação, cortinas, pintura, objetos de decoração e qualquer móvel não descrito na página 2.</div>
  </div>
  <div class="cx">
   <div class="tot"><div class="k">O projeto completo</div><div class="v">{br(TOTAL)}</div>
    <div class="sp"></div><table class="pg">{pay}</table>
    <div class="ob">Todas as parcelas por transferência bancária.</div></div>
   <div class="cd">
    <div><div class="k">Prazo</div><div class="v">{E(PRAZO)}</div><div class="s">Contados a partir da medição técnica no local.</div></div>
    <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div><div class="s">A partir desta data.</div></div>
    <div><div class="k">Garantia</div><div class="v">10 anos</div><div class="s">Marcenaria e ferragem Hettich.</div></div>
    <div><div class="k">Incluso</div><div class="v">Do projeto à instalação</div><div class="s">Executivo, material, ferragem, espelho, transporte, montagem.</div></div>
   </div>
  </div>
 </div>
 <div class="sig"><div class="ln">Cliente</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

EXTRA = '''
:root{--paper:#FCFAF5}
.slide{background:var(--paper)}
.slide.dark{background:var(--deep)}
.p1{display:grid;grid-template-columns:150mm 1fr;height:100%}
.p1-l{padding:16mm 12mm 12mm 16mm;display:flex;flex-direction:column;color:#F6F1E7}
.p1-nome{font-family:'Cormorant Garamond',Georgia,serif;font-size:38pt;line-height:1;margin-top:9mm}
.p1-s{color:var(--gold-lt);font-size:9pt;letter-spacing:.06em;margin-top:3mm}
.p1-t{font-size:9pt;line-height:1.6;color:#D9D2C4;margin-top:7mm}
.p1-pil{display:grid;gap:2.6mm;margin-top:6mm}
.p1-pil div{border-left:2px solid var(--gold);padding-left:3mm}
.p1-pil b{display:block;font-size:8.2pt;color:#F6F1E7}
.p1-pil span{font-size:7.6pt;color:#BDB5A6;line-height:1.45}
.p1-meta{display:grid;grid-template-columns:1fr 1fr;gap:3mm 6mm;margin-top:auto;padding-top:4mm;border-top:1px solid rgba(255,255,255,.14)}
.p1-meta .k{font-size:6.2pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-lt)}
.p1-meta .v{font-size:8.4pt;margin-top:.6mm}
.p1-r{position:relative;overflow:hidden}
.p1-r img{width:100%;height:100%;object-fit:cover;display:block}
.p1-r .tag{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);font-size:6.4pt;
  letter-spacing:.28em;text-transform:uppercase;padding:3mm 6mm;font-weight:600}
.p2,.p3{padding-bottom:18mm}
.p2g{display:grid;grid-template-columns:1.6fr 1fr;gap:8mm;flex:1;min-height:0}
.mvs{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}
.mv3{border-top:2px solid var(--gold);padding-top:2.4mm}
.mv3 .k{font-size:6.2pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700}
.mv3 .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:13pt;line-height:1.1;margin-top:.8mm}
.mv3 p{font-size:7.5pt;color:var(--soft);line-height:1.45;margin-top:1.2mm}
.dfs{margin-top:5mm;border:1.4px solid var(--gold);border-radius:4px;background:rgba(201,169,106,.07);padding:3.6mm 4.4mm}
.dfs .dk{font-size:6.8pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700}
.dfs .ds{font-size:7.4pt;color:var(--soft);margin-top:.8mm}
.dfs ul{list-style:none;margin:2mm 0 0;padding:0}
.dfs li{display:grid;grid-template-columns:30mm 1fr;gap:3mm;padding:1.2mm 0;border-top:1px solid var(--hair)}
.dfs li span{font-size:7.4pt;font-weight:700;color:var(--ink)}
.dfs li p{font-size:7.6pt;line-height:1.4;color:var(--soft);margin:0}
.dfs li p b{color:var(--ink)}
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
.p3g{display:grid;grid-template-columns:1.2fr 1fr;gap:9mm;flex:1;min-height:0}
.inv3 td,.inv3 th{padding-top:2.6mm !important;padding-bottom:2.6mm !important;font-size:10pt}
.inv3 td .sub{font-size:7.4pt;color:var(--mut);font-weight:400;margin-top:.6mm}
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
.sig{display:grid;grid-template-columns:1fr 1fr;gap:14mm;margin-top:6mm}
.sig .ln{border-top:1px solid var(--ink);padding-top:1.6mm;font-size:7.4pt;color:var(--soft)}
'''
HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Proposta · {E(CLIENTE)}</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&'
        'family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
        f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S) + '</body></html>')

_t = re.sub(r'<[^>]+>', ' ', re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S)))
assert 'R$' not in ''.join(S[:2]), '⛔ preço antes da folha de valor'
assert not [c for c in '⭐⛔⚠' if c in _t]
for _p in ('cartão', 'desconto', 'margem', 'comissão', 'blum', 'sensys', 'nada corta', 'jessica', 'dayane', 'odiney'):
    assert _p not in _t.lower(), _p
assert 'Definições consideradas' in _t
OUT = R / 'proposta-quartos-nova-lima.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-quartos-nova-lima.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
npg = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(PDF)], capture_output=True, text=True).stdout).group(1))
assert npg == 3, f'⛔ 3 páginas: saiu com {npg}'
print(f'{PDF.name} · {npg} folhas · {br(TOTAL)} · entrada {br(TOTAL * PAGTO[0][1])}')
