# -*- coding: utf-8 -*-
"""CARLA · BH 2026 — APRESENTAÇÃO PREMIUM, A4 paisagem, 16 páginas.

[Jonathan 24/08] "utilize imagens do projeto na proposta" — e depois, ao ver a
de 9 páginas: "a proposta veio sem nenhuma imagem". Este é o documento que
fecha esse pedido. Mesma gramática do deck do Vinícius (padrão Junior), nos
valores de `corte-carla.py`.

  Investimento .................... R$ 109.300
  + Upgrade · tudo na cor ......... R$  18.500
  Com o upgrade ................... R$ 127.800

IMAGENS: 13 renders extraídos da `Apresentação_Carla.pdf` (arquiteta Virginia
Duarte), em `projetos/img-carla/`. São renders DO PROJETO DA CARLA — não são as
"imagens de referência" que os detalhamentos rotulam como inspiração de
terceiros, e que a regra da casa proíbe usar.

⚠ O RENDER MOSTRA MAIS DO QUE O ORÇAMENTO COBRE. A apresentação é do
  apartamento inteiro; o pacote de detalhamentos tem sete conjuntos. Página 3
  e página 15 dizem isso com todas as letras — proposta ilustrada com o
  apartamento todo e escopo de sete conjuntos é armadilha se não for nomeada.

REGRAS DA CASA APLICADAS (`referencias/proposta-comercial.md`):
  1. ⛔ nenhuma cota de móvel no texto — onde a dimensão é o argumento, ela é
     dita em palavras ("do piso ao forro", "parede inteira", "sem divisória")
  2. ⛔ nenhuma explicação de formação de preço — o upgrade é vendido por
     benefício, não por chapa, nesting ou otimização
  3. ✅ imagens do projeto conduzindo o layout — é o eixo deste arquivo
"""
import base64, os, subprocess

CLIENTE  = 'Carla'
OBRA     = 'Apartamento em Belo Horizonte'
ARQ      = 'Virginia Duarte'
DATA     = '24 de agosto de 2026'
VALIDADE = '7 dias corridos'
PRAZO    = 'Até 75 dias corridos'
IMGDIR   = 'projetos/img-carla'

def img(nome):
    with open(f'{IMGDIR}/{nome}.jpeg', 'rb') as f:
        return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()

INV, UP = 109300, 18500
INV_UP = INV + UP
assert INV_UP == 127800

