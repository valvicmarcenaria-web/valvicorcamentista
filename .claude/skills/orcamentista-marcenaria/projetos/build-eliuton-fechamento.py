# -*- coding: utf-8 -*-
"""ELIUTON RIBEIRO · Brisas da Pampulha — PROPOSTA DE FECHAMENTO, 7 páginas.

[Jonathan 20/08] fechamento da linha Intermediária (Hardt · garantia 5 anos),
condição especial de 10% de desconto.

[Jonathan 20/08 · 2ª rodada] seis correções, todas aplicadas:
  1. prazo de entrega passa a 65 dias corridos
  2. entrada de R$ 27.000 (redonda) — deixa de ser "30%"
  3. cai a caixa "o que essa condição significa na prática"
  4. tábua de passar e os dois varais retráteis SAEM do escopo
  5. sai o quantitativo de chapa, fita e ferragem — fica a especificação
  6. sai o espaço de assinatura

  Validade da condição ......................... sábado, 22/08/2026
  Investimento cheio da linha Intermediária .... R$ 100.500
  Condição especial de fechamento (−10%) ....... R$  90.450
  Entrada na assinatura ........................ R$  27.000
  Saldo à vista, após a entrega ................ R$  63.450

⚠ PREÇO MANTIDO EM R$ 90.450 mesmo com a saída da tábua e dos varais. Era a
  leitura que fecha com a entrada redonda de R$ 27.000 que o Jonathan cravou —
  27.000 é 29,9% de 90.450. Se ele quiser abater a retirada do preço, o número
  vai a R$ 87.700 e a entrada volta a ser ~31%.

  Efeito na margem: o custo direto cai de R$ 42.716 para R$ 41.536, e a MC
  sobe de 32,8% para **34,1%** — recupera 1,3 ponto do que o desconto tinha
  levado. Continua abaixo da faixa ideal da casa (35–40%).

⚠ E a entrada segue sem cobrir o material: R$ 27.000 contra R$ 41.536 de custo
  direto (65%). A Valvic banca R$ 14.536 de capital de giro pelos 65 dias, além
  do custo fixo do período. Com o prazo caindo de 90–120 para 65 dias, a
  exposição dura menos — mas fica mais intensa, porque a compra de material se
  concentra.

Valores de `corte-eliuton.py`. SEM RT. Mármore fora do escopo.
⚠ MONTAGEM: fora do CUSTO (equipe é salário fixo), DENTRO do escopo entregue.
"""
import subprocess

CLIENTE   = 'Eliuton Ribeiro'
OBRA      = 'Residência Brisas da Pampulha'
ARQUITETA = 'Arq. Luciana Beatriz Simplício · Núcleo SC Arquitetura'
DATA      = '20 de agosto de 2026'
# [Jonathan 20/08] validade até sábado. Dato em vez de escrever só "sábado":
# proposta é documento, e "sábado" sem data fica ambíguo na semana seguinte.
VALIDADE  = 'Sábado, 22/08/2026'
PRAZO     = '65 dias corridos'          # [Jonathan 20/08]

CHEIO    = 100500
FECHA    = 90450
ECONOMIA = CHEIO - FECHA
ENTRADA  = 27000                        # [Jonathan 20/08] valor redondo
SALDO    = FECHA - ENTRADA
assert SALDO == 63450

