# -*- coding: utf-8 -*-
"""CENTURION MOTORS — Showroom Vila da Serra · proposta em TRÊS páginas  [26/11/2026]

⭐ [Jonathan, 26/11/2026] "vamos montar com esse cenario": cinco itens com preço fechado, R$ 295.500
  (valores em `centurion-motors/valores.py`, onde também ficam custo e MC — nunca na proposta).
⚠ Condições NÃO informadas para este projeto: repetidas as últimas (40% + 20% a 30/60/90, 90 dias,
  validade 5 dias) e garantia de 5 anos (padrão comercial, Honda Minas Motos) — confirmar com o Jonathan.
⛔ Sem medida e sem contagem nas descrições · sem preço antes da folha 3 · espelho É nosso (23/11/2026),
  tinta e pedra não.
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'centurion-motors'
sys.path.insert(0, str(R))
with contextlib.redirect_stdout(io.StringIO()):
    import valores as PR
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')

CLIENTE, DESIGNER, OBRA, DATA = 'Centurion Motors', 'CLS Arquitetas Associadas', 'Showroom · Vila da Serra, Nova Lima', 'Novembro de 2026'
PRAZO, VALIDADE = '90 dias corridos', '5 dias'
PAGTO = [('Entrada, na assinatura do contrato', 0.40), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.20)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
IMG = {p.stem: 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
       for p in (P / 'img-centurion-motors').glob('*.jpg')}
TOTAL = PR.TOTAL
assert TOTAL == sum(v for _, _, v, _ in PR.VALORES) == 295500

S, N = [], [0]
def folha(corpo, dark=False, rodape=True):
    N[0] += 1
    f = (f'<div class="foot"><span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span><span>{N[0]:02d} / 03</span></div>'
         if rodape else '')
    S.append(f'<div class="slide{" dark" if dark else ""}">{corpo}{f}</div>')

# ── 01 · capa ─────────────────────────────────────────────────────────
PIL = [('Do corte à instalação', 'Fábrica e equipe próprias: uma só empresa responde pela madeira, pela laca, pela luz e pelo espelho.'),
       ('Executivo nosso', 'Cada pórtico, painel e módulo de forro é detalhado por nós e aprovado pelas arquitetas antes do corte.'),
       ('Obra comercial, prazo de loja', 'Montagem planejada para que o showroom volte a receber clientes o quanto antes.')]
folha(f"""<div class="p1">
 <div class="p1-l">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="p1-nome">Centurion<br>Motors</div>
  <div class="p1-s">A marcenaria do showroom.</div>
  <p class="p1-t">No projeto da <b>{E(DESIGNER)}</b>, a madeira envolve o salão do forro às paredes e
   emoldura os carros; na área de convivência, os pórticos em arco laqueados café abrigam nichos
   iluminados, e os espelhos ampliam o espaço e multiplicam a vitrine.</p>
  <div class="p1-pil">{''.join(f'<div><b>{E(t)}</b><span>{E(d)}</span></div>' for t, d in PIL)}</div>
  <div class="p1-meta">
   <div><div class="k">Projeto</div><div class="v">{E(DESIGNER)}</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Escopo</div><div class="v">Forro, pórticos, painéis e espelhos</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="p1-r"><img class="g1" src="{IMG['nichos']}" alt=""><img class="g2" src="{IMG['frontal']}" alt="">
  <img class="g3" src="{IMG['corredor']}" alt=""></div>
</div>""", dark=True, rodape=False)

# ── 02 · o projeto, item a item ─────────────────────────────────────────
MOV = [
 ('01', 'Forro amadeirado', 'convivencia',
  'O forro em MDF amadeirado que aquece o salão e a convivência, contínuo de ponta a ponta.'),
 ('02', 'Nichos e pórticos', 'nichos',
  'Pórticos curvos laqueados café, nichos com fundo amadeirado e prateleiras iluminadas, e os arcos de acesso aos ambientes.'),
 ('03', 'Painéis de parede', 'corredor',
  'As paredes revestidas em MDF amadeirado, no lugar do adesivo, emoldurando os quadros e a vitrine.'),
 ('04 · 05', 'Painéis e espelhos', 'destaque',
  'A base em MDF que recebe os espelhos, e o espelho prata colado sobre ela, que amplia o salão e multiplica os carros.'),
]
mov = ''.join(f"""<div class="mv2"><div class="mi"><img src="{IMG[img]}" alt=""><span>{n}</span></div>
  <div class="mt"><b>{E(t)}</b><p>{E(d)}</p></div></div>""" for n, t, img, d in MOV)
folha(f"""<div class="pad p2">
 <div class="eyebrow">O projeto</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">A madeira como moldura dos carros.</h1>
 <div class="p2g">
  <div class="movs">{mov}</div>
  <div class="het">
   <div class="hf"><img src="{IMG['lounge']}" alt=""><img src="{IMG['lateral']}" alt=""></div>
   <div class="hk">Como entregamos</div>
   <div class="ht">Fabricado aqui, instalado por nós.</div>
   <p><b>Laca café</b> sobre a curva dos pórticos, com a moldura e o intradorso acabados · <b>prateleiras com alma de aço</b>,
    que não empenam com o peso das peças expostas · <b>luz embutida</b> já instalada nos nichos ·
    <b>espelho</b> colado sobre painel, nunca direto na alvenaria.</p>
   <div class="hs"><div class="sl"><b>5</b><span>anos</span></div>
    <div><div class="hk">Garantia Valvic</div><div class="hx">Cinco anos sobre a marcenaria.
     Termo assinado na entrega.</div></div></div>
  </div>
 </div>
 <div class="acab"><b>Acabamentos:</b> MDF amadeirado e MDF branco TX · laca fosca PU café nos pórticos ·
  compensado flexível nas curvas · luz embutida nos nichos · espelho prata.</div>
