# -*- coding: utf-8 -*-
"""GUSTAVO RAPOSO — proposta · casa completa  [30/10/2026]

⭐ Mesmo layout do `build-michelle-arlei.py`, que o Jonathan cravou em 19/10:
   > "NUNCA APRESENTE PREÇO SEM ANTES GERAR VALOR na proposta. Fale um pouco
   >  da empresa e dos processos antes de expor valores. Mostre as duas
   >  linhas antes, fale das diferenças. (...) Descreva os itens junto com a
   >  listagem dos ambientes, só listando item por item mesmo."

   Aqui são TRÊS linhas, não duas, e há DUAS TROCAS de ambiente no fim.
⛔ Sem metragem e sem contagem em nenhuma descrição.
⛔⛔ Nenhum número vem digitado: tudo sai de `gustavo-raposo/cenarios.py`.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('cen', P/'gustavo-raposo'/'cenarios.py')
cen = importlib.util.module_from_spec(spec); sys.modules['cen'] = cen
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(cen)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, OBRA = 'Gustavo Raposo', 'Condomínio Vale dos Pinhais · Nova Lima'
ARQ, DATA = 'Luiza Pacheco Arquitetura', '30 de outubro de 2026'
PRAZO, VALIDADE = '120 dias corridos', '7 dias úteis'
NP = 16                      # páginas · o assert no fim confere
N0 = 13                      # ⛔ a primeira página com preço

def uri(n):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img-gustavo-raposo'/n).read_bytes()).decode())
IMG = {n.stem: uri(n.name) for n in sorted((P/'img-gustavo-raposo').iterdir())}

# ── os ambientes: imagens e LISTA ITEM A ITEM ───────────────────────────
#    (título, imagens, tags, acabamento, [(móvel, descrição)])
PG = [
 ('A varanda.', ['varanda-01', 'varanda-02'], ['Varanda'],
  'Nogueira Caiena da linha Design, com interno em branco.',
  [('Armário da parede',
    'Corre a parede inteira, com portas de giro e gavetas sob a bancada de '
    'pedra. A caixaria recebe a travessa que sustenta o granito.'),
   ('Gaveteiro da ilha',
    'Embutido na ilha de alvenaria, com gavetas e porta-temperos vertical '
    'de altura cheia ao lado do forno.'),
   ('Cristaleira',
    'Portas de vidro temperado em cima e de madeira embaixo, com prateleiras '
    'reforçadas por alma de aço e fundo na cor — atrás do vidro não existe '
    'peça escondida.')]),

 ('A cozinha, a despensa<br>e o lavabo.',
  ['cozinha-01', 'cozinha-02', 'cozinha-03'], ['Cozinha', 'Despensa', 'Lavabo'],
  'Laca acetinada Sayerlack sobre MDF cru, com interno em branco.',
  [('Armário superior',
    'Portas de giro com moldura usinada na própria peça e perfil de luz '
    'correndo por baixo.'),
   ('Nicho sobre a geladeira',
    'Aberto, então sai lacado por dentro também — ali tudo aparece.'),
   ('Armário inferior',
    'Gavetões de carga sob a bancada, com frente de moldura provençal.'),
   ('Armário da bancada do cooktop',
    'Gaveta de talheres, gavetas e báscula com articulador que sobe sozinho '
    'e para onde a mão soltar.'),
   ('Prateleiras da despensa',
    'As duas paredes da despensa, em prateleiras de vão livre com alma de '
    'aço onde o vão pede.'),
   ('Espelho do lavabo',
    'Espelho prata colado, dividido pela bancada de pedra — a folha de cima '
    'e a de baixo, cortadas, transportadas e instaladas por nós.')]),

 ('A lavanderia<br>e a rouparia.', ['lavanderia-01', 'lavanderia-02', 'rouparia-01'],
  ['Lavanderia', 'Rouparia'],
  'Branco TX na caixaria, com frentes na cor do ambiente.',
  [('Armário superior da lavanderia',
    'Fecha a parede acima das máquinas, com básculas que liberam a vista '
    'inteira do vão quando abrem.'),
   ('Armário inferior',
    'Sob a bancada, com gavetões para o que é pesado e porta de giro para '
    'o resto.'),
   ('Torre de vassouras',
    'Altura cheia, para o que não cabe deitado — e é ela que tira o esfregão '
    'de trás da porta.'),
   ('Armário da rouparia',
    'A rouparia inteira da circulação, em portas de giro, com prateleiras '
    'que vencem o vão sem flecha.')]),

 ('O office.', ['office-01', 'office-muxarabi', 'office-02'], ['Office'],
  'Nogueira Caiena, em grade de réguas encaixadas.',
  [('Painel muxarabi em grade de réguas',
    'Não é painel furado: são réguas inteiras cruzando umas nas outras em '
    'meia-madeira, cada uma perdendo metade da largura no encontro para que '
    'as duas fiquem niveladas. A espessura da chapa é a ripa que se vê de '
    'frente, e a largura da régua é a profundidade do painel. É o móvel que '
    'mais pede mão nesta casa.')]),

 ('A suíte master.',
  ['suite-master-01', 'closet-master-01', 'banho-master-01'],
  ['Suíte', 'Closet', 'Banho'],
  'Nogueira Caiena nas faces, branco no interno do closet.',
  [('Painel da cabeceira',
    'Painel ripado atrás da cama, com as mesas de cabeceira nascendo dele.'),
   ('Porta pivotante mimetizada',
    'Uma folha com duas caras: do quarto ela some no painel, do closet ela '
    'é a porta. Pivô de piso e teto, porque a folha pesa.'),
   ('Armário da suíte',
    'Portas de giro com puxador cava usinado na própria peça.'),
   ('Armário do closet',
    'Os dois lados do closet, com gaveteiro interno, cabideiro em dois '
    'níveis e sapateira.'),
   ('Bandeira sobre a porta',
    'Fecha o vão acima da pivotante até o forro, sem frestas.'),
   ('Armário do banho com portas de espelho',
    'Espelho de alumínio correndo sobre a bancada, que é porta e é espelho '
    'ao mesmo tempo.'),
   ('Gabinete suspenso',
    'Sob a bancada de pedra, solto do piso para a limpeza passar por baixo.')]),

 ('A suíte dos filhos.', ['suite01-01', 'suite01-02', 'suite01-03'],
  ['Suíte 01', 'Banho'],
  'Painéis frisados na cor da suíte, com interno em branco.',
  [('Painel de cabeceira frisado',
    'Frisos verticais usinados de ponta a ponta, subindo a parede inteira.'),
   ('Armários do quarto',
    'Dois armários e o módulo de canto que os une em L — o canto é item '
    'próprio, para não ser contado duas vezes.'),
   ('Mesa suspensa',
    'Corre sob a janela, sem pé, apoiada na estrutura da parede.'),
   ('Gaveteiro com rodízios',
    'Solto embaixo da mesa, e são os rodízios que dão o vão até o chão.'),
   ('Bases de cama',
    'Duas bases com estrado em metalon, dimensionadas para colchão de '
    'solteiro.'),
   ('Gabinete do banho',
    'Suspenso sob a bancada, com espelho colado na folha de correr.')]),

 ('A suíte das filhas.', ['suite02-01', 'suite02-02', 'banho02-01'],
  ['Suíte 02', 'Closet', 'Banho'],
  'Painéis e estante na cor da suíte, com canto arredondado.',
  [('Estante e armário de canto arredondado',
    'O canto da estante sai curvo, usinado, não montado em esquadro.'),
   ('Painéis de parede',
    'Frisos usinados nos dois painéis que ladeiam as camas.'),
   ('Porta pivotante mimetizada',
    'Mesma solução da master: some na parede do quarto e é porta do lado '
    'do closet.'),
   ('Penteadeira',
    'Corre a parede com gavetas, e o tampo recebe o espelho redondo.'),
   ('Armários do closet',
    'Os dois lados mais o módulo de canto em L.'),
   ('Mesa de cabeceira',
    'Entre as duas camas, nascendo do painel.'),
   ('Bases de cama',
    'Duas bases com estrado em metalon.')]),

 ('Hóspedes<br>e banho social.',
  ['hospedes-01', 'hospedes-02', 'banho-social-01'],
  ['Suíte hóspedes', 'Banho hóspedes', 'Banho social'],
  'Nogueira Caiena nas frentes, branco no interno.',
  [('Armário da suíte de hóspedes',
    'Portas de correr com sistema sem amortecedor, como a prancha pede, e '
    'interno dividido em cabideiro e prateleira.'),
   ('Gabinete do banho de hóspedes',
    'Suspenso sob a bancada de pedra.'),
   ('Gabinete do banho social',
    'Mesma solução, na cor do ambiente.')]),

 ('O homeschooling.', ['homeschooling-01', 'homeschooling-02'], ['Homeschooling'],
  'Azul Secreto nos nichos, com armários na cor da casa.',
  [('Nicho em Azul Secreto',
    'A estante de estudo, com prateleiras de vão livre reforçadas por alma '
    'de aço — prateleira de vão longo carregada de livro flecha no meio, e '
    'ali isso se vê de longe.'),
   ('Armário inferior',
    'Fecha a base da parede, com gavetões para material.'),
   ('Armário da outra parede',
    'Portas de giro de altura cheia, para o que precisa sumir da vista.')]),
]

# ⭐ O CSS é o do Michelle e Arlei, sem uma vírgula de diferença — é o layout
#   que o Jonathan aprovou. O que acrescento são só as variações de TRÊS
#   colunas, porque aqui são três linhas de ferragem e não duas.
CSS = """
:root{
  --ink:#1E1B17; --soft:#5E574E; --mut:#9A9287; --line:#E0D8CB;
  --hair:#EFE9DF; --sand:#F6F1E8; --wood:#A8794A; --wood-lt:#D9BD96;
  --dk:#262220; --paper:#fff;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);
     font-size:9.5pt;line-height:1.55;}