# ── memorial descritivo · sem quantitativo de chapa, fita e ferragem ──────
ITENS = [
 ('01', 'Cozinha — conjunto completo',
  'MDF Arauco <strong>Nogueira Persa</strong> (torre e acabamento) e '
  '<strong>Sálvia</strong> (bancada, aéreo e ilha).',
  ['<strong>Torre de cocção com nicho de geladeira</strong> — 187 × 70 × 290. '
   'Lateral vazada servindo de batente da porta do gourmet, divisória e lateral '
   'internas, horizontais da coluna, três portas basculantes (103 × 58, 70 × 58 '
   'e 70 × 39) e gavetão de 70 × 58 com prateleira interna.',
   '<strong>Os nichos de eletrodoméstico não levam fundo de MDF.</strong> '
   'Geladeira, forno e micro-ondas precisam de ventilação, tomada e folga de '
   'dissipação — o fundo é a alvenaria. É especificação técnica, não economia.',
   '<strong>Acabamento superior</strong> — faixa de 15 cm sob o forro, ao longo '
   'de toda a parede, com emenda executada sobre divisória.',
   '<strong>Bancada 01</strong> — 355 × 70 × 88, corpo de 78 com rodapé recuado '
   'de 10. Três frentes de gaveta de 64 × 15, gavetão de 64 × 29, quatro portas '
   'de 50 × 74, porta do pano de prato de 23 × 74 e prateleiras internas. Nicho '
   'preparado para lava-louças de embutir.',
   '<strong>Aéreo</strong> — 351 × 40 × 96, cinco portas (85 · 85 · 56 · 57 · 56).',
   '<strong>Ilha</strong> — 226 × 70 × 88, quatro gavetas e três módulos de '
   'porta. O tampo em cascata é de mármore e não está neste valor.',
   'Puxador em <strong>cava 35° usinada</strong> no próprio material, na CNC.'],
  30700),
 ('02', 'Painel ripado do estar e jantar',
  'MDF Arauco <strong>Nogueira Persa</strong>, parede inteira de 572 × 288.',
  ['Construção <strong>tipo 2</strong>: painel de fundo com régua colada no topo '
   'e fitada em uma face. Régua de 4,0 cm com espaçamento de 1,5 — passo de '
   '5,5 cm, mantido do rodapé ao forro.',
   'A régua de 288 cm <strong>não cabe na chapa</strong>. Sai emendada em dois '
   'trechos, com a emenda caindo na horizontal do acabamento sobre a porta de '
   'correr — onde ela desaparece. Está previsto no plano de corte, não é '
   'improviso de obra.',
   '<strong>Porta de correr embutida</strong> com sistema deslizante amortecido, '
   'e <strong>porta pivotante de 80 × 210</strong>. As duas são ripadas e '
   'alinhadas ao painel: de fora, a parede é contínua e as portas somem nela.',
   'O ripado é caro pela <strong>mão de obra de borda</strong>, não pela chapa. '
   'Cada régua é cortada, fitada e colada uma a uma, e o desenho só fecha se o '
   'passo não variar em nenhum ponto da parede.'],
  20400),
 ('03', 'Área gourmet — bancada 02',
  'MDF Arauco <strong>Nogueira Persa</strong>.',
  ['<strong>Armário inferior com gaveteiro</strong> — 145 × 70, gavetas com '
   'corrediça oculta.',
   '<strong>Coluna da cervejeira</strong> — 70 × 290, do piso ao forro, com '
   'nicho ventilado para o aparelho.',
   '<strong>Prateleira com iluminação embutida</strong> — fita de LED em perfil '
   'de alumínio, embutida na própria peça.',
   '<strong>Armário superior com duas portas basculantes</strong> em estrutura '
   'metálica fendi e vidro incolor temperado de 8 mm. A serralheria das folhas '
   'está no valor.'],
  12000),
 ('04', 'Área de serviço',
  'MDF Arauco <strong>Nogueira Persa</strong>, armário de 359 × 55 × 226.',
  ['Armário do <strong>piso ao forro</strong>, 55 cm de profundidade, com módulo '
   'alto para vassouras e material de limpeza.',
   '<strong>Nichos de máquina de lavar e secadora</strong>, com o vão e a '
   'usinagem previstos — precisamos das medidas de fábrica dos aparelhos antes '
   'do corte.',
   '<strong>Dois gavetões</strong> e armário inferior sob a bancada.',
   'O rodapé de 359 cm também <strong>não cabe na chapa</strong> e sai emendado, '
   'previsto no plano de corte.'],
  15000),
 ('05', 'Lavabo externo',
  'MDF Arauco <strong>Nogueira Persa</strong>.',
  ['<strong>Painel de parede</strong> de 130 × 248.',
   '<strong>Acabamento de forro em MDF</strong> de 130 × 40 — a madeira desce da '
   'parede e vira teto.',
   '<strong>Gabinete suspenso</strong> de 150 × 50 com porta basculante e nicho '
   'aberto. O tampo é de pedra e não está neste valor.'],
  3400),
 ('06', 'Banheiro master',
  'MDF Arauco <strong>Jequitibá</strong> — o único ambiente nesta cor.',
  ['<strong>Espelheira de 1,85 m</strong> com três portas espelhadas de correr e '
   'nichos vazados nas laterais.',
   'Espelho <strong>prata com perfil</strong>, sobre sistema deslizante '
   '<strong>RO65 Rometal</strong>. RO65 é o sistema correto para folha de '
   'armário raso — SS150 é de roupeiro e não se aplica aqui.',
   '<strong>Gabinete suspenso de 1,85 × 50 com quatro portas ripadas</strong>, '
   'no mesmo desenho do painel do estar, com puxadores metálicos tipo alça '
   'preto.'],
  7600),
 ('07', 'Banheiro social — 1º pavimento',
  'MDF Arauco <strong>Nogueira Persa</strong>, com prateleiras em '
  '<strong>Beige</strong>.',
  ['<strong>Armário superior de 1,90 m</strong> com portas espelhadas de correr '
   'sobre sistema RO65, e nicho aberto com prateleiras.',
   '<strong>Iluminação em LED em L</strong> — fita em perfil de alumínio, '
   'contornando o nicho em dois planos.',
   '<strong>Gabinete inferior de 1,10 m</strong> com nicho papeleiro.'],
  5200),
 ('08', 'Banheiro 04',
  'MDF Arauco <strong>Nogueira Persa</strong>.',
  ['<strong>Armário superior de 1,10 m</strong> com duas portas espelhadas de '
   'correr sobre sistema RO65.',
   '<strong>Prateleiras laterais sobre suporte metálico dourado.</strong>',
   '<strong>Gabinete inferior de 1,46 m</strong> com nicho aberto.'],
  6200),
]
assert sum(i[4] for i in ITENS) == CHEIO

