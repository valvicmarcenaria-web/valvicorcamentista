# -*- coding: utf-8 -*-
# Elevação frontal técnica — Balcão de apoio (Café/Impressora/Papelaria/Arquivos)
# Escritório comercial 40 m² (4x10m). Fonte: board de proposta + fotos do local (Drive).
# Desenho vetorial à escala. Medidas em mm (a confirmar no local).

S = 0.205  # px por mm (escala de tela ~1:25 em A3)
def X(mm): return MARGIN_L + mm*S
def Y(mm): return BASE - mm*S     # y-up real -> y-down svg

MARGIN_L = 130
BASE = 560                        # linha de piso (svg y)

# ---- geometria (mm) ----
W = 5400                          # largura total do balcão
H_TAMPO = 900                     # altura do tampo (bancada baixa)
T_TAMPO = 40                      # espessura tampo grafite
RODAPE  = 100                     # recuo/altura rodapé
H_SHELF = 1500                    # altura prateleira flutuante
T_SHELF = 40
H_AER_B = 1650                    # base dos aéreos
H_AER_T = 2150                    # topo dos aéreos
BACK_T  = 1500                    # topo do backsplash grafite

# módulos base: (x0, x1, tipo, rótulo, subdivisões)
MOD = [
 (0,    900,  'porta2', 'ARQUIVOS',  2),
 (900,  1800, 'porta2', 'ARQUIVOS',  2),
 (1800, 2400, 'gav4',   'PAPELARIA', 4),
 (2400, 3300, 'cafe',   'CAFÉ',      2),
 (3300, 4050, 'imp',    'IMPRESSORA',0),
 (4050, 4650, 'frigo',  'FRIGOBAR',  0),
 (4650, 5400, 'nicho',  'NICHO',     0),
]

# cores
C_WOOD  = '#C99A63'; C_WOOD2='#BC8A50'
C_GRAF  = '#3C4046'; C_GRAF2='#33363B'
C_TAMPO = '#2E3236'
C_LED   = '#F4C978'
C_LINE  = '#20242A'
C_WALL  = '#EFEBE2'
C_DIM   = '#8A8375'
C_INK   = '#221B12'

svg = []
def r(x,y,w,h,fill,stroke=C_LINE,sw=1.4,extra=''):
    svg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')
def line(x1,y1,x2,y2,stroke=C_LINE,sw=1.2,dash=''):
    d=f'stroke-dasharray="{dash}"' if dash else ''
    svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}" {d}/>')
def txt(x,y,s,size=11,fill=C_INK,anchor='middle',weight='400',ls='0',style=''):
    svg.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" letter-spacing="{ls}" style="{style}" font-family="Helvetica,Arial,sans-serif">{s}</text>')

# ---------- parede de fundo ----------
r(X(0)-40, Y(2500), W*S+80, (2500-0)*S, C_WALL, 'none', 0)
# laje nervurada aparente (topo) — hachura leve
for gx in range(0, W+1, 300):
    line(X(gx), Y(2500), X(gx), Y(2380), '#D8D2C4', 1)
for gy in range(2380,2501,60):
    line(X(0)-40, Y(gy), X(W)+40, Y(gy), '#D8D2C4', 1)
txt(X(W)-8, Y(2540), 'LAJE NERVURADA APARENTE', 9, '#9C9482', 'end', '600','.06em')

# ---------- backsplash grafite (café/impressora/frigobar/nicho) ----------
r(X(2400), Y(BACK_T), (4650-2400)*S, (BACK_T-H_TAMPO)*S, C_GRAF2, C_LINE, 1)
txt(X(3525), Y(1230), 'PAINEL GRAFITE', 8.5, '#C9CDd3', 'middle','600','.05em')

# ---------- aéreos (amêndoa) sobre arquivos ----------
r(X(0), Y(H_AER_T), 1800*S, (H_AER_T-H_AER_B)*S, C_WOOD, C_LINE, 1.4)
line(X(900), Y(H_AER_T), X(900), Y(H_AER_B))
for dx in (450,1350):   # cava puxador nos aéreos (inferior)
    line(X(dx)-14, Y(H_AER_B)+7, X(dx)+14, Y(H_AER_B)+7, C_LINE, 2)
