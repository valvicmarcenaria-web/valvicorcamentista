# -*- coding: utf-8 -*-
"""APARTAMENTO JPC — a proposta de UMA PÁGINA.

⭐ [Jonathan, 17/11/2026] "Faça esse orçamento em uma página. Bonito e
  organizado / Prazo de entrega 60 dias / Pagamento 50% + 50% / Ferragens
  Hettich / Preço de venda - R$ 6.700".

⭐⭐ OS DOIS DESENHOS SÃO GERADOS DAS MESMAS MEDIDAS QUE O ORÇAMENTO USA,
  não redesenhados à mão. Largura, altura, divisão de porta, altura de
  gaveta e o nicho saem das constantes abaixo, e as constantes são as da
  prancha. ⛔ Desenho que diverge do orçamento é a pior linha de uma
  proposta: o cliente aprova a figura e a fábrica corta a tabela.

⚠ O PREÇO DE CADA BANHO É RATEIO, não orçamento separado. Os R$ 6.700 são
  do projeto; `levantamento.RATEIO` os divide pelo custo direto e o último
  item absorve o centavo, para que a tabela some o preço fechado exato.
"""
import pathlib, subprocess, os, importlib.util, datetime

P = pathlib.Path(__file__).resolve().parent
def _mod(nome, arq):
    sp = importlib.util.spec_from_file_location(nome, P / arq)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
b  = _mod('jpc_base', 'base.py')
lv = _mod('jpc_lv', 'levantamento.py')

CSS = (P.parent / 'css-brinquedoteca.css').read_text()
br = lambda v: f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')

MES = ('janeiro fevereiro março abril maio junho julho agosto setembro '
       'outubro novembro dezembro').split()
_h = datetime.date.today()
#   ⛔ Data de documento é a do dia em que ele foi gerado — nunca literal.
#     Duas propostas na mão do cliente com a mesma data e preços diferentes
#     foi o que custou isso no job da Eliza [30/10/2026].
DATA = f'{_h.day} de {MES[_h.month - 1]} de {_h.year}'

# ════════════════════════════════════════════════════════════════════════
# OS DESENHOS · elevação em SVG, nas cotas da prancha
# ════════════════════════════════════════════════════════════════════════
#   ⭐ Os dois SVG têm a MESMA altura de viewBox e larguras proporcionais à
#     largura real, e as colunas do grid usam essas mesmas proporções. Com
#     isso os dois desenhos saem na MESMA ESCALA na folha, sem que ninguém
#     precise calcular escala nenhuma.
#   ⛔ A COTA DE 63 SAÍA PELA ESQUERDA DO viewBox e o PDF imprimia "3".
#     Margem simétrica não serve: só o lado esquerdo tem cota vertical.
MARG_E, MARG_D = 8.0, 3.0
TOPO, PEDRA, BASE_V = 10.0, 3.5, 10.0
ALT = 63.0
VB_W = lambda larg: larg + MARG_E + MARG_D
VB_H = TOPO + ALT + BASE_V                # 83

FINO, GROSSO, FINISSIMO = 0.22, 0.42, 0.14
TINTA, VERDE, TERRA, MUT, LINHA = '#16211B', '#2C4034', '#B0704E', '#8E8A80', '#D8D4C9'


def _cot_h(x0, x1, y, txt, cor=VERDE):
    """Cota horizontal: dois tiques, uma linha e o número por cima."""
    return (f'<path d="M{x0} {y-1.1}V{y+1.1}M{x1} {y-1.1}V{y+1.1}M{x0} {y}H{x1}" '
            f'stroke="{cor}" stroke-width="{FINISSIMO}" fill="none"/>'
            f'<text x="{(x0+x1)/2}" y="{y-1.8}" font-size="3.7" fill="{cor}" '
            f'text-anchor="middle" font-family="Inter,sans-serif">{txt}</text>')


def _cot_v(y0, y1, x, txt, cor=VERDE):
    return (f'<path d="M{x-1.1} {y0}H{x+1.1}M{x-1.1} {y1}H{x+1.1}M{x} {y0}V{y1}" '
            f'stroke="{cor}" stroke-width="{FINISSIMO}" fill="none"/>'
            f'<text x="{x-1.6}" y="{(y0+y1)/2}" font-size="3.7" fill="{cor}" '
            f'text-anchor="middle" font-family="Inter,sans-serif" '
            f'transform="rotate(-90 {x-1.6} {(y0+y1)/2})">{txt}</text>')


