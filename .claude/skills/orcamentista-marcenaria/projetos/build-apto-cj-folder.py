# -*- coding: utf-8 -*-
"""FOLDER Apto CJ (B+G Estúdio) — material gráfico de alto impacto, 8 páginas.
Capa · conceitual lâmina de Freijó · conceitual laca fosca PU · descritivo ·
miolo (6 configurações) · preço por móvel · técnico · garantia+condições.
Preços FECHADOS comercialmente [Jonathan 28/07] — auditados em precos-apto-cj.py:
as duas colunas (à vista e parcelado) são aditivas, desconto à vista 10% em tudo,
e a opção 1 honra exatamente os R$ 84.600 / 76.100 já entregues."""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

HERO    = open('/tmp/uri_cj_hero.txt').read()      # entrada em freijó — capa
ESTANTE = open('/tmp/uri_cj_estante.txt').read()   # estante das salas (laca)
GOURMET = open('/tmp/uri_cj_gourmet.txt').read()   # varanda gourmet ambientada
OBJ     = open('/tmp/uri_cj_obj.txt').read()       # móvel entrada sobre branco
CRIST   = open('/tmp/uri_cj_crist.txt').read()     # crop cristaleira
TEX     = open('/tmp/uri_cj_tex.txt').read()       # textura freijó (crop do projeto)
ELEV    = open('/tmp/uri_cj_elev.txt').read()      # render frontal 636 cm na cor — laca
EST2    = open('/tmp/uri_cj_est2.txt').read()      # crop cristaleira + nicho + bancada
EST3    = open('/tmp/uri_cj_est3.txt').read()      # crop painel de TV + portas altas
PUX     = open('/tmp/uri_cj_pux.txt').read()       # puxador bolinha dourado fosco
CSS     = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .page:last-of-type{{page-break-after:avoid; break-after:avoid;}}
  .cover .hero-img img{{object-position:center 40%; filter:brightness(1.06);}}
  .cover .veil{{background:linear-gradient(180deg,
      rgba(24,19,14,.88) 0%, rgba(24,19,14,.38) 26%, rgba(24,19,14,.16) 50%,
      rgba(24,19,14,.62) 76%, rgba(24,19,14,.94) 100%);}}

  /* ── contracapa conceitual (fundo escuro) */
  .concept{{background:var(--deep); color:#EFE9DC;}}
  .concept .pad{{padding:16mm 19mm 14mm;}}
  .concept .eyebrow{{color:var(--gold-lt);}}
  .concept .h-sec{{color:#fff;}}
  .concept .body-t{{color:#C9C2B4;}}
  .concept .body-t b{{color:#F0E7D6;}}
  .texband{{border-radius:6px; overflow:hidden; margin:5mm 0 0;
      box-shadow:inset 0 0 0 1px rgba(201,169,106,.25);}}
  .texband img{{width:100%; height:36mm; object-fit:cover; display:block;}}
  .objcard{{background:#F6F2E9; border-radius:6px; padding:5mm 6mm 3.5mm; margin-top:5mm;}}
  .objcard img{{width:100%; display:block;}}
  .objcard .cap{{color:#8F8578; margin-top:2mm;}}
  .proc{{display:flex; gap:0; margin-top:5.5mm; border-top:1px solid rgba(201,169,106,.30);
      padding-top:3.6mm;}}
  .proc > div{{flex:1; padding:0 4.5mm; border-left:1px solid rgba(201,169,106,.16);}}
  .proc > div:first-child{{padding-left:0; border-left:0;}}
  .proc .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:15pt; font-weight:700;
      color:var(--gold-lt); line-height:1;}}
  .proc .d{{font-size:7.9pt; color:#B9B1A2; line-height:1.5; margin-top:1.4mm;}}
  .proc .d b{{color:#F0E7D6;}}

  /* ── conceitual laca */
  .p-laca .pad{{padding:13mm 19mm 10mm;}}
  .p-laca .body-t{{font-size:9.2pt;}}
  .p-laca .objcard{{background:#F2EEE5; padding:4mm 4.5mm 2.5mm;}}
  .p-laca .objcard img{{width:100%; display:block; border-radius:3px;}}
  .p-laca .objcard .cap{{font-size:7.2pt; line-height:1.4;}}
  .p-laca .texband img{{width:100%; display:block;}}

  /* ── descritivo */
  .p-esc .amb{{padding-top:2.6mm; margin-bottom:3.8mm;}}
  .p-esc .amb ul{{line-height:1.5; margin-top:1.8mm;}}

  /* ── miolo comparativo */
  .opt1{{background:var(--deep); border-radius:7px; padding:5.5mm 7mm; position:relative;
      overflow:hidden; box-shadow:inset 0 0 0 1.5px rgba(201,169,106,.55); margin-top:4.5mm;}}
  .opt1::after{{content:""; position:absolute; left:0; top:0; bottom:0; width:4px;
      background:var(--gold-lt);}}
  .opt1 .tag{{display:inline-block; padding:1mm 3.6mm; border-radius:99px;
      background:rgba(201,169,106,.16); border:1px solid rgba(201,169,106,.5);
      font-size:7pt; font-weight:700; letter-spacing:.16em; text-transform:uppercase;
      color:var(--gold-lt);}}
  .opt1 .nm{{font-family:'Cormorant Garamond',Georgia,serif; font-size:16.5pt; font-weight:700;
      color:#fff; margin-top:2.2mm; line-height:1.15;}}
  .opt1 .ds{{font-size:8.4pt; color:#C6BFB2; margin-top:1.4mm; line-height:1.55;}}
  .opt1 .ds b{{color:#F0E7D6;}}
  .opt1 .prices{{display:flex; gap:8mm; margin-top:3mm; padding-top:2.8mm;
      border-top:1px solid rgba(201,169,106,.30); align-items:baseline;}}
  .opt1 .pr .k{{font-size:6.8pt; letter-spacing:.18em; text-transform:uppercase;
      color:#9C9288; font-weight:700;}}
  .opt1 .pr .v{{font-family:'Cormorant Garamond',Georgia,serif; font-size:21pt; font-weight:700;
      color:#fff; line-height:1.05;}}
  .opt1 .pr.gold .v{{color:var(--gold-lt); font-size:25pt;}}
  .opt1 .pr .s{{font-size:7.6pt; color:#9C9288;}}

  .lever{{display:flex; gap:6mm; margin-top:4.5mm;}}
  .lever > div{{flex:1; border-top:2px solid var(--ink); padding-top:2.8mm;}}
  .lever .k{{font-size:7pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .lever .d{{font-size:8.4pt; color:var(--soft); line-height:1.55; margin-top:1.4mm;}}
  .lever .d b{{color:var(--ink);}}

  .mrow.one{{background:var(--deep); border-radius:6px; border-top:0; margin:1mm 0 1.5mm;
      padding:3.6mm 5.5mm; box-shadow:inset 0 0 0 1.5px rgba(201,169,106,.5);}}
  .mrow.one .n{{color:#fff; font-size:13.5pt;}}
  .mrow.one .n small{{color:#C6BFB2;}}
  .mrow.one .n small b{{color:#F0E7D6;}}
  .mrow.one .v{{color:#fff; font-size:15pt;}}
  .mrow.one .v.gold{{color:var(--gold-lt);}}
  .mrow.one .v small{{color:#9C9288;}}
  .tag1{{display:inline-block; padding:1mm 3mm; border-radius:99px; text-align:center;
      background:rgba(201,169,106,.16); border:1px solid rgba(201,169,106,.5);
      font-size:6.6pt; font-weight:700; letter-spacing:.12em; text-transform:uppercase;
      color:var(--gold-lt); line-height:1.3;}}

  .same{{margin-top:5.5mm; background:var(--gold-pale); border-radius:6px;
      padding:4.4mm 6mm 4mm;}}
  .same .hd{{font-family:'Cormorant Garamond',Georgia,serif; font-size:13pt; font-weight:700;
      color:var(--ink); line-height:1.2;}}
  .same .hd em{{color:var(--gold);}}
  .same .grid{{display:grid; grid-template-columns:1fr 1fr; gap:3.2mm 7mm; margin-top:3.2mm;}}
  .same .k{{font-size:6.8pt; letter-spacing:.16em; text-transform:uppercase; color:var(--gold);
      font-weight:700;}}
  .same .d{{font-size:8pt; color:var(--soft); line-height:1.5; margin-top:.8mm;}}
  .p-tec .same{{padding:3.8mm 6mm 3.4mm;}}
  .p-tec .same .grid{{grid-template-columns:repeat(4,1fr); gap:0 5mm; margin-top:2.6mm;}}
  .p-tec .same .d{{font-size:7.6pt; line-height:1.45;}}

  /* ── tabela de preços por móvel */
  .ptab{{width:100%; border-collapse:collapse; margin-top:3mm;}}
  .ptab th{{text-align:right; font-size:6.8pt; letter-spacing:.16em; text-transform:uppercase;
      color:var(--mut); font-weight:700; padding-bottom:1.6mm;}}
  .ptab th:first-child{{text-align:left;}}
  .ptab th.g{{color:var(--gold);}}
  .ptab tr.grp td{{padding:2.7mm 0 1.2mm; border-bottom:1.5px solid var(--ink);
      font-family:'Cormorant Garamond',Georgia,serif; font-size:13pt; font-weight:700;
      color:var(--ink); line-height:1.15;}}
  .ptab tr.grp:first-child td{{padding-top:0;}}
  .ptab tr.grp td em{{font-family:system-ui,sans-serif; font-style:normal; font-size:7.6pt;
      font-weight:400; color:var(--mut);}}
  .ptab td{{padding:1.8mm 0; border-bottom:1px solid var(--hair); vertical-align:middle;}}
  .ptab td.n{{font-size:9pt; color:var(--ink); padding-right:6mm;}}
  .ptab td.n small{{display:block; font-size:7.4pt; color:var(--mut); margin-top:.4mm;
      line-height:1.35;}}
  .ptab td.r{{text-align:right; white-space:nowrap; font-variant-numeric:tabular-nums;
      font-family:'Cormorant Garamond',Georgia,serif; font-size:13pt; font-weight:700;
      width:31mm;}}
  .ptab td.r.g{{color:var(--gold);}}
  .bg-spec{{display:inline-block; margin-left:2.4mm; padding:.4mm 2.4mm; border-radius:99px;
      background:var(--gold-pale); border:1px solid rgba(169,124,21,.35); font-size:6.4pt;
      font-weight:700; letter-spacing:.1em; text-transform:uppercase; color:var(--gold);
      vertical-align:1.2mm;}}

  .menu{{margin-top:3.5mm;}}
  .mrow{{display:grid; grid-template-columns:1fr 30mm 30mm 27mm; gap:4mm; align-items:center;
      border-top:1px solid var(--line); padding:2.5mm 0;}}
  .mrow:first-child{{border-top:2px solid var(--ink);}}
  .mrow .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:12.5pt; font-weight:700;
      line-height:1.15;}}
  .mrow .n small{{display:block; font-family:system-ui,sans-serif; font-size:7.8pt;
      font-weight:400; color:var(--mut); margin-top:1mm; line-height:1.45;}}
  .mrow .v{{text-align:right; font-family:'Cormorant Garamond',Georgia,serif; font-size:13.5pt;
      font-weight:700;}}
  .mrow .v small{{display:block; font-family:system-ui,sans-serif; font-size:6.6pt;
      font-weight:700; letter-spacing:.14em; text-transform:uppercase; color:var(--mut);}}
  .mrow .v.gold{{color:var(--gold);}}
  .econ-p{{display:inline-block; padding:1mm 3.2mm; border-radius:99px; text-align:center;
      background:var(--gold-pale); border:1px solid rgba(169,124,21,.35);
      font-size:7.6pt; font-weight:700; color:var(--gold); white-space:nowrap;}}
  .mnote{{margin-top:3mm; padding-left:4mm; border-left:2px solid var(--gold-lt);
      font-size:7.4pt; color:var(--soft); line-height:1.55;}}
  .mnote b{{color:var(--ink);}}

  /* ── técnico / garantia */
  .hinge{{background:var(--deep); border-left:3px solid var(--gold-lt);
      border-radius:0 5px 5px 0; padding:4.6mm 6.5mm; margin-top:4mm; display:flex; gap:7mm;}}
  .hinge .lead-t{{flex:0 0 50mm;}}
  .hinge .lead-t .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:14.5pt;
      font-weight:700; line-height:1.2; color:#fff;}}
  .hinge .lead-t .k{{font-size:7pt; letter-spacing:.2em; text-transform:uppercase;
      color:var(--gold-lt); font-weight:700; margin-bottom:1.6mm;}}
  .hinge .d{{font-size:8.4pt; color:#C6BFB2; line-height:1.55;}}
  .hinge .d b{{color:#F0E7D6;}}
  .warr-big{{background:var(--deep); border-radius:6px; padding:4.6mm 7mm; margin-top:4mm;
      position:relative; overflow:hidden; box-shadow:inset 0 0 0 1px rgba(201,169,106,.30);}}
  .warr-big::after{{content:""; position:absolute; left:0; top:0; bottom:0; width:4px;
      background:var(--gold-lt);}}
  .warr-big .k{{font-size:7.2pt; letter-spacing:.2em; text-transform:uppercase;
      color:var(--gold-lt); font-weight:700;}}
  .warr-big .big{{font-family:'Cormorant Garamond',Georgia,serif; font-size:21pt; font-weight:700;
      color:#fff; line-height:1.12; margin-top:1.4mm;}}
  .warr-big .d{{font-size:8.4pt; color:#C6BFB2; line-height:1.55; margin-top:2mm;}}
  .warr-big .d b{{color:#F0E7D6;}}
  .pay-lad{{margin-top:3mm;}}
  .pay-lad .r{{display:flex; justify-content:space-between; border-top:1px solid var(--line);
      padding:2.4mm 0; font-size:8.6pt; color:var(--soft);}}
  .pay-lad .r:first-child{{border-top:2px solid var(--ink);}}
  .pay-lad b{{color:var(--ink);}}
  .pay-lad .gold{{color:var(--gold); font-weight:700;}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover">
  <div class="hero-img"><img src="{HERO}" alt=""></div>
  <div class="veil"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria sob medida</div>
      <div class="tit">Apartamento CJ.</div>
      <div class="sub">Projeto B+G Estúdio · Belo Horizonte</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">3 ambientes + adega</div></div>
      <div class="c"><div class="k">Destaque</div><div class="v">Lâmina natural de Freijó</div></div>
      <div class="c"><div class="k">Ferragens</div><div class="v">Hettich · Alemanha</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. CONTRACAPA — A LÂMINA ══════ -->
<div class="page concept"><div class="pad">
  <div class="eyebrow">Lâmina natural de Freijó</div>
  <div class="h-sec serif">A madeira,<br><em style="color:var(--gold-lt);">uma única vez.</em></div>
  <hr class="rule">
  <p class="body-t" style="margin-top:4mm;">
  O melamínico <b>imprime</b> o desenho da madeira — e o repete, chapa após chapa, sempre
  igual. A lâmina natural <b>é</b> a madeira: uma tora de Freijó faqueada em folhas finas
  como papel, na sequência exata em que o veio cresceu dentro do tronco.<br><br>
  Por isso não existem dois móveis iguais em lâmina. O desenho que vai morar na sua
  entrada e na sua varanda <b>não existe em nenhum outro apartamento</b> — e não existirá.</p>

  <div class="texband"><img src="{TEX}" alt=""></div>

  <div class="proc">
    <div><div class="n">01</div><div class="d"><b>Faqueamento.</b> A tora é cortada em
      folhas de ~0,6 mm, mantidas na ordem em que saem — o veio segue de uma folha
      para a outra.</div></div>
    <div><div class="n">02</div><div class="d"><b>Casamento.</b> As folhas são espelhadas
      e emendadas para compor o painel, com o desenho contínuo entre peças vizinhas.</div></div>
    <div><div class="n">03</div><div class="d"><b>Prensagem.</b> A lâmina é prensada
      sobre o MDF e passa a ser a face do móvel — madeira de verdade, estável.</div></div>
    <div><div class="n">04</div><div class="d"><b>Acabamento.</b> Lixamento fino e
      verniz que sela a superfície e mantém o toque da madeira.</div></div>
  </div>

  <div class="objcard">
    <img src="{OBJ}" alt="">
    <div class="cap">Móvel da entrada · frentes em lâmina natural de Freijó — veio contínuo entre as portas</div>
  </div>

  <div class="big-q serif" style="color:#fff; font-size:17pt; margin-top:11mm;">
  Enquanto o melamínico se repete,<br>a lâmina <em style="color:var(--gold-lt);">assina</em>.</div>

  <div class="pfoot" style="color:#8F8578;"><span class="bl" style="color:#EFE9DC;">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════ 3. CONCEITUAL — A LACA ══════ -->
<div class="page concept p-laca"><div class="pad">
  <div class="eyebrow">Laca fosca PU</div>
  <div class="h-sec serif">A cor,<br><em style="color:var(--gold-lt);">sem uma emenda.</em></div>
  <hr class="rule">
  <p class="body-t" style="margin-top:4mm;">
  O melamínico chega pronto da fábrica: a cor vem impressa na face e a borda é uma
  <b>fita colada em volta</b> — sempre há a linha onde a face termina. A laca não é uma
  chapa, é um <b>processo</b>: aplicada sobre o móvel já montado, ela sobe pela face,
  <b>vira a quina e continua</b>. São <b>6,36 m de parede</b> lidos como um volume único,
  numa cor definida pelo B+G Estúdio — não escolhida num catálogo de chapas.</p>

  <div class="texband"><img src="{ELEV}" alt="" style="height:auto;"></div>
  <div class="cap" style="color:#8F8578;margin-top:1.8mm;">Estante das salas · 636 cm de parede em laca fosca — um plano contínuo, sem borda aparente em nenhuma quina</div>

  <div class="proc">
    <div><div class="n">01</div><div class="d"><b>Preparação.</b> O MDF é poroso e bebe
      tinta. Selador, massa nas juntas e lixamento até a superfície ficar plana — a
      etapa que ninguém vê e que decide o resultado.</div></div>
    <div><div class="n">02</div><div class="d"><b>Fundo.</b> Demãos de primer PU com
      lixamento fino entre cada uma. Cada demão fecha o poro que a anterior deixou
      aberto.</div></div>
    <div><div class="n">03</div><div class="d"><b>Cor.</b> Laca PU aplicada em cabine,
      em camadas cruzadas — sem marca de aplicação, sem sombra, sem borda.</div></div>
    <div><div class="n">04</div><div class="d"><b>Cura.</b> A peça descansa dias até o
      poliuretano endurecer por completo. Só então é embalada — é isso que dá a
      resistência ao toque e ao tempo.</div></div>
  </div>

  <div class="split2" style="margin-top:4.5mm;align-items:center;">
    <div style="flex:1;">
      <div class="objcard" style="margin-top:0;">
        <img src="{CRIST}" alt="" style="height:33mm;object-fit:cover;object-position:center 32%;">
        <div class="cap">Caixilho lacado e vidro · a quina é a mesma pele que a face</div>
      </div>
    </div>
    <div style="flex:1.15;">
      <p class="body-t" style="margin:0;">E há o que só a laca permite: <b>ela se recupera</b>.
      Um risco é retocado no próprio móvel, e daqui a dez anos a mesma estante pode receber
      outra cor sem trocar um único módulo. Chapa arranhada se substitui —
      <b>laca se restaura</b>.<br><br>
      É também onde está o custo: não na chapa, mas nas <b>horas de preparo, lixamento e
      pintura de cada face</b>. É por isso que a laca é a maior alavanca de investimento
      deste projeto — e a razão de existirem as configurações das próximas páginas.</p>
    </div>
  </div>

  <div class="big-q serif" style="color:#fff; font-size:16.5pt; margin-top:4.5mm;">
  O melamínico tem borda.<br>A laca tem <em style="color:var(--gold-lt);">silhueta</em>.</div>

  <div class="pfoot" style="color:#8F8578;"><span class="bl" style="color:#EFE9DC;">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════ 4. DESCRITIVO ══════ -->
<div class="page p-esc"><div class="pad">
  <div class="eyebrow">O que será executado</div>
  <div class="h-sec serif">Três ambientes,<br><em>e uma adega.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:4mm;">Fornecimento e instalação, conforme o projeto
  executivo do B+G Estúdio.</p>

  <div class="amb">
    <div class="n">Entrada <span class="badge">lâmina natural</span></div>
    <div class="s">Móvel suspenso em Freijó</div>
    <ul>
      <li>Móvel suspenso com <b>2 gavetões para sapatos</b> e 2 portas, frentes em
          <b>lâmina natural de Freijó</b> com veio contínuo.</li>
      <li><b>Puxador em cava 45°</b> usinado no próprio móvel · interior em Freijó melamínico.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Varanda gourmet <span class="badge">lâmina natural</span></div>
    <div class="s">Ripado em Freijó · bancada de granito da marmoraria</div>
    <ul>
      <li>Armário superior e inferior com <b>portas ripadas em lâmina natural</b> —
          cada ripa acabada individualmente, nas três faces.</li>
      <li>Vão dimensionado para <b>cervejeira</b> · apoio para a bancada de granito.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Salas de TV e jantar <span class="badge">estante · laca fosca</span></div>
    <div class="s">636 × 232 cm · laca fosca PU na cor do projeto</div>
    <ul>
      <li><b>Estante de parede inteira</b>: painel de TV, armários altos, gavetas,
          nichos e <b>cristaleira com 4 portas de vidro</b> e puxadores dourados.</li>
      <li>Executada como <b>móvel novo</b>, em laca fosca — a opção premium do projeto.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Adega <span class="badge">serralheria</span></div>
    <div class="s">Estrutura metálica para vinhos</div>
    <ul>
      <li>Adega vertical em serralheria, integrada à parede da entrada.</li>
    </ul>
  </div>

  <div class="split2" style="margin-top:2mm;">
    <div><div class="figure"><img src="{GOURMET}" alt="" style="height:40mm;object-fit:cover;object-position:center 42%;"></div>
      <div class="cap">Varanda gourmet · ripado em Freijó</div></div>
    <div><div class="figure"><img src="{EST3}" alt="" style="height:40mm;object-fit:cover;object-position:center 55%;"></div>
      <div class="cap">Salas · painel de TV e portas altas</div></div>
    <div><div class="figure"><img src="{EST2}" alt="" style="height:40mm;object-fit:cover;object-position:center 42%;"></div>
      <div class="cap">Cristaleira, nichos e bancada</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════ 5. MIOLO — AS SEIS CONFIGURAÇÕES ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento · as seis configurações</div>
  <div class="h-sec serif" style="font-size:21pt;">Um projeto,<br><em>seis maneiras de chegar lá.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">
  <p class="lead" style="margin-bottom:2mm;">Dois acabamentos respondem por quase todo o
  investimento: a <b>lâmina natural</b> da entrada e da varanda e a <b>laca fosca</b> da
  estante. As seis configurações movem esses dois — e nada mais. Cada valor é o
  <b>projeto completo</b>, sem mudar uma medida sequer.</p>

  <div class="menu">
    <div class="mrow" style="border-top:0; padding:0 0 1.6mm;">
      <div style="font-size:6.8pt; letter-spacing:.18em; text-transform:uppercase; color:var(--mut); font-weight:700;">Configuração</div>
      <div style="font-size:6.8pt; letter-spacing:.18em; text-transform:uppercase; color:var(--gold); font-weight:700; text-align:right;">Projeto à vista</div>
      <div style="font-size:6.8pt; letter-spacing:.18em; text-transform:uppercase; color:var(--mut); font-weight:700; text-align:right;">Parcelado</div>
      <div style="font-size:6.8pt; letter-spacing:.18em; text-transform:uppercase; color:var(--mut); font-weight:700;">vs. opção 1</div>
    </div>
    <div class="mrow one">
      <div class="n">1 · Integral — lâmina natural + laca fosca completa
        <small>Entrada e varanda em <b>lâmina natural de Freijó</b> · estante inteira em
        <b>laca fosca</b>, por dentro e por fora. A especificação do B+G Estúdio, sem
        nenhuma substituição.</small></div>
      <div class="v gold">R$ 76.100<small>à vista</small></div>
      <div class="v">R$ 84.600<small>parcelado</small></div>
      <div><span class="tag1">como o projeto pede</span></div>
    </div>
    <div class="mrow" style="border-top:0;">
      <div class="n">2 · Entrada + varanda em melamínico Freijó
        <small>O móvel fica <b>100% em melamínico Freijó Puro — por fora e por dentro</b>.
        Ripado e cava permanecem. A estante das salas segue <b>integral, em laca</b>.</small></div>
      <div class="v gold">R$ 65.500<small>à vista</small></div>
      <div class="v">R$ 72.800<small>parcelado</small></div>
      <div><span class="econ-p">economiza R$ 11.800</span></div>
    </div>
    <div class="mrow">
      <div class="n">3 · Estante: laca por fora · melamínico fosco na cor por dentro
        <small>A laca permanece em <b>tudo o que se vê de frente</b>; o interior dos
        armários vai em melamínico fosco <b>na mesma cor</b> — e não em branco. Lâmina
        natural <b>mantida</b> na entrada e na varanda.</small></div>
      <div class="v gold">R$ 64.300<small>à vista</small></div>
      <div class="v">R$ 71.400<small>parcelado</small></div>
      <div><span class="econ-p">economiza R$ 13.200</span></div>
    </div>
    <div class="mrow">
      <div class="n">4 · Estante sem laca — melamínico na cor, por inteiro
        <small>Dentro e fora na cor do projeto, em melamínico fosco. Lâmina natural
        <b>mantida</b> na entrada e na varanda.</small></div>
      <div class="v gold">R$ 48.700<small>à vista</small></div>
      <div class="v">R$ 54.100<small>parcelado</small></div>
      <div><span class="econ-p">economiza R$ 30.500</span></div>
    </div>
    <div class="mrow">
      <div class="n">5 · Estante sem laca — cor por fora · branco por dentro
        <small>Faces externas em melamínico na cor; todo o miolo em branco TX, inclusive
        atrás dos vidros da cristaleira. Os nichos abertos seguem na cor.</small></div>
      <div class="v gold">R$ 46.700<small>à vista</small></div>
      <div class="v">R$ 51.900<small>parcelado</small></div>
      <div><span class="econ-p">economiza R$ 32.700</span></div>
    </div>
    <div class="mrow">
      <div class="n">6 · Projeto 100% melamínico — sem lâmina, sem laca
        <small>Entrada e varanda <b>100% em melamínico Freijó Puro</b> · estante na cor
        por fora e branco TX por dentro (configurações 2 + 5). O desenho inteiro
        permanece — ripado, cava, cristaleira, Hettich.</small></div>
      <div class="v gold">R$ 36.100<small>à vista</small></div>
      <div class="v">R$ 40.100<small>parcelado</small></div>
      <div><span class="econ-p">economiza R$ 44.500</span></div>
    </div>
  </div>

  <div class="mnote">
    <b>Como comparar:</b> a conta fecha na sua frente — a configuração 6 é a soma da 2 com
    a 5: R$ 72.800 + R$ 51.900 − R$ 84.600 = <b>R$ 40.100</b>. Some as linhas que quiser.
    Entre a 4 e a 5 há apenas <b>R$ 2.200</b>: trocar o miolo por branco quase não muda o
    preço — <b>o que move o preço é a laca</b> (página 3). Em todas elas, medidas, ferragens
    Hettich, vidros e garantia são <b>exatamente os mesmos</b>.
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════ 6. PREÇO POR MÓVEL ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento · móvel a móvel</div>
  <div class="h-sec serif" style="font-size:21pt;">Monte a sua<br><em>combinação.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">
  <p class="lead" style="margin-bottom:0;">As seis configurações são as combinações mais
  prováveis — mas você não está preso a elas. Aqui está <b>cada móvel em cada versão</b>:
  some as linhas que quiser, em qualquer uma das colunas — a de <b>à vista</b> já traz os
  10% aplicados linha a linha.</p>

  <table class="ptab">
    <tr><th>Móvel e versão</th><th class="g">À vista</th><th>Parcelado</th></tr>

    <tr class="grp"><td colspan="3">Entrada <em>· móvel suspenso, 2 gavetões e 2 portas</em></td></tr>
    <tr><td class="n">Lâmina natural de Freijó<span class="bg-spec">projeto B+G</span>
        <small>Frentes em lâmina com veio contínuo · interior em Freijó melamínico</small></td>
      <td class="r g">R$ 7.900</td><td class="r">R$ 8.800</td></tr>
    <tr><td class="n">100% melamínico Freijó Puro
        <small>Por fora e por dentro, no mesmo tom · cava a 45° mantida</small></td>
      <td class="r g">R$ 4.500</td><td class="r">R$ 5.000</td></tr>

    <tr class="grp"><td colspan="3">Varanda gourmet <em>· armário superior e inferior, portas ripadas</em></td></tr>
    <tr><td class="n">Lâmina natural de Freijó<span class="bg-spec">projeto B+G</span>
        <small>Cada ripa acabada individualmente, nas três faces</small></td>
      <td class="r g">R$ 12.600</td><td class="r">R$ 14.000</td></tr>
    <tr><td class="n">100% melamínico Freijó Puro
        <small>Ripado mantido, executado em melamínico no mesmo tom</small></td>
      <td class="r g">R$ 5.400</td><td class="r">R$ 6.000</td></tr>

    <tr class="grp"><td colspan="3">Salas de TV e jantar <em>· estante de 636 cm, com cristaleira</em></td></tr>
    <tr><td class="n">Laca fosca completa<span class="bg-spec">projeto B+G</span>
        <small>Por dentro e por fora, na cor do projeto</small></td>
      <td class="r g">R$ 54.400</td><td class="r">R$ 60.500</td></tr>
    <tr><td class="n">Laca fosca por fora · melamínico fosco na cor por dentro
        <small>A laca em tudo o que se vê de frente; interior na mesma cor, não em branco</small></td>
      <td class="r g">R$ 42.600</td><td class="r">R$ 47.300</td></tr>
    <tr><td class="n">Melamínico na cor, por inteiro
        <small>Sem laca · dentro e fora na cor do projeto, em melamínico fosco</small></td>
      <td class="r g">R$ 27.000</td><td class="r">R$ 30.000</td></tr>
    <tr><td class="n">Melamínico na cor por fora · branco TX por dentro
        <small>Miolo branco, inclusive atrás dos vidros · nichos abertos seguem na cor</small></td>
      <td class="r g">R$ 25.000</td><td class="r">R$ 27.800</td></tr>

    <tr class="grp"><td colspan="3">Adega <em>· serralheria sob medida</em></td></tr>
    <tr><td class="n">Estrutura metálica para vinhos<span class="bg-spec">projeto B+G</span>
        <small>Vertical, integrada à parede da entrada</small></td>
      <td class="r g">R$ 1.200</td><td class="r">R$ 1.300</td></tr>
  </table>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════ 7. TÉCNICO ══════ -->
<div class="page p-tec"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="h-sec serif">O que está por dentro<br><em>do que você não vê.</em></div>
  <hr class="rule">

  <table class="spec-tb" style="margin-top:3mm;">
    <thead><tr><th>Item</th><th>Especificação</th></tr></thead>
    <tbody>
      <tr><td>Lâmina natural</td><td><b>Freijó faqueado</b>, aplicado e acabado com verniz —
        faces externas da entrada e da varanda, ripas acabadas nas três faces.</td></tr>
      <tr><td>Laca</td><td><b>Laca fosca PU</b> na cor do projeto, sobre MDF preparado —
        superfície contínua, sem poro aparente.</td></tr>
      <tr><td>Interior dos móveis</td><td><b>Freijó melamínico</b> nos móveis de lâmina —
        o tom continua ao abrir a porta.</td></tr>
      <tr><td>Dobradiças</td><td><b>Hettich Sensys</b>, com amortecimento integrado e
        <b>garantia vitalícia da ferragem</b>.</td></tr>
      <tr><td>Corrediças</td><td><b>Hettich Actro 5D</b> nos gavetões — regulagem em 5
        dimensões, abertura total · <b>Quadro V6</b> ocultas nas gavetas.</td></tr>
      <tr><td>Puxadores</td><td><b>Cava 45° usinada</b> no próprio móvel · <b>bolinha
        dourado fosco</b> na cristaleira, conforme projeto.</td></tr>
      <tr><td>Vidros</td><td>Incolor nas 4 portas da cristaleira, com caixilho em laca.</td></tr>
      <tr><td>Adega</td><td>Serralheria sob medida para garrafas, fixada na alvenaria.</td></tr>
    </tbody>
  </table>

  <div class="hinge">
    <div class="lead-t">
      <div class="k">Ferragem alemã</div>
      <div class="t">Hettich<br>Sensys.</div>
    </div>
    <div class="d">O amortecimento fica <b>dentro do corpo da dobradiça</b> — a porta
    desacelera sozinha e encosta macia em qualquer velocidade. Cada uma é testada para
    <b>80 mil ciclos</b>, e a ferragem tem <b>garantia vitalícia</b> do fabricante.<br><br>
    Nos gavetões, a <b>Actro 5D</b> ajusta a frente em cinco dimensões — é o que mantém
    as frestas perfeitas anos depois da instalação.</div>
  </div>

  <div class="same" style="margin-top:4.5mm;">
    <div class="hd">Tudo desta página vale para as <em>seis</em> configurações</div>
    <div class="grid">
      <div><div class="k">Projeto</div><div class="d">Todas as medidas do executivo
        B+G — os 636 cm, o ripado, a cava a 45°.</div></div>
      <div><div class="k">Ferragens</div><div class="d">Hettich Sensys · Actro 5D ·
        Quadro V6, com garantia vitalícia.</div></div>
      <div><div class="k">Cristaleira</div><div class="d">As 4 portas de vidro e os
        puxadores em dourado fosco.</div></div>
      <div><div class="k">Garantia</div><div class="d">10 anos em contrato — igual na
        configuração 1 e na 6.</div></div>
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════ 8. GARANTIA + CONDIÇÕES ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Garantia e condições</div>
  <div class="h-sec serif">O que assinamos<br><em>junto com o móvel.</em></div>
  <hr class="rule">

  <div class="warr-big">
    <div class="k">Garantia</div>
    <div class="big">10 anos. Em contrato.</div>
    <div class="d">Marcenaria sob medida costuma sair com <b>1 a 3 anos</b> de garantia —
    quando sai por escrito. A nossa é de <b>10 anos</b> sobre estrutura, montagem e
    acabamento, mais <b>2 anos</b> de instalação e regulagem — e a ferragem Hettich tem
    <b>garantia vitalícia</b> do fabricante. Conseguimos assinar isso porque a equipe é
    <b>própria do corte à instalação</b>.</div>
  </div>

  <div class="lever" style="margin-top:4.5mm;">
    <div>
      <div class="k">Formas de pagamento</div>
      <div class="pay-lad">
        <div class="r"><span>Entrada 30% + até 10× no cartão</span><b>valor de tabela</b></div>
        <div class="r"><span>Entrada 50% + até 8× no cartão</span><b>−4%</b></div>
        <div class="r"><span>Entrada 70% + até 6× no cartão</span><b>−7%</b></div>
        <div class="r"><span>À vista / transferência</span><span class="gold">−10%</span></div>
      </div>
    </div>
    <div>
      <div class="k">Condições</div>
      <div class="pay-lad">
        <div class="r"><span>Prazo de entrega</span><b>50 a 60 dias corridos</b></div>
        <div class="r"><span>Validade da proposta</span><b>15 dias corridos</b></div>
        <div class="r"><span>Medição</span><b>conferida no local</b></div>
        <div class="r"><span>Ferragens</span><b>Hettich · Alemanha</b></div>
      </div>
      <div class="mnote" style="margin-top:3mm;">
        <b>Não incluso:</b> espelhos · relaqueamento do móvel existente (avaliação in loco) ·
        granito e frontão (marmoraria) · pontos elétricos.
      </div>
    </div>
  </div>

  <div class="figure" style="margin-top:4.5mm;"><img src="{GOURMET}" alt="" style="height:62mm;object-fit:cover;object-position:center 60%;"></div>
  <div class="cap">Varanda gourmet · a marcenaria que recebe — e envelhece bem</div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio · 28/07/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-apto-cj-folder.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-apto-cj-folder.html', len(HTML))