# ── os sete conjuntos ─────────────────────────────────────────────────────
# `w` escolhe a gramática da página:
#   False → imagem em coluna vertical (móvel alto: torre, cristaleira, roupeiro)
#   True  → faixa de largura total (móvel comprido: painel de parede inteira)
#   'fit' → imagem emoldurada (o render da suíte tem 545 px; esticado vira pixel)
# `pos` é o object-position do recorte — é ele que decide QUAL móvel do render
# fica no enquadramento. Sem isso o corte centralizado mostra sempre o sofá.
AMB = [
 dict(n='01', nome='Cozinha', foto='copa-2', pos='48% 50%', w=False,
      tag='Bancada linear com a torre da geladeira integrada',
      mv=[('Armários inferiores em quatro módulos',
           'com nicho para lava-louças de embutir e gaveteiro no módulo do cooktop'),
          ('Aéreos com três portas',
           'alinhados à porta superior da torre — a linha de cima corre sem degrau de uma ponta à outra'),
          ('Nicho contínuo, sem divisória',
           'forno e micro-ondas lado a lado, sem moldura entre eles, com ventilação e passa-cabo previstos'),
          ('Torre da geladeira, do piso ao forro',
           'com o fundo alinhado ao fundo da bancada'),
          ('Puxador em cava usinada',
           'no próprio material, sem perfil aplicado'),
          ('Iluminação em LED 3000 K',
           'sob o aéreo e dentro do nicho')],
      nota=('A torre morre no mesmo plano',
            'De frente, ela avança e cria profundidade. De lado, o fundo da '
            'torre e o fundo da bancada terminam na mesma linha. É o que faz a '
            'cozinha parecer embutida na arquitetura, e não encostada nela.')),
 dict(n='02', nome='Painel amadeirado', foto='estar', pos='50% 30%', w=True,
      tag='Parede inteira revestida, do rodapé ao forro, com a porta integrada',
      mv=[('Painel sobre estrutura niveladora ancorada à parede',
           'não é chapa colada em reboco — por isso não estufa nem descola com o tempo'),
          ('Porta integrada ao painel',
           'batente oculto e dobradiça invisível: de fora, a parede é contínua e a porta desaparece nela'),
          ('Espelho lapidado com película de segurança',
           'instalado entre os frisos, sem sobreposição'),
          ('Frisos verticais usinados no próprio MDF',
           'em três faixas, com o mesmo veio do painel'),
          ('Reforço estrutural para a TV e para o rack',
           'a carga não fica na chapa')],
      nota=('Procure a porta',
            'Ela está na imagem. Batente oculto, dobradiça invisível e a '
            'paginação do painel atravessando a folha sem interrupção — é esse '
            'detalhe que separa um painel de um revestimento.')),
 dict(n='03', nome='Rack suspenso', foto='estar', pos='21% 50%', w=False,
      tag='Quatro frentes basculantes, solto do chão, com luz por baixo',
      mv=[('Quatro portas basculantes',
           'articulador dimensionado pela massa real de cada frente — abrem leves e param onde você soltar'),
          ('Tampo e base encorpados',
           'num móvel suspenso e longo, é a rigidez que impede a barriga no meio com o passar dos anos'),
          ('Barra metálica contínua ancorada na alvenaria',
           'o painel decorativo não recebe sozinho a carga do rack'),
          ('LED 3000 K em perfil recuado com difusor leitoso',
           'a luz aparece, a fita não')],
      nota=('Suspenso é decisão estrutural',
            'Um rack que não toca o chão joga todo o peso na parede. A barra '
            'metálica é chumbada na alvenaria <strong>antes</strong> de o '
            'painel subir. Depois que a parede fecha, não tem como.')),
 dict(n='04', nome='Cristaleira', foto='cozinha-1', pos='47% 50%', w=False,
      tag='Portas de vidro, prateleiras iluminadas e arremate no forro',
      mv=[('Duas portas de giro',
           'perfil de alumínio preto e vidro temperado, com puxador vertical metálico'),
          ('Prateleiras de vidro temperado lapidado',
           'cada uma com a sua própria linha de luz — o que se vê é a peça exposta, não a fonte'),
          ('Lateral esquerda com acabamento estendido até a parede',
           'para absorver o desaprumo sem deixar fresta'),
          ('Base niveladora e arremate superior recortado em obra',
           'depois do nivelamento, para o móvel encostar no forro sem vão')],
      nota=('Seis prateleiras, seis linhas de luz',
            'Iluminar a cristaleira por cima acende a prateleira de cima e '
            'deixa as outras cinco na sombra. Aqui cada prateleira tem a sua, '
            'recuada no perfil: você vê a louça, não a fita.')),
 dict(n='05', nome='Guarda-roupa da suíte', foto='suite', pos='50% 50%', w='fit',
      tag='Três folhas deslizantes, com a central em espelho',
      mv=[('Três folhas de correr',
           'perfil de alumínio escuro, roldana regulável e sistema antidescarrilamento'),
          ('Folha central integral em espelho',
           'com película de segurança na face de trás'),
          ('Oito gavetas em corrediça oculta',
           'mais prateleiras e maleiro superior com prateleira encorpada'),
          ('Cabideiros ovais metálicos com suporte reforçado',
           'com a profundidade útil preservada para os cabides')],
      nota=('Correr não pode ter folga',
            'Porta de correr desalinha quando a roldana não é regulável e o '
            'trilho não é nivelado peça a peça. As três folhas saem reguladas '
            'na montagem e voltamos a regular na entrega.')),
 dict(n='06', nome='Guarda-roupa em L', foto='quarto-2', pos='61% 50%', w=False,
      tag='Roupeiro e cabeceira no mesmo desenho, virando a esquina',
      mv=[('Roupeiro com quatro portas de giro',
           'do piso ao forro, com cabideiro contínuo'),
          ('Mesa de cabeceira com duas gavetas',
           'alinhada ao último módulo do roupeiro — a esquina fecha sem sobra nem emenda aparente'),
          ('Módulo vertical com prateleiras',
           'resolvendo o encontro entre o roupeiro e a cama'),
          ('Nicho iluminado sobre a cabeceira',
           'em MDF encorpado, com passa-fio previsto'),
          ('Armário aéreo com duas portas de giro',
           'sobre a cama')],
      nota=('A esquina é onde o móvel mente',
            'Roupeiro em L quase sempre entrega um vão morto no canto ou uma '
            'emenda no meio da frente. Aqui o retorno é dimensionado junto com '
            'a cabeceira, e o canto fecha no desenho.')),
 dict(n='07', nome='Marcenaria sob a escada', foto='escada', pos='35% 50%', w=False,
      tag='O vão da escada vira armário e vitrine',
      mv=[('Porta em vidro Reflecta temperado',
           'em perfil de alumínio preto, com dobradiça reforçada e puxador vertical'),
          ('Nichos que acompanham a diagonal da escada',
           'e terminam zerados sobre a base — o desenho segue a escada em vez de brigar com ela'),
          ('LED 3000 K inclusive nos nichos diagonais',
           'em perfil recuado, sem ponto de luz aparente'),
          ('Prateleiras encorpadas e rodapé recuado',
           'para o vão respirar por baixo')],
      nota=('Debaixo da escada é onde se perde metro quadrado',
            'Cada nicho tem uma altura diferente, porque a escada desce. '
            'Fechar tudo num armário reto desperdiça o vão; seguir a diagonal '
            'dá aproveitamento e desenho ao mesmo tempo.')),
]

