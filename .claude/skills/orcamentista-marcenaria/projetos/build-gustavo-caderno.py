# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO — caderno de proposta · casa completa  [30/10/2026]

⛔⛔ LI O DOCUMENTO ERRADO TRÊS RODADAS SEGUIDAS.
  O Jonathan pediu "a proposta igual à do Michel" e eu fui atrás da
  `proposta-michelle-arlei.pdf` — Michelle e Arlei, A4 retrato, doze
  páginas. O "Michel" dele é a JÉSSICA E MICHELL DO ICA, cujo caderno é
  `build-caderno-ica.py`: A4 PAISAGEM, trinta e cinco folhas.
  Tudo o que ele repetiu três vezes bate com o caderno do ICA e não bate
  com o do Michelle:
    · "as páginas 3, 4 e 5 são de extrema importância"
         ICA 3/4/5 = a empresa · as doze etapas · a arquiteta.
         Michelle 3/4/5 = tabela de linhas · ambiente Sala · ambiente Cozinha.
    · "a forma de pagamento, idem"
         ICA = 30% na assinatura, 20% em 30 dias, 20% em 60, 30% em 90,
         todas por TRANSFERÊNCIA BANCÁRIA. Michelle = escada de desconto
         com cartão, que é justamente o que ele mandou tirar.
    · "as mesmas etapas" = as doze etapas do ICA, não as cinco do Michelle.
    · "a página da arquiteta" = a folha 05 do ICA. O Michelle não tem.
  ⭐ A LIÇÃO: quando o pedido aponta para um documento, ABRA O DOCUMENTO.
    Eu "sabia" qual era o Michel e nunca conferi — e a planilha de dúvidas
    estava a um `pdftotext` de distância.

⛔ SÓ A ESTRUTURA VEM DO CADERNO DO ICA. Nenhum número, nenhum ambiente e
  nenhum nome daquele cliente entra aqui: "não pode haver informações
  relacionadas ao orçamento do Michell, é outro cliente". Os asserts no
  fim do arquivo provam isso a cada build.

⛔⛔ NENHUM NÚMERO É DIGITADO: tudo sai de `gustavo-raposo/cenarios.py`.
⛔ Sem metragem e sem contagem em nenhuma descrição de móvel.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64, json, html, re

P = pathlib.Path(__file__).resolve().parent


def _mod(nome, arquivo):
    spec = importlib.util.spec_from_file_location(nome, P / arquivo)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nome] = m
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


cen = _mod('cen', 'gustavo-raposo/cenarios.py')
amb = _mod('amb', 'gustavo-raposo/ambientes.py')
CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')
TXT = json.loads((P / 'gustavo-raposo/copy.json').read_text(encoding='utf-8'))

CLIENTE = 'Gustavo Raposo'
OBRA, CIDADE = 'Condomínio Vale dos Pinhais', 'Nova Lima · MG'
ARQ, DATA = 'Luiza Pacheco Arquitetura', 'Outubro de 2026'
PRAZO, VALIDADE = '120 dias corridos', '7 dias úteis'
LIN = ('Telescópica', 'Hettich', 'Blum')     # ⭐ sempre da entrada ao topo
NF = 23                                      # folhas · o assert confere
N0 = 19                                      # ⛔ a primeira folha com preço

br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')
brs = lambda v: f'{v:,.0f}'.replace(',', '.')
E = lambda t: html.escape(str(t))


def uri(n):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P / 'img-gustavo-raposo' / n).read_bytes()).decode())


IMG = {n.stem: uri(n.name) for n in sorted((P / 'img-gustavo-raposo').iterdir())}

# ⛔ Um agente ABRIU cada um dos 31 renders e cortou os que não mostram
#   marcenaria — entre eles o que eu tinha posto na capa, que era mesa,
#   cadeira e pedra. Nenhum destes pode voltar à peça; o assert no fim prova.
CORTADAS = {'varanda-01', 'office-02', 'office-muxarabi', 'banho-master-02',
            'banho02-02', 'hospedes-01',
            # ⛔ cortado na revisão da peça pronta: parede branca com TV e
            #   um móvel solto. A folha vende armário de correr flutuante
            #   e a foto não mostra nenhum.
            'hospedes-02'}

S, N = [], [0]


def folha(corpo, dark=False, rodape=True, foot_r=False):
    N[0] += 1
    f = (f'<div class="foot{" r" if foot_r else ""}">'
         f'<span>Valvic&nbsp;·&nbsp;{E(CLIENTE)}</span>'
         f'<span>{N[0]:02d}</span></div>') if rodape else ''
    S.append(f'<div class="slide{" dark" if dark else ""}">{corpo}{f}</div>')


# ── 01 · capa ───────────────────────────────────────────────────────────
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">A casa<br>inteira.</div>
  <div class="cv-s">Dezenove ambientes,<br>
     do primeiro desenho ao dia da instalação.</div>
  <div class="cv-meta">
   <div><div class="k">Cliente</div><div class="v">{E(CLIENTE)}</div></div>
   <div><div class="k">Projeto</div><div class="v">{E(ARQ)}</div></div>
   <div><div class="k">Local</div><div class="v">{E(OBRA)} · {E(CIDADE)}</div></div>
   <div><div class="k">Data</div><div class="v">{E(DATA)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['cozinha-03']}" alt=""></div>
</div>
<div class="foot" style="right:auto;width:92mm;border-top-color:rgba(255,255,255,.13)">
 <span>Proposta de marcenaria</span><span>Valvic · Vargas Decor</span></div>''',
      dark=True, rodape=False)

# ── 02 · abertura ───────────────────────────────────────────────────────
ab = TXT['abertura']
folha(f'''<div class="ambw">
 <div class="band" style="height:104mm"><img src="{IMG['varanda-02']}" alt="">
   <div class="tag">Varanda</div></div>
 <div class="low" style="grid-template-columns:1fr;padding:11mm 18mm 12mm">
  <div><div class="eyebrow">O que esta casa pede</div><div class="rule"></div>
   <h1 class="h1" style="margin:0 0 5mm">{E(ab['titulo'])}</h1>
   <p class="lead" style="max-width:none;font-size:10.4pt">{ab['texto']}</p></div>
 </div></div>''')

# ── 03 · a empresa e a infraestrutura ───────────────────────────────────
em = TXT['empresa']
pil = '\n'.join(f'''<div class="c"><div class="n">{E(p['numero'])}</div>
  <div class="t">{E(p['titulo'])}</div><div class="d">{p['texto']}</div></div>'''
                for p in em['pilares'])
folha(f'''<div class="pad">
 <div class="eyebrow">A empresa e a infraestrutura</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">{E(em['titulo'])}</h1>
 <p class="lead" style="max-width:215mm">{em['abertura']}</p>
 <div class="fr" style="margin-top:6mm;flex:1;min-height:0">{pil}</div>
 <div class="box" style="margin-top:5mm"><p style="font-size:9.4pt;color:var(--ink)">
   {em['fechamento']}</p></div>
