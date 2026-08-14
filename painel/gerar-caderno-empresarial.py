#!/usr/bin/env python3
"""Gera o Caderno Empresarial da Valvic — A4 retrato, para impressão e encadernação.

Reúne, num volume único, o conteúdo dos documentos do Dossiê Walton:
posição comercial, estrutura e pessoas, economia da operação, passivo
trabalhista e caminhos de expansão.

Uso:  python3 gerar-caderno-empresarial.py
Saída: caderno-empresarial-valvic.html
"""

# ─────────────────────────────────────────────────────────────── estilo

CSS = """
@page { size: A4 portrait; margin: 0; }
*,*::before,*::after{ box-sizing:border-box; margin:0; padding:0; }
:root{
  --navy:#0E2038; --navy2:#16314f; --navy3:#1b3a5e;
  --gold:#C2A05A; --gold-soft:#d8bd80; --gold-dk:#a9863f; --gold-bg:#f6edd6;
  --cream:#FBFAF7; --ink:#1b2733; --body:#33414f; --muted:#6c7785;
  --line:#e8e3d8; --line2:#dfdacd;
  --ok:#2f7d4f; --blue:#2f5d8c; --red:#b0413f; --gray:#6c7785;
}
html{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
body{ font-family:'Inter','Helvetica Neue',Arial,sans-serif; color:var(--ink);
  background:#d9dde3; font-size:10px; line-height:1.5; -webkit-font-smoothing:antialiased; }
.sheet{ position:relative; width:210mm; height:297mm; background:var(--cream);
  margin:14px auto; box-shadow:0 10px 40px rgba(11,22,40,.22); overflow:hidden;
  display:flex; flex-direction:column; page-break-after:always; }
.sheet:last-child{ page-break-after:auto; }

/* ── correntes de página (miolo) ── */
.rh{ display:flex; justify-content:space-between; align-items:baseline;
  padding:11mm 16mm 0 24mm; }
.rh .rl{ font-size:7.2px; font-weight:800; letter-spacing:2.4px; text-transform:uppercase; color:var(--gold-dk); }
.rh .rr{ font-size:7px; letter-spacing:1.8px; text-transform:uppercase; color:var(--muted); }
.rh::after{ content:""; }
.pg{ flex:1; padding:5mm 16mm 0 24mm; display:flex; flex-direction:column; min-height:0; }
.rf{ display:flex; justify-content:space-between; align-items:center;
  padding:0 16mm 9mm 24mm; margin-top:auto; }
.rf .fl{ font-size:6.8px; color:var(--muted); letter-spacing:.3px; }
.rf .pn{ font-family:'Cormorant Garamond',serif; font-size:13px; font-weight:700; color:var(--navy); }
.rf .pn i{ font-style:normal; color:var(--gold); margin-right:4px; }

/* ── capa ── */
.cover{ background:radial-gradient(120% 80% at 82% -8%, #1e4270 0%, rgba(30,66,112,0) 58%),
  linear-gradient(158deg,#0E2038 0%,#0b1a2e 58%,#08131f 100%); color:#fff;
  padding:24mm 24mm 18mm; display:flex; flex-direction:column; height:100%; }
.cover{ position:relative; }
.cover::after{ content:"V"; position:absolute; right:14mm; top:36mm;
  font-family:'Cormorant Garamond',serif; font-weight:700; font-size:250px; line-height:.78;
  color:rgba(226,200,140,.085); letter-spacing:-8px; pointer-events:none; }
.cover > *{ position:relative; z-index:1; }
.cover .brand{ display:flex; align-items:center; gap:13px; }
.cover .mono{ width:48px; height:48px; border:1.6px solid var(--gold); border-radius:5px;
  display:flex; align-items:center; justify-content:center; font-family:'Cormorant Garamond',serif;
  font-weight:700; font-size:26px; color:var(--gold); }
.cover .co{ font-size:14px; font-weight:700; letter-spacing:3.2px; text-transform:uppercase; }
.cover .cosub{ font-size:8.4px; color:rgba(255,255,255,.5); letter-spacing:.5px; margin-top:3px; }
.cover .mid{ margin-top:auto; }
.cover .kx{ font-size:9px; letter-spacing:5px; text-transform:uppercase; color:var(--gold); }
.cover h1{ font-family:'Cormorant Garamond',serif; font-weight:600; font-size:62px;
  line-height:1.02; margin-top:10px; letter-spacing:-.5px; }
.cover h1 span{ display:block; color:var(--gold-soft); font-style:italic; }
.cover .rule{ height:2.5px; width:64mm; margin:11mm 0 9mm;
  background:linear-gradient(90deg,var(--gold),var(--gold-dk) 60%,transparent); }
.cover .lead{ font-size:11px; color:rgba(255,255,255,.72); line-height:1.7; max-width:118mm; }
.cover .facts{ display:grid; grid-template-columns:repeat(4,1fr); gap:0; margin-top:12mm;
  border-top:1px solid rgba(255,255,255,.14); padding-top:7mm; }
.cover .fx{ padding-right:6mm; }
.cover .fx .fv{ font-family:'Cormorant Garamond',serif; font-size:22px; font-weight:700; color:var(--gold-soft); line-height:1; }
.cover .fx .fl2{ font-size:7.2px; letter-spacing:1.4px; text-transform:uppercase; color:rgba(255,255,255,.45); margin-top:5px; line-height:1.5; }
.cover .btm{ margin-top:12mm; display:flex; justify-content:space-between; align-items:flex-end;
  border-top:1px solid rgba(255,255,255,.14); padding-top:6mm; }
.cover .btm .b1{ font-size:8.4px; color:rgba(255,255,255,.5); letter-spacing:.5px; line-height:1.7; }
.cover .btm .b2{ font-size:8px; letter-spacing:2.4px; text-transform:uppercase; color:var(--gold); text-align:right; }

/* ── divisória de parte ── */
.part{ background:linear-gradient(158deg,#0E2038 0%,#0b1a2e 62%,#08131f 100%); color:#fff;
  padding:42mm 24mm 20mm; display:flex; flex-direction:column; height:100%; position:relative; }
.part::before{ content:""; position:absolute; right:0; top:0; bottom:0; width:9mm;
  background:linear-gradient(180deg,var(--gold),var(--gold-dk) 55%,rgba(169,134,63,0)); opacity:.85; }
.part::after{ content:"Valvic Marcenaria · Caderno Empresarial · 2026"; position:absolute;
  left:24mm; right:20mm; bottom:20mm; padding-top:5mm; border-top:1px solid rgba(255,255,255,.13);
  font-size:7.4px; letter-spacing:2.8px; text-transform:uppercase; color:rgba(255,255,255,.3); }
.part .pnum{ position:absolute; right:20mm; top:30mm; font-family:'Cormorant Garamond',serif;
  font-size:200px; font-weight:700; color:rgba(232,206,148,.26); line-height:.72;
  letter-spacing:-6px; z-index:0; }
.part > *:not(.pnum){ position:relative; z-index:1; }
.part .plabel{ font-size:9px; letter-spacing:5px; text-transform:uppercase; color:var(--gold); }
.part h2{ font-family:'Cormorant Garamond',serif; font-weight:600; font-size:42px;
  line-height:1.08; margin-top:6px; max-width:120mm; }
.part .pintro{ font-size:10.6px; color:rgba(255,255,255,.7); line-height:1.75; max-width:112mm; margin-top:8mm; }
.part .plist{ margin-top:13mm; border-top:1px solid rgba(255,255,255,.14); padding-top:7mm;
  display:flex; flex-direction:column; gap:5px; max-width:112mm; }
.part .pli{ display:flex; align-items:baseline; gap:10px; font-size:9.4px; color:rgba(255,255,255,.78); }
.part .pli b{ font-family:'Cormorant Garamond',serif; font-size:13px; color:var(--gold-soft); font-weight:700; min-width:22px; }

/* ── títulos de página ── */
.ptitle{ margin-bottom:6mm; }
.ptitle .kx{ font-size:7.4px; letter-spacing:3px; text-transform:uppercase; color:var(--gold-dk); font-weight:800; }
.ptitle h3{ font-family:'Cormorant Garamond',serif; font-weight:600; font-size:29px;
  line-height:1.1; color:var(--navy); margin-top:3px; }
.ptitle .sub{ font-size:10.2px; color:var(--muted); line-height:1.6; margin-top:5px; max-width:150mm; }
.ptitle::after{ content:""; display:block; height:2px; width:26mm; margin-top:5mm;
  background:linear-gradient(90deg,var(--gold),transparent); }

.sec{ display:flex; align-items:center; gap:9px; margin:0 0 7px; }
.sec:not(:first-child){ margin-top:5mm; }
.sec .bar{ width:14px; height:2px; background:var(--gold); }
.sec .tx{ font-size:8.4px; font-weight:800; letter-spacing:2px; text-transform:uppercase; color:var(--navy); }
.sec .ct{ margin-left:auto; font-size:7.8px; color:var(--muted); }

p.t{ font-size:10.2px; line-height:1.62; color:var(--body); }
p.t + p.t{ margin-top:6px; }
p.t b{ color:var(--navy); font-weight:700; }
p.t i{ font-style:normal; color:var(--gold-dk); font-weight:700; }
.lead2{ font-size:11px; line-height:1.65; color:var(--body); }
.lead2 b{ color:var(--navy); }

/* ── KPIs ── */
.kpis{ display:grid; gap:7px; }
.k4{ grid-template-columns:repeat(4,1fr); } .k3{ grid-template-columns:repeat(3,1fr); }
.k2{ grid-template-columns:repeat(2,1fr); }
.kpi{ background:#fff; border:1px solid var(--line); border-radius:8px; padding:10px 12px;
  position:relative; overflow:hidden; }
.kpi::before{ content:""; position:absolute; left:0; top:0; bottom:0; width:3px; background:var(--line2); }
.kpi.a::before{ background:var(--blue); } .kpi.b::before{ background:var(--gold); }
.kpi.c::before{ background:var(--gold-dk); } .kpi.d::before{ background:var(--navy); }
.kpi.e::before{ background:var(--ok); }   .kpi.f::before{ background:var(--red); }
.kpi .kl{ font-size:7px; font-weight:800; letter-spacing:1.1px; text-transform:uppercase; color:var(--muted); }
.kpi .kv{ font-family:'Cormorant Garamond',serif; font-size:24px; font-weight:700; color:var(--navy); line-height:1.1; margin-top:3px; }
.kpi .kv small{ font-family:'Inter',sans-serif; font-size:10.5px; font-weight:700; }
.kpi .kd{ font-size:7.5px; color:var(--muted); line-height:1.45; margin-top:4px; }
.kpi .kd b{ color:var(--navy); }

/* ── tabelas ── */
table{ width:100%; border-collapse:collapse; background:#fff; }
thead th{ background:var(--navy2); color:#fff; font-size:7px; font-weight:600; letter-spacing:.6px;
  text-transform:uppercase; padding:6px 7px; text-align:left; }
thead th.num{ text-align:right; }
tbody td{ padding:5.6px 7px; border-bottom:1px solid var(--line); font-size:8.9px;
  vertical-align:middle; line-height:1.4; }
tbody td.num{ text-align:right; font-variant-numeric:tabular-nums; }
tbody td.nm{ font-weight:800; color:var(--navy); }
tbody td .fn{ display:block; font-size:7.2px; font-weight:500; color:var(--muted); margin-top:1px; line-height:1.35; }
tbody td.sub{ font-weight:800; color:var(--navy); background:#faf7f0; }
tbody tr.tot td{ background:var(--navy); color:#fff; font-weight:800; font-size:9.2px;
  border-bottom:none; padding:7px; }
tbody tr.tot td.num{ color:var(--gold-soft); }
tbody tr.sec2 td{ background:#f1eee6; font-size:7.2px; font-weight:800; letter-spacing:1.4px;
  text-transform:uppercase; color:var(--navy); padding:4.5px 7px; border-bottom:1px solid var(--line2); }
tbody tr.enc td{ background:var(--gold-bg); font-weight:700; color:#7a5b17; border-bottom:none; padding:7px; }
tbody tr.enc td.num{ color:#7a5b17; font-weight:800; }
table.tight tbody td{ padding:4.6px 7px; font-size:8.5px; }
table.xt tbody td{ padding:3.2px 7px; font-size:8.2px; }
table.xt tbody tr.tot td{ padding:5px 7px; font-size:8.8px; }
.dt{ font-size:8px; color:var(--muted); font-variant-numeric:tabular-nums; }

.badge{ display:inline-block; font-size:6.6px; font-weight:800; letter-spacing:.7px;
  text-transform:uppercase; padding:1.5px 5px; border-radius:8px; white-space:nowrap; }
.b-clt{ background:#eaf1f8; color:var(--blue); } .b-pj{ background:#f3ece1; color:var(--gold-dk); }
.b-ext{ background:#efefef; color:var(--gray); } .b-soc{ background:#e9f2ec; color:var(--ok); }
.b-need{ background:#fbeceb; color:var(--red); } .b-new{ background:#eaf1f8; color:var(--blue); }

/* ── cartões ── */
.cards{ display:grid; gap:7px; }
.c2{ grid-template-columns:repeat(2,1fr); } .c3{ grid-template-columns:repeat(3,1fr); }
.c4{ grid-template-columns:repeat(4,1fr); }
.card{ background:#fff; border:1px solid var(--line); border-radius:8px; padding:10px 12px; }
.card .ct{ font-size:7.2px; font-weight:800; letter-spacing:1.2px; text-transform:uppercase; color:var(--gold-dk); }
.card h4{ font-size:11.4px; font-weight:800; color:var(--navy); line-height:1.25; margin-top:3px; }
.card .cv{ font-family:'Cormorant Garamond',serif; font-size:21px; font-weight:700; color:var(--navy); line-height:1.15; margin-top:2px; }
.card p{ font-size:8.8px; color:var(--body); line-height:1.55; margin-top:5px; }
.card p b{ color:var(--navy); }
.card ul{ margin:5px 0 0; padding-left:13px; }
.card li{ font-size:8.6px; color:var(--body); line-height:1.5; margin-bottom:2.5px; }
.card li::marker{ color:var(--gold); }
.card li b{ color:var(--navy); }
.card.gold{ border-color:var(--gold); box-shadow:0 0 0 2px rgba(194,160,90,.12); }
.card.warn{ background:#fdf5f4; border-color:#e8cdcb; }
.card.warn .ct{ color:var(--red); } .card.warn li::marker{ color:var(--red); }
.card.blue{ background:#f2f6fa; border-color:#d3e0ec; } .card.blue .ct{ color:var(--blue); }
.card.ok{ background:#f3f7f4; border-color:#cadfd2; } .card.ok .ct{ color:var(--ok); }
.card .pill{ display:inline-block; font-size:7px; font-weight:800; letter-spacing:.8px;
  text-transform:uppercase; padding:2px 7px; border-radius:9px; background:var(--gold-bg);
  color:var(--gold-dk); margin-top:4px; }

/* ── notas ── */
.note{ background:#f6f3ec; border:1px solid var(--line); border-radius:8px; padding:10px 13px; }
.note .nt{ font-size:7.2px; letter-spacing:1.4px; text-transform:uppercase; color:var(--navy);
  font-weight:800; margin-bottom:5px; }
.note p{ font-size:8.9px; color:var(--body); line-height:1.55; }
.note p + p{ margin-top:4px; }
.note b{ color:var(--navy); }
.note ul{ margin:0; padding-left:13px; }
.note li{ font-size:8.9px; color:var(--body); line-height:1.5; margin-bottom:3px; }
.note li:last-child{ margin-bottom:0; }
.note li::marker{ color:var(--gold); }
.note li b{ color:var(--navy); }
.note.warn{ background:#fdf5f4; border-color:#e8cdcb; }
.note.warn .nt{ color:var(--red); } .note.warn li::marker{ color:var(--red); }
.note.blue{ background:#f2f6fa; border-color:#d3e0ec; }
.note.blue .nt{ color:var(--blue); } .note.blue li::marker{ color:var(--blue); }
.note.ok{ background:#f3f7f4; border-color:#cadfd2; }
.note.ok .nt{ color:var(--ok); } .note.ok li::marker{ color:var(--ok); }

/* ── faixa de destaque ── */
.band{ background:linear-gradient(150deg,var(--navy) 0%,#0b1a2e 100%); color:#fff;
  border-radius:8px; padding:12px 16px; display:flex; align-items:center; gap:15px;
  position:relative; overflow:hidden; }
.band::after{ content:""; position:absolute; left:0; top:0; bottom:0; width:3px; background:var(--gold); }
.band .bl{ font-size:7.4px; letter-spacing:2.2px; text-transform:uppercase; color:var(--gold); }
.band .bv{ font-family:'Cormorant Garamond',serif; font-size:32px; font-weight:700; line-height:1; margin-top:3px; }
.band .br{ margin-left:auto; text-align:right; font-size:8.4px; color:rgba(255,255,255,.62);
  line-height:1.6; max-width:88mm; }
.band .br b{ color:#fff; }

/* ── sumário ── */
.toc{ display:flex; flex-direction:column; gap:0; }
.toc .tp{ margin-top:3.6mm; padding-bottom:4px; border-bottom:1.5px solid var(--navy);
  display:flex; align-items:baseline; gap:9px; }
.toc .tp:first-child{ margin-top:0; }
.toc .tp .tn{ font-family:'Cormorant Garamond',serif; font-size:15px; font-weight:700; color:var(--gold-dk); }
.toc .tp .tt{ font-size:9.2px; font-weight:800; letter-spacing:2px; text-transform:uppercase; color:var(--navy); }
.toc .tp .tg{ margin-left:auto; font-size:7.4px; color:var(--muted); letter-spacing:1px; }
.toc .ti{ display:flex; align-items:baseline; gap:8px; padding:3.3px 0 3.3px 4px;
  border-bottom:1px solid var(--line); }
.toc .ti .il{ font-size:9.8px; color:var(--ink); font-weight:600; }
.toc .ti .id{ font-size:8.4px; color:var(--muted); }
.toc .ti .dots{ flex:1; border-bottom:1px dotted var(--line2); margin:0 4px 3px; }
.toc .ti .ip{ font-family:'Cormorant Garamond',serif; font-size:13px; font-weight:700; color:var(--navy); min-width:16px; text-align:right; }

/* ── escada ── */
.stair{ display:grid; grid-template-columns:repeat(5,1fr); gap:6px; align-items:end; }
.st{ display:flex; flex-direction:column; justify-content:flex-end; }
.st .sbar{ border-radius:6px 6px 0 0; padding:9px 9px 8px; color:#fff; position:relative; }
.st .sv{ font-family:'Cormorant Garamond',serif; font-size:22px; font-weight:700; line-height:1; }
.st .sv small{ font-family:'Inter',sans-serif; font-size:8.4px; font-weight:600; display:block; margin-top:2px; opacity:.75; }
.st .sw{ font-size:6.8px; letter-spacing:1.3px; text-transform:uppercase; opacity:.7; }
.st .sbody{ border:1px solid var(--line); border-top:none; background:#fff;
  border-radius:0 0 6px 6px; padding:8px 9px; flex:1; }
.st .sk{ font-size:6.6px; font-weight:800; letter-spacing:.9px; text-transform:uppercase; color:var(--gold-dk); }
.st .sp{ font-size:8.2px; color:var(--body); line-height:1.45; margin-top:2px; }
.st .sp b{ color:var(--navy); }
.st .sp + .sk{ margin-top:5px; }

/* ── fluxo de etapas ── */
.flow{ display:flex; flex-direction:column; gap:4px; }
.fst{ display:grid; grid-template-columns:8mm 1fr 46mm 44mm; gap:9px; align-items:stretch;
  background:#fff; border:1px solid var(--line); border-radius:7px; padding:8px 10px; }
.fst .fn2{ font-family:'Cormorant Garamond',serif; font-size:21px; font-weight:700; color:var(--gold); line-height:1; }
.fst .fnm{ font-size:10px; font-weight:800; color:var(--navy); line-height:1.2; }
.fst .fwho{ font-size:8px; color:var(--muted); line-height:1.5; margin-top:3px; }
.fst .fwho b{ color:var(--navy2); font-weight:700; }
.fst .fh{ font-size:6.6px; font-weight:800; letter-spacing:1px; text-transform:uppercase; color:var(--gold-dk); }
.fst .fv2{ font-size:8.2px; color:var(--body); line-height:1.5; margin-top:2px; }
.fst .fv2 b{ color:var(--navy); }
.fst .risk{ display:block; font-size:7.4px; color:var(--red); font-weight:700; margin-top:3px; line-height:1.4; }

/* ── legenda ── */
.leg{ display:flex; flex-wrap:wrap; gap:11px; margin-top:6px; }
.leg span{ display:flex; align-items:center; gap:5px; font-size:7.4px; color:var(--muted); }
.leg i{ width:9px; height:9px; border-radius:2px; display:block; font-style:normal; }

.two{ display:grid; grid-template-columns:1fr 1fr; gap:7px; }
.two-a{ display:grid; grid-template-columns:1.25fr 1fr; gap:7px; }
.mt{ margin-top:5mm; }
.mts{ margin-top:7px; }

/* ── fecho ── */
.end{ background:linear-gradient(158deg,#0E2038 0%,#0b1a2e 62%,#08131f 100%); color:#fff;
  padding:28mm 24mm 20mm; display:flex; flex-direction:column; height:100%; }
.end .kx{ font-size:8.5px; letter-spacing:4.5px; text-transform:uppercase; color:var(--gold); }
.end h2{ font-family:'Cormorant Garamond',serif; font-weight:600; font-size:38px; line-height:1.1; margin-top:7px; }
.end h2 span{ color:var(--gold-soft); font-style:italic; }
.end .src{ margin-top:10mm; border-top:1px solid rgba(255,255,255,.14); padding-top:7mm; }
.end .sh{ font-size:7.2px; letter-spacing:2.4px; text-transform:uppercase; color:var(--gold); margin-bottom:5mm; }
.end .sr{ display:flex; align-items:baseline; gap:9px; padding:5px 0; border-bottom:1px solid rgba(255,255,255,.09); }
.end .sr .sd{ font-size:8px; color:rgba(255,255,255,.4); min-width:16mm; letter-spacing:.5px; }
.end .sr .sn{ font-size:9.4px; color:rgba(255,255,255,.85); font-weight:600; }
.end .sr .sf{ margin-left:auto; font-size:7.6px; color:rgba(255,255,255,.35); }
.end .fin{ margin-top:auto; border-top:1px solid rgba(255,255,255,.14); padding-top:6mm;
  display:flex; justify-content:space-between; align-items:flex-end; }
.end .fin .f1{ font-size:8.4px; color:rgba(255,255,255,.5); line-height:1.7; max-width:110mm; }
.end .fin .f2{ font-size:8px; letter-spacing:2.4px; text-transform:uppercase; color:var(--gold); text-align:right; }

.btn{ position:fixed; top:16px; right:16px; z-index:99; background:var(--navy); color:#fff;
  border:1px solid var(--gold); padding:10px 18px; border-radius:6px; font-size:12px;
  font-weight:600; cursor:pointer; }
@media print{ body{ background:#fff; } .sheet{ margin:0; box-shadow:none; } .btn{ display:none; } }
"""