txt(X(900), Y(H_AER_B+250), 'AÉREOS', 10, C_INK,'middle','700','.04em')
# LED sob aéreos
line(X(0)+6, Y(H_AER_B)+3, X(1800)-6, Y(H_AER_B)+3, C_LED, 3)

# ---------- prateleira flutuante + LED (café->frigobar) ----------
r(X(2400), Y(H_SHELF), (4650-2400)*S, T_SHELF*S, C_WOOD2, C_LINE, 1.2)
line(X(2400)+6, Y(H_SHELF)+T_SHELF*S+2, X(4650)-6, Y(H_SHELF)+T_SHELF*S+2, C_LED, 3)
txt(X(3525), Y(H_SHELF)-8, 'PRATELEIRA FLUTUANTE · LED 3000K', 8.5, '#7B7healthy'.replace('healthy','367'), 'middle','600','.04em')

# ---------- nicho grafite alto (fim) ----------
r(X(4650), Y(H_AER_T), 750*S, (H_AER_T-H_TAMPO)*S, C_GRAF, C_LINE, 1.4)
line(X(4650), Y(H_SHELF), X(5400), Y(H_SHELF))   # prateleira interna
line(X(4650), Y(1900), X(5400), Y(1900))
txt(X(5025), Y(1700), 'NICHO', 9, '#D6Dae0','middle','700','.05em')
txt(X(5025), Y(1620), 'ABERTO', 8, '#AEB4BC','middle','600','.05em')

# ---------- balcão baixo: tampo + módulos + rodapé ----------
# tampo grafite contínuo
r(X(0), Y(H_TAMPO), W*S, T_TAMPO*S, C_TAMPO, C_LINE, 1.2)
# corpo dos módulos
def draw_door(x0,x1,y0,y1,fill,n):
    w=(x1-x0)/n
    for i in range(n):
        dx0=x0+i*w
        r(X(dx0), Y(y1), w*S, (y1-y0)*S, fill, C_LINE, 1.2)
        # cava puxador vertical (borda interna superior)
        px = dx0+ (w-30 if i==n-1 else 30)
        line(X(px), Y(y1)+10, X(px), Y(y1)+70, C_LINE, 2)

for (x0,x1,tp,lab,sub) in MOD:
    top = H_TAMPO - T_TAMPO
    if tp=='porta2':
        draw_door(x0,x1,RODAPE,top,C_WOOD,2)
    elif tp=='gav4':
        h=(top-RODAPE)/sub
        for i in range(sub):
            r(X(x0), Y(RODAPE+(i+1)*h), (x1-x0)*S, h*S, C_WOOD, C_LINE, 1.1)
            line(X((x0+x1)/2)-16, Y(RODAPE+(i+1)*h)-h*S/2, X((x0+x1)/2)+16, Y(RODAPE+(i+1)*h)-h*S/2, C_LINE,2)
    elif tp=='cafe':
        draw_door(x0,x1,RODAPE,top,C_WOOD,2)
    elif tp=='imp':
        # nicho aberto (papel) em cima + gavetão embaixo
        r(X(x0), Y(top), (x1-x0)*S, (top-580)*S, '#E8E2D6', C_LINE, 1.2)   # nicho aberto
        r(X(x0), Y(580), (x1-x0)*S, (580-RODAPE)*S, C_WOOD, C_LINE, 1.2)   # gavetão
        line(X((x0+x1)/2)-16, Y(580)+ (580-RODAPE)*S/2, X((x0+x1)/2)+16, Y(580)+(580-RODAPE)*S/2, C_LINE,2)
        txt(X((x0+x1)/2), Y(top-120), 'nicho', 7.5, '#9a927f','middle','400','.03em')
    elif tp=='frigo':
        r(X(x0), Y(top), (x1-x0)*S, (top-820)*S, '#DfD9CC', C_LINE, 1.2)   # tampo apoio
        r(X(x0), Y(820), (x1-x0)*S, (820-RODAPE)*S, '#C9CDD2', C_LINE, 1.2) # frigobar (inox/cinza)
        txt(X((x0+x1)/2), Y(430), 'FRIGO', 7.5, '#5a5e63','middle','700','.04em')
    elif tp=='nicho':
        draw_door(x0,x1,RODAPE,top,C_GRAF,1)
