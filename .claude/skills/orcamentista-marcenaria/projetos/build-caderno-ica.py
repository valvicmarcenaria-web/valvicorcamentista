# -*- coding: utf-8 -*-
"""Caderno de proposta ICA · Jéssica e Michell · Valvic Marcenaria.
   Padrão da casa: css-apresentacao.css (referência Junior Lagoa Santa).
   ⛔ REGRA DO RENDER: só os campos da BRANCA entram no HTML. alertas,
   ressalvas, mudou e pedir_ao_jonathan são meus, nunca do cliente."""
import json, pathlib, html, re

RAIZ = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/'
                    'orcamentista-marcenaria/projetos')
SCR  = pathlib.Path('/tmp/claude-0/-home-user-valvicorcamentista/'
                    '7882701a-ab48-5bc5-bc38-040da97b2b38/scratchpad')
CSS  = (RAIZ/'css-apresentacao.css').read_text()
W    = json.loads((SCR/'wf2.json').read_text())
CEN  = json.loads((SCR/'cenarios.json').read_text())

BRANCA = {'ambiente', 'itens', 'nota', 'materiais'}   # ⛔ o resto não renderiza

# ─── limpeza: tirar a frase repetida e a promessa de linha zerada ────────
TROCA = [
 ('Cozinha',
  'A Valvic articula todas as soluções do projeto: o que está nesta folha entra no nosso escopo e sai no mesmo contrato da marcenaria, com uma só data e uma só responsabilidade.',
  'Tudo o que está nesta folha sai no mesmo contrato da marcenaria, com uma só data e uma só responsabilidade.'),
 ('Lavanderia',
  'a Valvic articula todas as soluções do projeto, e o que entra no nosso escopo sai no mesmo contrato da marcenaria, na mesma medição e com um só responsável. A folha de investimento mostra item por item o que está incluído.',
  'o que entra no nosso escopo sai no mesmo contrato da marcenaria, na mesma medição e com um só responsável.'),
 ('Banho hóspedes',
  'com uma só data e um só responsável: a Valvic articula todas as soluções do projeto, e a folha de investimento mostra item por item o que está incluído.',
  'com uma só data e um só responsável.'),
 ('Sala de cinema e ateliê',
  'A luz dos nichos do ateliê já vem montada dentro do móvel, e a folha de investimento mostra item por item o que está incluído: uma só data, um só contrato, uma só responsabilidade.',
  'A luz dos nichos do ateliê já vem montada dentro do móvel: uma só data, um só contrato, uma só responsabilidade.'),
 ('Suíte master',
  'Estofamento, espelho e a estrutura metálica sob o colchão não são marcenaria, e é aí que a Valvic articula todas as soluções do projeto: o que entra no nosso escopo sai no mesmo contrato da marcenaria, numa só data e com um só responsável. A folha de investimento mostra item por item o que está incluído.',
  'Estofamento, espelho e a estrutura metálica sob o colchão não são marcenaria — e saem no mesmo contrato dela, na mesma data e com o mesmo responsável. Vocês não contratam mais ninguém.'),
 ('Banho Master',
  'na mesma data e com um só responsável: a Valvic articula todas as soluções do projeto. Os espelhos assentam entre os montantes e a medida deles sai da nossa medição técnica; a folha de investimento mostra item por item o que está incluído.',
  'na mesma data e com um só responsável. Os espelhos assentam entre os montantes, e a medida deles sai da nossa medição técnica.'),
 ('Banho Mariana',
  'junto com o móvel: a Valvic articula todas as soluções do projeto e, fechado o escopo de fornecimento desses dois itens, eles saem no mesmo contrato da marcenaria — uma só data, uma só responsabilidade.',
  'junto com o móvel, e o escopo de fornecimento dos dois fecha na medição técnica, antes do contrato.'),
 ('Suíte 03',
  'cada uma é um quadro metálico com malha de cordas náuticas tecida dentro, e a Valvic articula todas as soluções do projeto; a folha de investimento mostra item por item o que está incluído.',
  'cada uma é uma estrutura metálica com malha de cordas náuticas tecida dentro, desenhada para a medida deste quarto e instalada junto com a marcenaria.'),
 ('Closet 03',
  'em peças altas que a Valvic usina, monta e instala: aqui não entra vidro, pedra nem serralheria, e o closet sai no mesmo contrato e na mesma data do resto da casa',
  'em peças altas que a Valvic usina, monta e instala. O closet sai no mesmo contrato e na mesma data do resto da casa'),
 ('Banho 03',
  'As hastes metálicas pretas que sustentam as prateleiras são serralheria desenhada para este banho — a Valvic articula todas as soluções do projeto, e esta folha fecha o armário, as prateleiras e a luz no mesmo contrato da marcenaria: uma só data, um só responsável.',
  'As hastes metálicas pretas que sustentam as prateleiras são desenhadas por nós para a medida deste vão. O armário, as prateleiras e a luz saem no mesmo contrato da marcenaria: uma só data, um só responsável.'),
]
AMB = {a['ambiente']: a for a in W['ambientes']}
for nome, velho, novo in TROCA:
    a = AMB[nome]
    assert velho in a['nota'], f'⛔ não achei o trecho em {nome}'
    a['nota'] = a['nota'].replace(velho, novo)