.serif{font-family:'Cormorant Garamond',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;
      background:var(--paper);page-break-after:always;}
.page:last-of-type{page-break-after:avoid;}
.pad{padding:15mm 17mm 14mm;height:100%;display:flex;flex-direction:column;}
.foot{margin-top:auto;padding-top:6mm;border-top:1px solid var(--hair);
      display:flex;justify-content:space-between;font-size:6.8pt;
      letter-spacing:.18em;text-transform:uppercase;color:var(--mut);flex:none;}
.hd{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1.4px solid var(--ink);padding-bottom:3mm;flex:none;}
.hd .b{font-size:7.6pt;letter-spacing:.4em;text-transform:uppercase;font-weight:700;}
.hd .m{font-size:6.8pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.eye{font-size:6.8pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--wood);font-weight:700;margin-top:5mm;flex:none;}
.h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:27pt;
  line-height:1.03;font-weight:600;letter-spacing:-.02em;margin-top:1.5mm;flex:none;}
.lead{color:var(--soft);font-size:9.6pt;line-height:1.5;margin-top:3mm;
  max-width:132mm;flex:none;}
.lead b{color:var(--ink);font-weight:600;}

/* ── capa ───────────────────────────────────────────────────────────── */
.cv{height:297mm;display:flex;flex-direction:column;}
.cv .ph{flex:1;overflow:hidden;line-height:0;background:#000;}
.cv .ph img{width:100%;height:100%;object-fit:cover;}
.cv .bt{background:var(--dk);color:#F4EFE6;padding:13mm 17mm 12mm;flex:none;}
.cv .mark{font-size:8pt;letter-spacing:.42em;text-transform:uppercase;
  color:#EFE6D6;font-weight:700;}
.cv h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:42pt;
  line-height:1;font-weight:600;letter-spacing:-.02em;margin:5mm 0 0;}
.cv .sub{font-size:10.5pt;color:#C6BDB0;margin-top:4mm;font-weight:300;}
.cv .sub b{color:#EFE7DA;font-weight:500;}

/* ── mosaico: fotos MENORES, composição assimétrica que alterna ─────── */
.mos{margin:6mm -17mm 0;display:grid;gap:2mm;line-height:0;overflow:hidden;
  flex:1 1 auto;min-height:68mm;max-height:128mm;}
.mos img{width:100%;height:100%;object-fit:cover;display:block;}
.mos.a{grid-template-columns:118mm 1fr;}
.mos.b{grid-template-columns:1fr 118mm;}
.mos .st{display:grid;grid-template-rows:1fr 1fr;gap:2mm;}
.mos.solo{grid-template-columns:1fr;}

/* ── lista item a item ──────────────────────────────────────────────── */
.lista{margin-top:7mm;columns:2;column-gap:10mm;flex:none;}
.li{break-inside:avoid;padding:3.6mm 0 3.6mm 5mm;border-left:2px solid var(--wood-lt);
  margin-bottom:3mm;}
.acab{margin-top:6mm;padding-top:4mm;border-top:1px solid var(--line);
  display:flex;align-items:baseline;gap:6mm;flex:none;}
.acab .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;flex:none;}
.acab .v{font-size:9pt;color:var(--soft);}
.acab .v b{color:var(--ink);font-weight:600;}
.li .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;
  font-weight:600;line-height:1.1;letter-spacing:-.01em;}
.li .d{color:var(--soft);font-size:8.2pt;line-height:1.42;margin-top:1.2mm;}
.tags{margin-top:5mm;display:flex;gap:3mm;flex-wrap:wrap;flex:none;}
.tags span{font-size:6.6pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--wood);font-weight:700;border:1px solid var(--line);
  border-radius:20px;padding:1.6mm 4mm;}

/* ── empresa e processo ─────────────────────────────────────────────── */
.duo{display:grid;grid-template-columns:1fr 1fr;gap:9mm;margin-top:7mm;flex:none;}
.step{display:grid;grid-template-columns:9mm 1fr;gap:4mm;padding:3.4mm 0;
  border-top:1px solid var(--line);}
.step:first-of-type{border-top:1.4px solid var(--ink);}
.step .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  font-weight:700;color:var(--wood-lt);line-height:.9;}
.step .t{font-size:10.5pt;font-weight:600;}
.step .d{color:var(--soft);font-size:8.2pt;line-height:1.42;margin-top:.8mm;}
.sel{background:var(--sand);border-radius:3px;padding:8mm;flex:none;}
.sel .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.sel .d{color:var(--soft);font-size:8.6pt;line-height:1.5;margin-top:2mm;}
.sel .d b{color:var(--ink);font-weight:600;}