</div>''')

# ── 04 · o processo, as doze etapas ─────────────────────────────────────
#    ⭐ [Jonathan 30/10] "as mesmas etapas que está na proposta do Michel".
#      São estas doze, em quatro blocos — o caminho que o projeto percorre
#      da decisão do cliente até a casa em uso.
BLOCOS = [
 ('Partida', 'da decisão ao contrato', [
  ('Decisão', 'Aprovação',
   'Escopo, acabamentos e ferragens definidos. Nada entra em produção sem '
   'essa decisão.', 'Escopo fechado, ambiente por ambiente.'),
  ('Registro', 'Contrato',
   'Contrato assinado, prazos e responsabilidades registrados. Tudo o que '
   'foi dito fica escrito.', 'Contrato e cronograma com datas.')]),
 ('Engenharia', 'da obra ao arquivo de máquina', [
  ('Parede', 'Medição técnica',
   'Nossa equipe mede a obra no local. O projeto passa a conversar com a '
   'parede real.', 'Medidas da obra construída, não do desenho.'),
  ('Desenho', 'Detalhamento',
   'Fechamos com vocês e com a arquitetura cada decisão de execução antes '
   'de cortar nada.', 'Nenhuma decisão de execução em aberto.'),
  ('Arquivo', 'Programação',
   'O detalhamento vira arquivo de máquina. O erro é corrigido na tela, '
   'não na chapa.', 'Plano de corte e usinagem programado.')]),
 ('Fábrica', 'onde o móvel nasce e é testado', [
  ('Corte', 'Usinagem',
   'Corte, furação, fresa e acabamento de borda. Tudo acontece dentro da '
   'nossa fábrica.', 'Peças prontas e identificadas, uma por uma.'),
  ('Encaixe', 'Montagem em fábrica',
   'O móvel é montado aqui antes de ir para a obra. Problema de encaixe '
   'morre aqui.', 'Móvel montado e testado antes de sair.'),
  ('Checklist', 'Conferência',
   'Peça por peça contra o projeto: medida, cor, ferragem, sentido de '
   'abertura, luz.', 'Checklist assinado antes do carregamento.')]),
 ('Entrega', 'da nossa fábrica à sua casa', [
  ('Carga', 'Transporte',
   'Embalagem, carregamento e transporte são nossos, da nossa fábrica até '
   'a porta da sua casa. O móvel não troca de mão no caminho.',
   'Móvel embalado e carregado por quem o montou.'),
  ('Prumo', 'Instalação',
   'Equipe própria instala, nivela e regula. A obra recebe móvel pronto, '
   'não peça solta.', 'Móveis no lugar, nivelados e regulados.'),
  ('Teste', 'Vistoria técnica',
   'Com vocês, abrimos tudo: cada porta, cada gaveta, cada luz. Nada passa '
   'sem testar.', 'Ajustes finais feitos na frente de vocês.'),
  ('Casa', 'Entrega final',
   'Ambiente limpo, móvel em uso e termo de garantia na mão de vocês. O '
   'projeto virou casa.', 'Termo de garantia emitido e assinado.')]),
]
assert sum(len(b[2]) for b in BLOCOS) == 12, '⛔ a folha promete DOZE etapas'
_n = [0]


def etapa(k, t, l, e):
    _n[0] += 1
    return f'''<div class="pe"><div class="pe-n">{_n[0]:02d}</div>
      <div class="pe-k">{E(k)}</div><div class="pe-t">{E(t)}</div>
      <div class="pe-l">{E(l)}</div><div class="pe-e">{E(e)}</div></div>'''


cols = '\n'.join(
    f'''<div class="pb"><div class="pb-h">{E(nome)}</div>
      <div class="pb-s">{E(sub)}</div>{''.join(etapa(*e) for e in ets)}</div>'''
    for nome, sub, ets in BLOCOS)
folha(f'''<div class="pad" style="padding:13mm 15mm 20mm">
 <div class="eyebrow">O caminho do seu projeto</div><div class="rule"></div>
 <div style="display:flex;align-items:baseline;gap:9mm;margin-bottom:5mm">
  <h1 class="h1" style="margin:0">Doze etapas,<br>um só responsável</h1>
  <p class="lead" style="margin:0;max-width:112mm">Da decisão de vocês até a casa
    pronta são doze etapas — e nenhuma delas muda de dono.</p></div>
 <div class="rail"></div>
 <div class="proc">{cols}</div>
