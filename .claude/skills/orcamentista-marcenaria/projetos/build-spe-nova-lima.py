# -*- coding: utf-8 -*-
"""SPE NOVA LIMA 1 — proposta COMPLETA (stand + apartamento decorado).

[Jonathan 07/08] "quero o layout igual a primeira versao que foi apresentada.
obs. NAO TEM NADA CONTRATADO AINDA."

→ Reaproveita o CSS de `build-lm.py` (a proposta de 17/07) lendo o arquivo
  direto: layout editorial claro, capa creme com moldura dourada, blocos com
  filete, tabela de frentes, hero do investimento. Mesma casca, escopo maior.

→ E cai a moldura "contratado + adição" que a versão anterior usava. Nada foi
  assinado: é UMA proposta, agora com dez frentes.

[Jonathan 07/08] "elevar a MC para 35% e dar 5 anos de garantia · SEMPRE mantendo
os valores do orçamento inicial do Stand de vendas."

  Stand ....... 88.200 INTOCADO (MC 40%, como saiu em 17/07)
  Decorado .... MC 35% exata: 25.300 + 15.500 + 29.400 + 31.000 = 101.200
  TOTAL ....... R$ 189.400

[Jonathan 21/08] DUAS PRANCHAS NOVAS entram no escopo do decorado:
  DET 07 · Armário 1 COPA  ·  DET 02 · ILHA GOURMET
Seis ambientes agora, 167,5 m² de chapa contra 137,0.

  Stand ....... 88.200 INTOCADO
  Decorado .... 24.700 + 15.800 + 29.800 + 30.300 + 6.200 + 9.000 = 115.800
  TOTAL ....... R$ 204.000

⚠️ NÃO É SOMAR DUAS LINHAS. O motor rodou inteiro e os quatro ambientes que já
   existiam MUDARAM: a chapa Frapé passou a render mais (a copa e a ilha
   preenchem sobra que a cozinha pagava sozinha) e a logística subiu com a
   área. A COZINHA CAIU de 25.300 para 24.700; sala, quarto e suíte subiram um
   pouco. A MC de 35% no decorado está mantida, exata.

⚠️ MC 35% exata no decorado dá R$ 101.200, e não os 103.300 que estavam na versão
   anterior. Aqueles 103.300 nunca foram alvo — eram o resíduo de segurar o número
   redondo de 191.500, o que deixava a MC em 35,9%. Travando 35%, o total cai
   R$ 2.100. MC combinada do contrato: 37,2% com o escopo de 21/08.

⚠️ GARANTIA 5 ANOS (era 2). Coerente com a tabela corrigida da casa: corrediça
   oculta = 5 anos. O decorado tem Dominus, oculta e articuladores; o stand é
   painelaria e pérgola, quase sem ferragem móvel — risco estrutural baixo.
"""
import pathlib, re
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

# CSS idêntico ao da primeira versão — lido do próprio build original
CSS = re.search(r'<style>\n(.*?)\n</style>',
                (P/'build-lm.py').read_text(encoding='utf-8'), re.S).group(1)

FRENTES = [
 ('Painéis — MDF Cravo Trend (Gourmet/Lounge + Corretores + Pilar)',      45700),
 ('Pérgola — 28 ripas metalon #10×5 revestido em MDF madeirado',          18000),
 ('Portas — de giro (copa + armário) e acesso ao QG',                      5500),
 ('Móveis + complementos — armário gourmet, móvel lounge, sanca, inox',   19000),
 ('Cozinha do decorado — bancada em “L”, aéreos em dois planos, torre do forno', 24700),
 ('Sala do decorado — 7,20 m de painelaria, espelhos e rodapé de inox',   15800),
 ('Quarto do decorado — roupeiro espelhado, nichos em laca, cabeceira',   29800),
 ('Suíte do decorado — torre de nichos, roupeiro espelhado, painel ripado', 30300),
 ('Copa — armário de 2,60 m em Frapé Matt, quatro portas e gaveteiro (DET 07)', 6200),
 ('Ilha gourmet — 3,40 × 0,90 m, nicho de adega, armário e prateleira (DET 02)', 9000),
]
TOT = sum(v for _, v in FRENTES)
assert TOT == 204000, TOT
def br(v): return f'{v:,.0f}'.replace(',', '.')
linhas = ''.join(f'<tr><td class="nmc">{n}</td><td class="r">R$ {br(v)}</td></tr>'
                 for n, v in FRENTES)

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8">
<style>
{CSS}
</style></head>
<body>

<!-- CAPA -->
<div class="page cover">
  <div class="frame"></div>
  <div class="inner">
    <div><div class="brand">valvic<span class="dot">.</span></div><div class="brand-sub">MARCENARIA</div></div>
    <div class="kicker">Proposta comercial</div>
    <div class="client">SPE Nova Lima 1</div>
    <div class="proj">Stand de vendas e apartamento decorado — projeto arq. Lodi Motta</div>
    <div class="meta">
      <div class="m"><div class="t">Escopo</div><div class="v">Stand · Cozinha · Sala · Quarto · Suíte</div></div>
      <div class="m"><div class="t">Acabamentos</div><div class="v">Cravo Trend · Anis · Frapé · Ciliegio</div></div>
    </div>
    <div class="foot">
      <div><span class="sparkles">&#10022; &#10022; &#10022;</span><br>Do executivo ao encaixe, medido no milímetro.</div>
      <div style="text-align:right">7 de agosto de 2026<br>validade 15 dias</div>
    </div>
  </div>