/* ── as duas linhas ─────────────────────────────────────────────────── */
.vs{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:6mm;flex:none;}
.vs .c{border:1px solid var(--line);border-radius:3px;padding:9mm 8mm 8mm;}
.vs .c.on{background:var(--dk);border-color:var(--dk);color:#F4EFE6;}
.vs .k{font-size:6.8pt;letter-spacing:.24em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.vs .c.on .k{color:var(--wood-lt);}
.vs .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:20pt;
  font-weight:600;margin-top:2mm;line-height:1.05;}
.vs .g{font-family:'Cormorant Garamond',Georgia,serif;font-size:36pt;
  font-weight:700;line-height:1;margin-top:4mm;letter-spacing:-.02em;}
.vs .gl{font-size:7.2pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--mut);font-weight:700;margin-top:1.5mm;}
.vs .c.on .gl{color:#9A9287;}
.vs .p{margin-top:5mm;padding-top:4mm;border-top:1px solid var(--line);
  font-size:9pt;color:var(--soft);}
.vs .c.on .p{border-top:1px solid rgba(255,255,255,.2);color:#BDB5A8;}
.vs .p b{font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;
  font-weight:700;color:var(--ink);display:block;margin-top:1mm;
  font-variant-numeric:tabular-nums;}
.vs .c.on .p b{color:#fff;}
.dif{margin-top:6mm;flex:none;}
.dif .r{display:grid;grid-template-columns:30mm 1fr 1fr;gap:6mm;
  padding:4.2mm 0;border-top:1px solid var(--line);align-items:baseline;}
.dif .r:first-child{border-top:1.4px solid var(--ink);}
.dif .k{font-size:6.8pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.dif .a{color:var(--soft);font-size:8.8pt;}
.dif .b2{font-size:8.8pt;font-weight:600;}

/* ── valores ────────────────────────────────────────────────────────── */
.rows{margin-top:6mm;flex:none;}
.row{display:flex;justify-content:space-between;align-items:baseline;
  padding:2.4mm 0;border-top:1px solid var(--line);font-size:10pt;}
.row:first-child{border-top:1.4px solid var(--ink);}
.row .v{font-variant-numeric:tabular-nums;font-weight:600;}
.vista{margin-top:7mm;background:var(--dk);color:#F4EFE6;border-radius:3px;
  padding:9mm;display:flex;justify-content:space-between;
  align-items:flex-end;gap:8mm;flex:none;}
.vista .lab{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--wood-lt);font-weight:700;}
.vista .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:44pt;
  font-weight:700;color:#fff;line-height:.9;letter-spacing:-.03em;
  margin-top:3mm;font-variant-numeric:tabular-nums;}
.vista .s{font-size:9pt;color:#C2BAAD;margin-top:3mm;}
.vista .rt{text-align:right;flex:none;}
.vista .rt .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:#8E867A;font-weight:700;}
.vista .rt .v{font-size:15pt;color:#B6AEA1;margin-top:1.5mm;
  font-variant-numeric:tabular-nums;}
.pay{margin-top:6mm;flex:none;}
.pay .r{display:flex;justify-content:space-between;align-items:baseline;gap:6mm;
  padding:2.6mm 0;border-top:1px solid var(--line);font-size:9.2pt;color:var(--soft);}
.pay .r:first-child{border-top:1.4px solid var(--ink);}
.pay .r b{color:var(--ink);font-weight:600;}
.pay .r .x{flex:none;font-size:8.6pt;letter-spacing:.06em;color:var(--wood);
  font-weight:700;}
.pay .r.on{color:var(--ink);}
.pay .r.on .x{font-size:10pt;}

/* ── condições ──────────────────────────────────────────────────────── */
.four{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:6mm;
  padding-top:4mm;border-top:1.4px solid var(--ink);flex:none;}
.four .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.four .v{font-size:11pt;font-weight:600;margin-top:1.2mm;}
.four .s{color:var(--soft);font-size:7.6pt;margin-top:.8mm;line-height:1.35;}
.notes{margin-top:6mm;display:grid;grid-template-columns:1fr 1fr;gap:4mm;
  flex:none;}
.notes .bx{background:var(--sand);border-radius:3px;padding:5.5mm 6mm;}
.notes .bx.w{background:#fff;border:1px solid var(--line);}
.notes .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--wood);font-weight:700;}
.notes .d{color:var(--soft);font-size:8pt;line-height:1.45;margin-top:2mm;}
.notes .d b{color:var(--ink);font-weight:600;}
"""

EXTRA = """
/* ── TRÊS linhas em vez de duas ─────────────────────────────────────── */
.vs.tri{grid-template-columns:repeat(3,1fr);gap:3mm;}
.vs.tri .c{padding:7mm 6mm 6mm;}
.vs.tri .n{font-size:15pt;}
.vs.tri .g{font-size:27pt;margin-top:3mm;}
.vs.tri .p b{font-size:14pt;}
.dif.tri .r{grid-template-columns:24mm 1fr 1fr 1fr;gap:4mm;}
.dif.tri .a,.dif.tri .b2{font-size:8.2pt;}
.dif.tri .c3{font-size:8.2pt;font-weight:600;}
/* ── as trocas ──────────────────────────────────────────────────────── */
.tr{margin-top:6mm;flex:none;}
.tr .r{display:grid;grid-template-columns:1fr 34mm;gap:6mm;align-items:baseline;
  padding:4.5mm 0;border-top:1px solid var(--line);}
.tr .r:first-child{border-top:1.4px solid var(--ink);}
.tr .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;
  font-weight:600;line-height:1.1;}
.tr .d{color:var(--soft);font-size:8.4pt;line-height:1.42;margin-top:1mm;}
.tr .v{text-align:right;font-variant-numeric:tabular-nums;font-size:16pt;
  font-weight:600;color:var(--wood);}
.rows.two{columns:2;column-gap:9mm;}
.rows.two .row{break-inside:avoid;}
"""

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · {OBRA}</span><span>{n} / {NP}</span></div>')
def head():
    return (f'<div class="hd"><div class="b">Valvic Marcenaria</div>'
            f'<div class="m">{CLIENTE} · {DATA}</div></div>')

pg = []
# ── 1 · capa ────────────────────────────────────────────────────────────
pg.append(f"""<div class="page"><div class="cv">
  <div class="ph"><img src="{IMG['varanda-01']}" alt=""></div>
  <div class="bt">
    <div class="mark">Valvic Marcenaria</div>
    <h1>A casa<br>inteira.</h1>
    <div class="sub"><b>{CLIENTE}</b> · {OBRA}<br>Projeto <b>{ARQ}</b></div>
  </div>
</div></div>""")

# ── 2 · a empresa e o processo ──────────────────────────────────────────
ETAPAS = [
 ('Medição', 'Vamos ao local antes de cortar e conferimos cada medida do '
  'projeto executivo. É aí que fecham as alturas do piso ao forro.'),
 ('Detalhamento', 'Compatibilizamos a marcenaria com a elétrica, com os '
  'eletrodomésticos e com a marmoraria, peça por peça.'),
 ('Corte', 'CNC próprio, com furação oculta — a cavilha só aparece onde '
  'ninguém vê. É o que deixa a face limpa e o móvel no esquadro.'),
 ('Montagem', 'Equipe nossa, não terceirizada. Quem monta responde pelo que '
  'cortou.'),
 ('Entrega', 'Regulagem de cada porta e cada gaveta, e a iluminação já '
  'instalada e acesa.'),
]
steps = ''.join(f'<div class="step"><div class="n serif">{i:02d}</div>'
                f'<div><div class="t">{t}</div><div class="d">{d}</div></div>'
                f'</div>' for i, (t, d) in enumerate(ETAPAS, 1))
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Quem faz</div>
  <div class="h1 serif">Marcenaria própria,<br>do desenho à regulagem.</div>
  <div class="lead">A Valvic é marcenaria de <b>fábrica própria em Belo
  Horizonte</b>. Projeto, corte, montagem e instalação saem da mesma casa —
  entre o desenho da arquiteta e a última porta regulada <b>não entra
  terceiro nenhum</b>. É por isso que conseguimos responder por prazo e por
  garantia sem repassar a conversa para outro.</div>

  <div class="mos a" style="flex:none;height:84mm;min-height:0;max-height:84mm;">
    <img src="{IMG['cozinha-01']}" alt="">
    <div class="st"><img src="{IMG['suite-master-01']}" alt="">
      <img src="{IMG['office-01']}" alt=""></div>
  </div>

  <div class="eye">Como fazemos</div>
  <div style="margin-top:3mm;flex:none;">{steps}</div>
  {foot(2)}
</div></div>""")