# ── especificação técnica — spec, não quantitativo ───────────────────────
ESPEC = [
 ('Chapa', 'MDF Arauco: <strong>18 mm</strong> em frentes e prateleiras, '
  '<strong>15 mm</strong> na caixaria e <strong>6 mm</strong> nos fundos. '
  'Fundos <strong>na cor</strong>, não em branco — as perspectivas do projeto '
  'mostram o interior todo no acabamento da frente. O plano de corte é fechado '
  'por cor e por espessura: cor nenhuma divide chapa com outra.'),
 ('Borda', 'Fita de borda na cor em todas as bordas aparentes, aplicada em '
  '<strong>coladeira automática</strong> com filetagem — não é fita passada a '
  'ferro nem colada em bancada.'),
 ('Puxador', '<strong>Cava 35° usinada na CNC</strong> no próprio material. Sem '
  'puxador aparente o desenho fica limpo, e não há peça de reposição a depender '
  'de fornecedor.'),
 ('Ferragem', 'Linha Intermediária em todos os conjuntos: <strong>dobradiça '
  'Hardt</strong> com amortecimento, <strong>corrediça oculta Hardt</strong> de '
  'fechamento suave e <strong>articulador Blum HK-xs</strong> nas básculas.'),
 ('Iluminação', 'Fita de LED em <strong>perfil de alumínio</strong>, embutida na '
  'marcenaria: prateleira do gourmet e nicho em L do banheiro social. O perfil é '
  'o que diferencia luz embutida de fita aparente.'),
 ('Espelho e vidro', '<strong>Espelho prata com perfil</strong> nas portas de '
  'correr dos três banheiros, sobre sistema deslizante RO65 Rometal. '
  '<strong>Vidro incolor temperado de 8 mm</strong> nas portas basculantes do '
  'gourmet.'),
 ('Serralheria', 'Estrutura metálica <strong>fendi</strong> das portas '
  'basculantes do gourmet, executada sob medida.'),
 ('Produção e montagem', 'Corte e usinagem em <strong>CNC própria</strong>, '
  'laminação de borda em coladeira automática própria, e <strong>instalação e '
  'montagem por equipe própria da Valvic</strong>. Não terceirizamos nem o que '
  'define o acabamento, nem quem entrega.'),
]

