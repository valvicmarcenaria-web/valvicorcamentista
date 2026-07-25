# -*- coding: utf-8 -*-
"""Proposta PREMIUM — Apartamento CJ (B+G Estúdio). 5 páginas.
Copy no estilo Light Copy (Leandro Ladeira): premissa antes da promessa,
quebra de objeção, prova concreta. Imagens extraídas do caderno do projeto."""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

HERO   = open('/tmp/uri_cj_hero.txt').read()
RIPADO = open('/tmp/uri_cj_ripado.txt').read()
LACA   = open('/tmp/uri_cj_laca.txt').read()
PUX    = open('/tmp/uri_cj_pux.txt').read()

CSS = """
:root{
  --ink:#1A1714; --soft:#5F594F; --mut:#928B7D; --line:#E2DCD0; --hair:#EFEAE0;
  --paper:#fff; --cream:#FAF7F1; --sand:#F2ECE1;
  --gold:#9C7A3C; --gold-lt:#C9A96A; --gold-pale:#F3EADA;
  --deep:#2A2521;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans','Liberation Sans',Arial,sans-serif;color:var(--ink);
     font-size:10.2pt;line-height:1.6;}
.serif{font-family:'Cormorant Garamond',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;background:var(--paper);
      page-break-after:always;}
.page:last-child{page-break-after:auto;}
.pad{padding:17mm 19mm 15mm;height:100%;}
h1,h2,h3{margin:0;font-weight:600;}
p{margin:0;}
.eyebrow{font-size:7.6pt;letter-spacing:.3em;text-transform:uppercase;color:var(--gold);font-weight:700;}
.rule{height:1.5px;width:42px;background:var(--gold-lt);border:0;margin:10px 0 12px;}
.h-sec{font-family:'Cormorant Garamond',Georgia,serif;font-size:25pt;font-weight:700;line-height:1.08;}
.h-sec em{font-style:italic;color:var(--gold);}
.lead{font-family:'Cormorant Garamond',Georgia,serif;font-size:13pt;font-style:italic;
      color:var(--soft);line-height:1.5;}
.pfoot{position:absolute;left:19mm;right:19mm;bottom:11mm;display:flex;justify-content:space-between;
       font-size:7pt;color:var(--mut);letter-spacing:.12em;border-top:1px solid var(--hair);padding-top:2.5mm;}
.bl{font-family:'Cormorant Garamond',Georgia,serif;font-weight:700;letter-spacing:.14em;}
.bl .d{color:var(--gold);}

/* ---------- CAPA ---------- */
.cover{background:var(--deep);color:#F5F1E8;padding:0;}
.cover .hero-img{position:absolute;inset:0;}
.cover .hero-img img{width:100%;height:100%;object-fit:cover;opacity:.92;display:block;}
.cover .veil{position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(26,23,20,.72) 0%,rgba(26,23,20,.30) 30%,rgba(26,23,20,.55) 62%,rgba(26,23,20,.93) 100%);}
.cover .inner{position:relative;height:100%;padding:20mm 20mm 16mm;display:flex;flex-direction:column;}
.cover .brand{font-family:'Cormorant Garamond',Georgia,serif;font-size:27pt;font-weight:700;letter-spacing:.2em;}
.cover .brand .d{color:var(--gold-lt);}
.cover .bsub{letter-spacing:.5em;font-size:6.8pt;font-weight:700;color:var(--gold-lt);margin-top:2px;}
.cover .mid{margin-top:96mm;}
.cover .kick{font-size:8pt;letter-spacing:.32em;text-transform:uppercase;color:var(--gold-lt);font-weight:700;}
.cover .tit{font-family:'Cormorant Garamond',Georgia,serif;font-size:37pt;font-weight:700;line-height:1.04;margin:5mm 0 3mm;}
.cover .sub{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:14pt;color:#D9D2C4;}
.cover .strip{position:absolute;left:20mm;right:20mm;bottom:16mm;display:flex;gap:8mm;
  border-top:1px solid rgba(201,169,106,.4);padding-top:5mm;}
.cover .strip .c .k{font-size:6.6pt;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-lt);font-weight:700;}
.cover .strip .c .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:12pt;font-weight:700;margin-top:1mm;}

/* ---------- COPY ---------- */
.big-q{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;line-height:1.32;color:var(--ink);}
.big-q b{color:var(--gold);font-weight:700;}
.body-t{font-size:10.2pt;color:var(--soft);line-height:1.72;}
.body-t b{color:var(--ink);}
.split2{display:flex;gap:9mm;}
.split2>div{flex:1;}
.figure{border-radius:5px;overflow:hidden;background:var(--sand);}
.figure img{width:100%;display:block;}
.cap{font-size:7.4pt;color:var(--mut);letter-spacing:.1em;text-transform:uppercase;margin-top:2.5mm;}
.pull{background:var(--gold-pale);border-left:3px solid var(--gold-lt);padding:5mm 6mm;border-radius:0 5px 5px 0;}
.pull .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;font-weight:700;line-height:1.25;}
.pull .d{font-size:9pt;color:var(--soft);margin-top:2mm;line-height:1.6;}

/* ---------- ESCOPO / TÉCNICO ---------- */
.amb{border-top:2px solid var(--ink);padding-top:3.5mm;margin-bottom:6mm;}
.amb .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;font-weight:700;}
.amb .s{font-size:7.2pt;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-top:.8mm;}
.amb ul{margin:2.5mm 0 0;padding-left:4.5mm;font-size:9.1pt;color:var(--soft);line-height:1.62;}
.amb li{margin:1.2mm 0;}
.amb b{color:var(--ink);}
.spec-tb{width:100%;border-collapse:collapse;font-size:8.8pt;margin-top:2mm;}
.spec-tb th{text-align:left;font-size:6.8pt;letter-spacing:.16em;text-transform:uppercase;color:var(--mut);
            font-weight:700;border-bottom:1.5px solid var(--ink);padding:0 0 2mm;}
.spec-tb td{padding:2.4mm 0;border-bottom:1px solid var(--hair);color:var(--soft);vertical-align:top;}
.spec-tb td:first-child{font-weight:600;color:var(--ink);width:44mm;padding-right:4mm;}
.badge{display:inline-block;background:var(--gold-pale);color:var(--gold);font-size:7pt;font-weight:700;
       letter-spacing:.1em;text-transform:uppercase;padding:1mm 2.5mm;border-radius:3px;}

/* ---------- INVESTIMENTO ---------- */
.inv-hero{border:1.5px solid var(--ink);border-radius:7px;padding:7mm 8mm;position:relative;}
.inv-hero .k{font-size:7.4pt;letter-spacing:.2em;text-transform:uppercase;color:var(--mut);font-weight:700;}
.inv-hero .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:31pt;font-weight:700;line-height:1;margin:3mm 0 1mm;}
.inv-hero .c{font-size:8.8pt;color:var(--soft);}
.pay-tb{width:100%;border-collapse:collapse;font-size:9.2pt;margin-top:5mm;}
.pay-tb th{text-align:left;font-size:6.8pt;letter-spacing:.16em;text-transform:uppercase;color:var(--mut);
           font-weight:700;border-bottom:1.5px solid var(--ink);padding:0 0 2mm;}
.pay-tb td{padding:2.8mm 0;border-bottom:1px solid var(--hair);}
.pay-tb td.r{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap;}
.pay-tb tr.best td{background:var(--gold-pale);font-weight:700;color:var(--ink);}
.pay-tb tr.best td:first-child{padding-left:3mm;border-radius:4px 0 0 4px;}
.pay-tb tr.best td:last-child{padding-right:3mm;border-radius:0 4px 4px 0;color:var(--gold);}
.terms{display:flex;gap:5mm;margin-top:5mm;}
.term{flex:1;border:1px solid var(--line);border-radius:5px;padding:4mm 4.5mm;text-align:center;}
.term .k{font-size:6.6pt;letter-spacing:.16em;text-transform:uppercase;color:var(--mut);font-weight:700;}
.term .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:12.5pt;font-weight:700;margin-top:1mm;line-height:1.15;}
.note{margin-top:5mm;padding-left:4mm;border-left:2px solid var(--gold-lt);font-size:8pt;color:var(--soft);line-height:1.55;}
.note b{color:var(--ink);}
"""

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>

