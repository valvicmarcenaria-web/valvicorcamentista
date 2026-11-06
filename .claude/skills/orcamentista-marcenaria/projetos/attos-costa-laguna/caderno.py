# -*- coding: utf-8 -*-
"""⭐⭐ O CADERNO DO ATTOS — a proposta, em A4 paisagem, pronta para PDF.

⛔⛔ A REGRA QUE DÁ SENTIDO A ESTE ARQUIVO: **a proposta LÊ o motor, não
  copia dele.** Todo valor impresso aqui sai de `linhas.monta()` no momento
  da geração. Se o preço mudar, o caderno muda junto — e não existe o caso
  de a planilha dizer um número e a folha do cliente dizer outro, que é o
  jeito mais caro de errar que esta casa conhece.

⛔ O QUE NÃO ATRAVESSA ESTA PORTA: custo, MC, alerta de caixa, dúvida
  interna, plano de corte. A proposta é a camada do cliente. O que ela
  mostra é escopo, versão, investimento, condição, prazo e garantia.

⭐ A IDENTIDADE É COMPARTILHADA: `../css-caderno.css` e `../js-caderno.js`
  são da casa, não deste cliente. Nenhum nome de cliente mora neles.
"""
import base64, importlib.util, contextlib, io, pathlib, re, sys, subprocess

AQUI = pathlib.Path(__file__).resolve().parent
CASA = AQUI.parent


def _mod(nome, arq):
    s = importlib.util.spec_from_file_location(nome, arq)
    m = importlib.util.module_from_spec(s)
    sys.modules[nome] = m
    with contextlib.redirect_stdout(io.StringIO()):
        s.loader.exec_module(m)
    return m


ln = _mod('ln', AQUI / 'linhas.py')
b = ln.b

# ── quem é o cliente ────────────────────────────────────────────────────
#   ⚠ [04/11/2026] NÃO EXISTE nome de cliente registrado neste projeto: o
#     executivo é assinado pela ATTOS e a pasta do Drive só diz "Costa
#     Laguna". ⛔ A regra do QA do closer é não inventar nome — então a capa
#     identifica o PROJETO, e CLIENTE fica vazio até o Jonathan dizer.
#     Preencher aqui e rodar de novo basta: o nome entra na capa, no rodapé
#     de todas as folhas e na linha de assinatura.
CLIENTE = ''
PROJETO = 'Costa Laguna'
ARQUITETURA = 'ATTOS · executivo Rev. 03'
DATA = 'Novembro de 2026'
VALIDADE = '7 dias úteis'

# ── o prazo ─────────────────────────────────────────────────────────────
#   ⭐ [Jonathan, 04/11/2026] "prazo de entrega 70 dias corridos pos medição
#     com entrega do escritorio ate 10 de dezembro".
#   ⛔ Prazo é o único número da proposta que a Lavinia não calcula: depende
#     da produção, e a regra da casa é nunca cravá-lo sem o dono.
PRAZO = '70 dias corridos'
PRAZO_DE = 'Contados da medição técnica no local, não da assinatura.'
ENTREGA_ANTECIPADA = ('Escritório', '10 de dezembro de 2026')

GARANTIA = {'Básica': ('1', 'ano'), 'Hettich': ('10', 'anos'), 'Blum': ('30', 'anos')}
#   ⚠ [Jonathan, 04/11/2026] "colocar a garantia da linha basica em 1 ano".
#     A tabela da casa põe a telescópica em 2 anos; nesta proposta vai 1.

ORDEM = ['Básica', 'Hettich', 'Blum']
ROTULO = {'Básica': 'Telescópica', 'Hettich': 'Hettich', 'Blum': 'Blum'}


def brl(v, centavos=True):
    s = f'{v:,.2f}' if centavos else f'{v:,.0f}'
    return 'R$ ' + s.replace(',', '§').replace('.', ',').replace('§', '.')


def capa_do_ripado():
    """⭐ A CAPA DE DESENHO — guardada, e não é mais a que vai.

    ⚠ [Jonathan, 05/11/2026] chegou o anteprojeto 3D e a capa passou a ser
      o render da suíte principal. Esta função fica porque a lição dela não
      envelhece, e porque um caderno sem render volta a precisar dela.

    ⭐ A CAPA PEDE CAMPO, NÃO FOLHA DE DESENHO.

    ⛔ A elevação inteira na capa entrega o título e a cota pela metade —
      'RIPADO 1:25' cortado no pé e um 'CORRE' solto no meio. ⭐ O que
      funciona ali é só o CAMPO de ripas: vira textura, e textura não tem
      metade errada.
    ⛔⛔ E O CAMPO LIMPO É ESTREITO. As duas portas de correr ficam entre
      20,7% e 34,6% da elevação, e cada uma leva a seta e a palavra CORRE.
      Sobra o trecho de 129,5 cm antes da primeira: 20% da folha.
    ⭐ Por isso ela não é RECORTE DO PNG, é RENDER NOVO da prancha, a 400
      dpi. Ampliar 390 px para treze centímetros de capa borraria a ripa —
      e ripa borrada é exatamente o defeito que esta proposta promete não
      ter."""
    alvo = AQUI / 'img' / 'capa-ripado.png'
    fonte = AQUI / 'pr' / 'cozinha-painel-02.pdf'
    if alvo.exists() and alvo.stat().st_mtime >= fonte.stat().st_mtime:
        return 'capa-ripado'
    import pymupdf
    des = _mod('des', AQUI / 'desenhos.py')
    d = pymupdf.open(fonte)
    pg = d[0]
    vis = des.vistas(pg)
    elev = max(vis, key=lambda r: r.get_area())      # a elevação é a maior
    r = pymupdf.Rect(elev.x0 + elev.width * .02, elev.y0 + elev.height * .10,
                     elev.x0 + elev.width * .20, elev.y0 + elev.height * .88)
    pg.get_pixmap(clip=r, dpi=400, alpha=False).save(str(alvo))
    d.close()
    return 'capa-ripado'


def b64(nome):
    """⭐ PNG para desenho, JPEG para render — e o nome não diz qual.
    O traço vetorial em JPEG ganha chuvisco em volta da linha; o render em
    PNG pesa cinco vezes mais sem ganhar nada. Cada um no seu formato, e a
    folha não precisa saber."""
    f = AQUI / 'img' / (nome + '.png')
    if not f.exists():
        f = AQUI / 'img' / (nome + '.jpg')
    tipo = 'png' if f.suffix == '.png' else 'jpeg'
    return f'data:image/{tipo};base64,' + base64.b64encode(f.read_bytes()).decode()