FORA = [
 ('Marmoraria', 'Bancadas 01, 02 e 03, ilha em cascata, rodabancas, nichos, '
  'cubas esculpidas, prateleiras e o "detalhe caixa" da cozinha — o projeto '
  'especifica Carrara e Travertino. É fornecimento de marmoraria.'),
 ('Tábua de passar e varais', 'A tábua de passar embutida e os varais retráteis '
  'da área de serviço <strong>não fazem parte deste escopo</strong>. O armário '
  'é executado sem eles.'),
 ('Louças, metais e eletrodomésticos', 'Especificados no projeto (Deca, '
  'Tramontina, Brastemp, Electrolux, Metalfrio). Prevemos o vão e a usinagem; '
  'precisamos das medidas de fábrica antes do corte.'),
 ('Alvenaria, revestimento e churrasqueira', 'Porcelanato, tijolete, azulejo, '
  'gesso e forro.'),
 ('Móveis soltos', 'Mesa de jantar, cadeiras, banquetas, buffet, sofá, poltronas '
  'e a escultura de parede.'),
 ('Elétrica e hidráulica', 'A iluminação embutida NA marcenaria é nossa; os '
  'pontos de energia e de água são da obra.'),
]

CSS = open('projetos/css-proposta.css', encoding='utf-8').read() + """
/* ── blocos exclusivos da proposta de FECHAMENTO ─────────────────────── */
.selo-f{display:inline-block;background:var(--gold);color:#fff;font-size:7pt;
  letter-spacing:.24em;text-transform:uppercase;padding:2mm 4.5mm;font-weight:700;
  border-radius:2px;}
.cv-val{font-family:'Cormorant Garamond',Georgia,serif;font-size:60pt;
  line-height:1;font-weight:600;color:#F6F1E7;letter-spacing:-.02em;}
.cv-de{font-size:11pt;color:#9A927F;margin-top:3mm;}
.cv-de s{color:#7E7768;}
.pf{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:6mm;}
.pf .c{border:1px solid var(--line);border-radius:2px;padding:5.5mm 6mm;}
.pf .c.hi{background:var(--deep);border-color:var(--deep);color:#F6F1E7;}
.pf .k{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.pf .c.hi .k{color:var(--gold-lt);}
.pf .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:31pt;
  line-height:1.05;font-weight:600;margin-top:2mm;}
.pf .s{color:var(--soft);font-size:8.4pt;margin-top:2mm;}
.pf .c.hi .s{color:#CFC6B4;}
.mem{padding:4mm 0;border-bottom:1px solid var(--hair);}
.mem:last-child{border-bottom:none;}
.mem-h{display:flex;align-items:baseline;gap:4mm;}
.mem-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;
  color:var(--gold-lt);font-weight:600;line-height:1;min-width:10mm;}
.mem-t{font-size:11pt;font-weight:700;letter-spacing:-.005em;}
.mem-m{color:var(--soft);font-size:8.4pt;margin:1.6mm 0 0 14mm;}
.mem ul{margin:2mm 0 0 14mm;padding:0;}
.mem li{list-style:none;color:var(--soft);font-size:8.4pt;line-height:1.52;
  margin-bottom:1.5mm;padding-left:4.5mm;position:relative;}
.mem li::before{content:'';position:absolute;left:0;top:1.9mm;width:3.5px;
  height:3.5px;border-radius:50%;background:var(--gold-lt);}
.mem-v{margin:2.4mm 0 0 14mm;font-size:8.6pt;}
.mem-v b{font-size:10.4pt;}
.mem-v s{color:var(--mut);font-weight:400;}
.esp{padding:2.5mm 0;border-bottom:1px solid var(--hair);display:grid;
  grid-template-columns:34mm 1fr;gap:5mm;}
.esp:last-child{border-bottom:none;}
.esp .k{font-size:7.4pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;padding-top:.5mm;}
.esp .v{color:var(--soft);font-size:8.7pt;}
.inv th:nth-child(2),.inv td:nth-child(2){padding-right:5mm;}
"""

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 8
def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria · {CLIENTE}</span>'
            f'<span>Proposta de fechamento</span><span>{n} / {NP}</span></div>')