# ── 3 · as TRÊS linhas, ANTES de qualquer preço ─────────────────────────
DIF = [
 ('Corrediça', 'Telescópica, com trilho aparente na lateral da gaveta.',
  'Oculta alemã: o trilho some por baixo e a gaveta abre inteira.',
  'Oculta Blum: a referência do mercado em suavidade e em carga.'),
 ('Dobradiça', 'Nacional, com abertura de noventa graus.',
  'Alemã, com amortecedor e regulagem nos três sentidos.',
  'Blum, com amortecedor e regulagem nos três sentidos.'),
 ('Fechamento', 'Sem amortecedor — a gaveta fecha no impulso.',
  'Amortecido, em todas as gavetas e portas.',
  'Amortecido, com o toque mais macio das três.'),
 ('Garantia', cen.CEN['Telescópica']['gar'], cen.CEN['Hettich']['gar'],
  cen.CEN['Blum']['gar']),
]
difs = ''.join(f'<div class="r"><div class="k">{k}</div><div class="a">{a}</div>'
               f'<div class="b2">{b}</div><div class="c3">{c}</div></div>'
               for k, a, b, c in DIF)
cards = ''.join(
  f'<div class="c{" on" if n == "Blum" else ""}"><div class="k">{n}</div>'
  f'<div class="n serif">{cen.CEN[n]["chamada"]}</div>'
  f'<div class="g serif">{cen.CEN[n]["gar"]}</div>'
  f'<div class="gl">de garantia</div></div>'
  for n in ('Telescópica', 'Hettich', 'Blum'))
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Uma escolha</div>
  <div class="h1 serif">Três linhas. A diferença<br>está na ferragem.</div>
  <div class="lead">O desenho, os padrões de MDF, a laca da cozinha, a
  furação oculta e o acabamento são <b>os mesmos nas três</b>. O que muda é
  a peça que vocês tocam todo dia — e é ela que decide <b>quanto tempo o
  móvel continua fechando bem</b>.</div>

  <div class="vs tri">{cards}</div>
  <div class="dif tri">{difs}</div>

  <div class="sel" style="margin-top:5mm;">
    <div class="k">O que não muda</div>
    <div class="d">Os <b>padrões de MDF especificados pela arquiteta</b>, a
    <b>laca acetinada da cozinha</b>, a <b>furação oculta</b>, o <b>puxador
    cava usinado na própria peça</b>, as <b>almas de aço</b> nas prateleiras
    de vão longo e a <b>equipe própria</b> do corte à montagem.</div>
  </div>
  {foot(3)}