# ─────────────────────────────────────────────────────── infraestrutura

PAGES = []          # (kind, html) — kind: 'full' (sangria) ou 'body'
_TOC = []           # (tipo, rótulo, descrição, página)


def full(html):
    PAGES.append(('full', html))


def page(rail, title_kx, title_h3, title_sub, body, foot=None):
    """Página de miolo com correntes."""
    head = ''
    if title_h3:
        sub = f'<div class="sub">{title_sub}</div>' if title_sub else ''
        head = (f'<div class="ptitle"><div class="kx">{title_kx}</div>'
                f'<h3>{title_h3}</h3>{sub}</div>')
    PAGES.append(('body', (rail, head + body, foot)))


def render():
    out = []
    n = 0
    for kind, data in PAGES:
        n += 1
        if kind == 'full':
            out.append(f'<section class="sheet">{data}</section>')
        else:
            rail, body, foot = data
            fl = foot or 'Caderno Empresarial · Valvic Marcenaria — Vargas Decor Ltda'
            out.append(
                f'<section class="sheet">'
                f'<div class="rh"><span class="rl">{rail}</span>'
                f'<span class="rr">Valvic Marcenaria</span></div>'
                f'<div class="pg">{body}</div>'
                f'<div class="rf"><span class="fl">{fl}</span>'
                f'<span class="pn"><i>·</i>{n:02d}</span></div>'
                f'</section>')
    return '\n'.join(out)


# ═══════════════════════════════════════════════════════ 01 · CAPA

full("""
<div class="cover">
  <div class="brand">
    <div class="mono">V</div>
    <div><div class="co">Valvic Marcenaria</div>
      <div class="cosub">Vargas Decor Ltda &nbsp;·&nbsp; CNPJ 17.269.304/0001-51 &nbsp;·&nbsp; Belo Horizonte / MG</div></div>
  </div>
  <div class="mid">
    <div class="kx">Volume único · 2026</div>
    <h1>Caderno<span>Empresarial</span></h1>
    <div class="rule"></div>
    <p class="lead">A empresa reunida num só documento: a posição comercial, a estrutura de pessoas,
      a economia da operação, o passivo trabalhista e os caminhos de expansão — cada assunto
      com os números abertos e as decisões postas na mesa.</p>
  </div>
  <div class="btm">
    <div class="b1">Documento de trabalho · uso restrito<br>Contém dado de remuneração e posição financeira</div>
    <div class="b2">Agosto<br>2026</div>
  </div>
</div>""")

# ═══════════════════════════════════════════════════════ 02 · SUMÁRIO

TOC = [
    ('parte', 'I', 'A Empresa Hoje', '4 páginas', None),
    ('item', 'Identidade, trajetória e capacidade instalada', 'o que já existe e está pago', '05'),
    ('item', 'Posição comercial — agosto e setembro', 'carteira, recebido e produção', '06'),
    ('item', 'Carteira em conclusão, contrato a contrato', '17 contratos · R$ 758,4 mil', '07'),
    ('item', 'Pipeline em negociação', 'R$ 1,06 mi fora da carteira', '08'),

    ('parte', 'II', 'Estrutura & Pessoas', '5 páginas', None),
    ('item', 'Organograma e carga operacional dos sócios', 'onde tudo converge hoje', '10'),
    ('item', 'Quadro de pessoal e folha mensal', 'vínculo, fixo e variável por pessoa', '11'),
    ('item', 'Estrutura de demandas', 'o que existe, o que entra, o que falta', '12'),
    ('item', 'Fluxo de trabalho — posição e impacto', 'a cadeia de valor em 6 etapas', '13'),

    ('parte', 'III', 'Economia da Operação', '4 páginas', None),
    ('item', 'Modelo econômico e alavancagem operacional', 'o que cada nível de volume gera', '15'),
    ('item', 'Custo fixo da operação', 'quanto custa manter a empresa de pé', '16'),
    ('item', 'Folha e estrutura, item a item', 'pessoa a pessoa e rubrica a rubrica', '17'),
    ('item', 'Fluxo de caixa — agosto e setembro', 'a receber, a pagar e demanda de material', '18'),

    ('parte', 'IV', 'Passivo Trabalhista', '2 páginas', None),
    ('item', 'Apuração por contrato', 'verbas, encargos e perímetro', '20'),

    ('parte', 'V', 'Caminhos de Expansão', '9 páginas', None),
    ('item', 'A escada de produção', 'de R$ 250 mil a R$ 1 milhão por mês', '22'),
    ('item', 'Galpão: adaptar o atual ou mudar', 'os dois caminhos, com custos abertos', '23'),
    ('item', 'Comparativo de coladeiras', 'cinco opções lado a lado', '24'),
    ('item', 'Linha industrial e complementares', 'nesting, furação, esteira e embaladora', '25'),
    ('item', 'Diferencial de mercado — puxadores', 'margem por posicionamento', '26'),
    ('item', 'Prestação de serviços', 'a capacidade ociosa como receita', '27'),
    ('item', 'Plano de expansão 2026–2027', 'fases, máquinas e mapa do investimento', '28'),
    ('item', 'Retorno e payback', 'cenários conservador e de capacidade', '29'),
]

rows = []
for r in TOC:
    if r[0] == 'parte':
        rows.append(f'<div class="tp"><span class="tn">{r[1]}</span>'
                    f'<span class="tt">{r[2]}</span><span class="tg">{r[3]}</span></div>')
    else:
        rows.append(f'<div class="ti"><span class="il">{r[1]}</span>'
                    f'<span class="id">· {r[2]}</span><span class="dots"></span>'
                    f'<span class="ip">{r[3]}</span></div>')

page('Sumário', 'Como este caderno está organizado', 'Sumário',
     'Cinco partes, da posição de hoje aos caminhos de crescimento. Cada parte abre com uma '
     'página de contexto e reúne o material que já existia em documentos separados.',
     '<div class="toc">' + ''.join(rows) + '</div>'
     '<div class="note mt"><div class="nt">Nota de leitura</div>'
     '<p>Este caderno <b>compila</b> documentos produzidos entre junho e agosto de 2026, cada parte '
     'preservando os números e as datas da sua origem — por isso convivem aqui referências de períodos '
     'diferentes, sempre identificadas. Onde duas fontes adotam premissas distintas, a divergência está '
     '<b>sinalizada em vez de resolvida</b>. Valores de máquina são <b>de feira</b>: referências de '
     'negociação, a confirmar na proposta final de cada fornecedor.</p></div>')

# ═════════════════════════════════════════════ 03 · ABERTURA

page('Abertura', 'O documento', 'O que este caderno reúne',
     'Uma leitura contínua da empresa: onde ela está, com quem opera, quanto custa, o que deve e para onde pode ir.',
     """
<p class="lead2">A Valvic é uma marcenaria industrial de móveis planejados sob medida em Belo Horizonte,
operando sob a razão social <b>Vargas Decor Ltda</b>. Cresceu <b>133% entre 2023 e 2025</b> — de
R$ 645 mil para R$ 1,5 milhão ao ano — <b>sem aporte externo de capital</b>, e chegou a 2026 com um
parque produtivo instalado e majoritariamente quitado.</p>

<p class="t mts">O material que segue foi produzido ao longo de junho, julho e agosto de 2026 em documentos
separados, cada um respondendo a uma pergunta específica. Reunidos aqui, eles formam um retrato único:
<b>a carteira que está em execução</b>, <b>as pessoas que fazem a operação girar</b> e o que ela custa,
<b>a economia que sustenta o negócio</b>, <b>o passivo trabalhista acumulado</b> e <b>os caminhos de
expansão</b> com os investimentos abertos item a item.</p>

<div class="sec mt"><span class="bar"></span><span class="tx">A empresa em números</span><span class="ct">posição consolidada · 08 de agosto de 2026</span></div>
<div class="kpis k4">
  <div class="kpi a"><div class="kl">Carteira em conclusão</div><div class="kv"><small>R$</small> 758<small>,4 mil</small></div><div class="kd">17 contratos a entregar em agosto e setembro</div></div>
  <div class="kpi b"><div class="kl">Já recebido</div><div class="kv"><small>R$</small> 319<small>,0 mil</small></div><div class="kd">42% do vendido, cobrado em meses anteriores</div></div>
  <div class="kpi c"><div class="kl">Saldo a receber</div><div class="kv"><small>R$</small> 439<small>,4 mil</small></div><div class="kd">R$ 215,9k em agosto · R$ 223,5k em setembro</div></div>
  <div class="kpi f"><div class="kl">Falta produzir</div><div class="kv"><small>R$</small> 497<small>,1 mil</small></div><div class="kd">66% da carteira ainda por fabricar</div></div>
</div>
<div class="kpis k4 mts">
  <div class="kpi e"><div class="kl">Equipe</div><div class="kv">10<small> + 2 sócios</small></div><div class="kd">Karla e Hugo com data · 4 a 5 vagas abertas</div></div>
  <div class="kpi a"><div class="kl">Custo fixo mensal</div><div class="kv"><small>R$</small> 77,2<small> mil</small></div><div class="kd">Folha R$ 62,6k + estrutura R$ 14,6k · setembro</div></div>
  <div class="kpi d"><div class="kl">Parque produtivo</div><div class="kv"><small>R$</small> 506<small> mil</small></div><div class="kd">Instalado e em grande parte quitado</div></div>
  <div class="kpi c"><div class="kl">Horizonte</div><div class="kv"><small>R$</small> 1<small> mi/mês</small></div><div class="kd">Meta aspiracional · hoje o teto é ~R$ 250 mil</div></div>
</div>

<div class="sec mt"><span class="bar"></span><span class="tx">Como ler as cinco partes</span></div>
<div class="cards c2">
  <div class="card"><div class="ct">Partes I e II · o retrato</div><h4>Onde a empresa está e com quem</h4>
    <p>A carteira em execução, projeto a projeto, e a estrutura de pessoas que a entrega — com a folha
    aberta por colaborador e o mapa de quem responde a quem. É a fotografia do presente.</p></div>
  <div class="card"><div class="ct">Partes III e IV · a conta</div><h4>Quanto rende e quanto deve</h4>
    <p>A alavancagem operacional — por que cada real novo de volume converte desproporcionalmente em
    resultado — e o passivo trabalhista apurado contrato a contrato.</p></div>
</div>
<div class="cards c1 mts" style="grid-template-columns:1fr">
  <div class="card gold"><div class="ct">Parte V · a decisão</div><h4>Os caminhos de expansão, com os custos abertos</h4>
    <p>De R$ 250 mil a R$ 1 milhão por mês, em degraus. Cada degrau com o seu gatilho de demanda, o gargalo
    que ataca e o investimento que exige. As máquinas com ficha técnica e preço; o galpão com os dois
    caminhos possíveis. <b>Não há recomendação</b> — há caminhos, custos e trade-offs postos lado a lado
    para que a decisão seja informada.</p></div>
</div>""")

# ═══════════════════════════════════════════ PARTE I

full("""
<div class="part">
  <div class="pnum">I</div>
  <div class="plabel">Parte um</div>
  <h2>A Empresa Hoje</h2>
  <p class="pintro">O que já existe, está instalado e está pago — e o que a empresa tem em execução
    neste momento. Uma marcenaria que dobrou de tamanho em dois anos sem capital externo e que hoje
    opera próxima do seu teto de capacidade, com uma carteira de 18 projetos e um pipeline maior
    que a própria carteira.</p>
  <div class="plist">
    <div class="pli"><b>05</b><span>Identidade, trajetória e capacidade instalada</span></div>
    <div class="pli"><b>06</b><span>Posição comercial — agosto e setembro</span></div>
    <div class="pli"><b>07</b><span>Carteira em conclusão, contrato a contrato</span></div>
    <div class="pli"><b>08</b><span>Pipeline em negociação</span></div>
  </div>
</div>""")

