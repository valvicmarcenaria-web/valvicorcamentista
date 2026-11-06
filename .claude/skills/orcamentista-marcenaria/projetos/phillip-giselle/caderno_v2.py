# -*- coding: utf-8 -*-
"""PHILLIP E GISELLE — VERSÃO 2, O CADERNO SINTETIZADO  [06/11/2026]

⭐ [Jonathan, 06/11/2026] "uma segunda versão do orçamento contemplando os
  seguintes itens e mantendo o valor da proposta: Quarto de casal: cabeceira e
  portas pivotantes · Painel circulação · Quarto Ana e quarto Mateus" · "pode
  gerar uma proposta mais sintetizada · não precisa dar nome para a linha,
  apenas informe a garantia de 10 anos".
⭐ Sete folhas: capa · a casa e a empresa · as doze etapas · duas folhas de
  ambiente · investimento · condições. No molde do caderno sintetizado do Attos.
⛔ Todo valor sai de `versao2.py`, que lê o preço de cada item em `precos.py`.
   Sem linha nomeada: o custo de referência é o da ferragem da garantia de dez
   anos, e o preço é o mesmo nas duas linhas.
⛔ O que NÃO atravessa esta porta: custo, MC, nome de linha de ferragem.
"""
import base64, html, re, os, sys, pathlib, subprocess, contextlib, io

AQUI = pathlib.Path(__file__).resolve().parent
CASA = AQUI.parent
sys.path.insert(0, str(AQUI)); sys.path.insert(0, str(CASA))
with contextlib.redirect_stdout(io.StringIO()):
    import versao2 as V
    import precos as PR
CSS = (CASA / 'css-apresentacao.css').read_text(encoding='utf-8')
src = (CASA / 'build-gustavo-caderno.py').read_text(encoding='utf-8')

CLIENTE = 'Phillip e Giselle'
ARQ, ARQ_CURTO = 'Janaina Pacheco Arquitetura & Interiores', 'Janaina Pacheco'
OBRA, DATA = 'Residência unifamiliar · pavimento íntimo', 'Novembro de 2026'
PRAZO, VALIDADE = '70 dias corridos', '7 dias úteis'
GARANTIA = '10'

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
IMG = {p.stem: 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
       for p in (CASA / 'img-phillip-giselle').glob('*.jpg') if not p.stem.startswith('des-')}

# ── os valores: o preço de cada item na proposta atual ──────────────────
PV = V.T['hettich']['pv']
assert PV == V.T['blum']['pv'], '⛔ a versão 2 não pode depender da linha'
NOME = {('Quarto casal', 'Portas ripadas pivotantes (closet e banho)'): 'Portas ripadas pivotantes do closet e do banho',
        ('Quarto casal', 'Cabeceira'): 'Cabeceira com luz no topo',
        ('Suíte Ana', 'Móvel da janela (nichos, banco e gavetões)'): 'Móvel da janela: nichos, banco e gavetões',
        ('Suíte Ana', 'Painel com 3 portas mimetizadas'): 'Painel com portas mimetizadas',
        ('Quarto Mateus', 'Painel com porta oculta'): 'Painel com porta oculta',
        ('Circulação', 'Painel com 4 portas mimetizadas'): 'Painel com portas mimetizadas'}
assert set(NOME) == set(V.V2)
ITENS = [(a, NOME[(a, m)], int(PV[(a, m)])) for a, m in V.V2]
TOTAL = sum(v for *_, v in ITENS)
assert TOTAL == 73550, TOTAL
PAGTO = PR.PAGTO
PARCELAS = [int(TOTAL * p + 0.5) for _r, p in PAGTO[:-1]]
PARCELAS.append(TOTAL - sum(PARCELAS))

S, N = [], [0]


def folha(corpo, dark=False, rodape=True):
    N[0] += 1
    f = (f'<div class="foot"><span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span>'
         f'<span>{N[0]:02d}</span></div>') if rodape else ''
    S.append(f'<div class="slide{" dark" if dark else ""}">{corpo}{f}</div>')


def mv(itens):
    return ''.join(f'''<div class="mv"><span class="b"></span><span>
      <span class="t">{E(t)}</span> <span class="d">{d}</span></span></div>''' for t, d in itens)


def bloco(amb, itens):
    return f'<div class="bl"><div class="eyebrow">{E(amb)}</div>{mv(itens)}</div>'


