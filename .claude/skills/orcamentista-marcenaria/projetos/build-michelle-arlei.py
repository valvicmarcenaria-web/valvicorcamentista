# -*- coding: utf-8 -*-
"""MICHELLE E ARLEI — proposta · casa completa  [19/10/2026]

⭐ [Jonathan 19/10 · segunda rodada] "o layout não ficou legal não.
   NUNCA APRESENTE PREÇO SEM ANTES GERAR VALOR na proposta. Fale um pouco
   da empresa e dos processos antes de expor valores. Mostre as duas linhas
   antes, fale das diferenças. As imagens ficaram muito grandes, crie um
   layout mais criativo. Descreva os itens junto com a listagem dos
   ambientes, só listando item por item mesmo."

   → ORDEM NOVA: nenhum número de dinheiro antes da página 10. Empresa e
     processo (2), as duas linhas e suas diferenças (3), os ambientes com a
     LISTA ITEM A ITEM (4–9) — e só então o investimento.
   → MOSAICO em vez de faixa: duas ou três fotos por página, menores, com
     composição assimétrica que ALTERNA de lado a cada ambiente.
   → O texto corrido saiu. Cada móvel é uma linha da lista.

Números de `corte-michelle-arlei.py`; nada digitado à mão.
⛔ Sem metragem e sem contagem em nenhuma descrição.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('ma', P/'corte-michelle-arlei.py')
ma = importlib.util.module_from_spec(spec); sys.modules['ma'] = ma
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(ma)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, OBRA, DATA = 'Michelle e Arlei', 'Residência', '19 de outubro de 2026'
ARQ = 'Inédita Arquitetura'
PRAZO, VALIDADE = '90 dias corridos', '7 dias úteis'
GAR_E, GAR_P = ma.GARANTIA['essencial'], ma.GARANTIA['premium']
TOT, VISTA = ma.TOTAL, ma.VISTA
TOT_P, VISTA_P = ma.TOTAL_PREM, ma.VISTA_PREM
DESC = ma.DESC_VISTA

def uri(n):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img-michelle-arlei'/n).read_bytes()).decode())
IMG = {n.stem: uri(n.name) for n in sorted((P/'img-michelle-arlei').iterdir())}

# ── os ambientes: imagens e LISTA ITEM A ITEM ───────────────────────────
PG = [
 ('Sala e área gourmet', ['sala-02', 'sala-01', 'sala-03'],
  ['Sala', 'Área gourmet'],
  'MDF Gianduia Natural, Duratex', [
   ('Painel de TV liso e ripado', 'MDF Gianduia Natural, com o ponto de luz '
    'transferido para dentro da marcenaria.'),
   ('Rack suspenso', 'Gavetas com puxador passante usinado na própria peça.'),
   ('Armário inferior do gourmet', 'Portas ripadas e gaveta de espetos, em '
    'MDF Gianduia Natural.')]),
 ('Cozinha', ['cozinha-01', 'cozinha-02'], ['Cozinha'],
  'MDF Gianduia Natural e Itapuã, Duratex', [
   ('Armário inferior em “U”', 'Portas de giro, gavetões e os nichos de '
    'temperos e pano de prato. MDF Gianduia Natural.'),
   ('Torre quente', 'Básculas, nicho de micro-ondas e nicho de forno, '
    'compatibilizados com os aparelhos de vocês. MDF Itapuã.'),
   ('Armário superior', 'Portas de giro com puxador cava, em MDF Gianduia '
    'Natural.'),
   ('Prateleira iluminada', 'MDF Itapuã, com perfil de LED embutido na peça.'),
   ('Bancada de lanche', 'MDF Itapuã, em espessura encorpada.'),
   ('Cachepôs de temperos', 'Estrutura metálica preta do piso ao teto, com '
    'os cachepôs em MDF Itapuã.')]),
 ('Lavanderia e banhos', ['lavanderia', 'banho-social', 'casal-04'],
  ['Lavanderia', 'Banho social', 'Banho do casal'],
  'MDF Itapuã e Gianduia Natural, Duratex · MDF Areia, Guararapes', [
   ('Armário de básculas', 'Iluminado, com prateleira, em MDF Itapuã.'),
   ('Armário inferior', 'Portas de giro sob a bancada, em MDF Gianduia '
    'Natural.'),
   ('Mesa de apoio', 'Estrutura metálica preta, tampo e prateleira em MDF '
    'Itapuã.'),
   ('Armário do banho social', 'Portas de giro e gavetas, em MDF Itapuã.'),
   ('Armário do banho do casal', 'Portas de giro e gavetas, em MDF Areia.')]),
 ('Quarto Gabriel', ['gabriel-01', 'gabriel-02'], ['Quarto Gabriel'],
  'MDF Brisa, Guararapes · MDF Itapuã, Duratex', [
   ('Painel liso e ripado', 'MDF Brisa, com apoio para o suporte da TV.'),
   ('Prateleira iluminada', 'MDF Itapuã, com perfil de LED embutido.'),
   ('Escrivaninha', 'MDF Itapuã, com caixa de tomada embutida na marcenaria.'),
   ('Armário suspenso', 'Abertura ao toque, sem puxador aparente. MDF Brisa.'),
   ('Cabeceira ripada iluminada', 'MDF Brisa, com a luz embutida na peça.'),
   ('Prateleiras', 'MDF Itapuã.')]),
 ('Quarto das gêmeas', ['gemeas-01', 'gemeas-02'], ['Quarto das gêmeas'],
  'MDF Brisa e Alecrim, Guararapes', [
   ('Painel de TV', 'MDF Brisa, com apoio para o suporte da TV.'),
   ('Armário superior', 'MDF Alecrim com portas em MDF Brisa e iluminação '
    'embutida.'),
   ('Escrivaninha com gavetas', 'MDF Alecrim, com caixa de tomada embutida '
    'e divisões internas alinhadas com vocês.'),
   ('Cabeceira iluminada', 'MDF Alecrim, com rodapé em perfil metálico.'),
   ('Armário', 'Portas de giro com puxador cava, em MDF Brisa.'),
   ('Baú', 'Tampo com puxador cava, em MDF Brisa.'),
   ('Mesas de cabeceira', 'Gavetas com puxador cava, em MDF Brisa.')]),
 ('Suíte master', ['casal-01', 'casal-02', 'casal-03'], ['Suíte master'],
  'MDF Itapuã, Duratex · MDF Areia, Guararapes', [
   ('Cabeceira iluminada', 'MDF Itapuã, com rodapé em perfil metálico.'),
   ('Painel de TV do piso ao forro', 'Porta de correr embutida com puxador '
    'cava, detalhe ripado em MDF Areia e reforço metálico para o suporte '
    'da TV.'),
   ('Prateleira iluminada', 'MDF Itapuã, com perfil de LED embutido.'),
   ('Closet aberto', 'Maleiros, cabideiros, nichos, gavetas e sapateiras em '
    'MDF Itapuã e Areia, com banco estofado e prateleira iluminada.')]),
]
# ⛔⛔ TRAVAS
_amb_pg = [a for _t, _i, ambs, _ac, _l in PG for a in ambs]
assert set(_amb_pg) == set(ma.AMBS), (
    f'⛔ A PROPOSTA NÃO COBRE OS MESMOS AMBIENTES DO MOTOR: '
    f'{set(_amb_pg) ^ set(ma.AMBS)}')
assert len(_amb_pg) == len(set(_amb_pg)), '⛔ AMBIENTE REPETIDO NA PROPOSTA'
assert abs(sum(ma.PV_AMB[a] for a in _amb_pg) - TOT) < 0.5, '⛔ O TOTAL NÃO FECHA'
assert abs(ma.MC_ALVO - 0.40) < 1e-9, f'⛔ A MC MUDOU: {ma.MC_ALVO:.3f}'
assert abs(ma.LINHAS['premium']['mc'] - 0.43) < 1e-9, '⛔ A MC DA PREMIUM MUDOU'
assert ma.RT_ON is True, '⛔ O RT SAIU DO MOTOR'
assert VISTA == round(TOT*(1-DESC)/10)*10, '⛔ O À VISTA NÃO FECHA'
NP = len(PG) + 6

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

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · {OBRA}</span><span>{n} / {NP}</span></div>')
def head():
    return (f'<div class="hd"><div class="b">Valvic Marcenaria</div>'
            f'<div class="m">{CLIENTE} · {DATA}</div></div>')

pg = []
# ── 1 · capa ────────────────────────────────────────────────────────────
pg.append(f"""<div class="page"><div class="cv">
  <div class="ph"><img src="{IMG['sala-01']}" alt=""></div>
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
  'eletrodomésticos de vocês e com a marmoraria, peça por peça.'),
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
    <div class="st"><img src="{IMG['gemeas-02']}" alt="">
      <img src="{IMG['casal-02']}" alt=""></div>
  </div>

  <div class="eye">Como fazemos</div>
  <div style="margin-top:3mm;flex:none;">{steps}</div>
  {foot(2)}