# ── 05 identidade
page('Parte I · A Empresa Hoje', 'Identidade & capacidade', 'A máquina já está construída',
     'A Valvic não é uma promessa a construir: é uma operação instalada, paga e com histórico. O que ela tem de capacidade supera o que fatura.',
     """
<div class="kpis k3">
  <div class="kpi a"><div class="kl">Parque produtivo instalado</div><div class="kv"><small>R$</small> 506<small> mil</small></div><div class="kd">Máquinas, ferramentas e infraestrutura — em grande parte quitado</div></div>
  <div class="kpi b"><div class="kl">Crescimento 2023 → 2025</div><div class="kv">+133%</div><div class="kd">De R$ 645 mil para R$ 1,5 milhão ao ano, sem capital externo</div></div>
  <div class="kpi e"><div class="kl">Margem de contribuição</div><div class="kv">43,5%</div><div class="kd">Referência do modelo econômico de jun/2026</div></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Os quatro ativos que o capital não compra rápido</span></div>
<table>
  <thead><tr><th style="width:24%">Ativo</th><th>Por que vale</th><th style="width:18%">Situação</th></tr></thead>
  <tbody>
    <tr><td class="nm">Parque de máquinas</td><td>CNC, esquadrejadeira, coladeira e exaustão — corte e usinagem em padrão industrial</td><td><span class="badge b-ok" style="background:#e9f2ec;color:#2f7d4f">Instalado · pago</span></td></tr>
    <tr><td class="nm">Equipe formada</td><td>Marceneiros, operador de máquinas, programador CNC e coordenação de produção</td><td><span class="badge b-ok" style="background:#e9f2ec;color:#2f7d4f">Em operação</span></td></tr>
    <tr><td class="nm">Marca &amp; carteira</td><td>Reputação de planejados sob medida em BH, com base de clientes recorrente e indicação ativa</td><td><span class="badge b-ok" style="background:#e9f2ec;color:#2f7d4f">Ativa</span></td></tr>
    <tr><td class="nm">Processo &amp; track record</td><td>Dobrou de tamanho em dois anos sozinha — sabe produzir e sabe entregar</td><td><span class="badge b-ok" style="background:#e9f2ec;color:#2f7d4f">Comprovado</span></td></tr>
  </tbody>
</table>

<div class="sec"><span class="bar"></span><span class="tx">Inventário do parque instalado</span><span class="ct">todos quitados</span></div>
<table class="tight">
  <thead><tr><th style="width:27%">Equipamento</th><th>Papel hoje</th><th style="width:30%">Papel na linha expandida</th></tr></thead>
  <tbody>
    <tr><td class="nm">Raizen Solid TAF<span class="fn">Centro de usinagem CNC · 380V · 3 eixos</span></td><td>Nesting e usinagens especiais, dividindo tempo entre as duas — ~35 chapas/dia</td><td>Passa a fazer <b>só usinagens especiais</b>, liberada pela CNC nesting dedicada</td></tr>
    <tr><td class="nm">SCM minimax me 25<span class="fn">Coladeira de bordas · fita 0,4 mm · cola EVA</span></td><td>Coladeira principal · atende até ~R$ 300 mil/mês e <b>não finaliza 100%</b> a peça</td><td>Vira <b>backup</b> da nova — garante uptime, elimina ponto único de falha</td></tr>
    <tr><td class="nm">Raizen RZN 3200P<span class="fn">Esquadrejadeira</span></td><td>Cluster de corte</td><td>Mantém a função de corte</td></tr>
    <tr><td class="nm">Ferramental &amp; infraestrutura<span class="fn">Tupia, serra, coletores, pneumático, bancadas</span></td><td>Apoio de produção</td><td>Mantém, somado ao compressor novo da linha</td></tr>
  </tbody>
</table>

<div class="two mt">
  <div class="note ok"><div class="nt">Princípio adotado</div>
    <p><b>Nenhuma máquina atual será vendida ou descartada.</b> Cada equipamento ganha um papel novo na
    linha expandida — a Solid TAF deixa de brigar entre nesting e especiais, e a me 25 vira redundância.
    O ganho imediato é que <b>o corte deixa de ser o gargalo</b>.</p></div>
  <div class="note"><div class="nt">A leitura de fundo</div>
    <p>Um concorrente que quisesse partir do zero precisaria desembolsar <b>~R$ 500 mil só em máquinas</b> e
    <b>dois anos para provar a operação</b>. A Valvic já tem os dois. A margem de 43,5% significa que cada
    projeto contribui com 43 centavos de cada real para cobrir estrutura e gerar lucro —
    <b>o que limita o resultado não é a margem, é a quantidade de projetos</b>.</p></div>
</div>""")

# ── 06 posição comercial
page('Parte I · A Empresa Hoje', 'Posição comercial · 08/08/2026', 'A carteira em conclusão',
     'Os 17 contratos com entrega prevista para agosto e setembro: quanto valem, quanto já entrou, quanto ainda entra e quanto falta fabricar.',
     """
<div class="kpis k4">
  <div class="kpi a"><div class="kl">Receita da carteira</div><div class="kv"><small>R$</small> 758<small>,4 mil</small></div><div class="kd">17 contratos · tickets de R$ 5,3k a R$ 124k</div></div>
  <div class="kpi e"><div class="kl">Já recebido</div><div class="kv"><small>R$</small> 319<small>,0 mil</small></div><div class="kd"><b>42%</b> do vendido, cobrado em meses anteriores</div></div>
  <div class="kpi b"><div class="kl">Saldo a receber</div><div class="kv"><small>R$</small> 439<small>,4 mil</small></div><div class="kd">R$ 215,9k em agosto · R$ 223,5k em setembro</div></div>
  <div class="kpi f"><div class="kl">Falta produzir</div><div class="kv"><small>R$</small> 497<small>,1 mil</small></div><div class="kd"><b>66%</b> da carteira ainda por fabricar</div></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Os dois meses lado a lado</span><span class="ct">valores em reais</span></div>
<table>
  <thead><tr><th style="width:24%">Mês</th><th class="num" style="width:19%">Vendido</th>
    <th class="num" style="width:19%">Recebido</th><th class="num" style="width:19%">A receber</th>
    <th class="num" style="width:19%">A produzir</th></tr></thead>
  <tbody>
    <tr><td class="nm">Agosto<span class="fn">11 contratos</span></td><td class="num">360.400</td><td class="num">144.500</td><td class="num sub">215.900</td><td class="num sub">185.880<span class="fn">52%</span></td></tr>
    <tr><td class="nm">Setembro<span class="fn">6 contratos</span></td><td class="num">398.000</td><td class="num">174.500</td><td class="num sub">223.500</td><td class="num sub">311.200<span class="fn">78%</span></td></tr>
    <tr class="tot"><td>Total da carteira</td><td class="num">758.400</td><td class="num">319.000</td><td class="num">439.400</td><td class="num">497.080</td></tr>
  </tbody>
</table>

<div class="sec"><span class="bar"></span><span class="tx">Onde está a carteira hoje</span><span class="ct">% do valor vendido</span></div>
<div class="cards c3">
  <div class="card ok"><div class="ct">Já produzido</div><div class="cv">R$ 261,3 mil</div><span class="pill" style="background:#e9f2ec;color:#2f7d4f">34% da carteira</span>
    <p>Fabricado ou entregue. Concentra-se nos contratos mais antigos — Augusto, Maria, Rejane e Cristiane.</p></div>
  <div class="card warn"><div class="ct">Falta produzir</div><div class="cv">R$ 497,1 mil</div><span class="pill" style="background:#fbeceb;color:#b0413f">66% da carteira</span>
    <p><b>Dez contratos estão integralmente por fabricar</b> — Jairo, Flavia, Simony, Ana Carolina, Andrea, Richard, Carla, Giseli, Luciana e Luiz.</p></div>
  <div class="card"><div class="ct">Carga por mês</div><div class="cv">52% <span style="font-size:12px;color:#6c7785">e</span> 78%</div><span class="pill">agosto e setembro</span>
    <p>Setembro é o mês pesado: <b>quase quatro quintos da produção do mês ainda não começou</b>.</p></div>
</div>

<div class="note mt"><div class="nt">Como ler estes números</div>
  <p><b>Vendido</b> é o valor de contrato. <b>Recebido</b> é o que já foi cobrado em meses anteriores — e que
  <b>já não está em caixa</b>, tendo sido aplicado em material e no custeio da operação. <b>A produzir</b> é a
  parcela de cada contrato que ainda precisa passar pela fábrica.</p>
  <p>Fora desta conta: <b>R$ 87 mil</b> do projeto André / Alphaville, entregue e com cobrança em aberto
  sem data de recebimento.</p></div>""")

# ── 07 carteira contrato a contrato
CART = [
    ('Augusto', '', 90000, 24000, 0.30, '08'),
    ('Cristiane', '', 94000, 42000, 0.50, '08'),
    ('Lucas Mello', '', 46000, 24000, 0.80, '08'),
    ('Rejane', '', 35600, 14000, 0.05, '08'),
    ('Carla', '', 27000, 13500, 1.00, '08'),
    ('Flavia', '', 15000, 7500, 1.00, '08'),
    ('Giseli', '', 14000, 7000, 1.00, '08'),
    ('Bernardo', 'fabricado', 13000, 4000, 0.00, '08'),
    ('Luciana Rajão', '', 12000, 0, 1.00, '08'),
    ('Tania', 'entregue e quitado', 8500, 8500, 0.00, '08'),
    ('Luiz', '', 5300, 0, 1.00, '08'),
    ('Maria · Vale dos Cristais', 'casa R$ 117.000 + lavanderia R$ 7.000', 124000, 58000, 0.30, '09'),
    ('Ana Carolina', '', 108000, 32500, 1.00, '09'),
    ('Jairo', '', 63000, 25000, 1.00, '09'),
    ('Andrea', 'clínica de dermatologia', 47000, 14000, 1.00, '09'),
    ('Simony', 'quitado, ainda por fabricar', 34000, 34000, 1.00, '09'),
    ('Richard', '', 22000, 11000, 1.00, '09'),
]
def _n(v):
    return '—' if v == 0 else format(int(round(v)), ',d').replace(',', '.')
lin = ''
for mes, rot in [('08', 'Agosto · 11 contratos'), ('09', 'Setembro · 6 contratos')]:
    sel = [c for c in CART if c[5] == mes]
    lin += f'<tr class="sec2"><td colspan="6">{rot}</td></tr>'
    for nm, sub, v, r, pct, _ in sel:
        f = f'<span class="fn">{sub}</span>' if sub else ''
        cor = ' style="color:#b0413f"' if pct == 1.0 else ''
        lin += (f'<tr><td class="nm">{nm}{f}</td><td class="num">{_n(v)}</td>'
                f'<td class="num">{_n(r)}</td><td class="num sub">{_n(v-r)}</td>'
                f'<td class="num dt"{cor}>{"—" if pct==0 else f"{pct:.0%}"}</td>'
                f'<td class="num sub">{_n(v*pct)}</td></tr>')
    sv = sum(c[2] for c in sel); sr = sum(c[3] for c in sel); sp = sum(c[2]*c[4] for c in sel)
    lin += (f'<tr class="enc"><td>Subtotal de {"agosto" if mes=="08" else "setembro"}</td>'
            f'<td class="num">{_n(sv)}</td><td class="num">{_n(sr)}</td><td class="num">{_n(sv-sr)}</td>'
            f'<td class="num">{sp/sv:.0%}</td><td class="num">{_n(sp)}</td></tr>')

page('Parte I · A Empresa Hoje', 'Carteira em conclusão · 08/08/2026', 'Contrato a contrato',
     'Os 17 projetos com entrega prevista nos dois meses, com valor, recebimento e o que ainda falta fabricar em cada um.',
     f"""
<table class="tight">
  <thead><tr><th style="width:27%">Cliente</th><th class="num" style="width:14%">Vendido</th>
    <th class="num" style="width:14%">Recebido</th><th class="num" style="width:15%">A receber</th>
    <th class="num" style="width:13%">% a produzir</th><th class="num" style="width:17%">R$ a produzir</th></tr></thead>
  <tbody>{lin}
    <tr class="tot"><td>Total · 17 contratos</td><td class="num">758.400</td><td class="num">319.000</td>
      <td class="num">439.400</td><td class="num">66%</td><td class="num">497.080</td></tr>
  </tbody>
</table>

<div class="two mt">
  <div class="note blue"><div class="nt">Concentração da carteira</div>
    <p>Os <b>cinco maiores contratos</b> — Maria (R$ 124k), Ana Carolina (R$ 108k), Cristiane (R$ 94k),
    Augusto (R$ 90k) e Jairo (R$ 63k) — somam <b>R$ 479 mil</b>, ou <b>63% de toda a carteira</b>. Os doze
    restantes dividem os R$ 279 mil finais.</p>
    <p style="margin-top:5px">Dois contratos já estão <b>quitados e ainda não produzidos</b>: Simony
    (R$ 34 mil, integralmente por fabricar) e Tania (R$ 8,5 mil, já entregue).</p></div>
  <div class="note warn"><div class="nt">Pontos de atenção</div>
    <ul>
      <li><b>Setembro concentra 78% da produção do mês por fazer</b> — R$ 311,2 mil em cinco semanas.</li>
      <li><b>Jairo e Flavia entraram com 100% a produzir</b>, sem nenhuma etapa iniciada.</li>
      <li><b>André / Alphaville — R$ 87 mil</b> entregue, com cobrança integralmente em aberto e sem data. Não integra esta carteira.</li>
      <li>Os percentuais de produção vêm da <b>última conferência de fábrica</b> e precisam de atualização semanal.</li>
    </ul></div>
</div>""")

# ── 08 pipeline
page('Parte I · A Empresa Hoje', 'Pipeline · posição de 25/07/2026', 'O que está em negociação',
     'R$ 1,06 milhão em conversas abertas, fora dos 17 contratos em conclusão. Levantamento de 25 de julho, ainda não reconferido.',
     """
<div class="kpis k3">
  <div class="kpi b"><div class="kl">Pipeline total</div><div class="kv"><small>R$</small> 1,06<small> mi</small></div><div class="kd">Fora da carteira em conclusão de R$ 758,4 mil</div></div>
  <div class="kpi e"><div class="kl">Fase final de negociação</div><div class="kv"><small>R$</small> 240<small> mil</small></div><div class="kd">Alta probabilidade de conversão</div></div>
  <div class="kpi a"><div class="kl">Duas contas grandes</div><div class="kv"><small>R$</small> 820<small> mil</small></div><div class="kd">Construtora e condomínio · ciclo mais longo</div></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Fase final de negociação</span><span class="ct">alta probabilidade · R$ 240 mil</span></div>
<table>
  <thead><tr><th style="width:34%">Conta</th><th class="num" style="width:14%">Valor</th><th>Situação</th></tr></thead>
  <tbody>
    <tr><td class="nm">Juliana</td><td class="num sub">R$ 120.000</td><td>Maior valor individual do bloco de conversão próxima.</td></tr>
    <tr><td class="nm">Marcelo Tolentino</td><td class="num sub">R$ 85.000</td><td>Negociação avançada.</td></tr>
    <tr><td class="nm">Cristiane</td><td class="num sub">R$ 35.000</td><td>Ampliação de escopo sobre projeto já em execução na carteira.</td></tr>
    <tr class="tot"><td>Subtotal em fase final</td><td class="num">R$ 240.000</td><td></td></tr>
  </tbody>
</table>

<div class="sec"><span class="bar"></span><span class="tx">Contas mais expressivas</span><span class="ct">R$ 820 mil · ciclo mais longo</span></div>
<div class="cards c2">
  <div class="card gold"><div class="ct">Construtora · Lagoa Santa</div><h4>Junior</h4><div class="cv">R$ 370.000</div>
    <p>Proposta <b>aprovada verbalmente</b>, pendente de alinhamento da forma de pagamento. O porte das
    casas que a construtora entrega é um perfil interessante para a Valvic — abre a porta para
    recorrência, não só para um projeto.</p></div>
  <div class="card gold"><div class="ct">Alphaville Vespasiano</div><h4>Fábio &amp; Quênia</h4><div class="cv">R$ 450.000</div>
    <p>Cliente <b>mais focado na experiência de recebimento do que no valor</b>. O contato é difícil e a
    conta exige acompanhamento de perto — é o maior valor isolado do pipeline.</p></div>
</div>

<div class="band mt">
  <div><div class="bl">Carteira + pipeline</div><div class="bv">R$ 1,82 mi</div></div>
  <div class="br">R$ 758,4 mil já contratados e em conclusão, somados a <b>R$ 1,06 milhão em negociação</b>.
    O pipeline sozinho supera em <b>1,4×</b> tudo o que a empresa tem hoje na fábrica — e é isso que
    dimensiona a urgência da estrutura descrita na Parte II.</div>
</div>

<div class="note mt"><div class="nt">O que esse número significa para a decisão</div>
  <p>A carteira atual já tem <b>R$ 497 mil por fabricar</b> — dois terços do que foi vendido. Se apenas os
  <b>R$ 240 mil em fase final</b> se converterem, a fábrica precisa absorver isso em cima de uma fila que já
  está cheia. Se as duas contas grandes entrarem, o volume ultrapassa o teto físico do galpão atual — que é
  exatamente a conversa da Parte V.</p></div>""")

# ═══════════════════════════════════════════ PARTE II

full("""
<div class="part">
  <div class="pnum">II</div>
  <div class="plabel">Parte dois</div>
  <h2>Estrutura &amp; Pessoas</h2>
  <p class="pintro">Quem faz a operação girar, quanto custa e onde o trabalho converge. Hoje a empresa
    tem dez profissionais ativos além dos dois sócios, com mais duas entradas já datadas — e os dois
    sócios atravessam quase toda a cadeia de valor, acumulando ao mesmo tempo a função de gestor e a de executor.</p>
  <div class="plist">
    <div class="pli"><b>10</b><span>Organograma e carga operacional dos sócios</span></div>
    <div class="pli"><b>11</b><span>Quadro de pessoal e folha mensal</span></div>
    <div class="pli"><b>12</b><span>Estrutura de demandas — o que existe, entra e falta</span></div>
    <div class="pli"><b>13</b><span>Fluxo de trabalho — posição e impacto</span></div>
  </div>
</div>""")

