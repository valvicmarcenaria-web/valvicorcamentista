# -*- coding: utf-8 -*-
"""ANA CAROLINA E ANDRÉ — caderno de proposta  [06/11/2026]

⭐ Layout do caderno do MICHELL na versão do GUSTAVO, como o do Phillip:
  A4 paisagem · capa · abertura · a empresa · as doze etapas · o Palha ·
  folhas de ambiente SEM preço · por que Blum · as ferragens · garantia ·
  investimento · condições · encerramento.
⭐ Pedido do Jonathan [06/11/2026]:
  · SÓ a versão Blum, com destaque especial para o benefício de trabalhar com
    ela (texto tirado do site da Blum: blum.com/br e blum.com/pt);
  · corrediça Blum TANDEM com BLUMOTION e dobradiça Blum CLIP top BLUMOTION;
  · porta de correr no SI Ocean 80, da Siforma;
  · uma folha DEDICADA às ferragens, com as imagens que ele mandou;
  · ênfase no glamour do móvel inteiro num padrão só — nada branco aparecendo.
⭐ Correções [Jonathan, 06/11/2026]: o padrão é o PALHA, DA DURATEX (não o Nude Vel);
  sai o bloco do closet aberto, porque os closets têm porta; a folha do padrão
  usa a imagem de closet que ele mandou; e o closet da suíte diz EXPLÍCITO que são
  dez gavetas (quatro gavetas e seis sapateiras) — exceção pedida à regra da contagem.
⭐⭐ REVISÃO [Jonathan, 09/11/2026], com as pranchas de 08/11: "interno agora será
  BRANCO TX, externo em PALHA, no closet teremos um PAR DE PORTAS com aplicação de
  PALHA SINTÉTICA (mencionar isso na proposta), ferragens mantém Blum"; entram o
  ROUPEIRO DA SUÍTE e o ARMÁRIO DO QUARTO ISABELLA; dois calceiros Slow Sense no
  lado André. O closet da suíte passa a VINTE gavetas (treze gavetas e sete
  sapateiras), e a exceção da contagem continua só nele.
⛔ Nenhum número digitado: tudo sai de `ana-carolina-andre/precos.py`.
⛔ Sem metragem e sem contagem nas descrições dos ambientes.
⛔ O projeto não tem render: as folhas de ambiente usam as ELEVAÇÕES do
   executivo, recortadas sem cota, multiplicadas sobre o campo Palha.
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'ana-carolina-andre'
sys.path.insert(0, str(R)); sys.path.insert(0, str(P))
with contextlib.redirect_stdout(io.StringIO()):
    import precos as PR
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')

CLIENTE = 'Ana Carolina e André'
ARQ = 'Ana Maria'
OBRA = 'Ed. La Concordia · Funcionários'
DATA = 'Novembro de 2026'
PRAZO, VALIDADE = '60 dias corridos', '3 dias corridos'   # [Jonathan, 09/11/2026]
GAR = '30'

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
def b64(p):
    mime = 'image/png' if p.suffix == '.png' else 'image/jpeg'
    return f'data:{mime};base64,' + base64.b64encode(p.read_bytes()).decode()
IMG = {p.stem: b64(p) for p in (P / 'img-ana-carolina-andre').glob('*.jpg')}

S, N = [], [0]
def folha(corpo, dark=False, rodape=True, foot_r=False, cls=''):
    N[0] += 1
    f = (f'<div class="foot{" r" if foot_r else ""}"><span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span>'
         f'<span>{N[0]:02d}</span></div>') if rodape else ''
    S.append(f'<div class="slide{" dark" if dark else ""}{" " + cls if cls else ""}">{corpo}{f}</div>')

def mv(itens):
    return ''.join(f'''<div class="mv"><span class="b"></span><span>
      <span class="t">{E(t)}</span> <span class="d">{d}</span></span></div>''' for t, d in itens)

def campo(*imgs, op=.9, tag=None, legenda=None, row=False):
    """O campo Palha com o desenho do executivo multiplicado por cima: o branco
    do papel some e fica só o traço — nada branco aparece."""
    figs = ''.join(f'<img src="{IMG[i]}" alt="">' for i in imgs)
    t = f'<div class="tag">{E(tag)}</div>' if tag else ''
    lg = f'<div class="leg">{E(legenda)}</div>' if legenda else ''
    return f'<div class="campo n{len(imgs)}{" row" if row else ""}" style="--op:{op}">{figs}{lg}{t}</div>'

# ── 01 · capa ───────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">Ana Carolina<br>e André</div>
  <div class="cv-s">Os closets e os roupeiros do apartamento,<br>
     em Palha da Duratex por fora e Branco TX por dentro,<br>com ferragem Blum.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">Arquiteta {E(ARQ)}</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Linha</div><div class="v">Blum</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r">{campo('des-closet-suite-e1', op=.55)}
  <div class="cv-selo"><div class="k">Padrão</div><div class="v">Palha</div>
   <div class="s">Duratex por fora · Branco TX por dentro</div></div></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''', dark=True, rodape=False)

# ── 02 · abertura ───────────────────────────────────────────────────────
folha(f'''<div class="ambw">
 <div class="band" style="height:96mm">{campo('des-suite-e1', 'des-closet-suite-e1', 'des-quarto-isabella', op=.6, row=True)}
   <div class="tag">O apartamento</div></div>
 <div class="low" style="grid-template-columns:1fr;padding:11mm 18mm 12mm">
  <div><div class="eyebrow">O que este apartamento pede</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 5mm">Cinco armários. Palha por fora, claro por dentro.</h1>
   <p class="lead" style="max-width:none;font-size:10.4pt">O roupeiro e o closet da suíte, o
    roupeiro do Gabriel, o closet e o armário da Isabella — um só projeto da arquiteta
    <b>{E(ARQ)}</b>, com portas de giro de cava usinada, portas de correr com espelho, um par
    de portas em palha sintética e gavetas que fecham sozinhas. <b>Por fora, o MDF Palha, da
    Duratex; por dentro, o Branco TX</b>, sobre ferragem Blum. <b>Uma só empresa responde por
    tudo o que está nestas folhas</b>, da medição à instalação. <em>Um contrato, uma data, um
    nome para chamar.</em></p></div>
 </div></div>''')

# ── 03 · a empresa e a infraestrutura ───────────────────────────────────
PIL = [
 ('01', 'O projeto pede mais que marcenaria.',
  'Porta de giro com cava usinada, sistema de correr com amortecimento, folha de espelho em '
  'alumínio, gaveta com corrediça Blum. Tudo isso entra no nosso escopo, no mesmo contrato e '
  'na mesma data. <b>Vocês não contratam mais ninguém</b> para a marcenaria e para o que faz '
  'parte dela. O que fica fora vem nomeado.'),
 ('02', 'A peça sai daqui conferida.',
  'Detalhamento, programação, usinagem, montagem e conferência acontecem dentro da nossa '
  'fábrica. Cada módulo é montado aqui antes de ser embalado: porta regulada, gaveta corrida, '
  'folha de correr alinhada. A conferência é <b>etapa do processo</b>, não boa vontade no fim.'),
 ('03', 'Uma arquiteta responsável pelo projeto.',
  'Do orçamento aprovado à entrega, o projeto tem uma arquiteta nossa como responsável. É ela '
  'quem lê o executivo prancha por prancha, está na medição e segue as peças pela fábrica. Ela '
  f'conversa com a arquiteta {E(ARQ)} na mesma linguagem técnica. <b>Vocês explicam o projeto '
  'uma vez, a uma pessoa.</b>'),
 ('04', 'O executivo de marcenaria é nosso.',
  'Antes de cortar, a Valvic desenha. O projeto de interiores diz o que o ambiente precisa ser; '
  'o nosso executivo diz como cada móvel se constrói — estrutura, ferragem, sentido de abertura, '
  'folga das portas. É nele que a divergência aparece <em>no papel, antes de virar '
  'retrabalho</em>.'),
]
pil = '\n'.join(f'''<div class="c"><div class="n">{n}</div><div class="t">{E(t)}</div>
  <div class="d">{d}</div></div>''' for n, t, d in PIL)
folha(f'''<div class="pad">
 <div class="eyebrow">A empresa e a infraestrutura</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">A Valvic articula todas as soluções do projeto.</h1>
 <p class="lead" style="max-width:215mm">Um projeto raramente se perde na marcenaria. Ele se
  perde na costura entre os ofícios, quando cada um chega com contrato, prazo e medida
  próprios. Aqui não há essa costura para fazer: tudo o que esta proposta reúne entra no mesmo
  escopo, no mesmo contrato e na mesma data.</p>
 <div class="fr" style="margin-top:6mm;flex:1;min-height:0">{pil}</div>
 <div class="box" style="margin-top:5mm"><p style="font-size:9.4pt;color:var(--ink)">
   Na próxima folha, o caminho que o projeto percorre — etapa por etapa, até o dia em que o
   apartamento está em uso.</p></div>
</div>''')

# ── 04 · as doze etapas (as mesmas do caderno de referência) ────────────
src = (P / 'build-gustavo-caderno.py').read_text(encoding='utf-8')
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
  <p class="lead" style="margin:0;max-width:112mm">Da decisão de vocês até o apartamento pronto
    são doze etapas — e nenhuma delas muda de dono.</p></div>
 <div class="rail"></div><div class="proc">{cols}</div>
</div>''')

# ── 05 · o Palha, por inteiro ───────────────────────────────────────────
PALHA = [
 ('O Palha no que se vê', 'Portas de giro, folhas de correr, rodapé e as laterais à vista saem '
  'no Palha da Duratex, com fita no mesmo tom. <b>Fechado, o armário é uma peça só</b>, de '
  'qualquer ângulo.'),
 ('O branco no que se usa', 'Caixa, prateleiras, divisórias e gavetas, por dentro, em '
  '<b>Branco TX</b>: o interior fica claro, a roupa aparece na cor verdadeira e o que está '
  'guardado se encontra rápido.'),
 ('A palha sintética', 'No closet da suíte, um par de portas recebe <b>aplicação de palha '
  'sintética</b>: a trama ventila o módulo e leva textura para a frente do armário.'),
]
folha(f'''<div class="ambw">
 <div class="band" style="height:104mm"><img src="{IMG['closet-palha']}" alt="" style="object-position:50% 40%">
  <div class="tag">Referência de ambiente</div>
  <div class="amostra"><img src="{IMG['palha']}" alt=""><div><div class="k">Palha</div>
   <div class="s">Duratex</div><div class="o">Imagens ilustrativas · a amostra física é
   apresentada na aprovação do projeto</div></div></div></div>
 <div class="low" style="display:block;padding:7mm 18mm 17mm"><div class="fitw">
  <div class="eyebrow">O padrão</div><div class="rule"></div>
  <h2 class="h2" style="margin:1mm 0 3mm">Palha por fora. Branco por dentro.</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:0 9mm">
   <div>{mv(PALHA[:1])}</div><div>{mv(PALHA[1:2])}</div><div>{mv(PALHA[2:])}</div></div>
  <div class="amb-nota" style="background:none;border-left-color:var(--gold);margin-top:4mm">
    <div class="t">O que isso pede da fábrica</div><p>Cada peça é cortada na cor do lado em
    que vai ficar — Palha no que se vê, Branco TX no que se usa — e recebe fita no tom do
    próprio lado. A troca de cor acontece onde a porta fecha, nunca à vista.</p></div></div>
 </div></div>''')

# ── 06… · as folhas de ambiente, SEM preço ──────────────────────────────
TANDEM = ('Gavetas e sapateiras', 'Sobre corrediça <b>Blum TANDEM com BLUMOTION</b>: a gaveta sai '
          'inteira e fecha sozinha, em silêncio.')
CLIP = ('Portas de giro', 'Com dobradiça <b>Blum CLIP top BLUMOTION</b> e puxador em cava '
        'usinado na própria folha: a porta fecha amortecida, sem bater.')
ACAB_GIRO = 'Exterior em MDF Palha · Duratex · interior em Branco TX · ferragem Blum'
ACAB_CORRER = 'Exterior em MDF Palha · interior em Branco TX · espelho prata em alumínio · SI Ocean 80 · Blum'
AMB = [
 ('O roupeiro<br>da suíte.', ['des-suite-e1'], 'Suíte master', ACAB_CORRER,
  [('Um lado para cada', 'O roupeiro se divide ao meio — um lado da Ana Carolina, o outro do '
    'André —, cada um com maleiro no alto, cabideiro e gavetas embaixo.'),
   ('Portas de correr', 'Correm no sistema <b>SI Ocean 80</b>, da Siforma, com amortecimento '
    'ao abrir e ao fechar: uma folha em Palha com cava usinada, a outra em espelho prata '
    'emoldurado em alumínio.'),
   ('As frentes das gavetas', 'Em Palha, como as portas: com o roupeiro aberto, o que aparece '
    'continua no mesmo padrão.'),
   TANDEM]),
 ('O closet<br>da suíte.', ['des-closet-suite-e1', 'des-closet-suite-e2'], 'Closet suíte master',
  ACAB_GIRO + ' · palha sintética',
  [('O lado da Ana Carolina', 'Do piso ao teto, fechado por portas de giro: maleiros no alto, '
    'cabideiros — o longo e o de calças — e, embaixo, gavetas, gavetas finas com chave e '
    'sapateiras.'),
   ('O lado do André', 'Maleiros, cabideiros e, embaixo, os <b>calceiros retráteis Slow '
    'Sense</b>, que deslizam para fora com amortecimento, e as sapateiras.'),
   ('Portas com palha sintética', 'O módulo de prateleiras e gavetas junto à porta se fecha com '
    '<b>um par de portas com aplicação de palha sintética</b>: a trama deixa o armário '
    'respirar.'),
   CLIP,
   ('Vinte gavetas', 'O closet contempla <b>vinte gavetas</b>: treze gavetas e sete sapateiras, '
    'todas sobre corrediça <b>Blum TANDEM com BLUMOTION</b> — a gaveta sai inteira e fecha '
    'sozinha, em silêncio.')]),
 ('O roupeiro<br>do Gabriel.', ['des-gabriel-e1'], 'Quarto Gabriel', ACAB_CORRER,
  [('Portas de correr', 'Correm no sistema <b>SI Ocean 80</b>, da Siforma, com amortecimento '
    'ao abrir e ao fechar: uma folha em Palha com cava usinada, a outra em espelho prata '
    'emoldurado em alumínio.'),
   ('O espelho do quarto', 'A folha de espelho é o espelho de corpo inteiro do Gabriel, sem '
    'ocupar parede.'),
   ('Por dentro', 'Maleiro no alto, cabideiros e, embaixo, gavetas e sapateiros.'),
   TANDEM]),
 ('O closet<br>da Isabella.', ['des-isabella-e01', 'des-isabella-e2'], 'Closet Isabella', ACAB_GIRO,
  [('Armário da parede da porta', 'Maleiros no alto, prateleiras, cabideiro longo e '
    'sapateiros embaixo, atrás de portas de giro.'),
   ('Armário da parede longa', 'Maleiros, prateleira, cabideiros e as colunas de gavetas, '
    'gavetas finas e sapateiros, todo fechado por portas de giro.'),
   CLIP, TANDEM]),
 ('O armário<br>da Isabella.', ['des-quarto-isabella'], 'Quarto Isabella', ACAB_CORRER,
  [('Portas de correr', 'No sistema <b>SI Ocean 80</b>, com amortecimento nos dois sentidos: '
    'folhas em Palha com cava usinada e uma em espelho prata emoldurado em alumínio.'),
   ('Por dentro', 'Maleiros no alto, uma coluna de prateleiras, cabideiros e gavetas com a '
    'frente em Palha.'),
   ('Junto à janela', 'Uma lateral fixa, recuada, deixa a cortina correr na frente do '
    'armário.'),
   TANDEM]),
]
for titulo, imgs, tag, acab, itens in AMB:
    folha(f'''<div class="amb">
     <div class="amb-img">{campo(*imgs, op=.92, tag=tag, legenda='Composição interna · desenho do projeto')}</div>
     <div class="amb-txt">
      <div class="eyebrow">Ambiente</div><div class="rule"></div>
      <div class="fit"><h2 class="h2" style="margin:1mm 0 4mm">{titulo}</h2>{mv(itens)}
       <div class="amb-nota" style="background:none;border-left-color:var(--line)">
         <div class="t">Acabamentos</div><p>{E(acab)}</p></div></div>
     </div></div>''', foot_r=True)
N_AMB = (5, N[0])          # folhas 6 a N: o texto dos ambientes

# ── por que Blum ────────────────────────────────────────────────────────
STATS = [
 ('200 mil', 'aberturas e fechamentos', 'É o ensaio a que a Blum submete as suas dobradiças '
  'antes de elas saírem da fábrica.'),
 (f'{GAR} anos', 'de garantia Valvic', 'No projeto inteiro, quando a ferragem é Blum — termo '
  'assinado no dia da entrega.'),
 ('Áustria', 'empresa familiar', 'A Blum desenha e fabrica as próprias ferragens, com controle '
  'de qualidade em cada etapa da produção.'),
 ('BLUMOTION', 'o fechamento amortecido', 'Porta e gaveta fecham suave e silenciosamente, toda '
  'vez — sem a batida que, com os anos, é o que desgasta o móvel.'),
]
st = ''.join(f'''<div class="st"><div class="n">{E(n)}</div><div class="u">{E(u)}</div>
  <div class="d">{E(d)}</div></div>''' for n, u, d in STATS)
folha(f'''<div class="pad">
 <div class="eyebrow">Por que Blum</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">A ferragem é a única parte<br>do móvel que trabalha todo dia.</h1>
 <p class="lead" style="max-width:225mm;color:#CFC6B4">É ela que decide se, daqui a muitos anos, a
  porta ainda fecha alinhada e a gaveta ainda corre macia. Por isso este projeto sai só na
  linha Blum, uma das referências mundiais em ferragem de movimento para móveis.</p>
 <div class="stats">{st}</div>
 <div class="frase">Neste projeto, toda porta de giro e toda gaveta se movem sobre Blum —
  <em>sem exceção.</em></div>
 <div class="box escuro" style="margin-top:auto"><div class="t">Testada antes de chegar aqui</div>
  <p>Na fábrica da Blum, as ferragens passam por ensaios de movimento, de carga e de corrosão —
   com calor, água e sal — que reproduzem em laboratório o desgaste de anos de uso. O que
   chega à nossa bancada já provou que dura.</p></div>
</div>''', dark=True)

# ── as ferragens deste projeto (a folha dedicada) ───────────────────────
FER = [
 ('Dobradiça', 'Blum CLIP top BLUMOTION', ['dobradica'], [
   'Amortecimento <b>BLUMOTION</b> embutido no caneco: a porta fecha suave e em silêncio.',
   'Encaixe <b>CLIP</b>: a porta se monta e se retira sem ferramenta, para limpeza ou ajuste.',
   'Regulagem em altura, lateral e profundidade: a porta se realinha em minutos.',
   'Testada em <b>200 mil</b> aberturas e fechamentos.']),
 ('Corrediça', 'Blum TANDEM com BLUMOTION', ['tandem', 'gaveta'], [
   'Oculta sob a gaveta: a lateral fica limpa, sem trilho de metal à vista.',
   'Extração total: a gaveta sai inteira e mostra o fundo.',
   '<b>BLUMOTION</b> integrado: no fim do curso, a gaveta se recolhe sozinha e fecha sem ruído.',
   'Carga de até <b>30 kg</b> por gaveta.']),
 ('Sistema de correr', 'SI Ocean 80 · Siforma', ['correr', 'si-ocean'], [
   'Para roupeiros de portas de correr, com folhas de até <b>80 kg</b>.',
   'Amortecimento nos dois sentidos: a folha desacelera ao abrir e ao fechar.',
   'Certificado em <b>100 mil</b> ciclos de uso.',
   'Recebe as folhas em Palha e as de espelho prata dos roupeiros e do armário da Isabella.']),
]
def fcard(k, nome, imgs, pts):
    principal = f'<div class="fi"><img src="{IMG[imgs[0]]}" alt=""></div>'
    extra = (f'<div class="fx"><img src="{IMG[imgs[1]]}" alt=""></div>' if len(imgs) > 1 else '')
    li = ''.join(f'<li>{p}</li>' for p in pts)
    return f'''<div class="fc"><div class="fimg">{principal}{extra}</div>
      <div class="fk">{E(k)}</div><div class="fn">{E(nome)}</div><ul>{li}</ul></div>'''
folha(f'''<div class="pad" style="padding-top:13mm">
 <div class="eyebrow">As ferragens deste projeto</div><div class="rule"></div>
 <div style="display:flex;align-items:baseline;gap:9mm;margin-bottom:4mm">
  <h1 class="h1" style="margin:0;white-space:nowrap">O que vocês tocam todo dia.</h1>
  <p class="lead" style="margin:0;max-width:120mm">Cada porta, cada gaveta e cada folha de correr
   deste projeto se move sobre uma destas três peças.</p></div>
 <div class="fers">{''.join(fcard(*f) for f in FER)}</div>
 <div class="leg-f">Imagens ilustrativas.</div>
</div>''')

# ── a garantia ──────────────────────────────────────────────────────────
PASSOS = [('Vocês nos chamam', 'Por telefone, WhatsApp ou e-mail, direto com a fábrica. Sem central e sem intermediário.'),
          ('Respondemos em 24 horas', 'Esse é o nosso compromisso de retorno, contado a partir do chamado.'),
          ('Visita em até três dias úteis', 'Se não resolvermos pelo telefone, a equipe vai ao local. Dentro do prazo de garantia, visita e reparo não têm custo.')]
passos = ''.join(f'''<div class="pe"><div class="pe-n">{i:02d}</div><div class="pe-t">{E(t)}</div>
  <div class="pe-l">{E(d)}</div></div>''' for i, (t, d) in enumerate(PASSOS, 1))
folha(f'''<div class="pad">
 <div class="eyebrow">Garantia</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Trinta anos. O termo é assinado na entrega.</h1>
 <p class="lead" style="max-width:215mm">A garantia da Valvic <b>é escalonada pela ferragem</b> —
  e a linha Blum é a do prazo mais longo da casa. Ela vale para o projeto inteiro e não é
  promessa de proposta: é <b>termo assinado no dia da entrega</b>, junto com o guia de
  conservação do móvel.</p>
 <div class="g1">
  <div class="gar justo" style="grid-template-columns:1fr;margin-top:0">
   <div class="c hi"><div class="anos">{GAR}</div><div class="unid">anos de garantia</div>
    <div class="nm">Linha Blum</div>
    <div class="x">Marcenaria e ferragem de movimento, no projeto inteiro.</div></div></div>
  <div><div class="eyebrow" style="margin-bottom:3mm">Como se aciona</div>{passos}</div>
  <div><div class="eyebrow" style="margin-bottom:3mm">O que o termo cobre</div>
   <div class="term"><div class="k">Marcenaria e ferragem de movimento</div>
    <div class="s">Estrutura, frentes, corrediças, dobradiças e o sistema de correr, pelo prazo da linha.</div></div>
   <div class="term"><div class="k">Montagem e instalação</div>
    <div class="s">Instalações e regulagens têm garantia de dois anos.</div></div>
   <div class="eyebrow" style="margin:4mm 0 2mm">O que fica de fora</div>
   <div class="term"><div class="k">Desgaste, umidade e alteração por terceiro</div>
    <div class="s">Dano vindo da obra ou mudança feita no móvel depois da entrega.</div></div></div>
 </div></div>''')
N0 = N[0] + 1   # ⛔ a primeira folha com preço

# ── investimento ────────────────────────────────────────────────────────
NOME_AMB = {'Suíte master': 'Roupeiro da suíte', 'Closet suíte master': 'Closet da suíte',
            'Quarto Gabriel': 'Roupeiro do Gabriel', 'Closet Isabella': 'Closet da Isabella',
            'Quarto Isabella': 'Armário da Isabella'}
DESC_AMB = {'Suíte master': 'Portas de correr SI Ocean 80, uma em espelho prata',
            'Closet suíte master': 'Portas de giro, par de portas em palha sintética, calceiros '
                                   'retráteis e vinte gavetas: treze gavetas e sete sapateiras',
            'Quarto Gabriel': 'Portas de correr SI Ocean 80, uma em espelho prata',
            'Closet Isabella': 'Armários com portas de giro, gavetas e sapateiros',
            'Quarto Isabella': 'Portas de correr SI Ocean 80, uma em espelho prata'}
rows = ''.join(f'<tr><td class="l">{E(NOME_AMB[a])}<div class="sub">{E(DESC_AMB[a])}</div></td>'
               f'<td class="hi">{brs(PR.PV_R[a])}</td></tr>' for a in PR.ORDEM)
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · linha Blum</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O apartamento, peça por peça.</h1>
 <div class="invg">
  <div>
   <p class="lead" style="max-width:none">Cada móvel foi levantado <b>peça por peça do projeto
    executivo</b> — nada é rateio nem estimativa por metro quadrado. Valores em reais.</p>
   <table class="inv" style="margin-top:5mm">
    <tr><th class="l">Ambiente</th><th class="hi">Linha Blum</th></tr>
    {rows}
    <tr class="tot"><td class="l">O projeto completo</td><td class="hi">{brs(PR.TOTAL)}</td></tr>
   </table>
  </div>
  <div class="gar justo" style="grid-template-columns:1fr;margin-top:0">
   <div class="c hi"><div class="unid" style="margin-top:0">O projeto completo</div>
    <div class="tv">{br(PR.TOTAL)}</div>
    <div class="x">MDF Palha por fora e Branco TX por dentro, ferragem Blum, sistema SI
     Ocean 80 e {GAR} anos de garantia.</div>
    <div class="l"><div class="k">Entrada, na assinatura</div>
     <div class="v">{br(PR.TOTAL * PR.PAGTO[0][1])}</div></div></div></div>
 </div>
 <div class="box" style="margin-top:auto"><div class="t">O que está incluso</div>
  <p>Projeto executivo de marcenaria, MDF Palha por fora e Branco TX por dentro, usinagem,
   ferragens Blum, o sistema de correr SI Ocean 80, as folhas de espelho em alumínio, a
   aplicação de palha sintética, os calceiros Slow Sense, transporte, montagem e instalação —
   num só contrato, com uma só data e uma só arquiteta responsável.</p></div>
</div>''')

# ── condições ───────────────────────────────────────────────────────────
pay = ''.join(f'<tr><td>{E(r)}</td><td class="d">{p*100:.0f}%</td></tr>' for r, p in PR.PAGTO)
folha(f'''<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">Condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Prazo, pagamento e fronteiras.</h1>
 <div class="three">
  <div>
   <div class="term"><div class="k">Validade desta proposta</div><div class="v">{E(VALIDADE)}</div>
     <div class="s">A partir desta data. É por esse tempo que conseguimos reservar a vaga
       na agenda da fábrica que sustenta a entrega em {E(PRAZO)}.</div></div>
   <div class="term"><div class="k">Prazo de execução</div><div class="v">{E(PRAZO)}</div>
     <div class="s">Contados a partir da medição técnica no local, não da assinatura. A
       medição tem data própria no cronograma.</div></div>
   <div class="term"><div class="k">Garantia</div><div class="v">{GAR} anos · linha Blum</div>
     <div class="s">Instalação e regulagem, dois anos. Termo assinado na entrega.</div></div>
   <div class="term"><div class="k">Projeto executivo de marcenaria</div><div class="v">Incluso</div>
     <div class="s">Aprovado por vocês e pela arquiteta {E(ARQ)} antes de qualquer corte.</div></div>
  </div>
  <div>
   <table class="pay" style="width:100%">
    <tr><td colspan="2" style="border:none;padding-bottom:2mm"><span class="eyebrow">Formas de pagamento</span></td></tr>
    {pay}</table>
   <div style="font-size:7.4pt;color:var(--mut);margin-top:2.5mm;letter-spacing:.06em">
     Todas as parcelas por transferência bancária.</div>
   <div class="box" style="margin-top:5mm"><div class="t">A amostra do padrão</div>
    <p>O Palha e a palha sintética são apresentados em amostra física na aprovação do
     projeto executivo, antes da compra da chapa.</p></div>
  </div>
  <div class="fora">
   <div class="eyebrow" style="margin-bottom:3mm">O que não está nesta proposta</div>
   <ul>
    <li><div class="k">Suíte</div><div class="v">A bancada sob a janela, as mesinhas e o
      painel de cabeceira.</div></li>
    <li><div class="k">Quarto da Isabella</div><div class="v">Cama, cômoda, estante e quadro
      de desenho, a cortina e o trilho.</div></li>
    <li><div class="k">Banheiros e pedra</div><div class="v">Bancadas, cubas, box, louças e
      metais.</div></li>
    <li><div class="k">Obra e iluminação</div><div class="v">Portas de passagem, iluminação de
      forro, elétrica e ar-condicionado.</div></li>
    <li><div class="k">Móveis existentes e decoração</div><div class="v">O berço, a poltrona,
      a cômoda e a cama do Gabriel, o puff e os objetos.</div></li>
   </ul>
  </div>
 </div>
 <div class="sig"><div class="ln">{E(CLIENTE)}</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

# ── encerramento ────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome" style="font-size:36pt">Um contrato.<br>Uma data.<br>Um nome<br>para chamar.</div>
  <div class="cv-s">Obrigado pela confiança de pôr este apartamento na nossa mão. O desenho da
   arquiteta {E(ARQ)} sai da nossa fábrica e chega instalado.</div>
  <div class="cv-meta">
   <div><div class="k">Proposta</div><div class="v">{E(CLIENTE)}</div></div>
   <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['dobradica']}" alt="" style="object-position:55% 50%"></div>
</div>''', dark=True, rodape=False)

# ── estilo e montagem ───────────────────────────────────────────────────
EXTRA = re.search(r"EXTRA = '''(.*?)'''", src, re.S).group(1)
AJUSTE = re.search(r"AJUSTE = '''(.*?)'''", src, re.S).group(1)
EXTRA += '''
/* ── a paleta deste caderno: papel quente e o Palha ────────────────── */
:root{--paper:#FCFAF5;--palha:#EAE6D5}
.slide{background:var(--paper)}
.slide.dark{background:var(--deep)}
/* o campo Palha com o desenho multiplicado: o branco do papel desaparece */
.campo{position:absolute;inset:0;display:flex;flex-direction:column;gap:6mm;
       justify-content:center;align-items:center;padding:14mm 12mm 18mm;
       background:radial-gradient(120% 95% at 28% 22%,#F4F1E7 0%,#E8E3D1 50%,#D6CDB3 100%)}
.slide .campo img{mix-blend-mode:multiply;opacity:var(--op);min-height:0;min-width:0;
          object-fit:contain;flex:1 1 0;width:100%;height:auto}
.slide .campo.row{flex-direction:row;gap:12mm}
.slide .campo.row img{height:100%;width:auto}
.campo .leg{position:absolute;top:7mm;left:9mm;font-size:6.2pt;letter-spacing:.26em;
           text-transform:uppercase;color:#7A6F55;font-weight:600}
.campo .tag{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);
  font-size:6.4pt;letter-spacing:.28em;text-transform:uppercase;padding:3mm 6mm;font-weight:600}
.cv-r .campo{padding:16mm 14mm}
.cv-selo{position:absolute;right:12mm;bottom:12mm;background:rgba(36,31,27,.86);
         padding:4.5mm 6mm;color:#F6F1E7;min-width:58mm}
.cv-selo .k{font-size:6.2pt;letter-spacing:.3em;text-transform:uppercase;color:var(--gold-lt);font-weight:600}
.cv-selo .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:24pt;line-height:1.05;margin-top:1mm}
.cv-selo .s{font-size:7.4pt;color:#CFC6B4;margin-top:1mm}
.band .campo{padding:9mm 30mm}
/* a ficha da amostra, sobre a foto de referência */
.amostra{position:absolute;right:12mm;bottom:9mm;background:var(--paper);padding:3.4mm;
         display:flex;gap:4mm;align-items:center;box-shadow:0 3mm 10mm rgba(26,23,20,.22);
         max-width:96mm}
.ambw .band .amostra img{width:30mm;height:30mm;flex:none;object-fit:cover}
.amostra .k{font-family:'Cormorant Garamond',Georgia,serif;font-size:24pt;line-height:1}
.amostra .s{font-size:7pt;letter-spacing:.28em;text-transform:uppercase;color:var(--gold);
            font-weight:600;margin-top:1.2mm}
.amostra .o{font-size:6.4pt;color:var(--mut);margin-top:2mm;line-height:1.4}
/* por que Blum: quatro números */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:6mm;margin-top:10mm}
.st{border-top:1.5px solid var(--gold-lt);padding-top:4mm}
.st .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:36pt;line-height:1;
       color:var(--gold-lt);font-weight:500;white-space:nowrap}
.st .u{font-size:6.8pt;letter-spacing:.24em;text-transform:uppercase;color:#E9E1D3;
       font-weight:600;margin-top:2.4mm}
.st .d{font-size:9pt;color:#CFC6B4;margin-top:2.6mm;line-height:1.5}
.frase{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;line-height:1.25;
       color:#EDE6D9;margin-top:13mm;max-width:210mm}
.frase em{color:var(--gold-lt)}
.box.escuro{background:rgba(255,255,255,.05);border-left-color:var(--gold-lt)}
.box.escuro .t{color:var(--gold-lt)}
.box.escuro p{color:#CFC6B4}
.dark .h1{color:#F6F1E7}
/* a folha dedicada às ferragens */
.fers{display:grid;grid-template-columns:repeat(3,1fr);gap:6mm;flex:1;min-height:0}
.fc{display:flex;flex-direction:column;min-height:0}
.fimg{position:relative;height:72mm;flex:none;display:flex;gap:2mm;background:var(--deep)}
.fi{flex:1;min-width:0;overflow:hidden}
.fi img,.fx img{width:100%;height:100%;object-fit:cover;display:block}
.fx{width:30mm;flex:none;overflow:hidden}
.fk{font-size:6.6pt;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);
    font-weight:700;margin-top:4mm}
.fn{font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;line-height:1.1;
    font-weight:500;margin-top:1mm}
.fc ul{margin:2.6mm 0 0;padding:0;list-style:none}
.fc li{font-size:8pt;color:var(--soft);line-height:1.45;padding:1.5mm 0 1.5mm 3.6mm;
       border-bottom:1px solid var(--hair);position:relative}
.fc li:last-child{border-bottom:none}
.fc li::before{content:"";position:absolute;left:0;top:3.2mm;width:4px;height:4px;
               border-radius:50%;background:var(--gold-lt)}
.fc li b{color:var(--ink)}
.leg-f{font-size:6.4pt;color:var(--mut);letter-spacing:.06em;margin-top:2mm}
/* garantia de uma linha só */
.g1{display:grid;grid-template-columns:.8fr 1fr 1fr;gap:8mm;margin-top:6mm;flex:1;align-items:start}
/* investimento de uma linha só */
.invg{display:grid;grid-template-columns:1.35fr 1fr;gap:10mm;margin-top:4mm;align-items:start}
.inv td .sub{font-size:7.4pt;color:var(--mut);margin-top:.6mm;font-weight:400}
.inv td.l{padding-top:2.6mm;padding-bottom:2.6mm}
.gar .tv{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;line-height:1.05;
         color:#F6F1E7;margin-top:3mm;white-space:nowrap}
'''
HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Proposta · {E(CLIENTE)}</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@'
        '9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
        f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S)
        + f'<script>{AJUSTE}caber();</script></body></html>')

# ── as travas ───────────────────────────────────────────────────────────
NF = len(S)
assert 'R$' not in ''.join(S[:N0 - 1]), '⛔⛔ PREÇO ANTES DA FOLHA DE VALOR'
_t = re.sub(r'<[^>]+>', ' ', re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S)))
for _c in ('Michell', 'Michelle', 'Jéssica', 'Jessica', 'Arlei', 'Gustavo', 'Luiza Pacheco',
           'Phillip', 'Giselle', 'Janaina', 'Mateus', 'Tereza', 'Júnia', 'Rafael',
           'Lagoa Santa', 'Vale dos Pinhais'):
    assert _c not in _t, f'⛔⛔ VESTÍGIO DE OUTRO CLIENTE: {_c}'
assert not [c for c in '⭐⛔⚠' if c in ''.join(S)], '⛔ marcação interna'
for _p in ('cartão', 'cartao', 'desconto', 'valor cheio', 'telescópica', 'hettich'):
    assert _p not in _t.lower(), f'⛔ a peça fala em "{_p}"'
_txt = lambda fs: re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', ''.join(fs)))
_amb = _txt(S[N_AMB[0] - 1:N_AMB[1]])
_suite = _txt([f for f in S[N_AMB[0] - 1:N_AMB[1]] if 'Closet suíte master' in f])
assert 'vinte gavetas' in _suite and 'treze gavetas e sete sapateiras' in _suite, '⛔ as vinte gavetas da suíte'
assert 'palha sintética' in _suite, '⛔ "mencionar isso na proposta": o par de portas em palha sintética'
assert 'Branco TX' in _t and 'por dentro e por fora' not in _t and 'Nenhuma chapa branca' not in _t, \
    '⛔ o interior agora é Branco TX [Jonathan, 09/11/2026]'
_g = sum(f[2] for i in __import__('levantamento').ITENS if i['amb'] == 'Closet suíte master'
         for f in i['ferr'] if f[4] == 'Corrediça')
assert _g == 20, ('⛔ as gavetas do closet da suíte mudaram no levantamento', _g)
assert set(NOME_AMB) == set(PR.ORDEM), '⛔ ambiente sem nome na folha de investimento'
_sem_suite = _txt([f for f in S[N_AMB[0] - 1:N_AMB[1]] if 'Closet suíte master' not in f])
assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _amb), '⛔ medida na descrição'
assert not re.search(r'\b(\d+|duas|dois|três|quatro|cinco|seis|dez|treze|doze)\s+(portas?|folhas?|gavet\w+|sapat\w+|prateleiras?)', _sem_suite, re.I), '⛔ contagem'
assert 'Nude' not in _t and 'Guararapes' not in _t, '⛔ o padrão é o Palha da Duratex'
assert PR.TOTAL == sum(PR.PV_R.values())

OUT = R / 'proposta-ana-carolina-andre.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-ana-carolina-andre.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'{PDF.name} · {NF} folhas · {PDF.stat().st_size // 1024} kB · primeiro preço na folha {N0}')
print(f'  Linha Blum {br(PR.TOTAL)} · entrada {br(PR.TOTAL * PR.PAGTO[0][1])}')
