# -*- coding: utf-8 -*-
"""HONDA · MINAS MOTOS SANTA EFIGÊNIA — proposta da marcenaria do showroom.

Layout editorial comercial — o mesmo do SPE Nova Lima, lendo o CSS direto do
`build-lm.py` para os dois nunca divergirem. Mesmo perfil de cliente: obra
comercial especificada por escritório de arquitetura.

[Jonathan 07/08] fechou os cinco pontos abertos:
  1. sem RT · MC 32%
  2. chapa Duratex na linha Fosco (18 mm R$ 600) — confirmado
  3. serralheria do metalon: R$ 600 (eu tinha estimado 1.200)
  4. tampo do MA-02 em MDF Palha — não é pedra
  5. fixação invisível orçada como está

  MA-01 · Armário superior ......  R$  5.900
  MA-02 · Armário inferior em L .  R$ 12.000
  TOTAL .........................  R$ 17.900     custo direto 8.599,01 · MC 32,0%

Pagamento 40/40/20 (contrato corporativo, canteiro em andamento) em vez da
escada — a MC 32% a escada chega a 28,2% no último degrau, encostada no piso.

Garantia 5 ANOS: o gaveteiro usa corrediça OCULTA HARDT. Tabela corrigida da
casa (telescópica 2 anos · oculta Hardt 5 anos). Sem abrir por componente.
"""
import pathlib, re
P = pathlib.Path('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos')

CSS = re.search(r'<style>\n(.*?)\n</style>',
                (P/'build-lm.py').read_text(encoding='utf-8'), re.S).group(1)

FRENTES = [
 ('MA-01 — Armário superior · 3,15 m em MDF Amêndola Rústica, básculas, '
  'nicho e prateleiras sobre metalon',                                     5900),
 ('MA-02 — Armário inferior em “L” · 4,36 m de desenvolvimento em MDF Palha, '
  '6 portas de giro e gaveteiro de 4 gavetas',                            12000),
]
TOT = sum(v for _, v in FRENTES)
assert TOT == 17900, TOT