# ── 10 organograma
page('Parte II · Estrutura & Pessoas', 'Organograma · posição agosto/2026', 'Onde tudo converge',
     'A estrutura de pessoal e a carga que recai sobre cada sócio — sem camada de gestão intermediária entre a direção e a execução.',
     """
<div class="kpis k4">
  <div class="kpi a"><div class="kl">Equipe total</div><div class="kv">10<small> ativos</small></div><div class="kd">Fora os 2 sócios · 2 entradas datadas e 4 a 5 a contratar</div></div>
  <div class="kpi c"><div class="kl">Convergem em Paulo</div><div class="kv">7</div><div class="kd">Deivson, Joelson, Filipe, Hugo, Karla, Bruna e Jennifer</div></div>
  <div class="kpi b"><div class="kl">Convergem em Jonathan</div><div class="kv">4<small> + clientes</small></div><div class="kd">Bruna, Deivson e Jennifer já ativos · Karla entra dia 10</div></div>
  <div class="kpi d"><div class="kl">Custo · estrutura completa</div><div class="kv"><small>R$</small> 62,9<small> mil</small></div><div class="kd">Hoje R$ 55,2 mil — inclui pró-labore e benefícios</div></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">A carga de cada sócio</span><span class="ct">ambos executam e gerenciam ao mesmo tempo</span></div>
<div class="two">
  <div class="card gold"><div class="ct">Sócio · pró-labore R$ 10.000</div><h4>Jonathan — Diretor Comercial &amp; Experiência</h4>
    <ul>
      <li><b>Comercial e fechamento</b> — toda a venda passa por ele</li>
      <li><b>Relacionamento</b> com cliente e parceiro (arquitetas e decoradoras)</li>
      <li><b>Administrativo</b> — interino, até a Karla assumir no dia 10</li>
      <li><b>Jurídico</b> (aciona advogado) e <b>contábil</b> (aciona contador)</li>
      <li><b>Suporte pontual à produção</b></li>
      <li><b>Pós-venda</b> — permanente, mesmo depois da contratação</li>
      <li><b>Visão e expansão</b></li>
    </ul>
    <p style="margin-top:6px"><b>4 pessoas sob gestão + toda a carteira de clientes.</b></p></div>
  <div class="card gold"><div class="ct">Sócio · pró-labore R$ 10.000</div><h4>Paulo — Diretor de Operações &amp; Tecnologia</h4>
    <ul>
      <li><b>Programação CNC</b> — o digital da produção</li>
      <li><b>Suporte total à produção</b></li>
      <li><b>Manutenção de máquinas</b></li>
      <li><b>Compras</b> — insumos e técnicas</li>
      <li><b>Captação de mão de obra</b></li>
      <li><b>Escalonamento técnico</b> da equipe</li>
    </ul>
    <p style="margin-top:6px"><b>7 pessoas sob gestão direta ou dupla checagem técnica.</b></p>
    <p style="margin-top:4px">Recrutamento e desligamento são <b>decisão conjunta</b> dos dois.</p></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Leitura da estrutura</span></div>
<p class="t">Toda a operação converge para dois pontos. <b>Quatro pessoas respondem aos dois sócios ao mesmo
tempo</b> — Karla, Bruna, Deivson e Jennifer — e é aí que a coordenação entre eles vira pré-requisito, não
preferência. Jonathan sustenta sozinho todo o comercial, administrativo, jurídico e contábil, e ainda
absorve o pós-venda de forma permanente.</p>
<p class="t">O próprio <b>Deivson acumula funções</b>: é Coordenador de Produção, mas atua na prática como
Marceneiro Sênior — justamente porque a bancada está curta. As contratações abertas (marceneiro
experiente, ajudantes e operador de CNC) existem para <b>liberar o Deivson para coordenar em vez de
operar</b> e o Joelson para migrar às máquinas novas.</p>
<p class="t"><b>Nenhum dos dois sócios tem hoje uma camada de gestão intermediária plena entre si e a
execução.</b> Qualquer ausência de um deles trava o fluxo — é o risco estrutural que a página seguinte
quantifica em folha e a página 13 destrincha por etapa.</p>""")

# ── 11 folha
page('Parte II · Estrutura & Pessoas', 'Folha mensal · dado de remuneração', 'Quadro de pessoal e custo',
     'Cada pessoa da estrutura, com vínculo, fixo mensal e variável — e o que ainda falta contratar.',
     """
<table class="tight">
  <thead><tr><th style="width:20%">Colaborador</th><th style="width:26%">Função</th>
    <th style="width:9%">Vínculo</th><th class="num" style="width:12%">Fixo mensal</th>
    <th>Variável / comissão</th></tr></thead>
  <tbody>
    <tr class="sec2"><td colspan="5">Direção · sócios</td></tr>
    <tr><td class="nm">Jonathan</td><td>Diretor Comercial &amp; Experiência</td><td><span class="badge b-soc">Sócio</span></td><td class="num sub">10.000</td><td class="dt">pró-labore</td></tr>
    <tr><td class="nm">Paulo</td><td>Diretor de Operações &amp; Tecnologia</td><td><span class="badge b-soc">Sócio</span></td><td class="num sub">10.000</td><td class="dt">pró-labore</td></tr>
    <tr class="sec2"><td colspan="5">Ativos hoje</td></tr>
    <tr><td class="nm">Deivson</td><td>Coordenador de Produção</td><td><span class="badge b-pj">PJ</span></td><td class="num sub">4.000</td><td class="dt">2,5% fabricação + 2,5% montagem + 1,0% coordenação</td></tr>
    <tr><td class="nm">Samuel</td><td>Marceneiro Sênior</td><td><span class="badge b-pj">PJ</span></td><td class="num sub">3.900</td><td class="dt">2,5% fabricação + 2,5% montagem</td></tr>
    <tr><td class="nm">Jackson</td><td>Marceneiro Pleno</td><td><span class="badge b-pj">PJ</span></td><td class="num sub">3.600</td><td class="dt">2,5% fabricação + 2,5% montagem</td></tr>
    <tr><td class="nm">Filipe</td><td>Programador CNC</td><td><span class="badge b-pj">PJ</span></td><td class="num sub">3.600</td><td class="dt">sem comissão</td></tr>
    <tr><td class="nm">Joelson</td><td>Operador CNC &amp; máquinas</td><td><span class="badge b-clt">CLT</span></td><td class="num sub">2.500</td><td class="dt">2,5% montagem + R$ 2,00/chapa cortada · VR 400 + VT 400</td></tr>
    <tr><td class="nm">Jomar</td><td>Marceneiro</td><td><span class="badge b-clt">CLT</span></td><td class="num sub">1.950</td><td class="dt">sem comissão · VR 400 + VT 400</td></tr>
    <tr><td class="nm">Davi</td><td>Ajudante</td><td><span class="badge b-clt">CLT</span></td><td class="num sub">1.950</td><td class="dt">sem comissão · VR 400 + VT 400</td></tr>
    <tr><td class="nm">Jonathan Godoy</td><td>Ajudante Geral · novo</td><td><span class="badge b-clt">CLT</span></td><td class="num sub">1.621</td><td class="dt">salário mínimo · sem comissão · VR 400 + VT 400</td></tr>
    <tr><td class="nm">Bruna<span class="fn">iniciou este mês</span></td><td>Arquiteta · programação + projetos</td><td><span class="badge b-pj">PJ</span></td><td class="num sub">4.000</td><td class="dt">50% dos projetos vendidos aos clientes que ela atende</td></tr>
    <tr><td class="nm">Cezar<span class="fn">iniciou este mês</span></td><td>Marceneiro</td><td><span class="badge b-clt">CLT</span></td><td class="num sub">2.900</td><td class="dt">2,5% fabricação + 2,5% montagem · VR 400 + VT 400</td></tr>
    <tr class="sec2"><td colspan="5">Entradas com data definida</td></tr>
    <tr><td class="nm">Karla<span class="fn">dia 10 deste mês</span></td><td>Assistente Operacional</td><td><span class="badge b-new">CLT</span></td><td class="num sub">2.000</td><td class="dt">VR 500 + transporte conforme local · progride a 3.200</td></tr>
    <tr><td class="nm">Hugo<span class="fn">dia 01 do mês que vem</span></td><td>Programador<span class="fn">função-chave · atravessa toda a operação</span></td><td><span class="badge b-new">CLT</span></td><td class="num sub">4.000</td><td class="dt">sem comissão · VR 400 + VT 400</td></tr>
    <tr class="sec2"><td colspan="5">Parceria externa</td></tr>
    <tr><td class="nm">Jennifer</td><td>Social media</td><td><span class="badge b-ext">Ext.</span></td><td class="num sub">1.400</td><td class="dt">contrato à parte · fora da folha</td></tr>
    <tr class="tot"><td colspan="3">Custo da estrutura completa · a partir da entrada do Hugo, dia 01 do mês que vem</td><td class="num">62.920</td><td></td></tr>
    <tr class="sec2"><td colspan="5">Necessidade de contratação — fora do número acima</td></tr>
    <tr><td class="nm">Paulo &quot;Baiano&quot;</td><td>Marceneiro experiente</td><td><span class="badge b-pj">PJ</span></td><td class="num sub">3.900</td><td class="dt">mesmo escopo do Samuel · 2,5% + 2,5%</td></tr>
    <tr><td class="nm">2 a 3 ajudantes</td><td>Apoio à produção · maior lacuna</td><td><span class="badge b-clt">CLT</span></td><td class="num sub">1.950<span class="fn">cada</span></td><td class="dt">sem comissão · VR 400 + VT 400 cada</td></tr>
    <tr><td class="nm">1 operador CNC</td><td>Assume a máquina atual</td><td><span class="badge b-clt">CLT</span></td><td class="num sub">2.500</td><td class="dt">sem comissão · VR 400 + VT 400</td></tr>
    <tr class="enc"><td colspan="3">Subtotal a contratar</td><td class="num">12.550 a 15.250</td><td class="dt" style="color:#96803f">Baiano + 2–3 ajudantes + operador CNC</td></tr>
  </tbody>
</table>

<div class="two mt">
  <div class="note"><div class="nt">Progressão validada da Karla</div>
    <p><b>1º ao 3º mês</b> R$ 2.000 &nbsp;·&nbsp; <b>3º ao 6º</b> R$ 2.500 &nbsp;·&nbsp;
    <b>6 meses a 1 ano</b> R$ 2.800 &nbsp;·&nbsp; <b>a partir de 1 ano</b> R$ 3.200.
    Cada degrau só avança por entrega validada, não por tempo de casa.</p></div>
  <div class="note blue"><div class="nt">Regra de comissão</div>
    <p>Por <b>profissional e por etapa</b>, não por dupla: 2,5% por fabricação e 2,5% por montagem, pagas
    conforme a etapa executada; o coordenador acrescenta 1,0%. <b>Só existem quando há venda</b> — são
    custo variável, não folha fixa. Base: faturamento bruto.</p>
    <p style="margin-top:5px">Sobre a carteira em conclusão de R$ 758,4 mil, a comissão estimada dos dois
    meses é de <b>R$ 45,5 mil</b>.</p></div>
</div>""")

# ── 12 demandas
page('Parte II · Estrutura & Pessoas', 'Estrutura de demandas · pessoas e infraestrutura', 'O que existe, o que entra e o que falta',
     'Toda a demanda abaixo existe para dar vazão à capacidade que as máquinas novas vão exigir — sem ela, o investimento em máquina não converte em entrega.',
     """
<div class="band" style="padding:10px 15px">
  <div><div class="bl">Contexto · ≈ 3 meses</div><div class="bv" style="font-size:20px">Novo galpão</div></div>
  <div class="br">Com <b>coladeira</b> e <b>centro de furação</b> novos. A equipe precisa estar formada e
    treinada <b>antes</b> da mudança — máquina parada por falta de gente é o pior dos cenários.</div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Como a estrutura está dividida</span></div>
<div class="cards c3">
  <div class="card ok"><div class="ct">Ativo hoje · 10 pessoas</div><h4>Chão de fábrica, tecnologia e 3 duplas completas</h4>
    <ul>
      <li><b>Montagem:</b> Samuel/Jomar, Jackson/Davi e Cezar/J. Godoy — as três duplas fechadas</li>
      <li><b>Chão de fábrica:</b> Deivson, o único no nível de marceneiro sênior</li>
      <li><b>Tecnologia:</b> Joelson (operação), Filipe (programação) e Bruna (projeto e programação)</li>
    </ul></div>
  <div class="card blue"><div class="ct">Entradas com data definida · 2 pessoas</div><h4>Já contratadas, ainda não em posto</h4>
    <ul>
      <li><b>Karla · dia 10 deste mês</b> — assume administrativo, jurídico e contábil e libera o Jonathan para vender</li>
      <li><b>Hugo · dia 01 do mês que vem</b> — programador; segunda pessoa em programação ao lado do Filipe</li>
    </ul>
    <p style="margin-top:6px"><b>Bruna e Cezar já entraram</b> neste mês — a arquiteta em projeto e programação, e o Cezar fechando a terceira dupla de montagem.</p></div>
  <div class="card warn"><div class="ct">A contratar · 4 a 5 pessoas</div><h4>O que ainda falta</h4>
    <ul>
      <li><b>1 marceneiro experiente</b> — alvo Paulo &quot;Baiano&quot;, em negociação; não sendo ele, perfil equivalente</li>
      <li><b>2 a 3 ajudantes</b> — a maior lacuna da operação</li>
      <li><b>1 operador CNC</b> — assume a máquina atual e libera o Joelson</li>
    </ul></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Sequência de entrada</span><span class="ct">o que destrava o quê</span></div>
<table class="tight">
  <thead><tr><th style="width:14%">Quando</th><th style="width:30%">O que entra</th><th>O que isso destrava</th></tr></thead>
  <tbody>
    <tr><td class="nm">Este mês<span class="fn">já ocorrido</span></td><td>Bruna e Cezar entraram</td><td>Bruna alivia o Filipe e o comercial em projeto e programação; Cezar <b>fecha a terceira dupla</b> de montagem ao lado do Godoy</td></tr>
    <tr><td class="nm">Dia 10<span class="fn">deste mês</span></td><td>Karla entra</td><td>Assume administrativo, jurídico e contábil e <b>libera o Jonathan para vender</b></td></tr>
    <tr><td class="nm">Dia 01<span class="fn">do mês que vem</span></td><td>Hugo entra</td><td>Programador — <b>elimina o ponto único na programação</b> e sustenta o volume que as máquinas novas vão exigir</td></tr>
    <tr><td class="nm">Curto prazo</td><td>4 a 5 contratações + ferramental</td><td>Marceneiro experiente, 2–3 ajudantes, operador CNC, 2 carros e 3 kits de ferramenta</td></tr>
    <tr><td class="nm">≈ 3 meses</td><td>Novo galpão</td><td>Coladeira e centro de furação — <b>exigem a equipe já formada e treinada</b></td></tr>
  </tbody>
</table>

<div class="sec"><span class="bar"></span><span class="tx">Investimento em infraestrutura</span><span class="ct">custo único</span></div>
<table class="tight">
  <thead><tr><th style="width:34%">Item</th><th style="width:36%">Para quem</th><th class="num" style="width:14%">Valor</th></tr></thead>
  <tbody>
    <tr><td class="nm">Cadeira + computador</td><td>Bruna</td><td class="num sub">4.000<span class="fn">cadeira a definir</span></td></tr>
    <tr><td class="nm">Kit de ferramentas</td><td>Paulo &quot;Baiano&quot;</td><td class="num sub">3.000</td></tr>
    <tr><td class="nm">Kit equipe de obra</td><td>Duplas de montagem</td><td class="num sub">6.000<span class="fn">varia com o nível definido</span></td></tr>
    <tr><td class="nm">Kit básico</td><td>Davi e Jonathan Godoy · R$ 1.000 cada</td><td class="num sub">2.000</td></tr>
    <tr><td class="nm">Cadeira + celular</td><td>Karla</td><td class="num sub">a definir</td></tr>
    <tr><td class="nm">2 carros</td><td>Duplas 2 e 3 — hoje sem veículo</td><td class="num sub">a definir</td></tr>
    <tr class="tot"><td colspan="2">Subtotal mapeado · carros e mobiliário em aberto</td><td class="num">15.000</td></tr>
  </tbody>
</table>

<div class="note warn mt"><div class="nt">O que já limita o ritmo atual</div>
  <p><b>2 das 3 duplas não têm veículo</b> e todas operam com ferramental parcial. Isso restringe a
  produção de hoje, antes mesmo de qualquer máquina nova entrar. O Joelson precisa de
  <b>treinamento urgente</b> no maquinário novo, e só pode ser liberado quando houver um operador
  formado para assumir a CNC atual.</p></div>""")

# ── 13 fluxo
FLOW = [
    ('01', 'Comercial &amp; Venda', 'contato → orçamento → contrato',
     '<b>Jonathan</b> (sócio) · <b>Karla</b> assist. operacional (entra dia 10) · <b>Jennifer</b> social media (externa)',
     'Escopo de Venda + projeto atualizado, contrato e cadastro no Calcme',
     'Define <b>escopo, preço e margem</b>. Informação incompleta aqui contamina toda a cadeia.',
     'Jonathan sozinho até a Karla entrar'),
    ('02', 'Projeto &amp; Programação', 'conferência técnica → CNC',
     '<b>Paulo</b> (sócio) · <b>Filipe</b> programador CNC · <b>Bruna</b> arquiteta · <b>Hugo</b> programador (entra dia 01/09) · <b>Deivson</b> olhar de produção',
     'Arquivos de corte no Drive + plano de produção validado',
     'Converte a venda em <b>arquivo de corte</b>. Define aproveitamento de chapa e retrabalho.',
     'Ainda sem folga: a Bruna já entrou, mas a redundância plena só vem com o Hugo'),
    ('03', 'Compras &amp; Recepção', 'insumos → conferência → estoque',
     '<b>Jonathan</b> e <b>Paulo</b> · <b>Karla</b> cotação e faturamento (entra dia 10) · <b>Deivson</b> recepção · <b>Joelson</b> separação',
     'Insumos conferidos, alocados no projeto e baixados no pedido',
     'Garante o <b>material certo na hora certa</b>. Falha aqui para a fábrica inteira.', None),
    ('04', 'Fabricação', 'corte → montagem de fábrica',
     '<b>Paulo</b> (sócio) · <b>Joelson</b> operador CNC · <b>Deivson</b> coord. + marceneiro · <b>Baiano</b>, <b>2–3 ajudantes</b> e <b>+1 operador CNC</b> a contratar',
     'Peças no padrão, conferidas pelo POP de qualidade e embaladas',
     'Transforma chapa em peça <b>no padrão</b>. Define qualidade e prazo de entrega.',
     'Maior lacuna — Deivson opera em vez de coordenar; Joelson sem backup na CNC'),
    ('05', 'Montagem &amp; Entrega', 'obra → vistoria → aceite',
     '<b>Jonathan</b> e <b>Paulo</b> · Samuel/Jomar (com carro) · Jackson/Davi (sem carro) · Cezar/J. Godoy (sem carro) · <b>2 carros e 3 kits</b> a adquirir',
     'Vistoria + aceite assinado pelo cliente',
     'É <b>o que o cliente vê e sente</b>. Define a percepção da marca e o aceite.',
     '2 das 3 duplas sem veículo · ferramental parcial'),
    ('06', 'Pós-venda', 'garantia → recompra',
     '<b>Jonathan</b> (permanente) · <b>Karla</b> registro e acionamento · duplas de montagem em assistência técnica',
     'Chamado registrado e garantia acionada quando necessário',
     'Sustenta a <b>garantia de 10 anos</b>, a recompra e a indicação — a receita mais barata.', None),
]
fl = ''.join(
    f'<div class="fst"><div class="fn2">{s[0]}</div>'
    f'<div><div class="fnm">{s[1]}</div><div class="fwho" style="font-size:7.4px;color:#8a94a0">{s[2]}</div>'
    f'<div class="fwho">{s[3]}</div></div>'
    f'<div><div class="fh">Entrega para a etapa seguinte</div><div class="fv2">{s[4]}</div></div>'
    f'<div><div class="fh">Impacto</div><div class="fv2">{s[5]}</div>'
    + (f'<span class="risk">⚠ {s[6]}</span>' if s[6] else '') +
    '</div></div>' for s in FLOW)