# ── investimento (mesma partição do `build-carla.py`) ──────────────────────
PRECO = {'01': 22200, '02': 15500, '03': 5200, '04': 4900,
         '05': 27500, '06': 25900, '07': 8100}
assert sum(PRECO.values()) == INV

NOMES_INV = {'01': 'Cozinha linear com torre de geladeira',
             '02': 'Painel amadeirado até o forro',
             '03': 'Rack suspenso',
             '04': 'Cristaleira até o forro',
             '05': 'Guarda-roupa de três portas de correr',
             '06': 'Guarda-roupa em L com cabeceira',
             '07': 'Marcenaria sob a escada'}

# ── as frentes que a Valvic coordena ──────────────────────────────────────
FRENTES = [
 ('01', 'Marcenaria', 'Corte e usinagem em CNC própria e laminação de borda em '
  'coladeira automática própria. O que define o acabamento não sai da nossa '
  'fábrica — e quem produz é quem monta.'),
 ('02', 'Vidraçaria', 'As duas portas de vidro temperado da cristaleira, as '
  'prateleiras temperadas lapidadas e a porta em vidro Reflecta sob a escada.'),
 ('03', 'Espelharia', 'Espelho lapidado com película de segurança no painel da '
  'sala e na folha central do guarda-roupa da suíte.'),
 ('04', 'Serralheria', 'A barra metálica contínua que sustenta o rack, chumbada '
  'na alvenaria, e os cabideiros ovais com suporte reforçado.'),
 ('05', 'Alumínio', 'Os perfis pretos das portas de vidro, os puxadores '
  'verticais metálicos e o sistema de correr de três folhas.'),
 ('06', 'Iluminação', 'Fita de LED 24 V · 3000 K · IRC ≥ 90 em perfil de '
  'alumínio com difusor leitoso, com driver bivolt acessível para manutenção.'),
]

# ── especificação que atravessa o projeto inteiro ─────────────────────────
ESPEC = [
 ('Chapa', 'MDF BP com painéis encorpados nos nichos e nas prateleiras longas, '
  'e fundo encaixado em ranhura — nunca grampeado por trás.'),
 ('Borda', 'Fita <strong>ABS</strong> aplicada em coladeira automática, mais '
  'espessa nas faces aparentes.'),
 ('Puxador', '<strong>Cava usinada</strong> no próprio material, e perfil '
  'vertical preto onde a prancha pede.'),
 ('Ferragem', 'Linha <strong>Hettich</strong> em todo o projeto: dobradiça '
  '<strong>Novisys</strong> com amortecimento, corrediça oculta '
  '<strong>Quadro</strong> e articulador <strong>Blum HK-xs</strong> nas '
  'básculas do rack.'),
 ('Iluminação', 'Fita de LED <strong>24 V · 3000 K · IRC ≥ 90</strong> em perfil '
  'de alumínio com difusor leitoso, com driver bivolt dimensionado com folga e '
  'acessível para manutenção.'),
 ('Vidro e espelho', 'Espelho lapidado com <strong>película de segurança</strong>; '
  'vidro temperado nas portas da cristaleira, nas prateleiras e na porta '
  'Reflecta sob a escada.'),
 ('Fixação', 'Niveladores, cantoneiras ocultas e ancoragem <strong>na alvenaria '
  'ou na estrutura</strong> — nunca só no painel decorativo.'),
 ('Produção e montagem', 'Corte, usinagem e laminação de borda em máquina '
  'própria, e <strong>instalação e montagem por equipe própria da Valvic</strong>.'),
]

PAGTO = [
    ('Entrada de 30% + saldo em até 10× no cartão', '—'),
    ('Entrada de 50% + saldo em até 8× no cartão',  '3%'),
    ('Entrada de 70% + saldo em até 6× no cartão',  '5%'),
    ('Entrada de 70% + saldo por transferência',    '7%'),
]