def br(v): return f'{v:,.0f}'.replace(',', '.')
linhas = ''.join(f'<tr><td class="nmc">{n}</td><td class="r" style="white-space:nowrap">R$ {br(v)}</td></tr>'
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
    <div class="client">Minas Motos · Santa Efigênia</div>
    <div class="proj">Marcenaria do showroom — projeto executivo Mímesis Arquitetura, prancha AR-18 R07</div>
    <div class="meta">
      <div class="m"><div class="t">Escopo</div><div class="v">MA-01 Armário superior · MA-02 Armário inferior</div></div>
      <div class="m"><div class="t">Acabamentos</div><div class="v">MDF Duratex Amêndola Rústica · Palha · metalon preto</div></div>
    </div>
    <div class="foot">
      <div><span class="sparkles">&#10022; &#10022; &#10022;</span><br>Do executivo ao encaixe, medido no milímetro.</div>
      <div style="text-align:right">7 de agosto de 2026<br>validade 15 dias</div>
    </div>
  </div>
</div>

<!-- ESCOPO -->
<div class="page">
  <div class="eyebrow">O que será executado</div>
  <div class="section-h serif">Duas peças, lidas cota a cota</div>
  <hr class="rule">
  <p class="lead">A prancha AR-18 separa <b>mobiliário</b> (MB01 a MB40, padrão Honda e fornecedores
  indicados) de <b>marcenaria</b> (MA-01 e MA-02). Esta proposta cobre exatamente a segunda tabela —
  nada a mais, nada a menos. O levantamento saiu das cotas do executivo, elevação por elevação,
  e não de estimativa por metro quadrado.</p>

  <div class="block">
    <div class="nm">MA-01 · Armário superior</div>
    <div class="sub">Showroom · 3,15 m × 30 cm de profundidade · topo a 2,24 m do piso acabado</div>
    <ul>
      <li>Corpo em <b>MDF Duratex Amêndola Rústica</b>, com a base inteira na cor — é aéreo, o
      fundo do móvel fica à vista de quem passa.</li>
      <li><b>3 portas basculantes</b> de 69,5 / 70 / 70 cm, em pistão a gás <b>com amortecimento</b>.</li>
      <li><b>Nicho aberto de 88 × 36 cm</b> com o interior integralmente na cor, inclusive o fundo.</li>
      <li><b>3 prateleiras</b> — uma de 2,13 m e duas de 92 cm — apoiadas nas prumadas de metalon.</li>
      <li>Puxador em <b>cava embutida</b> usinada na própria frente, conforme o DT-01 da prancha.</li>
    </ul>
  </div>

  <div class="block">
    <div class="nm">MA-02 · Armário inferior em “L”</div>
    <div class="sub">Showroom · 2,34 m + 2,02 m · altura 84 cm (sóculo 10 + corpo 74)</div>
    <ul>
      <li>Corpo em <b>MDF Duratex Palha</b>, com <b>tampo do móvel</b> no mesmo acabamento.</li>
      <li><b>6 portas de giro</b> — 39 / 39 / 39 cm numa perna e 46 / 46 / 45,5 cm na outra —
      todas em <b>dobradiça com amortecimento</b>.</li>
      <li><b>Gaveteiro de 55 cm com 4 gavetas</b> de 16,5 cm em <b>corrediça oculta</b>.</li>
      <li>Sóculo recuado de 10 cm correndo todo o desenvolvimento.</li>
      <li>Puxador em <b>cava embutida superior</b> contra o tampo, conforme o DT-02 da prancha.</li>
    </ul>
  </div>

  <div class="highlights">
    <div class="hl perg">
      <div class="t">Metalon preto — estrutura, não enfeite</div>
      <ul>
        <li><b>3 prumadas em metalon 20×20</b> com <b>pintura eletrostática preta</b>, que carregam
        as prateleiras abertas do MA-01.</li>
        <li>Travessa sob a prateleira de 2,13 m — em vão livre desse tamanho, o apoio é o que
        mantém a linha reta ao longo do tempo.</li>
      </ul>
    </div>
    <div class="hl port">
      <div class="t">Fixação invisível</div>
      <ul>
        <li>O MA-01 sobe <b>sem nenhum suporte aparente</b>, conforme a nota 3 da prancha.</li>
        <li>3,15 m em balanço exigem ancoragem dimensionada — <b>a parede de fixação será
        conferida na obra</b> antes da produção, como pede a nota 2.</li>
      </ul>
    </div>
  </div>

  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>Minas Motos Santa Efigênia · Projeto Mímesis Arquitetura</span></div>
</div>

<!-- INVESTIMENTO -->
<div class="page">
  <div class="eyebrow">Investimento</div>
  <div class="section-h serif">Do desenho ao encaixe</div>
  <hr class="rule">

  <div class="hero" style="margin-top:4mm;">
    <div class="t">Investimento total</div>
    <div class="big serif">R$ {br(TOT)}</div>
    <div class="cap">Marcenaria MA-01 e MA-02 do showroom — fornecimento, serralheria coordenada
    e instalação por equipe própria Valvic.</div>
  </div>

  <table>
    <thead><tr><th>Frente</th><th class="r">Valor</th></tr></thead>
    <tbody>
      {linhas}
    </tbody>
    <tfoot><tr class="grand"><td class="serif">Total</td><td class="r serif" style="white-space:nowrap">R$ {br(TOT)}</td></tr></tfoot>
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
        <div class="term"><div class="t">Entrega</div><div class="b">30 a 40<br>dias úteis</div></div>
        <div class="term"><div class="t">Garantia</div><div class="b">5 anos</div></div>
      </div>
    </div>
  </div>

  <div class="note" style="margin-top:5mm;">
    <div class="h">Premissas &amp; não inclusos</div>
    <b>Acabamentos:</b> MDF Duratex Amêndola Rústica no MA-01 e MDF Duratex Palha no MA-02;
    caixaria interna em branco, exceto o nicho aberto do MA-01, que vai integralmente na cor.
    Metalon 20×20 com pintura eletrostática preta — item de serralheria, fornecido por parceiro e
    <b>coordenado e instalado pela Valvic</b> (incluso).
    <b>Adições técnicas já contempladas:</b> duas divisórias internas no caixote das básculas
    (o desenho traz 2,09 m de vão sem apoio) e uma prateleira por módulo de porta no MA-02.
    <b>Não inclusos:</b> os itens de mobiliário MB01 a MB40 (padrão Honda, Home Office, Leroy
    Merlin, Madeira Madeira), a bancada BG07, a cervejeira e a adega, pontos elétricos e
    hidráulicos, gesso, pintura e obra civil. Medidas a conferir no local e parede de fixação a
    verificar antes da produção, conforme as notas da prancha AR-18.
  </div>

  <div class="pfoot"><span class="brandline">valvic<span class="dot">.</span> marcenaria</span><span>Minas Motos Santa Efigênia · Prancha AR-18 R07 · 07/08/2026</span></div>
</div>

</body></html>"""

(P/'proposta-honda-minas-motos.html').write_text(HTML, encoding='utf-8')
print('wrote proposta-honda-minas-motos.html', len(HTML))
