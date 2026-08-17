# -*- coding: utf-8 -*-
"""ELIUTON RIBEIRO · Residência Brisas da Pampulha — PROPOSTA, 5 páginas.

Três cenários de investimento, como o Jonathan pediu em 13/08:
  1 · Telescópica (MC 32% · 2 anos) · 2 · Hardt (37% · 5 anos) ·
  3 · Hettich Novisys / oculta Quadro (42% · 10 anos)

Valores de `corte-eliuton.py`, 3ª rodada — já sem a linha de montagem, que
NÃO entra na proposta (montador é salário fixo; ver validacao-orcamento.md).

[Jonathan 17/08] · cozinha como conjunto completo num item só
                 · realocação de R$ 5.000 da área de serviço para o painel ripado

⚠ SEM RT. Se houver RT de 10% para a arquiteta Luciana Beatriz Simplício, os
  valores sobem 24% a 30% e a proposta tem de ser refeita.
⚠ PRAZO e VALIDADE são premissa minha (F3 e F5 sem resposta). Trocar em PRAZO
  e VALIDADE abaixo se o Jonathan cravar outro.
⚠ MÁRMORE FORA. Está escrito na página 5, mas é a maior fronteira de escopo do
  job — confirmar antes de enviar.
"""
import subprocess, unicodedata

CLIENTE   = 'Eliuton Ribeiro'
OBRA      = 'Residência Brisas da Pampulha'
ARQUITETA = 'Arq. Luciana Beatriz Simplício · Núcleo SC Arquitetura'
DATA      = '17 de agosto de 2026'
VALIDADE  = '7 dias corridos'          # ⚠ premissa
PRAZO     = '90 a 120 dias úteis'      # ⚠ premissa

CEN = [
    dict(n='I', nome='Essencial', mc='2 anos',
         dobr='Dobradiça padrão com amortecimento',
         corr='Corrediça telescópica',
         basc='Pistão a gás',
         gar='2 anos',
         txt='A configuração de referência do mercado. Mecanismo correto, '
             'regulagem completa, acabamento idêntico ao das outras duas linhas — '
             'a diferença está na vida útil do movimento, não no que se vê.'),
    dict(n='II', nome='Intermediária', mc='5 anos',
         dobr='Dobradiça Hardt com amortecimento',
         corr='Corrediça oculta Hardt, fechamento suave',
         basc='Articulador Blum HK-xs',
         gar='5 anos',
         txt='A gaveta passa a correr por baixo, escondida: some o trilho lateral '
             'e o vão útil cresce. O articulador da báscula vira Blum HK-xs — o '
             'mesmo das duas linhas superiores. Dobra a garantia.'),
    dict(n='III', nome='Superior', mc='10 anos',
         dobr='Dobradiça Hettich Novisys',
         corr='Corrediça oculta Hettich Quadro',
         basc='Articulador Blum HK-xs',
         gar='10 anos',
         txt='A corrediça Quadro é o degrau que se sente na mão: curso mais longo, '
             'carga maior, retorno mais macio, e ciclo de teste muito acima do uso '
             'doméstico. Dobra a garantia outra vez.'),
]