# ⚠ O PRIMEIRO ITEM DA LISTA É O MAIS IMPORTANTE DESTA PROPOSTA.
#   O deck é ilustrado com os renders do apartamento inteiro. Se ele não disser
#   nominalmente o que ficou de fora, a cliente lê "o apartamento" e a falta
#   aparece na obra — que é o pior lugar do mundo para descobrir escopo.
FORA = [
 ('Os móveis que aparecem nos renders e ainda não têm prancha executiva',
  'A apresentação da arquiteta é do apartamento inteiro. Também aparecem nela '
  'marcenaria no <strong>banheiro social</strong>, no <strong>banheiro da '
  'suíte</strong>, no <strong>quarto com sofá</strong> e a <strong>bancada com '
  'espelho</strong> do quarto do guarda-roupa em L — além da estante e do '
  'balcão da <strong>copa</strong>. Esses conjuntos não vieram no pacote de '
  'detalhamento executivo e <strong>não estão neste valor</strong>. Assim que '
  'as pranchas chegarem, orçamos e apresentamos à parte.'),
 ('Tampo e rodabanca da cozinha', 'O projeto especifica <strong>pedra</strong> '
  'sobre toda a bancada. É fornecimento de marmoraria.'),
 ('Eletrodomésticos, louças e metais', 'Cooktop, forno, micro-ondas, '
  'lava-louças, geladeira, coifa, cuba e torneira. Prevemos o vão e a usinagem '
  '— precisamos das medidas de fábrica antes do corte.'),
 ('Elétrica e hidráulica', 'A iluminação embutida NA marcenaria é nossa; os '
  'pontos de energia, água e esgoto e os circuitos exclusivos dos '
  'eletrodomésticos são da obra.'),
 ('Alvenaria, gesso, revestimento e pintura', 'Inclusive o forro sobre o qual o '
  'painel, a cristaleira e os roupeiros são arrematados.'),
 ('Móveis soltos, cortinas e decoração', 'Cama, mesa de jantar, cadeiras, '
  'poltronas, tapetes e TV.'),
]

CSS = open('projetos/css-apresentacao.css', encoding='utf-8').read()
def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 16
def foot(n, r=False):
    return (f'<div class="foot{" r" if r else ""}">'
            f'<span>Valvic&nbsp;·&nbsp;{CLIENTE}</span><span>{n} / {NP}</span></div>')
def mvlist(mv):
    return ''.join(f'<div class="mv"><span class="b"></span><div>'
                   f'<span class="t">{t}</span> <span class="d">— {d}</span>'
                   f'</div></div>' for t, d in mv)

S = []

# 1 · capa
S.append(f"""<div class="slide dark"><div class="cv">
  <div class="cv-l">
    <div class="cv-brand">Valvic Marcenaria</div>
    <div style="margin-top:auto">
      <div class="eyebrow">Marcenaria planejada para</div>
      <div class="rule"></div>
      <div class="cv-nome">{CLIENTE}</div>
      <div class="cv-s">{OBRA} — sete conjuntos,<br>
      sobre o projeto executivo de {ARQ}</div>
    </div>
    <div class="cv-meta">
      <div><div class="k">Garantia Valvic</div><div class="v">10 anos</div></div>
      <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
      <div><div class="k">Data</div><div class="v">{DATA}</div></div>
      <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
    </div>
  </div>
  <div class="cv-r"><img src="{img('cozinha-2')}" style="object-position:56% 50%"></div>
</div></div>""")

# 2 · abertura — texto + planta
S.append(f"""<div class="slide"><div class="pad">
  <div style="display:grid;grid-template-columns:1.25fr 1fr;gap:14mm;flex:1;min-height:0">
    <div style="display:flex;flex-direction:column">
      <div class="eyebrow">A proposta</div>
      <div class="rule"></div>
      <h1 class="h1">Orçado sobre o projeto,<br>não sobre uma estimativa.</h1>
      <p class="lead" style="margin-top:4mm;max-width:none">O projeto de
      {ARQ} chegou detalhado peça a peça: cada prancha com quadro de peças,
      memorial de materiais, ferragens e acabamentos. Isso é raro, e muda o
      orçamento de natureza — o que está descrito nas páginas seguintes é
      <strong>o que será executado</strong>, e não uma aproximação a ajustar
      depois.</p>
      <p class="lead" style="margin-top:3.5mm;max-width:none">Os três princípios
      que a arquiteta declara no projeto — <strong>funcionalidade, estética e
      iluminação</strong> — são também os três lugares onde a marcenaria decide
      se um ambiente funciona. É por eles que cada conjunto é apresentado aqui:
      o que o móvel faz, como ele se resolve e onde a luz entra nele.</p>
      <div class="amb-nota" style="margin-top:auto">
        <div class="t">Sete conjuntos, nomeados um a um</div>
        <p>Cozinha · painel amadeirado · rack suspenso · cristaleira ·
        guarda-roupa da suíte · guarda-roupa em L · marcenaria sob a escada.</p>
      </div>
    </div>
    <div style="background:var(--cream);display:flex;padding:6mm">
      <img src="{img('planta')}" style="width:100%;height:auto;max-height:100%;
           object-fit:contain;margin:auto;mix-blend-mode:multiply">
    </div>
  </div>
  {foot(2)}
</div></div>""")