<!-- ══════════ 1. CAPA ══════════ -->
<div class="page cover">
  <div class="hero-img"><img src="{HERO}" alt=""></div>
  <div class="veil"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria</div>
      <div class="tit">Lâmina natural<br>e laca fosca.</div>
      <div class="sub">Apartamento CJ · Belo Horizonte — projeto B+G Estúdio</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Ambientes</div><div class="v">Entrada · Varanda · Salas</div></div>
      <div class="c"><div class="k">Acabamentos</div><div class="v">Louro freijó · Laca N048/X148</div></div>
      <div class="c"><div class="k">Ferragens</div><div class="v">Hettich</div></div>
    </div>
  </div>
</div>

<!-- ══════════ 2. COPY — A NOBREZA DO MATERIAL ══════════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Antes do preço, o material</div>
  <hr class="rule">
  <div class="big-q serif">Existe uma diferença entre um móvel que <b>imita</b> madeira<br>
  e um móvel que <b>é</b> madeira.</div>

  <p class="body-t" style="margin-top:6mm;">
  Ela não aparece na foto. Aparece quando você passa a mão.<br><br>
  A <b>lâmina natural de louro freijó</b> é madeira de verdade — fatiada em folhas finíssimas e aplicada
  peça por peça. Cada porta do seu móvel vai ter um desenho de veio que <b>não se repete em lugar nenhum
  do mundo</b>. Não é um padrão impresso que se repete a cada 30 centímetros: é a árvore, do jeito que
  ela cresceu.<br><br>
  E a <b>laca fosca</b> é o oposto exato disso — e é justamente por isso que as duas convivem tão bem.
  Onde a lâmina tem textura e movimento, a laca tem silêncio: uma superfície contínua, sem emenda visível,
  sem poro, sem brilho que denuncie marca de dedo. Sete demãos entre fundo, lixamento e acabamento para
  chegar num plano que parece esculpido de uma peça só.</p>

  <div style="margin-top:7mm;" class="split2">
    <div>
      <div class="figure"><img src="{RIPADO}" alt=""></div>
      <div class="cap">Varanda gourmet · ripado em lâmina natural freijó</div>
    </div>
    <div style="display:flex;flex-direction:column;justify-content:center;">
      <div class="pull">
        <div class="t">50 ripas. 3 faces cada.<br>Uma só direção de veio.</div>
        <div class="d">O ripado da varanda é a peça mais exigente do projeto. Cada ripa recebe lâmina em
        três faces e é posicionada para que o veio corra contínuo de uma ponta à outra do móvel — como se
        o painel inteiro tivesse sido cortado de uma única tábua.<br><br>
        É o tipo de detalhe que ninguém consegue explicar por que ficou bonito. Só sente.</div>
      </div>
    </div>
  </div>

  <p class="body-t" style="margin-top:6mm;">
  <b>A premissa é simples:</b> material nobre não perdoa execução mediana. Lâmina mal aplicada descola
  na emenda. Laca mal preparada marca. Por isso a proposta abaixo não é só sobre o que você leva —
  é sobre <b>como</b> vai ser feito.</p>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════════ 3. ESCOPO ══════════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">O que será executado</div>
  <div class="h-sec serif">Três ambientes,<br><em>um mesmo padrão.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:7mm;">Escopo lido prancha a prancha do caderno do B+G Estúdio,
  decomposto em plano de corte antes de qualquer chapa entrar na serra.</p>

  <div class="amb">
    <div class="n">Móvel de entrada</div>
    <div class="s">238 × 40 × 45 · suspenso · lâmina louro freijó</div>
    <ul>
      <li>Suspenso com recuo inferior de 2 cm — o móvel parece flutuar sobre o mármore.</li>
      <li><b>2 gavetões para sapatos</b> + 2 portas de abrir, com prateleira interna.</li>
      <li><b>Puxador cava 45°</b> usinado na face superior — sem ferragem aparente.</li>
      <li>Faces externas em <b>lâmina natural de louro freijó</b>; interior em <b>MDF melamínico Freijó Puro</b>.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Marcenaria da varanda / gourmet <span class="badge">peça-chave</span></div>
    <div class="s">Superior 140 × 66 × 32 + inferior 95,5 × 69 × 61 · ripado</div>
    <ul>
      <li>Módulo superior com <b>3 portas de abrir</b>; módulo inferior com <b>2 portas</b> e prateleira.</li>
      <li><b>Ripado em lâmina natural freijó</b> — 50 ripas de 3 cm, acabadas em 3 faces.</li>
      <li>Vão de 44 cm reservado para a <b>cervejeira</b>; puxador cava 45°.</li>
      <li>Interior em <b>MDF melamínico Freijó Puro</b>, com prateleira.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Salas de TV e jantar</div>
    <div class="s">636 × 232 × 47 · laca fosca Sayerlack N048 ou X148</div>
    <ul>
      <li><b>Painel de TV</b> e armários altos, com prateleira superior em laca de <b>3 cm de espessura</b>.</li>
      <li><b>Cristaleira</b> de 138,5 cm — 4 portas de abrir em vidro incolor, profundidade recuada 32 cm,
          <b>puxadores bolinha dourado fosco</b>.</li>
      <li>Módulo de nichos e base de 136,5 cm.</li>
      <li>Executado como <b>móvel novo</b> (opção prevista no projeto), em laca fosca sobre MDF branco;
          interior em <b>MDF melamínico</b>.</li>
    </ul>
  </div>

  <div class="split2" style="margin-top:1mm;">
    <div style="flex:2.4;">
      <div class="figure"><img src="{LACA}" alt=""></div>
      <div class="cap">Salas TV e jantar · elevação frontal — 636 cm em laca fosca</div>
    </div>
    <div style="flex:1;">
      <div class="figure"><img src="{PUX}" alt=""></div>
      <div class="cap">Puxador bolinha<br>dourado fosco</div>
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════════ 4. TÉCNICO ══════════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="h-sec serif">O que está por dentro<br><em>do que você não vê.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:6mm;">Toda marcenaria parece boa no dia da entrega.
  A diferença aparece no terceiro ano.</p>

  <table class="spec-tb">
    <thead><tr><th>Item</th><th>Especificação</th></tr></thead>
    <tbody>
      <tr><td>Lâmina natural</td><td>Louro freijó em folha natural, aplicada nas <b>faces externas</b>
        e acabada com selador e verniz. Veio orientado e casado entre peças adjacentes.</td></tr>
      <tr><td>Laca</td><td><b>Sayerlack fosca N048 ou X148</b> sobre MDF branco — fundo, lixamento
        intermediário e acabamento. Superfície contínua, sem poro aparente.</td></tr>
      <tr><td>Parte interna</td><td><b>MDF melamínico Freijó Puro</b> nos módulos de lâmina e
        <b>MDF melamínico</b> nos módulos de laca — resistente a risco, umidade e limpeza diária.</td></tr>
      <tr><td>Estrutura</td><td>MDF <b>15 mm</b> em caixaria e portas · <b>18 mm</b> em prateleiras
        (evita flecha no vão longo) · <b>6 mm</b> em fundos · prateleira da TV em <b>3 cm</b>.</td></tr>
      <tr><td>Dobradiças</td><td><b>Hettich Sensys</b> com amortecimento integrado — 40 unidades.
        Fecho suave em qualquer velocidade. <b>Garantia vitalícia do fabricante.</b></td></tr>
      <tr><td>Corrediças</td><td><b>Hettich Actro 5D</b> nos gavetões da entrada (regulagem em 5 eixos,
        carga até 40 kg) e <b>Quadro V6</b> nas gavetas do painel — abertura total, retorno silencioso.</td></tr>
      <tr><td>Puxadores</td><td>Cava 45° usinada na própria peça (entrada e varanda) ·
        bolinha dourado fosco na cristaleira.</td></tr>
      <tr><td>Vidros</td><td>Incolor nas 4 portas da cristaleira — fornecimento e instalação
        coordenados pela Valvic.</td></tr>
      <tr><td>Emendas</td><td>O móvel das salas tem 636 cm — acima da chapa. As juntas são
        <b>projetadas para cair em linha de módulo</b>, alinhadas e simétricas.</td></tr>
    </tbody>
  </table>

  <div class="split2" style="margin-top:6mm;">
    <div class="pull" style="background:var(--cream);border-left-color:var(--ink);">
      <div class="t">Garantia</div>
      <div class="d"><b>5 anos</b> na marcenaria (estrutura, montagem e acabamento).<br>
      <b>Vitalícia</b> nas dobradiças Hettich, direto do fabricante.<br>
      <b>2 anos</b> na instalação e regulagem.<br><br>
      Garantia formal, assinada em contrato — não é promessa verbal.</div>
    </div>
    <div class="pull">
      <div class="t">Equipe própria,<br>do corte à instalação</div>
      <div class="d">Quem projeta é quem produz é quem instala. Sem terceirização de montagem —
      a responsabilidade não muda de mão no meio do caminho.<br><br>
      Produção em <b>CNC próprio</b>: cada peça sai do plano de corte conferido, não do improviso de obra.</div>
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio</span></div>
</div></div>