# ── 01 · capa ───────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">Phillip<br>e Giselle</div>
  <div class="cv-s">Os painéis, a cabeceira e as portas pivotantes<br>
     do pavimento íntimo, do desenho à instalação.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">{E(ARQ_CURTO)}</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Garantia</div><div class="v">{GARANTIA} anos</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['fachada-02']}" alt=""></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''', dark=True, rodape=False)

# ── 02 · a casa, a empresa e a arquiteta ────────────────────────────────
PIL = [
 ('01', 'O projeto pede mais que marcenaria.',
  'Painel que esconde porta, porta ripada com metalon contra empeno, porta pivotante rente ao '
  'painel e luz embutida na peça. Entra tudo no nosso escopo e sai no mesmo contrato. O que '
  'fica fora vem nomeado.'),
 ('02', 'A peça sai daqui conferida.',
  'Usinagem, montagem e conferência acontecem dentro da nossa fábrica. Cada painel e cada porta '
  'são montados aqui antes de embalar: folha aprumada, pivô regulado, luz ligada para ver.'),
 ('03', 'Uma arquiteta responsável.',
  'Do orçamento aprovado à entrega, o projeto tem uma arquiteta nossa como responsável. Ela lê o '
  f'executivo da {E(ARQ_CURTO)} prancha por prancha, está na medição e segue as peças pela '
  'fábrica. <b>Vocês explicam o projeto uma vez, a uma pessoa.</b>'),
 ('04', 'O executivo de marcenaria é nosso.',
  'Antes de cortar, a Valvic desenha: onde a porta encontra o painel, por onde passa a fiação, '
  'qual a folga de instalação. É nele que a divergência aparece <em>no papel, antes de virar '
  'retrabalho</em>.'),
]
pil = ''.join(f'''<div class="c"><div class="n">{n}</div><div class="t">{E(t)}</div>
  <div class="d">{d}</div></div>''' for n, t, d in PIL)
folha(f'''<div class="ambw">
 <div class="band" style="height:94mm"><img src="{IMG['fachada']}" alt="" style="object-position:50% 40%">
  <div class="tag">A casa</div></div>
 <div class="low" style="display:block;padding:8mm 18mm 17mm"><div class="fitw">
  <div class="eyebrow">O projeto e a Valvic</div><div class="rule"></div>
  <h1 class="h1" style="margin:0 0 2.5mm;font-size:25pt">Paredes que escondem portas. Uma empresa só.</h1>
  <p class="lead" style="max-width:none">Os painéis do corredor e dos quartos, a cabeceira do casal
   e o móvel da janela da Ana, num só projeto da <b>{E(ARQ)}</b>. Painel é a peça que não
   perdoa: é grande, é contínua e esconde a porta — qualquer desaprumo aparece. Por isso tudo o
   que esta proposta reúne entra <b>no mesmo escopo, no mesmo contrato e na mesma data</b>.</p>
  <div class="fr" style="margin-top:4mm">{pil}</div></div></div>
</div>''')

# ── 03 · as doze etapas ─────────────────────────────────────────────────
BLOCOS = eval(re.search(r'^BLOCOS = (\[.*?\n\])', src, re.S | re.M).group(1))
assert sum(len(b[2]) for b in BLOCOS) == 12
_n = [0]


def etapa(k, t, l, e):
    _n[0] += 1
    return f'''<div class="pe"><div class="pe-n">{_n[0]:02d}</div><div class="pe-k">{E(k)}</div>
      <div class="pe-t">{E(t)}</div><div class="pe-l">{E(l)}</div><div class="pe-e">{E(e)}</div></div>'''


cols = '\n'.join(f'''<div class="pb"><div class="pb-h">{E(nm)}</div><div class="pb-s">{E(sub)}</div>
  {''.join(etapa(*e) for e in ets)}</div>''' for nm, sub, ets in BLOCOS)
folha(f'''<div class="pad" style="padding:13mm 15mm 20mm">
 <div class="eyebrow">O caminho do seu projeto</div><div class="rule"></div>
 <div style="display:flex;align-items:baseline;gap:9mm;margin-bottom:5mm">
  <h1 class="h1" style="margin:0">Doze etapas,<br>um só responsável</h1>
  <p class="lead" style="margin:0;max-width:112mm">Da decisão de vocês até a casa pronta são doze
    etapas — e nenhuma delas muda de dono. Cinco acontecem dentro da nossa fábrica.</p></div>
 <div class="rail"></div><div class="proc">{cols}</div>