</div>

<!-- ESCOPO 1 · STAND -->
<div class="page">
  <div class="eyebrow">O que será executado · parte 1</div>
  <div class="section-h serif">Stand de vendas</div>
  <hr class="rule">
  <p class="lead">Leitura fiel do seu executivo — cada painel medido parede a parede e o metalon
  da pérgola calculado ripa a ripa. Nada estimado.</p>

  <div class="block">
    <div class="nm">Gourmet / Lounge</div>
    <div class="sub">Painéis · armário gourmet · móvel do lounge</div>
    <ul>
      <li>Painéis em <b>MDF Arauco Realce Cravo Trend</b> revestindo as paredes do ambiente (~63 m²), com rodapé em perfil de inox h=5.</li>
      <li><b>Armário Gourmet</b> (97,5×248×42) — exterior Cravo Trend, caixa/nicho em Moscada Matt, 2 portas.</li>
      <li><b>Móvel do Lounge</b> (300×60×35) em Moscada Matt — 2 nichos e 4 gavetas, sobre pés metálicos.</li>
      <li>Porta ripada e forro em MDF madeirado.</li>
    </ul>
  </div>

  <div class="block">
    <div class="nm">Corretores &amp; Pilar central</div>
    <div class="sub">Backdrop · stand · pilar</div>
    <ul>
      <li>Painel dos corretores em Cravo Trend (backdrop 8,17×3,85) com <b>caixa em marcenaria</b> (nicho central recuado, h=260).</li>
      <li>Painel do <b>pilar central</b> envolvendo a coluna (h=3,85) com <b>moldura de hidrante em MDF</b> e <b>sanca com LED 3000K</b>.</li>
    </ul>
  </div>

  <div class="highlights">
    <div class="hl perg">
      <div class="t">Pérgola — metalon #10×5</div>
      <ul>
        <li><b>28 ripas de 3,09 m</b> em perfil metálico #10×5 <b>revestido em MDF madeirado</b>.</li>
        <li>Calculadas ripa a ripa (barra de 6 m, 1 ripa/barra). Fornecimento, revestimento e instalação.</li>
      </ul>
    </div>
    <div class="hl port">
      <div class="t">Portas em destaque</div>
      <ul>
        <li><b>Portas de giro</b> na copa (2, com painel entre elas) e no <b>armário gourmet</b> (2).</li>
        <li><b>Porta de acesso ao QG</b> embutida no painel, sem ferragem aparente.</li>
      </ul>
    </div>
  </div>

  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>SPE Nova Lima 1 · Projeto Lodi Motta</span></div>
</div>

<!-- ESCOPO 2 · DECORADO -->
<div class="page">
  <div class="eyebrow">O que será executado · parte 2</div>
  <div class="section-h serif">Apartamento decorado</div>
  <hr class="rule">
  <p class="lead">Seis ambientes das pranchas MO 03, DET 05, DET 06, DET 02 e DET 07 — executivas e cotadas.
  O levantamento saiu das elevações, não de estimativa por metro quadrado.</p>

  <div class="block">
    <div class="nm">Cozinha</div>
    <div class="sub">MO 03 · Anis Matt + Frapé Matt</div>
    <ul>
      <li>Bancada em <b>“L”</b> com módulos de giro e a <b>torre do forno</b> com 3 gavetas em corrediça oculta.</li>
      <li>Aéreos em <b>dois planos de profundidade</b> — 62 cm em Anis e 40 cm em Frapé, com <b>8 básculas</b> em articulador.</li>
      <li>Nicho do micro-ondas, vão da coifa de embutir e painel alto de <b>2,55 m</b> com nichos.</li>
      <li>Puxador em <b>cava usinada</b>, conforme o DET.03 da prancha.</li>
    </ul>
  </div>

  <div class="block">
    <div class="nm">Sala</div>
    <div class="sub">MO 03 · 7,20 m de painelaria</div>
    <ul>
      <li>Duas elevações de painel a <b>2,55 m</b> de altura, em Anis Matt.</li>
      <li>Painel com <b>4 nichos de espelho</b> emoldurados e <b>espelho de 1,90 m</b>; painel com 3 nichos e porta embutida.</li>
      <li><b>Rodapé em perfil de inox escovado</b> 5×0,5 correndo a base, como no stand.</li>
    </ul>
  </div>

  <div class="highlights" style="display:grid;grid-template-columns:1fr 1fr;gap:5mm">
    <div class="hl perg">
      <div class="t">Quarto — Ciliegio Poro + laca</div>
      <ul>
        <li>Roupeiro de 1,54 m com <b>duas portas de correr espelhadas</b> em esquadria de alumínio, sistema <b>Dominus</b>.</li>
        <li>Módulo de <b>nichos iluminados em laca brilhante</b> Sayerlack M072.</li>
        <li>Cabeceira estofada, painel de TV, prateleira suspensa, bancada de trabalho e criado suspenso.</li>
      </ul>
    </div>
    <div class="hl port">
      <div class="t">Suíte — Anis + Frapé</div>
      <ul>
        <li><b>Torre de 5 nichos iluminados</b> em Frapé, do piso ao teto.</li>
        <li>Roupeiro de 1,935 m com <b>duas portas de correr espelhadas</b>, sistema Dominus.</li>
        <li><b>Painel ripado</b> em perfil de madeira 5×1,5 · cabeceira estofada e cortineiro com iluminação.</li>
      </ul>
    </div>
    <div class="hl perg">
      <div class="t">Copa — armário 1 · DET 07</div>
      <ul>
        <li>Armário de <b>2,60 m</b> em <b>Frapé Matt</b>: quatro portas de giro, gaveteiro central de quatro gavetas e prateleira em cada módulo.</li>
        <li><b>Puxador em cava usinada</b> com fita de bordo, conforme o DET.01.</li>
        <li>Vão preparado para a cuba; bancada e rodabanca são <b>pedra</b>.</li>
      </ul>
    </div>
    <div class="hl port">
      <div class="t">Ilha gourmet · DET 02</div>
      <ul>
        <li>Corpo de <b>3,40 × 0,90 m</b>. Móvel de ilha: <b>não há face de fundo</b> — os quatro lados são acabamento.</li>
        <li><b>Nicho ventilado para a adega Duo Maxi Crissair</b>, armário com porta e prateleira aberta.</li>
        <li>Bancada em pedra, cuba e torneira <b>fora deste valor</b>.</li>
      </ul>
    </div>
  </div>

  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>SPE Nova Lima 1 · Projeto Lodi Motta</span></div>
