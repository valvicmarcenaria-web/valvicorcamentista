# -*- coding: utf-8 -*-
"""LUCIANA — PROPOSTA, 7 páginas. Os 41 móveis descritos um a um.

Valores de `corte-a4d.py` · três linhas com as MCs cravadas pelo Jonathan em
18/08: telescópica 30% · Hardt 35% · Hettich 38%.

DECISÕES DO JONATHAN, 18/08, todas aplicadas:
  · chapa = MDF melamínico COR PADRÃO da tabela
  · pedras FORA do escopo
  · básculas da cozinha em MDF — e SINALIZADO na proposta (pág. 3 e 7)
  · palhinha a R$ 550/m · escrivaninha com regulagem é processo de marcenaria

⚠ ESTE ORÇAMENTO É DE 1ª RODADA. As pranchas foram lidas pelo conector do
  Drive, que devolve texto sem coordenadas — dá o móvel, o material e as
  larguras, não o corte peça a peça. A área de chapa saiu do fator empírico da
  casa. Serve para decidir, não para assinar. Está escrito na página 7.

⚠ ESCOPO DE AMBIENTES EM ABERTO [Jonathan 18/08]. A proposta traz os dez
  ambientes lidos; se algum sair, é recalcular — não basta subtrair a linha,
  porque o custo fixo se redistribui.
⚠ PRAZO e VALIDADE são premissa minha.
⚠ SEM RT.
"""
import subprocess

CLIENTE  = 'Luciana'
OBRA     = 'Projeto de interiores — residência'
DATA     = '18 de agosto de 2026'
VALIDADE = '7 dias corridos'            # ⚠ premissa
PRAZO    = '120 a 150 dias corridos'    # ⚠ premissa (job 78% maior que o Eliuton)

CEN = [
    dict(n='I', nome='Essencial', gar='2 anos',
         dobr='Dobradiça padrão com amortecimento',
         corr='Corrediça telescópica',
         basc='Pistão a gás',
         txt='A configuração de referência do mercado. Mecanismo correto, '
             'regulagem completa e acabamento idêntico ao das outras duas '
             'linhas — a diferença está na vida útil do movimento, não no que '
             'se vê.'),
    dict(n='II', nome='Intermediária', gar='5 anos',
         dobr='Dobradiça Hardt com amortecimento',
         corr='Corrediça oculta Hardt, fechamento suave',
         basc='Articulador Blum HK-xs',
         txt='A gaveta passa a correr por baixo, escondida: some o trilho '
             'lateral e o vão útil cresce. Num projeto com 68 gavetas, é o '
             'degrau que mais se sente no dia a dia. Dobra a garantia.'),
    dict(n='III', nome='Superior', gar='10 anos',
         dobr='Dobradiça Hettich Novisys',
         corr='Corrediça oculta Hettich Quadro',
         basc='Articulador Blum HK-xs',
         txt='A corrediça Quadro tem curso mais longo, carga maior, retorno '
             'mais macio e ciclo de teste muito acima do uso doméstico. '
             'Dobra a garantia outra vez.'),
]