def elevacao(larg, divisoes, gavetas=(), prateleira=False, nicho=None):
    """⭐ `divisoes` são as larguras das colunas, da esquerda para a direita.
    `gavetas` são as alturas da ÚLTIMA coluna, de cima para baixo.
    `nicho` é (largura, altura) do nicho encostado na lateral direita."""
    x0, y0 = MARG_E, TOPO
    x1, y1 = MARG_E + larg, TOPO + ALT
    s = [f'<svg viewBox="0 0 {VB_W(larg)} {VB_H}" '
         f'xmlns="http://www.w3.org/2000/svg">']
    #   a pedra, que NÃO é nossa — em cinza e nomeada, para que a folha
    #   mostre exatamente onde o nosso escopo começa
    s.append(f'<rect x="{x0-1.5}" y="{y0-PEDRA-1}" width="{larg+3}" '
             f'height="{PEDRA}" fill="#EDEAE2" stroke="{MUT}" '
             f'stroke-width="{FINISSIMO}"/>')
    s.append(f'<text x="{x0+larg/2}" y="{y0-PEDRA-2.6}" font-size="2.6" '
             f'fill="{MUT}" font-family="Inter,sans-serif" text-anchor="middle" '
             f'letter-spacing=".35">BANCADA DE PEDRA · FORA DO ESCOPO</text>')
    #   o gabinete
    s.append(f'<rect x="{x0}" y="{y0}" width="{larg}" height="{ALT}" '
             f'fill="#FFFFFF" stroke="{TINTA}" stroke-width="{GROSSO}"/>')
    x = x0
    for i, d in enumerate(divisoes[:-1]):
        x += d
        s.append(f'<path d="M{x} {y0}V{y1}" stroke="{TINTA}" '
                 f'stroke-width="{FINO}"/>')
    if prateleira:
        #   ⭐ ela morre no nicho, como na prancha — o nicho come 15 cm do
        #     compartimento da direita e a prateleira não atravessa o vazio.
        xf = (x1 - nicho[0]) if nicho else x1
        s.append(f'<path d="M{x0} {y0+ALT/2}H{xf}" stroke="{VERDE}" '
                 f'stroke-width="{FINO}" stroke-dasharray="1.6 1.2"/>')
    if gavetas:
        xg = x0 + sum(divisoes[:-1])
        yg = y0
        for h in gavetas[:-1]:
            yg += h
            s.append(f'<path d="M{xg} {yg}H{x1}" stroke="{TINTA}" '
                     f'stroke-width="{FINO}"/>')
    if nicho:
        nw, nh = nicho
        ny = y0 + (ALT - nh) / 2
        s.append(f'<rect x="{x1-nw}" y="{ny}" width="{nw}" '
                 f'height="{nh}" fill="none" stroke="{TERRA}" '
                 f'stroke-width="{FINO}" stroke-dasharray="1.4 1"/>')
        s.append(f'<text x="{x1-0.8}" y="{ny+nh+3.6}" font-size="2.6" '
                 f'fill="{TERRA}" font-family="Inter,sans-serif" '
                 f'text-anchor="end" letter-spacing=".3">'
                 f'PORTA-PAPEL · RECUO {nw:g}</text>')
    s.append(_cot_h(x0, x1, y1 + 7.0, f'{larg:g}'.replace('.', ',')))
    s.append(_cot_v(y0, y1, x0 - 3.4, '63'))
    s.append('</svg>')
    return ''.join(s)


SVG_SUITE  = elevacao(67.5, [33.75, 33.75], prateleira=True, nicho=(15, 18))
SVG_SOCIAL = elevacao(88.5, [29.5, 29.5, 29.5], gavetas=(15, 15, 33))

# ════════════════════════════════════════════════════════════════════════
# A TABELA
# ════════════════════════════════════════════════════════════════════════
ITENS = [
 ('Banho Suíte', 'gabinete suspenso sob bancada',
  'Caixa de <b>67,5 × 63 × 49,5 cm</b>, suspensa 20 cm do piso, em duas portas '
  'de 33,75 com prateleira interna. O <b>porta-papel higiênico</b> fica dentro '
  'da marcenaria: um nicho de 25 × 18 aberto na lateral, recuado 15 cm e '
  'forrado por dentro — nada aparafusado no revestimento.'),
 ('Banho Social', 'gabinete suspenso sob bancada',
  'Caixa de <b>88,5 × 63 × 45 cm</b>, suspensa, em três colunas de 29,5: duas '
  'portas inteiras e uma <b>torre de três gavetas</b> de 15, 15 e 33, sobre '
  'corrediça Hettich de extensão total com fechamento amortecido.'),
]
assert len(ITENS) == len(lv.RATEIO), (len(ITENS), len(lv.RATEIO))

