# -*- coding: utf-8 -*-
"""ELIUTON RIBEIRO · Brisas da Pampulha — PROPOSTA DE FECHAMENTO, 8 páginas.

[Jonathan 20/08] "versão de fechamento da versão intermediária, com todas as
descrições técnicas pertinentes, condição especial de fechamento com 10% de
desconto, entrada de 30% e o restante à vista pós entrega."

UMA LINHA SÓ — a Intermediária (Hardt · MC 37% · garantia 5 anos). Não há
comparação de cenários aqui: proposta de fechamento não oferece escolha, oferece
decisão. Os outros dois cenários ficam na proposta de 17/08.

  Investimento da linha Intermediária ......... R$ 100.500
  Condição especial de fechamento (−10%) ...... R$  90.450
  Entrada de 30% na assinatura ................ R$  27.135
  Saldo de 70% à vista, após a entrega ........ R$  63.315

⚠ O DESCONTO CUSTA 4,7 PONTOS DE MC: 37,5% → 32,8%, contra custo direto de
  R$ 42.716. Abaixo da faixa ideal da casa (35–40%). Está registrado aqui e foi
  dito ao Jonathan — a decisão é dele, e ele a tomou.

⚠ E A ENTRADA NÃO COBRE O MATERIAL: R$ 27.135 de entrada contra R$ 42.716 de
  custo direto. A Valvic banca R$ 15.581 de capital de giro por 90 a 120 dias,
  além do custo fixo do período. Também dito, também decisão dele.

Valores de `corte-eliuton.py`. SEM RT. Mármore fora do escopo.
⚠ MONTAGEM: fora do CUSTO (equipe é salário fixo), DENTRO do escopo entregue.
"""
import subprocess

CLIENTE   = 'Eliuton Ribeiro'
OBRA      = 'Residência Brisas da Pampulha'
ARQUITETA = 'Arq. Luciana Beatriz Simplício · Núcleo SC Arquitetura'
DATA      = '20 de agosto de 2026'
VALIDADE  = '7 dias corridos'
PRAZO     = '90 a 120 dias corridos'

CHEIO    = 100500
DESC_PCT = 0.10
FECHA    = int(round(CHEIO*(1-DESC_PCT)))      # 90.450
ECONOMIA = CHEIO - FECHA                        # 10.050
ENTRADA  = int(round(FECHA*0.30))               # 27.135
SALDO    = FECHA - ENTRADA                      # 63.315
assert (FECHA, ENTRADA, SALDO) == (90450, 27135, 63315)