# 3 · escopo — o que está dentro, e o que os renders mostram e não está
lista = ''.join(
    f'<div class="mv"><span class="b"></span><div>'
    f'<span class="t">{a["n"]} &nbsp; {NOMES_INV[a["n"]]}</span></div></div>'
    for a in AMB)
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Escopo</div>
  <div class="rule"></div>
  <h2 class="h2" style="margin-bottom:5mm">O que esta proposta cobre.</h2>
  <div style="display:grid;grid-template-columns:1fr 1.2fr;gap:12mm;flex:1;
       min-height:0;margin-bottom:3mm">
    <div style="display:flex;flex-direction:column">
      <div>{lista}</div>
      <div class="amb-nota" style="margin-top:6mm;border-left-color:var(--mut)">
        <div class="t" style="color:var(--mut)">E o que ainda não</div>
        <p>As imagens desta apresentação são do projeto da arquiteta e mostram
        <strong>o apartamento inteiro</strong>. Aparecem nelas móveis que ainda
        <strong>não têm prancha executiva</strong> — os dois banheiros, o quarto
        com sofá, a bancada com espelho e a copa. Eles <strong>não estão neste
        valor</strong>, e a página 15 lista cada um. Assim que as pranchas
        chegarem, orçamos à parte.</p>
      </div>
    </div>
    <div class="mos" style="grid-template-columns:1fr 1fr;grid-auto-rows:1fr">
      <figure><img src="{img('copa-2')}" style="object-position:48% 50%">
        <figcaption>Cozinha</figcaption></figure>
      <figure><img src="{img('estar')}" style="object-position:30% 50%">
        <figcaption>Painel e rack</figcaption></figure>
      <figure><img src="{img('quarto-2')}" style="object-position:61% 50%">
        <figcaption>Guarda-roupa em L</figcaption></figure>
      <figure><img src="{img('escada')}" style="object-position:35% 50%">
        <figcaption>Sob a escada</figcaption></figure>
    </div>
  </div>
  {foot(3)}
</div></div>""")

# 4 a 10 · um conjunto por página
for k, a in enumerate(AMB):
    pg = 4 + k
    if a['w'] is True:                       # faixa de largura total
        S.append(f"""<div class="slide"><div class="ambw">
          <div class="band"><img src="{img(a['foto'])}"
               style="object-position:{a['pos']}">
            <div class="tag">{a['tag']}</div></div>
          <div class="low">
            <div>
              <div style="display:flex;align-items:baseline;gap:4mm">
                <div class="amb-n">{a['n']}</div>
                <h2 class="h2">{a['nome']}</h2></div>
              <div class="eyebrow" style="margin:2mm 0 2mm">Móveis contemplados</div>
              {mvlist(a['mv'])}
            </div>
            <div class="amb-nota" style="margin-top:0;align-self:start">
              <div class="t">{a['nota'][0]}</div><p>{a['nota'][1]}</p></div>
          </div>
        </div>{foot(pg)}</div>""")
    else:
        fit = ' fit' if a['w'] == 'fit' else ''
        sty = '' if fit else f' style="object-position:{a["pos"]}"'
        S.append(f"""<div class="slide"><div class="amb">
          <div class="amb-img{fit}"><img src="{img(a['foto'])}"{sty}>
            <div class="tag">{a['tag']}</div></div>
          <div class="amb-txt">
            <div class="amb-n">{a['n']}</div>
            <div class="eyebrow" style="margin-top:2mm">Móveis contemplados</div>
            <h2 class="h2" style="margin:1mm 0 4mm">{a['nome']}</h2>
            <div>{mvlist(a['mv'])}</div>
            <div class="amb-nota" style="margin-top:auto"><div class="t">{a['nota'][0]}</div>
              <p>{a['nota'][1]}</p></div>
          </div>
        </div>{foot(pg, r=True)}</div>""")

# 11 · frentes coordenadas
cards = ''.join(f'<div class="c"><div class="n">{n}</div>'
                f'<div class="t">{t}</div><div class="d">{d}</div></div>'
                for n, t, d in FRENTES)
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Coordenação</div>
  <div class="rule"></div>
  <h1 class="h1">Seis frentes, um interlocutor,<br>uma data de entrega.</h1>
  <p class="lead" style="margin-top:3.5mm">Vidraceiro, espelheiro, serralheiro e
  aluminista têm cada um o seu prazo, a sua medida e a sua sequência — e todos
  dependem de a marcenaria estar pronta na hora certa. Vidro se mede depois do
  móvel montado; espelho, depois do vidro; a barra do rack, antes de o painel
  subir. <strong>A Valvic contrata, mede, agenda e responde por todas.</strong>
  A cliente trata com uma empresa; a obra recebe uma equipe.</p>
  <div class="fr" style="grid-template-columns:repeat(3,1fr)">{cards}</div>
  <div class="mos" style="grid-template-columns:repeat(4,1fr);flex:none;
       height:18mm;margin-top:auto;margin-bottom:3mm">
    <figure><img src="{img('cozinha-1')}" style="object-position:47% 42%"></figure>
    <figure><img src="{img('escada')}" style="object-position:42% 55%"></figure>
    <figure><img src="{img('cozinha-2')}" style="object-position:88% 45%"></figure>
    <figure><img src="{img('estar')}" style="object-position:30% 55%"></figure>
  </div>
  {foot(11)}
</div></div>""")