linhas = ''.join(
  f'<div class="cj"><div class="n">{i:02d}</div>'
  f'<div><div class="t">{nome} · <span style="color:var(--mut)">{sub}</span></div>'
  f'<div class="d">{d}</div></div>'
  f'<div class="v">R$ {br(v)}</div></div>'
  for i, ((nome, sub, d), v) in enumerate(zip(ITENS, lv.RATEIO), 1))

ENTRADA = b.PRECO_FECHADO * b.PAGAMENTO[0][1]
SALDO   = b.PRECO_FECHADO * b.PAGAMENTO[1][1]

HTML = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Apartamento JPC · Proposta Valvic</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}
/* ⭐ uma folha só: tudo encolhe para caber, e nada sai */
.in{{padding:12mm 19mm 7mm;}}
.ttl{{font-size:22pt;margin-top:3mm;line-height:1.1;}}
.sub1{{font-size:8.4pt;color:var(--verde-lt);margin-top:3.2mm;}}
.sub1 b{{color:var(--tinta);font-weight:500;}}
/* ⛔ A PRANCHA DE DESENHO COMIA 76 mm DE ALTURA e empurrava o bloco "a
   conferir" para fora da folha — e `.pg` é overflow:hidden, então ele não
   ia para a página 2, ele SUMIA. ⭐ As proporções das colunas são as dos
   viewBox (67,5+11 e 88,5+11): com isso os dois desenhos saem na MESMA
   escala, e o max-width manda na altura dos dois de uma vez. */
.dois{{display:grid;grid-template-columns:78.5fr 99.5fr;gap:0 6mm;
  max-width:136mm;margin:4.5mm auto 0;align-items:end;}}
.dois svg{{width:100%;height:auto;display:block;}}
.leg{{font-size:6.2pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--verde-lt);font-weight:600;margin-top:1.2mm;text-align:center;}}
.cj{{padding:1.9mm 0;grid-template-columns:7mm 1fr auto;}}
.cj .t{{font-size:9.6pt;}}
.cj .d{{font-size:7.2pt;line-height:1.44;margin-top:.9mm;max-width:120mm;}}
.cj .v{{font-size:11.5pt;}}
.tot{{margin-top:4mm;background:var(--verde);color:#F4F2EC;padding:4mm 6mm;
  display:flex;align-items:center;justify-content:space-between;}}