page('Parte II · Estrutura & Pessoas', 'Cadeia de valor · posição agosto/2026', 'Fluxo de trabalho — posição e impacto',
     'As seis etapas do primeiro contato ao pós-venda: quem atua, o que passa adiante e o que cada etapa define no resultado.',
     f"""
<div class="kpis k4" style="margin-bottom:5mm">
  <div class="kpi b"><div class="kl">Jonathan atravessa</div><div class="kv">5<small> de 6 etapas</small></div><div class="kd">Sem substituto em nenhuma delas</div></div>
  <div class="kpi c"><div class="kl">Paulo atravessa</div><div class="kv">4<small> de 6 etapas</small></div><div class="kd">Projeto → compras → fabricação → montagem</div></div>
  <div class="kpi a"><div class="kl">Demais colaboradores</div><div class="kv">1<small> a 2 etapas</small></div><div class="kd">Cada um na sua especialidade</div></div>
  <div class="kpi f"><div class="kl">Etapas com risco</div><div class="kv">3</div><div class="kd">Projeto, fabricação e montagem</div></div>
</div>
<div class="flow">{fl}</div>

<div class="note warn mt"><div class="nt">Leitura do fluxo</div>
  <p>O fluxo mostra por que a estrutura é frágil hoje: <b>os dois sócios atravessam quase toda a cadeia</b>
  enquanto cada colaborador ocupa apenas uma ou duas etapas. Nenhuma etapa avança sem passar por um deles,
  e qualquer ausência trava o fluxo inteiro. As entradas já alinhadas atacam justamente as pontas —
  Karla nas etapas 1, 3 e 6; Bruna e Hugo dando redundância à programação, hoje ainda concentrada no Filipe.
  O centro da cadeia, <b>a fabricação, segue sendo a maior lacuna</b>.</p></div>""")

# ═══════════════════════════════════════════ PARTE III

full("""
<div class="part">
  <div class="pnum">III</div>
  <div class="plabel">Parte três</div>
  <h2>Economia da Operação</h2>
  <p class="pintro">Por que uma estrutura majoritariamente fixa transforma cada real adicional de
    faturamento em resultado desproporcional — e quanto custa, hoje, manter essa estrutura de pé.
    A margem já é conhecida e boa; o que limita o resultado é a quantidade de projetos.</p>
  <div class="plist">
    <div class="pli"><b>15</b><span>Modelo econômico e alavancagem operacional</span></div>
    <div class="pli"><b>16</b><span>Custo fixo da operação</span></div>
    <div class="pli"><b>17</b><span>Folha e estrutura, item a item</span></div>
    <div class="pli"><b>18</b><span>Fluxo de caixa — agosto e setembro</span></div>
  </div>
</div>""")

# ── 15 modelo econômico
page('Parte III · Economia da Operação', 'Modelo econômico · jun/2026', 'Alavancagem operacional',
     'A estrutura é majoritariamente fixa. Depois de cobrir o custo fixo, cada real adicional converte cerca de 34 centavos direto em resultado.',
     """
<p class="lead2">As mesmas máquinas, o mesmo galpão e a mesma equipe-base atendem um volume bem maior
que o atual. É a definição de <b>alavancagem operacional</b> — e a Valvic está sentada sobre
<b>capacidade ociosa</b>. A capacidade custa o mesmo cheia ou vazia, porque o custo fixo já está pago.</p>

<div class="sec mt"><span class="bar"></span><span class="tx">O que cada nível de volume gera</span><span class="ct">MC líquida de 34% · estrutura atual</span></div>
<table>
  <thead><tr><th style="width:34%">Faturamento / mês</th><th class="num" style="width:20%">Margem gerada</th>
    <th class="num" style="width:22%">Resultado / mês</th><th class="num" style="width:24%">Resultado / ano</th></tr></thead>
  <tbody>
    <tr><td class="nm">~R$ 163k<span class="fn">posição de referência · capacidade ociosa</span></td><td class="num">R$ 55k</td><td class="num" style="color:#6c7785">limiar</td><td class="num" style="color:#6c7785">—</td></tr>
    <tr><td class="nm">R$ 246k<span class="fn">ponto de equilíbrio</span></td><td class="num">R$ 84k</td><td class="num sub">R$ 0</td><td class="num" style="color:#6c7785">break-even</td></tr>
    <tr><td class="nm">R$ 300k</td><td class="num">R$ 102k</td><td class="num sub">+R$ 18,5k</td><td class="num sub">+R$ 222k</td></tr>
    <tr><td class="nm">R$ 400k<span class="fn">meta Fase 1 — dobrar</span></td><td class="num">R$ 136k</td><td class="num sub">+R$ 52,5k</td><td class="num sub">+R$ 630k</td></tr>
    <tr><td class="nm">R$ 600k</td><td class="num">R$ 204k</td><td class="num sub">+R$ 120k</td><td class="num sub">+R$ 1,4 mi</td></tr>
    <tr class="tot"><td>R$ 1.000k — visão (Fase 2)</td><td class="num">R$ 340k</td><td class="num">+R$ 256k</td><td class="num">+R$ 3,1 mi</td></tr>
  </tbody>
</table>
<p class="t mts">Até cerca de <b>R$ 400k/mês a estrutura atual absorve o volume</b> com custo fixo praticamente
constante. De R$ 400k a R$ 1 mi, a Fase 2 — novas máquinas e galpão — adiciona capacidade. É exatamente
onde o capital de um sócio investidor é aplicado.</p>

<div class="sec"><span class="bar"></span><span class="tx">O encaixe · o que cada lado traz</span></div>
<table class="tight">
  <thead><tr><th style="width:44%">A Valvic já tem</th><th>O sócio aporta</th></tr></thead>
  <tbody>
    <tr><td class="nm">Capacidade instalada e paga</td><td>Capital para a Fase 2 — novas máquinas e galpão — que eleva o teto de R$ 400k para R$ 1 mi/mês</td></tr>
    <tr><td class="nm">Operação que sabe entregar</td><td>Pipeline e demanda — o insumo que falta para encher a capacidade ociosa</td></tr>
    <tr><td class="nm">Margem saudável e conhecida</td><td>Capital de giro para subsidiar orçamentos e acelerar o ciclo comercial</td></tr>
  </tbody>
</table>

<div class="two mt">
  <div class="note ok"><div class="nt">O que isto é</div>
    <p>Uma <b>aposta em volume e escala</b> — o terreno onde capital e pipeline rendem mais. E a entrada
    numa empresa que <b>já cresce, já produz e já tem marca</b>, para acelerar o que funciona.</p>
    <p style="margin-top:5px">O caminho: manter o <b>bespoke premium</b> (marca e margem) e abrir uma
    <b>linha modular</b> para incorporação e construtora, que absorve volume — duas pistas, sem trair a identidade.</p></div>
  <div class="note warn"><div class="nt">Divergência de premissa · sinalizada, não resolvida</div>
    <p>Este modelo usa <b>margem de contribuição de 43,5%</b> (34% líquida). O Plano de Expansão da Parte V
    trabalha com <b>MC de ~30%</b> — premissa mais conservadora, adotada para o cálculo de payback.</p>
    <p style="margin-top:5px">As duas referências convivem neste caderno porque vêm de estudos distintos.
    <b>Qualquer decisão de aporte deve fixar uma única premissa</b>, validada com o contador.</p></div>
</div>""")

# ── 16 custo fixo da operação
page('Parte III · Economia da Operação', 'Custo fixo · agosto e setembro de 2026', 'O que custa manter a operação',
     'As duas contas que existem independentemente de vender: a folha de pagamento e a estrutura. Juntas somam R$ 152,2 mil nos dois meses.',
     """
<div class="kpis k4">
  <div class="kpi a"><div class="kl">Custo fixo · agosto</div><div class="kv"><small>R$</small> 75,1<small> mil</small></div><div class="kd">Folha R$ 57,8k + estrutura R$ 17,3k</div></div>
  <div class="kpi b"><div class="kl">Custo fixo · setembro</div><div class="kv"><small>R$</small> 77,2<small> mil</small></div><div class="kd">Folha R$ 62,6k + estrutura R$ 14,6k · com o Hugo</div></div>
  <div class="kpi e"><div class="kl">Peso da folha</div><div class="kv">81%</div><div class="kd">Do custo fixo total · 19% é instalação e administrativo</div></div>
  <div class="kpi f"><div class="kl">Ainda a contratar</div><div class="kv"><small>R$</small> 12,6<small>–15,3 mil</small></div><div class="kd">Baiano + 2–3 ajudantes + operador CNC · fora do número acima</div></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Composição do custo fixo</span><span class="ct">valores em reais</span></div>
<table>
  <thead><tr><th style="width:40%">Bloco</th><th class="num" style="width:16%">Agosto</th>
    <th class="num" style="width:16%">Setembro</th><th class="num" style="width:14%">Peso</th>
    <th style="width:14%">Natureza</th></tr></thead>
  <tbody>
    <tr><td class="nm">Folha de pagamento<span class="fn">salários, adiantamentos, pró-labore, benefícios e contratos PJ</span></td>
      <td class="num">57.786</td><td class="num sub">62.586</td><td class="num dt">81%</td><td class="dt">Fixo</td></tr>
    <tr><td class="nm">Estrutura<span class="fn">galpão, energia, contador, software, logística e marketing</span></td>
      <td class="num">17.280</td><td class="num sub">14.580</td><td class="num dt">19%</td><td class="dt">Fixo</td></tr>
    <tr class="tot"><td>Custo fixo total</td><td class="num">75.066</td><td class="num">77.166</td><td class="num">100%</td><td></td></tr>
    <tr class="enc"><td>Necessidades de contratação — ainda fora do cálculo</td><td class="num" colspan="2">12.550 a 15.250</td>
      <td class="dt" colspan="2" style="color:#96803f">Elevaria o custo fixo a R$ 89,7–92,4 mil</td></tr>
  </tbody>
</table>

<div class="sec"><span class="bar"></span><span class="tx">Natureza do vínculo</span><span class="ct">a estrutura é mista por desenho</span></div>
<div class="cards c3">
  <div class="card"><div class="ct">PJ · produção e tecnologia</div><h4>Deivson, Samuel, Jackson, Filipe, Bruna</h4>
    <p>Os papéis de <b>maior autonomia técnica</b> e remuneração variável relevante. Comissionados por etapa executada.</p></div>
  <div class="card"><div class="ct">CLT · formação, apoio e programação</div><h4>Joelson, Jomar, Davi, J. Godoy, Cezar, Karla, Hugo</h4>
    <p>Funções de <b>formação, apoio e programação</b>, com benefícios fixos: <b>R$ 800/mês</b> (VR 400 + VT 400) na
    produção e VR 500 mais transporte para a Karla.</p></div>
  <div class="card"><div class="ct">Variável · só existe com venda</div><h4>Comissões e participação</h4>
    <p>2,5% fabricação + 2,5% montagem por profissional, 1,0% de coordenação para o Deivson e R$ 2,00/chapa para
    o Joelson. A Bruna tem <b>50% dos projetos que vender</b>. <b>Nada disso é folha fixa.</b></p></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Investimento em infraestrutura</span><span class="ct">custo único, fora do fixo mensal</span></div>
<table class="tight">
  <thead><tr><th style="width:36%">Item</th><th style="width:44%">Para quem</th><th class="num" style="width:20%">Valor</th></tr></thead>
  <tbody>
    <tr><td class="nm">Cadeira + computador</td><td>Bruna</td><td class="num sub">4.000<span class="fn">cadeira a definir</span></td></tr>
    <tr><td class="nm">Kit de ferramentas</td><td>Marceneiro experiente a contratar</td><td class="num sub">3.000</td></tr>
    <tr><td class="nm">Kit equipe de obra</td><td>Duplas de montagem</td><td class="num sub">6.000</td></tr>
    <tr><td class="nm">Kit básico</td><td>Davi e Jonathan Godoy · R$ 1.000 cada</td><td class="num sub">2.000</td></tr>
    <tr><td class="nm">2 carros</td><td>Duplas 2 e 3 — hoje sem veículo</td><td class="num sub">a definir</td></tr>
    <tr class="tot"><td colspan="2">Subtotal mapeado · carros e mobiliário em aberto</td><td class="num">15.000</td></tr>
  </tbody>
</table>""")

# ── 17 folha e estrutura, item a item
page('Parte III · Economia da Operação', 'Custo fixo · detalhamento', 'Folha e estrutura, item a item',
     'Cada pessoa e cada rubrica que compõem os R$ 77,2 mil de custo fixo mensal.',
     """
<div class="sec"><span class="bar"></span><span class="tx">Folha de pagamento</span><span class="ct">custo total por pessoa · fixo + benefícios</span></div>
<table class="xt">
  <thead><tr><th style="width:24%">Pessoa</th><th style="width:32%">Função</th><th style="width:11%">Vínculo</th>
    <th class="num" style="width:16%">Agosto</th><th class="num" style="width:17%">Setembro</th></tr></thead>
  <tbody>
    <tr><td class="nm">Jonathan</td><td>Diretor Comercial &amp; Experiência</td><td><span class="badge b-soc">Sócio</span></td><td class="num">10.000</td><td class="num sub">10.000</td></tr>
    <tr><td class="nm">Paulo</td><td>Diretor de Operações &amp; Tecnologia</td><td><span class="badge b-soc">Sócio</span></td><td class="num">10.000</td><td class="num sub">10.000</td></tr>
    <tr><td class="nm">Hugo<span class="fn">entra dia 01/09</span></td><td>Programador</td><td><span class="badge b-clt">CLT</span></td><td class="num dt">—</td><td class="num sub">4.800</td></tr>
    <tr><td class="nm">Deivson</td><td>Coordenador de Produção</td><td><span class="badge b-pj">PJ</span></td><td class="num">4.000</td><td class="num sub">4.000</td></tr>
    <tr><td class="nm">Bruna</td><td>Arquiteta · projeto e programação</td><td><span class="badge b-pj">PJ</span></td><td class="num">4.000</td><td class="num sub">4.000</td></tr>
    <tr><td class="nm">Samuel</td><td>Marceneiro Sênior</td><td><span class="badge b-pj">PJ</span></td><td class="num">3.900</td><td class="num sub">3.900</td></tr>
    <tr><td class="nm">Cezar</td><td>Marceneiro</td><td><span class="badge b-clt">CLT</span></td><td class="num">3.700</td><td class="num sub">3.700</td></tr>
    <tr><td class="nm">Jackson</td><td>Marceneiro Pleno</td><td><span class="badge b-pj">PJ</span></td><td class="num">3.600</td><td class="num sub">3.600</td></tr>
    <tr><td class="nm">Filipe</td><td>Programador CNC</td><td><span class="badge b-pj">PJ</span></td><td class="num">3.600</td><td class="num sub">3.600</td></tr>
    <tr><td class="nm">Joelson</td><td>Operador CNC &amp; máquinas</td><td><span class="badge b-clt">CLT</span></td><td class="num">3.300</td><td class="num sub">3.300</td></tr>
    <tr><td class="nm">Karla</td><td>Assistente Operacional</td><td><span class="badge b-clt">CLT</span></td><td class="num">3.050</td><td class="num sub">3.050</td></tr>
    <tr><td class="nm">Jomar</td><td>Marceneiro</td><td><span class="badge b-clt">CLT</span></td><td class="num">2.750</td><td class="num sub">2.750</td></tr>
    <tr><td class="nm">Davi</td><td>Ajudante</td><td><span class="badge b-clt">CLT</span></td><td class="num">2.750</td><td class="num sub">2.750</td></tr>
    <tr><td class="nm">Jonathan Godoy</td><td>Ajudante Geral</td><td><span class="badge b-clt">CLT</span></td><td class="num">2.421</td><td class="num sub">2.421</td></tr>
    <tr><td class="nm">INSS sobre pró-labore</td><td>Encargo dos sócios · GPS</td><td class="dt">—</td><td class="num">715</td><td class="num sub">715</td></tr>
    <tr class="tot"><td colspan="3">Total da folha · 14 pessoas em agosto, 15 em setembro</td><td class="num">57.786</td><td class="num">62.586</td></tr>
  </tbody>
</table>

<div class="sec"><span class="bar"></span><span class="tx">Custo fixo da estrutura</span><span class="ct">o que sustenta o galpão e o administrativo</span></div>
<table class="xt">
  <thead><tr><th style="width:38%">Rubrica</th><th style="width:26%">Natureza</th>
    <th class="num" style="width:18%">Agosto</th><th class="num" style="width:18%">Setembro</th></tr></thead>
  <tbody>
    <tr><td class="nm">Aluguel do galpão</td><td class="dt">Instalações</td><td class="num">4.980</td><td class="num sub">4.980</td></tr>
    <tr><td class="nm">Marketing e publicidade<span class="fn">tráfego pago + social media</span></td><td class="dt">Comercial</td><td class="num">2.300</td><td class="num sub">2.300</td></tr>
    <tr><td class="nm">Energia elétrica</td><td class="dt">Instalações</td><td class="num">1.500</td><td class="num sub">1.500</td></tr>
    <tr><td class="nm">Software e licenças</td><td class="dt">Administrativo</td><td class="num">1.430</td><td class="num sub">1.130</td></tr>
    <tr><td class="nm">Combustível</td><td class="dt">Logística</td><td class="num">750</td><td class="num sub">1.000</td></tr>
    <tr><td class="nm">Honorários contábeis</td><td class="dt">Administrativo</td><td class="num">700</td><td class="num sub">700</td></tr>
    <tr><td class="nm">Lanches e refeições da equipe</td><td class="dt">Produção</td><td class="num">600</td><td class="num sub">800</td></tr>
    <tr><td class="nm">Limpeza</td><td class="dt">Instalações</td><td class="num">600</td><td class="num sub">600</td></tr>
    <tr><td class="nm">Manutenção predial e de equipamentos</td><td class="dt">Instalações</td><td class="num">1.135</td><td class="num sub">—</td></tr>
    <tr><td class="nm">Materiais de escritório<span class="fn">cadeiras — aquisição pontual</span></td><td class="dt">Administrativo</td><td class="num">1.265</td><td class="num sub">—</td></tr>
    <tr><td class="nm">Vigilância e segurança</td><td class="dt">Instalações</td><td class="num">390</td><td class="num sub">390</td></tr>
    <tr><td class="nm">Viagens e representações</td><td class="dt">Comercial</td><td class="num">370</td><td class="num sub">370</td></tr>
    <tr><td class="nm">Seguros de veículos</td><td class="dt">Logística</td><td class="num">255</td><td class="num sub">255</td></tr>
    <tr><td class="nm">Demais rubricas<span class="fn">água, telefonia, lixo, seguro de vida, cursos, transporte urbano, carretos</span></td><td class="dt">Diversos</td><td class="num">1.006</td><td class="num sub">556</td></tr>
    <tr class="tot"><td colspan="2">Total da estrutura</td><td class="num">17.280</td><td class="num">14.580</td></tr>
  </tbody>
</table>

<div class="note ok mt"><div class="nt">O que este detalhamento mostra</div>
  <p>A operação é <b>enxuta em custo de ocupação e pesada em mão de obra qualificada</b>. O aluguel do galpão
  responde por menos de 7% do custo fixo, enquanto a folha responde por 81%. É o perfil de uma empresa que
  investe em gente, não em metro quadrado.</p></div>""")

