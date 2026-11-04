# -*- coding: utf-8 -*-
"""ARTHUR & YASMIM — relação de portas para cotação  [14/10/2026]

⭐ [Jonathan 13/10] "nós adquirimos a porta pronta · me dê a relação das
   portas com as especificações para que eu faça a cotação com o fornecedor"

⛔ Documento de COMPRA, não proposta: aqui MEDIDA É O ASSUNTO. A regra de
   não pôr metragem vale para o que vai ao cliente, não para o que vai ao
   fornecedor — sem cota ele não cota.
"""
import pathlib, subprocess, os

P = pathlib.Path(__file__).resolve().parent
NP = 1
CSS = open(P/'css-proposta.css', encoding='utf-8').read() + """
.topAY{display:flex;justify-content:space-between;align-items:baseline;gap:8mm;
  padding-bottom:4mm;border-bottom:1px solid var(--hair);flex:none;}
.topAY .b{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;
  font-weight:700;}
.topAY .m{font-size:7.2pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;text-align:right;}
table.ayT{width:100%;border-collapse:collapse;margin-top:3mm;font-size:8.6pt;
  flex:none;}
table.ayT th{font-size:6.8pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--mut);font-weight:700;text-align:left;padding:0 3mm 2mm 0;
  border-bottom:1.2px solid var(--gold);}
table.ayT td{padding:2mm 3mm 2mm 0;border-bottom:1px solid var(--hair);
  vertical-align:top;}
table.ayT td.k{font-weight:600;width:42mm;}
table.ayT td.r,table.ayT th.r{text-align:right;}
.hAY{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;margin-top:5.5mm;flex:none;}
.pAY{color:var(--soft);font-size:8.6pt;line-height:1.55;margin-top:1.6mm;
  flex:none;}
.pAY b{color:var(--ink);font-weight:600;}
ol.ayL{margin:1.6mm 0 0;padding-left:5mm;color:var(--soft);font-size:8.5pt;
  line-height:1.5;flex:none;}
ol.ayL li{margin-bottom:1.4mm;}
ol.ayL b{color:var(--ink);font-weight:600;}
.boxAY{margin-top:4mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:8.2pt;color:var(--soft);line-height:1.5;flex:none;}
.boxAY b{color:var(--ink);}
"""

LINHAS = [
 ('Porta de vidro <b>reflecta bronze</b>', '52,5 × 250', '105 · duas folhas',
  'ver quadro abaixo'),
 ('Porta de <b>espelho prata</b> · sapateira', '56 × 250', '112 · duas folhas',
  '2 folhas'),
]
VERS = [('1 · mista', '5 folhas'), ('2 · como o projeto', '16 folhas'),
        ('3 · toda em MDF', 'nenhuma')]

tab = ''.join(f'<tr><td class="k">{a}</td><td>{b}</td><td>{c}</td>'
              f'<td class="r">{d}</td></tr>' for a, b, c, d in LINHAS)
ver = ''.join(f'<tr><td class="k">Versão {a}</td><td colspan="2"></td>'
              f'<td class="r">{b}</td></tr>' for a, b in VERS)

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="page"><div class="pad">
  <div class="topAY">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Relação de portas para cotação<br>Closet Arthur &amp; Yasmim · 14/10/2026</div>
  </div>

  <div style="margin-top:5mm;" class="eyebrow">Pedido de cotação</div>
  <div class="h-sec serif" style="font-size:21pt;">Portas prontas em perfil<br>
    de alumínio com vidro.</div>
  <div class="rule"></div>
  <div class="pAY">Fornecimento de <b>portas prontas</b> — perfil, vidro,
  dobradiça e puxador — para instalação em marcenaria nossa.</div>

  <table class="ayT">
    <thead><tr><th>Item</th><th>Folha (cm)</th><th>Vão (cm)</th>
      <th class="r">Quantidade</th></tr></thead>
    <tbody>{tab}{ver}</tbody>
  </table>
  <div class="pAY"><b>A cliente pediu orçamento de três formas</b> e cada uma
  compra uma quantidade diferente de porta de vidro. Precisamos do
  <b>preço unitário nas duas quantidades</b> — 5 folhas e 16 folhas —
  porque dificilmente serão o mesmo preço. Na hipótese cheia são
  <b>18 folhas</b> no total.</div>

  <div class="hAY">Especificação comum</div>
  <div class="pAY">
  Perfil de alumínio, acabamento <b>preto/grafite fosco</b>, com
  <b>puxador vertical integrado ao perfil</b> — não há puxador aplicado no
  projeto. <b>Abertura de giro</b>, três dobradiças por folha, com
  amortecimento. Vedação, contra-vidro e escovinha conforme a linha.
  Fixação em lateral de MDF de 18 mm.</div>

  <div class="hAY">O que precisamos que responda</div>
  <ol class="ayL">
    <li><b>Altura máxima de folha da linha.</b> 250 cm com 52,5 de largura
      é folha alta e estreita; se precisar de <b>travessa intermediária</b>,
      muda o desenho e a cliente aprova antes.</li>
    <li><b>Preço unitário para 5 folhas e para 16 folhas</b>, separadamente
      — e também <b>por m²</b>, para recalcularmos sem nova cotação.</li>
    <li><b>O que está no preço</b>: vidro, perfil, dobradiça, puxador,
      vedação, instalação. E o que não está.</li>
    <li><b>Espessura do vidro</b> nessa altura — 4 ou 6 mm. Em 6 mm o peso
      sobe cerca de 50% e muda a nossa fixação.</li>
    <li><b>Peso por folha</b>, para dimensionarmos a lateral.</li>
    <li><b>Prazo</b> a partir do pedido, e se mede no local.</li>
    <li><b>Tolerância de medida</b> e em que momento precisa da medida
      final — antes ou depois da nossa caixa montada.</li>
    <li>Se o <b>espelho sai no mesmo perfil</b> e no mesmo prazo. E, por
      comparação, quanto sairia a <b>folha única de 112</b> no lugar das
      duas de 56.</li>
    <li><b>Garantia</b> do conjunto, e o que acontece com uma folha
      trincada depois de instalada.</li>
  </ol>

  <div class="boxAY"><b>Observação.</b> A modulação do closet ainda não está
  fechada: o caderno numera dez módulos mas não traz a página de cada um.
  Esta relação usa o <b>módulo tipo de 105 com duas folhas</b>, o único
  cotado na prancha. Se houver módulo de outra largura, a quantidade muda —
  por isso o preço <b>por folha e por m²</b>. As portas em MDF não entram
  nesta cotação: essas são de fabricação nossa.</div>

  <div class="foot"><span>Valvic Marcenaria</span>
    <span>Arthur &amp; Yasmim · closet</span><span>1 / {NP}</span></div>
</div></div></body></html>"""

(P/'relacao-portas-arthur-yasmim.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'relacao-portas-arthur-yasmim.pdf')],
               check=True, env=env)
print('relacao-portas-arthur-yasmim.pdf · 1 página')