</div></div>""")

# ── 3 · as duas linhas, ANTES de qualquer preço ─────────────────────────
DIF = [
 ('Corrediça', 'Telescópica reforçada, com amortecedor.',
  'Oculta alemã: o trilho some por baixo, a gaveta abre inteira e não '
  'mostra ferragem na lateral.'),
 ('Dobradiça', 'Nacional, com amortecedor e abertura de noventa graus.',
  'Alemã, com amortecedor e regulagem nos três sentidos.'),
 ('Básculas', 'Pistão a gás com amortecimento.',
  'Articulador premium: a porta sobe sozinha e para onde você soltar.'),
 ('Iluminação', 'Fita e perfil de linha comum, com difusor.',
  'Linha profissional, com difusor sem pontos e cor estável no tempo.'),
 ('Garantia', GAR_E, GAR_P),
]
difs = ''.join(f'<div class="r"><div class="k">{k}</div>'
               f'<div class="a">{a}</div><div class="b2">{b}</div></div>'
               for k, a, b in DIF)
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Uma escolha</div>
  <div class="h1 serif">Duas linhas. A diferença<br>está na ferragem.</div>
  <div class="lead">O desenho, as cinco cores de MDF, a furação oculta e o
  acabamento são <b>os mesmos nas duas</b>. O que muda é a peça que você
  toca todo dia — e é ela que decide <b>quanto tempo o móvel continua
  fechando bem</b>.</div>

  <div class="vs">
    <div class="c"><div class="k">Essencial</div>
      <div class="n serif">Corrediça telescópica</div>
      <div class="g serif">{GAR_E}</div>
      <div class="gl">de garantia</div></div>
    <div class="c on"><div class="k">Premium · Hettich</div>
      <div class="n serif">Corrediça oculta, alemã</div>
      <div class="g serif">{GAR_P}</div>
      <div class="gl">de garantia</div></div>
  </div>

  <div class="dif">{difs}</div>

  <div class="sel" style="margin-top:6mm;">
    <div class="k">O que não muda</div>
    <div class="d">Os <b>cinco padrões de MDF</b> especificados pela
    arquiteta, a <b>furação oculta</b>, o <b>puxador cava usinado na própria
    peça</b>, a <b>iluminação entregue instalada</b> e a <b>equipe
    própria</b> do corte à montagem.</div>
  </div>
  {foot(3)}
</div></div>""")