# 12 · garantia
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Garantia</div>
  <div class="rule"></div>
  <h1 class="h1">Dez anos. E é a nossa<br>assinatura embaixo.</h1>
  <div style="display:grid;grid-template-columns:1.05fr 1fr;gap:12mm;flex:1;
       min-height:0;margin:5mm 0 7mm;grid-template-rows:minmax(0,1fr)">
    <div style="display:flex;flex-direction:column">
      <p class="lead" style="max-width:none">Ferragem não se escolhe por marca:
      se escolhe por <strong>ciclo de abertura</strong>. Uma gaveta de cozinha
      abre e fecha algumas dezenas de milhares de vezes numa década, e uma
      báscula de rack carrega a frente inteira em dois pontos. É aí que a linha
      superior se paga.</p>
      <p class="lead" style="margin-top:3.5mm;max-width:none">Neste projeto são
      <strong>46 dobradiças, 13 gavetas e 4 básculas</strong> — e todas na linha
      superior, sem degrau intermediário. Não há neste orçamento uma versão
      "econômica" de ferragem: só existe uma, e é esta.</p>
      <div class="amb-nota" style="margin-top:6mm">
        <div class="t">Garantia Valvic, não do fabricante</div>
        <p>Os dez anos são nossos — escritos e assinados na entrega, cobrindo
        <strong>estrutura, ferragem e acabamento</strong>. Garantia de fabricante
        de ferragem cobre a ferragem e manda você procurar o fabricante. Esta
        cobre o móvel e manda você nos procurar.</p></div>
      <div class="amb-nota" style="margin-top:4mm">
        <div class="t">Quem produz é quem monta</div>
        <p>Instalação e montagem por <strong>equipe própria da Valvic</strong>,
        dentro deste valor. A mesma empresa que cortou a peça é a que a instala
        e a que responde pela garantia.</p></div>
    </div>
    <div class="gar" style="grid-template-columns:1fr;margin-top:0">
      <div class="c hi" style="position:relative;padding:5mm 5.5mm">
        <div class="selo">Linha única</div>
        <div class="anos" style="font-size:48pt">10</div>
        <div class="unid">anos de garantia</div>
        <div class="nm">Hettich em todo o projeto</div>
        <div class="x">Curso mais longo, carga maior, retorno mais macio e
        ciclo de teste muito acima do uso doméstico. Nas oito gavetas do
        guarda-roupa da suíte e nas quatro básculas do rack, é o que separa um
        móvel que abre bem no primeiro ano de um que abre bem no décimo.</div>
        <div class="x" style="margin-top:4mm">A dobradiça Novisys regula nos
        três eixos — altura, profundidade e inclinação. Porta que sai do prumo
        com o assentamento da casa volta ao esquadro com uma chave de fenda,
        sem desmontar nada e sem furo novo.</div>
        <div class="l">
          <div class="k">Dobradiça</div><div class="v">Hettich Novisys, com amortecimento</div>
          <div class="k">Corrediça</div><div class="v">Hettich Quadro, oculta</div>
          <div class="k">Báscula</div><div class="v">Articulador Blum HK-xs</div>
          <div class="k">Correr</div><div class="v">Roldana regulável, antidescarrilamento</div>
        </div>
      </div>
    </div>
  </div>
  {foot(12)}