</div>''')

# ── 05 · a arquiteta responsável ────────────────────────────────────────
#    ⭐ [Jonathan 30/10] "a página da arquiteta".
aq = TXT['arquiteta']
pars = ''.join(f'<p style="margin:0 0 3mm">{x}</p>' for x in aq['paragrafos'])
folha(f'''<div class="amb">
 <div class="amb-img"><img src="{IMG['suite-master-01']}" alt="">
   <div class="tag">Suíte master</div></div>
 <div class="amb-txt" style="padding:15mm 15mm 21mm 12mm">
  <div class="eyebrow">Quem responde</div><div class="rule"></div>
  <h2 class="h2" style="margin:1mm 0 5mm">{E(aq['titulo'])}</h2>
  <div style="color:var(--soft);font-size:9pt">{pars}</div>
  <div class="amb-nota" style="margin-top:auto"><div class="t">{E(aq['nota_titulo'])}</div>
   <p>{aq['nota_texto']}</p></div>
 </div></div>''', foot_r=True)

# ── 06 · índice dos dezenove ambientes ──────────────────────────────────
#    ⛔ O material de cada ambiente sai da folha que o contém, não de uma
#      segunda lista digitada à mão: duas cópias do mesmo texto divergem
#      sem dar erro.
#    ⛔ E quando a folha traz MENOS acabamentos que ambientes, o que falta
#      repete o ÚLTIMO, não o primeiro: na folha dos hóspedes os dois
#      banhos dividem o Nogueira Thar, e herdar o Off-White da suíte punha
#      material errado no índice — erro que ninguém vê, porque a linha
#      continua bonita.
RUIDO = re.compile(r'^(Linha \w+|Duratex|Guararapes|Sayerlack|sem MDF'
                   r'|sobre MDF|n[ao] \w+|com .*|e \w+ interno.*)$', re.I)


def enxuto(parte):
    pedacos = [x.strip() for x in parte.split(',')]
    pedacos = [x for x in pedacos if x and not RUIDO.match(x)]
    return ', '.join(pedacos).replace(', e ', ' e ')


MAT = {}
for (titulo, _i, tags, acab, _it), (a, b) in zip(amb.PG, amb.MAPA):
    partes = [x.strip() for x in acab.split('·')]
    for k, idx in enumerate(range(a, b)):
        MAT[idx] = enxuto(partes[min(k, len(partes) - 1)])
assert len(MAT) == 19
assert MAT[16] == MAT[17] == 'MDF Nogueira Thar e Branco', MAT[16]
assert MAT[18] == 'MDF Cinza Fóssil e Azul Secreto', MAT[18]
assert MAT[2] == 'Laca acetinada M048', MAT[2]


def coluna(pares):
    return ''.join(
        f'<div class="ix"><span class="ix-n">{i + 1:02d}</span>'
        f'<span class="ix-t">{E(cen.AMB[i][0][3:])}</span>'
        f'<span class="ix-d">{E(MAT[i])}</span></div>' for i in pares)


folha(f'''<div class="pad">
 <div class="eyebrow">Os ambientes</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 2mm">Dezenove ambientes,<br>uma casa inteira.</h1>
 <p class="lead" style="margin-bottom:5mm">Uma folha para cada conjunto, com o que
    a Valvic executa ali e em que material cada peça sai.</p>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 12mm;flex:1;min-height:0">
  <div>{coluna(range(0, 10))}</div><div>{coluna(range(10, 19))}</div>
 </div></div>''')

# ── 07…15 · as nove folhas de ambiente, SEM preço ───────────────────────
PUX = {'A cozinha<br>e a despensa.': cen.PUXADOR_COZINHA + ', em todas as frentes'}
for titulo, imgs, tags, acab, itens in amb.PG:
    mv = ''.join(f'''<div class="mv"><span class="b"></span><span>
      <span class="t">{E(t)}</span> <span class="d">{E(d)}</span></span></div>'''
                 for t, d in itens)
    nota = (f'<div class="amb-nota"><div class="t">Puxador</div>'
            f'<p>{E(PUX[titulo])}</p></div>' if titulo in PUX else '')
    tag = ' · '.join(tags)
    limpo = titulo.replace('<br>', ' ')
    if len(imgs) == 1:
        # imagem à esquerda, a lista desce na coluna da direita
        curto = ' curto' if len(itens) <= 2 else ''
        folha(f'''<div class="amb">
         <div class="amb-img"><img src="{IMG[imgs[0]]}" alt="">
           <div class="tag">{E(tag)}</div></div>
         <div class="amb-txt{curto}">
          <div class="eyebrow">Ambiente</div><div class="rule"></div>
          <div class="fit"><h2 class="h2" style="margin:1mm 0 4mm">{titulo}</h2>
           {mv}{nota}
           <div class="amb-nota" style="background:none;border-left-color:var(--line)">
             <div class="t">Acabamentos</div><p>{E(acab)}</p></div></div>
         </div></div>''', foot_r=True)
    else:
        # faixa de imagens no alto, a lista em duas colunas embaixo
        band = ''.join(f'<img src="{IMG[i]}" alt="" style="flex:1;min-width:0">'
                       for i in imgs)
        meio = (len(itens) + 1) // 2
        c1 = ''.join(f'''<div class="mv"><span class="b"></span><span>
          <span class="t">{E(t)}</span> <span class="d">{E(d)}</span></span></div>'''
                     for t, d in itens[:meio])
        c2 = ''.join(f'''<div class="mv"><span class="b"></span><span>
          <span class="t">{E(t)}</span> <span class="d">{E(d)}</span></span></div>'''
                     for t, d in itens[meio:])
        # ⛔ A FAIXA FIXA ESTOUROU A FOLHA DA SUÍTE DAS FILHAS. Onze móveis
        #   em duas colunas não cabem sob 88mm de foto: o último item saía
        #   pela borda e os acabamentos sumiam, sem erro nenhum no build.
        #   A faixa agora cede altura quando a lista é longa, e o que sobrar
        #   encolhe no `.fitw` até caber — a mesma trava do `.amb-txt`.
        alt = 88 if len(itens) <= 4 else (76 if len(itens) <= 6 else
              (70 if len(itens) <= 8 else 62))
        folha(f'''<div class="ambw">
         <div class="band" style="height:{alt}mm;display:flex;gap:2mm">{band}
           <div class="tag">{E(tag)}</div></div>
         <div class="low" style="display:block;padding:7mm 18mm 17mm">
          <div class="fitw">
           <div class="eyebrow">Ambiente</div><div class="rule"></div>
           <h2 class="h2" style="margin:1mm 0 3mm">{titulo}</h2>
           <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 11mm">
            <div>{c1}</div><div>{c2}</div></div>
           {nota}
           <div class="amb-nota" style="background:none;border-left-color:var(--line)">
             <div class="t">Acabamentos</div><p>{E(acab)}</p></div>
          </div>
         </div></div>''')

# ── 16 · a escolha: três linhas, a diferença está na ferragem ───────────
DIF = [
 ('Corrediça',
  'Telescópica, com o trilho aparente na lateral da gaveta e sem amortecedor '
  'de fechamento.',
  'Oculta alemã: o trilho some por baixo, a gaveta abre inteira e não mostra '
  'ferragem na lateral.',
  'Oculta Blum: a mesma discrição da alemã, com o curso mais macio e a maior '
  'capacidade de carga das três.'),
 ('Dobradiça',
  'Nacional, com abertura de noventa graus.',
  'Alemã, com amortecedor e regulagem nos três sentidos.',
  'Blum, com amortecedor e regulagem nos três sentidos.'),
 ('Básculas',
  'Articulador premium de molas: a porta sobe sozinha e para onde você '
  'soltar. O mesmo nas três linhas.',
  'O mesmo articulador premium.', 'O mesmo articulador premium.'),
 ('Iluminação',
  'Perfil de LED embutido na própria peça, com difusor sem pontos e cor '
  'estável no tempo. O mesmo nas três linhas.',
  'O mesmo perfil, entregue instalado.', 'O mesmo perfil, entregue instalado.'),
 ('Garantia', cen.CEN['Telescópica']['gar'], cen.CEN['Hettich']['gar'],
  cen.CEN['Blum']['gar']),
]
linhas = ''.join(
    f'<tr><td class="l">{E(k)}</td><td style="text-align:left;font-size:8.4pt">{E(a)}</td>'
    f'<td class="hi" style="text-align:left;font-size:8.4pt">{E(b)}</td>'
    f'<td style="text-align:left;font-size:8.4pt">{E(c)}</td></tr>'
    for k, a, b, c in DIF)
folha(f'''<div class="pad">
 <div class="eyebrow">Uma escolha</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Três linhas. A diferença está na ferragem.</h1>
 <p class="lead" style="max-width:215mm">O desenho, os padrões de MDF, a laca da
   cozinha, a furação oculta e o acabamento são <b>os mesmos nas três</b>. O que muda
   é a peça que vocês tocam todo dia — e é ela que decide quanto tempo o móvel
   continua fechando bem.</p>
 <table class="cmp" style="margin-top:6mm">
  <tr><th class="l" style="text-align:left"></th>
   {''.join(f'<th{" class=hi" if n == "Hettich" else ""}>{E(n)}</th>' for n in LIN)}</tr>
  {linhas}
 </table>
 <div class="box" style="margin-top:auto"><div class="t">O que não muda</div>
  <p>Os padrões de MDF especificados pela arquiteta, a laca acetinada da cozinha,
   a furação oculta, o puxador cava usinado na própria peça, as almas de aço nas
   prateleiras de vão longo, a iluminação entregue instalada e a equipe própria
   do corte à montagem.</p></div>