# ── 18 fluxo de caixa
page('Parte III · Economia da Operação', 'Fluxo de caixa · agosto e setembro de 2026', 'A receber, a pagar e o que sobra',
     'O movimento dos dois meses conforme os lançamentos do sistema financeiro, e a compra de material que ainda precisa acontecer.',
     """
<div class="kpis k4">
  <div class="kpi a"><div class="kl">Total a receber</div><div class="kv"><small>R$</small> 402<small> mil</small></div><div class="kd">Parcelas em aberto com vencimento nos dois meses</div></div>
  <div class="kpi f"><div class="kl">Total a pagar</div><div class="kv"><small>R$</small> 260<small> mil</small></div><div class="kd">Folha, estrutura, material e compromissos</div></div>
  <div class="kpi e"><div class="kl">Saldo do período</div><div class="kv" style="color:#2f7d4f"><small>+R$</small> 142<small> mil</small></div><div class="kd">Antes da compra de material ainda a fazer</div></div>
  <div class="kpi c"><div class="kl">Demanda de material</div><div class="kv"><small>R$</small> 200<small> mil</small></div><div class="kd">R$ 120k em agosto + R$ 80k em setembro · estimativa</div></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Composição do total a pagar</span><span class="ct">R$ 260 mil nos dois meses</span></div>
<table>
  <thead><tr><th style="width:46%">Bloco</th><th class="num" style="width:20%">Dois meses</th>
    <th class="num" style="width:14%">Peso</th><th style="width:20%">Natureza</th></tr></thead>
  <tbody>
    <tr><td class="nm">Folha de pagamento<span class="fn">15 pessoas · salários, pró-labore, benefícios e PJ</span></td>
      <td class="num sub">120.372</td><td class="num dt">46,3%</td><td class="dt">Fixo</td></tr>
    <tr><td class="nm">Material, comissões e compromissos<span class="fn">material lançado, RT de parceiros, comissões, máquinas e dívida</span></td>
      <td class="num sub">107.767</td><td class="num dt">41,4%</td><td class="dt">Variável e parcelado</td></tr>
    <tr><td class="nm">Custo fixo da estrutura</td><td class="num sub">31.861</td><td class="num dt">12,3%</td><td class="dt">Fixo</td></tr>
    <tr class="tot"><td>Total a pagar</td><td class="num">260.000</td><td class="num">100%</td><td></td></tr>
  </tbody>
</table>

<div class="sec"><span class="bar"></span><span class="tx">A demanda de material que falta</span><span class="ct">o que ainda precisa ser comprado para concluir a produção</span></div>
<table>
  <thead><tr><th style="width:30%">Período</th><th class="num" style="width:20%">Estimativa</th><th>Base</th></tr></thead>
  <tbody>
    <tr><td class="nm">Agosto</td><td class="num sub">120.000</td><td class="dt">Produção a executar no mês: R$ 185,9 mil</td></tr>
    <tr><td class="nm">Setembro</td><td class="num sub">80.000</td><td class="dt">Produção a executar no mês: R$ 311,2 mil</td></tr>
    <tr class="enc"><td>Demanda total de material</td><td class="num">200.000</td><td class="dt" style="color:#96803f">Estimativa da direção · não é levantamento por projeto</td></tr>
  </tbody>
</table>

<div class="band mt">
  <div><div class="bl">Saldo da carteira menos o material</div><div class="bv">R$ 239,4 mil</div></div>
  <div class="br">Dos <b>R$ 439,4 mil</b> que a carteira ainda tem a receber, <b>R$ 200 mil</b> vão para a compra
    de material necessária para concluir a produção. O que resta precisa cobrir folha, estrutura e
    compromissos do período.</div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Pontos de atenção</span><span class="ct">fora do fluxo dos dois meses</span></div>
<div class="cards c3">
  <div class="card warn"><div class="ct">Aporte já consumido</div><div class="cv">R$ 71 mil</div>
    <p>Parcela do primeiro aporte usada para <b>cobrir o déficit de caixa de julho</b>. Não foi aplicada em
    máquina, estrutura ou expansão.</p></div>
  <div class="card warn"><div class="ct">Passivo trabalhista</div><div class="cv">R$ 30,0 mil</div>
    <p>Verbas e encargos dos seis desligamentos já ocorridos, <b>fora do fluxo acima</b>. Detalhamento na
    Parte IV.</p></div>
  <div class="card"><div class="ct">A receber sem data</div><div class="cv">R$ 87 mil</div>
    <p>Projeto <b>André / Alphaville</b>, entregue e com cobrança integralmente em aberto. Não entra em
    nenhum dos dois meses.</p></div>
</div>

<div class="note warn mt"><div class="nt">A incógnita deste quadro</div>
  <p>O material já adquirido <b>mistura obras entregues e obras a executar, sem rastreio por projeto</b>. Os
  R$ 200 mil de demanda são estimativa da direção, não levantamento. <b>Enquanto essa medição não existir, o
  saldo do período é um teto, não uma previsão</b> — e construí-la é a prioridade número um do financeiro.</p></div>""")

# ═══════════════════════════════════════════ PARTE IV

full("""
<div class="part">
  <div class="pnum">IV</div>
  <div class="plabel">Parte quatro</div>
  <h2>Passivo Trabalhista</h2>
  <p class="pintro">O levantamento das verbas rescisórias e dos encargos incidentes sobre os
    desligamentos já ocorridos no quadro de produção, apurado contrato a contrato. Um número fechado,
    com o perímetro do cálculo declarado — o que entra, o que não entra e por quê.</p>
  <div class="plist">
    <div class="pli"><b>20</b><span>Apuração por contrato, encargos e perímetro</span></div>
  </div>
</div>""")

# ── 18 passivo
PASS = [
    ('Jomar', 'Marceneiro · 47 meses', '24/06/2022', '30/04/2026', '1.950,00', '650,00', '2.166,67', '7.332,00', '10.148,67'),
    ('Samuel', 'Marceneiro · 9 meses', '01/08/2025', '30/04/2026', '2.500,00', '833,33', '2.500,00', '1.800,00', '5.133,33'),
    ('Deivison', 'Marceneiro · 9 meses', '01/09/2025', '31/05/2026', '2.500,00', '1.041,67', '2.500,00', '1.800,00', '5.341,67'),
    ('Joelson', 'Marceneiro · 15 meses', '01/02/2025', '30/04/2026', '1.950,00', '650,00', '650,00', '2.340,00', '3.640,00'),
    ('Davi', 'Marceneiro · 6 meses', '01/11/2025', '30/04/2026', '1.950,00', '650,00', '1.300,00', '936,00', '2.886,00'),
    ('Filipe', 'Marceneiro · 3 meses', '01/03/2026', '31/05/2026', '1.700,00', '425,00', '566,67', '408,00', '1.399,67'),
]
pl = ''.join(
    f'<tr><td class="nm">{p[0]}<span class="fn">{p[1]}</span></td>'
    f'<td class="dt">{p[2]} &nbsp;a&nbsp; {p[3]}</td><td class="num">{p[4]}</td>'
    f'<td class="num">{p[5]}</td><td class="num">{p[6]}</td><td class="num">{p[7]}</td>'
    f'<td class="num sub">{p[8]}</td></tr>' for p in PASS)

page('Parte IV · Passivo Trabalhista', 'Levantamento · posição até o presente momento', 'Apuração por contrato',
     'Verbas rescisórias e encargos incidentes sobre os seis desligamentos do quadro de produção, com data de conclusão definida.',
     f"""
<div class="kpis k4">
  <div class="kpi a"><div class="kl">Contratos encerrados</div><div class="kv">6</div><div class="kd">Equipe de produção · marceneiros</div></div>
  <div class="kpi b"><div class="kl">Verbas rescisórias</div><div class="kv"><small>R$</small> 28.549<small>,34</small></div><div class="kd">13º, férias + 1/3 e FGTS</div></div>
  <div class="kpi c"><div class="kl">Encargos patronais</div><div class="kv"><small>R$</small> 1.479<small>,00</small></div><div class="kd">Incidentes sobre o 13º</div></div>
  <div class="kpi d"><div class="kl">Passivo total</div><div class="kv"><small>R$</small> 30.028<small>,34</small></div><div class="kd">Sem saldo de dias · sem multa de 40%</div></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Apuração contrato a contrato</span><span class="ct">valores em reais · base salário contratual</span></div>
<table>
  <thead><tr><th style="width:20%">Colaborador</th><th style="width:19%">Período do contrato</th>
    <th class="num" style="width:9%">Salário</th><th class="num" style="width:13%">13º prop.</th>
    <th class="num" style="width:14%">Férias + 1/3</th><th class="num" style="width:12%">FGTS 8%</th>
    <th class="num" style="width:13%">Subtotal</th></tr></thead>
  <tbody>{pl}
    <tr class="tot"><td colspan="3">Total das verbas rescisórias</td><td class="num">4.250,00</td>
      <td class="num">9.683,34</td><td class="num">14.616,00</td><td class="num">28.549,34</td></tr>
    <tr class="enc"><td colspan="6">Encargos patronais sobre o 13º<span class="fn">INSS patronal + terceiros / RAT 26,8% &nbsp;·&nbsp; FGTS 8%</span></td>
      <td class="num">1.479,00</td></tr>
  </tbody>
</table>

<div class="band mt">
  <div><div class="bl">Passivo trabalhista apurado</div><div class="bv">R$ 30.028,34</div></div>
  <div class="br">O valor está concentrado no <b>tempo de casa, não no número de pessoas</b>: o FGTS
    responde por <b>51% do total</b>, e o contrato mais antigo sozinho por <b>R$ 10.148,67</b>.</div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Critérios da apuração</span></div>
<div class="two">
  <div class="note"><div class="nt">Como cada verba foi calculada</div>
    <ul>
      <li><b>Base.</b> Salário contratual mensal, sem médias de variáveis ou adicionais.</li>
      <li><b>Conclusão.</b> 30/04/2026, exceto Deivison e Filipe em 31/05/2026. Todos por demissão sem justa causa.</li>
      <li><b>FGTS.</b> 8% da remuneração de cada mês, sobre a duração integral do vínculo.</li>
      <li><b>Férias.</b> Proporcionais do período aquisitivo em curso, acrescidas do terço constitucional.</li>
      <li><b>Encargos.</b> Incidem apenas sobre o 13º, por ser verba salarial. Confirmado enquadramento no Simples sem CPP, o passivo recua para <b>R$ 28.889,34</b>.</li>
    </ul></div>
  <div class="note warn"><div class="nt">Não computado nesta apuração</div>
    <ul>
      <li><b>Multa de 40% do FGTS</b> — incidiria sobre o saldo da conta vinculada de cada colaborador.</li>
      <li><b>Aviso prévio</b> — devido em desligamento sem justa causa, indenizado ou trabalhado, crescendo 3 dias por ano de casa.</li>
      <li><b>Férias vencidas</b> — considerados regularmente gozados os períodos aquisitivos já completados.</li>
    </ul>
    <p style="margin-top:6px">Os itens acima são <b>conhecidos e mapeados</b>. Ficaram fora para que o
    número apresente exatamente o perímetro definido.</p></div>
</div>""")

# ═══════════════════════════════════════════ PARTE V

full("""
<div class="part">
  <div class="pnum">V</div>
  <div class="plabel">Parte cinco</div>
  <h2>Caminhos de Expansão</h2>
  <p class="pintro">De R$ 250 mil a R$ 1 milhão por mês, em degraus. Cada degrau com o seu gatilho de
    demanda, o gargalo que ataca e o investimento que exige. As máquinas com ficha técnica e preço; o
    galpão com os dois caminhos possíveis. <b>Não há recomendação aqui</b> — há caminhos, custos e
    trade-offs postos lado a lado, para que a decisão seja informada e consciente.</p>
  <div class="plist">
    <div class="pli"><b>22</b><span>A escada de produção</span></div>
    <div class="pli"><b>23</b><span>Galpão: adaptar o atual ou mudar</span></div>
    <div class="pli"><b>24</b><span>Comparativo de coladeiras</span></div>
    <div class="pli"><b>25</b><span>Linha industrial e complementares</span></div>
    <div class="pli"><b>26</b><span>Diferencial de mercado — puxadores</span></div>
    <div class="pli"><b>27</b><span>Prestação de serviços</span></div>
    <div class="pli"><b>28</b><span>Plano de expansão 2026–2027</span></div>
    <div class="pli"><b>29</b><span>Retorno e payback</span></div>
  </div>
</div>""")

# ── 20 escada
STAIR = [
    ('#5a6a7a', 78, 'Hoje', '250', 'mil / mês', 'Estrutura atual',
     [('Situação', 'Teto da capacidade atual. A coladeira <b>SCM ME25</b> atende até ~300 mil e <b>não entrega a peça 100% finalizada</b>.'),
      ('Investimento', '—')]),
    ('#2f5d8c', 100, 'Degrau 1', '300', 'mil / mês', '+ Mão de obra · zero máquina',
     [('Gatilho', 'Demanda sustentada acima do teto atual, com carteira firme.'),
      ('Investimento', '+1 marceneiro · +2 ajudantes · +1 carro.<br><b>Folha ~R$ 9 mil/mês</b> + veículo.'),
      ('Ganho', '+20% de capacidade sem tocar na estrutura.')]),
    ('#2f7d4f', 126, 'Degrau 2', '400', 'mil / mês', '+ Upgrade de coladeira',
     [('Gatilho', 'Demanda acima de 300 mil; a ME25 não passa daqui nem finaliza 100%.'),
      ('Investimento', 'Coladeira <b>R$ 160–480k</b> + habilitação do galpão <b>~R$ 56–61k</b> (única).'),
      ('Ganho', 'Remove o gargalo da colagem e libera mão de obra para produzir.')]),
    ('#a9863f', 158, 'Degrau 3', '600', 'mil / mês', '+ Reorg. galpão + equipe',
     [('Gatilho', 'Demanda acima de 400 mil.'),
      ('Investimento', 'Reorganização do galpão <b>~R$ 50–79k</b> (única) + folha de 2 duplas <b>~R$ 14k/mês</b>.'),
      ('Ganho', 'Fluxo contínuo; base para o salto industrial.')]),
    ('#0E2038', 196, 'Horizonte', '1', 'milhão / mês', 'Linha industrial',
     [('Gatilho', 'Demanda acima de 600 mil + mudança de galpão.'),
      ('Investimento', 'Novo galpão + nesting (R$ 530k) + furação (R$ 360k) + coladeira.'),
      ('Ganho', 'Produção em linha, escalável e rastreável.')]),
]
st = ''.join(
    f'<div class="st"><div class="sbar" style="background:{s[0]};min-height:{s[1]}px">'
    f'<div class="sw">{s[2]}</div><div class="sv">{s[3]}<small>{s[4]}</small></div></div>'
    f'<div class="sbody"><div class="sk" style="color:#1b2733;font-size:7.4px">{s[5]}</div>'
    + ''.join(f'<div class="sk" style="margin-top:5px">{k}</div><div class="sp">{t}</div>' for k, t in s[6]) +
    '</div></div>' for s in STAIR)