</div></div>""")

# 13 · upgrade — tudo na cor
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Upgrade de projeto</div>
  <div class="rule"></div>
  <h1 class="h1">O interior na mesma cor<br>da estrutura externa.</h1>
  <div style="display:grid;grid-template-columns:1.1fr 1fr;gap:12mm;margin-top:5mm">
    <div>
      <p class="lead" style="max-width:none">O projeto especifica o interior dos
      armários em <strong>branco</strong> — fora na cor, dentro em branco. É o
      padrão do mercado, e é o que está no valor de {brl(INV)}.</p>
      <p class="lead" style="margin-top:3.5mm;max-width:none">O upgrade troca
      esse interior pela <strong>mesma cor da frente</strong>, e é
      <strong>integral</strong>: caixaria, prateleiras, fundos e a caixa de cada
      gaveta. <strong>Nenhuma peça branca fica no projeto.</strong></p>
      <div class="fr" style="grid-template-columns:1fr 1fr;margin-top:6mm">
        <div class="c"><div class="n">—</div>
          <div class="t">Como o projeto especifica</div>
          <div class="d" style="font-size:11pt;color:var(--mut);margin-top:2mm">
          R$ {brl(INV)}</div></div>
        <div class="c" style="border-color:var(--gold)"><div class="n">+</div>
          <div class="t">Com o upgrade · tudo na cor</div>
          <div class="d" style="font-size:11pt;color:var(--ink);font-weight:700;
               margin-top:2mm">R$ {brl(INV_UP)}</div></div>
      </div>
    </div>
    <div>
      <div class="amb-nota" style="margin-top:0">
        <div class="t">O que muda no dia a dia</div>
        <p><strong>Abrir a porta deixa de mostrar branco.</strong> O móvel fica
        inteiro na mesma cor, e o interior passa a fazer parte do desenho em vez
        de contrastar com ele.</p></div>
      <div class="amb-nota" style="margin-top:4mm">
        <div class="t">E o que não muda</div>
        <p>Nada além disso. <strong>Mesmo escopo, mesma ferragem Hettich, mesma
        garantia de dez anos e o mesmo prazo de entrega.</strong> O upgrade é
        uma decisão de acabamento, e pode ser tomada até a aprovação do projeto
        executivo — depois do corte, não.</p></div>
      <div class="amb-nota" style="margin-top:4mm">
        <div class="t">E envelhece melhor</div>
        <p>Marca de uso, poeira e risco de manuseio aparecem muito menos em
        superfície colorida do que em branca. Num armário que abre e fecha todo
        dia por dez anos, o interior na cor é também uma decisão de
        manutenção.</p></div>
    </div>
  </div>
  <div class="eyebrow" style="margin-top:auto">Os três lugares onde o interior fica à vista</div>
  <div class="rule"></div>
  <div class="mos" style="grid-template-columns:repeat(3,1fr);flex:none;
       height:30mm;margin:2mm 0 3mm">
    <figure><img src="{img('cozinha-1')}" style="object-position:47% 38%">
      <figcaption>Atrás do vidro da cristaleira</figcaption></figure>
    <figure><img src="{img('escada')}" style="object-position:42% 62%">
      <figcaption>Nos nichos sob a escada</figcaption></figure>
    <figure><img src="{img('quarto-2')}" style="object-position:72% 32%">
      <figcaption>No nicho da cabeceira</figcaption></figure>
  </div>
  {foot(13)}
</div></div>""")

# 14 · investimento
linhas = ''.join(f'<tr><td class="l">{n} &nbsp; {NOMES_INV[n]}</td>'
                 f'<td class="hi">{brl(PRECO[n])}</td></tr>'
                 for n in sorted(PRECO))
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h2" style="margin-bottom:4mm">Conjunto a conjunto.</h2>
  <div style="display:grid;grid-template-columns:1.3fr 1fr;gap:12mm;flex:1;min-height:0">
    <div>
      <table class="inv">
        <tr><th class="l">Conjunto</th><th class="hi">Investimento</th></tr>
        {linhas}
        <tr class="tot"><td class="l">Investimento total</td>
          <td class="hi">{brl(INV)}</td></tr>
        <tr><td class="l" style="padding-top:3mm;color:var(--gold);font-weight:600">
          + Upgrade · tudo na cor</td>
          <td class="hi" style="padding-top:3mm">{brl(UP)}</td></tr>
        <tr class="tot"><td class="l">Com o upgrade</td>
          <td class="hi">{brl(INV_UP)}</td></tr>
      </table>
    </div>
    <div style="display:flex;flex-direction:column">
      <div class="box" style="margin-top:0"><div class="t">O que está dentro do valor</div>
      <p>Projeto executivo de marcenaria, fornecimento de material, produção em
      máquina própria, <strong>e as seis frentes coordenadas</strong> — espelhos
      com película, portas e prateleiras de vidro temperado, porta Reflecta,
      barra metálica do rack, cabideiros, perfis e sistema de correr, e
      iluminação em LED com driver. Mais transporte, entrega na obra e
      <strong>instalação e montagem por equipe própria da Valvic</strong>.</p></div>
      <div class="box"><div class="t">Coordenação de projeto</div>
      <p>O acompanhamento do projeto executivo está contemplado no valor, com e
      sem o upgrade.</p></div>
      <div class="box" style="border-left-color:var(--mut)">
      <div class="t" style="color:var(--mut)">O escopo dos sete conjuntos</div>
      <p>Este valor cobre <strong>os sete conjuntos nomeados acima</strong>. Os
      demais móveis que aparecem nos renders estão listados na página seguinte,
      e serão orçados quando as pranchas forem emitidas.</p></div>
    </div>
  </div>
  {foot(14)}