def mem(i):
    n, tit, mat, bul, val = i
    li = ''.join(f'<li>{b}</li>' for b in bul)
    return (f'<div class="mem"><div class="mem-h"><div class="mem-n">{n}</div>'
            f'<div class="mem-t">{tit}</div></div>'
            f'<div class="mem-m">{mat}</div><ul>{li}</ul>'
            f'<div class="mem-v"><s>R$ {brl(val)}</s> &nbsp;→&nbsp; '
            f'<b>R$ {brl(int(round(val*0.9)))}</b> '
            f'<span style="color:var(--mut)">com a condição de fechamento</span>'
            f'</div></div>')

p1 = f"""<div class="page cover"><div class="pad">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div style="margin-top:auto">
    <div class="selo-f">Proposta de fechamento</div>
    <div class="cv-t" style="margin-top:6mm">{CLIENTE}</div>
    <div class="cv-s">{OBRA}<br>{ARQUITETA}</div>
    <div style="margin-top:11mm">
      <div class="eyebrow">Linha Intermediária · garantia de 5 anos</div>
      <div class="rule"></div>
      <div class="cv-val">R$ {brl(FECHA)}</div>
      <div class="cv-de">de <s>R$ {brl(CHEIO)}</s> &nbsp;·&nbsp; condição especial
      de fechamento, −10%</div>
    </div>
  </div>
  <div class="cv-meta">
    <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
    <div><div class="k">Data</div><div class="v">{DATA}</div></div>
    <div><div class="k">Validade da condição</div><div class="v">{VALIDADE}</div></div>
  </div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condição especial de fechamento</div>
  <div class="rule"></div>
  <h2 class="h-sec">Dez por cento a menos,<br>e o saldo só depois de entregue.</h2>
  <p class="lead" style="margin-top:4mm">Esta é uma condição de fechamento: vale
  para a assinatura dentro da validade desta proposta e não se soma a outras
  condições. O desconto incide sobre o investimento cheio da linha Intermediária,
  <strong>sem simplificar um único conjunto</strong> — o que muda é o preço, não
  o que será executado.</p>
  <div class="pf">
    <div class="c"><div class="k">Investimento da linha Intermediária</div>
      <div class="v" style="color:var(--mut)">R$ {brl(CHEIO)}</div>
      <div class="s">Valor da proposta de 17 de agosto, com a mesma ferragem e a
      mesma garantia de 5 anos.</div></div>
    <div class="c hi"><div class="k">Com a condição de fechamento</div>
      <div class="v">R$ {brl(FECHA)}</div>
      <div class="s">Economia de <strong>R$ {brl(ECONOMIA)}</strong>.</div></div>
  </div>
  <div class="pf" style="margin-top:5mm">
    <div class="c"><div class="k">Entrada na assinatura</div>
      <div class="v">R$ {brl(ENTRADA)}</div>
      <div class="s">Libera a compra de material e a entrada do projeto na fila
      de produção.</div></div>
    <div class="c"><div class="k">Saldo à vista, após a entrega</div>
      <div class="v">R$ {brl(SALDO)}</div>
      <div class="s">Pago depois da instalação concluída e conferida na obra.
      Não há parcela durante a produção.</div></div>
  </div>
  <div class="box" style="margin-top:7mm"><div class="t">O que não muda</div>
  <p>Materiais, ferragem, iluminação, espelhos, vidros, serralheria e a garantia
  de 5 anos são <strong>exatamente os da proposta de 17 de agosto</strong>.
  Nenhum conjunto foi substituído ou simplificado para chegar a este valor.</p></div>
  <div class="box"><div class="t">Prazo de entrega</div>
  <p><strong>{PRAZO}</strong>, contados da assinatura, do pagamento da entrada e
  da definição da chapa. Os oito conjuntos são entregues por frentes, na ordem
  em que a obra puder recebê-los.</p></div>
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">A linha escolhida</div>
  <div class="rule"></div>
  <h2 class="h-sec">Intermediária.<br>Cinco anos de garantia Valvic.</h2>
  <p class="lead" style="margin-top:4mm">O desenho, a chapa, o acabamento e o
  esquadro são os mesmos das três linhas apresentadas. O que define a
  Intermediária é a ferragem — e ferragem se mede em ciclo de abertura,
  amortecimento e regulagem.</p>
  <div class="cen hi" style="margin-top:6mm">
    <div class="cen-h"><div class="cen-n">II</div>
      <div class="cen-t">Intermediária</div>
      <div class="cen-g">Garantia 5 anos</div></div>
    <div class="cen-x">A gaveta passa a correr por baixo, escondida: some o
    trilho lateral e o vão útil cresce. O articulador da báscula é o Blum HK-xs
    — o mesmo da linha Superior. Numa casa com esta quantidade de gavetas, é o
    degrau que mais se sente no dia a dia.</div>
    <div class="cen-l">
      <div><div class="k">Dobradiça</div>
        <div class="v">Hardt com amortecimento</div></div>
      <div><div class="k">Corrediça</div>
        <div class="v">Oculta Hardt, fechamento suave</div></div>
      <div><div class="k">Báscula</div>
        <div class="v">Articulador Blum HK-xs</div></div>
    </div>
  </div>
  <div class="box"><div class="t">Sobre a garantia</div>
  <p>Os cinco anos são <strong>garantia Valvic</strong> — nossa, escrita e
  assinada na entrega, cobrindo estrutura, ferragem e acabamento. Não é a
  garantia do fabricante da ferragem, que não faz parte do que vendemos.</p></div>
  <div class="box"><div class="t">Sobre a montagem</div>
  <p>A <strong>instalação e a montagem são feitas por equipe própria da
  Valvic</strong> e estão dentro deste valor. Não terceirizamos a entrega: quem
  produz é quem monta, e é a mesma empresa que responde pela garantia.</p></div>
  <div class="box" style="border-left-color:var(--mut)">
  <div class="t" style="color:var(--mut)">Uma definição ainda em aberto</div>
  <p>A <strong>linha da chapa Arauco</strong>. O projeto nomeia Nogueira Persa,
  Sálvia, Jequitibá e Beige, e este valor considera as quatro na faixa de cor
  padrão. Se alguma delas for de acabamento especial, o conjunto é recotado
  antes da assinatura — a chapa é o maior item isolado deste orçamento.</p></div>
  {foot(3)}
</div></div>"""

