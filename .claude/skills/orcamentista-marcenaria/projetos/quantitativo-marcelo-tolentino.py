# -*- coding: utf-8 -*-
"""QUANTITATIVO DE MATERIAL — MARCELO TOLENTINO · BRZ Nova Lima

⛔ DOCUMENTO INTERNO DE PRODUÇÃO E COMPRA. NÃO VAI AO CLIENTE.
   É o oposto da proposta: aqui tudo é cota, m² e contagem de peça.
   Os auditores de metragem NÃO se aplicam a este arquivo.

Sai de `corte-marcelo-tolentino.py`; nada é digitado à mão.
Gera três arquivos:
  · quantitativo-marcelo-tolentino.pdf   — compra e resumo
  · plano-de-corte-marcelo-tolentino.csv — lista de peças para a seccionadora
  · quantitativo-marcelo-tolentino.md    — registro legível
"""
import pathlib, importlib.util, sys, io, contextlib, csv, subprocess, os
from collections import defaultdict

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('mt', P/'corte-marcelo-tolentino.py')
mt = importlib.util.module_from_spec(spec); sys.modules['mt'] = mt
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(mt)

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
br2 = lambda v: f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

# ── fita de borda, separada por família ───────────────────────────────────
fita_fam = defaultdict(float)          # 'branca' | 'cor'
for mov, mat, d, c, l, q in mt.p:
    fam = 'branca' if mat.startswith('BR') else 'cor'
    fita_fam[fam] += (c + l)*2/100*q * (0.55 if mat.startswith('BR') else 0.75)
FITA_COMPRA = {k: v*1.10 for k, v in fita_fam.items()}   # +10% de folga

# ── ferragem consolidada ──────────────────────────────────────────────────
fer_q = defaultdict(float)
for m in mt.MOVS:
    for k, v in mt.FER[m].items(): fer_q[k] += v
FER_NOME = {
    'dobr':   ('Dobradiça',               'un'),
    'corr':   ('Corrediça de gaveta',     'par'),
    'tipon':  ('Pulsador de fecho-toque', 'un'),
    'roup2p': ('Sistema de roupeiro de correr, 2 portas com trilho', 'cj'),
    'sup':    ('Suporte de prateleira',   'cj'),
}
FER_LINHA = {
    'standard': {'dobr':'Hettich Novisys','corr':'Telescópica',
                 'tipon':'Pulsador Blum','roup2p':'RO65 Prime Rometal ★',
                 'sup':'—'},
    'gold':     {'dobr':'Hettich Sensys','corr':'Oculta Quadro (Hettich)',
                 'tipon':'Pulsador Blum','roup2p':'Dominus Rometal',
                 'sup':'—'},
}

# ── terceirizados, por tipo ───────────────────────────────────────────────
TER_ITENS = [
    ('Laca fosca verde',                    'm²', mt.LACA_M2,      None),
    ('Vidro incolor temperado',             'm²', mt.VIDRO_M2,     None),
    ('Vidro canelado',                      'm²', mt.VIDRO_CAN_M2, None),
    ('Vidro bronze',                        'm²', mt.VIDRO_BRZ_M2, None),
    ('Perfil de alumínio (bronze/preto)',   'm',  mt.ALUM_M,       None),
    ('Tubo de alumínio 2×2 preto',          'm',  mt.TUBO_ALU_M,   None),
    ('Estofado em linho',                   'm²', mt.ESTOFADO_M2,  None),
    ('LED COB (fita + perfil)',             'm',  mt.LED_M,        None),
    ('Perfil cava usinado',                 'm',  mt.CAVA_M,       None),
    ('Usinagem do muxarabi',                'm²', mt.USIN_MUX_M2,  None),
    ('Montagem do ripado',                  'm²', mt.RIPADO_M2,    None),
    ('Bite 0,5 × 0,5 nas juntas do pilar',  'm',  mt.BITE_M,       None),
]