.tot .k{{font-size:6.6pt;letter-spacing:.3em;text-transform:uppercase;
  color:#A9BFAF;font-weight:500;}}
.tot .t{{font-size:9pt;color:#D3DDD5;margin-top:1.6mm;}}
.tot .t b{{color:#fff;font-weight:500;}}
.tot .v{{font-family:'Fraunces',Georgia,serif;font-size:25pt;font-weight:300;
  letter-spacing:-.025em;white-space:nowrap;padding-left:8mm;}}
.gr{{grid-template-columns:repeat(4,1fr);gap:0 6mm;margin-top:5mm;}}
.gr .k{{font-size:6.1pt;letter-spacing:.24em;}}
.gr .v{{font-size:7.2pt;line-height:1.44;margin-top:1.3mm;}}
.fora{{margin-top:4.5mm;padding:4.5mm 5.5mm;}}
.fora .k{{font-size:6.4pt;}}
.lst{{font-size:7.1pt;line-height:1.42;margin-top:2.4mm;}}
.lst li{{margin-bottom:1.1mm;}}
.conf{{margin-top:3.6mm;padding-top:3mm;border-top:1px solid var(--linha);
  font-size:7pt;line-height:1.48;color:var(--mut);}}
.conf b{{color:#4A463E;font-weight:600;}}
.conf .k{{font-size:6.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--verde-lt);font-weight:600;display:block;margin-bottom:1.6mm;}}
.pe2{{margin-top:auto;padding-top:5mm;font-size:6.2pt;}}
</style></head><body>

<div class="pg"><div class="in">
  <div class="sel">Proposta de marcenaria · {b.PROJETO}</div>
  <h1 class="ttl disp">Dois banhos, dois gabinetes —<br>
    <em>e nenhum porta-papel na parede.</em></h1>
  <div class="sub1">Projeto <b>{b.ARQUITETA}</b> · {b.EXECUTIVO}</div>

  <div class="dois">
    <div><div>{SVG_SUITE}</div><div class="leg">Banho Suíte · 67,5 × 63</div></div>
    <div><div>{SVG_SOCIAL}</div><div class="leg">Banho Social · 88,5 × 63</div></div>
  </div>

  {linhas}

  <div class="tot">
    <div><div class="k">Investimento · os dois banhos</div>
      <div class="t"><b>R$ {br(ENTRADA)}</b> na assinatura ·
        <b>R$ {br(SALDO)}</b> na entrega</div></div>
    <div class="v">R$ {br(b.PRECO_FECHADO)}</div>
  </div>

  <div class="gr">
    <div><div class="k">Ferragens</div><div class="v">
      <b>Hettich em todo o escopo.</b> Dobradiça <b>Sensys</b>, 100 mil ciclos
      de ensaio e ajuste 3D; corrediça <b>Quadro V6</b>, 30 kg, com Silent
      System.</div></div>
    <div><div class="k">Entrega</div><div class="v">
      <b>{b.PRAZO_DIAS} dias corridos</b>, contados da assinatura, da entrada e
      da conferência de medidas no local.</div></div>
    <div><div class="k">Garantia</div><div class="v">
      <b>{b.GARANTIA_ANOS} anos</b> sobre marcenaria e ferragem — o prazo da
      linha Hettich, que é a única linha deste projeto.</div></div>
    <div><div class="k">Acabamento</div><div class="v">
      MDF de <b>cor ou amadeirado de catálogo</b>, fita de borda na mesma cor em
      toda face aparente e abertura em <b>cava usinada</b>, sem puxador
      aplicado — como no desenho.</div></div>
  </div>

  <div class="fora"><div class="k">O que não está nesta proposta</div>
  <ul class="lst">
    <li><b>Bancada de pedra e cuba</b> dos dois banhos. Estão desenhadas nas
      pranchas e <b>não são marcenaria</b> — o gabinete é entregue pronto para
      recebê-las.</li>
    <li><b>Espelhos.</b> São colados na parede, não fazem parte do móvel e não
      têm cota em nenhuma das duas folhas. Orçamos à parte, com a medida
      conferida.</li>
    <li><b>Metais, válvulas, sifões, ducha higiênica e box.</b></li>
    <li><b>Alvenaria, elétrica, hidráulica e revestimento</b>, inclusive os
      pontos de fixação na parede.</li>
  </ul></div>

  <div class="conf"><span class="k">A conferir na medição, antes do corte</span>
    <b>A profundidade do gabinete do Banho Social</b> — a prancha não a cota, e
    adotamos <b>45 cm</b>, que é a bancada de 50,5 com o mesmo recuo da suíte ·
    <b>o padrão e a cor do MDF</b>, que as pranchas não especificam: o preço
    acima vale para qualquer cor ou amadeirado de catálogo, e padrões especiais
    — sincronizado, alto-relevo, super matte — têm acréscimo ·
    <b>as prateleiras internas do Banho Social</b>, que o desenho não mostra e
    que incluímos sem acréscimo, se a arquiteta quiser.
  </div>

  <div class="pe2"><span>Valvic Marcenaria</span>
    <span>{b.PROJETO} · {DATA} · proposta válida por {b.VALIDADE_DIAS} dias</span>
  </div>
</div></div>
</body></html>'''

SAIDA = P / 'proposta-jpc.html'
PDF   = P / 'Apartamento JPC · Proposta Valvic.pdf'
SAIDA.write_text(HTML, encoding='utf-8')
subprocess.run(['node', str(P.parent / 'render-pdf.js'), str(SAIDA), str(PDF)],
               check=True, env=dict(os.environ,
                                    NODE_PATH='/opt/node22/lib/node_modules'))
print(f'  {"APARTAMENTO JPC · proposta de uma página":<44}')
for (nome, _s, _d), v in zip(ITENS, lv.RATEIO):
    print(f'    {nome:<42}{"R$ " + br(v):>14}')
print(f'    {"INVESTIMENTO":<42}{"R$ " + br(b.PRECO_FECHADO):>14}')
print(f'    {"custo direto":<42}{"R$ " + br(lv.DIRETO):>14}')
print(f'    {"MC lida":<42}{lv.MC*100:>13.2f}%')
print(f'  → {PDF}')