def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


# ════════════════════════════════════════════════════════════════════════
S = ln.monta()
TOTAL = {k: sum(d[k + '_pv'] for d in S) for k in ORDEM}
N_ITENS = len(S)
N_AMB = len({d['amb'] for d in S})

PAGINAS = []


def folha(html, escura=False, rodape=True):
    PAGINAS.append((html, escura, rodape))


# ═══ 01 · CAPA ══════════════════════════════════════════════════════════
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">O ripado<br>que atravessa<br>a casa.</div>
  <div class="cv-s">Oito ambientes do executivo,<br>
     do primeiro desenho ao dia da instalação.</div>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">{PROJETO}</div></div>
   <div><div class="k">Executivo</div><div class="v">{ARQUITETURA}</div></div>
   <div><div class="k">Escopo</div><div class="v">{N_AMB} ambientes · {N_ITENS} itens</div></div>
   <div><div class="k">Data</div><div class="v">{DATA}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{b64('r-suite-cabeceira')}" alt=""></div>
</div>''', escura=True, rodape=False)

# ═══ 02 · O QUE ESTA CASA PEDE ══════════════════════════════════════════
folha(f'''<div class="ambw">
 <div class="band solo"><img class="r" src="{b64('r-sala-tv-amb')}" alt="">
   <div class="tag">Sala de estar · render do anteprojeto</div></div>
 <div class="low"><div class="fitw">
   <div class="eyebrow">O projeto</div><div class="rule"></div>
   <div class="h2">O que esta casa pede.</div>
   <div class="lead" style="margin:3mm 0 4mm;max-width:none">Esta não é uma
     casa de armário. É uma casa de <b>painel</b> — e painel é a peça que não
     perdoa: ela é grande, é contínua, fica à altura dos olhos e qualquer
     desaprumo aparece de uma ponta à outra.</div>
   <div class="mv"><span class="b"></span><span><span class="t">Vinte e quatro metros quadrados de ripado</span>
     <span class="d"> — 626 cm no corredor da cozinha, 353,5 na sala, 316 no
     escritório e 200 na cabeceira da suíte. Ripa de 2 cm com vão de 1, passo
     de 3: mais de seiscentas ripas, todas fitadas.</span></span></div>
   <div class="mv"><span class="b"></span><span><span class="t">Duas portas que somem dentro do painel</span>
     <span class="d"> — vestiário e despensa, 87 cm cada, ripadas na mesma
     cadência da parede. Fechadas, não existem; é o alinhamento da ripa que
     entrega, ou não, o trabalho.</span></span></div>
   <div class="mv"><span class="b"></span><span><span class="t">Duas cabeceiras estofadas</span>
     <span class="d"> — 240 cm na suíte principal e 192 na suíte 01, em MDF,
     espuma e revestimento, com as mesas sobre pé metálico.</span></span></div>
   <div class="mv"><span class="b"></span><span><span class="t">Vidro reflecta cristal</span>
     <span class="d"> — na cristaleira de 147 × 275 e nas portas dos armários
     da cozinha e do gourmet. O vidro é nosso: sai no mesmo contrato.</span></span></div>
  </div>
  <div><div class="amb-nota"><div class="t">Sobre as imagens deste caderno</div>
    <p>As perspectivas são <b>do anteprojeto da arquitetura</b> e mostram a
      casa inteira — mobiliário solto, pedra, eletrodomésticos e decoração
      aparecem nelas e <b>não estão nesta proposta</b>. Ao lado de cada
      render vai a <b>elevação cotada do executivo</b>: é ela que diz,
      milímetro a milímetro, o que sai da nossa fábrica.</p></div></div>
 </div>
</div>''')

# ═══ 03 · A EMPRESA ═════════════════════════════════════════════════════
folha(f'''<div class="pad">
  <div class="eyebrow">A empresa e a infraestrutura</div><div class="rule"></div>
  <div class="h1">A Valvic responde pelo conjunto.</div>
  <div class="lead" style="margin-top:4mm">Um painel ripado de seis metros não
    se perde na marcenaria. Ele se perde na costura entre os ofícios — o vidro
    que chega com a cota de antes, o metal que atrasa, o estofado que aparece
    depois da instalação —, e alguém tem de decidir quem espera quem. Aqui não
    há essa costura para fazer: o que esta proposta reúne entra no mesmo
    escopo, no mesmo contrato e na mesma data.</div>
  <div class="fr">
   <div class="c"><div class="n">01</div><div class="t">A casa pede mais que marcenaria.</div>
     <div class="d">O executivo pede <b>vidro reflecta cristal</b>, <b>estofado</b>
       nas duas cabeceiras, <b>pé metálico</b> nas mesas e perfil de <b>LED</b>
       embutido na peça — e nada disso é marcenaria. Entra tudo no nosso escopo
       e sai no mesmo contrato: uma especificação, uma medição, uma data.
       O que fica fora vem nomeado.</div></div>
   <div class="c"><div class="n">02</div><div class="t">A peça sai daqui conferida.</div>
     <div class="d">Usinagem, montagem e conferência acontecem dentro da nossa
       fábrica. Cada módulo é montado aqui antes de ser embalado: porta
       regulada, gaveta corrida, ripa alinhada, vidro posto. O que chega na
       obra chega para ser instalado, não para ser resolvido.</div></div>
   <div class="c"><div class="n">03</div><div class="t">Uma arquiteta responsável.</div>
     <div class="d">Do orçamento aprovado à entrega, o projeto tem uma arquiteta
       nossa como responsável. Ela lê o executivo prancha por prancha, está na
       medição no local e segue as peças pela fábrica. Vocês explicam o projeto
       uma vez, a uma pessoa — e é essa pessoa que responde quando é chamada.</div></div>
   <div class="c"><div class="n">04</div><div class="t">O executivo de marcenaria é nosso.</div>
     <div class="d">Antes de cortar, a Valvic desenha. As folhas deste caderno
       trazem o executivo de interiores; o nosso executivo de marcenaria diz
       <b>como</b> cada peça se constrói — onde cai a emenda do painel, por
       onde passa a fiação, qual a folga de instalação. É nele que a
       divergência aparece no papel, antes de virar retrabalho.</div></div>
  </div>