page('Parte V · Caminhos de Expansão', 'A escada de produção', 'Do teto atual ao horizonte de R$ 1 milhão',
     'Cada degrau responde à demanda que passou a puxar acima do patamar anterior e ao gargalo que limita a produção naquele ponto.',
     f"""
<div class="stair">{st}</div>

<div class="sec mt"><span class="bar"></span><span class="tx">Quadro-resumo da escada</span><span class="ct">valores-âncora</span></div>
<table class="tight">
  <thead><tr><th style="width:14%">Degrau</th><th style="width:32%">O que entra</th>
    <th style="width:32%">Investimento-âncora</th><th>Gatilho</th></tr></thead>
  <tbody>
    <tr><td class="nm">R$ 250 mil<span class="fn">hoje</span></td><td>Estrutura atual</td><td class="dt">—</td><td class="dt">ponto de partida</td></tr>
    <tr><td class="nm">R$ 300 mil<span class="fn">degrau 1</span></td><td>+1 marceneiro, +2 ajudantes, +1 carro</td><td>Folha ~R$ 9k/mês + veículo</td><td class="dt">demanda &gt; teto</td></tr>
    <tr><td class="nm">R$ 400 mil<span class="fn">degrau 2</span></td><td>Upgrade de coladeira + habilitação (única)</td><td>R$ 160–480k + R$ 56–61k</td><td class="dt">demanda &gt; 300</td></tr>
    <tr><td class="nm">R$ 600 mil<span class="fn">degrau 3</span></td><td>Reorganização do galpão (única) + 2 duplas</td><td>Reorg. ~R$ 50–79k + folha ~R$ 14k/mês</td><td class="dt">demanda &gt; 400</td></tr>
    <tr class="tot"><td>R$ 1 milhão<span class="fn" style="color:#b9c2cc">horizonte</span></td><td>Galpão novo + linha interligada</td><td>Galpão + nesting + furação + coladeira</td><td>demanda &gt; 600</td></tr>
  </tbody>
</table>

<div class="two mt">
  <div class="note ok"><div class="nt">Por que uma escada, e não um salto</div>
    <p>Cada degrau ataca o gargalo daquele momento e destrava a capacidade seguinte. Assim, o
    <b>capital entra na medida em que a demanda real o justifica</b>, e o risco fica distribuído no tempo
    em vez de concentrado numa aposta única.</p>
    <p style="margin-top:5px">A escada não é um cronograma rígido — é um <b>mapa de decisão</b>. O ritmo
    real é ditado pela demanda, não pelo documento.</p></div>
  <div class="note"><div class="nt">O fio condutor financeiro</div>
    <p>A régua que atravessa todos os degraus é a <b>margem de contribuição de ~40%</b>. Cada passo só se
    justifica se o faturamento adicional <b>preservar essa margem</b> — cobrindo o custo fixo que ele mesmo
    cria e ainda ampliando o resultado.</p>
    <p style="margin-top:5px">Os números são <b>âncoras</b>: ordem de grandeza para orientar a decisão,
    não um orçamento fechado. Valores de máquina são de feira.</p></div>
</div>""")

# ── 21 galpão
page('Parte V · Caminhos de Expansão', 'Infraestrutura', 'Galpão: adaptar o atual ou mudar',
     'Os dois caminhos para a mesma meta, com os custos abertos. A diferença entre eles é sobretudo de capital e de risco.',
     """
<div class="two">
  <div class="card"><div class="ct">Caminho A</div><h4>Escada dentro do galpão atual</h4>
    <p><b>Cheque menor por etapa</b>, capital diluído no tempo, na medida da demanda. Em contrapartida,
    <b>parte da obra civil não migra</b> — vira custo afundado ao mudar de galpão — e o teto físico do
    atual fica em ~R$ 600 mil/mês.</p></div>
  <div class="card"><div class="ct">Caminho B</div><h4>Salto direto para o galpão novo</h4>
    <p><b>Sem retrabalho.</b> Nenhuma obra afundada, a estrutura já nasce para o milhão e chega ao topo
    mais rápido. Em contrapartida, o <b>cheque de largada é grande e concentrado</b>, e exige demanda já
    engatilhada para não ociar a capacidade instalada.</p></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Caminho A · custos abertos da adaptação</span><span class="ct">investimento único · não migra</span></div>
<table class="tight">
  <thead><tr><th style="width:44%">Item</th><th style="width:24%">Natureza</th><th class="num" style="width:18%">Referência</th></tr></thead>
  <tbody>
    <tr class="sec2"><td colspan="3">Habilitação da coladeira · degrau 2</td></tr>
    <tr><td class="nm">Compressor maior<span class="fn">ar comprimido para a máquina</span></td><td class="dt">Equipamento</td><td class="num sub">R$ 25.000</td></tr>
    <tr><td class="nm">Exaustor 5 cv<span class="fn">exaustão de pó e vapores</span></td><td class="dt">Equipamento</td><td class="num sub">R$ 6.000</td></tr>
    <tr><td class="nm">Rede elétrica + transformador</td><td class="dt">Instalação</td><td class="num sub">~R$ 10.000</td></tr>
    <tr><td class="nm">Frete + instalação</td><td class="dt">Logística</td><td class="num sub">~R$ 20.000</td></tr>
    <tr class="sec2"><td colspan="3">Reorganização do espaço · degrau 3</td></tr>
    <tr><td class="nm">Mezanino no fundo<span class="fn">área adicional de apoio e estoque</span></td><td class="dt">Obra civil</td><td class="num sub">~R$ 25.000</td></tr>
    <tr><td class="nm">Elétrica / iluminação / ventilação</td><td class="dt">Instalação</td><td class="num sub">R$ 12–15.000</td></tr>
    <tr><td class="nm">Carrinhos / esteira interna<span class="fn">circulação de peças</span></td><td class="dt">Equipamento</td><td class="num sub">~R$ 8.000</td></tr>
    <tr><td class="nm">Rede pneumática</td><td class="dt">Instalação</td><td class="num sub">~R$ 5.000</td></tr>
    <tr><td class="nm">Piso usinado<span class="fn">opcional</span></td><td class="dt">Obra civil</td><td class="num sub">~R$ 12.000</td></tr>
    <tr><td class="nm">Patamar + rampa<span class="fn">ou descer a esquadrejadeira — alternativa</span></td><td class="dt">Obra civil</td><td class="num sub">a definir</td></tr>
    <tr class="tot"><td colspan="2">Faixa total da adaptação · habilitação + reorganização</td><td class="num">R$ 90–120 mil</td></tr>
  </tbody>
</table>

<div class="sec"><span class="bar"></span><span class="tx">Caminho B · composição do salto</span></div>
<div class="kpis k3">
  <div class="kpi c"><div class="kl">Caminho A · obra no atual</div><div class="kv"><small>R$</small> 90–120k</div><div class="kd">Diluído entre os degraus 2 e 3 · <b>não migra</b></div></div>
  <div class="kpi d"><div class="kl">Caminho B · cheque de largada</div><div class="kv"><small>R$</small> 1,5–2 mi</div><div class="kd">Galpão + linha de máquinas · concentrado</div></div>
  <div class="kpi f"><div class="kl">Teto do galpão atual</div><div class="kv"><small>~R$</small> 600k</div><div class="kd">O milhão exige a mudança de qualquer forma</div></div>
</div>

<div class="note warn mt"><div class="nt">⚑ Ponto de contexto — fato, não recomendação</div>
  <p>As <b>máquinas Giben migram e têm revenda/troca</b> — acompanham a empresa para o galpão novo.
  Já a <b>obra civil é específica de cada galpão</b> e não se muda. Onde o capital é alocado — em ativo que
  migra ou em estrutura fixa — pesa de forma diferente em cada caminho.</p></div>""")

# ── 22 coladeiras
page('Parte V · Caminhos de Expansão', 'Comparativo de máquinas', 'As coladeiras, lado a lado',
     'A coladeira de bordas é a máquina que destrava a produção. A atual atende até ~R$ 300 mil e não finaliza 100% — por isso o upgrade no degrau 2.',
     """
<table class="tight">
  <thead><tr><th style="width:19%">Critério</th>
    <th style="width:16%">Raizen<br>Spectra 7GT</th><th style="width:16%">Usikraft<br>Pegasus 1100</th>
    <th style="width:16%">Giben<br>KG668</th><th style="width:16%">Giben<br>KG712</th>
    <th style="width:17%">Giben KG398J<br>Puxadores ★</th></tr></thead>
  <tbody>
    <tr><td class="nm">Valor de feira</td><td class="num sub">R$ 160 mil</td><td class="num sub">R$ 200 mil</td><td class="num sub">R$ 260 mil</td><td class="num sub">R$ 410 mil</td><td class="num sub">R$ 480 mil</td></tr>
    <tr><td class="nm">Posição</td><td class="dt">Menor cheque de entrada</td><td class="dt">Meio-termo de acabamento</td><td class="dt">Referência do mercado moveleiro</td><td class="dt">Topo — automação plena</td><td class="dt">Puxador integrado · lançamento</td></tr>
    <tr><td class="nm">Recursos</td><td class="dt">7 grupos de trabalho</td><td class="dt">12 grupos · fita até 3 mm · 6 rolos pneum.</td><td class="dt">Regulagens finas manuais · manutenção simples</td><td class="dt">Regulagens automáticas · magazine de 4 fitas</td><td class="dt">Usina puxador / perfil integrado na peça</td></tr>
    <tr><td class="nm">Filetagem (peça reta)</td><td class="dt">a confirmar</td><td class="dt">a confirmar</td><td class="dt">22 m/min</td><td class="dt">a confirmar (alta)</td><td class="dt" style="color:#b0413f">8 m/min (baixa)</td></tr>
    <tr><td class="nm">Bipagem / telemetria</td><td class="dt">Não</td><td class="dt">Não</td><td class="dt">Não</td><td class="dt" style="color:#2f7d4f;font-weight:700">Sim</td><td class="dt">a confirmar</td></tr>
    <tr><td class="nm">Pega a usada na troca</td><td class="dt">Não</td><td class="dt">Não</td><td class="dt" style="color:#2f7d4f;font-weight:700">Sim</td><td class="dt" style="color:#2f7d4f;font-weight:700">Sim</td><td class="dt" style="color:#2f7d4f;font-weight:700">Sim</td></tr>
    <tr><td class="nm">Assistência / revenda</td><td class="dt" style="color:#b0413f">Fraca</td><td class="dt">Média</td><td class="dt" style="color:#2f7d4f;font-weight:700">Forte · BH</td><td class="dt" style="color:#2f7d4f;font-weight:700">Forte</td><td class="dt" style="color:#2f7d4f;font-weight:700">Forte · Giben</td></tr>
    <tr><td class="nm">Logística + instalação</td><td class="dt">~R$ 20 mil</td><td class="dt">~R$ 20 mil</td><td class="dt">~R$ 20 mil</td><td class="dt">~R$ 20 mil</td><td class="dt">~R$ 20 mil</td></tr>
    <tr><td class="nm">Atende até R$ 600k sem troca</td><td class="dt">Provável que não</td><td class="dt">Meio-termo</td><td class="dt" style="color:#2f7d4f;font-weight:700">Sim</td><td class="dt" style="color:#2f7d4f;font-weight:700">Sim</td><td class="dt">Diferencial · não é a de volume</td></tr>
    <tr class="tot"><td>Entra no degrau</td><td class="num">2 · 400 mil</td><td class="num">2 · 400 mil</td><td class="num">2–3 · 400–600</td><td class="num">3 · 600 mil</td><td class="num">qualquer fase</td></tr>
  </tbody>
</table>

<div class="sec"><span class="bar"></span><span class="tx">O que pesa em cada escolha</span></div>
<div class="cards c3">
  <div class="card"><div class="ct">Raizen Spectra 7GT · R$ 160k</div><h4>O menor cheque possível</h4>
    <p><b>A favor:</b> menor investimento de entrada; marca que a equipe já conhece e opera.</p>
    <p><b>A ponderar:</b> depreciação alta e revenda fraca; não pega usada na troca — <b>vira custo afundado
    ao migrar</b> — e provavelmente não basta até os 600 mil.</p></div>
  <div class="card"><div class="ct">Usikraft Pegasus 1100 · R$ 200k</div><h4>O meio-termo de acabamento</h4>
    <p><b>A favor:</b> 12 grupos operacionais, bordas mais limpas e fita PVC/ABS até 3 mm, que cobre a
    linha premium. Bom custo-benefício.</p>
    <p><b>A ponderar:</b> sem bipagem ou telemetria; não pega usada na troca; assistência a confirmar na região.</p></div>
  <div class="card gold"><div class="ct">Giben KG668 · R$ 260k</div><h4>O capital que se preserva</h4>
    <p><b>A favor:</b> marca moveleira conceituada que preserva valor; <b>pega a usada na troca</b>, migra para
    o galpão novo e tem showroom, técnico e treinamento em BH. Atende até 600 sem nova troca.</p>
    <p><b>A ponderar:</b> regulagens ainda manuais; sem bipagem.</p></div>
</div>

<div class="note mt"><div class="nt">Nota sobre custos que não aparecem no preço</div>
  <p>Além do valor da máquina, cada coladeira exige <b>frete e instalação (~R$ 20 mil)</b> e a
  <b>habilitação no galpão</b> — compressor, exaustão e elétrica — um investimento único de
  <b>~R$ 56–61 mil no total</b>. A diferença real entre as opções não está só no preço de etiqueta:
  está em <b>revenda, assistência local e migração</b> para o galpão novo.</p></div>""")

# ── 23 linha industrial
page('Parte V · Caminhos de Expansão', 'Fichas técnicas · linha industrial', 'Corte, furação e apoio',
     'As máquinas do horizonte de R$ 1 milhão — nesting e centro de usinagem — e os equipamentos que sustentam o fluxo.',
     """
<div class="two">
  <div class="card"><div class="ct">Valor de feira · R$ 530 mil</div><h4>Nesting Giben</h4>
    <div class="sp" style="font-size:8px;color:#6c7785;margin-top:2px">Centro de corte nesting com bipagem · base da linha</div>
    <table class="tight" style="margin-top:6px">
      <tbody>
        <tr><td class="nm" style="width:42%">Função</td><td class="dt">Corte nesting</td></tr>
        <tr><td class="nm">Rastreabilidade</td><td class="dt">Bipagem de peça</td></tr>
        <tr><td class="nm">Aproveitamento</td><td class="dt">Plano otimizado</td></tr>
        <tr><td class="nm">Integração</td><td class="dt">Coladeira + furação</td></tr>
      </tbody>
    </table>
    <p style="margin-top:6px">Substitui o corte tradicional por um fluxo <b>automatizado e rastreável</b>,
    com menos desperdício de chapa. É a <b>porta de entrada da linha interligada</b>.</p>
    <p style="margin-top:4px;color:#b0413f"><b>A ponderar:</b> cheque elevado, só no salto industrial —
    pede galpão maior e demanda engatilhada.</p></div>
  <div class="card"><div class="ct">Valor de feira · R$ 360 mil</div><h4>Giben Flexdrill</h4>
    <div class="sp" style="font-size:8px;color:#6c7785;margin-top:2px">Centro de usinagem / furação CNC com bipagem</div>
    <table class="tight" style="margin-top:6px">
      <tbody>
        <tr><td class="nm" style="width:42%">Função</td><td class="dt">Furação CNC</td></tr>
        <tr><td class="nm">Rastreabilidade</td><td class="dt">Bipagem de peça</td></tr>
        <tr><td class="nm">Precisão</td><td class="dt">Programada, repetível</td></tr>
        <tr><td class="nm">Integração</td><td class="dt">Fecha corte–colagem–furação</td></tr>
      </tbody>
    </table>
    <p style="margin-top:6px">Fecha o <b>trio da linha</b>: a peça sai cortada, colada e <b>furada</b>, pronta
    para montar. Menos retrabalho e montagem mais rápida — o que sustenta o volume do milhão.</p>
    <p style="margin-top:4px;color:#b0413f"><b>A ponderar:</b> ganho pleno só com nesting e coladeira juntos.</p></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Complementares</span><span class="ct">apoio de fluxo e expedição</span></div>
<table>
  <thead><tr><th style="width:22%">Equipamento</th><th>Papel</th><th style="width:20%">Entra quando</th><th class="num" style="width:16%">Referência</th></tr></thead>
  <tbody>
    <tr><td class="nm">Esteira de retorno</td><td>Devolve a peça ao operador após a colagem sem carregar manualmente. Reduz o deslocamento interno, acelera o ciclo da coladeira e sustenta o ritmo quando a produção sobe.</td><td class="dt">Reorganização · degrau 3+</td><td class="num sub">R$ 60.000</td></tr>
    <tr><td class="nm">Embaladora</td><td>Protege e padroniza a peça na expedição — acabamento profissional na entrega e menos avaria no transporte. Ganha relevância com volume alto e operação de linha.</td><td class="dt">Linha industrial</td><td class="num sub">a partir de R$ 60.000</td></tr>
  </tbody>
</table>

<div class="band mt">
  <div><div class="bl">Linha completa · horizonte</div><div class="bv">R$ 890 mil</div></div>
  <div class="br">Nesting (R$ 530k) + Flexdrill (R$ 360k), <b>antes</b> da coladeira, dos complementares e do
    galpão. É o núcleo do cheque de R$ 1,5–2 milhões do Caminho B.</div>
</div>

<div class="note mt"><div class="nt">Por que só faz sentido em conjunto</div>
  <p>Cada máquina isolada entrega menos do que promete. O ganho real da linha industrial vem da
  <b>integração</b>: corte nesting, colagem e furação falando a mesma língua, com bipagem entre as etapas.
  Deixa de ser &quot;uma máquina a mais&quot; e passa a ser um <b>sistema de produção</b> — e é isso que o
  patamar de R$ 1 milhão exige.</p></div>""")