</div>""")

# ── 03 · investimento e condições ───────────────────────────────────────
rows = ''.join(f'<tr><td class="l">{E(n)}<div class="sub">{E(d)}</div></td><td class="hi">{brs(v)}</td></tr>'
               for n, d, v, _ in PR.VALORES)
pay = ''.join(f'<tr><td>{E(r)}</td><td class="d">{p*100:.0f}%</td><td class="d">{br(TOTAL * p)}</td></tr>'
              for r, p in PAGTO)
folha(f"""<div class="pad p3">
 <div class="eyebrow">Investimento e condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">O showroom completo.</h1>
 <div class="p3g">
  <div>
   <table class="inv inv3"><tr><th class="l">Item</th><th class="hi">Valor</th></tr>{rows}</table>
   <div class="fora"><div class="eyebrow" style="margin-bottom:2mm">Não estão nesta proposta</div>
    Pintura e tinta indicadas no projeto · pedras e bancadas · forro de gesso e iluminação geral do salão ·
    pontos elétricos · mobiliário solto, quadros, tapetes e objetos de decoração.</div>
  </div>
  <div class="cx">
   <div class="tot"><div class="k">O projeto completo</div><div class="v">{br(TOTAL)}</div>
    <div class="sp"></div>
    <table class="pg">{pay}</table>
    <div class="ob">Todas as parcelas por transferência bancária.</div></div>
   <div class="cd">
    <div><div class="k">Prazo</div><div class="v">{E(PRAZO)}</div><div class="s">Contados a partir da medição técnica no local.</div></div>
    <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div><div class="s">A partir desta data.</div></div>
    <div><div class="k">Garantia</div><div class="v">5 anos</div><div class="s">Sobre a marcenaria.</div></div>
    <div><div class="k">Incluso</div><div class="v">Do projeto à instalação</div><div class="s">Executivo, material, laca, luz dos nichos, espelho, transporte, montagem.</div></div>
   </div>
  </div>
 </div>
 <div class="sig"><div class="ln">{E(CLIENTE)}</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>""")

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
.movs{grid-template-rows:auto auto;align-content:start}
.movs .mv2 .mi{flex:none;height:46mm}
.p3g{display:grid;grid-template-columns:1.2fr 1fr;gap:9mm;flex:1;min-height:0}
.inv3 td,.inv3 th{padding-top:2mm !important;padding-bottom:2mm !important;font-size:9.6pt}
.inv3 td .sub{font-size:7.2pt;color:var(--mut);font-weight:400;margin-top:.6mm}
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

# ── as travas ───────────────────────────────────────────────────────────
_t = re.sub(r'<[^>]+>', ' ', re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S)))
assert 'R$' not in ''.join(S[:2]), '⛔ preço antes da folha de valor'
assert not [c for c in '⭐⛔⚠' if c in _t]
for _p in ('cartão', 'desconto', 'margem', 'telescópica', 'blum', 'sensys', 'mariana', 'odiney', 'hettich', 'luiza', 'custo', 'mc ', 'nada corta'):
    assert _p not in _t.lower(), _p
assert not re.search(r'\d+\s*(cm|mm|m²)', re.sub(r'<[^>]+>', ' ', S[1])), '⛔ medida na descrição'
OUT = R / 'proposta-centurion-motors.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-centurion-motors.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
npg = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', str(PDF)], capture_output=True, text=True).stdout).group(1))
assert npg == 3, f'⛔ a proposta tem de ter 3 páginas: saiu com {npg}'
print(f'{PDF.name} · {npg} folhas · {br(TOTAL)} · entrada {br(TOTAL * PAGTO[0][1])}')