</div></div>""")

# ── 4…12 · os ambientes, SEM preço ──────────────────────────────────────
for n, (titulo, imgs, ambs, acab, itens) in enumerate(PG, start=4):
    lado = 'a' if n % 2 == 0 else 'b'          # ⭐ alterna a cada página
    if len(imgs) == 3:
        st = (f'<div class="st"><img src="{IMG[imgs[1]]}" alt="">'
              f'<img src="{IMG[imgs[2]]}" alt=""></div>')
        mos = (f'<img src="{IMG[imgs[0]]}" alt="">{st}' if lado == 'a'
               else f'{st}<img src="{IMG[imgs[0]]}" alt="">')
    else:
        mos = ''.join(f'<img src="{IMG[i]}" alt="">'
                      for i in (imgs if lado == 'a' else imgs[::-1]))
    lis = ''.join(f'<div class="li"><div class="t">{t}</div>'
                  f'<div class="d">{d}</div></div>' for t, d in itens)
    tags = ''.join(f'<span>{a}</span>' for a in ambs)
    pg.append(f"""<div class="page"><div class="pad">
      {head()}
      <div class="eye">Ambiente</div>
      <div class="h1 serif">{titulo}</div>
      <div class="tags">{tags}</div>
      <div class="mos {lado}">{mos}</div>
      <div class="lista">{lis}</div>
      <div class="acab"><div class="k">Acabamentos</div>
        <div class="v">{acab}</div></div>
      {foot(n)}
    </div></div>""")

# ── 13 · o investimento — a PRIMEIRA página com preço ───────────────────
REF = 'Hettich'          # ⭐ a linha especificada hoje, e a do meio
rows = ''.join(f'<div class="row"><span>{nome[3:]}</span>'
               f'<span class="v">{br(cen.CEN[REF]["pv"][i])}</span></div>'
               for i, (nome, *_) in enumerate(cen.AMB))
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Investimento · linha Hettich</div>
  <div class="h1 serif">Ambiente por ambiente.</div>
  <div class="lead">Dezenove ambientes, levantados peça por peça do projeto
  executivo. <b>Cada linha abaixo é um ambiente fechado</b> — nada é rateio
  nem estimativa por metro quadrado.</div>
  <div class="rows two">{rows}</div>
  <div class="mos a" style="max-height:58mm;margin-top:5mm;">
    <img src="{IMG['cozinha-02']}" alt="">
    <div class="st"><img src="{IMG['banho02-02']}" alt="">
      <img src="{IMG['rouparia-01']}" alt=""></div>
  </div>
  <div class="vista" style="padding:8mm 9mm;">
    <div><div class="lab">A casa inteira · linha Hettich</div>
      <div class="big">R$ {br(cen.CEN[REF]['preco'])}</div>
      <div class="s">Com <b>{cen.CEN[REF]['gar']} de garantia</b> sobre a
      marcenaria, a ferragem e a instalação.</div></div>
  </div>
  {foot(N0)}
</div></div>""")