# rodapé (recuo) — sombra
r(X(120), Y(RODAPE), (W-240)*S, RODAPE*S, '#0000', C_LINE, 0)
line(X(0), Y(RODAPE), X(W), Y(RODAPE), C_LINE, 1)
# linha de piso forte
line(X(-30), Y(0), X(W)+30, Y(0), C_INK, 2.4)

# equipamentos sobre o tampo (contorno leve) — café e impressora
def equip(cx, w, h, label):
    r(X(cx-w/2), Y(H_TAMPO+h), w*S, h*S, '#00000000', '#B9B2A2', 1.2, 'stroke-dasharray="4 3"')
    txt(X(cx), Y(H_TAMPO+h)+ h*S/2+3, label, 7.5, '#9a927f','middle','500','.03em')
equip(2850, 260, 360, 'cafeteira')
equip(3675, 520, 300, 'impressora')

svg_body = "\n".join(svg)

# ---------- cotas (dimension lines) ----------
dim=[]
def dimtick(x,y): dim.append(f'<line x1="{x-4:.1f}" y1="{y-4:.1f}" x2="{x+4:.1f}" y2="{y+4:.1f}" stroke="{C_DIM}" stroke-width="1.1"/>')
def hdim(x0,x1,ymm,val,off=0):
    y=Y(ymm)+off
    dim.append(f'<line x1="{X(x0):.1f}" y1="{y:.1f}" x2="{X(x1):.1f}" y2="{y:.1f}" stroke="{C_DIM}" stroke-width="1"/>')
    dimtick(X(x0),y); dimtick(X(x1),y)
    dim.append(f'<line x1="{X(x0):.1f}" y1="{y-5:.1f}" x2="{X(x0):.1f}" y2="{y+5:.1f}" stroke="{C_DIM}" stroke-width="1"/>')
    dim.append(f'<line x1="{X(x1):.1f}" y1="{y-5:.1f}" x2="{X(x1):.1f}" y2="{y+5:.1f}" stroke="{C_DIM}" stroke-width="1"/>')
    dim.append(f'<text x="{(X(x0)+X(x1))/2:.1f}" y="{y-4:.1f}" font-size="9.5" fill="{C_INK}" text-anchor="middle" font-family="Helvetica,Arial">{val}</text>')
def vdim(ymm0,ymm1,xpx,val):
    dim.append(f'<line x1="{xpx:.1f}" y1="{Y(ymm0):.1f}" x2="{xpx:.1f}" y2="{Y(ymm1):.1f}" stroke="{C_DIM}" stroke-width="1"/>')
    for yy in (ymm0,ymm1):
        dim.append(f'<line x1="{xpx-5:.1f}" y1="{Y(yy):.1f}" x2="{xpx+5:.1f}" y2="{Y(yy):.1f}" stroke="{C_DIM}" stroke-width="1"/>')
    dim.append(f'<text x="{xpx-8:.1f}" y="{(Y(ymm0)+Y(ymm1))/2+3:.1f}" font-size="9.5" fill="{C_INK}" text-anchor="middle" transform="rotate(-90 {xpx-8:.1f} {(Y(ymm0)+Y(ymm1))/2+3:.1f})" font-family="Helvetica,Arial">{val}</text>')

# cota superior: módulos
for (x0,x1,tp,lab,sub) in MOD:
    hdim(x0,x1, 2320, f'{x1-x0}')
# cota total
hdim(0, W, -170, f'{W}  (largura total — conferir no local)')
# cotas verticais (à esquerda)
vdim(0, H_TAMPO, X(0)-40, f'{H_TAMPO}')
vdim(H_TAMPO, H_SHELF, X(0)-40, f'{H_SHELF-H_TAMPO}')
vdim(H_AER_B, H_AER_T, X(0)-70, f'{H_AER_T-H_AER_B}')
vdim(0, H_AER_T, X(0)-100, f'{H_AER_T}')
# rótulos de função sob cada módulo
labels="\n".join(
  f'<text x="{(X(x0)+X(x1))/2:.1f}" y="{BASE+40:.1f}" font-size="10.5" fill="{C_INK}" text-anchor="middle" font-weight="700" letter-spacing=".04em" font-family="Helvetica,Arial">{lab}</text>'
  for (x0,x1,tp,lab,sub) in MOD)
dim_body="\n".join(dim)

DRAW_W = X(W)+110
DRAW_H = 640

# perspectivas de referência (data URIs)
URI1 = open('/tmp/uri_p01.txt').read()
URI2 = open('/tmp/uri_p02.txt').read()

