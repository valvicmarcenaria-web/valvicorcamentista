# -*- coding: utf-8 -*-
"""ODINEY — caderno de proposta, linha Hettich  [16/11/2026]

⭐ [Jonathan, 16/11/2026] "ajuste o total para 629k considerando que o serviço será executado em
  Governador Valadares · crie a proposta com a linha Hettich com a página especial que fizemos
  para a Hettich". Valores por ambiente de `odiney/precos.py` (valores_gv): os preços fechados do
  Jonathan + a logística de Governador Valadares rateada, fechando em R$ 629.000.
⭐ Ripado 1×1 da suíte de hóspedes em DESTAQUE, como ponto de atenção [Jonathan, 16/11/2026].
⭐ Estrutura do caderno do Ed. Mônica Salles: dois ambientes por folha, página da Hettich (Novisys).
⚠ RT 10%, sem comissão, prazo, pagamento e validade no padrão da casa — confirmar.
⛔ Sem metragem e sem contagem nas descrições · nenhum número digitado.
"""
import pathlib, subprocess, os, sys, base64, html, re, io, contextlib

P = pathlib.Path(__file__).resolve().parent
R = P / 'odiney'
sys.path.insert(0, str(R)); sys.path.insert(0, str(P))
with contextlib.redirect_stdout(io.StringIO()):
    import precos as PR
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')
src = (P / 'build-gustavo-caderno.py').read_text(encoding='utf-8')

CLIENTE = 'Odiney'
ARQ = 'ArqForma'
OBRA = 'Governador Valadares'
DATA = 'Novembro de 2026'
PRAZO, VALIDADE = '90 dias corridos', '7 dias úteis'
LIN = ('Hettich',)
GAR = {'Hettich': '10'}
CHAMADA = {'Hettich': 'Ferragem Hettich'}
PAGTO = [('Entrada, na assinatura do contrato', 0.30), ('30 dias após a assinatura', 0.20),
         ('60 dias após a assinatura', 0.20), ('90 dias após a assinatura', 0.30)]
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))
def b64(p): return 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
IMG = {p.stem: b64(p) for p in (P / 'img-odiney').glob('*.jpg')}

# ── os valores: por ambiente, em real cheio; o total é a soma do que se lê ──
VGV = PR.valores_gv()
DESC = {
 'Sala de TV': 'Home suspenso, painel Titânio com frisos dourados, cristaleira, painel com porta embutida e a prateleira iluminada do hall',
 'Cozinha': 'Armários almofadados da pia, torres da ilha e o painel em Carvalho',
 'Despensa': 'Prateleiras em L',
 'Lavanderia e lavabo': 'Armários almofadados com luz, nicho, despenseiro e a prateleira ripada do lavabo',
 'Quarto 01': 'Roupeiro com portas espelhadas, home ripado, painel, ripado, cabeceira estofada e criados',
 'Banheiro social': 'Armário de gavetões suspenso e espelho retroiluminado',
 'Suíte master': 'Painel frisado, muxarabi usinado com luz, mesas de cabeceira, bancada e painéis de TV',
 'Closet master': 'Closet aberto em Frapê e Carvalho, porta espelhada e prateleiras de vidro iluminadas',
 'Banheiro master': 'Armário suspenso com nicho central',
 'Hall íntimo': 'Armário em Frapê com nicho iluminado em Carvalho',
 'Suíte hóspedes': 'Roupeiro de correr, home, cabeceira em ripado 1×1 com painel frisado e mesa de cabeceira',
 'Banheiro suíte hóspedes': 'Armário suspenso iluminado e prateleiras',
 'Suíte filha': 'Estante, home, ripados com portas embutidas, bancada, criado oval e cabeceira estofada',
 'Banheiro suíte filha': 'Armário em Verde Jade com nicho e prateleiras suspensas',
 'Closet filha': 'Roupeiro almofadado com palhinha natural',
}
assert list(DESC) == PR.L.AMBIENTES, set(PR.L.AMBIENTES) ^ set(DESC)
LINHAS_INV = [(a, DESC[a], {l: VGV[a] for l in LIN}) for a in PR.L.AMBIENTES]
VAL = {l: [round(v[l]) for *_, v in LINHAS_INV] for l in LIN}
TOT = {l: sum(VAL[l]) for l in LIN}
assert TOT['Hettich'] == 629000, TOT