# ── memorial descritivo · 8 itens, com o valor cheio e o de fechamento ────
ITENS = [
 ('01', 'Cozinha — conjunto completo', '56,42 m² de chapa · 32 dobradiças · 9 gavetas · 3 básculas',
  'MDF Arauco <strong>Nogueira Persa</strong> (torre e acabamento) e '
  '<strong>Sálvia</strong> (bancada, aéreo e ilha).',
  ['<strong>Torre de cocção com nicho de geladeira</strong> — 187 × 70 × 290. '
   'Lateral vazada de 18 mm servindo de batente da porta do gourmet, divisória e '
   'lateral em 15 mm, seis horizontais na coluna, três portas basculantes '
   '(103 × 58, 70 × 58 e 70 × 39) e gavetão de 70 × 58 com prateleira interna.',
   '<strong>Os nichos de eletrodoméstico não levam fundo de MDF.</strong> '
   'Geladeira, forno e micro-ondas precisam de ventilação, tomada e folga de '
   'dissipação — o fundo é a alvenaria. É especificação técnica, não economia.',
   '<strong>Acabamento superior</strong> — faixa de 15 cm sob o forro, ao longo '
   'dos 5,415 m, executada em duas peças com emenda sobre divisória.',
   '<strong>Bancada 01</strong> — 355 × 70 × 88 (corpo de 78 + rodapé recuado de '
   '10). Sete verticais, base em duas peças, travessa superior, fundo de 6 mm, '
   'três frentes de gaveta de 64 × 15, gavetão de 64 × 29, quatro portas de '
   '50 × 74, porta do pano de prato de 23 × 74 e duas prateleiras internas. '
   'Nicho preparado para lava-louças de embutir.',
   '<strong>Aéreo</strong> — 351 × 40 × 96, cinco portas (85 · 85 · 56 · 57 · 56).',
   '<strong>Ilha</strong> — 226 × 70 × 88, quatro gavetas e três módulos de porta. '
   'O tampo em cascata é de mármore e não está neste valor.',
   'Puxador em <strong>cava 35° usinada</strong> no próprio material, na CNC.'],
  30700),
 ('02', 'Painel ripado do estar e jantar', '28,45 m² de chapa · ripado integral · 305 m de fita',
  'MDF Arauco <strong>Nogueira Persa</strong>, parede inteira de 572 × 288.',
  ['Construção <strong>tipo 2</strong>: painel de fundo em 15 mm com régua de '
   '18 mm colada no topo, fitada em uma face. Régua de 4,0 cm com espaçamento de '
   '1,5 — passo de 5,5 cm.',
   'A régua de 288 cm <strong>não cabe na chapa de 275 × 185</strong>. Sai '
   'emendada em dois trechos de 144, com a emenda caindo na horizontal do '
   'acabamento sobre a porta de correr — onde ela desaparece. Está previsto no '
   'plano de corte, não é improviso de obra.',
   '<strong>Porta de correr embutida</strong> com sistema deslizante amortecido, '
   'e <strong>porta pivotante de 80 × 210</strong>. As duas são ripadas e '
   'alinhadas ao painel: de fora, a parede é contínua e as portas somem nela.',
   'São <strong>305 metros de fita de borda</strong> só neste item — 53% da fita '
   'do projeto inteiro. O ripado é caro pela mão de obra de borda, não pela chapa.'],
  20400),
 ('03', 'Área gourmet — bancada 02', '17,97 m² de chapa · 6 dobradiças · 4 gavetas · 1 báscula',
  'MDF Arauco <strong>Nogueira Persa</strong>.',
  ['<strong>Armário inferior com gaveteiro</strong> — 145 × 70, quatro gavetas '
   'com corrediça oculta.',
   '<strong>Coluna da cervejeira</strong> — 70 × 290, do piso ao forro, com nicho '
   'ventilado para o aparelho.',
   '<strong>Prateleira com iluminação embutida</strong> — 1,45 m de fita de LED '
   'em perfil de alumínio, embutida na própria peça.',
   '<strong>Armário superior com duas portas basculantes</strong> em estrutura '
   'metálica fendi e vidro incolor temperado de 8 mm (duas folhas de 71 × 73). '
   'A serralheria das duas folhas está no valor.'],
  12000),
 ('04', 'Área de serviço', '32,10 m² de chapa · 16 dobradiças · 4 gavetas · 2 básculas',
  'MDF Arauco <strong>Nogueira Persa</strong>, armário de 359 × 55 × 226.',
  ['Armário do <strong>piso ao forro</strong>, 55 cm de profundidade, com módulo '
   'alto para vassouras e material de limpeza.',
   '<strong>Tábua de passar embutida dobrável</strong>, integrada ao módulo.',
   '<strong>Nichos de máquina de lavar e secadora</strong>, com o vão e a '
   'usinagem previstos — precisamos das medidas de fábrica dos aparelhos antes '
   'do corte.',
   '<strong>Dois varais retráteis embutidos</strong>, dois gavetões e armário '
   'inferior sob a bancada.',
   'O rodapé de 359 cm também <strong>não cabe na chapa</strong> e sai emendado, '
   'previsto no plano de corte.'],
  15000),
 ('05', 'Lavabo externo', '6,01 m² de chapa · 2 dobradiças · 1 báscula',
  'MDF Arauco <strong>Nogueira Persa</strong>.',
  ['<strong>Painel de parede</strong> de 130 × 248.',
   '<strong>Acabamento de forro em MDF</strong> de 130 × 40 — a madeira desce da '
   'parede e vira teto.',
   '<strong>Gabinete suspenso</strong> de 150 × 50 com porta basculante e nicho '
   'aberto. O tampo é de pedra e não está neste valor.'],
  3400),
 ('06', 'Banheiro master', '8,01 m² de chapa · 8 dobradiças · gabinete ripado',
  'MDF Arauco <strong>Jequitibá</strong> — o único ambiente nesta cor.',
  ['<strong>Espelheira de 1,85 m</strong> com três portas espelhadas de correr e '
   'nichos vazados nas laterais.',
   'Espelho <strong>prata com perfil</strong>, três folhas, sobre sistema '
   'deslizante <strong>RO65 Rometal</strong> com trilho de 2 m. RO65 é o sistema '
   'correto para folha de armário raso — SS150 é de roupeiro e não se aplica aqui.',
   '<strong>Gabinete suspenso de 1,85 × 50 com quatro portas ripadas</strong>, no '
   'mesmo desenho do painel do estar, e oito puxadores metálicos tipo alça preto.'],
  7600),
 ('07', 'Banheiro social — 1º pavimento', '6,34 m² de chapa · 4 dobradiças',
  'MDF Arauco <strong>Nogueira Persa</strong>, com quatro prateleiras em '
  '<strong>Beige</strong>.',
  ['<strong>Armário superior de 1,90 m</strong> com portas espelhadas de correr '
   'sobre sistema RO65, e nicho aberto com prateleiras.',
   '<strong>Iluminação em LED em L</strong> — 2,6 m de fita em perfil de alumínio, '
   'contornando o nicho em dois planos.',
   '<strong>Gabinete inferior de 1,10 m</strong> com nicho papeleiro.'],
  5200),
 ('08', 'Banheiro 04', '5,52 m² de chapa · 4 dobradiças',
  'MDF Arauco <strong>Nogueira Persa</strong>.',
  ['<strong>Armário superior de 1,10 m</strong> com duas portas espelhadas de '
   'correr sobre sistema RO65.',
   '<strong>Prateleiras laterais sobre suporte metálico dourado</strong> — quatro '
   'unidades.',
   '<strong>Gabinete inferior de 1,46 m</strong> com nicho aberto.'],
  6200),
]
assert sum(i[5] for i in ITENS) == CHEIO