</div>''')

# ── 04 e 05 · os ambientes, SEM preço ───────────────────────────────────
AMB = [
 (['casal-01', 'ana-janela'], 'Quarto do casal e suíte da Ana · render do projeto',
  'O quarto do casal e a suíte da Ana.', 'As portas que viram parede, e o banco sob a janela.',
  [('Quarto casal', [
     ('Portas ripadas pivotantes', 'As portas do closet e do banho, em ripado amadeirado do lado '
      'do quarto e Areia do lado de dentro, giram sobre pivô rente ao painel ripado: fechadas, '
      'viram parede.'),
     ('Cabeceira', 'Em Areia, de parede a parede, com luz quente no topo que lava a parede.')]),
   ('Suíte Ana', [
     ('Móvel da janela', 'Nichos com prateleiras dos dois lados da janela e um banco sob ela, com '
      'gavetões que guardam o que o quarto precisa esconder.'),
     ('Painel com portas mimetizadas', 'Painel de parede inteira em que as portas pivotantes '
      'desaparecem: fechadas, a parede fica lisa.')])],
  'O painel ripado do quarto do casal já existe: entram as portas, feitas para ele.'),
 (['mateus-01', 'circulacao'], 'Quarto do Mateus e circulação · render do projeto',
  'O quarto do Mateus e a circulação.', 'O corredor que vira uma parede só.',
  [('Quarto Mateus', [
     ('Painel com porta oculta', 'Painel em Grafite na parede da TV, com a porta do closet '
      'escondida no mesmo material: fechada, a parede fica inteira.')]),
   ('Circulação', [
     ('Painel da circulação', 'Em toda a extensão do corredor, em material de cor, com as portas '
      'pivotantes dos quartos mimetizadas no painel: o corredor vira uma parede só.')])],
  'Nas portas pivotantes, o fecho fica escondido na folha: nenhuma ferragem aparente no painel.'),
]
AMB_I = N[0] + 1
for imgs, tag, titulo, sub, blocos, nota in AMB:
    band = ''.join(f'<img src="{IMG[i]}" alt="">' for i in imgs)
    folha(f'''<div class="ambw">
     <div class="band duo" style="height:{110 if sum(len(it) for _a, it in blocos) > 2 else 124}mm">{band}<div class="tag">{E(tag)}</div></div>
     <div class="low" style="display:block;padding:7mm 18mm 17mm"><div class="fitw">
       <div class="eyebrow">Ambiente</div><div class="rule"></div>
       <div style="display:flex;align-items:baseline;gap:8mm;margin-bottom:2mm">
        <h2 class="h2" style="margin:0;white-space:nowrap">{E(titulo)}</h2>
        <p class="lead" style="margin:0;max-width:none">{E(sub)}</p></div>
       <div class="bls" style="grid-template-columns:repeat({len(blocos)},1fr)">{''.join(bloco(a, it) for a, it in blocos)}</div>
       <div class="amb-nota" style="margin-top:3mm;background:none;border-left-color:var(--line)">
         <p style="margin:0">{E(nota)}</p></div></div>
     </div></div>''')
AMB_F = N[0]
N0 = N[0] + 1   # ⛔ a primeira folha com preço

# ── 06 · investimento ───────────────────────────────────────────────────
rows, amb = [], None
for a, nome, v in ITENS:
    rot = a if a != amb else ''
    amb = a
    rows.append(f'<tr{" class=g" if rot else ""}><td class="a">{E(rot)}</td><td class="l">{E(nome)}</td>'
                f'<td class="hi">{brs(v)}</td></tr>')
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O projeto, item a item.</h1>
 <div class="invg">
  <table class="inv invh">
   <tr><th class="a">Ambiente</th><th class="l">Item</th><th class="hi">Valor</th></tr>
   {''.join(rows)}
   <tr class="tot"><td class="a"></td><td class="l">O projeto completo</td><td class="hi">{brs(TOTAL)}</td></tr>
  </table>
  <div>
   <div class="gar justo" style="grid-template-columns:1fr;margin-top:0">
    <div class="c hi"><div class="unid" style="margin-top:0">O projeto completo</div>
     <div class="tv">R$ {brs(TOTAL)}</div>
     <div class="x">Valores em reais. Cada item foi levantado peça por peça do executivo — nada
      é rateio nem estimativa por metro quadrado.</div>
     <div class="l"><div class="k">Entrada, na assinatura</div>
      <div class="v">R$ {brs(PARCELAS[0])}</div>
      <div class="k" style="margin-top:2.4mm">Garantia</div><div class="v">{GARANTIA} anos</div></div></div></div>
   <div class="box" style="margin-top:5mm"><div class="t">O que está incluso</div>
    <p>Projeto executivo de marcenaria, material, usinagem, ferragem com amortecimento, os
     sistemas pivotantes com fecho, a estrutura metálica das portas ripadas, a luz embutida na
     cabeceira, transporte, montagem e instalação.</p></div>
  </div>
 </div>
</div>''')

# ── 07 · condições ──────────────────────────────────────────────────────
pay = ''.join(f'<tr><td>{E(r)}</td><td class="d" style="width:11mm">{p*100:.0f}%</td>'
              f'<td class="d" style="width:27mm;color:var(--ink)">R$ {brs(v)}</td></tr>'
              for (r, p), v in zip(PAGTO, PARCELAS))