# ── 14 · as três linhas, com preço ──────────────────────────────────────
cards2 = ''.join(
  f'<div class="c{" on" if n == "Blum" else ""}"><div class="k">{n}</div>'
  f'<div class="n serif">{cen.CEN[n]["chamada"]}</div>'
  f'<div class="g serif">{cen.CEN[n]["gar"]}</div>'
  f'<div class="gl">de garantia</div>'
  f'<div class="p">A casa inteira<b>R$ {br(cen.CEN[n]["preco"])}</b></div></div>'
  for n in ('Telescópica', 'Hettich', 'Blum'))
dif_b = cen.CEN['Blum']['preco'] - cen.CEN['Telescópica']['preco']
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Investimento · as três linhas</div>
  <div class="h1 serif">Dois anos, dez, ou trinta.</div>
  <div class="lead">A mesma casa, o mesmo desenho e os mesmos padrões. A
  diferença é a <b>ferragem</b> — e o tempo pelo qual respondemos por ela.
  A garantia do conjunto segue sempre <b>a ferragem de menor linha
  presente</b>: é por isso que a escolha vale para a casa toda, e não móvel
  a móvel.</div>

  <div class="vs tri">{cards2}</div>

  <div class="mos b" style="max-height:74mm;">
    <div class="st"><img src="{IMG['closet-master-02']}" alt="">
      <img src="{IMG['suite02-01']}" alt=""></div>
    <img src="{IMG['banho-master-01']}" alt="">
  </div>

  <div class="vista" style="padding:7mm 9mm;">
    <div><div class="lab">Da telescópica à Blum</div>
      <div class="big" style="font-size:34pt;">R$ {br(dif_b)}</div>
      <div class="s">É o que separa os dois extremos — e o que compra
      <b>vinte e oito anos a mais</b> de garantia.</div></div>
    <div class="rt"><div class="k">Garantia</div>
      <div class="v" style="font-size:19pt;color:#fff;">2 → 30 anos</div></div>
  </div>
  {foot(N0+1)}