# ─── a garantia é a da casa, escalonada por ferragem [garantia.md] ───────
GARANTIA = {'Blum': ('Vitalícia', 'de garantia Valvic sobre a marcenaria'),
            'Hettich': ('10 anos', 'de garantia Valvic sobre a marcenaria')}

ORDEM = ['Living', 'Cozinha', 'Lavanderia', 'Quarto', 'Área gourmet',
         'Banho gourmet', 'Home office', 'Suíte hóspedes', 'Banho hóspedes',
         'Sala de cinema e ateliê', 'Suíte master', 'Closet master',
         'Banho Master', 'Suíte Mariana', 'Closet Mariana', 'Banho Mariana',
         'Suíte 03', 'Closet 03', 'Banho 03']
IMG = {'Living':'living','Cozinha':'cozinha','Lavanderia':'lavanderia',
 'Quarto':'quarto','Área gourmet':'areagourmet','Banho gourmet':'banhogourmet',
 'Home office':'homeoffice','Suíte hóspedes':'suitehospedes',
 'Banho hóspedes':'banhohospedes','Sala de cinema e ateliê':'salacinema',
 'Suíte master':'suitemaster','Closet master':'closetmaster',
 'Banho Master':'banhomaster','Suíte Mariana':'suitemariana',
 'Closet Mariana':'closetmariana','Banho Mariana':'banhomariana',
 'Suíte 03':'suite03','Closet 03':'closet03','Banho 03':'banho03'}
# os dois que não têm perspectiva no executivo: entram pelo desenho
DESENHO = {'Cozinha', 'Closet master'}
PRECO = {a['ambiente']: a for a in CEN['ambientes']}
PRECO['Banho Master'] = PRECO['Banho master']

def br(v): return 'R$ ' + f'{v:,.2f}'.replace(',','@').replace('.',',').replace('@','.')
def E(t):  return html.escape(str(t))

S, N = [], [0]
def folha(corpo, dark=False, rodape=True, foot_r=False):
    N[0] += 1
    f = (f'<div class="foot{" r" if foot_r else ""}">'
         f'<span>Valvic&nbsp;·&nbsp;Jéssica e Michell</span>'
         f'<span>{N[0]:02d}</span></div>') if rodape else ''
    S.append(f'<div class="slide{" dark" if dark else ""}">{corpo}{f}</div>')

TOT = CEN['total']

# ── 01 · capa ───────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">Jéssica<br>e Michell</div>
  <div class="cv-s">Dezenove ambientes de uma casa inteira,<br>
      do primeiro desenho ao dia da instalação.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">Iara Cezar Arquitetura</div></div>
   <div><div class="k">Local</div><div class="v">Manhumirim · MG</div></div>
   <div><div class="k">Cenários</div><div class="v">Blum · Hettich</div></div>
   <div><div class="k">Data</div><div class="v">Outubro de 2026</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="img/capa.jpg" alt="Living"></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''',
 dark=True, rodape=False)

# ── 02 · abertura ───────────────────────────────────────────────────────
ab = W['empresa']['abertura_do_caderno']
folha(f'''<div class="ambw">
 <div class="band" style="height:104mm"><img src="img/empresa.jpg" alt="">
   <div class="tag">O que esta casa pede</div></div>
 <div class="low" style="grid-template-columns:1fr;padding:11mm 18mm 12mm">
  <div><div class="eyebrow">{E(ab['eyebrow'])}</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 5mm">{E(ab['titulo'])}</h1>
   <p class="lead" style="max-width:none;font-size:10.4pt">{E(ab['texto'])}</p></div>
 </div></div>''')

# ── 03 · a empresa ──────────────────────────────────────────────────────
em = W['empresa']
pil = '\n'.join(f'''<div class="c"><div class="n">{E(p.get('numero','')) }</div>
  <div class="t">{E(p['titulo'])}</div><div class="d">{E(p['texto'])}</div></div>'''
  for p in em['pilares'])
folha(f'''<div class="pad">
 <div class="eyebrow">{E(em['eyebrow'])}</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">{E(em['titulo'])}</h1>
 <p class="lead" style="max-width:215mm">{E(em['abertura'])}</p>
 <div class="fr" style="margin-top:6mm;flex:1;min-height:0">{pil}</div>
 <div class="box" style="margin-top:5mm"><p style="font-size:9.4pt;color:var(--ink)">
   {E(em['frase_de_fechamento'])}</p></div>