</div></div>""")

# 15 · condições e fronteiras
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <h2 class="h2" style="margin-bottom:2mm">Prazo, pagamento e fronteiras.</h2>
  <div class="three">
    <div>
      <div class="term"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da aprovação e da medição em obra.</div></div>
      <div class="term"><div class="k">Conferência de medidas</div>
        <div class="v">Visita técnica antes do corte</div>
        <div class="s">As próprias pranchas marcam "conferir em obra" na cota
        vertical do rack, na inclinação da escada e nos modelos dos
        eletrodomésticos. Nada vai para a CNC antes da nossa medição.</div></div>
      <div class="term"><div class="k">Validade da proposta</div>
        <div class="v">{VALIDADE}</div></div>
      <div class="term"><div class="k">Garantia</div>
        <div class="v">10 anos, Valvic</div>
        <div class="s">Escrita e assinada na entrega, cobrindo estrutura,
        ferragem e acabamento.</div></div>
    </div>
    <div>
      <table class="pay">
        <tr><td colspan="2" style="border:none;padding-bottom:1.4mm">
          <span class="eyebrow">Formas de pagamento</span></td></tr>
        {''.join(f'<tr><td>{c}</td><td class="d">{d}</td></tr>' for c, d in PAGTO)}
      </table>
      <p style="color:var(--mut);font-size:7.6pt;margin-top:2.5mm">
      O desconto por transferência devolve à cliente a taxa de máquina que
      deixamos de pagar.</p>
      <div class="box"><div class="t">Produção e montagem</div>
      <p>Corte, usinagem e laminação de borda em <strong>máquina própria</strong>;
      instalação e montagem por <strong>equipe própria</strong>. Não
      terceirizamos nem o que define o acabamento, nem quem entrega.</p></div>
    </div>
    <div class="fora">
      <div class="eyebrow">Não incluso nesta proposta</div>
      <div class="rule"></div>
      <ul>{''.join(f'<li><div class="k">{k}</div><div class="v">{v}</div></li>'
                   for k, v in FORA)}</ul>
    </div>
  </div>
  {foot(15)}
</div></div>""")

# 16 · especificação técnica
esp = ''.join(f'<div class="term"><div class="k">{k}</div>'
              f'<div class="s" style="font-size:8.4pt;margin-top:1mm">{v}</div></div>'
              for k, v in ESPEC)
S.append(f"""<div class="slide"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="rule"></div>
  <h2 class="h2" style="margin-bottom:3mm">O que atravessa<br>o projeto inteiro.</h2>
  <p class="lead">As oito linhas abaixo valem para os sete conjuntos, e são o
  que sustenta a garantia de dez anos.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 12mm;margin-top:5mm">{esp}</div>
  <div class="mos" style="grid-template-columns:repeat(4,1fr);flex:none;
       height:26mm;margin-top:7mm">
    <figure><img src="{img('copa-2')}" style="object-position:48% 50%"></figure>
    <figure><img src="{img('estar')}" style="object-position:30% 50%"></figure>
    <figure><img src="{img('quarto-2')}" style="object-position:61% 50%"></figure>
    <figure><img src="{img('escada')}" style="object-position:35% 50%"></figure>
  </div>
  <div class="sig">
    <div class="ln">Valvic Marcenaria</div>
    <div class="ln">{CLIENTE}</div>
  </div>
  {foot(16)}
</div></div>""")

assert len(S) == NP, (len(S), NP)

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>{"".join(S)}</body></html>')

OUT_H = 'projetos/apresentacao-carla.html'
OUT_P = 'projetos/apresentacao-carla.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML)
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r2.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}  ({os.path.getsize(OUT_P)//1024} KB)')
print(f'R$ {brl(INV)}  ·  com upgrade R$ {brl(INV_UP)}')