p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Memorial descritivo</div>
  <div class="rule"></div>
  <h2 class="h-sec">Oito conjuntos,<br>descritos um a um.</h2>
  <p class="lead" style="margin-top:3.5mm;margin-bottom:1mm">Cada item traz o
  material, a composição construtiva e o que a define. O valor cheio e o valor
  com a condição de fechamento aparecem ao pé de cada um.</p>
  {mem(ITENS[0])}
  {mem(ITENS[1])}
  {foot(4)}
</div></div>"""

p5 = f"""<div class="page"><div class="pad">
  {mem(ITENS[2])}
  {mem(ITENS[3])}
  {mem(ITENS[4])}
  {mem(ITENS[5])}
  {foot(5)}
</div></div>"""

linhas = ''.join(
    f'<tr><td class="l">{n} · {t}</td><td>{brl(v)}</td>'
    f'<td class="hi">{brl(int(round(v*0.9)))}</td></tr>'
    for n, t, _m, _b, v in ITENS)

p6 = f"""<div class="page"><div class="pad">
  {mem(ITENS[6])}
  {mem(ITENS[7])}
  <div style="margin-top:6mm">
  <div class="eyebrow">Resumo do investimento</div>
  <div class="rule" style="margin:5px 0 3mm"></div>
  <table class="inv">
    <tr><th class="l">Conjunto</th><th>Valor cheio</th>
        <th class="hi">Fechamento −10%</th></tr>
    {linhas}
    <tr class="tot"><td class="l">Investimento total</td>
      <td style="font-size:10.5pt;color:var(--mut)">{brl(CHEIO)}</td>
      <td class="hi">{brl(FECHA)}</td></tr>
  </table>
  </div>
  {foot(6)}