# ── especificação técnica que atravessa o projeto ─────────────────────────
ESPEC = [
 ('Chapa', 'MDF Arauco: <strong>18 mm</strong> em frentes e prateleiras, '
  '<strong>15 mm</strong> na caixaria e <strong>6 mm</strong> nos fundos. '
  'Fundos <strong>na cor</strong>, não em branco — as perspectivas do projeto '
  'mostram o interior todo no acabamento da frente. São 160,82 m² em 48 chapas, '
  'com o plano de corte fechado por cor e por espessura: cor nenhuma divide chapa '
  'com outra.'),
 ('Borda', '579,55 m de fita de borda na cor, aplicada em <strong>coladeira '
  'automática</strong> com filetagem. O desperdício de 10% já está previsto no '
  'valor — não é reajuste posterior.'),
 ('Puxador', '30,3 m de <strong>cava 35° usinada na CNC</strong> no próprio '
  'material. Sem puxador aparente, o desenho fica limpo e não há peça de '
  'reposição a depender de fornecedor.'),
 ('Ferragem', '72 dobradiças, 17 conjuntos de corrediça, 7 articuladores de '
  'báscula e 30 prateleiras com suporte — todos na linha Intermediária '
  'especificada na página 3.'),
 ('Iluminação', 'Fita de LED em <strong>perfil de alumínio</strong>, embutida na '
  'marcenaria: prateleira do gourmet e nicho em L do banheiro social. O perfil é '
  'o que diferencia luz embutida de fita aparente.'),
 ('Espelho e vidro', 'Sete folhas de <strong>espelho prata com perfil</strong> '
  'nas portas de correr dos três banheiros, e duas folhas de <strong>vidro '
  'incolor temperado 8 mm</strong> nas básculas do gourmet.'),
 ('Serralheria', 'Estrutura metálica <strong>fendi</strong> das duas portas '
  'basculantes do gourmet, sob medida.'),
 ('Produção e montagem', 'Corte e usinagem em <strong>CNC própria</strong>, '
  'laminação de borda em coladeira automática própria, e '
  '<strong>instalação e montagem por equipe própria da Valvic</strong>. Não '
  'terceirizamos nem o que define o acabamento, nem quem entrega.'),
]