# ── os 41 móveis, por ambiente ─────────────────────────────────────────────
ESCOPO = [
 ('Cozinha', '4,28 m de parede', [
  ('Armários inferiores', '428,5 × 41 prof — sete portas e quatro gavetas, com '
   'nichos para lava-louças de embutir, cervejeira e adega. Puxador em cava '
   'usinada no próprio material.'),
  ('Armário suspenso com básculas', '264 × 35 prof — três portas e duas '
   'básculas em MDF, com fita de LED na parte inferior e báscula com '
   'escorredor em inox.'),
  ('Torre de fornos', '98 × 211, prof 70 — quatro portas e nicho para '
   'micro-ondas de embutir.'),
  ('Armário do nicho da geladeira', '108 × 211, prof 70 — duas portas.'),
  ('Armário inferior com ripado vazado', '108 × 88 — o ripado é funcional: '
   'ventila a churrasqueira sem abrir mão do desenho contínuo.'),
 ]),
 ('Sala e home theater', 'painel de 6,77 m', [
  ('Painel de parede', '677 × 273 — com porta de correr embutida de acesso ao '
   'corredor, puxador usinado no próprio material. De fora, o painel é '
   'contínuo: a porta desaparece nele.'),
  ('Cristaleira', '99,5 × 218,5 — portas de giro em vidro reflecta bronze, '
   'prateleiras com iluminação em LED.'),
  ('Rack de equipamentos', '183 × 62 × 45 prof — três gavetas, ventilação e '
   'passagem de cabo previstas para receiver e subwoofer.'),
  ('Móvel inferior', '245 × 43,5 × 45 prof — cinco portas de giro, cava.'),
  ('Nicho com fundo ripado', '140 × 69 × 20 prof — LED na parte superior.'),
 ]),
 ('Espaço kids', 'painel de 3,72 m', [
  ('Estrutura do painel de TV', '372,5 × 249, prof 45 — painel de fundo e '
   'nicho central preparado para suporte de TV ajustável em altura e posição.'),
  ('Painel ripado sobreposto', '350 × 249, prof 2 — a camada ripada que dá o '
   'relevo à parede inteira.'),
  ('Prateleiras', 'três de 1,29 m, prof 20.'),
  ('Gavetões com rodízio embutido', 'quatro de 50 × 45 — rodam para fora e '
   'viram baú de brinquedo.'),
 ]),
 ('Quarto infantil', '', [
  ('Cabeceira ripada', '264 × 118 — com rebaixo para a descida da persiana.'),
  ('Cabeceira ripada iluminada', '239 × 118 — com perfil de LED na parte '
   'superior.'),
  ('Guarda-roupa', '200 × 200 × 70 prof — quatro portas, oito gavetas, '
   'maleiro, varão cromado e prateleiras.'),
  ('Gavetas com centro em palhinha', 'quatro de 50 × 45, com rodízio embutido '
   '— palhinha natural aplicada na frente.'),
  ('Nichos porta-livros', 'três de 60 × 15, frente em palhinha natural.'),
  ('Cômoda', '150 × 50 × 50 prof — três gavetas e dois nichos com LED.'),
  ('Móvel de estudo', '215 × 80 × 55 prof — portas com centro em palhinha, '
   'duas básculas e nichos com LED.'),
  ('Trocador', '70 × 95 × 55 prof — uma porta e três gavetas.'),
  ('Escrivaninha com regulagem de altura', '160 × 75 × 55 prof — a regulagem '
   'é executada em marcenaria, não por mecanismo comprado. Acompanha móvel '
   'suspenso.'),
 ]),
 ('Suíte do casal', '', [
  ('Armário com portas de correr', '208 × 221 × 66 prof — duas folhas de '
   'correr em estrutura com vidro refletente. Maleiro, varão, nichos, '
   'sapateiras e quatro gavetas.'),
  ('Quadro da cabeceira estofada', '308 × 120 — a marcenaria executa o quadro; '
   'o revestimento é do estofador e está no valor.'),
  ('Nichos em MDF madeirado', '249 × 45, prof 20 — com LED.'),
  ('Painel de nichos e prateleiras', '307 × 204 — estrutura madeirada com seis '
   'portas.'),
  ('Prateleiras superiores', 'duas de 2,21 m, prof 18.'),
 ]),
 ('Suíte 02', '', [
  ('Painel de cabeceira', '271 × 45 — com recuo para a descida da cortina.'),
  ('Criado-mudo', '45 × 45 × 45 prof — três gavetas, cava central.'),
  ('Prateleira superior', '2,71 m, prof 20.'),
 ]),
 ('Home office', '3,46 m de parede', [
  ('Bancada e rodobanca', '346 × 70 prof — em MDF madeirado, com fita de LED '
   'na parte superior da rodobanca.'),
  ('Armário inferior da bancada', '346 × 70 × 45 prof — quatro portas e quatro '
   'gavetas, cava no mesmo material.'),
  ('Armário 01', '200 × 200 × 45 prof — estrutura madeirada, frentes em tom '
   'contrastante, seis portas e quatro gavetas.'),
  ('Armário 02', '200 × 200 × 45 prof — prateleiras internas prof 41, quatro '
   'portas e quatro gavetas.'),
  ('Prateleiras', 'dezenove peças em quatro modelos, prof 20.'),
  ('Gaveteiro móvel', '45 × 50 × 45 prof — quatro gavetas sobre rodízio.'),
 ]),
 ('Banho da suíte', '', [
  ('Armário suspenso', '196 × 35 × 35 prof — quatro portas de abrir em espelho '
   'prata, com fita de LED na parte inferior.'),
  ('Armário inferior', '215 × 85 × 45 prof — quatro gavetas, dois gavetões e '
   'duas básculas de roupa suja.'),
 ]),
 ('Área de serviço', '', [
  ('Armário superior', '326 × 73 × 35 prof — cinco portas e prateleiras.'),
  ('Armário inferior', '326 × 85 × 60 prof — quatro portas, três gavetões e '
   'três cestos de roupa suja.'),
 ]),
 ('Despensa', '', [
  ('Armários', '293,5 × 173 × 40 prof — seis portas, prateleiras e vão livre '
   'para escada e vassouras.'),
 ]),
]

