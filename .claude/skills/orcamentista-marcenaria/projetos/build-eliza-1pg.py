# -*- coding: utf-8 -*-
"""ELIZA E LUIZ GUSTAVO — proposta de UMA PÁGINA  [29/10/2026]

⭐ [Jonathan 29/10] "faça uma proposta sintetizando em uma pagina o projeto
   da brinquedoteca e esse banco considerando as corrediças ocultas da
   hettich e o estofado. considere um desconto de 10% para pagamento a
   vista."
⛔ A cozinha de brinquedo SAI: o cliente tirou do escopo.

Os números não são novos. A brinquedoteca vem de `orcamento-brinquedoteca-v2.py`
(preços DECLARADOS, não rateados) e o banco vem da proposta que já foi ao
cliente — canto alemão na coluna OCULTA, R$ 23.000, mais o estofado R$ 6.500.
"""
import pathlib, base64, subprocess, os

P = pathlib.Path(__file__).resolve().parent
CSS = (P/'css-brinquedoteca.css').read_text()
br = lambda v: f'{v:,.0f}'.replace(',', '.')

def uri(p):
    return 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()

HERO = uri(P/'img-brinquedoteca'/'capa.jpg')
BANCO = uri(pathlib.Path('/tmp/elz/sal-001-009.jpg'))

# ⭐ os doze itens da v2 agrupados em cinco conjuntos legíveis — a soma é a
#   mesma, item a item, e nenhum preço foi recalculado
BRINQ = [
 ('Estrutura e paredes cenográficas',
  'Parede estrutural com efeito tijolinho, paredes da casinha, escada da '
  'casinha e as janelas e pórticos moldurados', 15400+8690+4870+25400),
 ('Circulação e proteção em altura',
  'Passarela suspensa, gradis de contenção das redes e plataformas '
  'acolchoadas', 8190+53370+10190),
 ('Brinquedos',
  'Escorregador com túnel de teto curvo e a estrutura da piscina de espuma',
  18920+15010),
 ('Mobiliário e arremates',
  'Banco extenso e toldo personalizado', 7680+1400),
 ('Pintura acrílica e papel de parede',
  'Mão de obra · ⛔ tinta, massa e papel não estão neste preço', 12500),
]
ESTUDIO = [
 ('Canto alemão em “C”',
  'Estrutura interna e externa em MDF melamínico amadeirado fosco, detalhes '
  'de molduras e puxadores em cava usinada · <b>corrediças ocultas Hettich</b>',
  23000),
 ('Estofado capitonê',
  'Conforme projeto, espuma D33, espessuras conforme projeto', 6500),
]
T_BRINQ = sum(v for _, _, v in BRINQ)
T_EST   = sum(v for _, _, v in ESTUDIO)
TOTAL   = T_BRINQ + T_EST
AVISTA  = round(TOTAL * 0.90)

assert T_BRINQ == 181_620, T_BRINQ      # v2 menos a cozinha de brinquedo
assert T_EST   == 29_500,  T_EST

def bloco(ls):
    return ''.join(
      f'<div class="cj"><div class="n"></div><div><div class="t">{t}</div>'
      f'<div class="d">{d}</div></div><div class="v">R$ {br(v)}</div></div>'
      for t, d, v in ls)

HTML = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}
/* ⭐ uma folha só: tudo encolhe para caber, e nada sai */
.in{{padding:13mm 20mm 9mm;}}
.ttl{{font-size:21pt;margin-top:3.5mm;}}
.cj{{padding:.75mm 0;}}
.cj .t{{font-size:9pt;}}
.cj .d{{font-size:6.9pt;line-height:1.32;}}
.cj .v{{font-size:10pt;}}
.cj.tot{{padding-top:3.4mm;}}
.cj.tot .t{{font-size:10.5pt;}}
.cj.tot .v{{font-size:19pt;}}
.gr{{grid-template-columns:repeat(4,1fr);gap:0 7mm;margin-top:5mm;}}
.gr .v{{font-size:7.9pt;line-height:1.48;margin-top:1.2mm;}}
.gr .k{{font-size:6.2pt;letter-spacing:.24em;}}
.obs{{margin-top:4mm;padding-top:3.5mm;font-size:6.9pt;line-height:1.5;}}
.pe2{{margin-top:4mm;padding-top:4mm;}}
.duo{{display:grid;grid-template-columns:1fr 1fr;gap:0;height:29mm;margin:0 -20mm 3.5mm;}}
.duo .ph{{height:100%;}}
.duo .ph span{{position:absolute;left:0;bottom:0;background:var(--verde);
  color:#DCE5DD;font-size:6.2pt;letter-spacing:.26em;text-transform:uppercase;
  padding:2mm 4mm;}}