# ── 24 puxadores
page('Parte V · Caminhos de Expansão', 'Diferencial de mercado', 'A máquina de puxadores',
     'Por que um único equipamento pode reposicionar o produto Valvic — ampliando margem por percepção de valor, não por volume.',
     """
<p class="lead2">Entre todas as máquinas deste caderno, a coladeira de puxadores é <b>a única cujo retorno
não vem de produzir mais, e sim de produzir diferente</b>. Ela usina o puxador — o perfil de pega —
<b>integrado à própria peça</b>, eliminando a ferragem comprada de terceiros. O resultado é um móvel de
linhas limpas, sem puxador aparente, com um acabamento que o cliente percebe imediatamente como superior.</p>

<div class="two mt">
  <div class="card gold"><div class="ct">Giben KG398J · valor de feira R$ 480 mil</div><h4>Modelo de lançamento, inédito em Minas Gerais</h4>
    <table class="tight" style="margin-top:6px">
      <tbody>
        <tr><td class="nm" style="width:38%">Função</td><td class="dt">Puxador / perfil integrado na peça</td></tr>
        <tr><td class="nm">Filetagem</td><td class="dt">8 m/min — baixa · diferencial, não volume</td></tr>
        <tr><td class="nm">Exclusividade</td><td class="dt">Nenhuma marcenaria de MG a tem ainda</td></tr>
        <tr><td class="nm">Pega usada na troca</td><td class="dt">Sim · Giben</td></tr>
      </tbody>
    </table></div>
  <div class="card"><div class="ct">O que ela cria</div><h4>Um produto que o concorrente não tem</h4>
    <ul>
      <li><b>Ineditismo em MG</b> — possivelmente alguém no Sul de Minas venha a ter, segundo vendedores do ramo</li>
      <li>Puxador integrado como <b>assinatura visual</b> difícil de copiar</li>
      <li>Elimina o <b>custo e o prazo</b> da ferragem de puxador comprada</li>
      <li>Eleva a <b>percepção de valor</b> e o preço praticável</li>
    </ul></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Por que importa para a decisão de investimento</span></div>
<p class="t">As demais máquinas ampliam <b>capacidade</b>; esta amplia <b>a marca</b>. Num mercado de móveis
planejados onde a concorrência disputa preço, um diferencial de <b>design proprietário</b> muda o eixo da
conversa com o cliente — de &quot;quanto custa&quot; para <b>&quot;isto só a Valvic faz&quot;</b>.</p>
<p class="t">Há sinal de mercado: em São Paulo, um proprietário dessa máquina está <b>amplamente abastecido
de demanda</b> de arquitetas e marcenarias do entorno. É um módulo que <b>se paga em posicionamento</b> —
cada projeto premium carrega margem maior.</p>

<div class="two mt">
  <div class="note warn"><div class="nt">A ponderar com clareza</div>
    <p>Ela <b>fileta a ~8 m/min</b>, velocidade baixa — <b>não é a coladeira de volume</b> em peças retas.
    O ideal em produtividade é ter uma coladeira rápida para retas (ex.: Giben KG668) <b>e</b> a KG398J
    como diferencial competitivo. Uma não substitui a outra.</p></div>
  <div class="note ok"><div class="nt">Leitura estratégica</div>
    <p>Não compete com as coladeiras de produção — <b>complementa</b>. Enquanto a linha resolve o
    <b>volume</b>, os puxadores resolvem o <b>valor</b>.</p>
    <p style="margin-top:5px">Em uma frase: transforma o móvel Valvic em <b>produto de assinatura</b> — e a
    marca em algo que se escolhe por desejo, não só por orçamento.</p></div>
</div>""")

# ── 25 serviços
page('Parte V · Caminhos de Expansão', 'Cenário adicional', 'Prestação de serviços',
     'Como a linha industrial vira um segundo motor de receita — e por que isso reduz o risco de todo o investimento.',
     """
<p class="lead2">Uma linha dimensionada para R$ 1 milhão de produção própria dificilmente estará
<b>100% ocupada o tempo todo</b>. Essa folga — que num modelo tradicional seria custo ocioso — pode virar
<b>receita</b>. Com nesting, coladeira e furação equipados com bipagem, a Valvic passa a poder
<b>vender capacidade de produção</b> a terceiros: corte, colagem e furação para marcenarias sem CNC próprio.</p>

<div class="cards c2 mt">
  <div class="card"><div class="ct">O modelo</div><h4>Capacidade ociosa vira receita</h4>
    <p>A mesma linha que produz o móvel Valvic presta <b>serviço B2B</b> nas janelas livres. O cliente é a
    marcenaria menor, sem máquina, que precisa de corte e colagem de qualidade industrial. A Valvic vende
    <b>a própria capacidade</b>, não só o produto final.</p></div>
  <div class="card"><div class="ct">O efeito no caixa</div><h4>Preenche os vales de demanda</h4>
    <p>Nos meses de produção própria mais fraca, o serviço <b>preenche o buraco de caixa</b>. A operação
    deixa de depender exclusivamente do ciclo de vendas de móveis planejados e ganha uma
    <b>receita mais estável</b> ao longo do ano.</p></div>
  <div class="card"><div class="ct">A precificação</div><h4>Margem alta e auditável</h4>
    <p>A <b>telemetria</b> da coladeira mede o metro colado real; a bipagem conta as peças. Isso permite
    <b>precificar por peça ou por metro</b> — cobrança justa, transparente e medida pela própria máquina,
    sem estimativa grosseira.</p></div>
  <div class="card gold"><div class="ct">O ponto central</div><h4>De-risca o investimento</h4>
    <p>A prestação de serviços <b>transforma o CAPEX em ativo que fatura mesmo com a produção própria não
    cheia</b>. A linha industrial passa a se pagar por <b>dois caminhos, não um só</b> — e é isso que reduz
    o risco de todo o investimento em máquinas.</p></div>
</div>

<div class="note blue mt"><div class="nt">Consequência prática — muda a estratégia de localização</div>
  <p>Se o serviço mirar atender a demanda de <b>BH, Contagem e entornos</b>, a
  <b>localização do galpão passa a ser fator estratégico</b>: estar perto dos clientes B2B — marcenarias e
  lojas — muda a escolha do endereço. Proximidade vira vantagem logística e comercial, e essa decisão
  precisa ser tomada <b>antes</b> de fechar o galpão novo, não depois.</p></div>

<div class="note mt"><div class="nt">Síntese do cenário</div>
  <p>Não é um negócio paralelo que disputa foco — é o <b>aproveitamento inteligente</b> de uma capacidade
  que, de outro modo, ficaria parada. Receita de margem alta, que estabiliza o caixa e reduz o risco de
  todo o investimento em máquinas.</p></div>""")

# ── 26 plano
page('Parte V · Caminhos de Expansão', 'Plano de expansão 2026–2027', 'Fases, máquinas e mapa do investimento',
     'A versão executiva do plano: o que entra na Fase 1 para girar já, e o que a Fase 2 exige para a estrutura completa.',
     """
<div class="two">
  <div class="card blue"><div class="ct">Fase 1 · imediato</div><h4>Start do negócio — girar com o essencial</h4>
    <ul>
      <li>Nova <b>coladeira de borda</b> Giben KG268 — arredondador, fita 1 mm</li>
      <li>Novo <b>compressor</b> Techto 10 HP — alimenta a nova linha</li>
      <li><b>Camionete usada</b> — reforço de logística imediato</li>
      <li>+1 marceneiro, +1 auxiliar administrativo, +1 ajudante</li>
      <li>Setup de postos: 2 kits de ferramentas + móveis</li>
    </ul>
    <div class="cv" style="margin-top:6px">≈ R$ 251–263 mil</div></div>
  <div class="card"><div class="ct">Fase 2 · estrutura completa</div><h4>Galpão novo, todas as máquinas rodando</h4>
    <ul>
      <li>Nova <b>CNC nesting</b> Giben — capacidade 2× a Solid TAF</li>
      <li><b>Furação horizontal</b> Raizen 3S — portas, cavilhas, fechaduras</li>
      <li><b>Galpão 1.000 m²</b> — 40 × 25 m com doca de caminhão</li>
      <li><b>Kia Bongo baú</b> — carga 1,5 t para o volume dobrado</li>
      <li>+1 marceneiro, +1 ajudante, +1 projetista</li>
    </ul>
    <div class="cv" style="margin-top:6px">≈ R$ 872 mil</div></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">Mapa do investimento</span><span class="ct">consolidado das duas fases</span></div>
<table class="tight">
  <thead><tr><th style="width:34%">Item</th><th style="width:36%">Detalhe</th><th class="num" style="width:18%">Valor R$</th></tr></thead>
  <tbody>
    <tr class="sec2"><td colspan="3">Fase 1 · start imediato</td></tr>
    <tr><td class="nm">Coladeira Giben KG268</td><td class="dt">Principal — arredondador + fita 1 mm · suporte local em BH</td><td class="num sub">~162.000</td></tr>
    <tr><td class="nm">Compressor Techto AT 10HP</td><td class="dt">10 HP / 7,5 kW · 8,5 bar · cabine acústica · instalação externa</td><td class="num sub">21.310</td></tr>
    <tr><td class="nm">Camionete usada</td><td class="dt">Reforço de logística</td><td class="num sub">50–60.000</td></tr>
    <tr><td class="nm">Setup de pessoal</td><td class="dt">CAPEX único · 2 kits + posto adm. + 7 cadeiras</td><td class="num sub">~18–20.000</td></tr>
    <tr class="enc"><td colspan="2">Total Fase 1</td><td class="num">≈ 251–263.000</td></tr>
    <tr class="sec2"><td colspan="3">Fase 2 · estrutura completa</td></tr>
    <tr><td class="nm">CNC Nesting Giben G2 1929</td><td class="dt">~1.430 chapas/mês · etiquetagem + furação · carga de palete inteiro</td><td class="num sub">490.000</td></tr>
    <tr><td class="nm">Furação horizontal Raizen 3S</td><td class="dt">Topo e borda do MDF — cavilha, minifix, fechadura, dobradiça</td><td class="num sub">82.000</td></tr>
    <tr><td class="nm">Kia Bongo baú</td><td class="dt">Carga ~1,5 t · entrega do volume dobrado</td><td class="num sub">~100.000</td></tr>
    <tr><td class="nm">Infraestrutura do galpão</td><td class="dt">Reforma · elétrica 150 kVA · aspiração · ar comprimido</td><td class="num sub">~200.000</td></tr>
    <tr class="enc"><td colspan="2">Total Fase 2</td><td class="num">≈ 872.000</td></tr>
    <tr class="tot"><td colspan="2">Investimento total · Fase 1 + Fase 2</td><td class="num">≈ R$ 1.100.000</td></tr>
  </tbody>
</table>

<div class="two mt">
  <div class="note ok"><div class="nt">Por que pagamento à vista</div>
    <p>O aporte <b>compra as máquinas à vista</b>, desbloqueando <b>desconto de 10–15%</b> que financia parte
    do próprio processo — e elimina parcelas mensais que pressionariam o caixa durante a rampa de produção.</p></div>
  <div class="note warn"><div class="nt">Ainda em aberto</div>
    <ul>
      <li><b>Custo mensal do galpão</b> (aluguel) — impacta o ponto de equilíbrio final.</li>
      <li><b>Capital de giro</b> operacional durante a rampa — não incluído no total.</li>
      <li><b>Estrutura do aporte</b> — valor e contrapartida (% societária ou empréstimo remunerado) não fixados.</li>
      <li>Confirmar se os preços Giben são <b>à vista</b> e solicitar desconto.</li>
    </ul></div>
</div>""")

# ── 27 payback
page('Parte V · Caminhos de Expansão', 'Retorno ao investidor', 'Cenários e payback',
     'Dois cenários sobre o mesmo investimento de R$ 1,1 milhão — o conservador, de dobrar a produção, e o de capacidade instalada.',
     """
<div class="two">
  <div class="card"><div class="ct">Cenário 1 · conservador</div><h4>Dobrar: R$ 200k → R$ 400k / mês</h4>
    <table class="tight" style="margin-top:6px">
      <tbody>
        <tr><td class="nm" style="width:46%">Receita nova</td><td class="num sub">+R$ 200k<span class="fn">/mês adicional</span></td></tr>
        <tr><td class="nm">MC 30%</td><td class="num sub">+R$ 60k<span class="fn">MC adicional/mês</span></td></tr>
        <tr><td class="nm">Folha nova</td><td class="num sub" style="color:#b0413f">−R$ 41k<span class="fn">com encargos/mês</span></td></tr>
        <tr><td class="nm">Sobra líquida</td><td class="num sub">≈ R$ 19k<span class="fn">/mês</span></td></tr>
      </tbody>
    </table>
    <div class="cv" style="margin-top:7px">~55 meses <span style="font-size:11px;color:#6c7785">· ~4,6 anos</span></div>
    <p style="margin-top:4px;color:#b0413f;font-size:8.2px">Antes de fixos novos — aluguel, energia e
    combustível — ainda a incluir. Eles reduzem o saldo e alongam o payback.</p></div>
  <div class="card gold"><div class="ct">Cenário 2 · capacidade instalada</div><h4>R$ 1 milhão / mês — teto das máquinas novas</h4>
    <table class="tight" style="margin-top:6px">
      <tbody>
        <tr><td class="nm" style="width:46%">Receita nova</td><td class="num sub">+R$ 800k<span class="fn">/mês adicional</span></td></tr>
        <tr><td class="nm">MC 30%</td><td class="num sub">+R$ 240k<span class="fn">MC adicional/mês</span></td></tr>
        <tr><td class="nm">Investimento</td><td class="num sub">R$ 1,1 mi<span class="fn">total da estrutura</span></td></tr>
        <tr><td class="nm">Payback no pico</td><td class="num sub" style="color:#2f7d4f">&lt; 5 meses</td></tr>
      </tbody>
    </table>
    <div class="cv" style="margin-top:7px">&lt; 12 meses <span style="font-size:11px;color:#6c7785">· por alavancagem operacional</span></div>
    <p style="margin-top:4px;font-size:8.2px">O cenário exige demanda engatilhada para não ociar a
    capacidade — é onde o pipeline do investidor pesa mais que o capital.</p></div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">A alavancagem operacional, em uma frase</span></div>
<div class="band">
  <div><div class="bl">O princípio</div><div class="bv" style="font-size:22px">Custo fixo linear,<br>capacidade exponencial</div></div>
  <div class="br">Com a estrutura instalada, o custo fixo cresce <b>de forma linear</b> enquanto a capacidade de
    faturamento cresce <b>de forma exponencial</b>. A mesma folha, o mesmo galpão e as mesmas máquinas que
    produzem R$ 400 mil/mês são as que chegam a <b>R$ 1 milhão/mês</b> — o diferencial vira
    <b>capital de giro e carteira comercial</b>.</div>
</div>

<div class="sec"><span class="bar"></span><span class="tx">As decisões que ficam na mesa</span></div>
<table class="tight">
  <thead><tr><th style="width:15%">Decisão</th><th style="width:44%">O que está em jogo</th><th>Extremos</th></tr></thead>
  <tbody>
    <tr><td class="nm">Ritmo</td><td>Crescer por etapas, na medida da demanda — o R$ 1 milhão como horizonte, não como prazo.</td><td class="dt">Gradual (menor risco) ↔ acelerado (chega antes)</td></tr>
    <tr><td class="nm">Galpão</td><td>Onde a expansão acontece e como o capital fica exposto.</td><td class="dt">Atual (obra R$ 90–120k) ↔ novo (cheque R$ 1,5–2 mi)</td></tr>
    <tr><td class="nm">Coladeira</td><td>Cheque menor agora × capital que preserva valor e migra.</td><td class="dt">Raizen R$ 160k ↔ Giben KG668 R$ 260k</td></tr>
    <tr><td class="nm">Alavancas</td><td>Diferenciação de produto e monetização da capacidade instalada.</td><td class="dt">Puxadores (margem) + serviços (de-risca)</td></tr>
  </tbody>
</table>

<div class="note mt"><div class="nt">O que validar antes de subir cada degrau</div>
  <p>Confirmar <b>demanda sustentada</b> acima do patamar atual &nbsp;·&nbsp; identificar o
  <b>gargalo real</b> que o investimento vai atacar &nbsp;·&nbsp; checar que o salto <b>preserva a margem</b>.
  Para fechar números: obter <b>propostas finais</b> das máquinas (de feira → firmes), orçar a
  <b>infraestrutura</b> com fornecedores locais e definir a <b>forma de aporte</b> e o payback aceitável por etapa.</p></div>""")

# ═══════════════════════════════════════════ FECHO

full("""
<div class="end">
  <div class="kx">Encerramento</div>
  <h2>Os caminhos estão<br><span>postos na mesa</span></h2>
  <p style="font-size:10.6px;color:rgba(255,255,255,.7);line-height:1.75;margin-top:8mm;max-width:118mm">
    Este caderno apresenta <b style="color:#fff">caminhos e realidades</b>, de forma organizada — não uma
    recomendação. Cada degrau tem o seu gatilho, cada máquina o seu momento, cada galpão o seu trade-off.
    O material existe para que a decisão seja <b style="color:#fff">informada e consciente</b>, por quem
    tem os números na ponta da língua.</p>

  <div class="src">
    <div class="sh">Documentos de origem · reunidos neste volume</div>
    <div class="sr"><span class="sd">07 ago 2026</span><span class="sn">Passivo Trabalhista — Posição Apurada</span><span class="sf">Parte IV</span></div>
    <div class="sr"><span class="sd">25 jul 2026</span><span class="sn">Estrutura de Demandas — Pessoas &amp; Infraestrutura</span><span class="sf">Parte II</span></div>
    <div class="sr"><span class="sd">25 jul 2026</span><span class="sn">Fluxo de Trabalho — Posição &amp; Impacto</span><span class="sf">Parte II</span></div>
    <div class="sr"><span class="sd">20 jul 2026</span><span class="sn">Organograma &amp; Carga Operacional</span><span class="sf">Parte II</span></div>
    <div class="sr"><span class="sd">16 jul 2026</span><span class="sn">Panorama Comercial — Rumo a Agosto</span><span class="sf">Parte I</span></div>
    <div class="sr"><span class="sd">06 jul 2026</span><span class="sn">Caminhos de Expansão — Apresentação Visual</span><span class="sf">Parte V</span></div>
    <div class="sr"><span class="sd">06 jul 2026</span><span class="sn">Dossiê Técnico de Expansão</span><span class="sf">Parte V</span></div>
    <div class="sr"><span class="sd">29 jun 2026</span><span class="sn">Modelo Econômico &amp; Alavancagem Operacional</span><span class="sf">Parte III</span></div>
    <div class="sr"><span class="sd">26 jun 2026</span><span class="sn">Plano de Expansão 2026–2027</span><span class="sf">Parte V</span></div>
  </div>

  <div class="fin">
    <div class="f1"><b style="color:#fff">Uso restrito.</b> Contém dado de remuneração e posição financeira —
      não circular fora dos sócios e do destinatário.<br>
      Valvic Marcenaria · Vargas Decor Ltda · CNPJ 17.269.304/0001-51 · Belo Horizonte / MG</div>
    <div class="f2">Agosto<br>2026</div>
  </div>
</div>""")

# ─────────────────────────────────────────────────────────── saída

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Caderno Empresarial — Valvic Marcenaria · 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<button class="btn" onclick="window.print()">⤓ Exportar PDF</button>
{render()}
</body>
</html>
"""

open('caderno-empresarial-valvic.html', 'w', encoding='utf-8').write(HTML)
print(f'escrito · {len(PAGES)} páginas · {round(len(HTML.encode())/1024)} KB')