# ── investimento por ambiente · valores de corte-a4d.py ────────────────────
INV = [
 ('Cozinha',                          15500,  18500,  20500),
 ('Sala e home theater',              18000,  20500,  22500),
 ('Espaço kids',                      19500,  21500,  23000),
 ('Quarto infantil',                  25500,  30000,  34500),
 ('Suíte do casal',                   22000,  24500,  27000),
 ('Suíte 02',                          1500,   1500,   2000),
 ('Home office',                       19500,  23000,  26500),
 ('Banho da suíte',                    6500,   8500,  10000),
 ('Área de serviço',                   7000,   8500,   9500),
 ('Despensa',                          5500,   6000,   6500),
 ('Iluminação em LED embutida — 21 m', 2000,   3000,   3000),
]
TOT = [sum(i[k] for i in INV) for k in (1, 2, 3)]
assert TOT == [142500, 165500, 185000], TOT

PAGTO = [
    ('Entrada de 30% + saldo em até 10× no cartão', '—'),
    ('Entrada de 50% + saldo em até 8× no cartão',  '3%'),
    ('Entrada de 70% + saldo em até 6× no cartão',  '5%'),
    ('Entrada de 70% + saldo por transferência',    '7%'),
]

FORA = [
    ('Pedras e marmoraria', 'O projeto especifica Taj Mahal acetinado, Bege '
     'Bahia levigado, Branco Siena polido, granito preto e travertino. Nenhuma '
     'delas está neste valor — pedra é fornecimento de marmoraria.'),
    ('Sóculos em alvenaria', 'Os sóculos revestidos em pedra, com instalação em '
     'meia-esquadria, são obra civil.'),
    ('Eletrodomésticos, louças e metais', 'Prevemos o vão e a usinagem; o '
     'aparelho é do cliente. Precisamos das medidas de fábrica antes do corte.'),
    ('Alvenaria, gesso, revestimento e pintura', 'Inclusive a pintura da parede '
     'de fundo do home office.'),
    ('Elétrica e hidráulica', 'A iluminação embutida NA marcenaria é nossa; os '
     'pontos de energia e de água são da obra.'),
    ('Móveis soltos e persianas', 'Camas, poltronas, mesas e cortinas.'),
]