FORA = [
 ('Marmoraria', 'Bancadas 01, 02 e 03, ilha em cascata, rodabancas, nichos, '
  'cubas esculpidas, prateleiras e o "detalhe caixa" da cozinha — o projeto '
  'especifica Carrara e Travertino. É fornecimento de marmoraria.'),
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

# ⚠ 20/08: `css-proposta.css` tinha código Python colado depois do CSS (linhas
# 122–265, sobra de uma sessão antiga). O parser do navegador entrava em erro
# ali e ENGOLIA tudo que viesse depois — inclusive as regras acrescentadas
# abaixo, que simplesmente não pintavam. Arquivo truncado no fim do CSS real.
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
.mem-q{margin-left:auto;font-size:7pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--mut);font-weight:600;white-space:nowrap;}
.mem-m{color:var(--soft);font-size:8.4pt;margin:1.6mm 0 0 14mm;}
.mem ul{margin:2mm 0 0 14mm;padding:0;}
.mem li{list-style:none;color:var(--soft);font-size:8.4pt;line-height:1.52;
  margin-bottom:1.5mm;padding-left:4.5mm;position:relative;}
.mem li::before{content:'';position:absolute;left:0;top:1.9mm;width:3.5px;
  height:3.5px;border-radius:50%;background:var(--gold-lt);}
.mem-v{margin:2.4mm 0 0 14mm;font-size:8.6pt;}
.mem-v b{font-size:10.4pt;}
.mem-v s{color:var(--mut);font-weight:400;}
.esp{padding:3mm 0;border-bottom:1px solid var(--hair);display:grid;
  grid-template-columns:34mm 1fr;gap:5mm;}
.esp:last-child{border-bottom:none;}
.esp .k{font-size:7.4pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;padding-top:.5mm;}
.esp .v{color:var(--soft);font-size:8.7pt;}
/* a coluna do valor cheio encostava na faixa bege do fechamento */
.inv th:nth-child(2),.inv td:nth-child(2){padding-right:5mm;}
"""

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 8
def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria · {CLIENTE}</span>'
            f'<span>Proposta de fechamento</span><span>{n} / {NP}</span></div>')

def mem(i):
    n, tit, qtd, mat, bul, val = i
    li = ''.join(f'<li>{b}</li>' for b in bul)
    return (f'<div class="mem"><div class="mem-h"><div class="mem-n">{n}</div>'
            f'<div class="mem-t">{tit}</div><div class="mem-q">{qtd}</div></div>'
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
  <strong>sem retirar um único item do escopo</strong> — o que muda é o preço,
  não o que será executado.</p>
  <div class="pf">
    <div class="c"><div class="k">Investimento da linha Intermediária</div>
      <div class="v" style="color:var(--mut)">R$ {brl(CHEIO)}</div>
      <div class="s">Valor da proposta de 17 de agosto, escopo completo,
      garantia de 5 anos.</div></div>
    <div class="c hi"><div class="k">Com a condição de fechamento</div>
      <div class="v">R$ {brl(FECHA)}</div>
      <div class="s">Economia de <strong>R$ {brl(ECONOMIA)}</strong>. Mesmo escopo,
      mesma ferragem, mesma garantia.</div></div>
  </div>
  <div class="pf" style="margin-top:5mm">
    <div class="c"><div class="k">Entrada — 30% na assinatura</div>
      <div class="v">R$ {brl(ENTRADA)}</div>
      <div class="s">Libera a compra de material e a entrada do projeto na fila
      de produção.</div></div>
    <div class="c"><div class="k">Saldo — 70% à vista, pós-entrega</div>
      <div class="v">R$ {brl(SALDO)}</div>
      <div class="s">Pago depois da instalação concluída e conferida na obra.
      Não há parcela durante a produção.</div></div>
  </div>
  <div class="box" style="margin-top:6mm"><div class="t">O que essa condição significa na prática</div>
  <p>Entre a assinatura e o pagamento do saldo passam-se <strong>90 a 120
  dias</strong>, e nesse intervalo a Valvic compra a chapa, a ferragem, o
  espelho, o vidro e a serralheria, produz os oito conjuntos e instala — com
  30% recebido. <strong>A produção inteira é financiada por nós.</strong> É por
  isso que a condição está atrelada ao fechamento dentro da validade: ela
  pressupõe uma agenda de produção reservada.</p></div>
  <div class="box"><div class="t">O que não muda</div>
  <p>Escopo, materiais, ferragem, iluminação, espelhos, vidros, serralheria,
  prazo e garantia de 5 anos são <strong>exatamente os da proposta de 17 de
  agosto</strong>. Nenhum item foi retirado, substituído ou simplificado para
  chegar a este valor.</p></div>
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
    — o mesmo da linha Superior. Nos 17 conjuntos de gaveta desta casa, é o
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
  material, a composição construtiva e a ferragem. O valor cheio e o valor com a
  condição de fechamento aparecem ao pé de cada um.</p>
  {mem(ITENS[0])}
  {mem(ITENS[1])}
  {foot(4)}
</div></div>"""