</div></div>""")

# ── 15 · as duas trocas ─────────────────────────────────────────────────
trs = ''.join(f'<div class="r"><div><div class="t">{t}</div>'
              f'<div class="d">{d}</div></div>'
              f'<div class="v">− R$ {br(dp)}</div></div>'
              for t, dp, _, d in cen.TROCA)
dois = sum(t[1] for t in cen.TROCA)
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Duas alternativas</div>
  <div class="h1 serif">Dois caminhos para<br>ajustar o investimento.</div>
  <div class="lead">Se o número precisar ceder, estes são os dois lugares
  onde ele cede <b>sem tocar na ferragem e sem tocar na garantia</b>. O
  desconto é o mesmo <b>qualquer que seja a linha escolhida</b>.</div>

  <div class="tr">{trs}
    <div class="r"><div><div class="t">As duas juntas</div></div>
      <div class="v">− R$ {br(dois)}</div></div>
  </div>

  <div class="notes" style="margin-top:7mm;">
    <div class="bx"><div class="k">A cozinha em melamínico</div>
      <div class="d">A laca é <b>mais da metade do custo da cozinha</b>, e
      sai em peça pintada dos dois lados — de um lado só, ela empena. Mas
      o melamínico <b>não aceita a moldura provençal</b>: ela é usinada na
      router e o rebaixo expõe o miolo da chapa, que na laca some debaixo da
      tinta. <b>Melamínico aqui é frente lisa</b> — é outra cozinha, não a
      mesma mais barata.</div></div>
    <div class="bx w"><div class="k">O painel do office usinado</div>
      <div class="d">A grade de réguas encaixadas em meia-madeira vira um
      <b>painel plano usinado na CNC</b>. O desenho do muxarabi continua; o
      que muda é que ele passa a ser <b>vazado na chapa</b> em vez de montado
      régua a régua. Sem as peças filetadas uma a uma, é o item que mais
      cede em proporção na casa inteira.</div></div>
  </div>
  <div class="mos b" style="max-height:62mm;margin-top:6mm;">
    <div class="st"><img src="{IMG['office-muxarabi']}" alt="">
      <img src="{IMG['cozinha-03']}" alt=""></div>
    <img src="{IMG['cozinha-01']}" alt="">
  </div>
  {foot(N0+2)}
</div></div>""")