# ── CSV · lista de peças para a seccionadora ──────────────────────────────
csv_p = P/'plano-de-corte-marcelo-tolentino.csv'
with open(csv_p, 'w', newline='', encoding='utf-8-sig') as fh:
    w = csv.writer(fh, delimiter=';')
    w.writerow(['AMBIENTE','ITEM','PEÇA','MATERIAL STANDARD','MATERIAL GOLD',
                'COMPR (cm)','LARG (cm)','QTD','ÁREA (m²)','FITA (m)'])
    for mov, mat, d, c, l, q in mt.p:
        pap = mt.papel(mat, d)
        ms  = mt.NOME[mt.mat_cen(mat, pap, 'standard')]
        mg  = mt.NOME[mt.mat_cen(mat, pap, 'gold')]
        fita = (c + l)*2/100*q
        w.writerow([mov.split(' · ')[0], mov.split(' · ')[1], d, ms, mg,
                    f'{c:g}'.replace('.', ','), f'{l:g}'.replace('.', ','), q,
                    br2(c*l*q/10000), br2(fita)])

# ── PDF · quantitativo de compra ──────────────────────────────────────────
CSS = """
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans','Liberation Sans',Arial,sans-serif;
  color:#1A1714;font-size:8.6pt;line-height:1.45;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;
  background:#fff;padding:13mm 15mm 10mm;page-break-after:always;
  display:flex;flex-direction:column;}
.page:last-of-type{page-break-after:avoid;}
h1{margin:0;font-size:17pt;font-weight:700;letter-spacing:-.01em;}
.sub{color:#5C564C;font-size:9pt;margin-top:1.5mm;}
.warn{margin-top:4mm;padding:3mm 4mm;background:#FDF3F0;border-left:3px solid #B4442A;
  font-size:8.2pt;color:#7A2E1C;}
.warn b{color:#5C1F11;}
h2{margin:5.5mm 0 1.6mm;font-size:7.4pt;letter-spacing:.2em;text-transform:uppercase;
  color:#9C7A3C;font-weight:700;}
table{width:100%;border-collapse:collapse;font-size:7.8pt;}
th{text-align:left;font-size:6.8pt;letter-spacing:.12em;text-transform:uppercase;
  color:#918A7C;font-weight:700;padding:0 4px 1.6mm;border-bottom:1px solid #D8D2C6;}
td{padding:0.95mm 4px;border-bottom:1px solid #F0EBE1;vertical-align:top;}
th.r,td.r{text-align:right;}
tr.tot td{border-top:1.2px solid #1A1714;border-bottom:none;font-weight:700;
  padding-top:2mm;}
tr.grp td{background:#FAF7F1;font-weight:700;font-size:7.6pt;
  letter-spacing:.1em;text-transform:uppercase;color:#5C564C;}
.two{display:grid;grid-template-columns:1fr 1fr;gap:8mm;}
.nota{margin-top:3mm;font-size:7.6pt;color:#5C564C;line-height:1.45;}
.nota b{color:#1A1714;}
.foot{margin-top:auto;padding-top:3mm;border-top:1px solid #F0EBE1;
  display:flex;justify-content:space-between;font-size:6.8pt;
  letter-spacing:.14em;text-transform:uppercase;color:#918A7C;}
"""

def tab_chapa(cen):
    r = ''
    for m in sorted(mt.CH[cen], key=lambda k: (k[:2], k)):
        n = mt.CH[cen][m]
        r += (f'<tr><td>{mt.NOME[m]}</td><td class="r">{br2(mt.area[cen][m])}</td>'
              f'<td class="r">{n}</td><td class="r">{mt.area[cen][m]/(n*mt.CH_AREA)*100:.0f}%</td>'
              f'<td class="r">{br(mt.PRECO[m])}</td>'
              f'<td class="r">{br(n*mt.PRECO[m])}</td></tr>')
    tch = sum(mt.CH[cen].values())
    r += (f'<tr class="tot"><td>TOTAL</td><td class="r">{br2(mt.ar_tot)}</td>'
          f'<td class="r">{tch}</td>'
          f'<td class="r">{mt.ar_tot/(tch*mt.CH_AREA)*100:.0f}%</td><td></td>'
          f'<td class="r">{br(mt.custo_chapa[cen])}</td></tr>')
    return r