</div>''')

# ── 04 · o processo, as doze etapas ─────────────────────────────────────
pr = W['processo']
n = [0]
def etapa(e):
    n[0] += 1
    ent = (f'<div class="pe-e">{E(e["entregavel"])}</div>'
           if e.get('entregavel') else '')
    return f'''<div class="pe"><div class="pe-n">{n[0]:02d}</div>
      <div class="pe-k">{E(e['chave'])}</div>
      <div class="pe-t">{E(e['titulo'])}</div>
      <div class="pe-l">{E(e['linha'])}</div>{ent}</div>'''
cols = '\n'.join(f'''<div class="pb"><div class="pb-h">{E(b['nome'].split('—')[0].strip())}</div>
   <div class="pb-s">{E(b.get('subtitulo') or (b['nome'].split('—')[1].strip() if '—' in b['nome'] else ''))}</div>
   {''.join(etapa(e) for e in b['etapas'])}</div>''' for b in pr['blocos'])
folha(f'''<div class="pad" style="padding:13mm 15mm 11mm">
 <div class="eyebrow">{E(pr['eyebrow'])}</div><div class="rule"></div>
 <div style="display:flex;align-items:baseline;gap:9mm;margin-bottom:5mm">
  <h1 class="h1" style="margin:0">{E(pr['titulo'])}</h1>
  <p class="lead" style="margin:0;max-width:112mm">{E(pr['abertura'])}</p></div>
 <div class="rail"></div>
 <div class="proc">{cols}</div>
</div>''')

# ── 05 · a arquiteta e a fábrica ────────────────────────────────────────
arq = pr['arquiteta']
pars = ''.join(f'<p style="margin:0 0 3mm">{E(x)}</p>'
               for x in arq['texto'].split('\n') if x.strip())
folha(f'''<div class="amb">
 <div class="amb-img"><img src="img/processo.jpg" alt="">
   <div class="tag">Sala de cinema e ateliê</div></div>
 <div class="amb-txt" style="padding:15mm 15mm 12mm 12mm">
  <div class="eyebrow">Quem responde</div><div class="rule"></div>
  <h2 class="h2" style="margin:1mm 0 5mm">{E(arq['titulo'])}</h2>
  <div style="color:var(--soft);font-size:9pt">{pars}</div>
  <div class="amb-nota" style="margin-top:auto"><div class="t">A fábrica</div>
   <p>{E(pr['fechamento'])}</p></div>
 </div></div>''', foot_r=True)

# ── 06 · índice ─────────────────────────────────────────────────────────
col = lambda ls: ''.join(
  f'<div class="ix"><span class="ix-n">{i:02d}</span><span class="ix-t">{E(nm)}</span>'
  f'<span class="ix-d">{E(", ".join(AMB[nm]["materiais"][:2]))}</span></div>'
  for i, nm in ls)
meio = 10
folha(f'''<div class="pad">
 <div class="eyebrow">Os ambientes</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 2mm">Dezenove ambientes,<br>uma casa inteira.</h1>
 <p class="lead" style="margin-bottom:5mm">Uma folha para cada um, com o que a Valvic
    executa ali e o que entra no mesmo contrato.</p>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 12mm;flex:1;min-height:0">
  <div>{col(list(enumerate(ORDEM[:meio], 1)))}</div>
  <div>{col(list(enumerate(ORDEM[meio:], meio+1)))}</div>
 </div></div>''')

# ── 07–25 · as dezenove folhas de ambiente ──────────────────────────────
for i, nome in enumerate(ORDEM, 1):
    a = AMB[nome]
    mv = ''.join(f'''<div class="mv"><span class="b"></span><span>
      <span class="t">{E(it['nome'])}</span> <span class="d">{E(it['descricao'])}</span>
      </span></div>''' for it in a['itens'])
    mat = ' · '.join(E(m) for m in a['materiais'])
    cls = 'amb-img fit' if nome in DESENHO else 'amb-img'
    sel = ('<div class="selo" style="background:var(--deep);color:var(--gold-lt)">'
           'Desenho de execução</div>') if nome in DESENHO else ''
    folha(f'''<div class="amb">
 <div class="{cls}">{sel}<img src="img/{IMG[nome]}.jpg" alt="{E(nome)}">
   <div class="tag">{E(nome)}</div></div>
 <div class="amb-txt"><div class="fit">
  <div class="amb-n">{i:02d}</div>
  <div class="eyebrow">Ambiente</div><div class="rule"></div>
  <h2 class="h2" style="margin:1mm 0 4mm">{E(nome)}</h2>
  {mv}
  <div class="amb-nota" style="margin-top:6mm"><div class="t">O que este ambiente pede</div>
   <p>{E(a['nota'])}</p></div>
  <div style="margin-top:4mm;padding-top:3mm;border-top:1px solid var(--hair);
       font-size:7.4pt;letter-spacing:.08em;color:var(--mut);text-transform:uppercase">
   {mat}</div>
 </div></div></div>''', foot_r=True)

# ── 26 · abertura do tema ferragem ──────────────────────────────────────
mk = W['marcas']; at = mk['abertura_do_tema']
blocos = ''.join(f'<p style="margin:0 0 3.4mm">{E(x.strip())}</p>'
                 for x in re.split(r'\n\s*\n|  +(?=[A-ZÀ-Ú])', at['texto']) if x.strip())
folha(f'''<div class="ambw">
 <div class="band" style="height:88mm"><img src="img/ferragem.jpg" alt="">
  <div class="tag">A ferragem</div></div>
 <div class="low" style="grid-template-columns:1.15fr 1fr;padding:9mm 18mm 12mm;gap:12mm">
  <div><div class="eyebrow">{E(at['eyebrow'])}</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 4mm;font-size:25pt">{E(at['titulo'])}</h1></div>
  <div style="color:var(--soft);font-size:8.8pt">{blocos}</div>
 </div></div>''')

# ── 27 e 29 · as duas marcas ────────────────────────────────────────────
def marca(k, destaque):
    m = mk[k]
    gnum, guni = GARANTIA['Blum' if k == 'blum' else 'Hettich']
    pil = ''.join(f'''<div class="mp"><div class="mp-t">{E(p['titulo'])}</div>
       <div class="mp-d">{E(p['texto'])}</div></div>''' for p in m['pilares'])
    dk = ' realce' if destaque else ''
    return f'''<div class="pad" style="padding:13mm 16mm 11mm">
 <div class="eyebrow">{E(m['eyebrow'])}</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm;font-size:27pt">{E(m['titulo'])}</h1>
 <div class="selos{dk}">
  <div class="selo-g"><div class="sg-n">{E(gnum)}</div>
    <div class="sg-u">{E(guni)}</div></div>
  <div class="selo-e"><div class="se-n">{E(m['numero'].split(' ')[0])}</div>
    <div class="se-u">ciclos de ensaio na dobradiça</div>
    <div class="se-l">{E(m['linha_numero'])}</div></div>
  <div class="selo-a">{E(m['abertura'])}</div>
 </div>
 <div class="mps">{pil}</div>
 <div class="box" style="margin-top:auto"><p style="font-size:9pt;color:var(--ink)">
   {E(m['fechamento'])}</p></div>
