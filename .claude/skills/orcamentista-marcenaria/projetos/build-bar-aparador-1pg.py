# -*- coding: utf-8 -*-
"""BAR / APARADOR — proposta de UMA PÁGINA  [11/11/2026]

⭐ [Jonathan, 11/11/2026] "monte uma proposta simples de uma página com margem de 40%
   e com comissão de arquiteta · entrega em até 90 dias corridos · pagamento 50%
   entrada + 50% entrega". Desenho técnico e render enviados na conversa.
⭐ Conta rápida: custo direto ≈ R$ 2.470 · BASE 76,09% (NF 5%, erro 2%, RT 10%) ·
   MC 40% → R$ 6.846.
⚠ O nome do cliente não veio: a folha sai sem nome até o Jonathan informar.
⚠ Profundidade de 11 cm (por dentro ≈ 8): garrafa em pé pode não caber — confirmar.
"""
import pathlib, subprocess, os, re, html

P = pathlib.Path(__file__).resolve().parent
R = P / 'bar-aparador'
R.mkdir(exist_ok=True)
br = lambda v: f'{v:,.0f}'.replace(',', '.')
br2 = lambda v: f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
E = lambda t: html.escape(str(t))

CLIENTE, ARQ, DATA = 'Bar e aparador', '', 'Novembro de 2026'
TOTAL = 6846.0
PAGTO = [('Na assinatura do contrato', 0.50), ('Na entrega', 0.50)]
PRAZO, VALIDADE = '90 dias corridos', '7 dias úteis'
assert abs(sum(p for _, p in PAGTO) - 1) < 1e-9

CSS = (P / 'css-proposta.css').read_text(encoding='utf-8') + """
.topU{display:flex;justify-content:space-between;align-items:baseline;gap:8mm;
  padding-bottom:4.5mm;border-bottom:1px solid var(--hair);flex:none;}
.topU .b{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;font-weight:700;
  letter-spacing:.02em;}
.topU .m{font-size:7.2pt;letter-spacing:.17em;text-transform:uppercase;color:var(--mut);
  font-weight:700;text-align:right;}
.leadU{color:var(--soft);font-size:9.4pt;line-height:1.58;flex:none;max-width:164mm;}
.leadU b{color:var(--ink);font-weight:600;}
.itU{display:grid;grid-template-columns:1fr 1fr;gap:7mm;margin-top:6mm;flex:none;}
.itU .c{border-top:1.5px solid var(--gold-lt);padding-top:3.6mm;}
.itU .n{font-family:'Cormorant Garamond',Georgia,serif;font-size:13pt;color:var(--gold);
  font-weight:600;line-height:1;}
.itU .t{font-size:10.6pt;font-weight:700;margin-top:1.6mm;color:var(--ink);}
.itU .d{font-size:8.6pt;color:var(--soft);line-height:1.55;margin-top:1.6mm;}
.itU .d b{color:var(--ink);font-weight:600;}
.feU{margin-top:6mm;padding:4mm 0;border-top:1px solid var(--hair);
  border-bottom:1px solid var(--hair);display:grid;grid-template-columns:repeat(3,1fr);
  gap:6mm;flex:none;}
.feU .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);
  font-weight:700;}
.feU .d{font-size:8.4pt;color:var(--soft);line-height:1.5;margin-top:1.2mm;}
.feU .d b{color:var(--ink);font-weight:600;}
.ofU{margin-top:6mm;border:1.5px solid var(--gold);border-radius:6px;
  background:rgba(201,169,106,.07);padding:5.6mm 6mm;flex:none;}
.ofU .k{font-size:7.2pt;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);
  font-weight:700;}
.ofU .tot{font-family:'Cormorant Garamond',Georgia,serif;font-size:32pt;font-weight:700;
  line-height:1;margin-top:1.6mm;}
.ofU .sp{height:1px;background:var(--gold-lt);opacity:.55;margin:4.6mm 0 4mm;}
.ofU .duo{display:flex;gap:7mm;align-items:center;}
.ofU .duo > div{flex:1;}
.ofU .duo .x{flex:none;font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  color:var(--gold);font-weight:700;}
.ofU .duo small{display:block;font-size:7.2pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.ofU .duo b{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;
  font-weight:700;line-height:1.05;margin-top:1.3mm;}
.ofU .duo em{display:block;font-style:normal;font-size:8.1pt;color:var(--soft);margin-top:1mm;}
.cndU{display:grid;grid-template-columns:repeat(2,1fr);gap:6mm;margin-top:5.5mm;flex:none;}
.cndU .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);
  font-weight:700;}
.cndU .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;font-weight:700;
  margin-top:1.2mm;line-height:1.1;}
.cndU .d{color:var(--soft);font-size:8.1pt;margin-top:1mm;line-height:1.46;}
.notaU{margin-top:5.5mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:7.9pt;color:var(--soft);line-height:1.5;flex:none;}
.notaU b{color:var(--ink);}
.sigU{display:grid;grid-template-columns:1fr 1fr;gap:12mm;margin-top:auto;padding-top:12mm;flex:none;}
.sigU .ln{border-top:1px solid var(--ink);padding-top:2mm;font-size:7.6pt;color:var(--soft);}
"""