def tab_fer(cen):
    r, tot = '', 0.0
    for k in ('dobr','corr','tipon','roup2p','sup'):
        if not fer_q[k]: continue
        pu = mt.PRECO_FER[cen][k]; v = fer_q[k]*pu; tot += v
        r += (f'<tr><td>{FER_NOME[k][0]}</td><td>{FER_LINHA[cen][k]}</td>'
              f'<td class="r">{fer_q[k]:.0f}</td><td>{FER_NOME[k][1]}</td>'
              f'<td class="r">{br2(pu)}</td><td class="r">{br(v)}</td></tr>')
    r += (f'<tr class="tot"><td colspan="5">TOTAL</td>'
          f'<td class="r">{br(tot)}</td></tr>')
    return r

ter_rows = ''
for nome, un, pu, _ in TER_ITENS:
    ter_rows += (f'<tr><td>{nome}</td><td>{un}</td>'
                 f'<td class="r">{br2(pu)}</td></tr>')

amb_rows = ''
for fr in ('Stand', 'Decorado'):
    amb_rows += f'<tr class="grp"><td colspan="4">{fr}</td></tr>'
    for am in mt.AMBS:
        if mt.FR_DE[am] != fr: continue
        ch_s = sum(mt.amov['standard'][m][x] for m in mt.amov['standard'] for x in mt.amov['standard'][m] if x.startswith(am)) if False else 0
        amb_rows += (f'<tr><td>{am}</td><td class="r">{br2(mt.AR_AMB[am])}</td>'
                     f'<td class="r">{br(mt.CD_AMB["standard"][am])}</td>'
                     f'<td class="r">{br(mt.CD_AMB["gold"][am])}</td></tr>')
amb_rows += (f'<tr class="tot"><td>TOTAL</td><td class="r">{br2(mt.ar_tot)}</td>'
             f'<td class="r">{br(mt.CD["standard"])}</td>'
             f'<td class="r">{br(mt.CD["gold"])}</td></tr>')

def foot(n, tot):
    return (f'<div class="foot"><span>Valvic · uso interno</span>'
            f'<span>Marcelo Tolentino · BRZ Nova Lima</span>'
            f'<span>{n} / {tot}</span></div>')

pg1 = f"""<div class="page">
  <h1>Quantitativo de material</h1>
  <div class="sub">Marcelo Tolentino · BRZ Nova Lima — estande de vendas e
  apartamento decorado · projeto Zilda Santiago e Anamaria Diniz</div>
  <div class="warn"><b>DOCUMENTO INTERNO DE PRODUÇÃO E COMPRA.</b>
  Não vai ao cliente — a proposta comercial não leva metragem nem
  quantitativo. Gerado de <b>corte-marcelo-tolentino.py</b>; nenhum número
  foi digitado à mão.</div>

  <h2>Chapa · cenário STANDARD <span style="color:#918A7C;font-weight:400;
    letter-spacing:0;text-transform:none;">(estrutura, porta e prateleira em 15 mm)</span></h2>
  <table><thead><tr><th>Material</th><th class="r">m² líquidos</th>
    <th class="r">Chapas</th><th class="r">Aprov.</th>
    <th class="r">R$/chapa</th><th class="r">R$</th></tr></thead>
    <tbody>{tab_chapa('standard')}</tbody></table>

  <h2>Chapa · cenário GOLD <span style="color:#918A7C;font-weight:400;
    letter-spacing:0;text-transform:none;">(porta e prateleira passam a 18 mm)</span></h2>
  <table><thead><tr><th>Material</th><th class="r">m² líquidos</th>
    <th class="r">Chapas</th><th class="r">Aprov.</th>
    <th class="r">R$/chapa</th><th class="r">R$</th></tr></thead>
    <tbody>{tab_chapa('gold')}</tbody></table>

  <div class="nota"><b>Chapa de 2,75 × 1,85 m (5,09 m²).</b> Os m² são
  líquidos de peça; as chapas já saem do plano de corte com o aproveitamento
  real. A porta ripada do salão principal está travada em <b>18 mm nos dois
  cenários</b> — ripa colada numa face só empena a porta de 15.</div>
  {foot(1, 4)}
</div>"""