S, N = [], [0]
def folha(corpo, dark=False, rodape=True, foot_r=False, cls=''):
    N[0] += 1
    f = (f'<div class="foot{" r" if foot_r else ""}"><span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span>'
         f'<span>{N[0]:02d}</span></div>') if rodape else ''
    S.append(f'<div class="slide{" dark" if dark else ""}{" " + cls if cls else ""}">{corpo}{f}</div>')

def mv(itens):
    return ''.join(f'''<div class="mv"><span class="b"></span><span>
      <span class="t">{E(t)}</span> <span class="d">{d}</span></span></div>''' for t, d in itens)

# ── 01 · capa ───────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">Odiney</div>
  <div class="cv-s">A marcenaria da casa inteira,<br>da sala ao closet da filha.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">{E(ARQ)} Arquitetura</div></div>
   <div><div class="k">Obra</div><div class="v">{E(OBRA)}</div></div>
   <div><div class="k">Ferragem</div><div class="v">Hettich</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['sala-a']}" alt="" style="object-position:50% 50%"></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''', dark=True, rodape=False)

# ── 02 · abertura ───────────────────────────────────────────────────────
folha(f'''<div class="ambw">
 <div class="band duo3" style="height:96mm"><img src="{IMG['coz-a']}" alt="">
   <img src="{IMG['master-a']}" alt=""><img src="{IMG['closet-a']}" alt="">
   <div class="tag">O projeto</div></div>
 <div class="low" style="grid-template-columns:1fr;padding:11mm 18mm 12mm">
  <div><div class="eyebrow">O que este projeto pede</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 5mm">Uma casa inteira. Uma só mão, do corte à montagem.</h1>
   <p class="lead" style="max-width:none;font-size:10.4pt">No projeto da <b>{E(ARQ)}</b>: Carvalho
    Hanover e Frapê em quase todos os ambientes, Areia Matt almofadado na cozinha e na
    lavanderia, Titânio com frisos dourados na sala, ripados, muxarabi, espelhos, palhinha natural e
    luz embutida nos nichos. Da sala ao closet da filha, <b>uma só empresa responde por tudo o que
    está nestas folhas</b>, da medição à instalação em Governador Valadares. <em>Um contrato, uma
    data, um nome para chamar.</em></p></div>
 </div></div>''')