# ── itens · valores de corte-eliuton.py (3ª rodada, com a realocação) ──────
ITENS = [
 ('Cozinha — conjunto completo',
  'Torre de cocção com nicho de geladeira (187 × 70 × 290), acabamento superior '
  'sob o forro, bancada 01 de 3,55 m com gaveteiro e nicho de lava-louças, '
  'aéreo de cinco portas (3,51 m) e ilha de 2,26 m. MDF Arauco Nogueira Persa '
  'e Sálvia 18 mm, puxador em cava usinada.',
  25300, 30700, 36000),
 ('Painel ripado do estar e jantar',
  'Parede inteira de 5,72 × 2,88 m em MDF Arauco Nogueira Persa 18 mm, ripada, '
  'com porta de correr e porta pivotante embutidas e alinhadas ao ripado — de '
  'fora, o painel é contínuo. Acabamento superior sobre a porta de correr.',
  20400, 20400, 20400),
 ('Área gourmet — bancada 02',
  'Armário inferior com gaveteiro (145 × 70), coluna da cervejeira até o forro '
  '(70 × 290), prateleira com iluminação em LED embutida e armário superior com '
  'portas em estrutura metálica fendi e vidro incolor. Nogueira Persa 18 mm.',
  10000, 12000, 14200),
 ('Área de serviço',
  'Armário de 3,59 m do piso ao forro (55 de profundidade): módulo alto para '
  'vassouras e tábua de passar embutida, nichos de máquina de lavar e secadora, '
  'dois varais retráteis, dois gavetões e armário inferior sob a bancada.',
  11600, 15000, 18200),
 ('Lavabo externo',
  'Painel de parede de 1,30 × 2,48 m, acabamento de forro em MDF e gabinete '
  'suspenso de 150 × 50 com porta basculante e nicho aberto. Nogueira Persa 18 mm.',
  2600, 3400, 3900),
 ('Banheiro master',
  'Espelheira de 1,85 m com três portas espelhadas de correr e nichos vazados '
  'nas laterais; gabinete suspenso de 1,85 × 50 com quatro portas RIPADAS e '
  'puxador metálico tipo alça preto. MDF Arauco Jequitibá 18 mm.',
  6800, 7600, 8500),
 ('Banheiro social — 1º pavimento',
  'Armário superior de 1,90 m com portas espelhadas de correr e nicho aberto com '
  'prateleiras e LED em L; gabinete inferior de 1,10 m com nicho papeleiro.',
  4700, 5200, 5900),
 ('Banheiro 04',
  'Armário superior de 1,10 m com portas espelhadas de correr e prateleiras laterais '
  'sobre suporte metálico dourado; gabinete inferior de 1,46 m com nicho aberto.',
  5500, 6200, 7000),
]
TOT = [sum(i[k] for i in ITENS) for k in (2, 3, 4)]
assert TOT == [86900, 100500, 114100], TOT

PAGTO = [
    ('Entrada de 30% + saldo em até 10× no cartão', '—'),
    ('Entrada de 50% + saldo em até 8× no cartão',  '3%'),
    ('Entrada de 70% + saldo em até 6× no cartão',  '5%'),
    ('Entrada de 70% + saldo por transferência',    '7%'),
]

FORA = [
    ('Marmoraria', 'Bancadas 01, 02 e 03, ilha em cascata, rodabancas, nichos, '
     'cubas esculpidas, prateleiras e o "detalhe caixa" da cozinha — o projeto '
     'especifica Carrara e Travertino. É fornecimento de marmoraria.'),
    ('Louças, metais e eletrodomésticos', 'Especificados no projeto (Deca, '
     'Tramontina, Brastemp, Electrolux, Metalfrio). Prevemos o vão e a usinagem.'),
    ('Alvenaria, revestimento e churrasqueira', 'Porcelanato, tijolete, azulejo, '
     'gesso e forro.'),
    ('Móveis soltos', 'Mesa de jantar, cadeiras, banquetas, buffet, sofá, '
     'poltronas e a escultura de parede.'),
    ('Elétrica e hidráulica', 'A iluminação embutida na marcenaria é nossa; os '
     'pontos de energia e de água são da obra.'),
]