pg2 = f"""<div class="page">
  <h2 style="margin-top:0;">Fita de borda</h2>
  <table><thead><tr><th>Tipo</th><th class="r">Perímetro útil (m)</th>
    <th class="r">Comprar com 10% (m)</th></tr></thead><tbody>
    <tr><td>Fita branca (peça interna)</td>
      <td class="r">{br2(fita_fam['branca'])}</td>
      <td class="r">{br2(FITA_COMPRA['branca'])}</td></tr>
    <tr><td>Fita de cor (peça aparente)</td>
      <td class="r">{br2(fita_fam['cor'])}</td>
      <td class="r">{br2(FITA_COMPRA['cor'])}</td></tr>
    <tr class="tot"><td>TOTAL</td>
      <td class="r">{br2(sum(fita_fam.values()))}</td>
      <td class="r">{br2(sum(FITA_COMPRA.values()))}</td></tr>
  </tbody></table>
  <div class="nota">O perímetro útil já considera o aproveitamento por
  família (peça interna fita menos faces que peça aparente). A coluna de
  compra acrescenta <b>10% de folga</b> de emenda e perda.</div>

  <h2>Ferragem · cenário STANDARD</h2>
  <table><thead><tr><th>Item</th><th>Linha</th><th class="r">Qtd</th><th>un</th>
    <th class="r">R$ un</th><th class="r">R$</th></tr></thead>
    <tbody>{tab_fer('standard')}</tbody></table>

  <h2>Ferragem · cenário GOLD</h2>
  <table><thead><tr><th>Item</th><th>Linha</th><th class="r">Qtd</th><th>un</th>
    <th class="r">R$ un</th><th class="r">R$</th></tr></thead>
    <tbody>{tab_fer('gold')}</tbody></table>

  <div class="nota">★ <b>RO65 Prime provisório.</b> A base só tem o RO65
  comum; o Prime entrou a R$ 400 o conjunto de duas portas com trilho.
  <b>Cotar antes de comprar.</b><br>
  ⛔ <b>As portas do salão principal abrem ao toque</b>, com pulsador Blum —
  a dobradiça tem de ser a versão <b>SEM MOLA</b>, nos dois cenários. Mola e
  pulsador mecânico brigam e a porta reabre sozinha.</div>
  {foot(2, 4)}
</div>"""

esp_rows = ''
for am in mt.AMBS:
    if mt.ESP_AMB[am] <= 0: continue
    esp_rows += (f'<tr><td>{am}</td>'
                 f'<td class="r">{br2(mt.ESP_AMB[am]/mt.ESPELHO_M2)}</td>'
                 f'<td class="r">{br(mt.ESP_AMB[am])}</td></tr>')
esp_rows += (f'<tr class="tot"><td>TOTAL</td>'
             f'<td class="r">{br2(mt.ESP_TOT/mt.ESPELHO_M2)}</td>'
             f'<td class="r">{br(mt.ESP_TOT)}</td></tr>')