# ── 4…9 · os ambientes, SEM preço ───────────────────────────────────────
for n, (titulo, imgs, ambs, acab, itens) in enumerate(PG, start=4):
    lado = 'a' if n % 2 == 0 else 'b'          # ⭐ alterna a cada página
    if len(imgs) == 3:
        st = f'<div class="st"><img src="{IMG[imgs[1]]}" alt="">' \
             f'<img src="{IMG[imgs[2]]}" alt=""></div>'
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

# ── 10 · o investimento — o primeiro número da proposta ─────────────────
N0 = len(PG) + 4
rows = ''.join(f'<div class="row"><span>{a}</span>'
               f'<span class="v">{br(ma.PV_AMB[a])}</span></div>'
               for a in ma.AMBS)
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Investimento · linha Essencial</div>
  <div class="h1 serif">Ambiente por ambiente.</div>
  <div class="rows">{rows}
    <div class="row"><b>Total</b><span class="v">R$ {br(TOT)}</span></div>
  </div>
  <div class="vista">
    <div><div class="lab">À vista · {DESC:.0%} de desconto</div>
      <div class="big">R$ {br(VISTA)}</div>
      <div class="s">Entrada e saldo por transferência, sem cartão —
      devolvemos a taxa que deixamos de pagar.</div></div>
    <div class="rt"><div class="k">Valor cheio</div>
      <div class="v">R$ {br(TOT)}</div></div>
  </div>
  <div class="pay">
    <div class="r on"><div>Entrada <b>70%</b> + saldo por transferência</div>
      <div class="x">−{DESC:.0%} · R$ {br(VISTA)}</div></div>
    <div class="r"><div>Entrada <b>70%</b> + saldo em até seis vezes no cartão</div>
      <div class="x">−5%</div></div>
    <div class="r"><div>Entrada <b>50%</b> + saldo em até oito vezes no cartão</div>
      <div class="x">−3%</div></div>
    <div class="r"><div>Entrada <b>30%</b> + saldo em até dez vezes no cartão</div>
      <div class="x">R$ {br(TOT)}</div></div>
  </div>
  {foot(N0)}