# ═══════════════════════════════════════════════════════════════════════════
CSS = """
:root{
  --ink:#1A1714; --soft:#5C564C; --mut:#918A7C; --line:#E3DDD1; --hair:#F0EBE1;
  --paper:#fff; --cream:#FAF7F1; --sand:#F1EBDF;
  --gold:#9C7A3C; --gold-lt:#C6A567; --gold-pale:#F5EEDF; --deep:#241F1B;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans','Liberation Sans',Arial,sans-serif;
     color:var(--ink);font-size:9.6pt;line-height:1.62;}
.serif{font-family:'Cormorant Garamond','Liberation Serif',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;
      background:var(--paper);page-break-after:always;}
.page:last-of-type{page-break-after:avoid;}
.pad{padding:17mm 19mm 14mm;height:100%;display:flex;flex-direction:column;}
h1,h2,h3{margin:0;font-weight:600;}
p{margin:0;}
.eyebrow{font-size:7.2pt;letter-spacing:.30em;text-transform:uppercase;
         color:var(--gold);font-weight:700;}
.rule{height:1.5px;width:40px;background:var(--gold);margin:7px 0 13px;}
.h-sec{font-family:'Cormorant Garamond',Georgia,serif;font-size:23pt;
       line-height:1.12;font-weight:600;letter-spacing:-.01em;}
.lead{color:var(--soft);font-size:9.9pt;max-width:150mm;}
.foot{margin-top:auto;padding-top:8mm;border-top:1px solid var(--hair);
      display:flex;justify-content:space-between;font-size:7.2pt;
      letter-spacing:.16em;text-transform:uppercase;color:var(--mut);}

/* capa */
.cover{background:var(--deep);color:#F6F1E7;}
.cover .pad{padding:24mm 19mm 16mm;}
.cover .eyebrow{color:var(--gold-lt);}
.cover .rule{background:var(--gold-lt);width:56px;height:2px;}
.cv-t{font-family:'Cormorant Garamond',Georgia,serif;font-size:38pt;
      line-height:1.05;font-weight:600;letter-spacing:-.015em;margin-top:3mm;max-width:150mm;}
.cv-s{font-size:12.5pt;color:#CFC6B4;margin-top:5mm;font-weight:300;}
.cv-meta{margin-top:13mm;display:grid;grid-template-columns:1fr 1fr 1fr;gap:6mm;
         border-top:1px solid rgba(255,255,255,.16);padding-top:7mm;}
.cv-meta .k{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
            color:var(--gold-lt);font-weight:700;}
.cv-meta .v{font-size:10.4pt;color:#EDE6D9;margin-top:2mm;}
.cv-brand{font-size:8.6pt;letter-spacing:.42em;text-transform:uppercase;
          color:#E8DFCB;font-weight:700;}
.cv-num{position:absolute;right:19mm;top:22mm;font-family:'Cormorant Garamond',Georgia,serif;
        font-size:110pt;line-height:1;color:rgba(198,165,103,.13);font-weight:600;}

/* itens */
.it{padding:3.1mm 0;border-bottom:1px solid var(--hair);display:flex;gap:6mm;}
.it:last-child{border-bottom:none;}
.it-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:14.5pt;color:var(--gold-lt);
      font-weight:600;min-width:9mm;line-height:1.1;}
.it-t{font-size:10.4pt;font-weight:600;letter-spacing:-.005em;}
.it-d{color:var(--soft);font-size:8.4pt;margin-top:1mm;line-height:1.5;}

/* cenários */
.cen{border:1px solid var(--line);border-radius:2px;padding:4.6mm 5.6mm;
     margin-bottom:3.4mm;background:var(--cream);}
.cen.hi{background:var(--gold-pale);border-color:var(--gold-lt);}
.cen-h{display:flex;align-items:baseline;gap:4mm;}
.cen-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:20pt;
       color:var(--gold);font-weight:600;line-height:1;}
.cen-t{font-size:12.5pt;font-weight:600;}
.cen-g{margin-left:auto;font-size:7.6pt;letter-spacing:.16em;text-transform:uppercase;
       color:#fff;background:var(--gold);padding:2.2mm 3.4mm;border-radius:2px;
       font-weight:700;white-space:nowrap;}
.cen-x{color:var(--soft);font-size:8.7pt;margin-top:2mm;}
.cen-l{margin-top:2.8mm;display:grid;grid-template-columns:1fr 1fr 1fr;gap:4mm;
       border-top:1px solid var(--line);padding-top:3.2mm;}
.cen-l .k{font-size:6.8pt;letter-spacing:.16em;text-transform:uppercase;
          color:var(--mut);font-weight:700;}
.cen-l .v{font-size:8.7pt;margin-top:1mm;line-height:1.4;}

/* tabela de investimento */
table{width:100%;border-collapse:collapse;}
.inv th{font-size:6.9pt;letter-spacing:.16em;text-transform:uppercase;
        color:var(--mut);font-weight:700;text-align:right;padding:0 0 3mm;
        border-bottom:1.5px solid var(--gold);}
.inv th.l{text-align:left;}
.inv td{padding:3.1mm 0;border-bottom:1px solid var(--hair);text-align:right;
        font-variant-numeric:tabular-nums;font-size:9.6pt;}
.inv td.l{text-align:left;font-size:9.5pt;}
.inv td.hi{background:var(--gold-pale);font-weight:600;
           padding-right:2.6mm;padding-left:2.6mm;}
.inv th.hi{background:var(--gold-pale);padding-right:2.6mm;padding-left:2.6mm;
           color:var(--gold);}
.inv tr.tot td{border-bottom:none;border-top:1.5px solid var(--ink);
               padding-top:4mm;font-size:13.5pt;font-weight:600;
               font-family:'Cormorant Garamond',Georgia,serif;}
.inv tr.tot td.l{font-family:inherit;font-size:8pt;letter-spacing:.18em;
                 text-transform:uppercase;font-weight:700;}

.box{background:var(--cream);border-left:2.5px solid var(--gold);
     padding:4mm 5.2mm;margin-top:4mm;}
.box .t{font-size:7.4pt;letter-spacing:.18em;text-transform:uppercase;
        color:var(--gold);font-weight:700;}
.box p{color:var(--soft);font-size:9pt;margin-top:2mm;}

.two{display:grid;grid-template-columns:1fr 1fr;gap:9mm;}
.term{padding:3.4mm 0;border-bottom:1px solid var(--hair);}
.term:last-child{border-bottom:none;}
.term .k{font-size:6.9pt;letter-spacing:.18em;text-transform:uppercase;
         color:var(--gold);font-weight:700;}
.term .v{font-size:9.5pt;margin-top:1.2mm;}
.term .s{color:var(--soft);font-size:8.5pt;margin-top:.8mm;}
.pay td{padding:2.6mm 0;border-bottom:1px solid var(--hair);font-size:9pt;}
.pay td.d{text-align:right;font-weight:600;color:var(--gold);
          font-variant-numeric:tabular-nums;}
.fora .k{font-size:9.3pt;font-weight:600;}
.fora .v{color:var(--soft);font-size:8.6pt;margin-top:.8mm;}
.fora li{margin-bottom:3.2mm;list-style:none;}
.fora ul{margin:0;padding:0;}
.sig{margin-top:auto;padding-top:9mm;display:grid;grid-template-columns:1fr 1fr;gap:14mm;}
.sig .ln{border-top:1px solid var(--ink);padding-top:2.4mm;font-size:8.4pt;
         color:var(--soft);}
"""