# CSS versionado no repo — não depender de /tmp, que some a cada sessão
CSS = open('projetos/css-proposta.css', encoding='utf-8').read()

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 8
def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria · {CLIENTE}</span>'
            f'<span>{OBRA}</span><span>{n} / {NP}</span></div>')

def bloco(amb, sub, itens):
    h = (f'<div style="margin-top:5.5mm"><div class="eyebrow">{amb}'
         + (f' &nbsp;·&nbsp; {sub}' if sub else '') + '</div>'
         '<div class="rule" style="margin:5px 0 3mm"></div>')
    for t, d in itens:
        h += (f'<div class="it" style="padding:2.2mm 0"><div>'
              f'<span class="it-t" style="font-size:9.8pt">{t}</span>'
              f'<span class="it-d" style="display:inline;margin-left:5px">'
              f'{d}</span></div></div>')
    return h + '</div>'

p1 = f"""<div class="page cover"><div class="pad">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div style="margin-top:auto">
    <div class="eyebrow">Proposta de marcenaria planejada</div>
    <div class="rule"></div>
    <div class="cv-t">Quarenta e um<br>móveis planejados</div>
    <div class="cv-s">{CLIENTE}</div>
  </div>
  <div class="cv-meta">
    <div><div class="k">Ambientes</div><div class="v">Dez</div></div>
    <div><div class="k">Data</div><div class="v">{DATA}</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
  </div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">O que está sendo proposto</div>
  <div class="rule"></div>
  <h2 class="h-sec">A casa inteira,<br>móvel por móvel.</h2>
  <p class="lead" style="margin-top:4mm">Levantamento feito sobre o projeto de
  interiores — as pranchas de layout, elevação e detalhamento de cada ambiente.
  São <strong>286 m² de chapa</strong> em MDF melamínico, com o interior dos
  móveis no mesmo acabamento da frente.</p>
  {bloco(*ESCOPO[0])}
  {bloco(*ESCOPO[1])}
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  {bloco(*ESCOPO[2])}
  {bloco(*ESCOPO[3])}
  <div class="box" style="margin-top:5mm"><div class="t">Sobre as básculas da cozinha</div>
  <p>O projeto abre duas possibilidades para as portas basculantes do armário
  suspenso: MDF ou vidro laqueado. <strong>Esta proposta considera MDF.</strong>
  O vidro laqueado é fornecimento de terceiro e altera o valor.</p></div>
  {foot(3)}
</div></div>"""

p4 = f"""<div class="page"><div class="pad">
  {bloco(*ESCOPO[4])}
  {bloco(*ESCOPO[5])}
  {bloco(*ESCOPO[6])}
  {foot(4)}
</div></div>"""

p5 = f"""<div class="page"><div class="pad">
  {bloco(*ESCOPO[7])}
  {bloco(*ESCOPO[8])}
  {bloco(*ESCOPO[9])}
  <div class="box" style="margin-top:6mm"><div class="t">O que atravessa a casa toda</div>
  <p><strong>Palhinha natural</strong> nas frentes de gaveta, nos porta-livros e
  nas portas do móvel de estudo do quarto infantil — aplicada sobre quadro de
  marcenaria. <strong>Iluminação em LED</strong> em perfil de alumínio, embutida
  na marcenaria, em vinte e um metros distribuídos entre cozinha, sala, quarto
  infantil, suíte, home office e banho. E <strong>puxador em cava usinada</strong>
  no próprio material, em praticamente todas as frentes: sem puxador aparente,
  o desenho fica limpo.</p></div>
  {foot(5)}
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

p6 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Três configurações</div>
  <div class="rule"></div>
  <h2 class="h-sec">O que muda entre elas<br>é o movimento.</h2>
  <p class="lead" style="margin-top:4mm">O desenho, a chapa, o acabamento e o
  esquadro são <strong>os mesmos nas três</strong>. O que separa uma da outra é
  a ferragem — e ferragem se mede em ciclo de abertura, amortecimento e
  regulagem. São <strong>164 dobradiças e 68 gavetas</strong> nesta casa: é
  muita coisa abrindo e fechando todo dia.</p>
  <div style="margin-top:5mm">{cen_html}</div>
  <div class="box"><div class="t">Uma observação honesta</div>
  <p>A garantia acima é <strong>garantia Valvic</strong> — nossa, escrita e
  assinada na entrega. Não é a garantia do fabricante da ferragem, que não faz
  parte do que a gente vende.</p></div>
  {foot(6)}
</div></div>"""