</div>''')

# ── 17 · as três opções, antes de qualquer valor ────────────────────────
#    ⭐ [Jonathan 30/10] "em uma página fale sobre as três opções de produto.
#      Antes de apresentar valores."
OPC = [
 ('Telescópica',
  'A corrediça telescópica corre sobre esferas e <b>mostra o trilho na '
  'lateral da gaveta</b> quando ela abre. Não tem amortecedor: a gaveta '
  'fecha no impulso que você der. É a ferragem que a maior parte do mercado '
  'entrega como padrão, e ela cumpre o que promete — <em>o que muda é por '
  'quanto tempo</em>.'),
 ('Hettich',
  'A corrediça oculta alemã corre <b>por baixo da caixa da gaveta</b>: você '
  'abre e não vê ferragem nenhuma, só a madeira. A gaveta sai inteira, o '
  'fechamento é amortecido e a regulagem é fina nos três sentidos. '
  '<em>É a linha que especificamos nesta casa</em> e a que o projeto da '
  'arquiteta pressupõe.'),
 ('Blum',
  'A mesma discrição da alemã, com o <b>curso mais macio e a maior '
  'capacidade de carga</b> das três — é o que se sente num gavetão cheio, '
  'que é onde ferragem fraca aparece primeiro. A Blum é a referência do '
  'mercado, e é por isso que respondemos por ela <em>por trinta anos</em>.'),
]
ops = ''.join(
    f'''<div class="c{" hi" if k == "Hettich" else ""}">
     <div class="anos">{E(cen.CEN[k]['gar'].split()[0])}</div>
     <div class="unid">anos de garantia</div>
     <div class="nm">{E(cen.CEN[k]['chamada'])}</div>
     <div class="x">{d}</div></div>''' for k, d in OPC)
folha(f'''<div class="pad">
 <div class="eyebrow">As três opções</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O que vocês vão sentir na mão.</h1>
 <p class="lead" style="max-width:215mm">A ferragem é a única peça da marcenaria
  que <b>se usa todo dia e se desgasta</b>. O MDF não cansa, a pintura não cansa,
  a furação não cansa. A corrediça e a dobradiça, sim — e é por isso que a escolha
  entre as três linhas <b>vale para a casa toda</b>: a garantia do conjunto segue
  sempre a ferragem de menor linha presente.</p>
 <div class="gar justo">{ops}</div>
 <div class="box" style="margin-top:5mm"><div class="t">Como escolher</div>
  <p>Abra uma gaveta de cada linha antes de decidir — <b>em trinta segundos a mão
   resolve o que a tabela não resolve</b>. Levamos as três amostras até vocês
   antes do fechamento, sem compromisso.</p></div>
</div>''')

# ── 18 · a garantia: o termo e como se aciona ───────────────────────────
#    ⭐ [Jonathan 30/10] "fale do nosso termo de garantia e formato de
#      acionamento". Os prazos saem de `closer-vendas/referencias/garantia.md`.
PASSOS = [
 ('Vocês nos chamam', 'Por telefone, WhatsApp ou e-mail, direto com a '
  'fábrica. Não há central, não há protocolo e não há intermediário.'),
 ('Respondemos em 24 horas', 'Esse é o nosso compromisso de retorno, '
  'contado em horas corridas a partir do chamado.'),
 ('Visita em até três dias úteis', 'Se não resolvermos pelo telefone, a '
  'equipe vai ao local. Dentro do prazo de garantia, a visita e o reparo '
  'não têm custo.'),
]
passos = ''.join(
    f'''<div class="pe"><div class="pe-n">{i:02d}</div>
     <div class="pe-t">{E(t)}</div><div class="pe-l">{E(d)}</div></div>'''
    for i, (t, d) in enumerate(PASSOS, 1))
folha(f'''<div class="pad">
 <div class="eyebrow">Garantia</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">O termo é assinado na entrega.</h1>
 <p class="lead" style="max-width:215mm">A garantia da Valvic <b>é escalonada pela
  ferragem</b>, e vale para a casa inteira pelo prazo da <b>linha de menor tempo
  presente no projeto</b>. Não é promessa de proposta: é <b>termo assinado no dia
  da entrega</b>, junto com o guia de conservação do móvel.</p>
 <div class="three" style="margin-top:6mm">
  <div>
   <div class="eyebrow" style="margin-bottom:3mm">Como se aciona</div>
   {passos}
  </div>
  <div>
   <div class="eyebrow" style="margin-bottom:3mm">O que o termo cobre</div>
   <div class="term"><div class="k">Marcenaria</div>
    <div class="s">Estrutura, painéis, frentes e acabamento, pelo prazo da linha
     escolhida.</div></div>
   <div class="term"><div class="k">Ferragem de movimento</div>
    <div class="s">Corrediça, dobradiça, articulador e pulsador, pelo prazo da
     linha escolhida.</div></div>
   <div class="term"><div class="k">Montagem e instalação</div>
    <div class="s">As instalações e regulagens têm garantia de dois anos em
     qualquer linha.</div></div>
  </div>
  <div>
   <div class="eyebrow" style="margin-bottom:3mm">O que fica de fora</div>
   <div class="term"><div class="k">Iluminação em LED</div>
    <div class="s">É componente eletrônico e segue a garantia do fabricante.</div></div>
   <div class="term"><div class="k">Desgaste de uso</div>
    <div class="s">Assim como o dano por umidade ou infiltração vinda
     da obra.</div></div>
   <div class="term"><div class="k">Alteração por terceiro</div>
    <div class="s">Feita no móvel depois da entrega. O termo traz também as
     obrigações de conservação do contratante.</div></div>
  </div>
 </div>
 <div class="mos" style="grid-template-columns:repeat(3,1fr);margin-top:auto;
      flex:none;height:52mm">
  <figure><img src="{IMG['suite-master-02']}" alt="">
    <figcaption>Suíte master</figcaption></figure>
  <figure><img src="{IMG['closet-master-02']}" alt="">
    <figcaption>Closet master</figcaption></figure>
  <figure><img src="{IMG['suite01-03']}" alt="">
    <figcaption>Suíte 01</figcaption></figure>
 </div>