def brl(v): return f'{v:,.0f}'.replace(',', '.')

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria · {CLIENTE}</span>'
            f'<span>{OBRA}</span><span>{n} / 5</span></div>')

# ── páginas ────────────────────────────────────────────────────────────────
p1 = f"""<div class="page cover"><div class="pad">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div style="margin-top:auto">
    <div class="eyebrow">Proposta de marcenaria planejada</div>
    <div class="rule"></div>
    <div class="cv-t">{OBRA}</div>
    <div class="cv-s">{CLIENTE}</div>
  </div>
  <div class="cv-meta">
    <div><div class="k">Projeto</div><div class="v">{ARQUITETA}</div></div>
    <div><div class="k">Data</div><div class="v">{DATA}</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
  </div>
</div></div>"""

itens_html = ''.join(
    f'<div class="it"><div class="it-n">{i:02d}</div><div>'
    f'<div class="it-t">{t}</div><div class="it-d">{d}</div></div></div>'
    for i, (t, d, *_v) in enumerate(ITENS, 1))

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O que está sendo proposto</div>
  <div class="rule"></div>
  <h2 class="h-sec">Oito conjuntos,<br>uma casa inteira.</h2>
  <p class="lead" style="margin-top:4mm">Levantamento feito peça a peça sobre o
  executivo da arquiteta — as dezoito pranchas, cota a cota. São
  <strong>160,8 m² de chapa</strong> em quatro acabamentos Arauco, com o interior
  dos móveis na mesma cor da frente.</p>
  <div style="margin-top:5mm">{itens_html}</div>
  {foot(2)}
</div></div>"""

cen_html = ''.join(
    f'<div class="cen{" hi" if c["n"]=="II" else ""}">'
    f'<div class="cen-h"><div class="cen-n">{c["n"]}</div>'
    f'<div class="cen-t">{c["nome"]}</div>'
    f'<div class="cen-g">Garantia {c["gar"]}</div></div>'
    f'<div class="cen-x">{c["txt"]}</div>'
    f'<div class="cen-l">'
    f'<div><div class="k">Dobradiça</div><div class="v">{c["dobr"]}</div></div>'
    f'<div><div class="k">Corrediça</div><div class="v">{c["corr"]}</div></div>'
    f'<div><div class="k">Báscula</div><div class="v">{c["basc"]}</div></div>'
    f'</div></div>' for c in CEN)

p3 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Três configurações</div>
  <div class="rule"></div>
  <h2 class="h-sec">O que muda entre elas<br>é o movimento.</h2>
  <p class="lead" style="margin-top:4mm">O desenho, a chapa, o acabamento e o
  esquadro são <strong>os mesmos nas três</strong>. O que separa uma da outra é
  a ferragem — e ferragem se mede em ciclo de abertura, amortecimento e
  regulagem. Por isso a garantia dobra a cada degrau: ela é a tradução, em papel,
  daquilo que a mão sente.</p>
  <div style="margin-top:5mm">{cen_html}</div>
  <div class="box"><div class="t">Uma observação honesta</div>
  <p>A garantia acima é <strong>garantia Valvic</strong> — nossa, escrita e
  assinada na entrega. Não é a garantia do fabricante da ferragem, que não faz
  parte do que a gente vende.</p></div>
  {foot(3)}
</div></div>"""