</div>'''
folha(marca('blum', True))

# ── 28 · articulador e pulsador Blum nos dois cenários ──────────────────
bd = mk['blum_nos_dois']
pp = ''.join(f'<p style="margin:0 0 4mm">{E(x.strip())}</p>'
             for x in re.split(r'\n\s*\n|  +(?=[A-ZÀ-Ú])', bd['texto']) if x.strip())
folha(f'''<div class="pad" style="justify-content:center">
 <div style="max-width:200mm;margin:0 auto">
  <div class="eyebrow" style="color:var(--gold-lt)">O que não entra na escolha</div>
  <div class="rule" style="background:var(--gold-lt);width:60px"></div>
  <h1 class="h1" style="margin:0 0 7mm;font-size:29pt">{E(bd['titulo'])}</h1>
  <div style="columns:2;column-gap:14mm;color:#CFC6B4;font-size:9.6pt">{pp}</div>
  <div class="dual">
   <div class="du"><div class="du-k">Articulador</div><div class="du-v">AVENTOS · Blum</div>
     <div class="du-s">Sistema de molas. A frente sobe e para onde você soltou.</div></div>
   <div class="du"><div class="du-k">Pulsador</div><div class="du-v">TIP-ON · Blum</div>
     <div class="du-s">Abertura por toque, cem por cento mecânica. Sem motor, sem fio.</div></div>
   <div class="du"><div class="du-k">O que muda entre os cenários</div>
     <div class="du-v">Dobradiça e corrediça</div>
     <div class="du-s">Só isso. O resto da ferragem de movimento é igual nos dois.</div></div>
  </div>
 </div></div>''', dark=True)

folha(marca('hettich', False))

# ── 30 · a garantia da casa ─────────────────────────────────────────────
gv = mk['garantia_valvic']
folha(f'''<div class="pad">
 <div class="eyebrow">A garantia</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">A garantia que vale aqui é a nossa.</h1>
 <p class="lead" style="max-width:200mm">A Valvic dá garantia sobre a marcenaria, e o prazo
   acompanha a ferragem de movimento do projeto. Não é garantia de fabricante: é a da casa que
   desenhou, produziu e instalou o móvel. Vocês não falam com fabricante nenhum — abrem um
   chamado com a Valvic, e a Valvic responde.</p>
 <div class="gar" style="margin-top:7mm">
  <div class="c hi"><div class="selo">O cenário recomendado</div>
   <div class="anos" style="font-size:40pt">Vitalícia</div>
   <div class="unid">Cenário Blum</div>
   <div class="nm">Garantia Valvic sobre a marcenaria</div>
   <div class="x">Enquanto o móvel for de vocês, contra defeito de fabricação e de montagem.
     É o prazo mais alto da política da casa, e ele acompanha a ferragem Blum.</div>
   <div class="l"><div class="k">Instalação e regulagem</div><div class="v">2 anos</div>
     <div class="k">Atendimento</div><div class="v">Retorno em 24 h · visita em até 3 dias úteis</div></div></div>
  <div class="c"><div class="anos">10</div><div class="unid">anos · Cenário Hettich</div>
   <div class="nm">Garantia Valvic sobre a marcenaria</div>
   <div class="x">Dez anos contra defeito de fabricação e de montagem. A mesma fábrica, a mesma
     equipe e a mesma arquiteta — o prazo acompanha a dobradiça e a corrediça do cenário.</div>
   <div class="l"><div class="k">Instalação e regulagem</div><div class="v">2 anos</div>
     <div class="k">Atendimento</div><div class="v">Retorno em 24 h · visita em até 3 dias úteis</div></div></div>
  <div class="c"><div class="anos" style="font-size:34pt">O&nbsp;termo</div>
   <div class="unid">o que está escrito</div>
   <div class="nm">Entregue assinado na instalação</div>
   <div class="x">O termo completo vai junto com o móvel, com as condições, os prazos e o canal de
     atendimento. Nada de garantia verbal.</div>
   <div class="l"><div class="k">Fora da garantia da marcenaria</div>
     <div class="v">A iluminação em LED segue a garantia do fabricante da fita, por nota técnica.
       Dizemos isso antes de vocês assinarem, não depois.</div></div></div>
 </div></div>''')

# ── 31–32 · investimento, os dois cenários ──────────────────────────────
def tabela(campo):
    linhas = ''.join(
      f'<tr><td class="l">{E(nm)}</td><td class="hi">{br(PRECO[nm][campo])}</td></tr>'
      for nm in ORDEM)
    return linhas
def invest(cen, titulo, eyebrow, campo, total, nota, dest):
    meio = 10
    la = ''.join(f'<tr><td class="l">{E(nm)}</td><td class="hi">{br(PRECO[nm][campo])}</td></tr>'
                 for nm in ORDEM[:meio])
    lb = ''.join(f'<tr><td class="l">{E(nm)}</td><td class="hi">{br(PRECO[nm][campo])}</td></tr>'
                 for nm in ORDEM[meio:])
    sel = '<div class="selo">O cenário recomendado</div>' if dest else ''
    return f'''<div class="pad">{sel}
 <div class="eyebrow">{E(eyebrow)}</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 5mm">{E(titulo)}</h1>
 <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:9mm;flex:none;align-items:start">
  <table class="inv"><tr><th class="l">Ambiente</th><th class="hi">Investimento</th></tr>{la}</table>
  <table class="inv"><tr><th class="l">Ambiente</th><th class="hi">Investimento</th></tr>{lb}</table>
  <div style="display:flex;flex-direction:column;gap:4mm">
   <div class="box" style="margin-top:0"><div class="t">O que está incluso</div>
    <p>Projeto executivo de marcenaria, material, usinagem, ferragens, iluminação embutida,
       os demais ofícios que a folha de cada ambiente nomeia, frete, montagem e instalação —
       num só contrato, com uma só data e uma só arquiteta responsável.</p></div>
   <div class="box" style="margin-top:0"><div class="t">Garantia</div><p>{E(nota)}</p></div>
   <div style="margin-top:6mm;border-top:1.5px solid var(--ink);padding-top:3mm">
    <div style="font-size:7.4pt;letter-spacing:.2em;text-transform:uppercase;
         color:var(--mut);font-weight:600">Total · cenário {E(cen)}</div>
    <div class="serif" style="font-size:23pt;line-height:1.1;margin-top:1.5mm;
         font-variant-numeric:tabular-nums">{br(total)}</div>
    <div style="color:var(--soft);font-size:7.8pt;margin-top:1.5mm">
      Dezenove ambientes · a casa completa</div></div>
  </div></div>
 <div class="mos" style="grid-template-columns:repeat(3,1fr);height:42mm;flex:none;margin-top:4mm">
  <figure><img src="img/areagourmet.jpg" alt=""><figcaption>Área gourmet</figcaption></figure>
  <figure><img src="img/suitemariana.jpg" alt=""><figcaption>Suíte Mariana</figcaption></figure>
  <figure><img src="img/banhomaster.jpg" alt=""><figcaption>Banho master</figcaption></figure>
 </div></div>'''
folha(invest('Blum', 'O investimento, ambiente a ambiente.', 'Investimento · cenário Blum',
             'preco_blum', TOT['preco_blum'],
             'Vitalícia sobre a marcenaria, contra defeito de fabricação e de montagem. '
             'Instalação e regulagem, 2 anos.', True))
folha(invest('Hettich', 'O segundo cenário, ambiente a ambiente.', 'Investimento · cenário Hettich',
             'preco_hettich', TOT['preco_hettich'],
             'Dez anos sobre a marcenaria, contra defeito de fabricação e de montagem. '
             'Instalação e regulagem, 2 anos.', False))

# ── 33 · a decisão ──────────────────────────────────────────────────────
dif = TOT['preco_blum'] - TOT['preco_hettich']
folha(f'''<div class="pad" style="justify-content:center">
 <div style="max-width:212mm;margin:0 auto;width:100%">
  <div class="eyebrow">A decisão</div><div class="rule"></div>
  <h1 class="h1" style="margin:0 0 6mm">Os dois cenários, lado a lado.</h1>
  <table class="cmp">
   <tr><th></th><th class="hi">Cenário Blum</th><th>Cenário Hettich</th></tr>
   <tr><td class="l">Garantia Valvic sobre a marcenaria</td>
       <td class="hi b">Vitalícia</td><td class="b">10 anos</td></tr>
   <tr><td class="l">Ciclos de ensaio na dobradiça</td>
       <td class="hi">200.000</td><td>80.000</td></tr>
   <tr><td class="l">Articulador e pulsador</td>
       <td class="hi">Blum</td><td>Blum</td></tr>
   <tr><td class="l">Dobradiça e corrediça</td>
       <td class="hi">Blum</td><td>Hettich</td></tr>
   <tr><td class="l">Projeto executivo, fábrica, equipe e arquiteta</td>
       <td class="hi">As mesmas</td><td>As mesmas</td></tr>
   <tr class="tot"><td class="l">Investimento</td>
       <td class="hi">{br(TOT['preco_blum'])}</td><td>{br(TOT['preco_hettich'])}</td></tr>
  </table>
  <div class="box" style="margin-top:6mm"><div class="t">A recomendação da casa</div>
   <p style="font-size:9pt">A diferença entre os dois cenários é de {br(dif)} — e ela está inteira
    na dobradiça e na corrediça, as duas peças que vocês vão acionar dezenas de vezes por dia
    durante vinte anos e nunca vão olhar. É a parte do móvel que não aparece na foto e aparece
    no terceiro ano. A Valvic assina os dois; recomenda o primeiro.</p></div>
 </div></div>''')

# ── 34 · condições ──────────────────────────────────────────────────────
folha(f'''<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">Condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Prazo, pagamento e fronteiras.</h1>
 <div class="three">
  <div>
   <div class="term"><div class="k">Validade desta proposta</div><div class="v">30 dias</div>
     <div class="s">Preço de material e ferragem importada reajusta com câmbio.</div></div>
   <div class="term"><div class="k">Prazo de execução</div><div class="v">90 dias corridos</div>
     <div class="s">Contados da aprovação do detalhamento de execução, não da assinatura.
       A medição técnica entra antes e tem data própria no cronograma.</div></div>
   <div class="term"><div class="k">Garantia</div><div class="v">Conforme o cenário</div>
     <div class="s">Vitalícia no cenário Blum, dez anos no cenário Hettich, sobre a marcenaria.
       Instalação e regulagem, dois anos. Termo assinado na entrega.</div></div>
   <div class="term"><div class="k">Projeto executivo de marcenaria</div><div class="v">Incluso</div>
     <div class="s">Aprovado por vocês e pela Iara Cezar antes de qualquer corte.</div></div>
  </div>
  <div>
   <table class="pay" style="width:100%">
    <tr><td colspan="2" style="border:none;padding-bottom:2mm">
      <span class="eyebrow">Formas de pagamento</span></td></tr>
    <tr><td>Entrada, na assinatura</td><td class="d">a definir</td></tr>
    <tr><td>Aprovação do detalhamento</td><td class="d">a definir</td></tr>
    <tr><td>Saída da fábrica</td><td class="d">a definir</td></tr>
    <tr><td>Entrega final</td><td class="d">a definir</td></tr>
   </table>
   <div class="box" style="margin-top:5mm"><div class="t">Um interlocutor</div>
    <p>Da aprovação à entrega, vocês tratam com a arquiteta responsável pelo projeto.
       Um contrato, uma data, um nome para chamar.</p></div>
  </div>
  <div class="fora">
   <div class="eyebrow" style="margin-bottom:3mm">O que não está nesta proposta</div>
   <ul>
    <li><div class="k">Lavabo</div><div class="v">O executivo traz o ambiente; ele não entra
      nesta proposta e pode ser levantado à parte.</div></li>
    <li><div class="k">Eletrodomésticos e metais</div><div class="v">Cooktop, forno, coifa,
      geladeira, lava-louças, cubas, torneiras e metais sanitários.</div></li>
    <li><div class="k">Obra civil e instalações</div><div class="v">Alvenaria, elétrica,
      hidráulica, pintura de parede, forro e piso.</div></li>
    <li><div class="k">Decoração</div><div class="v">Mobiliário solto, cortinas, tapetes,
      objetos e quadros.</div></li>
   </ul>
  </div>
 </div>
 <div class="sig"><div class="ln">Jéssica e Michell</div>
   <div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