<!-- ══════════ 5. INVESTIMENTO ══════════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif">Uma execução completa,<br><em>do corte à instalação.</em></div>
  <hr class="rule">

  <div class="inv-hero" style="margin-top:5mm;">
    <div class="k">Investimento total</div>
    <div class="v serif">R$ 83.100</div>
    <div class="c">Móvel de entrada, marcenaria da varanda/gourmet e marcenaria das salas de TV e jantar —
    material, ferragens Hettich, acabamento, fornecimento e instalação por equipe própria Valvic.</div>
  </div>

  <table class="pay-tb">
    <thead><tr><th>Condição de pagamento</th><th class="r">Desconto</th><th class="r">Valor final</th></tr></thead>
    <tbody>
      <tr><td>Entrada 30% + saldo em até 10× no cartão</td><td class="r">—</td><td class="r">R$ 83.100</td></tr>
      <tr><td>Entrada 50% + saldo em até 8× no cartão</td><td class="r">4%</td><td class="r">R$ 79.800</td></tr>
      <tr><td>Entrada 70% + saldo em até 6× no cartão</td><td class="r">7%</td><td class="r">R$ 77.300</td></tr>
      <tr class="best"><td>À vista / transferência</td><td class="r">10%</td><td class="r">R$ 74.800</td></tr>
    </tbody>
  </table>
  <p style="font-size:8pt;color:var(--soft);margin-top:2.5mm;">
  O desconto à vista não é cortesia: é a <b>taxa de parcelamento que deixamos de pagar</b> à operadora,
  devolvida integralmente para você.</p>

  <div class="terms">
    <div class="term"><div class="k">Prazo</div><div class="v">50 a 60<br>dias úteis</div></div>
    <div class="term"><div class="k">Garantia</div><div class="v">5 anos<br><span style="font-size:7.6pt;font-family:'DM Sans',sans-serif;font-weight:400;color:var(--soft);">vitalícia nas Hettich</span></div></div>
    <div class="term"><div class="k">Validade</div><div class="v">7 dias<br>corridos</div></div>
  </div>

  <div class="note">
    <b>Incluso:</b> marcenaria dos três ambientes, ferragens Hettich, lâmina natural aplicada e acabada,
    laca fosca, vidros da cristaleira, fornecimento e instalação.<br>
    <b>Não incluso:</b> espelho · manutenção/relaqueamento do móvel existente (exige avaliação in loco) ·
    serralheria da adega · futton estofado · granito/frontão da bancada (marmoraria) · ponto elétrico do
    nicho (eletricista) · retirada e descarte do móvel antigo.<br>
    <b>Premissas:</b> medidas do caderno conferidas no local antes da produção. Laca N048 ou X148 e
    tonalidade da lâmina a definir em amostra física antes do início.
  </div>

  <div style="margin-top:7mm;padding-top:5mm;border-top:1px solid var(--hair);">
    <div class="h-sec serif" style="font-size:17pt;">Qual o próximo passo?</div>
    <p class="body-t" style="margin-top:2mm;">Aprovada a proposta, agendamos a <b>medição final</b> e
    apresentamos as <b>amostras físicas</b> de lâmina e laca antes de qualquer corte. Nada entra em
    produção sem o seu aceite na amostra.</p>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Apartamento CJ · B+G Estúdio · 22/07/2026</span></div>
</div></div>

</body></html>"""

(P/'proposta-apto-cj.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-apto-cj.html', len(HTML))