linhas = ''.join(
    f'<tr><td class="l">{t}</td><td>{brl(a)}</td>'
    f'<td class="hi">{brl(b)}</td><td>{brl(c)}</td></tr>'
    for t, _d, a, b, c in ITENS)

p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h-sec">Item a item,<br>nas três linhas.</h2>
  <table class="inv" style="margin-top:7mm">
    <tr><th class="l">Conjunto</th><th>I · Essencial</th>
        <th class="hi">II · Intermediária</th><th>III · Superior</th></tr>
    {linhas}
    <tr class="tot"><td class="l">Investimento total</td>
      <td>{brl(TOT[0])}</td><td class="hi">{brl(TOT[1])}</td>
      <td>{brl(TOT[2])}</td></tr>
  </table>
  <div class="box"><div class="t">Por que o painel ripado não muda de preço</div>
  <p>Ele é o único conjunto sem uma única dobradiça, corrediça ou báscula: são
  ripas, painel e dois sistemas de porta. Como a diferença entre as três linhas
  está inteiramente na ferragem, o painel custa o mesmo nas três — e representa
  <strong>{TOT[1] and round(20400/TOT[1]*100)}% do investimento na linha
  intermediária</strong>.</p></div>
  <div class="box" style="border-left-color:var(--mut)">
  <div class="t" style="color:var(--mut)">O que está dentro do valor</div>
  <p>Projeto executivo de marcenaria, fornecimento de material, produção em CNC
  e coladeira automática próprias, transporte e entrega na obra.</p></div>
  {foot(4)}
</div></div>"""

pay = ''.join(f'<tr><td>{c}</td><td class="d">{d}</td></tr>' for c, d in PAGTO)
fora = ''.join(f'<li><div class="k">{k}</div><div class="v">{v}</div></li>'
               for k, v in FORA)

p5 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <h2 class="h-sec">Prazo, pagamento<br>e fronteiras.</h2>
  <div class="two" style="margin-top:7mm">
    <div>
      <div class="term"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da liberação da frente de trabalho na obra e da
        aprovação do projeto executivo de marcenaria.</div></div>
      <div class="term"><div class="k">Garantia</div>
        <div class="v">2, 5 ou 10 anos — conforme a linha escolhida</div>
        <div class="s">Garantia Valvic, documentada e assinada na entrega.
        Retorno em 24 h e visita técnica em até 3 dias úteis, sem custo dentro
        do prazo.</div></div>
      <div class="term"><div class="k">Validade desta proposta</div>
        <div class="v">{VALIDADE}</div></div>
      <div class="term"><div class="k">Produção</div>
        <div class="v">CNC e coladeira automática próprias</div>
        <div class="s">Corte, usinagem da cava e laminação de borda feitos na
        nossa fábrica — sem terceirizar o que define o acabamento.</div></div>
      <table class="pay" style="margin-top:5mm">
        <tr><td colspan="2" style="border:none;padding-bottom:1mm">
          <span class="eyebrow">Formas de pagamento</span></td></tr>
        {pay}
      </table>
      <p style="color:var(--mut);font-size:7.9pt;margin-top:2.5mm">
      O desconto por transferência devolve ao cliente a taxa de máquina que
      deixamos de pagar.</p>
    </div>
    <div class="fora">
      <div class="eyebrow">Não incluso nesta proposta</div>
      <div class="rule"></div>
      <ul>{fora}</ul>
    </div>
  </div>
  <div class="sig">
    <div class="ln">Valvic Marcenaria</div>
    <div class="ln">{CLIENTE}</div>
  </div>
  {foot(5)}
</div></div>"""

HTML = (f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        f'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>'
        f'{p1}{p2}{p3}{p4}{p5}</body></html>')

OUT_H = 'projetos/proposta-eliuton.html'
OUT_P = 'projetos/proposta-eliuton.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML)
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H}  ·  {OUT_P}')
print(f'Total: {brl(TOT[0])} · {brl(TOT[1])} · {brl(TOT[2])}')