</div>''')

# ── 19 · o investimento, ambiente a ambiente, NAS TRÊS LINHAS ───────────
#    ⭐ [Jonathan 30/10] "a apresentação de preços de cada ambiente precisa
#      ser nas três linhas (obs, a despensa e o office não muda de valor)".
#    ⛔⛔ O QUE NÃO MUDA NESSES AMBIENTES É O CUSTO, NÃO O PREÇO. Nenhum
#      deles leva gaveta nem porta de giro, então não há corrediça nem
#      dobradiça para trocar — mas Hettich e Blum fecham a 42% de margem e
#      a telescópica a 35%, e por isso o preço da telescópica cai mesmo
#      ali. A nota da folha afirma só o que a tabela mostra.
#    ⛔⛔ E O EMPATE SAI DA TABELA, NÃO DE UMA LISTA QUE EU ESCREVO. A nota
#      é montada a partir dos próprios preços impressos acima dela: se um
#      ambiente entrar ou sair do empate, a frase muda sozinha.
IGUAIS = [i for i in range(len(cen.AMB))
          if abs(cen.CEN['Hettich']['pv'][i] - cen.CEN['Blum']['pv'][i]) < 0.01]
assert IGUAIS and all(cen.AMB[i][2] == 0 for i in IGUAIS), \
    '⛔ empatou Hettich com Blum num ambiente que TEM corrediça'
assert all(abs(cen.CEN['Hettich']['pv'][i] - cen.CEN['Telescópica']['pv'][i]) > 1.0
           for i in IGUAIS), '⛔ a telescópica não pode empatar: a MC dela é outra'
NOMES = [cen.AMB[i][0][3:] for i in IGUAIS]
EMPATE = (', '.join(NOMES[:-1]) + ' e ' + NOMES[-1]) if len(NOMES) > 1 else NOMES[0]
QUANTOS = {1: 'Um ambiente tem', 2: 'Dois ambientes têm', 3: 'Três ambientes têm',
           4: 'Quatro ambientes têm', 5: 'Cinco ambientes têm',
           6: 'Seis ambientes têm', 7: 'Sete ambientes têm'}[len(NOMES)]


CEL = {}
for _n in LIN:
    _v = [round(x) for x in cen.CEN[_n]['pv']]
    _resto = round(cen.CEN[_n]['preco']) - sum(_v)
    _v[max(range(len(_v)), key=lambda i: _v[i])] += _resto
    assert abs(_resto) <= 3, f'⛔ resíduo grande demais em {_n}: {_resto}'
    assert sum(_v) == round(cen.CEN[_n]['preco'])
    CEL[_n] = _v


def bloco(faixa):
    return ''.join(
        f'<tr><td class="l">{E(cen.AMB[i][0][3:])}</td>'
        + ''.join(f'<td{" class=hi" if n == "Hettich" else ""}>'
                  f'{brs(CEL[n][i])}</td>' for n in LIN)
        + '</tr>' for i in faixa)


folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · ambiente a ambiente</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Dezenove ambientes, nas três linhas.</h1>
 <p class="lead" style="max-width:215mm">Cada ambiente foi levantado <b>peça por
  peça do projeto executivo</b> — nada é rateio nem estimativa por metro quadrado.</p>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:0 10mm;margin-top:5mm">
  <table class="inv">
   <tr><th class="l">Ambiente</th>
    {''.join(f'<th{" class=hi" if n == "Hettich" else ""}>{E(n)}</th>' for n in LIN)}</tr>
   {bloco(range(0, 10))}</table>
  <table class="inv">
   <tr><th class="l">Ambiente</th>
    {''.join(f'<th{" class=hi" if n == "Hettich" else ""}>{E(n)}</th>' for n in LIN)}</tr>
   {bloco(range(10, 19))}
   <tr class="tot"><td class="l">A casa inteira</td>
    {''.join(f'<td{" class=hi" if n == "Hettich" else ""}>'
             f'{brs(cen.CEN[n]["preco"])}</td>' for n in LIN)}</tr></table>
 </div>
 <div class="box" style="margin-top:auto"><p style="font-size:8.4pt">
  <b>{QUANTOS} o mesmo valor nas linhas Hettich e Blum:</b> {E(EMPATE)}.
  Nenhum deles leva gaveta, e <b>entre essas duas linhas o que muda é só a
  corrediça</b> — a dobradiça é a mesma nas duas.</p></div>
</div>''')

# ── 20 · a decisão: as três linhas, um valor cada ───────────────────────
#    ⛔ Sem o resumo do meio, o cartão ficava com meio palmo de branco entre
#      o nome da linha e o valor — e um vazio ali, na folha que decide, lê
#      como falta de assunto.
RESUMO = {
 'Telescópica': 'Trilho aparente na lateral da gaveta e fechamento sem '
                'amortecedor.',
 'Hettich': 'Trilho oculto por baixo, gaveta que sai inteira e fechamento '
            'amortecido. <em>É a linha especificada neste projeto.</em>',
 'Blum': 'O curso mais macio e a maior capacidade de carga das três — é o '
         'que se sente num gavetão cheio.',
}
cards = ''.join(
    f'''<div class="c{" hi" if k == "Hettich" else ""}">
     <div class="anos">{E(cen.CEN[k]['gar'].split()[0])}</div>
     <div class="unid">anos de garantia</div>
     <div class="nm">{E(cen.CEN[k]['chamada'])}</div>
     <div class="x">{RESUMO[k]}</div>
     <div class="l"><div class="k">A casa inteira</div>
      <div class="v" style="font-family:'Cormorant Garamond',Georgia,serif;
           font-size:19pt">{br(cen.CEN[k]['preco'])}</div></div></div>'''
    for k in LIN)
folha(f'''<div class="pad">
 <div class="eyebrow">Investimento · as três linhas</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Dois anos, dez, ou trinta.</h1>
 <p class="lead" style="max-width:215mm">A mesma casa, o mesmo desenho e os mesmos
  padrões. A diferença é a <b>ferragem</b> — e o tempo pelo qual respondemos por ela.</p>
 <div class="gar justo">{cards}</div>
 <div class="box" style="margin-top:5mm"><div class="t">O que está incluso</div>
  <p>Projeto executivo de marcenaria, material, usinagem, ferragem e iluminação
   em LED embutida, mais os ofícios que esta proposta reúne — <b>espelho, vidro
   temperado, serralheria embutida e palhinha natural</b> —, transporte, montagem
   e instalação, num só contrato, com uma só data e uma só arquiteta responsável.
   A pedra é marmoraria e fica fora; a folha de condições nomeia o resto.</p></div>
</div>''')