linhas = ''.join(
    f'<tr><td class="l">{t}</td><td>{brl(a)}</td>'
    f'<td class="hi">{brl(b)}</td><td>{brl(c)}</td></tr>'
    for t, a, b, c in INV)

p7 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Investimento</div>
  <div class="rule"></div>
  <h2 class="h-sec">Ambiente a ambiente,<br>nas três linhas.</h2>
  <table class="inv" style="margin-top:5mm">
    <tr><th class="l">Ambiente</th><th>I · Essencial</th>
        <th class="hi">II · Intermediária</th><th>III · Superior</th></tr>
    {linhas}
    <tr class="tot"><td class="l">Investimento total</td>
      <td>{brl(TOT[0])}</td><td class="hi">{brl(TOT[1])}</td>
      <td>{brl(TOT[2])}</td></tr>
  </table>
  <div class="box"><div class="t">O que está dentro do valor</div>
  <p>Projeto executivo de marcenaria, fornecimento de material, produção em CNC
  e coladeira automática próprias, transporte, entrega na obra e
  <strong>instalação e montagem por equipe própria da Valvic</strong> — não
  terceirizamos a montagem.</p></div>
  <div class="box" style="border-left-color:var(--mut)">
  <div class="t" style="color:var(--mut)">Duas definições ainda em aberto</div>
  <p><strong>Quais ambientes entram no contrato</strong> — se algum sair, o
  conjunto é recalculado, porque o custo de produção se redistribui entre os que
  ficam. E a <strong>linha e a cor da chapa</strong>: o valor considera MDF
  melamínico de cor padrão.</p></div>
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
        <div class="s">Contados da liberação da frente de trabalho na obra e da
        aprovação do projeto executivo de marcenaria.</div></div>
      <div class="term"><div class="k">Garantia</div>
        <div class="v">2, 5 ou 10 anos — conforme a linha escolhida</div>
        <div class="s">Garantia Valvic, documentada e assinada na entrega.
        Retorno em 24 h e visita técnica em até 3 dias úteis, sem custo dentro
        do prazo.</div></div>
      <div class="term"><div class="k">Validade desta proposta</div>
        <div class="v">{VALIDADE}</div></div>
      <div class="term"><div class="k">Produção e montagem</div>
        <div class="v">Fábrica e equipe próprias, do corte à instalação</div>
        <div class="s">Corte, usinagem da cava e laminação de borda na nossa CNC
        e coladeira automática; instalação e montagem pela nossa equipe. Não
        terceirizamos nem o que define o acabamento, nem quem entrega.</div></div>
      <table class="pay" style="margin-top:5mm">
        <tr><td colspan="2" style="border:none;padding-bottom:1mm">
          <span class="eyebrow">Formas de pagamento</span></td></tr>
        {''.join(f'<tr><td>{c}</td><td class="d">{d}</td></tr>' for c, d in PAGTO)}
      </table>
      <p style="color:var(--mut);font-size:7.9pt;margin-top:2.5mm">
      O desconto por transferência devolve ao cliente a taxa de máquina que
      deixamos de pagar.</p>
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

HTML = (f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        f'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>'
        f'{p1}{p2}{p3}{p4}{p5}{p6}{p7}{p8}</body></html>')

OUT_H, OUT_P = 'projetos/proposta-luciana.html', 'projetos/proposta-luciana.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML)
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}')
print('Total: ' + ' · '.join(brl(t) for t in TOT))