p5 = f"""<div class="page"><div class="pad">
  {mem(ITENS[2])}
  {mem(ITENS[3])}
  {mem(ITENS[4])}
  {foot(5)}
</div></div>"""

linhas = ''.join(
    f'<tr><td class="l">{n} · {t}</td><td>{brl(v)}</td>'
    f'<td class="hi">{brl(int(round(v*0.9)))}</td></tr>'
    for n, t, _q, _m, _b, v in ITENS)

p6 = f"""<div class="page"><div class="pad">
  {mem(ITENS[5])}
  {mem(ITENS[6])}
  {mem(ITENS[7])}
  <div style="margin-top:5mm">
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

p7 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="rule"></div>
  <h2 class="h-sec">O que atravessa<br>o projeto inteiro.</h2>
  <p class="lead" style="margin-top:3.5mm">As oito linhas abaixo valem para
  todos os conjuntos do memorial, e são o que sustenta a garantia de cinco
  anos.</p>
  <div style="margin-top:4mm">{esp}</div>
  {foot(7)}
</div></div>"""

p8 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <h2 class="h-sec">Prazo, pagamento<br>e fronteiras.</h2>
  <div class="two" style="margin-top:6mm">
    <div>
      <div class="term"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da assinatura, do pagamento da entrada e da
        definição da chapa. Oito conjuntos entregues por frentes.</div></div>
      <div class="term"><div class="k">Pagamento</div>
        <div class="v">30% na assinatura · 70% à vista, pós-entrega</div>
        <div class="s">R$ {brl(ENTRADA)} na assinatura e R$ {brl(SALDO)} após a
        instalação concluída e conferida na obra. Não há parcela durante a
        produção.</div></div>
      <div class="term"><div class="k">Validade da condição</div>
        <div class="v">{VALIDADE}</div>
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
      <ul>{''.join(f'<li><div class="k">{k}</div><div class="v">{v}</div></li>'
                   for k, v in FORA)}</ul>
    </div>
  </div>
  <div class="sig">
    <div class="ln">Valvic Marcenaria</div>
    <div class="ln">{CLIENTE}</div>
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
print(f'cheio {brl(CHEIO)} → fechamento {brl(FECHA)} '
      f'(entrada {brl(ENTRADA)} + saldo {brl(SALDO)})')