# ── 03 · a empresa e a infraestrutura ───────────────────────────────────
PIL = [
 ('01', 'O projeto pede mais que marcenaria.',
  'Espelhos, ripados, muxarabi, frisos metálicos, estofados, palhinha, portas embutidas nos '
  'painéis e luz embutida. Tudo isso entra no nosso escopo, no mesmo contrato e na mesma data. '
  '<b>Vocês não contratam mais ninguém</b> para a marcenaria e para o que faz parte dela. O que '
  'fica fora vem nomeado.'),
 ('02', 'A peça sai daqui conferida.',
  'Detalhamento, programação, usinagem, montagem e conferência acontecem dentro da nossa '
  'fábrica. Cada módulo é montado aqui antes de ser embalado: porta regulada, gaveta corrida, '
  'báscula ajustada. A conferência é <b>etapa do processo</b>, não boa vontade no fim.'),
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
   Na próxima folha, o caminho que o projeto percorre — etapa por etapa, até o dia em que a
   casa está em uso.</p></div>
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
  <p class="lead" style="margin:0;max-width:112mm">Da sua decisão até a casa pronta são doze
    etapas — e nenhuma delas muda de dono.</p></div>
 <div class="rail"></div><div class="proc">{cols}</div>
</div>''')


# ── as folhas de ambiente, SEM preço ────────────────────────────────────
AMB = [
 ('A sala de TV.', ['sala-a'], 'Sala de TV',
  'MDF Titânio e Carvalho Hanover, Duratex · Areia Matt, Guararapes · frisos metálicos dourados · vidro incolor',
  [('Home suspenso', 'Gavetões de puxador cava e o nicho em Carvalho, sob o tampo de pedra.'),
   ('Painel Titânio', 'Do home ao forro, desenhado por frisos metálicos dourados.'),
   ('Cristaleira', 'Em Carvalho com interior Areia Matt, portas de vidro, prateleiras iluminadas e o suporte de vinhos.'),
   ('Painel com porta embutida', 'Em Carvalho, com a porta de correr que leva à cozinha escondida no painel.'),
   ('Hall de acesso', 'A prateleira iluminada que atravessa o espelho orgânico.')]),
 ('A cozinha.', ['coz-a'], 'Cozinha',
  'MDF Areia Matt almofadado, Guararapes · painel em Carvalho Hanover · puxador alça Space gold',
  [('A pia', 'Armários almofadados com portas, gavetões, gavetas e o porta-pano.'),
   ('A ilha', 'As torres do forno e do micro-ondas, com gaveta.'),
   ('O painel', 'Em Carvalho, com a TV e a porta embutida da sala.')]),
 ('A lavanderia,<br>a despensa e o lavabo.', ['lav'], 'Serviço',
  'MDF Areia Matt almofadado · interior em Carvalho no nicho · puxador Órion cromo',
  [('Lavanderia', 'Armário superior com luz embaixo, inferiores almofadados, nicho iluminado e o despenseiro.'),
   ('Despensa', 'Prateleiras em L em Areia Matt.'),
   ('Lavabo', 'A prateleira ripada em Carvalho, sob a pia esculpida.')]),
 ('O quarto 01<br>e o banheiro social.', ['quarto'], 'Quarto 01',
  'MDF Areia Matt e Carvalho Hanover · espelho com perfil cromado · estofado',
  [('Roupeiro', 'Portas de correr espelhadas; por dentro, maleiro, cabideiros, gavetas, sapateiras e calceiro.'),
   ('Cama e TV', 'Painel em Carvalho, cabeceira estofada, ripado sob o forro e o home suspenso ripado.'),
   ('Criados', 'Em Areia Matt, com pés de serralheria cromados.'),
   ('Banheiro social', 'Armário de gavetões suspenso e espelho retroiluminado.')]),
 ('A suíte master.', ['master-a'], 'Suíte master',
  'MDF Carvalho Hanover, Duratex · Frapê, Arauco · pés de serralheria dourados',
  [('A cabeceira', 'Painel frisado sobre o muxarabi usinado, com uma linha de luz entre os dois.'),
   ('Mesas de cabeceira', 'Em Frapê, sobre pés de serralheria dourados, com prateleira entre os pés.'),
   ('A parede da TV', 'Painéis em Carvalho, bancada suspensa de gavetões e a prateleira em Frapê.')]),
 ('O closet<br>e o banheiro master.', ['closet-a'], 'Master',
  'MDF Frapê com interior em Carvalho Hanover · espelho · vidro com serralheria dourada',
  [('Closet', 'Aberto, com cabideiros, gavetas, sapateiras, porta de correr espelhada e prateleiras de vidro iluminadas.'),
   ('Banheiro master', 'Armário suspenso em Carvalho com o nicho central.')]),
 ('O hall íntimo.', ['hall-intimo'], 'Hall íntimo',
  'MDF Frapê, Arauco · nicho em Carvalho Hanover com luz',
  [('Armário', 'Do piso ao forro, com o nicho iluminado em Carvalho no meio das portas.')]),
 ('A suíte de hóspedes.', ['hosp-a'], 'Suíte hóspedes',
  'MDF Frapê e Carvalho Hanover · ripado 1×1 · frisos metálicos pretos · espelho',
  [('Roupeiro', 'De correr, com uma folha espelhada, puxador perfil preto e interior completo.'),
   ('Cabeceira e TV', 'Painel em Frapê com frisos pretos entre os ripados, e o home suspenso de gavetões.'),
   ('Mesa de cabeceira', 'Em Frapê, com pés de serralheria pretos.')]),
 ('Os banheiros<br>das suítes.', ['banho-filha'], 'Banheiros',
  'MDF Carvalho Hanover · Verde Jade, Arauco · metalon dourado',
  [('Suíte hóspedes', 'Armário suspenso em Carvalho com luz embaixo, e prateleiras.'),
   ('Suíte filha', 'Armário em Verde Jade com nicho em Carvalho e as prateleiras suspensas no metalon dourado.')]),
 ('A suíte<br>da filha.', ['filha-a'], 'Suíte filha',
  'MDF Frapê com Carvalho Hanover · ripados · estofado em suede · pés dourados',
  [('Parede da TV', 'Painel e ripados até o forro, com as portas do banheiro e do closet embutidas no ripado.'),
   ('Estante e home', 'Estante em Frapê com fundo em Carvalho, sobre o home suspenso.'),
   ('Bancada e mesa de cabeceira', 'Ripadas, com gavetões e portas.'),
   ('Criado oval', 'Com gavetas curvas e pés dourados, e a cabeceira estofada em gomos.')]),
 ('O closet<br>da filha.', ['closet-filha'], 'Closet filha',
  'MDF Frapê almofadado com palhinha natural · interior em Areia Matt · puxador ponto cup gold',
  [('Roupeiro', 'Portas almofadadas com palhinha natural; por dentro, maleiros, cabideiros, gavetas, sapateiras e calceiro.')]),
]
_a0 = N[0] + 1
# ⭐ [Jonathan, 12/11/2026] "mude a estrutura colocando dois ambientes por página":
#   cada folha leva duas metades, cada uma com a sua foto, o título, os itens e o acabamento
def metade(titulo, imgs, tag, acab, itens):
    return f'''<div class="dp">
     <div class="dp-img"><img src="{IMG[imgs[0]]}" alt=""><div class="tag">{E(tag)}</div></div>
     <div class="dp-txt"><div class="eyebrow">Ambiente</div><div class="rule"></div>
      <h2 class="h2">{titulo.replace("<br>", " ")}</h2>{DESTAQUE.get(tag, "")}{mv(itens)}
      <div class="amb-nota" style="background:none;border-left-color:var(--line)">
        <div class="t">Acabamentos</div><p>{E(acab)}</p></div></div></div>'''
DESTAQUE = {'Suíte hóspedes': '''<div class="dq"><div class="k">Ponto de atenção · ripado 1×1</div>
  <p>A cabeceira leva um ripado de <b>ripa e vão iguais, de desenho muito fino</b>. É o detalhe que
  mais pede precisão de usinagem e de montagem: as ripas são conferidas uma a uma na fábrica e
  montadas no prumo na obra.</p></div>'''}
for k in range(0, len(AMB), 2):
    folha(f'<div class="duplo">{"".join(metade(*a) for a in AMB[k:k + 2])}</div>')
N_AMB = (_a0, N[0])

# ── a garantia ──────────────────────────────────────────────────────────
PASSOS = [('Vocês nos chamam', 'Por telefone, WhatsApp ou e-mail, direto com a fábrica. Sem central e sem intermediário.'),
          ('Respondemos em 24 horas', 'Esse é o nosso compromisso de retorno, contado a partir do chamado.'),
          ('Visita em até três dias úteis', 'Se não resolvermos pelo telefone, a equipe vai ao local. Dentro do prazo de garantia, visita e reparo não têm custo.')]
passos = ''.join(f'''<div class="pe"><div class="pe-n">{i:02d}</div><div class="pe-t">{E(t)}</div>
  <div class="pe-l">{E(d)}</div></div>''' for i, (t, d) in enumerate(PASSOS, 1))
folha(f'''<div class="pad">
 <div class="eyebrow">Garantia</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O termo é assinado na entrega.</h1>
 <p class="lead" style="max-width:215mm">A garantia da Valvic <b>segue a ferragem</b>:
  dez anos na Hettich, para todo o projeto. Não é promessa
  de proposta: é <b>termo assinado no dia da entrega</b>, junto com o guia de conservação do
  móvel.</p>
 <div class="three" style="margin-top:6mm">
  <div><div class="eyebrow" style="margin-bottom:3mm">Como se aciona</div>{passos}</div>
  <div><div class="eyebrow" style="margin-bottom:3mm">O que o termo cobre</div>
   <div class="term"><div class="k">Marcenaria</div>
    <div class="s">Estrutura, painéis, frentes e acabamento, pelo prazo da linha escolhida.</div></div>
   <div class="term"><div class="k">Ferragem de movimento</div>
    <div class="s">Corrediça, dobradiça, articulador e o sistema de correr, pelo prazo da linha escolhida.</div></div>
   <div class="term"><div class="k">Montagem e instalação</div>
    <div class="s">Instalações e regulagens têm garantia de dois anos em qualquer linha.</div></div></div>
  <div><div class="eyebrow" style="margin-bottom:3mm">O que fica de fora</div>
   <div class="term"><div class="k">Iluminação em LED</div>
    <div class="s">É componente eletrônico e segue a garantia do fabricante.</div></div>
   <div class="term"><div class="k">Desgaste de uso</div>
    <div class="s">Assim como o dano por umidade ou infiltração vinda da obra.</div></div>
   <div class="term"><div class="k">Alteração por terceiro</div>
    <div class="s">Feita no móvel depois da entrega.</div></div></div>
 </div></div>''')
# ── a página da Hettich (a mesma do caderno do Attos, com imagens)  [Jonathan, 12/11/2026]
#   "use a página dedicada à hettich (com imagens) que já usamos em alguma proposta"
#   ⛔ dobradiça Hettich da casa = NOVISYS (Sensys não trabalhamos mais) · sem "Silent System"
FER = [
 ('Dobradiça', 'Hettich Novisys', [
   'Amortecimento <b>integrado à dobradiça</b>: a porta fecha suave e em silêncio, sem bater.',
   'Regulagem nos três sentidos: a porta se realinha em minutos, na obra ou anos depois.',
   'A mesma dobradiça em todas as portas de giro da casa, da cozinha ao closet da filha.']),
 ('Corrediça', 'Hettich · oculta, com amortecimento', [
   'O trilho corre <b>escondido por baixo da gaveta</b>: a lateral fica limpa.',
   'Extração total: a gaveta sai inteira — é o que o gavetão e o closet pedem.',
   'Fechamento amortecido: a gaveta se recolhe sozinha no fim do curso.']),
 ('Padrão Hettich', 'Ferragem alemã', [
   'A Hettich é ferragem alemã, testada para <b>dezenas de milhares de ciclos</b> de abertura.',
   'Peças de reposição e regulagem com a mesma marca, por todo o prazo da garantia.',
   'É a ferragem que nos permite responder pelo projeto <b>por dez anos</b>.']),
]


def fcol(k, nome, pts):
    li = ''.join(f'<li>{x}</li>' for x in pts)
    return f'''<div class="fc"><div class="fk">{E(k)}</div><div class="fn">{E(nome)}</div><ul>{li}</ul></div>'''


FAIXA = [('fer-hettich-gaveta', 'Gaveta Hettich'), ('fer-corredica-oculta', 'A corrediça oculta, sob a gaveta'),
         ('fer-sensys', 'Dobradiça Hettich')]
faixa = ''.join(f'<figure><img src="{IMG[i]}" alt=""><figcaption>{E(c)}</figcaption></figure>' for i, c in FAIXA)
folha(f'''<div class="pad" style="padding-top:13mm">
 <div class="eyebrow">A ferragem escolhida · linha Hettich</div><div class="rule"></div>
 <div style="display:flex;align-items:baseline;gap:9mm;margin-bottom:4mm">
  <h1 class="h1" style="margin:0;white-space:nowrap">O que se toca todo dia.</h1>
  <p class="lead" style="margin:0;max-width:118mm">A ferragem é a única parte do móvel que
   trabalha todos os dias — e é ela que decide por quanto tempo o móvel continua fechando bem.</p></div>
 <div class="faixa">{faixa}</div>
 <div class="fers">{''.join(fcol(*f) for f in FER)}</div>
 <div class="garf"><div class="anos">{GAR['Hettich']}</div><div><div class="k">anos de garantia Valvic</div>
  <div class="s">Na linha Hettich, sobre a marcenaria e a ferragem de movimento do projeto inteiro.
   Termo assinado no dia da entrega.</div></div><div class="leg-f">Imagens ilustrativas.</div></div>
</div>''')
N0 = N[0] + 1   # ⛔ a primeira folha com preço

rows = ''.join(
    f'<tr><td class="l">{E(n)} <span class="sub">· {E(d)}</span></td>'
    + ''.join(f'<td{" class=hi" if l == "Hettich" else ""}>{brs(VAL[l][i])}</td>' for l in LIN)
    + '</tr>' for i, (n, d, _v) in enumerate(LINHAS_INV))
folha(f'''<div class="pad" style="padding-top:11mm">
 <div class="eyebrow">Investimento · ambiente a ambiente</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 2mm">A casa, ambiente a ambiente.</h1>
 <p class="lead" style="max-width:235mm;font-size:9pt">Cada móvel foi levantado <b>peça por peça
  do caderno de marcenaria</b> — nada é rateio nem estimativa por metro quadrado. Valores em reais.</p>
 <table class="inv inv13" style="margin-top:3mm">
  <tr><th class="l">Ambiente</th>
   {''.join(f'<th{" class=hi" if l == "Hettich" else ""}>{E(l)}</th>' for l in LIN)}</tr>
  {rows}
  <tr class="tot"><td class="l">O projeto completo</td>
   {''.join(f'<td{" class=hi" if l == "Hettich" else ""}>{brs(TOT[l])}</td>' for l in LIN)}</tr>
 </table>
</div>''')

folha(f'''<div class="pad">
 <div class="eyebrow">Investimento</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O projeto completo.</h1>
 <p class="lead" style="max-width:215mm">A casa inteira, com ferragem <b>Hettich</b> e dez anos
  de garantia sobre a marcenaria e a ferragem, instalada em Governador Valadares.</p>
 <div class="gar justo duas"><div class="c hi">
     <div class="anos">{GAR['Hettich']}</div><div class="unid">anos de garantia</div>
     <div class="nm">Ferragem Hettich</div>
     <div class="x">Dobradiça com amortecedor e regulagem nos três sentidos.</div>
     <div class="l"><div class="k">O projeto completo</div>
      <div class="v" style="font-family:'Cormorant Garamond',Georgia,serif;font-size:23pt">{br(TOT['Hettich'])}</div></div>
     <div class="l" style="margin-top:2mm"><div class="k">Entrada, na assinatura</div>
      <div class="v">{br(TOT['Hettich'] * PAGTO[0][1])}</div></div></div>
  <div class="c"><div class="nm" style="margin-top:0">O que está incluso</div>
   <div class="x">Projeto executivo de marcenaria, material, usinagem, ferragem Hettich, os
    espelhos, os vidros, os estofados, a palhinha, os frisos metálicos, a serralheria dos pés e
    das prateleiras, a iluminação em LED embutida, <b>transporte, deslocamento e estadia da
    equipe em Governador Valadares</b>, montagem e instalação — num só contrato, com uma só data
    e uma só arquiteta responsável.</div></div></div>
</div>''')

pay = ''.join(f'<tr><td>{E(r)}</td><td class="d">{p*100:.0f}%</td></tr>' for r, p in PAGTO)
folha(f'''<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">Condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Prazo, pagamento e fronteiras.</h1>
 <div class="three">
  <div>
   <div class="term"><div class="k">Validade desta proposta</div><div class="v">{E(VALIDADE)}</div>
     <div class="s">A partir desta data.</div></div>
   <div class="term"><div class="k">Prazo de execução</div><div class="v">{E(PRAZO)}</div>
     <div class="s">Contados a partir da medição técnica no local, não da assinatura. A
       medição tem data própria no cronograma.</div></div>
   <div class="term"><div class="k">Garantia</div><div class="v">Dez anos</div>
     <div class="s">Dez anos na marcenaria e na ferragem Hettich. Instalação e regulagem, dois anos.
       Termo assinado na entrega.</div></div>
   <div class="term"><div class="k">Projeto executivo de marcenaria</div><div class="v">Incluso</div>
     <div class="s">Aprovado por vocês e pela {E(ARQ)} antes de qualquer corte.</div></div>
  </div>
  <div>
   <table class="pay" style="width:100%">
    <tr><td colspan="2" style="border:none;padding-bottom:2mm"><span class="eyebrow">Formas de pagamento</span></td></tr>
    {pay}</table>
   <div style="font-size:7.4pt;color:var(--mut);margin-top:2.5mm;letter-spacing:.06em">
     Todas as parcelas por transferência bancária.</div>

  </div>
  <div class="fora">
   <div class="eyebrow" style="margin-bottom:3mm">O que não está nesta proposta</div>
   <ul>
    <li><div class="k">Pedra</div><div class="v">Bancadas, tampos, ilha, sóculos, a caixa do
      nicho da sala e a pia esculpida do lavabo são marmoraria.</div></li>
    <li><div class="k">Eletros, metais e louças</div><div class="v">Televisões, adega, cooktop,
      coifa, forno, geladeira, cubas, torneiras, box e banheira.</div></li>
    <li><div class="k">Móveis e madeira maciça</div><div class="v">Cabeceiras, bancos, poltronas,
      camas e puffs comprados prontos, e o tampo da mesa em madeira maciça.</div></li>
    <li><div class="k">Acabamentos de obra</div><div class="v">Boiseries pintadas, portas de
      passagem Pormade, espelhos soltos de parede e o forro de gesso.</div></li>
    <li><div class="k">Obra e iluminação geral</div><div class="v">Pontos elétricos, piso,
      revestimentos e pintura de parede.</div></li>
   </ul>
  </div>
 </div>
 <div class="sig"><div class="ln">{E(CLIENTE)}</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome" style="font-size:36pt">Um contrato.<br>Uma data.<br>Um nome<br>para chamar.</div>
  <div class="cv-s">Obrigado pela confiança. O projeto da {E(ARQ)} sai da nossa fábrica e chega
   instalado em Governador Valadares.</div>
  <div class="cv-meta">
   <div><div class="k">Proposta</div><div class="v">{E(CLIENTE)}</div></div>
   <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['filha-b']}" alt="" style="object-position:50% 50%"></div>