.sub2{{font-size:6.4pt;letter-spacing:.28em;text-transform:uppercase;
  color:var(--verde-lt);font-weight:500;margin:4.5mm 0 2mm;}}
.av{{margin-top:4.5mm;background:var(--verde);color:#F4F2EC;padding:4mm 5mm;
  display:flex;align-items:baseline;justify-content:space-between;}}
.av .k{{font-size:6.8pt;letter-spacing:.3em;text-transform:uppercase;color:#A9BFAF;}}
.av .t{{font-size:9pt;color:#C3CFC5;margin-top:1.5mm;}}
.av .v{{font-size:20pt;letter-spacing:-.025em;}}
</style></head><body>

<div class="pg"><div class="in">
  <div class="sel">Proposta · Eliza e Luiz Gustavo</div>
  <h1 class="ttl disp">A brinquedoteca e o<br><em>canto alemão do estúdio.</em></h1>

  <div class="duo">
    <div class="ph"><img src="{HERO}" alt=""><span>Brinquedoteca</span></div>
    <div class="ph"><img src="{BANCO}" alt=""><span>Estúdio · canto alemão</span></div>
  </div>

  <div class="sub2">Brinquedoteca · projeto Helena Antunes</div>
  {bloco(BRINQ)}
  <div class="cj" style="border-top:none"><div class="n"></div>
    <div><div class="t" style="color:var(--mut)">Subtotal</div></div>
    <div class="v" style="font-size:9.6pt;color:var(--mut)">R$ {br(T_BRINQ)}</div></div>

  <div class="sub2">Estúdio de música · salinha</div>
  {bloco(ESTUDIO)}
  <div class="cj" style="border-top:none"><div class="n"></div>
    <div><div class="t" style="color:var(--mut)">Subtotal</div></div>
    <div class="v" style="font-size:9.6pt;color:var(--mut)">R$ {br(T_EST)}</div></div>

  <div class="cj tot"><div class="n"></div>
    <div><div class="t">Investimento</div>
      <div class="d">Os dois escopos, num só contrato e numa só data</div></div>
    <div class="v">R$ {br(TOTAL)}</div></div>

  <div class="av">
    <div><div class="k">À vista · 10% de desconto</div>
      <div class="t">Pagamento integral por transferência, na assinatura.</div></div>
    <div class="v">R$ {br(AVISTA)}</div>
  </div>

  <div class="gr">
    <div><div class="k">Corrediças</div><div class="v">
      <b>Ocultas Hettich</b>, com fechamento suave em slowmotion — não aparecem
      na lateral da gaveta. Garantia de <b>5 anos</b>.</div></div>
    <div><div class="k">Estofado</div><div class="v">
      Capitonê conforme projeto, em <b>espuma D33</b> — a densidade de assento
      de uso intenso, que não achata com o tempo.</div></div>
    <div><div class="k">Entrega</div><div class="v">
      <b>60 dias</b> para o projeto completo, contados do aceite e da
      medição técnica.</div></div>
    <div><div class="k">Outras condições</div><div class="v">
      Entrada de 30% + 10× no cartão · 50% + 8× (−3%) · 70% + 6× (−5%) ·
      70% + transferência (−7%).</div></div>
  </div>

  <div class="obs"><b>Fora desta proposta:</b> a <b>cozinha de brinquedo</b>,
  retirada a pedido do cliente · tinta, massa e papel de parede, que são
  fornecimento da contratante — nossa é a mão de obra de aplicação.
  As paredes saem em <b>MDF ultra premium cru</b>, seladas e lixadas, prontas
  para pintura; ⛔ a garantia não cobre patologia causada por pintura de
  terceiro. O <b>projeto estrutural com ART</b> da passarela, do gradil e das
  plataformas está incluso.</div>

  <div class="pe2"><span>Valvic Marcenaria</span>
    <span>Eliza e Luiz Gustavo · 29 de outubro de 2026</span></div>
</div></div>
</body></html>'''

(P/'proposta-eliza-1pg.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-eliza-1pg.pdf')], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
print(f'  {"BRINQUEDOTECA":<38}{br(T_BRINQ):>10}')
for t, _, v in BRINQ: print(f'    {t:<36}{br(v):>10}')
print(f'  {"ESTÚDIO":<38}{br(T_EST):>10}')
for t, _, v in ESTUDIO: print(f'    {t:<36}{br(v):>10}')
print(f'  {"TOTAL":<38}{br(TOTAL):>10}')
print(f'  {"À VISTA (−10%)":<38}{br(AVISTA):>10}')