duo = '<div class="x">+</div>'.join(
    f'<div><small>{E(r)} · {p*100:.0f}%</small><b>R$ {br2(TOTAL*p)}</b></div>' for r, p in PAGTO)

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Proposta · {E(CLIENTE)}</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="page"><div class="pad">

  <div class="topU">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta de marcenaria<br>{E(CLIENTE)} · {E(DATA)}</div>
  </div>

  <div style="margin-top:8mm;" class="eyebrow">Sala de jantar · bar</div>
  <div class="h-sec serif" style="font-size:27pt;">O bar entre as pilastras,<br>
    <em>em madeira, de piso a teto.</em></div>
  <div class="rule"></div>

  <div class="leadU">Esta é a proposta para a marcenaria do bar e aparador da sala de jantar: as
    duas pilastras em madeira que emolduram a parede e o armário entre elas, onde ficam as
    garrafas. Do corte à instalação, com <b>equipe própria</b> e medida conferida no local antes
    de qualquer corte.</div>

  <div class="itU">
    <div class="c"><div class="n">01</div><div class="t">Pilastras laterais</div>
      <div class="d">Duas pilastras do piso ao teto, em <b>MDF amadeirado</b>, com frente e
      laterais no mesmo padrão: emolduram a parede e fazem a moldura do bar.</div></div>
    <div class="c"><div class="n">02</div><div class="t">Armário central</div>
      <div class="d">Entre as pilastras, com <b>portas de giro</b> e uma prateleira interna em
      toda a largura, pensado para as garrafas. Sem fundo de madeira: o fundo é a própria
      parede.</div></div>
  </div>

  <div class="feU">
    <div><div class="k">Portas</div><div class="d"><b>Dobradiças com amortecimento</b>: a porta
      fecha suave, sem bater.</div></div>
    <div><div class="k">Puxadores</div><div class="d"><b>Cava usinada</b> na própria porta:
      nenhuma peça saltada na frente.</div></div>
    <div><div class="k">Projeto</div><div class="d">O executivo de marcenaria é nosso e é
      aprovado por vocês e pela arquiteta <b>antes do corte</b>.</div></div>
  </div>

  <div class="ofU">
    <div class="k">O investimento</div>
    <div class="tot">R$ {br2(TOTAL)}</div>
    <div class="sp"></div>
    <div class="duo">{duo}</div>
  </div>

  <div class="cndU">
    <div><div class="k">Entrega</div><div class="v">{E(PRAZO)}</div>
      <div class="d">Contados da medição técnica no local, que tem data própria no
      cronograma.</div></div>
    <div><div class="k">Validade</div><div class="v">{E(VALIDADE)}</div>
      <div class="d">A partir desta data.</div></div>
  </div>

  <div class="notaU"><b>Não inclusos:</b> pedra, revestimento da parede, spots e iluminação do
  forro, elétrica, quadros e objetos de decoração.</div>

  <div class="sigU"><div class="ln">Cliente</div>
    <div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>

  <div class="foot"><span>Valvic Marcenaria</span><span>{E(CLIENTE)} · proposta</span>
    <span>{E(DATA)}</span></div>
</div></div>
</body></html>"""

# ── as travas ───────────────────────────────────────────────────────────
_t = re.sub(r'<[^>]+>', ' ', HTML.split('<body>')[1])
for _c in ('Alexandre', 'Gisele', 'Ionah', 'Haverson', 'Ana Carolina', 'Gustavo', 'Phillip', 'Attos', 'Luiza Pacheco', 'Michell'):
    assert _c not in _t, f'⛔ vestígio de outro cliente: {_c}'
assert not [c for c in '⭐⛔⚠' if c in _t], '⛔ marcação interna'
assert not re.search(r'\d+\s*(cm|mm|m²)', _t), '⛔ medida na folha'
# [Jonathan, 09/11/2026] "tire apenas o bloco sobre garantia"
assert 'garantia' not in _t.lower(), '⛔ o bloco de garantia saiu da folha'
for _p in ('cartão', 'desconto', 'margem'):
    assert _p not in _t.lower(), _p

OUT = R / 'proposta-bar-aparador.html'
OUT.write_text(HTML, encoding='utf-8')
PDF = R / 'proposta-bar-aparador.pdf'
subprocess.run(['node', str(P / 'render-pdf.js'), str(OUT), str(PDF)], check=True,
               env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
pg = subprocess.run(['pdfinfo', str(PDF)], capture_output=True, text=True).stdout
npg = int(re.search(r'Pages:\s+(\d+)', pg).group(1))
assert npg == 1, f'⛔ a proposta tem de caber em UMA página: saiu com {npg}'
print(f'{PDF.name} · 1 página · R$ {br2(TOTAL)} · ' + ' + '.join(f'R$ {br2(TOTAL*p)}' for _, p in PAGTO))
