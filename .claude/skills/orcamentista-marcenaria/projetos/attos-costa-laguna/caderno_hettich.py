# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — O CADERNO SINTETIZADO, NA LINHA HETTICH  [06/11/2026]

⭐ [Jonathan, 06/11/2026] "preciso de uma versão mais sintetizada, sem deixar
  de informar sobre a arquiteta e os processos da empresa. O cliente optou
  pela linha hettich." · "na página que irá falar sobre as ferragens
  escolhidas acrescente essas imagens" (a gaveta Hettich, a corrediça oculta
  e a dobradiça Sensys) · "tire os valores de centavos dos itens".
⭐ Nove folhas no lugar de dezoito: capa · a casa e a empresa · as doze
  etapas · três folhas de ambiente · as ferragens · investimento ·
  condições. Some a comparação das três linhas: a escolha está feita.
⛔ Todo valor sai de `hettich.py`, que lê `linhas.monta()`.
⛔ O que NÃO atravessa esta porta: custo, MC, dúvida interna.
"""
import base64, html, re, os, sys, pathlib, subprocess, contextlib, io, importlib.util

AQUI = pathlib.Path(__file__).resolve().parent
CASA = AQUI.parent


def _mod(nome, arq):
    s = importlib.util.spec_from_file_location(nome, arq)
    m = importlib.util.module_from_spec(s); sys.modules[nome] = m
    with contextlib.redirect_stdout(io.StringIO()): s.loader.exec_module(m)
    return m


H = _mod('hettich', AQUI / 'hettich.py')
CSS = (CASA / 'css-apresentacao.css').read_text(encoding='utf-8')
src = (CASA / 'build-gustavo-caderno.py').read_text(encoding='utf-8')

PROJETO = 'Costa Laguna'
EXECUTIVO = 'ATTOS · executivo Rev. 03'
DATA = 'Novembro de 2026'
VALIDADE = '7 dias úteis'
PRAZO = '70 dias corridos'                       # [Jonathan, 04/11/2026]
ANTECIPADA = ('Escritório', '10 de dezembro de 2026')

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))


def b64(p):
    mime = 'image/png' if p.suffix == '.png' else 'image/jpeg'
    return f'data:{mime};base64,' + base64.b64encode(p.read_bytes()).decode()


IMG = {p.stem: b64(p) for p in (AQUI / 'img').glob('*.jpg') if p.stem.startswith(('c-', 'fer-'))}

S, N = [], [0]


def folha(corpo, dark=False, rodape=True):
    N[0] += 1
    f = (f'<div class="foot"><span>Valvic&nbsp;·&nbsp;{E(PROJETO)}</span>'
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
  <div class="cv-nome">O ripado<br>que atravessa<br>a casa.</div>
  <div class="cv-s">A marcenaria da casa, na linha Hettich,<br>do primeiro desenho ao dia da instalação.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">{E(PROJETO)}</div></div>
   <div><div class="k">Executivo</div><div class="v">{E(EXECUTIVO)}</div></div>
   <div><div class="k">Linha</div><div class="v">Hettich · {H.GARANTIA} anos de garantia</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['c-sala-tv-amb']}" alt="" style="object-position:30% 50%"></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''', dark=True, rodape=False)

# ── 02 · a casa, a empresa e a arquiteta ────────────────────────────────
PIL = [
 ('01', 'A casa pede mais que marcenaria.',
  'O executivo pede <b>vidro reflecta cristal</b>, <b>estofado</b> na cabeceira, perfil de '
  '<b>LED</b> embutido na peça e porta que some dentro do painel. Entra tudo no nosso escopo e '
  'sai no mesmo contrato. O que fica fora vem nomeado.'),
 ('02', 'A peça sai daqui conferida.',
  'Usinagem, montagem e conferência acontecem dentro da nossa fábrica. Cada módulo é montado '
  'aqui antes de ser embalado: porta regulada, gaveta corrida, ripa alinhada, vidro posto.'),
 ('03', 'Uma arquiteta responsável.',
  'Do orçamento aprovado à entrega, o projeto tem uma arquiteta nossa como responsável. Ela lê '
  'o executivo da ATTOS prancha por prancha, está na medição e segue as peças pela fábrica. '
  '<b>Vocês explicam o projeto uma vez, a uma pessoa</b> — e é essa pessoa que responde quando '
  'é chamada.'),
 ('04', 'O executivo de marcenaria é nosso.',
  'Antes de cortar, a Valvic desenha: onde cai a emenda do painel, por onde passa a fiação, qual '
  'a folga de instalação. É nele que a divergência aparece <em>no papel, antes de virar '
  'retrabalho</em>.'),
]
pil = ''.join(f'''<div class="c"><div class="n">{n}</div><div class="t">{E(t)}</div>
  <div class="d">{d}</div></div>''' for n, t, d in PIL)
folha(f'''<div class="ambw">
 <div class="band" style="height:94mm"><img src="{IMG['c-cozinha-corredor']}" alt="" style="object-position:50% 55%">
  <div class="tag">Cozinha · render do anteprojeto</div></div>
 <div class="low" style="display:block;padding:8mm 18mm 17mm"><div class="fitw">
  <div class="eyebrow">O projeto e a Valvic</div><div class="rule"></div>
  <h1 class="h1" style="margin:0 0 2.5mm;font-size:25pt">Uma casa de painel. Uma empresa só.</h1>
  <p class="lead" style="max-width:none">Esta não é uma casa de armário: é uma casa de painel — e
   painel é a peça que não perdoa. É grande, é contínua, fica à altura dos olhos, e qualquer
   desaprumo aparece de uma ponta à outra. Por isso tudo o que esta proposta reúne entra <b>no
   mesmo escopo, no mesmo contrato e na mesma data</b>.</p>
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

# ── 04…06 · os ambientes, SEM preço ─────────────────────────────────────
AMB = [
 (['c-cozinha-corredor', 'c-cozinha-armarios'], 'Cozinha · render do anteprojeto',
  'A cozinha.', 'Seis metros de ripado com as portas dentro, e o vidro que é nosso.',
  [('Cozinha', [
     ('Painel ripado do corredor', 'A parede inteira do corredor de serviço vira uma só peça, e '
      'as portas pivotantes do vestiário e da despensa giram dentro dela: fechadas, viram ripa.'),
     ('Cristaleira', 'Portas de vidro reflecta cristal com perfil, prateleiras e nicho inferior: '
      'a peça de vitrine do ambiente.')]),
   ('', [
     ('Armário superior com portas de vidro', 'Sobre a bancada existente, no mesmo vidro reflecta.'),
     ('Coluna de eletrodoméstico', 'De piso a teto, com o vão do forno e do micro-ondas.')])],
  'A bancada e a alvenaria da cozinha são existentes. A altura livre sob o armário superior fecha na medição.'),
 (['c-escritorio', 'c-sala-tv'], 'Escritório e sala de TV · render do anteprojeto',
  'O escritório e a sala de TV.', 'A mesa que avança sem balançar, e a parede de dois acabamentos.',
  [('Escritório', [
     ('Painel ripado de fundo', 'A mesma ripa do resto da casa, na parede inteira do fundo.'),
     ('Armário superior, bancada e armário inferior', 'A bancada corre sobre o armário e avança '
      'em mesa, com apoio metálico na ponta; armário superior de portas e armário inferior com '
      'gaveteiro.')]),
   ('Sala de TV', [
     ('Painel ripado e painel liso', 'O ripado entra pela esquerda e o liso recebe a televisão, '
      'em continuidade, sem fio aparente entre eles. No ripado, duas portas compridas, '
      'mimetizadas na ripa e abertas por toque, dão acesso ao quadro de energia e à rede '
      'hidráulica.'),
     ('Rack de TV suspenso', 'Gavetões sobre corrediça oculta Hettich, atravessando a junção dos '
      'dois painéis.')])],
  f'O {ANTECIPADA[0].lower()} sai à frente do cronograma: entregue instalado até {ANTECIPADA[1]}.'),
 (['c-suite-tv', 'c-suite01'], 'Suítes · render do anteprojeto',
  'As suítes, o hall e o jantar.', 'Painéis que escondem a porta, e uma cortesia para o quarto de hóspedes.',
  [('Suíte', [
     ('Parede painelada da TV', 'Painel de ponta a ponta com as duas portas mimetizadas e puxador '
      'em cava usinada na própria peça: nenhuma ferragem aparente na parede.'),
     ('Painel ripado da cabeceira', 'O ripado sobe atrás da cama, na mesma cadência da casa.')]),
   ('Suíte 01 · hall · jantar', [
     ('Cabeceira estofada da suíte 01', 'Base de MDF, espuma e revestimento.'),
     ('Painel do hall', 'Com a porta da lavanderia mimetizada no painel e a faixa de canto.'),
     ('Aparador suspenso do jantar', 'Portas de giro e gaveta interna, suspenso do piso.')]),
   #   ⛔ [Jonathan, 06/11/2026] "tirando o painel da rouparia"
   ('Quarto de hóspedes', [
     ('Painel liso', 'Uma <b>cortesia da Valvic</b> para a casa, no mesmo padrão dos painéis '
      'da casa.')])],
  'A cabeceira da suíte 01 e o painel do quarto de hóspedes fecham a medida na medição técnica.'),
]
AMB_I = N[0] + 1
for imgs, tag, titulo, sub, blocos, nota in AMB:
    band = ''.join(f'<img src="{IMG[i]}" alt="">' for i in imgs)
    cols = len(blocos)
    folha(f'''<div class="ambw">
     <div class="band duo" style="height:110mm">{band}<div class="tag">{E(tag)}</div></div>
     <div class="low" style="display:block;padding:7mm 18mm 17mm"><div class="fitw">
       <div class="eyebrow">Ambiente</div><div class="rule"></div>
       <div style="display:flex;align-items:baseline;gap:8mm;margin-bottom:2mm">
        <h2 class="h2" style="margin:0;white-space:nowrap">{E(titulo)}</h2>
        <p class="lead" style="margin:0;max-width:none">{E(sub)}</p></div>
       <div class="bls" style="grid-template-columns:repeat({cols},1fr)">{''.join(bloco(a, it) for a, it in blocos)}</div>
       <div class="amb-nota" style="margin-top:3mm;background:none;border-left-color:var(--line)">
         <p style="margin:0">{E(nota)}</p></div></div>
     </div></div>''')
AMB_F = N[0]

# ── 07 · as ferragens escolhidas ────────────────────────────────────────
FER = [
 ('Corrediça', 'Hettich · oculta, com amortecimento', ['fer-hettich-gaveta', 'fer-corredica-oculta'], [
   'O trilho corre <b>escondido por baixo da gaveta</b>: a lateral fica limpa, sem ferragem à vista.',
   'Extração total: a gaveta sai inteira e mostra o fundo — é o que o gavetão do rack pede.',
   'Fechamento amortecido <b>Silent System</b>: a gaveta se recolhe sozinha no fim do curso.',
   'Carga de até <b>30 kg</b> por gaveta, com regulagem fina da frente.']),
 ('Dobradiça', 'Hettich Sensys', ['fer-sensys'], [
   'Amortecimento <b>integrado à dobradiça</b>: a porta fecha suave e em silêncio, sem bater.',
   'Regulagem nos três sentidos: a porta se realinha em minutos, na obra ou anos depois.',
   'A mesma dobradiça em todas as portas de giro da casa.']),
 ('Pivô e toque', 'Sistema pivotante · Blum TIP-ON', ['c-cozinha-corredor'], [
   'As portas do corredor giram sobre <b>pivô</b>, dentro do próprio painel ripado: fechadas, viram parede.',
   'Nas portas de manutenção da sala de TV, o pulsador <b>Blum TIP-ON</b>: a porta '
   'abre com um toque e dispensa o puxador.',
   'Na suíte e no hall, a cava usinada na própria folha esconde a porta no painel.']),
]


def fcol(k, nome, imgs, pts):
    li = ''.join(f'<li>{p}</li>' for p in pts)
    return f'''<div class="fc"><div class="fk">{E(k)}</div><div class="fn">{E(nome)}</div><ul>{li}</ul></div>'''


FAIXA = [('fer-hettich-gaveta', 'Gaveta Hettich'), ('fer-corredica-oculta', 'A corrediça oculta, sob a gaveta'),
         ('fer-sensys', 'Dobradiça Hettich Sensys')]
faixa = ''.join(f'<figure><img src="{IMG[i]}" alt=""><figcaption>{E(c)}</figcaption></figure>' for i, c in FAIXA)
folha(f'''<div class="pad" style="padding-top:13mm">
 <div class="eyebrow">As ferragens escolhidas · linha Hettich</div><div class="rule"></div>
 <div style="display:flex;align-items:baseline;gap:9mm;margin-bottom:4mm">
  <h1 class="h1" style="margin:0;white-space:nowrap">O que vocês tocam todo dia.</h1>
  <p class="lead" style="margin:0;max-width:118mm">A ferragem é a única parte do móvel que
   trabalha todos os dias — e é ela que decide por quanto tempo ele continua fechando bem.</p></div>
 <div class="faixa">{faixa}</div>
 <div class="fers">{''.join(fcol(*f) for f in FER)}</div>
 <div class="garf"><div class="anos">{H.GARANTIA}</div><div><div class="k">anos de garantia Valvic</div>
  <div class="s">Na linha Hettich, sobre a marcenaria e a ferragem de movimento do projeto inteiro.
   Termo assinado no dia da entrega.</div></div><div class="leg-f">Imagens ilustrativas.</div></div>
</div>''')
N0 = N[0] + 1   # ⛔ a primeira folha com preço

# ── 08 · investimento ───────────────────────────────────────────────────
rows, amb = [], None
for it in H.ITENS:
    a = it['amb'] if it['amb'] != amb else ''
    amb = it['amb']
    v = 'Cortesia' if it['pv'] == 0 else brs(it['pv'])
    rows.append(f'<tr{" class=g" if a else ""}><td class="a">{E(a)}</td><td class="l">{E(it["nome"])}</td>'
                f'<td class="hi">{v}</td></tr>')
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · linha Hettich</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">A casa, item a item.</h1>
 <div class="invg">
  <table class="inv invh">
   <tr><th class="a">Ambiente</th><th class="l">Item</th><th class="hi">Hettich</th></tr>
   {''.join(rows)}
   <tr class="tot"><td class="a"></td><td class="l">A casa inteira</td><td class="hi">{brs(H.TOTAL)}</td></tr>
  </table>
  <div>
   <div class="gar justo" style="grid-template-columns:1fr;margin-top:0">
    <div class="c hi"><div class="unid" style="margin-top:0">A casa inteira · linha Hettich</div>
     <div class="tv">R$ {brs(H.TOTAL)}</div>
     <div class="x">Valores em reais. Cada item foi levantado peça por peça do executivo — nada
      é rateio nem estimativa por metro quadrado.</div>
     <div class="l"><div class="k">Entrada, na assinatura</div>
      <div class="v">R$ {brs(H.PARCELAS[0])}</div>
      <div class="k" style="margin-top:2.4mm">Garantia</div><div class="v">{H.GARANTIA} anos</div></div></div></div>
   <div class="box" style="margin-top:5mm"><div class="t">O que está incluso</div>
    <p>Projeto executivo de marcenaria, material, usinagem, ferragem Hettich, os pulsadores
     Blum da sala de TV, a iluminação em LED embutida, o vidro reflecta cristal e o estofado da
     cabeceira, transporte, montagem e instalação.</p></div>
  </div>
 </div>
</div>''')

# ── 09 · condições ──────────────────────────────────────────────────────
#   ⭐ [Jonathan, 06/11/2026] "vamos colocar o valor de R$ ao lado das porcentagens tbm"
pay = ''.join(f'<tr><td>{E(r)}</td><td class="d" style="width:11mm">{p*100:.0f}%</td>'
              f'<td class="d" style="width:27mm;color:var(--ink)">R$ {brs(v)}</td></tr>'
              for (r, p), v in zip(H.PAGTO, H.PARCELAS))
folha(f'''<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">Condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Prazo, pagamento e fronteiras.</h1>
 <div class="three">
  <div>
   <div class="term"><div class="k">Validade desta proposta</div><div class="v">{E(VALIDADE)}</div>
     <div class="s">A partir desta data.</div></div>
   <div class="term"><div class="k">Prazo de execução</div><div class="v">{E(PRAZO)}</div>
     <div class="s">Contados da medição técnica no local, não da assinatura.</div></div>
   <div class="term"><div class="k">Entrega antecipada</div><div class="v">{E(ANTECIPADA[0])} até {E(ANTECIPADA[1])}</div>
     <div class="s">Entregue instalado nesta data, independentemente do prazo do restante.</div></div>
   <div class="term"><div class="k">Garantia</div><div class="v">{H.GARANTIA} anos · linha Hettich</div>
     <div class="s">Marcenaria e ferragem de movimento. Instalação e regulagem, dois anos.
       Iluminação em LED segue a garantia do fabricante.</div></div>
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
    <li><div class="k">Pedra</div><div class="v">O painel de travertino do jantar e qualquer
      bancada, soleira ou peitoril: é marmoraria.</div></li>
    <li><div class="k">Eletrodomésticos, metais e obra</div><div class="v">Cooktop, forno,
      coifa, cubas e torneiras; alvenaria, elétrica, forro, piso e pintura.</div></li>
    <li><div class="k">Retirados nesta versão</div><div class="v">O armário do gourmet, o painel
      liso e a cabeceira estofada da suíte, as mesas de cabeceira e o painel da rouparia.</div></li>
    <li><div class="k">A confirmar antes da produção</div><div class="v">Os pontos de
      iluminação, a posição das portas de manutenção da sala de TV e as
      medidas que fecham na medição.</div></li>
   </ul>
  </div>
 </div>
 <div class="fecho">Um contrato. Uma data. <em>Um nome para chamar.</em></div>
 <div class="sig" style="padding-top:5mm"><div class="ln">{E(PROJETO)}</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

# ── estilo e montagem ───────────────────────────────────────────────────
EXTRA = re.search(r"EXTRA = '''(.*?)'''", src, re.S).group(1)
AJUSTE = re.search(r"AJUSTE = '''(.*?)'''", src, re.S).group(1)
EXTRA += '''
.slide{background:#FCFAF6}
.slide.dark{background:var(--deep)}
.ambw .band.duo{display:flex;gap:2mm;background:var(--deep)}
.ambw .band.duo img{flex:1;min-width:0;height:100%;object-fit:cover}
.bls{display:grid;gap:0 9mm}
.bl .eyebrow{margin-bottom:1mm;min-height:3mm}
.bl .mv .t{font-size:9pt}
.bl .mv .d{font-size:8.2pt}
.faixa{display:flex;gap:3mm;height:58mm;flex:none;margin-top:1mm}
.faixa figure{margin:0;position:relative;height:100%;background:#fff;overflow:hidden}
.faixa img{height:100%;width:auto;display:block}
.faixa figcaption{position:absolute;left:0;bottom:0;background:rgba(36,31,27,.86);color:var(--gold-lt);
  font-size:6pt;letter-spacing:.22em;text-transform:uppercase;padding:1.8mm 3.4mm;font-weight:600}
.fecho{font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt;line-height:1.2;margin-top:auto;padding-top:6mm}
.fecho em{color:var(--gold);font-style:normal}
.fr .c{padding:3.4mm 4mm}
.fr .d{font-size:7.6pt}
/* as ferragens */
.fers{display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;flex:1;min-height:0;margin-top:1mm}
.fc{display:flex;flex-direction:column;min-height:0}
.fimg{position:relative;height:66mm;flex:none;display:flex;gap:2mm;background:#fff}
.fi{flex:1;min-width:0;overflow:hidden}
.fi img,.fx img{width:100%;height:100%;object-fit:cover;display:block}
.fx{width:30mm;flex:none;overflow:hidden}
.fk{font-size:6.6pt;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-top:3.5mm}
.fn{font-family:'Cormorant Garamond',Georgia,serif;font-size:16pt;line-height:1.1;font-weight:500;margin-top:.8mm}
.fc ul{margin:2mm 0 0;padding:0;list-style:none}
.fc li{font-size:7.9pt;color:var(--soft);line-height:1.42;padding:1.3mm 0 1.3mm 3.6mm;
       border-bottom:1px solid var(--hair);position:relative}
.fc li:last-child{border-bottom:none}
.fc li::before{content:"";position:absolute;left:0;top:3mm;width:4px;height:4px;border-radius:50%;background:var(--gold-lt)}
.fc li b{color:var(--ink)}
.garf{display:flex;align-items:center;gap:5mm;border-top:1px solid var(--line);padding-top:3mm;margin-top:2mm}
.garf .anos{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;line-height:1;color:var(--gold)}
.garf .k{font-size:6.8pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:600}
.garf .s{font-size:8pt;color:var(--soft);margin-top:.6mm}
.leg-f{font-size:6.4pt;color:var(--mut);margin-left:auto;align-self:flex-end}
/* investimento de uma linha só */
.invg{display:grid;grid-template-columns:1.5fr 1fr;gap:10mm;margin-top:3mm;align-items:start}
.invh td{padding-top:1.35mm;padding-bottom:1.35mm;font-size:8.6pt}
.invh td.a,.invh th.a{text-align:left;padding-left:0;width:30mm;font-size:6.4pt;letter-spacing:.2em;
       text-transform:uppercase;color:var(--gold);font-weight:700}
.invh td.l{font-size:8.6pt;padding-left:2mm}
.invh tr.g td{border-top:1px solid var(--line)}
.invh tr.tot td{font-size:12.5pt}
.gar .tv{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;line-height:1.05;color:#F6F1E7;margin-top:3mm;white-space:nowrap}
'''
HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Proposta · {E(PROJETO)} · Hettich</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@'
        '9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
        f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S)
        + f'<script>{AJUSTE}caber();</script></body></html>')

# ── as travas ───────────────────────────────────────────────────────────
assert 'R$' not in ''.join(S[:N0 - 1]), '⛔⛔ PREÇO ANTES DA FOLHA DE VALOR'
_t = re.sub(r'<[^>]+>', ' ', re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S)))
assert not [c for c in '⭐⛔⚠' if c in ''.join(S)], '⛔ marcação interna'
for _p in ('cartão', 'desconto', 'telescópica', 'movento', 'gourmet ·', 'mesas de cabeceira,'):
    assert _p not in _t.lower(), f'⛔ a peça fala em "{_p}"'
for _c in ('Ana Carolina', 'André', 'Phillip', 'Giselle', 'Michell', 'Gustavo', 'Tereza', 'Júnia'):
    assert _c not in _t, f'⛔⛔ VESTÍGIO DE OUTRO CLIENTE: {_c}'
_amb = re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', ''.join(S[AMB_I - 1:AMB_F])))
assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _amb), '⛔ medida na descrição'
assert ',' not in ''.join(brs(it['pv']) for it in H.ITENS), '⛔ centavo num item'
assert H.TOTAL == 164000, H.TOTAL

OUT = AQUI / 'proposta-costa-laguna-hettich.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = AQUI / 'proposta-costa-laguna-hettich.pdf'
subprocess.run(['node', str(CASA / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'{PDF.name} · {len(S)} folhas · {PDF.stat().st_size // 1024} kB · primeiro preço na folha {N0}')
print(f'  Hettich {br(H.TOTAL)} · parcelas ' + ' · '.join(brs(v) for v in H.PARCELAS))