</div>''', dark=True, rodape=False)

# ── estilo e montagem ───────────────────────────────────────────────────
EXTRA = re.search(r"EXTRA = '''(.*?)'''", src, re.S).group(1)
AJUSTE = re.search(r"AJUSTE = '''(.*?)'''", src, re.S).group(1)
EXTRA += '''
:root{--paper:#FCFAF5}
.slide{background:var(--paper)}
.slide.dark{background:var(--deep)}
.campo{position:absolute;inset:0;display:flex;flex-direction:column;gap:6mm;
       justify-content:center;align-items:center;padding:14mm 12mm 18mm;
       background:radial-gradient(120% 95% at 28% 22%,#F7F5EF 0%,#ECE8DD 55%,#DDD6C6 100%)}
.slide .campo img{mix-blend-mode:multiply;opacity:var(--op);min-height:0;min-width:0;
          object-fit:contain;flex:1 1 0;width:100%;height:auto}
.slide .campo.row{flex-direction:row;gap:10mm}
.slide .campo.row img{height:100%;width:auto}
.campo .leg{position:absolute;top:7mm;left:9mm;font-size:6.2pt;letter-spacing:.26em;
           text-transform:uppercase;color:#7A6F55;font-weight:600}
.campo .tag,.amb-img>.tag{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);
  font-size:6.4pt;letter-spacing:.28em;text-transform:uppercase;padding:3mm 6mm;font-weight:600}
.band .campo{padding:9mm 22mm}
.inv td .sub{font-size:7.4pt;color:var(--mut);margin-top:.6mm;font-weight:400}
.inv td.l{padding-top:2.4mm;padding-bottom:2.4mm}
.dark .h1{color:#F6F1E7}
.amb-img.duo{display:grid;grid-template-rows:1fr 1fr;gap:2mm;background:var(--paper)}
.amb-img.duo img{width:100%;height:100%;object-fit:cover;min-height:0}
.band.duo3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:2mm;position:relative}
.band.duo3 img{width:100%;height:100%;object-fit:cover;min-width:0}
.band.duo3 .tag{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);
  font-size:6.4pt;letter-spacing:.28em;text-transform:uppercase;padding:3mm 6mm;font-weight:600}
.gar.duas{grid-template-columns:1fr 1fr !important}
.duplo{display:grid;grid-template-columns:1fr 1fr;gap:9mm;height:100%;padding:10mm 14mm 16mm}
.dp{display:flex;flex-direction:column;min-height:0}
.dp-img{position:relative;height:70mm;flex:none;overflow:hidden;background:var(--sand)}
.dp-img img{width:100%;height:100%;object-fit:cover;display:block}
.dp-img .tag{position:absolute;left:0;bottom:0;background:var(--deep);color:var(--gold-lt);
  font-size:6.4pt;letter-spacing:.28em;text-transform:uppercase;padding:3mm 6mm;font-weight:600}
.dp-txt{padding-top:5mm;min-height:0}
.dp-txt .h2{font-size:19pt;margin:1mm 0 2.5mm}
.dp-txt .mv .t{font-size:8.8pt}
.dp-txt .mv .d{font-size:8.1pt}
.dp-txt .amb-nota{margin-top:3mm}
.dq{border:1.6px solid var(--gold);background:rgba(201,169,106,.10);border-radius:4px;padding:2.6mm 3.4mm;margin:0 0 2.6mm}
.dq .k{font-size:6.8pt;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);font-weight:700}
.dq p{font-size:8.2pt;line-height:1.45;margin-top:1mm;color:var(--ink)}
.faixa{display:flex;gap:3mm;height:58mm;flex:none;margin-top:1mm}
.faixa figure{margin:0;position:relative;height:100%;background:#fff;overflow:hidden}
.faixa img{height:100%;width:auto;display:block}
.faixa figcaption{position:absolute;left:0;bottom:0;background:rgba(36,31,27,.86);color:var(--gold-lt);
  font-size:6pt;letter-spacing:.22em;text-transform:uppercase;padding:1.8mm 3.4mm;font-weight:600}
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

.inv13 td,.inv13 th{padding-top:.8mm !important;padding-bottom:.8mm !important;font-size:8.4pt}
.inv13 td.l{padding-top:1.05mm;padding-bottom:1.05mm;font-size:8.8pt}
.inv13 td .sub{font-size:7pt;color:var(--mut);font-weight:400}

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
for _c in ('Michell', 'Michelle', 'Arlei', 'Gustavo', 'Raposo', 'Haverson', 'Luiza Pacheco',
           'Phillip', 'Giselle', 'Gisele', 'Alexandre', 'Ana Carolina', 'André', 'Attos', 'Kenia', 'Fábio',
           'Orlando', 'Ivone', 'Corsino', 'Sollero', 'Mônica', 'Salles', 'OCAPI', 'Dalila', 'Tereza', 'Júnia', 'Rafael', 'Lagoa Santa', 'Costa Laguna', 'Residencial Árvores'):
    assert _c not in _t, f'⛔⛔ VESTÍGIO DE OUTRO CLIENTE: {_c}'
assert not [c for c in '⭐⛔⚠' if c in ''.join(S)], '⛔ marcação interna'
for _p in ('cartão', 'cartao', 'desconto', 'margem', 'comissão', 'telescópica', 'sensys', 'blum', 'nada corta', 'corsino', 'gran royalle', 'jéssica', 'academia', 'sauna'):
    assert _p not in _t.lower(), f'⛔ a peça fala em "{_p}"'
_amb = re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', ''.join(S[N_AMB[0] - 1:N_AMB[1]]))).replace('1×1', '')
assert 'ripado 1×1' in ''.join(S) and 'Ponto de atenção' in ''.join(S), '⛔ o ripado 1×1 tem de estar em destaque [Jonathan, 16/11/2026]'
assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _amb), '⛔ medida na descrição'
assert not re.search(r'\b(\d+|duas|dois|três|quatro|cinco|seis|sete|oito|dez)\s+(portas?|folhas?|gavet\w+|básculas?|nichos?|prateleiras?)', _amb, re.I), '⛔ contagem'

OUT = R / 'proposta-odiney.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-odiney.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'{PDF.name} · {NF} folhas · {PDF.stat().st_size // 1024} kB · primeiro preço na folha {N0}')
for l in LIN:
    print(f'  {l:8s} {br(TOT[l])} · entrada {br(TOT[l] * PAGTO[0][1])}'); [print(f'    {n[:60]:60s} {brs(v)}') for (n, _d, _v), v in zip(LINHAS_INV, VAL[l])]