pg3 = f"""<div class="page">
  <h2 style="margin-top:0;">Terceirizados e serviços · preços de referência</h2>
  <table><thead><tr><th>Item</th><th>un</th><th class="r">R$/un</th></tr></thead>
    <tbody>{ter_rows}</tbody></table>
  <div class="nota">O total de terceirizados do projeto é
  <b>R$ {br(sum(mt.TER.values()))}</b>, igual nos dois cenários. A quantidade de cada
  linha sai item a item no CSV do plano de corte.</div>

  <h2>Espelho · linha própria</h2>
  <table><thead><tr><th>Ambiente</th><th class="r">m²</th>
    <th class="r">R$ (a {br(mt.ESPELHO_M2)}/m²)</th></tr></thead>
    <tbody>{esp_rows}</tbody></table>

  {foot(3, 4)}
</div>

<div class="page">
  <h2 style="margin-top:0;">Resumo por ambiente</h2>
  <table><thead><tr><th>Ambiente</th><th class="r">m² de chapa</th>
    <th class="r">Custo standard</th><th class="r">Custo gold</th></tr></thead>
    <tbody>{amb_rows}</tbody></table>

  <h2>Fechamento</h2>
  <table><thead><tr><th>Linha de custo</th><th class="r">Standard</th>
    <th class="r">Gold</th></tr></thead><tbody>
    <tr><td>Chapa</td><td class="r">{br(mt.custo_chapa['standard'])}</td>
      <td class="r">{br(mt.custo_chapa['gold'])}</td></tr>
    <tr><td>Fita de borda</td><td class="r">{br(sum(mt.fita_custo.values()))}</td>
      <td class="r">{br(sum(mt.fita_custo.values()))}</td></tr>
    <tr><td>Consumíveis (6%)</td><td class="r">{br(mt.consum['standard'])}</td>
      <td class="r">{br(mt.consum['gold'])}</td></tr>
    <tr><td>Logística</td><td class="r">{br(mt.LOG_TOT)}</td>
      <td class="r">{br(mt.LOG_TOT)}</td></tr>
    <tr><td>Ferragem</td>
      <td class="r">{br(sum(mt.custo_fer(m,'standard') for m in mt.MOVS))}</td>
      <td class="r">{br(sum(mt.custo_fer(m,'gold') for m in mt.MOVS))}</td></tr>
    <tr><td>Espelho</td><td class="r">{br(mt.ESP_TOT)}</td>
      <td class="r">{br(mt.ESP_TOT)}</td></tr>
    <tr><td>Terceirizados</td><td class="r">{br(sum(mt.TER.values()))}</td>
      <td class="r">{br(sum(mt.TER.values()))}</td></tr>
    <tr class="tot"><td>CUSTO DIRETO</td><td class="r">{br(mt.CD['standard'])}</td>
      <td class="r">{br(mt.CD['gold'])}</td></tr>
  </tbody></table>
  <div class="nota">A <b>lista de peças completa</b> — {len(mt.p)} lançamentos com
  material, medida, quantidade, área e fita — está em
  <b>plano-de-corte-marcelo-tolentino.csv</b>, pronta para abrir na
  seccionadora.</div>
  {foot(4, 4)}
</div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:'
        'wght@300;400;500;700&display=swap" rel="stylesheet">'
        '<style>' + CSS + '</style></head><body>' + pg1 + pg2 + pg3 + '</body></html>')
(P/'quantitativo-marcelo-tolentino.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'quantitativo-marcelo-tolentino.pdf')],
               check=True, env=env)

# ── MD · registro legível ─────────────────────────────────────────────────
md = ["# QUANTITATIVO DE MATERIAL — Marcelo Tolentino · BRZ Nova Lima", "",
      "⛔ **Documento interno de produção e compra. Não vai ao cliente.**",
      "Gerado de `corte-marcelo-tolentino.py` por",
      "`quantitativo-marcelo-tolentino.py`. Nenhum número digitado à mão.", "",
      "| | standard | gold |", "|---|--:|--:|",
      f"| chapas | **{sum(mt.CH['standard'].values())}** | **{sum(mt.CH['gold'].values())}** |",
      f"| m² líquidos de peça | {br2(mt.ar_tot)} | {br2(mt.ar_tot)} |",
      f"| aproveitamento médio | {mt.ar_tot/(sum(mt.CH['standard'].values())*mt.CH_AREA)*100:.0f}% | {mt.ar_tot/(sum(mt.CH['gold'].values())*mt.CH_AREA)*100:.0f}% |",
      f"| custo de chapa | {br(mt.custo_chapa['standard'])} | {br(mt.custo_chapa['gold'])} |", ""]
for cen in mt.CEN:
    md += [f"## Chapa · {cen}", "", "| material | m² | chapas | aprov. | R$/chapa | R$ |",
           "|---|--:|--:|--:|--:|--:|"]
    for m in sorted(mt.CH[cen], key=lambda k: (k[:2], k)):
        n = mt.CH[cen][m]
        md.append(f"| {mt.NOME[m]} | {br2(mt.area[cen][m])} | {n} | "
                  f"{mt.area[cen][m]/(n*mt.CH_AREA)*100:.0f}% | {br(mt.PRECO[m])} | {br(n*mt.PRECO[m])} |")
    md += [f"| **TOTAL** | **{br2(mt.ar_tot)}** | **{sum(mt.CH[cen].values())}** | | | "
           f"**{br(mt.custo_chapa[cen])}** |", ""]
md += ["## Fita de borda", "", "| tipo | perímetro útil (m) | comprar com 10% (m) |",
       "|---|--:|--:|",
       f"| branca (peça interna) | {br2(fita_fam['branca'])} | {br2(FITA_COMPRA['branca'])} |",
       f"| de cor (peça aparente) | {br2(fita_fam['cor'])} | {br2(FITA_COMPRA['cor'])} |",
       f"| **TOTAL** | **{br2(sum(fita_fam.values()))}** | **{br2(sum(FITA_COMPRA.values()))}** |", ""]
md += ["## Ferragem", "", "| item | qtd | un | standard | gold |", "|---|--:|---|---|---|"]
for k in ('dobr','corr','tipon','roup2p','sup'):
    if not fer_q[k]: continue
    md.append(f"| {FER_NOME[k][0]} | **{fer_q[k]:.0f}** | {FER_NOME[k][1]} | "
              f"{FER_LINHA['standard'][k]} · R$ {br2(mt.PRECO_FER['standard'][k])} | "
              f"{FER_LINHA['gold'][k]} · R$ {br2(mt.PRECO_FER['gold'][k])} |")
md += ["", f"Total de ferragem: **R$ {br(sum(mt.custo_fer(m,'standard') for m in mt.MOVS))}** "
       f"na standard · **R$ {br(sum(mt.custo_fer(m,'gold') for m in mt.MOVS))}** na gold.", "",
       "★ **RO65 Prime provisório** — cotar antes de comprar.",
       "⛔ **As portas do salão principal abrem ao toque**: a dobradiça tem de ser a",
       "versão **sem mola**, nos dois cenários.", "",
       "## Espelho", "", "| ambiente | m² | R$ |", "|---|--:|--:|"]
for am in mt.AMBS:
    if mt.ESP_AMB[am] <= 0: continue
    md.append(f"| {am} | {br2(mt.ESP_AMB[am]/mt.ESPELHO_M2)} | {br(mt.ESP_AMB[am])} |")
md += [f"| **TOTAL** | **{br2(mt.ESP_TOT/mt.ESPELHO_M2)}** | **{br(mt.ESP_TOT)}** |", "",
       "## Terceirizados · preços de referência", "", "| item | un | R$/un |", "|---|---|--:|"]
for nome, un, pu, _ in TER_ITENS:
    md.append(f"| {nome} | {un} | {br2(pu)} |")
md += ["", f"Total de terceirizados do projeto: **R$ {br(sum(mt.TER.values()))}**, "
       "igual nos dois cenários.", "",
       "## Resumo por ambiente", "", "| ambiente | m² de chapa | custo std | custo gold |",
       "|---|--:|--:|--:|"]
for am in mt.AMBS:
    md.append(f"| {am} | {br2(mt.AR_AMB[am])} | {br(mt.CD_AMB['standard'][am])} | "
              f"{br(mt.CD_AMB['gold'][am])} |")
md += [f"| **TOTAL** | **{br2(mt.ar_tot)}** | **{br(mt.CD['standard'])}** | "
       f"**{br(mt.CD['gold'])}** |", "",
       f"A lista de peças completa — **{len(mt.p)} lançamentos** — está em",
       "`plano-de-corte-marcelo-tolentino.csv`."]
(P/'quantitativo-marcelo-tolentino.md').write_text('\n'.join(md), encoding='utf-8')

import pymupdf as _fz
print(f'quantitativo-marcelo-tolentino.pdf  · {len(_fz.open(P/"quantitativo-marcelo-tolentino.pdf"))} páginas')
print('quantitativo-marcelo-tolentino.md    · registro legível')
print(f'plano-de-corte-marcelo-tolentino.csv · {len(mt.p)} peças')
print()
print(f'  chapas      standard {sum(mt.CH["standard"].values()):>4}   '
      f'gold {sum(mt.CH["gold"].values()):>4}')
print(f'  m² de peça  {mt.ar_tot:>13.2f}')
print(f'  fita        {sum(FITA_COMPRA.values()):>13.2f} m a comprar')
for k in ('dobr','corr','tipon','roup2p','sup'):
    if fer_q[k]: print(f'  {FER_NOME[k][0]:<12}{fer_q[k]:>13.0f} {FER_NOME[k][1]}')
print(f'  espelho     {mt.ESP_TOT/mt.ESPELHO_M2:>13.2f} m²')