# ── 16 · condições ──────────────────────────────────────────────────────
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Condições</div>
  <div class="h1 serif">Como fechamos.</div>

  <div class="mos a" style="max-height:72mm;">
    <img src="{IMG['varanda-02']}" alt="">
    <div class="st"><img src="{IMG['homeschooling-01']}" alt="">
      <img src="{IMG['lavanderia-01']}" alt=""></div>
  </div>

  <div class="four">
    <div><div class="k">Prazo</div><div class="v">{PRAZO}</div>
      <div class="s">Do aceite e da medição no local.</div></div>
    <div><div class="k">Garantia</div><div class="v">2 · 10 · 30 anos</div>
      <div class="s">Conforme a linha escolhida.</div></div>
    <div><div class="k">Execução</div><div class="v">Equipe própria</div>
      <div class="s">Do corte à instalação.</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div>
      <div class="s">A partir desta data.</div></div>
  </div>

  <div class="notes">
    <div class="bx"><div class="k">O que não está incluso</div>
      <div class="d">Toda a <b>pedra</b> — bancadas, rodobancas, sóculos,
      soleiras e a cuba esculpida do lavabo, que são marmoraria. Os
      <b>eletrodomésticos</b>, as <b>cubas, torneiras e louças</b>. A
      <b>elétrica</b> — pontos, circuitos, drivers e interruptores. As
      <b>esquadrias</b>, o <b>forro</b>, o <b>piso</b>, a <b>pintura de
      parede</b> e o <b>corpo de alvenaria</b> da ilha da varanda.</div></div>
    <div class="bx w"><div class="k">A confirmar antes da produção</div>
      <div class="d">A <b>medição no local</b> antes do corte, que é ela que
      fecha a altura dos móveis do piso ao forro. A <b>cristaleira da
      varanda</b>, que a planta desenha curva e a elevação desenha reta — e
      as duas não podem estar certas ao mesmo tempo. O <b>modelo dos
      puxadores</b>. E <b>amostra</b> dos padrões de MDF e da cor da laca,
      aprovadas por vocês e pela arquiteta.</div></div>
  </div>
  {foot(NP)}
</div></div>""")

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + EXTRA + '</style></head><body>'
        + ''.join(pg) + '</body></html>')
assert len(pg) == NP, f'⛔ {len(pg)} páginas, o rodapé diz {NP}'
# ⛔⛔ "NUNCA APRESENTE PREÇO SEM ANTES GERAR VALOR" — a trava, não a boa fé:
#   nenhum "R$" pode aparecer antes da página do investimento.
_antes = ''.join(pg[:N0-1])
assert 'R$' not in _antes, '⛔⛔ TEM PREÇO ANTES DA PÁGINA DE VALOR'
# ⛔⛔ MARCAÇÃO INTERNA NÃO VAI PARA O CLIENTE. ⭐/⛔/⚠ são a minha linguagem
#   de orçamento, não a da peça — impressas, viram emoji vermelho no meio da
#   frase. Eu já tinha APONTADO esse defeito na folha da Eliza e repeti aqui
#   na primeira rodada. Boa fé não bastou duas vezes; vai de assert.
_marca = [c for c in '⭐⛔⚠' if c in ''.join(pg)]
assert not _marca, f'⛔⛔ MARCAÇÃO INTERNA NA PEÇA DO CLIENTE: {_marca}'

(P/'proposta-gustavo-raposo.html').write_text(HTML, encoding='utf-8')
subprocess.run(['node', str(P/'render-pdf.js'), str(P/'proposta-gustavo-raposo.html'),
                str(P/'proposta-gustavo-raposo.pdf')], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'proposta-gustavo-raposo.pdf · {NP} páginas · '
      f'{(P/"proposta-gustavo-raposo.pdf").stat().st_size//1024} kB')
print(f'  primeiro preço: página {N0}')
for n in ('Telescópica', 'Hettich', 'Blum'):
    print(f'  {n:14s} R$ {br(cen.CEN[n]["preco"]):>10s} · {cen.CEN[n]["gar"]}')