# ── 21 · os dois ajustes possíveis ──────────────────────────────────────
#    ⭐ [Jonathan 31/10] "Acrescente apenas a versão diferente da cozinha e
#      do painel de muxarabi." Ele tinha mandado tirar na rodada anterior
#      ("não apresentamos o downgrade"); agora entram, numa folha só,
#      DEPOIS do preço cheio — porque continuam sendo alternativa, não
#      proposta.
#    ⛔⛔ E A COZINHA EM MELAMÍNICO NÃO É A MESMA COZINHA MAIS BARATA. A
#      moldura provençal é peça de 6 mm usinada na router e colada sobre a
#      frente: em laca a pintura fecha a junta e ela some; em melamínico o
#      rebaixo da fresa EXPÕE O MIOLO CRU DO MDF e não há como acabar. São
#      catorze frentes. A conta já tirou as molduras — então a folha tem de
#      dizer que a frente fica LISA. É decisão de projeto, não de orçamento,
#      e esconder isso seria vender uma cozinha que não existe.
AJUSTES = [
 ('A cozinha, em melamínico', cen.TROCA[0][1],
  'A laca acetinada sai e entra o <b>MDF melamínico</b>, no padrão que vocês '
  'escolherem com a arquiteta. É a troca que mais pesa no total da casa — '
  'mais do que trocar a ferragem inteira de linha.',
  'A moldura provençal não sobrevive à troca',
  'Ela é uma peça usinada e colada sobre a frente. Na laca, a pintura fecha '
  'a junta e a moldura vira parte do desenho; no melamínico, o rebaixo da '
  'fresa expõe o miolo do MDF e não há acabamento que resolva. A cozinha '
  'passa a ter <b>frente lisa</b>, nas catorze portas e gavetões. É uma '
  'decisão de projeto, não de orçamento — e é por isso que ela está aqui, '
  'e não embutida no preço.'),
 ('O painel do office, usinado', cen.TROCA[1][1],
  'A grade de réguas encaixadas uma a uma em meia-madeira vira um <b>painel '
  'plano, usinado na CNC</b> em chapa inteira. A parede continua vazada e '
  'continua em MDF Nogueira Caiena, de ponta a ponta.',
  'O que sai é a mão de obra, não o desenho',
  'Somem a montagem régua por régua, a fita de cada peça e a filetagem '
  'manual que acabava os topos. O que fica é o mesmo desenho, resolvido '
  'pela máquina em vez da bancada: o relevo é <b>usinado na própria chapa</b> '
  'e não montado peça a peça.'),
]
cards = ''.join(
    f'''<div class="aj"><div class="k">{E(t)}</div>
     <div class="vv">− {br(v)}</div>
     <div class="dd">{d}</div>
     <div class="box" style="margin-top:4mm"><div class="t">{E(av)}</div>
       <p>{ad}</p></div></div>''' for t, v, d, av, ad in AJUSTES)

ESTADOS = [('Como está no projeto', []),
           ('Com a cozinha em melamínico', [0]),
           ('Com o painel do office usinado', [1]),
           ('Com os dois ajustes', [0, 1])]
#    ⛔ O preço de cada combinação sai de `mc_apos`, que é a mesma conta da
#      planilha — e o assert de `cenarios.py` já provou que nenhuma das doze
#      combinações fura o piso de 35%.
linhas_aj = ''.join(
    f'<tr{" class=tot" if not c else ""}><td class="l">{E(rot)}</td>'
    + ''.join(f'<td{" class=hi" if n == "Hettich" else ""}>'
              f'{brs(cen.mc_apos(n, c)[1])}</td>' for n in LIN)
    + '</tr>' for rot, c in ESTADOS)
for _n in LIN:
    for _c in ([], [0], [1], [0, 1]):
        assert cen.mc_apos(_n, _c)[0] >= 0.35 - 1e-9, (_n, _c)

folha(f'''<div class="pad apertada"><div class="fitp">
 <div class="eyebrow">Investimento · dois ajustes possíveis</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Dois lugares onde a casa<br>aceita uma execução mais curta.</h1>
 <p class="lead" style="max-width:215mm">Os valores das folhas anteriores são o
  <b>projeto como a arquiteta desenhou</b>. Há dois pontos — e só dois — em que
  a execução admite uma versão mais simples sem mexer em mais nada da casa. Um
  deles <b>muda o desenho</b>, e isso está dito abaixo.</p>
 <div class="ajs">{cards}</div>
 <table class="inv" style="margin-top:6mm">
  <tr><th class="l">A casa inteira</th>
   {''.join(f'<th{" class=hi" if n == "Hettich" else ""}>{E(n)}</th>' for n in LIN)}</tr>
  {linhas_aj}
 </table>
</div></div>''')

# ── 22 · condições ──────────────────────────────────────────────────────
#    ⭐⭐ [Jonathan 30/10, três vezes] "não coloque parcelamento, nada de
#      cartão. Repita a mesma forma de pagamento do Michel." É esta, e ela
#      é a do caderno do ICA: quatro parcelas por transferência bancária.
PAGTO = [('Entrada, na assinatura do contrato', '30%'),
         ('30 dias após a assinatura', '20%'),
         ('60 dias após a assinatura', '20%'),
         ('90 dias após a assinatura', '30%')]
assert sum(int(p[:-1]) for _r, p in PAGTO) == 100, '⛔ o pagamento não fecha 100%'
pay = ''.join(f'<tr><td>{E(r)}</td><td class="d">{E(p)}</td></tr>' for r, p in PAGTO)
folha(f'''<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">Condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 3mm">Prazo, pagamento e fronteiras.</h1>
 <div class="three">
  <div>
   <div class="term"><div class="k">Validade desta proposta</div>
     <div class="v">{E(VALIDADE)}</div>
     <div class="s">A partir desta data.</div></div>
   <div class="term"><div class="k">Prazo de execução</div>
     <div class="v">{E(PRAZO)}</div>
     <div class="s">Contados da aprovação do detalhamento de execução, não da
       assinatura. A medição técnica entra antes e tem data própria no
       cronograma.</div></div>
   <div class="term"><div class="k">Garantia</div><div class="v">Conforme a linha</div>
     <div class="s">Trinta anos na linha Blum, dez na Hettich e dois na telescópica,
       sobre a marcenaria e a ferragem. Instalação e regulagem, dois anos. Termo
       assinado na entrega.</div></div>
   <div class="term"><div class="k">Projeto executivo de marcenaria</div>
     <div class="v">Incluso</div>
     <div class="s">Aprovado por vocês e pela {E(ARQ.split()[0])} {E(ARQ.split()[1])}
       antes de qualquer corte.</div></div>
  </div>
  <div>
   <table class="pay" style="width:100%">
    <tr><td colspan="2" style="border:none;padding-bottom:2mm">
      <span class="eyebrow">Formas de pagamento</span></td></tr>
    {pay}
   </table>
   <div style="font-size:7.4pt;color:var(--mut);margin-top:2.5mm;letter-spacing:.06em">
     Todas as parcelas por transferência bancária.</div>
   <div class="box" style="margin-top:5mm"><div class="t">Um interlocutor</div>
    <p>Da aprovação à entrega, vocês tratam com a arquiteta responsável pelo projeto.
       Um contrato, uma data, um nome para chamar.</p></div>
  </div>
  <div class="fora">
   <div class="eyebrow" style="margin-bottom:3mm">O que não está nesta proposta</div>
   <ul>
    <li><div class="k">Pedra</div><div class="v">Bancadas, rodobancas, sóculos,
      soleiras e a cuba esculpida do lavabo são marmoraria e não entram no escopo
      da Valvic.</div></li>
    <li><div class="k">Eletrodomésticos e metais</div><div class="v">Cooktop, forno,
      coifa, geladeira, lava-louças, cubas, torneiras e louças.</div></li>
    <li><div class="k">Obra civil e instalações</div><div class="v">Alvenaria,
      elétrica — pontos, circuitos, drivers e interruptores —, esquadrias, forro,
      piso e pintura de parede. O corpo de alvenaria da ilha da varanda.</div></li>
    <li><div class="k">Decoração</div><div class="v">Mobiliário solto, cortinas,
      tapetes, objetos e quadros.</div></li>
    <li><div class="k">A confirmar antes da produção</div><div class="v">A medição
      no local, que fecha a altura do piso ao forro. A cristaleira da varanda, que
      a planta desenha curva e a elevação desenha reta. O forno e o micro-ondas,
      para a torre da cozinha. E amostra dos padrões de MDF e da cor da laca.</div></li>
   </ul>
  </div>
 </div>
 <div class="sig"><div class="ln">{E(CLIENTE)}</div>
   <div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

# ── 22 · encerramento ───────────────────────────────────────────────────
fim = TXT['encerramento']
folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome" style="font-size:36pt">
    {'<br>'.join(E(x.strip()) for x in fim['titulo'].split('|'))}</div>
  <div class="cv-s">{E(fim['subtitulo'])}</div>
  <div class="cv-meta">
   <div><div class="k">Proposta</div><div class="v">{E(CLIENTE)}</div></div>
   <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG['closet-master-01']}" alt=""></div>
</div>''', dark=True, rodape=False)