</div></div>""")

# ── 11 · o investimento da linha Premium ────────────────────────────────
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Investimento · as duas linhas</div>
  <div class="h1 serif">Dois anos, ou dez.</div>
  <div class="lead">A mesma casa, o mesmo desenho e as mesmas cores. A
  diferença é a <b>ferragem alemã</b> — e o tempo pelo qual respondemos
  por ela.</div>

  <div class="vs">
    <div class="c"><div class="k">Essencial</div>
      <div class="n serif">Corrediça telescópica</div>
      <div class="g serif">{GAR_E}</div>
      <div class="gl">de garantia</div>
      <div class="p">À vista<b>R$ {br(VISTA)}</b></div></div>
    <div class="c on"><div class="k">Premium · Hettich</div>
      <div class="n serif">Corrediça oculta, alemã</div>
      <div class="g serif">{GAR_P}</div>
      <div class="gl">de garantia</div>
      <div class="p">À vista<b>R$ {br(VISTA_P)}</b></div></div>
  </div>

  <div class="mos a">
    <img src="{IMG['casal-03']}" alt="">
    <div class="st"><img src="{IMG['gabriel-01']}" alt="">
      <img src="{IMG['sala-02']}" alt=""></div>
  </div>

  <div class="vista" style="padding:7mm 9mm;">
    <div><div class="lab">A diferença</div>
      <div class="big" style="font-size:36pt;">R$ {br(TOT_P-TOT)}</div>
      <div class="s">Sobre o valor cheio — <b>{(TOT_P/TOT-1):.0%} a mais</b>
      pela ferragem alemã e pela garantia que vem com ela.</div></div>
    <div class="rt"><div class="k">Garantia</div>
      <div class="v" style="font-size:19pt;color:#fff;">{GAR_E} → {GAR_P}</div></div>
  </div>
  {foot(N0+1)}
</div></div>""")

# ── 12 · condições ──────────────────────────────────────────────────────
pg.append(f"""<div class="page"><div class="pad">
  {head()}
  <div class="eye">Condições</div>
  <div class="h1 serif">Como fechamos.</div>

  <div class="mos b">
    <div class="st"><img src="{IMG['gemeas-01']}" alt="">
      <img src="{IMG['lavanderia']}" alt=""></div>
    <img src="{IMG['casal-01']}" alt="">
  </div>

  <div class="four">
    <div><div class="k">Prazo</div><div class="v">{PRAZO}</div>
      <div class="s">Do aceite e da medição no local.</div></div>
    <div><div class="k">Garantia</div><div class="v">{GAR_E} · {GAR_P}</div>
      <div class="s">Essencial e Premium.</div></div>
    <div><div class="k">Execução</div><div class="v">Equipe própria</div>
      <div class="s">Do corte à instalação.</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div>
      <div class="s">A partir desta data.</div></div>
  </div>

  <div class="notes">
    <div class="bx"><div class="k">O que não está incluso</div>
      <div class="d">As <b>bancadas e os rodapés em granito</b>, que são
      marmoraria. Os <b>eletrodomésticos</b>, as <b>cubas, torneiras e
      louças</b>. A <b>elétrica</b> — pontos, circuitos, drivers e
      interruptores. Os <b>espelhos de parede</b>, os <b>cobogós</b>, as
      <b>esquadrias</b>, o <b>forro de gesso</b>, o <b>piso</b> e a
      <b>pintura</b>.</div></div>
    <div class="bx w"><div class="k">A confirmar antes da produção</div>
      <div class="d">O projeto pede <b>conferir todas as medidas no
      local</b> — fazemos a medição antes do corte, e é ela que fecha a
      altura dos móveis do piso ao forro. O <b>forno e o micro-ondas</b>
      precisam estar definidos para a torre da cozinha. E <b>amostra</b>
      dos cinco padrões de MDF, aprovada por vocês e pela
      arquiteta.</div></div>
  </div>
  {foot(NP)}
</div></div>""")

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + ''.join(pg) + '</body></html>')
assert len(pg) == NP, f'⛔ {len(pg)} páginas, o rodapé diz {NP}'
# ⛔⛔ "NUNCA APRESENTE PREÇO SEM ANTES GERAR VALOR" — a trava, não a boa fé:
#   nenhum "R$" pode aparecer antes da página do investimento.
_antes = ''.join(pg[:N0-1])
assert 'R$' not in _antes, '⛔⛔ TEM PREÇO ANTES DA PÁGINA DE VALOR'

(P/'proposta-michelle-arlei.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-michelle-arlei.pdf')],
               check=True, env=env)
print(f'proposta-michelle-arlei.pdf · {NP} páginas · '
      f'{(P/"proposta-michelle-arlei.pdf").stat().st_size//1024} kB')
print(f'  primeiro preço: página {N0}')
print(f'  {"TOTAL":<22} R$ {br(TOT):>8}')
print(f'  {"À VISTA −"+f"{DESC:.0%}":<22} R$ {br(VISTA):>8}')
print(f'  {"Premium Hettich":<22} R$ {br(TOT_P):>8}  (à vista {br(VISTA_P)})')