# ── 35 · encerramento ───────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome" style="font-size:36pt">Um contrato.<br>Uma data.<br>Um nome<br>para chamar.</div>
  <div class="cv-s">Obrigado pela confiança em pôr esta casa<br>na nossa mão.</div>
  <div class="cv-meta">
   <div><div class="k">Proposta</div><div class="v">Jéssica e Michell · ICA</div></div>
   <div><div class="k">Validade</div><div class="v">30 dias</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="img/salacinema.jpg" alt=""></div>
</div>''', dark=True, rodape=False)

EXTRA = '''
/* ── o processo: doze etapas em quatro blocos, num trilho só ─────────── */
.rail{height:1.5px;background:linear-gradient(90deg,var(--gold),var(--gold-lt) 70%,var(--hair));
      margin:0 0 0;flex:none}
.proc{display:grid;grid-template-columns:repeat(4,1fr);gap:0 7mm;flex:1;min-height:0;
      margin-top:-1px}
.pb{border-left:1px solid var(--hair);padding:5mm 5mm 0 5mm}
.pb:first-child{border-left:none;padding-left:0}
.pb-h{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);
      font-weight:700}
.pb-s{font-size:7.6pt;color:var(--mut);margin:1mm 0 4mm;min-height:8mm;line-height:1.35}
.pe{position:relative;padding:0 0 4.6mm 0}
.pe-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;color:var(--gold-lt);
      line-height:1;float:right;margin-left:3mm}