EXTRA = '''
/* ── o processo: doze etapas em quatro blocos, num trilho só ─────────── */
.rail{height:1.5px;background:linear-gradient(90deg,var(--gold),var(--gold-lt) 70%,var(--hair));
      margin:0;flex:none}
.proc{display:grid;grid-template-columns:repeat(4,1fr);gap:0 7mm;flex:1;min-height:0;
      margin-top:-1px;overflow:hidden;align-content:start;align-items:start}
.proc .pb{transform-origin:top left}
.pb{border-left:1px solid var(--hair);padding:5mm 5mm 0 5mm}
.pb:first-child{border-left:none;padding-left:0}
.pb-h{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;color:var(--gold);
      font-weight:700}
.pb-s{font-size:7.6pt;color:var(--mut);margin:1mm 0 3.4mm;min-height:6mm;line-height:1.35}
.pe{position:relative;padding:0 0 3.2mm 0}
.pe-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;color:var(--gold-lt);
      line-height:1;float:right;margin-left:3mm}
.pe-k{font-size:6pt;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);
      font-weight:700}
.pe-t{font-size:9.6pt;font-weight:700;margin:.6mm 0 1mm;letter-spacing:-.006em}
.pe-l{font-size:7.8pt;color:var(--soft);line-height:1.46}
.pe-e{font-size:7.1pt;color:var(--mut);margin-top:1.4mm;padding-left:3mm;
      border-left:1.5px solid var(--gold-pale);line-height:1.38}

/* ── a coluna de texto do ambiente encolhe até caber na folha ────────── */
.amb-txt{overflow:hidden;padding-bottom:19mm}
.amb-txt.curto{justify-content:center;padding-bottom:22mm}
.amb-txt.curto .fit{margin-bottom:6mm}
.amb-txt .fit{transform-origin:top left}
.ambw .low{flex:1;min-height:0;overflow:hidden}
.ambw .low .fitw{transform-origin:top left}

/* ── índice ───────────────────────────────────────────────────────────── */
.ix{display:grid;grid-template-columns:9mm 46mm 1fr;align-items:baseline;gap:2mm;
    padding:2.25mm 0;border-bottom:1px solid var(--hair)}
.ix-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:11pt;color:var(--gold-lt)}
.ix-t{font-size:9.4pt;font-weight:600}
.ix-d{font-size:7.4pt;color:var(--mut);text-align:right}

/* ── ajustes do caderno ───────────────────────────────────────────────── */
/* o .foot é absoluto e o fio dele cai a 13,9mm do pé; o padding de 12mm do
   css da casa deixava a caixa de conteúdo passar por baixo do fio. */
.pad{padding-bottom:20mm}
/* a calha entre as colunas: sem ela o número encostava na tarja da Hettich */
.inv td, .inv th{padding-left:3.4mm}
.inv td.l, .inv th.l{padding-left:0}
/* a cauda do "3" do algarismo antigo cruzava a linha de baixo, só na Blum */
.gar .anos{padding-bottom:2.2mm}
/* cartão na altura do conteúdo: o vazio sai de dentro dele e vai para o pé */
.gar.justo{flex:none}
.gar.justo .c{padding-bottom:6mm}
.gar.justo .l{margin-top:5mm}

/* ── os dois ajustes: dois blocos lado a lado ─────────────────────────── */
.pad.apertada{overflow:hidden}
.pad.apertada .fitp{transform-origin:top left;width:100%}
.ajs{display:grid;grid-template-columns:1fr 1fr;gap:9mm;margin-top:6mm}
.aj{border-top:1.5px solid var(--gold);padding-top:4mm}
.aj .k{font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;
       line-height:1.1;font-weight:500}
.aj .vv{font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt;
        color:var(--gold);line-height:1;margin-top:2mm}
.aj .dd{color:var(--soft);font-size:8.4pt;margin-top:2.5mm;line-height:1.5}
.aj .box{margin-top:4mm}

/* ── comparativo das três linhas ──────────────────────────────────────── */
.cmp{width:100%;border-collapse:collapse}
.cmp th{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);
        font-weight:700;text-align:center;padding:0 4mm 3mm;border-bottom:1px solid var(--line)}
.cmp th.hi{background:var(--gold-pale);color:var(--gold)}
.cmp td{padding:3mm 4mm;border-bottom:1px solid var(--hair);text-align:center;font-size:9.6pt;
        vertical-align:top}
.cmp td.l{text-align:left;color:var(--gold);font-size:6.6pt;letter-spacing:.2em;
          text-transform:uppercase;font-weight:700;padding-top:3.6mm;width:24mm}
.cmp td.hi{background:var(--gold-pale)}

/* ── a faixa de imagens da folha de ambiente ──────────────────────────── */
.ambw .band img{flex:1;min-width:0}
'''