folha(f'''<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">Condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Prazo, pagamento e fronteiras.</h1>
 <div class="three">
  <div>
   <div class="term"><div class="k">Validade desta proposta</div><div class="v">{E(VALIDADE)}</div>
     <div class="s">A partir desta data.</div></div>
   <div class="term"><div class="k">Prazo de execução</div><div class="v">{E(PRAZO)}</div>
     <div class="s">Contados da medição técnica no local, não da assinatura.</div></div>
   <div class="term"><div class="k">Garantia</div><div class="v">{GARANTIA} anos</div>
     <div class="s">Marcenaria e ferragem de movimento. Instalação e regulagem, dois anos.
       Iluminação em LED segue a garantia do fabricante. Termo assinado na entrega.</div></div>
   <div class="term"><div class="k">Projeto executivo de marcenaria</div><div class="v">Incluso</div>
     <div class="s">Aprovado por vocês e pela {E(ARQ_CURTO)} antes de qualquer corte.</div></div>
  </div>
  <div>
   <table class="pay" style="width:100%">
    <tr><td colspan="3" style="border:none;padding-bottom:2mm"><span class="eyebrow">Formas de pagamento</span></td></tr>
    {pay}</table>
   <div style="font-size:7.4pt;color:var(--mut);margin-top:2.5mm;letter-spacing:.06em">
     Todas as parcelas por transferência bancária.</div>
   <div class="box" style="margin-top:5mm"><div class="t">Um interlocutor</div>
    <p>Da aprovação à entrega, vocês tratam com a arquiteta responsável pelo projeto. Um
     contrato, uma data, um nome para chamar.</p></div>
  </div>
  <div class="fora">
   <div class="eyebrow" style="margin-bottom:3mm">O que não está nesta proposta</div>
   <ul>
    <li><div class="k">Fora desta versão</div><div class="v">Os closets do casal, da Ana e do
      Mateus, a rouparia e, no quarto do casal, a mesa rack, a torre de nichos, o espelho com
      luz e as mesinhas de cabeceira.</div></li>
    <li><div class="k">Banheiros e pedra</div><div class="v">Gabinetes, armários e cristaleiras
      dos banhos; bancadas e revestimentos em mármore.</div></li>
    <li><div class="k">Obra, luminárias e eletros</div><div class="v">Alvenaria, elétrica,
      spots e perfis de forro, metais e eletrodomésticos.</div></li>
    <li><div class="k">Decoração</div><div class="v">Camas, tapetes, cadeiras, TVs e objetos.</div></li>
   </ul>
  </div>
 </div>
 <div class="fecho">Um contrato. Uma data. <em>Um nome para chamar.</em></div>
 <div class="sig" style="padding-top:5mm"><div class="ln">{E(CLIENTE)}</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

# ── estilo e montagem: o mesmo do caderno sintetizado do Attos ──────────
EXTRA = re.search(r"EXTRA = '''(.*?)'''", src, re.S).group(1)
AJUSTE = re.search(r"AJUSTE = '''(.*?)'''", src, re.S).group(1)
ATTOS = (CASA / 'attos-costa-laguna' / 'caderno_hettich.py').read_text(encoding='utf-8')
EXTRA += re.search(r"EXTRA \+= '''(.*?)'''", ATTOS, re.S).group(1)
HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Proposta · {E(CLIENTE)}</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@'
        '9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
        f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S)
        + f'<script>{AJUSTE}caber();</script></body></html>')

# ── as travas ───────────────────────────────────────────────────────────
assert 'R$' not in ''.join(S[:N0 - 1]), '⛔⛔ PREÇO ANTES DA FOLHA DE VALOR'
_t = re.sub(r'<[^>]+>', ' ', re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S)))
assert not [c for c in '⭐⛔⚠' if c in ''.join(S)], '⛔ marcação interna'
for _p in ('hettich', 'blum', 'telescóp', 'linha de ferragem', 'cartão', 'desconto'):
    assert _p not in _t.lower(), f'⛔ a peça fala em "{_p}"'
for _c in ('Michell', 'Gustavo', 'Luiza Pacheco', 'Costa Laguna', 'ATTOS', 'Haverson', 'Ana Carolina'):
    assert _c not in _t, f'⛔⛔ VESTÍGIO DE OUTRO CLIENTE: {_c}'
_amb = re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', ''.join(S[AMB_I - 1:AMB_F])))
assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _amb), '⛔ medida na descrição'
assert not re.search(r'\b(\d+|duas|dois|três|quatro|cinco|seis)\s+(portas?|gavet\w+|prateleiras?)', _t, re.I), '⛔ contagem'
assert sum(PARCELAS) == TOTAL

OUT = AQUI / 'proposta-phillip-giselle-v2.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = AQUI / 'proposta-phillip-giselle-v2.pdf'
subprocess.run(['node', str(CASA / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'{PDF.name} · {len(S)} folhas · {PDF.stat().st_size // 1024} kB · primeiro preço na folha {N0}')
print(f'  {br(TOTAL)} · parcelas ' + ' · '.join(brs(v) for v in PARCELAS))