.pe-k{font-size:6pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);
      font-weight:700}
.pe-t{font-size:9.6pt;font-weight:700;margin:.6mm 0 1mm;letter-spacing:-.006em}
.pe-l{font-size:7.8pt;color:var(--soft);line-height:1.46}
.pe-e{font-size:7.1pt;color:var(--mut);margin-top:1.4mm;padding-left:3mm;
      border-left:1.5px solid var(--gold-pale);line-height:1.38}

/* ── a coluna de texto do ambiente encolhe até caber na folha ────────── */
.amb-txt{overflow:hidden;padding-bottom:16mm}
.amb-txt .fit{transform-origin:top left}
.ambw .low .fit{transform-origin:top left}

/* ── índice ───────────────────────────────────────────────────────────── */
.ix{display:grid;grid-template-columns:9mm 46mm 1fr;align-items:baseline;gap:2mm;
    padding:2.25mm 0;border-bottom:1px solid var(--hair)}
.ix-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:11pt;color:var(--gold-lt)}
.ix-t{font-size:9.4pt;font-weight:600}
.ix-d{font-size:7.4pt;color:var(--mut);text-align:right}

/* ── páginas de marca ─────────────────────────────────────────────────── */
.selos{display:grid;grid-template-columns:40mm 46mm 1fr;gap:7mm;align-items:start;
       padding:5mm 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.selos.realce{background:var(--deep);border:none;padding:6mm 6mm 6.5mm;
  box-shadow:0 2mm 7mm rgba(26,23,20,.18)}
.selos.realce .sg-n{color:var(--gold-lt)}
.selos.realce .sg-u{color:var(--gold-lt)}
.selos.realce .se-n{color:#F6F1E7}
.selos.realce .se-u{color:var(--gold-lt)}
.selos.realce .se-l{color:#BDB3A4}
.selos.realce .selo-a{color:#E6DECF}
.sg-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;line-height:.95;
      color:var(--gold);font-weight:500}
.sg-u{font-size:6.6pt;letter-spacing:.17em;text-transform:uppercase;color:var(--mut);
      font-weight:600;margin-top:2mm;line-height:1.4}
.se-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;line-height:1;
      color:var(--ink)}
.se-u{font-size:6.4pt;letter-spacing:.17em;text-transform:uppercase;color:var(--mut);
      font-weight:600;margin-top:1.2mm}
.se-l{font-size:7.2pt;color:var(--soft);margin-top:2mm;line-height:1.42}
.selo-a{font-size:8.8pt;color:var(--soft);line-height:1.56}
.mps{display:grid;grid-template-columns:1fr 1fr 1fr;gap:5mm 8mm;margin-top:5mm;
     flex:1;min-height:0;align-content:start}
.mp-t{font-size:8.6pt;font-weight:700;letter-spacing:-.004em}
.mp-d{font-size:7.7pt;color:var(--soft);margin-top:1.2mm;line-height:1.5}

/* ── bloco escuro das ferragens que não mudam ─────────────────────────── */
.dual{display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin-top:8mm;
      border-top:1px solid rgba(255,255,255,.15);padding-top:5mm}
.du-k{font-size:6.4pt;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-lt);
      font-weight:700}
.du-v{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;margin-top:1.5mm;
      color:#F6F1E7}
.du-s{font-size:7.8pt;color:#A79E8E;margin-top:1.5mm;line-height:1.45}

/* ── comparativo ──────────────────────────────────────────────────────── */
.cmp{width:100%;border-collapse:collapse}
.cmp th{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);
        font-weight:700;text-align:center;padding:0 4mm 3mm;border-bottom:1px solid var(--line)}
.cmp th.hi{background:var(--gold-pale);color:var(--gold)}
.cmp td{padding:3mm 4mm;border-bottom:1px solid var(--hair);text-align:center;font-size:9.6pt}
.cmp td.l{text-align:left;color:var(--soft);font-size:8.8pt}
.cmp td.hi{background:var(--gold-pale);font-weight:700}
.cmp td.b{font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;line-height:1}
.cmp tr.tot td{border-bottom:none;border-top:1.5px solid var(--ink);font-size:14pt;
               font-weight:700;padding-top:4mm;font-variant-numeric:tabular-nums}
.cmp tr.tot td.l{font-size:7.4pt;letter-spacing:.2em;text-transform:uppercase;
                 font-weight:600;color:var(--mut)}
'''

AJUSTE = '''
  const caber = () => document.querySelectorAll('.amb-txt').forEach(tx => {
    const f = tx.querySelector('.fit'); if (!f) return;
    f.style.zoom = 1;
    const cs = getComputedStyle(tx);
    const alt = tx.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
    const pede = f.scrollHeight;
    if (pede > alt) f.style.zoom = Math.max(.62, alt / pede);
  });
'''

PG = f'''<meta name="claude:viewport-fit-sides" content="cover">
<title>Proposta ICA · Jéssica e Michell</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&display=swap">
<style>
{CSS}
{EXTRA}
body.caderno{{background:#2A2622;margin:0;padding:22px 14px 60px}}
.wrap{{max-width:1500px;margin:0 auto}}
.cap{{color:#C6A567;font-family:'DM Sans',Arial,sans-serif;font-size:10.5px;
     letter-spacing:.26em;text-transform:uppercase;font-weight:600;margin:26px 0 8px}}
.stage{{position:relative;width:100%;aspect-ratio:297/210;overflow:hidden;
       box-shadow:0 16px 40px rgba(0,0,0,.42);background:#fff}}
.stage .slide{{position:absolute;top:0;left:0;transform-origin:top left;
              transform:scale(var(--s,1))}}
@media (max-width:620px){{.stage{{box-shadow:0 8px 20px rgba(0,0,0,.4)}}}}
</style>
<body class="caderno"><div class="wrap">
{''.join(f'<div class="cap">Folha {i:02d}</div><div class="stage">{s}</div>'
         for i, s in enumerate(S, 1))}
</div>
<script>
{AJUSTE}
  const fit = () => document.querySelectorAll('.stage').forEach(s =>
    s.style.setProperty('--s', s.clientWidth / (297 / 25.4 * 96)));
  addEventListener('resize', () => {{ caber(); fit(); }});
  addEventListener('load', () => {{ caber(); fit(); }});
  caber(); fit();
</script>
'''
out = SCR/'caderno-ica.html'
out.write_text(PG)

# ⭐ versão de impressão: as folhas no tamanho real, sem a moldura de leitura.
#    O css-apresentacao.css já traz @page A4 paisagem e page-break por folha.
PRT = SCR/'print'
PRT.mkdir(exist_ok=True)
(PRT/'caderno.html').write_text(
  '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
  '<title>Proposta ICA · Jéssica e Michell</title>'
  '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
  'family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@'
  '9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
  f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S) +
  '<script>' + AJUSTE + 'caber();</script></body></html>')
print(out, f'{len(PG):,} chars · {len(S)} folhas · Blum {br(TOT["preco_blum"])} · '
           f'Hettich {br(TOT["preco_hettich"])}')