</div>

<!-- INVESTIMENTO -->
<div class="page">
  <div class="eyebrow">Investimento</div>
  <div class="section-h serif">Uma execução, do desenho ao encaixe</div>
  <hr class="rule">

  <div class="hero" style="margin-top:4mm;">
    <div class="t">Investimento total</div>
    <div class="big serif">R$ {br(TOT)}</div>
    <div class="cap">Stand de vendas e apartamento decorado — fornecimento, terceiros coordenados
    e instalação por equipe própria Valvic.</div>
  </div>

  <table>
    <thead><tr><th>Frente</th><th class="r">Valor</th></tr></thead>
    <tbody>
      {linhas}
    </tbody>
    <tfoot><tr class="grand"><td class="serif">Total</td><td class="r serif">R$ {br(TOT)}</td></tr></tfoot>
  </table>

  <div class="split" style="margin-top:5mm;">
    <div>
      <h3 class="blk">Condições de pagamento</h3>
      <div class="hrule"></div>
      <ul class="pay">
        <li><b>40%</b> de entrada (assinatura)</li>
        <li><b>40%</b> no início da montagem</li>
        <li><b>20%</b> na entrega final</li>
      </ul>
    </div>
    <div>
      <h3 class="blk">Prazo &amp; garantia</h3>
      <div class="hrule"></div>
      <div class="terms">
        <div class="term"><div class="t">Entrega</div><div class="b">60 a 75<br>dias úteis</div></div>
        <div class="term"><div class="t">Garantia</div><div class="b">5 anos</div></div>
      </div>
    </div>
  </div>

  <div class="note" style="margin-top:5mm;">
    <div class="h">Premissas &amp; não inclusos</div>
    <b>Stand:</b> painéis em MDF Arauco Realce Cravo Trend (aparente) e Moscada Matt
    (caixas/móveis); pérgola em metalon #10×5 revestido em MDF madeirado.
    <b>Decorado:</b> MDF Arauco Anis Matt e Frapé Matt na cozinha, sala e suíte; Ciliegio Poro
    e laca brilhante Sayerlack M072 no quarto; caixaria interna em branco.
    Rodapé em perfil de <b>inox escovado 5×0,5 (h=5 cm)</b> — item de serralheria, fornecido por
    parceiro e coordenado/instalado pela Valvic (incluso). Espelhos, laca, estofados e LED
    <b>coordenados pela Valvic e entregues instalados</b>.
    <b>Não inclusos:</b> forro e caixas em gypsum, porta veneziana e vidro temperado do pilar
    (terceiros), pintura, cortinas, tapetes, eletrodomésticos, bancadas de pedra, cubas e
    metais, pontos elétricos/hidráulicos e obra civil. Medidas a conferir no local, conforme
    nota das pranchas.
  </div>

  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>SPE Nova Lima 1 · Projeto Lodi Motta · 21/08/2026</span></div>
</div>

</body></html>"""

(P/'proposta-spe-nova-lima.html').write_text(HTML, encoding='utf-8')
import subprocess
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-spe-nova-lima.pdf')], check=True)
print(f'proposta-spe-nova-lima.html · .pdf   ·   total R$ {br(TOT)}')