</div>''')


# ═══ 04 · O PROCESSO ════════════════════════════════════════════════════
ETAPAS = [
 ('Partida', 'da decisão ao contrato', [
   ('01', 'Decisão', 'Aprovação', 'Escopo, acabamentos e ferragens definidos. Nada entra em produção sem essa decisão.', 'Escopo fechado, ambiente por ambiente.'),
   ('02', 'Registro', 'Contrato', 'Contrato assinado, prazos e responsabilidades registrados. Tudo o que foi dito fica escrito.', 'Contrato e cronograma com datas.')]),
 ('Engenharia', 'da obra ao arquivo de máquina', [
   ('03', 'Parede', 'Medição técnica', 'Nossa equipe mede a obra no local. É daqui que o prazo passa a contar.', 'Medidas da obra construída, não do desenho.'),
   ('04', 'Desenho', 'Detalhamento', 'Fechamos com vocês e com a arquitetura cada decisão de execução antes de cortar nada.', 'Nenhuma decisão de execução em aberto.'),
   ('05', 'Arquivo', 'Programação', 'O detalhamento vira arquivo de máquina. O erro é corrigido na tela, não na chapa.', 'Plano de corte e usinagem programado.')]),
 ('Fábrica', 'onde o móvel nasce e é testado', [
   ('06', 'Corte', 'Usinagem', 'Corte, furação, fresa e acabamento de borda. Tudo dentro da nossa fábrica.', 'Peças prontas e identificadas, uma por uma.'),
   ('07', 'Encaixe', 'Montagem em fábrica', 'O móvel é montado aqui antes de ir para a obra. Problema de encaixe morre aqui.', 'Móvel montado e testado antes de sair.'),
   ('08', 'Checklist', 'Conferência', 'Peça por peça contra o projeto: medida, cor, ferragem, sentido de abertura, luz.', 'Checklist assinado antes do carregamento.')]),
 ('Entrega', 'da nossa fábrica à sua casa', [
   ('09', 'Carga', 'Transporte', 'Embalagem, carregamento e transporte são nossos. O móvel não troca de mão no caminho.', 'Carregado por quem o montou.'),
   ('10', 'Prumo', 'Instalação', 'Equipe própria instala, nivela e regula. A obra recebe móvel pronto, não peça solta.', 'Móveis no lugar, nivelados e regulados.'),
   ('11', 'Teste', 'Vistoria técnica', 'Com vocês, abrimos tudo: cada porta, cada gaveta, cada luz. Nada passa sem testar.', 'Ajustes finais na frente de vocês.'),
   ('12', 'Casa', 'Entrega final', 'Ambiente limpo, móvel em uso e termo de garantia na mão de vocês.', 'Termo de garantia emitido e assinado.')]),
]
_bl = ''
for _h, _s, _es in ETAPAS:
    _bl += f'<div class="pb"><div class="pb-h">{_h}</div><div class="pb-s">{_s}</div>'
    for _n, _k, _t, _l, _e in _es:
        _bl += (f'<div class="pe"><div class="pe-n">{_n}</div><div class="pe-k">{_k}</div>'
                f'<div class="pe-t">{_t}</div><div class="pe-l">{_l}</div>'
                f'<div class="pe-e">{_e}</div></div>')
    _bl += '</div>'
folha(f'''<div class="pad">
  <div class="eyebrow">O caminho do seu projeto</div><div class="rule"></div>
  <div class="h1">Doze etapas, <span style="color:var(--gold)">um só responsável</span>.</div>
  <div class="lead" style="margin:3mm 0 5mm">Da decisão de vocês até a casa
    pronta são doze etapas — e nenhuma delas muda de dono.</div>
  <div class="rail"></div>
  <div class="proc">{_bl}</div>
</div>''')

# ═══ 05 · OS AMBIENTES ══════════════════════════════════════════════════
AMB_ORD = ['Cozinha', 'Gourmet', 'Escritório', 'Sala de TV', 'Suíte',
           'Suíte 01', 'Hall', 'Jantar']
AMB_DESC = {
 'Cozinha': 'Painel ripado do corredor com as duas portas de correr, cristaleira, armário superior e coluna',
 'Gourmet': 'Armário complementar com portas de vidro reflecta',
 'Escritório': 'Painel ripado de fundo, armário superior, bancada e armário inferior',
 'Sala de TV': 'Painel ripado, painel liso e rack suspenso de quatro gavetões',
 'Suíte': 'Parede painelada da TV, painel da cabeceira, cabeceira estofada e mesas de cabeceira',
 'Suíte 01': 'Cabeceira estofada',
 'Hall': 'Painel do hall com a porta da lavanderia mimetizada',
 'Jantar': 'Aparador suspenso de três portas',
}
_ix = ''
for _i, _a in enumerate(AMB_ORD, 1):
    _n = len([d for d in S if d['amb'] == _a])
    _ix += (f'<div class="ix"><div class="ix-n">{_i:02d}</div>'
            f'<div class="ix-t">{_a}</div>'
            f'<div class="ix-d">{AMB_DESC[_a]}</div></div>')
folha(f'''<div class="pad">
  <div class="eyebrow">Os ambientes</div><div class="rule"></div>
  <div class="h1">Oito ambientes, dezoito itens.</div>
  <div class="lead" style="margin:3mm 0 5mm">O escopo desta proposta, ambiente
    por ambiente, exatamente como ele aparece na folha de investimento.</div>
  {_ix}