AJUSTE = '''
  const encolhe = (caixa, alvo, piso) => {
    const f = caixa.querySelector(alvo); if (!f) return;
    f.style.zoom = 1;
    const cs = getComputedStyle(caixa);
    const alt = caixa.clientHeight - parseFloat(cs.paddingTop)
                                   - parseFloat(cs.paddingBottom);
    const pede = f.scrollHeight;
    if (pede > alt) f.style.zoom = Math.max(piso, alt / pede);
  };
  const MM = 96 / 25.4;
  const sobra = (low, f) => {
    const cs = getComputedStyle(low);
    return low.clientHeight - parseFloat(cs.paddingTop)
                            - parseFloat(cs.paddingBottom) - f.scrollHeight;
  };
  // ⭐ quem cede é a FOTO, não o corpo do texto: o caderno tem de ter um
  //   tamanho de letra só, e a faixa é que desce até a lista caber.
  const caberBanda = (w) => {
    const band = w.querySelector('.band'), low = w.querySelector('.low'),
          f = low && low.querySelector('.fitw');
    if (!band || !f) return;
    f.style.zoom = 1;
    const piso = 62 * MM;
    for (let i = 0; i < 30; i++) {
      const s = sobra(low, f);
      if (s >= 0) break;
      const h = band.getBoundingClientRect().height;
      if (h <= piso) break;
      band.style.height = Math.max(piso, h + s - 1) + 'px';
    }
    // ⛔ E SE NEM COM OS DOIS COUBER, A FAIXA CEDE O RESTO. Sem este
    //   terceiro passo o bloco estourava o padding e o `overflow:hidden`
    //   o cortava só na borda da folha — a barrinha do bloco de
    //   acabamentos saía por baixo do fio do rodapé, 1,6 mm de sujeira
    //   que só aparece com lupa e que eu já tinha dado por resolvida uma
    //   vez sem medir.
    let s = sobra(low, f);
    if (s < 0) {
      f.style.zoom = Math.max(.90, (low.clientHeight + s) / low.clientHeight);
      const chao = 48 * MM;
      for (let i = 0; i < 30; i++) {
        s = sobra(low, f);
        if (s >= 0) break;
        const h = band.getBoundingClientRect().height;
        if (h <= chao) break;
        band.style.height = Math.max(chao, h + s - 1) + 'px';
      }
    }
  };
  const caber = () => {
    // ⛔ a coluna ENTREGA leva quatro etapas e transbordava a caixa: o
    //   `overflow:hidden` não resolvia, só cortava o fio divisor na borda
    //   da folha, 1,9mm por baixo do rodapé. Encolhe na origem.
    document.querySelectorAll('.proc').forEach(pr => {
      pr.style.zoom = 1;
      if (pr.scrollHeight > pr.clientHeight)
        pr.style.zoom = Math.max(.85, pr.clientHeight / pr.scrollHeight);
    });
    document.querySelectorAll('.amb-txt').forEach(c => encolhe(c, '.fit', .62));
    document.querySelectorAll('.pad.apertada').forEach(c => encolhe(c, '.fitp', .80));
    document.querySelectorAll('.ambw').forEach(caberBanda);
  };
'''

HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Proposta · {E(CLIENTE)}</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@'
        '9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
        f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S)
        + f'<script>{AJUSTE}caber();</script></body></html>')

# ── as travas ───────────────────────────────────────────────────────────
assert len(S) == NF, f'⛔ {len(S)} folhas, o rodapé diz {NF}'

# ⛔⛔ "NUNCA APRESENTE PREÇO SEM ANTES GERAR VALOR" — a trava, não a boa fé.
_antes = ''.join(S[:N0 - 1])
assert 'R$' not in _antes, '⛔⛔ TEM PREÇO ANTES DA FOLHA DE VALOR'

# ⛔ AS TRAVAS DE TEXTO LEEM O TEXTO, NÃO O HTML COM AS IMAGENS DENTRO.
#   Cada render entra como base64, e numa peça de megabytes qualquer
#   sequência curta de letras aparece por acaso lá dentro: a trava de
#   "ICA" dispararia no meio de uma foto. Tiro os data: URIs primeiro.
_texto = re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S))
_texto = re.sub(r'<[^>]+>', ' ', _texto)

# ⛔⛔ NADA DE CARTÃO E NADA DE DESCONTO. O Jonathan pediu três vezes; agora
#   é assert. A forma de pagamento é a do caderno de referência: quatro
#   parcelas por transferência, e só.
for _p in ('cartão', 'cartao', 'parcelamento', 'desconto', 'valor cheio',
           'valor de tabela'):
    assert _p.lower() not in _texto.lower(), f'⛔⛔ A PEÇA FALA EM "{_p}"'

# ⛔ "à vista" e "vezes" são português comum nas descrições de móvel — o
#   fundo que fica à vista, o puxador à vista. Só são proibidos na folha
#   de condições, onde seriam escada de desconto.
_cond = re.sub(r'<[^>]+>', ' ', S[NF - 2])
for _p in ('à vista', 'vezes', '%'):
    assert _p not in _cond.replace('30%', '').replace('20%', ''), \
        f'⛔⛔ ESCADA DE DESCONTO NA FOLHA DE CONDIÇÕES: "{_p}"'

# ⛔⛔ NENHUM VESTÍGIO DE OUTRO CLIENTE. "Não pode haver informações
#   relacionadas ao orçamento do Michell, é outro cliente" — e o caderno
#   dele foi a referência de layout, então o risco é real.
for _c in ('Michell', 'Michelle', 'Jéssica', 'Jessica', 'Arlei', 'Iara Cezar',
           'Lagoa Santa'):
    assert _c not in _texto, f'⛔⛔ VESTÍGIO DE OUTRO CLIENTE NA PEÇA: {_c}'

# ⛔⛔ MARCAÇÃO INTERNA NÃO VAI PARA O CLIENTE. ⭐/⛔/⚠ são a minha linguagem
#   de orçamento; impressas, viram emoji vermelho no meio da frase.
_marca = [c for c in '⭐⛔⚠' if c in ''.join(S)]
assert not _marca, f'⛔⛔ MARCAÇÃO INTERNA NA PEÇA DO CLIENTE: {_marca}'

# ⛔ E nenhuma imagem reprovada na triagem pode ter entrado.
for _c in CORTADAS:
    assert IMG[_c] not in HTML, f'⛔⛔ IMAGEM REPROVADA NA PEÇA: {_c}'

(P / 'proposta-gustavo-raposo.html').write_text(HTML, encoding='utf-8')
subprocess.run(['node', str(P / 'render-pdf.js'),
                str(P / 'proposta-gustavo-raposo.html'),
                str(P / 'proposta-gustavo-raposo.pdf')], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'proposta-gustavo-raposo.pdf · {NF} folhas · A4 paisagem · '
      f'{(P / "proposta-gustavo-raposo.pdf").stat().st_size // 1024} kB · '
      f'primeiro preço na folha {N0}')
for n in LIN:
    print(f'  {n:13s} {br(cen.CEN[n]["preco"]):>16s} · {cen.CEN[n]["gar"]}')