</div></div>"""

esp = ''.join(f'<div class="esp"><div class="k">{k}</div>'
              f'<div class="v">{v}</div></div>' for k, v in ESPEC)
fora = ''.join(f'<li><div class="k">{k}</div><div class="v">{v}</div></li>'
               for k, v in FORA)

p7 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="rule"></div>
  <h2 class="h-sec">O que atravessa<br>o projeto inteiro.</h2>
  <p class="lead" style="margin-top:3.5mm">As oito linhas abaixo valem para
  todos os conjuntos do memorial, e são o que sustenta a garantia de cinco
  anos.</p>
  <div style="margin-top:5mm">{esp}</div>
  {foot(7)}
</div></div>"""

p8 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <h2 class="h-sec">Prazo, pagamento<br>e fronteiras.</h2>
  <div class="two" style="margin-top:7mm">
    <div>
      <div class="term"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da assinatura, do pagamento da entrada e da
        definição da chapa. Os oito conjuntos são entregues por frentes, na
        ordem em que a obra puder recebê-los.</div></div>
      <div class="term"><div class="k">Pagamento</div>
        <div class="v">R$ {brl(ENTRADA)} + R$ {brl(SALDO)}</div>
        <div class="s">Entrada na assinatura e saldo à vista após a instalação
        concluída e conferida na obra. Não há parcela durante a produção.</div></div>
      <div class="term"><div class="k">Validade da condição</div>
        <div class="v">Até sábado, 22 de agosto de 2026</div>
        <div class="s">Passada a validade, volta a valer o investimento cheio de
        R$ {brl(CHEIO)}.</div></div>
      <div class="term"><div class="k">Garantia</div>
        <div class="v">5 anos, Valvic</div>
        <div class="s">Escrita e assinada na entrega, cobrindo estrutura,
        ferragem e acabamento.</div></div>
      <div class="term"><div class="k">Conferência de medidas</div>
        <div class="v">Visita técnica antes do corte</div>
        <div class="s">Nada vai para a CNC antes da nossa medição na obra e da
        confirmação das medidas de fábrica dos eletrodomésticos.</div></div>
    </div>
    <div class="fora">
      <div class="eyebrow">Não incluso nesta proposta</div>
      <div class="rule"></div>
      <ul>{fora}</ul>
    </div>
  </div>
  {foot(8)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>'
        f'{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}</body></html>')

OUT_H = 'projetos/proposta-eliuton-fechamento.html'
OUT_P = 'projetos/proposta-eliuton-fechamento.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML)
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}')
print(f'cheio {brl(CHEIO)} → fechamento {brl(FECHA)} · '
      f'entrada {brl(ENTRADA)} + saldo {brl(SALDO)} · prazo {PRAZO}')