</div>''')


# ═══ 06 a 12 · OS AMBIENTES, UM A UM ════════════════════════════════════
#   ⛔ A IMAGEM AQUI É DESENHO, NÃO FOTO. `object-fit:cover` recortaria a
#     elevação pela metade — e meia elevação não é imagem, é erro. Tudo
#     contido, sobre o campo areia, com respiro.
SUPLEMENTO = '''
.ambw .band{display:flex;gap:3mm;padding:5mm 6mm;background:var(--sand)}
.ambw .band img{object-fit:contain;height:100%;width:auto;flex:1;min-width:0;
                background:#fff;padding:3mm;box-shadow:0 1mm 4mm rgba(26,23,20,.10)}
.amb-img.fit img{max-width:92%;max-height:86%;background:#fff;padding:4mm}
.ambw .band .tag{z-index:2}
/* ⭐ quando a faixa tem RENDER e ELEVAÇÃO lado a lado, o render puxa mais
   largura: é ele que vende, e o desenho ao lado é que prova. */
.ambw .band img.r{flex:1.55}
.ambw .band img.d{flex:1}
/* ⛔ FAIXA DE UMA IMAGEM SÓ: contida, um render 16:9 fica ilhado no meio de
   doze centímetros de areia de cada lado — parece engano de montagem. Foto
   pode ser cortada; desenho, não. Então a faixa solo de RENDER sangra. */
.ambw .band.solo{padding:0;gap:0}
.ambw .band.solo img.r{object-fit:cover;width:100%;height:100%;padding:0;
                       box-shadow:none}
/* ⛔ O ALGARISMO DA GARANTIA. A Cormorant Garamond vem com algarismo de
   TEXTO: o "1" sai da altura de x e lê como "I" maiúsculo, o "10" como
   "IO". Numa folha onde o número é a promessa, isso não é estilo, é
   ambiguidade — e o "1 ano" desta proposta é justamente o que mais sofre. */
.gar .anos{font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1,'onum' 0}
/* a folha de investimento tem dezenove linhas: a calha aperta para o
   rodapé não subir por cima do total */
.inv td{padding:1.55mm 0}
'''

#   ⭐ E UM PASSE A MAIS DE AJUSTE, só deste caderno: o script da casa
#     encolhe a folha apertada até o piso de .80, e a tabela de dezenove
#     linhas pedia mais que isso — o rodapé entrava por cima da linha do
#     total. Aqui o piso é .60, e quem cede é a folha, nunca o rodapé.
POS_AJUSTE = '''
document.querySelectorAll('.pad.apertada').forEach(c => {
  const f = c.querySelector('.fitp'); if (!f) return;
  f.style.zoom = 1;
  const cs = getComputedStyle(c);
  const alt = c.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
  const pede = f.scrollHeight;
  if (pede > alt) f.style.zoom = Math.max(.60, (alt / pede) - .012);
});
/* ⛔ E A FOLHA DE AMBIENTE TAMBÉM. O script da casa faz a FAIXA ceder até
   62 mm para a lista caber — mas quando a faixa é render sangrado ela não
   deve encolher, senão a foto vira tira. Aqui quem cede é o texto. */
document.querySelectorAll('.ambw .low').forEach(low => {
  const f = low.querySelector('.fitw'); if (!f) return;
  const cs = getComputedStyle(low);
  const alt = low.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
  const pede = f.scrollHeight;
  if (pede > alt) f.style.zoom = Math.max(.70, (alt / pede) - .02);
});
'''

AMBIENTES = [
 dict(img=['r-cozinha-corredor', 'ripado-corredor'],
      tag='Cozinha · o corredor no render do anteprojeto e na elevação do executivo',
      eyebrow='Cozinha · o corredor', h2='Seis metros de ripado, e duas portas dentro dele.',
      lead='A parede inteira do corredor de serviço vira uma só peça — e as '
           'portas do vestiário e da despensa desaparecem nela.',
      mv=[('Painel ripado do corredor, 626 × 272',
           'Ripa de 2 cm com vão de 1, passo de 3 — <b>209 ripas de 2,72 m</b>, '
           'todas fitadas, sobre base contínua de MDF. A emenda da base cai '
           'atrás de uma ripa e não se vê.'),
          ('Duas portas de correr ripadas, 87 cada',
           'Vestiário e despensa. Ripadas na mesma cadência da parede, com '
           'folga de 3,2 cm, e sistema de correr embutido. <b>Fechadas, elas '
           'não existem</b> — é o alinhamento da ripa que entrega o trabalho.')],
      nota=('Por que este é o item mais caro da casa',
            'Ele carrega sozinho mais fita e mais filetagem que todo o resto do '
            'projeto somado. Não é a área de chapa que o faz caro: é a quantidade '
            'de peças pequenas que precisam sair idênticas.')),
 dict(img=['r-cozinha-armarios', 'cristaleira'],
      tag='Cozinha · o armário de portas de vidro no render · a cristaleira na elevação',
      eyebrow='Cozinha e gourmet', h2='O vidro é nosso, e sai no mesmo contrato.',
      lead='Quatro peças em volta da bancada existente — e em três delas o '
           'vidro reflecta cristal é parte do móvel, não acessório.',
      mv=[('Cristaleira, 147 × 275 × 54',
           'Duas portas de vidro reflecta com perfil, seis prateleiras e nicho '
           'inferior. A peça de vitrine do ambiente: é ela que fica acesa.'),
          ('Armário superior com portas de vidro, 387',
           'Seis portas — quatro de 70,8 e duas de 49 — sobre a bancada '
           'existente, 35 cm de profundidade.'),
          ('Coluna de eletrodoméstico, 98 × 275 × 60',
           'De piso a teto, com o vão do forno e do micro-ondas.'),
          ('Gourmet · armário complementar, 102 × 86 × 55',
           'Duas portas de vidro reflecta, no mesmo padrão da cozinha.')],
      nota=('O que a medição confirma',
            'A bancada e a alvenaria da cozinha são existentes. A altura livre '
            'sob o armário superior fecha na medição no local, antes do corte.')),
 dict(img=['r-escritorio', 'escritorio'],
      tag='Escritório · render do anteprojeto e elevações do executivo',
      eyebrow='Escritório', h2='A mesa que avança dois metros e não balança.',
      lead='A bancada corre 2,36 m sobre o armário e avança 2,19 m em mesa — '
           'é a peça que mais exige estrutura em toda a casa.',
      mv=[('Painel ripado de fundo, 316 × 272',
           'A mesma ripa de 2 com vão de 1 do resto da casa, agora na parede '
           'inteira do fundo.'),
          ('Armário superior, 190 × 80 × 32',
           'Quatro portas de 47,5, a 60 cm do teto.'),
          ('Bancada e mesa, 236 + 216 × 100',
           'Tampo de <b>duas chapas coladas</b> na mesa que avança, com apoio '
           'metálico na ponta. Tampo a 75 cm do piso.'),
          ('Armário inferior, 228 × 68 × 60',
           'Portas e gaveteiro, com rodapé recuado.')],
      nota=('O revestimento atrás da bancada não é nosso',
            'A parede atrás é travertino romano escovado — pedra. Nosso é o '
            'ripado, os armários e a bancada.')),
 dict(img=['r-sala-tv', 'sala-tv'],
      tag='Sala de televisão · render do anteprojeto e elevação do executivo',
      eyebrow='Sala de televisão', h2='Seis metros e meio de parede, dois acabamentos.',
      lead='O ripado entra pela esquerda, o liso recebe a televisão, e o rack '
           'suspenso atravessa a junção dos dois sem mostrar onde ela está.',
      mv=[('Painel ripado, 353,5 × 272', 'Em continuidade com o painel liso, sem fio aparente entre eles.'),
          ('Painel liso, 300 × 272', 'Recebe a televisão de 70 polegadas, a 140 cm do piso.'),
          ('Rack de TV suspenso, 400 × 30',
           'Quatro gavetões de 100 cm, suspenso a 20 do piso. <b>É aqui que a '
           'corrediça aparece</b>: gavetão de um metro cheio é onde ferragem '
           'fraca entrega primeiro.')],
      nota=None),
 dict(img=['r-suite-tv', 'suite-parede-tv'],
      tag='Suíte principal · a parede da televisão, no render e na elevação 02',
      eyebrow='Suíte master · a parede da TV', h2='Uma parede, duas portas e nenhuma emenda à vista.',
      lead='A parede de frente para a cama é painelada de ponta a ponta, com '
           'duas portas embutidas no próprio painel.',
      mv=[('Parede painelada da TV, com as duas portas, 467 × 272',
           'Painel contínuo com o nicho da televisão e as duas folhas '
           'mimetizadas. Puxador tipo <b>cava usinada na própria peça</b> — '
           'não há ferragem aparente na parede inteira.')],
      nota=('O preço desta peça é o mesmo nas três linhas',
            'Ela não leva corrediça nem sistema de correr, e a escolha de '
            'ferragem não a atravessa. Vocês verão o mesmo número nas três '
            'colunas da folha de investimento — isso é proposital.')),
 dict(img=['r-suite01', 'suite-planta'],
      tag='Suíte 01 no render · suíte principal na planta, com a cabeceira centrada na cama',
      eyebrow='Suíte master e suíte 01', h2='As duas cabeceiras.',
      lead='A cabeceira da master tem 2,40 m e fica centrada na cama — a planta '
           'mostra, e nós medimos: ela passa 20 cm por trás de cada mesa de '
           'cabeceira.',
      mv=[('Painel ripado da cabeceira, 200 × 272', 'O ripado sobe atrás da cama, no mesmo passo de 3 cm.'),
          ('Painel liso da cabeceira, 267 × 272',
           'Completa os 467 cm da parede. A emenda entre as duas faixas cai '
           '<b>debaixo da cabeceira estofada</b>.'),
          ('Cabeceira estofada, 240 × 120',
           'Base de MDF, espuma de 30 mm e revestimento — 5 cm de espessura, '
           'como o executivo desenha.'),
          ('Mesas de cabeceira, duas de 90 × 50',
           'Corpo de 40 sobre pé metálico de 15, duas gavetas cada, a 10 cm da cama.'),
          ('Suíte 01 · cabeceira estofada, 192 × 120',
           'Mesma construção da master, em escala menor.')],
      nota=('A cabeceira da suíte 01 fecha na medição',
            'O executivo Rev. 03 não traz a prancha da suíte 01. A medida de '
            '192 × 120 é a nossa estimativa e está orçada como tal; ela é '
            'confirmada na medição no local, antes de qualquer corte.')),
 dict(img=['hall-painel', 'aparador-jantar'],
      tag='Hall e jantar · elevações do executivo · o anteprojeto não traz estes dois',
      eyebrow='Hall e jantar', h2='A porta da lavanderia, que não parece porta.',
      lead='Duas peças de entrada da casa — e as duas vivem de alinhamento, '
           'não de ferragem.',
      mv=[('Painel do hall, com porta de lavanderia e bit de canto',
           '206 × 272 mais a faixa de canto de 23. A porta de 80 × 210 é '
           '<b>mimetizada no painel</b>, com bandeira de 64 em cima e puxador '
           'tipo cava a 105 do piso.'),
          ('Aparador suspenso do jantar, 308 × 50 × 45',
           'Três portas de giro, suspenso a 35 cm do piso, com gaveta interna. '
           'Tampo de 45 sobre corpo de 41.')],
      nota=('O painel de 367 × 585 do jantar é travertino',
            'Pé-direito duplo, revestimento de pedra, marmoraria. Está no '
            'desenho ao lado do aparador e <b>não está nesta proposta</b>.')),
]

for _a in AMBIENTES:
    _imgs = ''.join(
        f'<img class="{"r" if n.startswith("r-") else "d"}" src="{b64(n)}" alt="">'
        for n in _a['img'])
    _mv = ''.join(f'<div class="mv"><span class="b"></span><span>'
                  f'<span class="t">{t}</span><span class="d"> — {d}</span>'
                  f'</span></div>' for t, d in _a['mv'])
    _nt = ''
    if _a['nota']:
        _nt = (f'<div class="amb-nota"><div class="t">{_a["nota"][0]}</div>'
               f'<p>{_a["nota"][1]}</p></div>')
    _solo = ' solo' if len(_a['img']) == 1 and _a['img'][0].startswith('r-') else ''
    folha(f'''<div class="ambw">
  <div class="band{_solo}">{_imgs}<div class="tag">{_a['tag']}</div></div>
  <div class="low"><div class="fitw">
    <div class="eyebrow">{_a['eyebrow']}</div><div class="rule"></div>
    <div class="h2">{_a['h2']}</div>
    <div class="lead" style="margin:3mm 0 4mm;max-width:none">{_a['lead']}</div>
    {_mv}</div>
   <div>{_nt}</div>
  </div>
</div>''')


# ═══ 13 · UMA ESCOLHA ═══════════════════════════════════════════════════
CMP = [
 ('Corrediça',
  'Telescópica, com o trilho aparente na lateral da gaveta e sem amortecedor de fechamento.',
  'Oculta alemã: o trilho some por baixo, a gaveta abre inteira e não mostra ferragem na lateral.',
  'Oculta Blum Movento: a mesma discrição da alemã, com o curso mais macio e a maior capacidade de carga das três.'),
 ('Dobradiça', 'Nacional, com abertura de noventa graus.',
  'Alemã, com amortecedor e regulagem nos três sentidos.',
  'Blum, com amortecedor e regulagem nos três sentidos.'),
 ('Sistema de correr', 'O mesmo sistema embutido nas três linhas, nas duas portas do corredor.',
  'O mesmo sistema embutido.', 'Sistema Blum, de curso mais macio.'),
 ('Ripado e painéis', 'A mesma ripa de 2 com vão de 1, a mesma base contínua e a mesma fita.',
  'Idêntico.', 'Idêntico.'),
 ('Iluminação', 'Perfil de LED embutido na própria peça, entregue instalado. O mesmo nas três.',
  'O mesmo perfil.', 'O mesmo perfil.'),
 ('Garantia', '1 ano', '10 anos', '30 anos'),
]
_lin = ''
for _k, *_v in CMP:
    _cls = ' style="font-weight:700;font-size:11pt"' if _k == 'Garantia' else ''
    _lin += (f'<tr><td class="l">{_k}</td>'
             f'<td{_cls}>{_v[0]}</td><td class="hi"{_cls}>{_v[1]}</td><td{_cls}>{_v[2]}</td></tr>')
folha(f'''<div class="pad apertada"><div class="fitp">
  <div class="eyebrow">Uma escolha</div><div class="rule"></div>
  <div class="h1">Três linhas. A diferença está na ferragem.</div>
  <div class="lead" style="margin:3mm 0 5mm">O desenho, os padrões de MDF, o
    ripado, a furação oculta, o puxador tipo cava e o acabamento são
    <b>os mesmos nas três</b>. O que muda é a peça que vocês tocam todo dia —
    e é ela que decide por quanto tempo o móvel continua fechando bem.</div>
  <table class="cmp">
   <tr><th></th><th>Telescópica</th><th class="hi">Hettich</th><th>Blum</th></tr>
   {_lin}
  </table>
  <div class="box"><div class="t">O que não muda</div>
   <p>Os padrões de MDF especificados no executivo, o ripado inteiro, o vidro
      reflecta cristal, as duas cabeceiras estofadas, o puxador tipo cava
      usinado na própria peça, a iluminação entregue instalada e a equipe
      própria do corte à montagem.</p></div>
</div></div>''')

# ═══ 14 · GARANTIA ══════════════════════════════════════════════════════
folha(f'''<div class="pad apertada"><div class="fitp">
  <div class="eyebrow">Garantia</div><div class="rule"></div>
  <div class="h1">O termo é assinado na entrega.</div>
  <div class="lead" style="margin:3mm 0 5mm">A garantia da Valvic é
    <b>escalonada pela ferragem</b> e vale para o escopo inteiro pelo prazo da
    <b>linha de menor tempo presente no projeto</b>. Não é promessa de
    proposta: é <b>termo assinado no dia da entrega</b>, junto com o guia de
    conservação do móvel.</div>
  <div class="three">
   <div><div class="term"><div class="k">Como se aciona</div></div>
    <div class="term"><div class="v">01 · Vocês nos chamam</div>
      <div class="s">Por telefone, WhatsApp ou e-mail, direto com a fábrica.
      Não há central, não há protocolo e não há intermediário.</div></div>
    <div class="term"><div class="v">02 · Respondemos em 24 horas</div>
      <div class="s">Compromisso de retorno, contado em horas corridas a
      partir do chamado.</div></div>
    <div class="term"><div class="v">03 · Visita em até três dias úteis</div>
      <div class="s">Se não resolvermos pelo telefone, a equipe vai ao local.
      Dentro do prazo, a visita e o reparo não têm custo.</div></div></div>
   <div><div class="term"><div class="k">O que o termo cobre</div></div>
    <div class="term"><div class="v">Marcenaria</div>
      <div class="s">Estrutura, painéis, ripado, frentes e acabamento, pelo
      prazo da linha escolhida.</div></div>
    <div class="term"><div class="v">Ferragem de movimento</div>
      <div class="s">Corrediça, dobradiça, articulador e sistema de correr,
      pelo prazo da linha escolhida.</div></div>
    <div class="term"><div class="v">Montagem e instalação</div>
      <div class="s">As instalações e regulagens têm garantia de <b>dois
      anos</b> em qualquer linha — inclusive na básica.</div></div></div>
   <div><div class="term"><div class="k">O que fica de fora</div></div>
    <div class="term"><div class="v">Iluminação em LED</div>
      <div class="s">É componente eletrônico e segue a garantia do fabricante
      da fita.</div></div>
    <div class="term"><div class="v">Desgaste de uso</div>
      <div class="s">Assim como o dano por umidade ou infiltração vinda da
      obra.</div></div>
    <div class="term"><div class="v">Alteração por terceiro</div>
      <div class="s">Feita no móvel depois da entrega. O termo traz também as
      obrigações de conservação do contratante.</div></div></div>
  </div>
</div></div>''')


# ═══ 15 · INVESTIMENTO · AS TRÊS LINHAS ═════════════════════════════════
_cards = ''
for _k, _nm, _d in [
   ('Básica', 'Corrediça telescópica',
    'Corre sobre esferas e <b>mostra o trilho na lateral da gaveta</b> quando '
    'ela abre. Não tem amortecedor: a gaveta fecha no impulso que você der. '
    'É o que a maior parte do mercado entrega como padrão, e ela cumpre o que '
    'promete — <b>o que muda é por quanto tempo</b>.'),
   ('Hettich', 'Corrediça oculta Hettich Quadro V6',
    'A oculta alemã corre <b>por baixo da caixa da gaveta</b>: você abre e não '
    'vê ferragem nenhuma, só a madeira. A gaveta sai inteira, o fechamento é '
    'amortecido e a regulagem é fina nos três sentidos. <b>É a linha de '
    'referência desta proposta.</b>'),
   ('Blum', 'Corrediça e dobradiça Blum Movento',
    'A mesma discrição da alemã, com o <b>curso mais macio e a maior '
    'capacidade de carga</b> das três — é o que se sente num gavetão de um '
    'metro cheio, que é o que o rack da sala tem quatro vezes.')]:
    _a, _u = GARANTIA[_k]
    _hi = ' hi' if _k == 'Hettich' else ''
    _cards += (f'<div class="c{_hi}"><div class="anos">{_a}</div>'
               f'<div class="unid">{_u} de garantia</div><div class="nm">{_nm}</div>'
               f'<div class="x">{_d}</div><div class="l">'
               f'<div class="k">A casa inteira</div>'
               f'<div class="v" style="font-size:15pt;font-weight:700">{brl(TOTAL[_k])}</div>'
               f'</div></div>')
folha(f'''<div class="pad apertada"><div class="fitp">
  <div class="eyebrow">Investimento · as três linhas</div><div class="rule"></div>
  <div class="h1">Um ano, dez, ou trinta.</div>
  <div class="lead" style="margin:3mm 0 0">O mesmo escopo, o mesmo desenho e os
    mesmos padrões. A diferença é a <b>ferragem</b> — a única peça da
    marcenaria que se usa todo dia e se desgasta — e o tempo pelo qual
    respondemos por ela. ⭐ <b>Abra uma gaveta de cada linha antes de
    decidir:</b> levamos as três amostras até vocês, sem compromisso, porque
    em trinta segundos a mão resolve o que a tabela não resolve.</div>
  <div class="gar justo">{_cards}</div>
  <div class="box"><div class="t">O que está incluso</div>
   <p>Projeto executivo de marcenaria, material, usinagem, ferragem e
      iluminação em LED embutida, mais os ofícios que esta proposta reúne —
      <b>vidro reflecta cristal, estofado das duas cabeceiras e o pé metálico
      das mesas</b> —, transporte, montagem e instalação, num só contrato, com
      uma só data e uma só arquiteta responsável. O travertino do jantar e as
      bancadas de pedra são marmoraria e ficam fora; a folha de condições
      nomeia o resto.</p></div>
</div></div>''')

# ═══ 16 · INVESTIMENTO · ITEM A ITEM ════════════════════════════════════
#   ⭐ A ordem do cliente é a do índice, não a do motor. ⛔ E a soma tem de
#     continuar a mesma depois de reordenar — a trava abaixo é o que prova.
ORDENADO = [d for a in AMB_ORD for d in S if d['amb'] == a]
assert len(ORDENADO) == len(S), 'ambiente fora do índice'
for _k in ORDEM:
    assert abs(sum(d[_k + '_pv'] for d in ORDENADO) - TOTAL[_k]) < .01

_rows, _ant = '', None
for d in ORDENADO:
    _a = d['amb'] if d['amb'] != _ant else ''
    _ant = d['amb']
    _nome = esc(d['nome'])
    _rows += (f'<tr><td class="l" style="color:var(--gold);font-size:6.6pt;'
              f'letter-spacing:.18em;text-transform:uppercase;font-weight:700">{_a}</td>'
              f'<td class="l">{_nome}</td>'
              + ''.join(f'<td{" class=hi" if k == "Hettich" else ""}>{brl(d[k + "_pv"])}</td>'
                        for k in ORDEM) + '</tr>')
folha(f'''<div class="pad apertada"><div class="fitp">
  <div class="eyebrow">Investimento · item a item</div><div class="rule"></div>
  <div class="h1">Dezoito itens, oito ambientes.</div>
  <div class="lead" style="margin:3mm 0 4mm">O mesmo escopo nas três colunas.
    <b>Doze dos dezoito itens valem o mesmo na telescópica e na Hettich</b> —
    são os que não levam corrediça nem sistema de correr, e a escolha de
    ferragem não os atravessa.</div>
  <table class="inv">
   <tr><th class="l"></th><th class="l">Item</th>
       <th>Telescópica</th><th class="hi">Hettich</th><th>Blum</th></tr>
   {_rows}
   <tr class="tot"><td class="l"></td><td class="l">A casa inteira</td>
    {''.join(f'<td{" class=hi" if k == "Hettich" else ""}>{brl(TOTAL[k], False)}</td>' for k in ORDEM)}</tr>
  </table>
</div></div>''')

# ═══ 17 · CONDIÇÕES ═════════════════════════════════════════════════════
_pay = ''.join(f'<tr><td>{_d}</td><td class="d">{_p:.0%}</td></tr>'
               for _d, _p in b.PARCELAS)
folha(f'''<div class="pad apertada"><div class="fitp">
  <div class="eyebrow">Condições</div><div class="rule"></div>
  <div class="h1">Prazo, pagamento e fronteiras.</div>
  <div class="three">
   <div>
    <div class="term"><div class="k">Validade desta proposta</div>
      <div class="v">{VALIDADE}</div><div class="s">A partir desta data.</div></div>
    <div class="term"><div class="k">Prazo de execução</div>
      <div class="v">{PRAZO}</div><div class="s">{PRAZO_DE}</div></div>
    <div class="term"><div class="k">Entrega antecipada</div>
      <div class="v">{ENTREGA_ANTECIPADA[0]} até {ENTREGA_ANTECIPADA[1]}</div>
      <div class="s">O escritório sai à frente do cronograma e é entregue
        instalado nesta data, independentemente do prazo do restante.</div></div>
    <div class="term"><div class="k">Garantia</div>
      <div class="v">Conforme a linha</div>
      <div class="s">Trinta anos na Blum, dez na Hettich e um ano na
        telescópica, sobre a marcenaria e a ferragem. Instalação e regulagem,
        dois anos em qualquer linha. Termo assinado na entrega.</div></div>
    <div class="term"><div class="k">Projeto executivo de marcenaria</div>
      <div class="v">Incluso</div><div class="s">Aprovado por vocês e pela
        arquitetura antes de qualquer corte.</div></div>
   </div>
   <div>
    <div class="term"><div class="k">Formas de pagamento</div></div>
    <table class="pay">{_pay}</table>
    <div class="term" style="border-bottom:none"><div class="s">{b.PARCELAS_NOTA}</div></div>
    <div class="box" style="margin-top:4mm"><div class="t">Um interlocutor</div>
     <p>Da aprovação à entrega, vocês tratam com a arquiteta responsável pelo
        projeto. Um contrato, uma data, um nome para chamar.</p></div>
   </div>
   <div class="fora">
    <div class="term"><div class="k">O que não está nesta proposta</div></div>
    <ul>
     <li><div class="k">Pedra</div><div class="v">O painel do jantar, de
       367 × 585, em travertino romano escovado, e qualquer bancada, sóculo,
       soleira ou peitoril. É marmoraria.</div></li>
     <li><div class="k">Eletrodomésticos e metais</div><div class="v">Cooktop,
       forno, micro-ondas, coifa, geladeira, lava-louças, cubas, torneiras e
       louças.</div></li>
     <li><div class="k">Obra civil e instalações</div><div class="v">Alvenaria,
       elétrica — pontos, circuitos, drivers e interruptores —, esquadrias,
       forro, piso e pintura de parede. A bancada e a alvenaria existentes da
       cozinha.</div></li>
     <li><div class="k">Decoração</div><div class="v">Mobiliário solto,
       cortinas, tapetes, objetos e quadros.</div></li>
     <li><div class="k">A confirmar antes da produção</div><div class="v">A
       medição no local, que fecha a altura do piso ao forro e de onde o prazo
       passa a contar. <b>O padrão do MDF amadeirado</b>, que o executivo
       deixa "a definir". <b>A cabeceira da suíte 01</b>, cuja prancha não está
       no Rev. 03 e cuja medida de 192 × 120 é estimativa nossa. E <b>os pontos
       de iluminação</b>, que as pranchas não trazem.</div></li>
    </ul>
   </div>
  </div>
  <div class="sig">
   <div class="ln">{CLIENTE or PROJETO}</div>
   <div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div>
  </div>
</div></div>''')

# ═══ 18 · FECHAMENTO ════════════════════════════════════════════════════
folha(f'''<div class="pad" style="justify-content:center">
  <div class="cv-brand" style="color:var(--gold-lt)">Valvic Marcenaria</div>
  <div class="h1" style="font-size:40pt;margin-top:6mm">Um contrato.<br>Uma data.<br>
    <span style="color:var(--gold-lt)">Um nome</span> para chamar.</div>
  <div class="lead" style="color:#CFC6B4;margin-top:7mm;max-width:150mm">
    Obrigado pela confiança de pôr esta casa na nossa mão. Do corredor da
    cozinha à cabeceira da suíte, o desenho sai da nossa fábrica e chega
    instalado.</div>
  <div class="cv-meta" style="margin-top:12mm;max-width:150mm">
   <div><div class="k">Proposta</div><div class="v">{CLIENTE or PROJETO}</div></div>
   <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
  </div>
</div>''', escura=True, rodape=False)


# ════════════════════════════════════════════════════════════════════════
# ⭐ A MONTAGEM
# ════════════════════════════════════════════════════════════════════════
CSS = (CASA / 'css-caderno.css').read_text(encoding='utf-8') + SUPLEMENTO
JS = (CASA / 'js-caderno.js').read_text(encoding='utf-8')

_corpo = ''
for _i, (_h, _escura, _rod) in enumerate(PAGINAS, 1):
    _cls = 'slide dark' if _escura else 'slide'
    _pe = ''
    if _rod:
        _pe = (f'<div class="foot"><span>Valvic&nbsp;·&nbsp;'
               f'{CLIENTE or PROJETO}</span><span>{_i:02d}</span></div>')
    _corpo += f'<div class="{_cls}">{_h}{_pe}</div>'

HTML = (
 '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
 f'<title>Proposta · {CLIENTE or PROJETO}</title>'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
 'family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@'
 '9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
 f'<style>{CSS}</style></head><body>{_corpo}'
 f'<script>{JS}</script><script>{POS_AJUSTE}</script></body></html>')

SAIDA_HTML = AQUI / 'proposta-costa-laguna.html'
SAIDA_PDF = AQUI / 'proposta-costa-laguna.pdf'


def _qa():
    """⛔⛔ O QA DO CLOSER, RODANDO — não é checklist de papel.

    Material premium morre de erro de dado, e o erro que mais mata é o nome
    de OUTRO cliente sobrevivendo de um template antigo. Aqui ele não passa:
    a trava lê o HTML pronto e procura."""
    #   ⛔ A VARREDURA NÃO PODE LER O BASE64 DAS IMAGENS. A primeira versão
    #     leu, e acusou "nan" na proposta: a sequência estava dentro do PNG
    #     da elevação, não no texto. ⭐ Trava que grita por acaso é trava que
    #     ninguém respeita — então ela passa a ler só o que o cliente lê.
    t = re.sub(r'data:image/[^"\']+', '«imagem»', HTML)
    proibidos = ['Gustavo', 'Raposo', 'Luiza Pacheco', 'Michel', 'Michell',
                 'Jessica', 'Eliza', 'Juliana', 'Alice', 'Vargas Decor LTDA.',
                 'R$ 0,00', 'None', 'nan']
    for p in proibidos:
        if p == 'Vargas Decor LTDA.':
            continue
        assert p not in t, f'⛔⛔ QA: "{p}" apareceu na proposta'
    for k in ORDEM:
        assert brl(TOTAL[k], False) in t or brl(TOTAL[k]) in t, \
            f'⛔ QA: o total da linha {k} não está impresso'
    assert 'Valvic Marcenaria · Vargas Decor LTDA' in t, '⛔ QA: falta a razão social'
    for a in AMB_ORD:
        assert a in t, f'⛔ QA: o ambiente {a} sumiu do caderno'
    assert PRAZO in t and ENTREGA_ANTECIPADA[1] in t, '⛔ QA: prazo não impresso'
    assert '>1<' in t and '>10<' in t and '>30<' in t, '⛔ QA: garantia não impressa'
    assert 'travertino' in t.lower(), '⛔ QA: a pedra não foi nomeada como fora'
    #   ⭐⭐ A ORDEM DAS FOLHAS É DECISÃO COMERCIAL, NÃO DIAGRAMAÇÃO.
    #     [Jonathan, 05/11/2026] "fale da garantia antes de apresentar
    #     valores". Quem lê o prazo de garantia antes do número lê o número
    #     como consequência; quem lê depois, lê como desculpa. A trava
    #     existe para que uma reordenação futura não desfaça isso em
    #     silêncio.
    assert t.index('O termo é assinado na entrega') < t.index('Um ano, dez, ou trinta'), \
        '⛔⛔ QA: a garantia voltou para DEPOIS do preço'
    #   ⛔ E a folha dos três cartões é UMA SÓ. Havia duas, quase iguais,
    #     e o cliente lia a mesma coisa duas vezes. Três cartões mais a
    #     linha do total da tabela = quatro "A casa inteira", nunca sete.
    assert t.count('A casa inteira') == 4, \
        f'⛔⛔ QA: {t.count("A casa inteira")} vezes "A casa inteira" — a folha redundante voltou'
    return True


if __name__ == '__main__':
    _qa()
    SAIDA_HTML.write_text(HTML, encoding='utf-8')
    print(f'✓ {SAIDA_HTML.name} · {len(PAGINAS)} folhas · {len(HTML)/1e6:.1f} MB')
    r = subprocess.run(
        ['node', str(CASA / 'render-pdf.js'), str(SAIDA_HTML), str(SAIDA_PDF)],
        env={**__import__('os').environ,
             'NODE_PATH': '/opt/node22/lib/node_modules'},
        capture_output=True, text=True)
    if r.returncode:
        print('⛔ render:', r.stderr[-900:])
        sys.exit(1)
    import pymupdf
    d = pymupdf.open(SAIDA_PDF)
    rr = d[0].rect
    print(f'✓ {SAIDA_PDF.name} · {len(d)} páginas · '
          f'{rr.width:.0f} x {rr.height:.0f} pt · '
          f'{SAIDA_PDF.stat().st_size/1e6:.1f} MB')
    assert len(d) == len(PAGINAS), (
        f'⛔⛔ {len(PAGINAS)} folhas montadas e {len(d)} páginas no PDF — '
        'alguma folha transbordou e virou duas')
    assert rr.width > rr.height, '⛔ o caderno saiu em retrato'
    d.close()
