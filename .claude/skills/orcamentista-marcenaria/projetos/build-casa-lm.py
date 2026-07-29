# -*- coding: utf-8 -*-
"""Proposta PREMIUM — Casa L&M · Alphaville. 5 páginas, sistema visual Apto CJ/TRT.
Renders extraídos do próprio caderno técnico da arquiteta."""
import pathlib
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

HERO  = open('/tmp/uri_lm_p31_0.txt').read()   # closet suíte — capa
SALA  = open('/tmp/uri_lm_p08_3.txt').read()   # sala de jantar / painel
COZ   = open('/tmp/uri_lm_p18_1.txt').read()   # cozinha
BANHO = open('/tmp/uri_lm_p39_4.txt').read()   # banheiro
SUITE = open('/tmp/uri_lm_p31_3.txt').read()   # suíte
CURVA = open('/tmp/uri_lm_curva.txt').read()    # closet — terminação curva
CSS   = open('/tmp/css_premium.txt', encoding='utf-8').read().split('CSS = """')[1].rsplit('"""',1)[0]

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style>
<style>
  .cover .hero-img img{{object-position:center 55%;}}
  .cover .veil{{background:linear-gradient(180deg,
      rgba(22,17,14,.86) 0%, rgba(22,17,14,.34) 26%, rgba(22,17,14,.12) 48%,
      rgba(22,17,14,.55) 76%, rgba(22,17,14,.93) 100%);}}
  .cover .hero-img img{{filter:brightness(1.28) saturate(1.06);}}
  .p-esc .h-sec{{font-size:20pt;}}
  .p-esc .amb{{padding-top:2.2mm; margin-bottom:2.5mm;}}
  .p-esc .amb ul{{line-height:1.44; margin-top:1.5mm; font-size:8.9pt;}}
  .p-esc .amb li{{margin:.5mm 0;}}
  .band{{height:100%; padding:4.5mm 5.5mm;}}
  .band .t{{font-size:12.5pt;}}
  .band .d{{font-size:8.5pt; line-height:1.55; margin-top:1.6mm;}}
  .amb .n small{{font-family:system-ui,sans-serif; font-size:7.4pt; font-weight:400;
      letter-spacing:.02em; color:var(--mut); margin-left:2mm;}}
  /* prova em números — benefícios com evidência */
  .stats{{display:flex; gap:7mm; margin-top:9mm;}}
  .stats > div{{flex:1; border-top:2px solid var(--ink); padding-top:3.2mm;}}
  .stats .n{{font-family:'Cormorant Garamond',Georgia,serif; font-size:27pt;
      font-weight:700; line-height:1; color:var(--gold);}}
  .stats .n em{{font-style:normal; font-size:13pt;}}
  .stats .t{{font-size:8.3pt; color:var(--soft); line-height:1.52; margin-top:2mm;}}
  .stats .t b{{color:var(--ink);}}
  /* destaque sutil do valor à vista */
  .hero-vista{{box-shadow:inset 0 0 0 1px rgba(201,169,106,.30);}}
  .hero-vista .v{{display:inline-block;}}
  .vtag{{font-family:system-ui,-apple-system,sans-serif; font-size:7.6pt; font-weight:700;
      letter-spacing:.22em; text-transform:uppercase; color:var(--gold-lt);
      vertical-align:middle; margin-left:4mm;}}
  .vrule{{width:26mm; height:1.5px; background:var(--gold-lt); opacity:.85;
      margin:1mm 0 2.4mm;}}
  .p-inv .inv-hero{{padding:4.6mm 7mm;}}
  .pr-tab{{margin-top:1.4mm;}}
  .pr-tab span{{font-family:system-ui,-apple-system,sans-serif; font-size:7.2pt;
      letter-spacing:.18em; text-transform:uppercase; color:#8F8578; font-weight:700;
      margin-right:3.5mm; vertical-align:middle;}}
  .pr-tab s{{font-family:'Cormorant Garamond',Georgia,serif; font-size:21pt; font-weight:700;
      color:#9C9288; text-decoration-thickness:1.5px;
      text-decoration-color:rgba(201,169,106,.7);}}
  .econ{{display:inline-block; margin-top:1.4mm; padding:1.2mm 4.2mm; border-radius:99px;
      background:rgba(201,169,106,.15); border:1px solid rgba(201,169,106,.45);
      font-size:8.2pt; font-weight:700; letter-spacing:.05em; color:var(--gold-lt);}}
  .item-tb tr.vista-row td{{color:var(--gold); font-size:12.5pt;}}
  .pay3{{display:flex; margin-top:2.6mm; padding-top:2.4mm;
      border-top:1px solid rgba(201,169,106,.28);}}
  .pay3 > div{{flex:1; padding-left:5mm; border-left:1px solid rgba(201,169,106,.18);}}
  .pay3 > div:first-child{{padding-left:0; border-left:0;}}
  .pay3 b{{display:block; font-family:'Cormorant Garamond',Georgia,serif; font-size:17pt;
      font-weight:700; color:var(--gold-lt); line-height:1;}}
  .pay3 span{{display:block; font-size:7.6pt; color:#C6BFB2; margin-top:1.2mm;}}
  /* banda da dobradiça */
  .hinge{{background:var(--deep); border-left:3px solid var(--gold-lt); border-radius:0 5px 5px 0;
      padding:5.2mm 7mm; margin-top:5mm; display:flex; gap:7mm; align-items:flex-start;}}
  .hinge .lead-t{{flex:0 0 52mm;}}
  .hinge .lead-t .t{{font-family:'Cormorant Garamond',Georgia,serif; font-size:15pt;
      font-weight:700; line-height:1.2; color:#fff;}}
  .hinge .lead-t .k{{font-size:7pt; letter-spacing:.2em; text-transform:uppercase;
      color:var(--gold-lt); font-weight:700; margin-bottom:1.8mm;}}
  .hinge .d{{font-size:8.5pt; color:#C6BFB2; line-height:1.58;}}
  .hinge .d b{{color:#F0E7D6;}}
  .warr{{background:var(--cream); border-left:3px solid var(--ink); border-radius:0 5px 5px 0;
      padding:3.2mm 6mm; margin-top:2.6mm; display:flex; gap:6mm; align-items:center;}}
  .warr .t{{flex:0 0 44mm; font-family:'Cormorant Garamond',Georgia,serif;
      font-size:13.5pt; font-weight:700; line-height:1.2;}}
  .warr .d{{font-size:8.4pt; color:var(--soft); line-height:1.6;}}
  .warr .d b{{color:var(--ink);}}
  /* página "além do móvel" */
  .coord{{display:flex; gap:0; margin-top:3mm; border-top:2px solid var(--ink); padding-top:2.8mm;}}
  .coord > div{{flex:1; padding:0 5mm; border-left:1px solid var(--line);}}
  .coord > div:first-child{{padding-left:0; border-left:0;}}
  .coord > div:last-child{{padding-right:0;}}
  .coord .k{{font-size:7pt; letter-spacing:.16em; text-transform:uppercase;
      color:var(--gold); font-weight:700;}}
  .coord .d{{font-size:8.4pt; color:var(--soft); line-height:1.55; margin-top:1.6mm;}}
  .coord .d b{{color:var(--ink);}}
  .warr-big{{background:var(--deep); border-radius:6px; padding:4.4mm 7mm; margin-top:3.4mm;
      position:relative; overflow:hidden; box-shadow:inset 0 0 0 1px rgba(201,169,106,.30);}}
  .warr-big::after{{content:""; position:absolute; left:0; top:0; bottom:0; width:4px;
      background:var(--gold-lt);}}
  .warr-big .k{{font-size:7.2pt; letter-spacing:.2em; text-transform:uppercase;
      color:var(--gold-lt); font-weight:700;}}
  .warr-big .big{{font-family:'Cormorant Garamond',Georgia,serif; font-size:22pt;
      font-weight:700; color:#fff; line-height:1.12; margin-top:1.6mm;}}
  .warr-big .d{{font-size:8.5pt; color:#C6BFB2; line-height:1.52; margin-top:2mm;}}
  .warr-big .d b{{color:#F0E7D6;}}
</style></head><body>

<!-- ══════ 1. CAPA ══════ -->
<div class="page cover">
  <div class="hero-img"><img src="{HERO}" alt=""></div>
  <div class="veil"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="d">.</span></div><div class="bsub">MARCENARIA</div></div>
    <div class="mid">
      <div class="kick">Proposta de marcenaria sob medida</div>
      <div class="tit">Casa L&amp;M.</div>
      <div class="sub">Alphaville · projeto executivo 07/2026 — 40 pranchas</div>
    </div>
    <div class="strip">
      <div class="c"><div class="k">Escopo</div><div class="v">14 móveis · 6 ambientes</div></div>
      <div class="c"><div class="k">Acabamento</div><div class="v">Duratex Carvalho</div></div>
      <div class="c"><div class="k">Ferragens</div><div class="v">Hettich · Alemanha</div></div>
    </div>
  </div>
</div>

<!-- ══════ 2. COPY ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Antes do preço</div>
  <hr class="rule">
  <div class="big-q serif">Num projeto deste tamanho, o orçamento<br>
  mais barato quase sempre é o que <b>leu menos</b>.</div>

  <p class="body-t" style="margin-top:6mm;">
  O caderno da sua arquiteta tem <b>40 pranchas</b>. E quase metade dos móveis
  encosta em algo que <b>já existe</b> na casa: bancada de granito, armário da
  cozinha, prateleira da despensa, gaveta do banheiro.<br><br>
  Quem orça por metro linear tem só dois caminhos, e os dois custam caro para você:
  <b>cobrar pelo que você já tem</b>, ou descobrir na montagem que a bancada existente
  não bate com o móvel novo — com a obra parada e o marceneiro pedindo aditivo.<br><br>
  Por isso esta proposta não começou por um preço. Começou pela leitura
  <b>prancha a prancha</b>: cada armário decomposto em <b>plano de corte</b>, cada
  ferragem contada uma a uma, antes de qualquer número ser escrito.</p>

  <div style="margin-top:6mm;" class="split2">
    <div>
      <div class="figure"><img src="{SALA}" alt=""></div>
      <div class="cap">Sala de jantar · painel em Carvalho Batur</div>
    </div>
    <div style="display:flex;flex-direction:column;justify-content:center;">
      <div class="pull">
        <div class="t">O que a leitura<br>encontrou.</div>
        <div class="d">As bandejas da sapateira têm <b>24,5 cm de profundidade</b> — e
        <b>não existe corrediça oculta nessa medida</b>. Especificamos telescópica ali,
        e mantivemos a oculta nas 20 gavetas do closet, que têm profundidade para isso.</div>
      </div>
    </div>
  </div>

  <div class="stats">
    <div>
      <div class="n">40</div>
      <div class="t"><b>pranchas lidas, uma a uma.</b> Plantas, elevações, cortes e
      detalhes — inclusive os que dizem o que já existe na casa.</div>
    </div>
    <div>
      <div class="n">14</div>
      <div class="t"><b>móveis num único contrato.</b> Da sala ao lavabo, um só
      responsável — sem coordenar marceneiros diferentes na mesma obra.</div>
    </div>
    <div>
      <div class="n">10 <em>anos</em></div>
      <div class="t"><b>de garantia formal em contrato.</b> Equipe própria do corte à
      instalação, com CNC próprio — sem terceirizar a sua obra.</div>
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Casa L&amp;M · Alphaville</span></div>
</div></div>

<!-- ══════ 3. ESCOPO ══════ -->
<div class="page p-esc"><div class="pad">
  <div class="eyebrow">O que será executado</div>
  <div class="h-sec serif">Catorze móveis,<br><em>lidos do executivo.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:2.5mm;font-size:12pt;">Fornecimento e instalação, conforme o caderno
  técnico de 07/2026.</p>

  <div class="amb">
    <div class="n">Sala de jantar <span class="badge">Carvalho Batur</span></div>
    <div class="s">Painel de 30 mm · três faces</div>
    <ul>
      <li><b>Painel em três faces</b>, do piso ao teto, sobre estrutura de fixação
          própria e afastado do piso.</li>
      <li><b>Porta pivotante mimetizada</b> — some no painel, com puxador em cava usinado
          e alça em inox preto do lado da cozinha.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Cozinha <span class="badge">Branco Ártico + Grafite</span></div>
    <div class="s">Aéreo em L · torre e gabinete</div>
    <ul>
      <li><b>Aéreo em L</b> em Branco Ártico, com recorte para a coifa de embutir e fita
          de LED sob a base.</li>
      <li><b>Torre e gabinete</b> na cor grafite do existente, com gavetões, porta-tempero
          e <b>6 prateleiras sobre corrediça</b>.</li>
      <li>Reorganização dos <b>módulos existentes</b> e sóculo novo no mesmo padrão.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Despensa</div>
    <div class="s">Armário alto, baixo e piso-teto</div>
    <ul>
      <li><b>Armário alto de 8 portas</b> e <b>gaveteiro de 11 gavetas</b>, três delas com
          <b>fundo em chapa metálica perfurada preta</b>.</li>
      <li><b>Armário piso-teto</b> com 5 bandejas deslizantes e ganchos de limpeza.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Suíte <span class="badge">maior conjunto</span></div>
    <div class="s">Closet em U · roupeiro · sapateira — Carvalho Brun</div>
    <ul>
      <li><b>Closet em U</b>: 20 gavetas com corrediça oculta, 13 prateleiras, cabideiros
          em metal e <b>prateleiras iluminadas</b>.</li>
      <li><b>Roupeiro</b> com lateral curva e <b>sapateira</b> com 13 bandejas deslizantes
          e iluminação vertical.</li>
      <li><b>8 portas em vidro reflecta</b> com estrutura metálica cinza grafite.</li>
    </ul>
  </div>

  <div class="amb">
    <div class="n">Banheiros e lavabo <span class="badge">5 ambientes</span></div>
    <div class="s">Carvalho Brun · puxador em cava 45°</div>
    <ul>
      <li>Armários da <b>suíte, visita, banho 02, banho 03 e lavabo</b>, com gavetas sobre
          corrediça telescópica e cesto de roupa embutido.</li>
      <li>Todos ajustados às <b>bancadas de granito existentes</b>, com furo de sifão
          conferido no local.</li>
    </ul>
  </div>

  <div class="split2" style="margin-top:1mm;">
    <div><div class="figure"><img src="{COZ}" alt="" style="height:30mm;object-fit:cover;object-position:center 45%;"></div>
      <div class="cap">Cozinha · aéreo em L e torre grafite</div></div>
    <div><div class="figure"><img src="{BANHO}" alt="" style="height:30mm;object-fit:cover;object-position:center 62%;"></div>
      <div class="cap">Banheiro · gaveteiro em Carvalho Brun</div></div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Casa L&amp;M · Alphaville</span></div>
</div></div>

<!-- ══════ 4. TÉCNICO ══════ -->
<div class="page p-tec"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="h-sec serif">O que está por dentro<br><em>do que você não vê.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:3mm;">Uma casa inteira é usada todos os dias, por
  todo mundo. A diferença aparece no terceiro ano.</p>

  <table class="spec-tb">
    <thead><tr><th>Item</th><th>Especificação</th></tr></thead>
    <tbody>
      <tr><td>Painéis e armários</td><td><b>MDF Duratex</b> — Carvalho Batur na sala,
        Carvalho Brun na suíte e banheiros, Branco Ártico e Cinza Chumbo na cozinha
        e despensa. Veio orientado e casado entre peças adjacentes.</td></tr>
      <tr><td>Estrutura</td><td><b>15 mm</b> em caixaria, portas e gavetas · <b>18 mm</b>
        nas prateleiras de maior vão, que evita a flecha ao longo do tempo ·
        <b>6 mm</b> em fundos.</td></tr>
      <tr><td>Dobradiças</td><td><b>Hettich Sensys Black</b>, com amortecimento integrado
        ao corpo. Fecho suave em qualquer velocidade.</td></tr>
      <tr><td>Corrediças</td><td><b>Hettich — corrediça oculta</b> nas gavetas do closet,
        do piso-teto e do banho da suíte: a gaveta abre inteira e a ferragem desaparece.
        <b>Telescópica</b> onde a profundidade não comporta a oculta.</td></tr>
      <tr><td>Portas em vidro</td><td><b>Reflecta com estrutura metálica cinza grafite</b>,
        em 8 folhas do piso ao teto.</td></tr>
      <tr><td>Puxadores</td><td><b>Cava usinada a 45°</b> no próprio MDF em 46 peças — sem
        ferragem aparente. Metálico cinza grafite nas portas de vidro.</td></tr>
      <tr><td>Iluminação</td><td><b>Fita LED 3000K e 4000K</b> com <b>lente difusora</b> e
        perfil de embutir, no closet, na sapateira e na cozinha. Luz contínua e uniforme,
        sem ponto quente.</td></tr>
      <tr><td>Detalhe especial</td><td><b>Chapa metálica perfurada 3 mm preta</b> no fundo
        de três gavetas da despensa, com quadro em MDF — ventilação para o que não pode abafar.</td></tr>
    </tbody>
  </table>

  <div class="hinge">
    <div class="lead-t">
      <div class="k">Ferragem alemã · desde 1888</div>
      <div class="t">Hettich<br>Sensys Black.</div>
    </div>
    <div class="d">
      O amortecimento fica <b>dentro do corpo da dobradiça</b> — não num cilindro
      aparente pendurado na lateral do móvel. A porta desacelera sozinha e encosta macia
      em qualquer velocidade, e o armário por dentro continua limpo, sem nada atravessado
      no caminho.<br><br>
      O acabamento <b>preto</b> faz a ferragem desaparecer no interior escuro do armário.
      É o oposto do cromado, que denuncia a dobradiça toda vez que a porta abre — e num
      projeto em Carvalho, esse detalhe é a diferença entre acabado e montado.<br><br>
      Cada uma é testada para <b>80 mil ciclos</b>: abrir e fechar dez vezes por dia,
      durante vinte anos.
    </div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Casa L&amp;M · Alphaville</span></div>
</div></div>


<!-- ══════ 5. ALÉM DO MÓVEL ══════ -->
<div class="page"><div class="pad">
  <div class="eyebrow">Além do móvel</div>
  <div class="h-sec serif">Uma obra,<br><em>um interlocutor.</em></div>
  <hr class="rule">
  <p class="lead" style="margin-bottom:1mm;">Um projeto deste porte não é só marcenaria.</p>

  <p class="body-t" style="margin-top:3mm;">
  Tem <b>porta de vidro com estrutura metálica</b>, <b>serralheria</b>, <b>fita de LED com
  fonte e comando</b>, <b>pintura e gesso</b> encostando no móvel. Cada um desses é um
  fornecedor com prazo próprio, medida própria — e desculpa própria quando alguma coisa
  não encaixa.<br><br>
  <b>A Valvic centraliza essa articulação.</b> Nós cotamos, especificamos, conferimos a
  medida e marcamos a sequência com cada um deles. Você trata com uma pessoa. E quando
  algo não encaixa, o problema é nosso — não vira uma reunião entre fornecedores com
  você no meio.</p>

  <div class="coord">
    <div><div class="k">Vidro</div><div class="d">Portas em reflecta com estrutura
      metálica — <b>cotação, medida e sequência de instalação</b> conosco.</div></div>
    <div><div class="k">Serralheria</div><div class="d">Estrutura em cinza grafite,
      <b>conferida contra a caixaria</b> antes de ir para a obra.</div></div>
    <div><div class="k">Iluminação</div><div class="d">Fita, perfil e lente — nós usinamos
      o rasgo e <b>alinhamos com o eletricista</b> onde entra a fonte.</div></div>
    <div><div class="k">Pintura e gesso</div><div class="d">Definimos com a obra
      <b>o que fecha primeiro</b>, para o móvel não voltar para retoque.</div></div>
  </div>

  <div class="split2" style="margin-top:4.5mm;">
    <div><div class="figure"><img src="{CURVA}" alt="" style="height:43mm;object-fit:cover;object-position:38% 50%;"></div>
      <div class="cap">Closet · terminação curva do piso ao teto</div></div>
    <div style="display:flex;flex-direction:column;justify-content:center;">
      <div class="pull">
        <div class="t">A peça mais difícil<br>da casa.</div>
        <div class="d">O closet <b>termina em curva</b> — dois raios ligados por um trecho
        reto, do piso ao teto. E o roupeiro repete a curva na lateral.<br><br>
        Curvar MDF é <b>usinagem de precisão na CNC</b>: o verso da peça recebe uma
        sequência de rasgos calculados para o raio exato — espaçamento errado, e a curva
        sai facetada ou trinca. E o revestimento ainda precisa fechar com o
        <b>veio contínuo</b> em relação às peças retas ao lado.<br><br>
        É o tipo de peça que separa quem tem <b>CNC própria</b> de quem terceiriza o corte.</div>
      </div>
    </div>
  </div>

  <div class="warr-big">
    <div class="k">Garantia</div>
    <div class="big">10 anos. Em contrato.</div>
    <div class="d">Marcenaria sob medida costuma sair com <b>1 a 3 anos</b> de garantia —
    quando sai por escrito. A nossa é de <b>10 anos</b> sobre estrutura, montagem e
    acabamento, mais <b>2 anos</b> de instalação e regulagem, formalizada em contrato.<br>
    Conseguimos assinar isso porque a equipe é <b>própria do corte à instalação</b> —
    não há terceiro para quem empurrar o defeito.</div>
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Casa L&amp;M · Alphaville</span></div>
</div></div>

<!-- ══════ 6. INVESTIMENTO ══════ -->
<div class="page p-inv"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="h-sec serif" style="font-size:21pt;">Preço fechado,<br><em>por ambiente.</em></div>
  <hr class="rule" style="margin:8px 0 9px;">

  <div class="inv-hero hero-vista">
    <div class="k">Marcenaria completa · 14 móveis</div>
    <div class="pr-tab"><span>Valor de tabela</span><s>R$ 199.300</s></div>
    <div class="v serif">R$ 179.300<span class="vtag">à vista</span></div>
    <div class="vrule"></div>
    <div class="econ">Você economiza R$ 20.000</div>
    <div class="c" style="margin-top:1.8mm;">Seis ambientes — fornecimento, produção e
    instalação por equipe própria, com ferragens Hettich, portas em vidro e iluminação LED.</div>
    <div class="pay3">
      <div><b>30%</b><span>na assinatura</span></div>
      <div><b>30%</b><span>no início da montagem</span></div>
      <div><b>40%</b><span>na entrega final</span></div>
    </div>
  </div>

  <table class="item-tb">
    <thead><tr><th>Ambiente</th><th class="r">Preço</th></tr></thead>
    <tbody>
      <tr><td class="nm">Suíte — closet, roupeiro e sapateira<small>Carvalho Brun · 8 portas em vidro reflecta · 20 gavetas com corrediça oculta</small></td><td class="r">R$ 107.800</td></tr>
      <tr><td class="nm">Cozinha — aéreo em L, torre e gabinete<small>Branco Ártico e Cinza Chumbo · inclui reorganizar os módulos existentes</small></td><td class="r">R$ 32.800</td></tr>
      <tr><td class="nm">Sala de jantar — painel e porta pivotante<small>Carvalho Batur · painel em três faces com porta mimetizada</small></td><td class="r">R$ 20.000</td></tr>
      <tr><td class="nm">Banheiros e lavabo — 5 ambientes<small>Carvalho Brun · sobre as bancadas de granito existentes</small></td><td class="r">R$ 19.700</td></tr>
      <tr><td class="nm">Despensa — armário alto, gaveteiro e piso-teto<small>11 gavetas · três com fundo em chapa perfurada</small></td><td class="r">R$ 19.000</td></tr>
      <tr class="tot"><td>Total</td><td class="r">R$ 199.300</td></tr>
      <tr class="tot vista-row"><td>À vista — 10% de desconto</td><td class="r">R$ 179.300</td></tr>
    </tbody>
  </table>

  <div class="terms" style="margin-top:2.4mm;">
    <div class="term"><div class="k">Pagamento</div><div class="v">À vista<br>−10%</div></div>
    <div class="term"><div class="k">Prazo</div><div class="v">70 a 90<br>dias corridos</div></div>
    <div class="term"><div class="k">Garantia</div><div class="v">10 anos</div></div>
    <div class="term"><div class="k">Validade</div><div class="v">15 dias<br>corridos</div></div>
  </div>

  <div class="note">
    <b>Incluso:</b> fornecimento, produção e instalação dos 14 móveis · ferragens Hettich ·
    8 portas em vidro reflecta com estrutura metálica · fita LED com perfil e lente difusora ·
    chapa metálica perfurada · reorganização dos módulos existentes da cozinha.<br>
    <b>Não incluso — já existe ou é de outro fornecedor:</b> bancadas em granito (cozinha e
    banheiros) · forro de gesso, tabica e cortineiro iluminado · espelhos · armários inferiores
    e prateleiras existentes · coifa, cooktop e demais eletrodomésticos · cesta elevatória ·
    pontos elétricos e hidráulicos · obra civil.<br>
    <b>Premissas:</b> medidas do executivo <b>conferidas no local</b> antes da produção —
    em especial as bancadas existentes e o furo de sifão · o <b>Grafite</b> é fornecido nas
    linhas foscas, <b>não contemplando as linhas Acetinato e Aris</b>.
  </div>

  <div class="pfoot"><span class="bl">valvic<span class="d">.</span> marcenaria</span><span>Casa L&amp;M · Alphaville · 28/07/2026</span></div>
</div></div>

</body></html>"""

(P/'casa-lm'/'proposta-casa-lm.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-casa-lm.html', len(HTML))