HTML=f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<style>
@page{{ size:420mm 297mm; margin:0; }}
*{{box-sizing:border-box; margin:0; padding:0;}}
body{{ width:420mm; height:297mm; background:#fff; color:{C_INK};
  font-family:Helvetica,Arial,sans-serif; -webkit-font-smoothing:antialiased; position:relative; }}
.sheet{{ position:absolute; inset:0; padding:14mm 16mm; }}
.frame{{ position:absolute; inset:8mm; border:1.5px solid #2b2b2b; }}
.frame::after{{content:""; position:absolute; inset:3mm; border:.5px solid #b9b2a2;}}
.hd{{ display:flex; justify-content:space-between; align-items:flex-end; border-bottom:2px solid #2b2b2b; padding-bottom:7px; margin-bottom:6px; }}
.hd .bd{{ font-family:Georgia,serif; font-weight:700; font-size:26px; letter-spacing:.01em; }}
.hd .bd span{{ color:{C_GRAF}; }}
.hd .sub{{ font-size:11px; color:#6C6152; letter-spacing:.16em; text-transform:uppercase; margin-top:3px;}}
.hd .rt{{ text-align:right; font-size:10.5px; color:#6C6152; line-height:1.6; }}
.hd .rt b{{ color:{C_INK}; }}
.stage{{ display:flex; gap:14px; margin-top:8px; }}
.draw{{ flex:1; display:flex; flex-direction:column; }}
.refstrip{{ margin-top:10px; border-top:1px solid #d9d2c3; padding-top:8px; }}
.refh{{ font-size:9.5px; letter-spacing:.16em; text-transform:uppercase; color:#8A8375; font-weight:700; margin-bottom:6px; }}
.refgrid{{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
.refgrid figure{{ margin:0; }}
.refgrid img{{ width:100%; height:205px; object-fit:cover; border:1px solid #cfc7b6; border-radius:5px; display:block; }}
.refgrid figcaption{{ font-size:9px; color:#8A8375; margin-top:4px; line-height:1.4; }}
.side{{ width:250px; flex:none; display:flex; flex-direction:column; gap:10px; }}
.card{{ border:1px solid #d9d2c3; border-radius:8px; padding:10px 11px; }}
.card h4{{ font-size:10px; letter-spacing:.16em; text-transform:uppercase; color:#8A8375; margin-bottom:8px; font-weight:700;}}
.leg{{ display:flex; align-items:center; gap:8px; font-size:11px; margin:5px 0; color:{C_INK};}}
.sw{{ width:22px; height:14px; border:1px solid #20242A; border-radius:2px; flex:none;}}
.spec{{ font-size:10.5px; color:#4b463d; line-height:1.65; }}
.spec b{{ color:{C_INK}; }}
.note{{ font-size:9.5px; color:#8A8375; line-height:1.5; }}
.tb{{ margin-top:auto; border:1px solid #2b2b2b; }}
.tb .row{{ display:flex; border-bottom:1px solid #d9d2c3; font-size:10px; }}
.tb .row:last-child{{border-bottom:0;}}
.tb .k{{ width:78px; padding:5px 7px; color:#8A8375; letter-spacing:.06em; text-transform:uppercase; font-size:8.5px; border-right:1px solid #d9d2c3; flex:none;}}
.tb .v{{ padding:5px 7px; color:{C_INK}; font-weight:600;}}
.kp{{ position:relative; }}
.cap{{ font-size:9px; color:#8A8375; letter-spacing:.14em; text-transform:uppercase; text-align:center; margin-top:5px;}}
.vtag{{ font-family:Georgia,serif; font-size:15px; font-weight:700; }}
</style></head><body>
<div class="frame"></div>
<div class="sheet">
  <div class="hd">
    <div>
      <div class="bd">valvic<span>.</span> marcenaria</div>
      <div class="sub">Projeto Técnico · Elevação Frontal</div>
    </div>
    <div class="rt">
      <b>ESCRITÓRIO COMERCIAL — 40 m² (4 × 10 m)</b><br>
      Peça: Balcão de apoio — Café · Impressora · Papelaria · Arquivos<br>
      Vista: <b>Elevação frontal</b> · Parede longa (apoio)
    </div>
  </div>

  <div class="stage">
    <div class="draw">
      <div class="vtag" style="margin:2px 0 4px 2px;">Elevação 01 — Balcão de apoio <span style="font-size:11px;color:#8A8375;font-weight:400;font-family:Helvetica">esc. 1:25 · cotas em mm</span></div>
      <svg viewBox="0 0 {DRAW_W:.0f} {DRAW_H:.0f}" width="100%" style="display:block;">
        {svg_body}
        {dim_body}
        {labels}
      </svg>
      <div class="refstrip">
        <div class="refh">Referência do projeto — perspectivas recebidas</div>
        <div class="refgrid">
          <figure><img src="{URI1}" alt="visão da entrada"><figcaption>01 · Visão da entrada — balcão café/impressora à direita</figcaption></figure>
          <figure><img src="{URI2}" alt="estações"><figcaption>02 · Estações de trabalho — balcão de apoio ao fundo</figcaption></figure>
        </div>
      </div>
    </div>

    <div class="side">
      <div class="card">
        <h4>Materiais / Acabamentos</h4>
        <div class="leg"><span class="sw" style="background:{C_WOOD}"></span> MDF <b>Amêndoa</b> — corpo e frentes</div>
        <div class="leg"><span class="sw" style="background:{C_GRAF}"></span> Frentes/painéis <b>Cinza Grafite</b></div>
        <div class="leg"><span class="sw" style="background:{C_TAMPO}"></span> Tampo <b>Grafite</b> (fosco)</div>
        <div class="leg"><span class="sw" style="background:{C_LED}"></span> Fita <b>LED 3000K</b> (quente)</div>
        <div class="leg"><span class="sw" style="background:#C9CDD2"></span> Frigobar (equip. cliente)</div>
        <div class="spec" style="margin-top:8px;">Puxador tipo <b>cava/perfil</b> (sem puxador aparente). Rodapé recuado 100 mm. Fixação dos aéreos em parede estruturada.</div>
      </div>

      <div class="card kp">
        <h4>Planta-chave</h4>
        <svg viewBox="0 0 220 150" width="100%">
          <rect x="20" y="10" width="90" height="130" fill="#F4EEE1" stroke="#2b2b2b" stroke-width="1.5"/>
          <!-- sala reuniao -->
          <rect x="24" y="14" width="82" height="40" fill="#fff" stroke="#b9b2a2" stroke-width="1" stroke-dasharray="3 2"/>
          <text x="65" y="37" font-size="7" fill="#8A8375" text-anchor="middle">reunião</text>
          <!-- bancada estacoes -->
          <rect x="46" y="66" width="40" height="46" fill="{C_WOOD}" stroke="#2b2b2b" stroke-width="1"/>
          <!-- credenza (parede direita) destacada -->
          <rect x="104" y="60" width="7" height="72" fill="{C_GRAF}" stroke="none"/>
          <text x="150" y="98" font-size="8" fill="{C_GRAF}" text-anchor="start" font-weight="700">◄ elevação 01</text>
          <text x="150" y="110" font-size="7.5" fill="#8A8375" text-anchor="start">balcão de apoio</text>
          <text x="65" y="150" font-size="7" fill="#8A8375" text-anchor="middle">entrada ▼   ·   janela ▲</text>
        </svg>
      </div>

      <div class="tb">
        <div class="row"><div class="k">Cliente</div><div class="v">Escritório · coworking</div></div>
        <div class="row"><div class="k">Projeto</div><div class="v">Sala comercial 40 m²</div></div>
        <div class="row"><div class="k">Desenho</div><div class="v">Elevação frontal — balcão apoio</div></div>
        <div class="row"><div class="k">Escala</div><div class="v">1:25 (A3) · indicativa</div></div>
        <div class="row"><div class="k">Data</div><div class="v">22/07/2026 · Rev. 00</div></div>
        <div class="row"><div class="k">Responsável</div><div class="v">Valvic Marcenaria</div></div>
      </div>
      <div class="note" style="margin-top:8px;">⚠ Medidas de referência — <b>confirmar largura da parede e pés-direito no local</b>. Elevação modular, ajustável em obra. Equipamentos (cafeteira, impressora, frigobar) por conta do cliente.</div>
    </div>
  </div>
</div>
</body></html>'''

open('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos/elevacao-escritorio.html','w',encoding='utf-8').write(HTML)
print('wrote elevacao-escritorio.html', len(HTML))
