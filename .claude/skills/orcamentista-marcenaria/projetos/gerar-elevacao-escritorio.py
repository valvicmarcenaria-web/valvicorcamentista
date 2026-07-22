# -*- coding: utf-8 -*-
# Elevação frontal técnica — PAREDE DIREITA (copa/apoio) — Escritório PORTO VERDE 40 m² (4x10m)
# Referência: render fotorrealista do cliente + board de proposta + fotos do local.
# Composição da parede direita: Estante metálica preta | Torre alta grafite | Balcão copa/café
#   (amêndoa + tampo grafite) sob parede grafite c/ logo PORTO VERDE + prateleira flutuante LED.
# Medidas em mm — a confirmar no local.

S = 0.262                          # px/mm (~1:25 em A3)
MARGIN_L = 150
BASE = 800                         # linha de piso (svg y)
def X(mm): return MARGIN_L + mm*S
def Y(mm): return BASE - mm*S

# ---- geometria (mm) ----
PH   = 2650                        # pé-direito útil da marcenaria (a confirmar)
RODAPE  = 100
H_TAMPO = 900
T_TAMPO = 40
H_SHELF = 1550
T_SHELF = 40

# larguras (esq->dir):  janela | ESTANTE | TORRE | BALCÃO CAFÉ | entrada
X_EST0, X_EST1 = 0,    900         # estante metálica preta
X_TOR0, X_TOR1 = 900,  1950        # torre alta grafite (porta piso-teto)
X_CAF0, X_CAF1 = 1950, 4650        # balcão copa/café + parede grafite/logo
W = X_CAF1                          # 4650

# cores (paleta PORTO VERDE)
C_WOOD='#C9A063'; C_WOOD2='#BB8F4E'
C_GRAF='#3A3E44'; C_GRAF2='#31353B'; C_GRAFdk='#292C31'
C_TAMPO='#2C3034'
C_LED='#F4C978'
C_MET='#1D2024'                    # metal preto
C_GREEN='#5E7B52'
C_LINE='#1C2026'; C_DIM='#8A8375'; C_INK='#221B12'; C_WALL='#EFEBE2'

svg=[]
def r(x,y,w,h,fill,stroke=C_LINE,sw=1.4,extra=''):
    svg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>')
def line(x1,y1,x2,y2,stroke=C_LINE,sw=1.2,dash=''):
    d=f'stroke-dasharray="{dash}"' if dash else ''
    svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}" {d}/>')
def txt(x,y,s,size=11,fill=C_INK,anchor='middle',weight='400',ls='0'):
    svg.append(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" letter-spacing="{ls}" font-family="Helvetica,Arial,sans-serif">{s}</text>')
def cava(xmm,y0,y1):   # puxador cava vertical
    line(X(xmm), Y(y0), X(xmm), Y(y1), C_LINE, 2)

# ---------- parede de fundo + laje nervurada ----------
r(X(0)-40, Y(PH+250), (W)*S+80, (PH+250)*S, C_WALL, 'none', 0)
for gx in range(0, int(W)+1, 300):
    line(X(gx), Y(PH+250), X(gx), Y(PH+120), '#D8D2C4', 1)
for gy in range(int(PH)+120, int(PH)+251, 60):
    line(X(0)-40, Y(gy), X(W)+40, Y(gy), '#D8D2C4', 1)
txt(X(W)-8, Y(PH+160), 'LAJE NERVURADA APARENTE', 9, '#9C9482','end','600','.06em')

# ======================================================
# 1) ESTANTE METÁLICA PRETA (aberta) — serralheria
# ======================================================
# montantes + prateleiras finas
for xm in (X_EST0, (X_EST0+X_EST1)/2, X_EST1):
    line(X(xm), Y(0), X(xm), Y(PH-100), C_MET, 3)
for ym in (150, 820, 1490, 2050, PH-100):
    line(X(X_EST0), Y(ym), X(X_EST1), Y(ym), C_MET, 3)
# plantas em algumas prateleiras
for (cx,cy) in [((X_EST0+X_EST1)/2, 820),(X_EST0+280,1490),((X_EST0+X_EST1)/2,2050)]:
    r(X(cx-70), Y(cy+150), 140*S, 150*S, C_GREEN, C_MET, 1)
txt((X(X_EST0)+X(X_EST1))/2, Y(PH-40), 'ESTANTE METÁLICA', 8.5, C_INK,'middle','700','.03em')

# ======================================================
# 2) TORRE ALTA GRAFITE (porta piso-teto)
# ======================================================
r(X(X_TOR0), Y(PH-100), (X_TOR1-X_TOR0)*S, (PH-100-RODAPE)*S, C_GRAF, C_LINE, 1.6)
line(X(X_TOR0), Y(1400), X(X_TOR1), Y(1400))          # divisão porta sup/inf
cava(X_TOR1-70, 1500, 2200)                            # puxador vertical sup
cava(X_TOR1-70, 500, 1250)                             # puxador vertical inf
# pictograma WC (opcional / a confirmar)
txt((X(X_TOR0)+X(X_TOR1))/2, Y(1950), 'TORRE', 9.5, '#D6DAE0','middle','700','.05em')
txt((X(X_TOR0)+X(X_TOR1))/2, Y(1830), 'GRAFITE', 8.5, '#AEB4BC','middle','600','.05em')
txt((X(X_TOR0)+X(X_TOR1))/2, Y(1030), 'piso-teto', 8, '#9aa0a7','middle','400','.03em')

# ======================================================
# 3) BALCÃO COPA / CAFÉ  (amêndoa + tampo grafite) + parede grafite atrás
# ======================================================
# parede grafite de fundo (feature wall) atrás do balcão
r(X(X_CAF0), Y(PH-100), (X_CAF1-X_CAF0)*S, (PH-100-H_TAMPO)*S, C_GRAF2, C_LINE, 1.2)

# --- base do balcão: módulos amêndoa ---
top = H_TAMPO - T_TAMPO
# módulos: portas | gaveteiro | portas(café) | porta + nicho baixo
mods=[(X_CAF0,      X_CAF0+750, 'porta2'),
      (X_CAF0+750,  X_CAF0+1250,'gav3'),
      (X_CAF0+1250, X_CAF0+2000,'porta2'),
      (X_CAF0+2000, X_CAF0+2700,'porta_nicho')]
for (x0,x1,tp) in mods:
    if tp=='porta2':
        w=(x1-x0)/2
        for i in range(2):
            r(X(x0+i*w), Y(top), w*S, (top-RODAPE)*S, C_WOOD, C_LINE,1.2)
            cava(x0+i*w+(w-28 if i==1 else 28), top-70, top-10)
    elif tp=='gav3':
        h=(top-RODAPE)/3
        for i in range(3):
            r(X(x0), Y(RODAPE+(i+1)*h), (x1-x0)*S, h*S, C_WOOD, C_LINE,1.1)
            line(X((x0+x1)/2)-16, Y(RODAPE+(i+1)*h)-h*S/2, X((x0+x1)/2)+16, Y(RODAPE+(i+1)*h)-h*S/2, C_LINE,2)
    elif tp=='porta_nicho':
        r(X(x0), Y(top), (x1-x0)*S, (top-560)*S, C_GRAFdk, C_LINE,1.2)   # nicho baixo aberto (grafite)
        txt((X(x0)+X(x1))/2, Y(top-160), 'nicho', 7.5, '#9aa0a7','middle')
        r(X(x0), Y(560), (x1-x0)*S, (560-RODAPE)*S, C_WOOD, C_LINE,1.2)
        cava((x0+x1)/2, 560-40, 560-260)
# tampo grafite
r(X(X_CAF0), Y(H_TAMPO), (X_CAF1-X_CAF0)*S, T_TAMPO*S, C_TAMPO, C_LINE,1.2)
# rodapé + piso
line(X(0), Y(RODAPE), X(W), Y(RODAPE), C_LINE,1)
line(X(-30), Y(0), X(W)+30, Y(0), C_INK,2.4)

# --- prateleira flutuante + LED (sobre a copa) ---
r(X(X_CAF0), Y(H_SHELF), 1600*S, T_SHELF*S, C_WOOD2, C_LINE,1.2)
line(X(X_CAF0)+6, Y(H_SHELF)+T_SHELF*S+2, X(X_CAF0+1600)-6, Y(H_SHELF)+T_SHELF*S+2, C_LED,3)
txt(X(X_CAF0+800), Y(H_SHELF)-8, 'PRATELEIRA FLUTUANTE · LED 3000K', 8.5, '#8a8272','middle','600','.04em')

# --- nicho aberto p/ impressora (recesso grafite) ---
r(X(X_CAF0+1750), Y(1520), 900*S, (1520-950)*S, C_GRAFdk, C_LINE,1.2)
txt(X(X_CAF0+2200), Y(1200), 'nicho impressora', 7.5, '#9aa0a7','middle','500','.03em')

# --- logo PORTO VERDE na parede grafite ---
lx=X_CAF0+330
# emblema (triângulo + barra) acima do texto
ey=Y(2560)
svg.append(f'<path d="M {X(lx):.1f} {ey:.1f} l 30 0 l -15 -30 z" fill="none" stroke="#9EA98F" stroke-width="2.4"/>')
svg.append(f'<line x1="{X(lx)+15:.1f}" y1="{ey-2:.1f}" x2="{X(lx)+15:.1f}" y2="{ey-26:.1f}" stroke="#9EA98F" stroke-width="2.4"/>')
txt(X(lx)-4, Y(2320), 'PORTO', 21, '#E7E3DA','start','700','.03em')
txt(X(lx)-4, Y(2110), 'VERDE', 21, '#E7E3DA','start','700','.03em')

# --- equipamentos sobre o tampo (contorno tracejado) — sem sobreposição ---
def equip(cx,w,h,label):
    r(X(cx-w/2), Y(H_TAMPO+h), w*S, h*S, '#00000000', '#B9B2A2',1.2,'stroke-dasharray="4 3"')
    txt(X(cx), Y(H_TAMPO+h)+h*S/2+3, label, 7.5, '#c9c2b2','middle','500','.03em')
equip(X_CAF0+2420, 300, 360, 'cafeteira')
equip(X_CAF0+2150, 480, 300, 'impressora')

svg_body="\n".join(svg)

# ---------- cotas ----------
dim=[]
def hdim(x0,x1,ymm,val):
    y=Y(ymm)
    dim.append(f'<line x1="{X(x0):.1f}" y1="{y:.1f}" x2="{X(x1):.1f}" y2="{y:.1f}" stroke="{C_DIM}" stroke-width="1"/>')
    for xx in (x0,x1):
        dim.append(f'<line x1="{X(xx):.1f}" y1="{y-5:.1f}" x2="{X(xx):.1f}" y2="{y+5:.1f}" stroke="{C_DIM}" stroke-width="1"/>')
    dim.append(f'<text x="{(X(x0)+X(x1))/2:.1f}" y="{y-4:.1f}" font-size="9.5" fill="{C_INK}" text-anchor="middle" font-family="Helvetica,Arial">{val}</text>')
def vdim(y0,y1,xpx,val):
    dim.append(f'<line x1="{xpx:.1f}" y1="{Y(y0):.1f}" x2="{xpx:.1f}" y2="{Y(y1):.1f}" stroke="{C_DIM}" stroke-width="1"/>')
    for yy in (y0,y1):
        dim.append(f'<line x1="{xpx-5:.1f}" y1="{Y(yy):.1f}" x2="{xpx+5:.1f}" y2="{Y(yy):.1f}" stroke="{C_DIM}" stroke-width="1"/>')
    ymid=(Y(y0)+Y(y1))/2
    dim.append(f'<text x="{xpx-7:.1f}" y="{ymid+3:.1f}" font-size="9.5" fill="{C_INK}" text-anchor="middle" transform="rotate(-90 {xpx-7:.1f} {ymid+3:.1f})" font-family="Helvetica,Arial">{val}</text>')

# larguras (topo)
hdim(X_EST0,X_EST1, PH+40, '900')
hdim(X_TOR0,X_TOR1, PH+40, '1050')
for (x0,x1,tp) in mods: hdim(x0,x1, PH+40, f'{int(x1-x0)}')
# total
hdim(0, W, -180, f'{int(W)}  (largura da parede — conferir no local)')
# alturas
vdim(0,H_TAMPO,   X(0)-42, '900')
vdim(H_TAMPO,H_SHELF, X(0)-42, '650')
vdim(0,PH-100,    X(0)-74, str(int(PH-100)))
# rótulos zona
zonas=[((X_EST0+X_EST1)/2,'ESTANTE'),((X_TOR0+X_TOR1)/2,'TORRE'),(X_CAF0+1350,'COPA / CAFÉ')]
labels="\n".join(f'<text x="{X(cx):.1f}" y="{BASE+42:.1f}" font-size="10.5" fill="{C_INK}" text-anchor="middle" font-weight="700" letter-spacing=".05em" font-family="Helvetica,Arial">{t}</text>' for cx,t in zonas)
dim_body="\n".join(dim)

DRAW_W=X(W)+90
DRAW_H=BASE+70

URI1=open('/tmp/uri_p01.txt').read(); URI2=open('/tmp/uri_p02.txt').read()

HTML=f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<style>
@page{{ size:420mm 297mm; margin:0; }}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{ width:420mm;height:297mm;background:#fff;color:{C_INK};font-family:Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased;position:relative;}}
.frame{{position:absolute;inset:8mm;border:1.5px solid #2b2b2b;}}
.frame::after{{content:"";position:absolute;inset:3mm;border:.5px solid #b9b2a2;}}
.sheet{{position:absolute;inset:0;padding:14mm 16mm;}}
.hd{{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #2b2b2b;padding-bottom:7px;margin-bottom:6px;}}
.hd .bd{{font-family:Georgia,serif;font-weight:700;font-size:26px;}} .hd .bd span{{color:{C_GRAF};}}
.hd .sub{{font-size:11px;color:#6C6152;letter-spacing:.16em;text-transform:uppercase;margin-top:3px;}}
.hd .rt{{text-align:right;font-size:10.5px;color:#6C6152;line-height:1.6;}} .hd .rt b{{color:{C_INK};}}
.stage{{display:flex;gap:14px;margin-top:8px;}}
.draw{{flex:1;display:flex;flex-direction:column;}}
.vtag{{font-family:Georgia,serif;font-size:15px;font-weight:700;margin:2px 0 4px 2px;}}
.refstrip{{margin-top:10px;border-top:1px solid #d9d2c3;padding-top:8px;}}
.refh{{font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;color:#8A8375;font-weight:700;margin-bottom:6px;}}
.refgrid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;}}
.refgrid figure{{margin:0;}} .refgrid img{{width:100%;height:150px;object-fit:cover;border:1px solid #cfc7b6;border-radius:5px;display:block;}}
.refgrid figcaption{{font-size:9px;color:#8A8375;margin-top:4px;line-height:1.4;}}
.side{{width:250px;flex:none;display:flex;flex-direction:column;gap:10px;}}
.card{{border:1px solid #d9d2c3;border-radius:8px;padding:10px 11px;}}
.card h4{{font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:#8A8375;margin-bottom:8px;font-weight:700;}}
.leg{{display:flex;align-items:center;gap:8px;font-size:11px;margin:5px 0;}}
.sw{{width:22px;height:14px;border:1px solid #1C2026;border-radius:2px;flex:none;}}
.spec{{font-size:10.5px;color:#4b463d;line-height:1.6;}} .spec b{{color:{C_INK};}}
.note{{font-size:9.5px;color:#8A8375;line-height:1.5;}}
.tb{{margin-top:auto;border:1px solid #2b2b2b;}}
.tb .row{{display:flex;border-bottom:1px solid #d9d2c3;font-size:10px;}} .tb .row:last-child{{border-bottom:0;}}
.tb .k{{width:78px;padding:5px 7px;color:#8A8375;letter-spacing:.06em;text-transform:uppercase;font-size:8.5px;border-right:1px solid #d9d2c3;flex:none;}}
.tb .v{{padding:5px 7px;color:{C_INK};font-weight:600;}}
</style></head><body>
<div class="frame"></div>
<div class="sheet">
  <div class="hd">
    <div><div class="bd">valvic<span>.</span> marcenaria</div>
      <div class="sub">Projeto Técnico · Elevação Frontal</div></div>
    <div class="rt"><b>PORTO VERDE — Escritório 40 m² (4 × 10 m)</b><br>
      Parede direita: Copa/Café · Torre grafite · Estante metálica<br>
      Vista: <b>Elevação frontal</b></div>
  </div>
  <div class="stage">
    <div class="draw">
      <div class="vtag">Elevação 01 — Parede direita <span style="font-size:11px;color:#8A8375;font-weight:400;font-family:Helvetica">esc. 1:25 · cotas em mm</span></div>
      <svg viewBox="0 0 {DRAW_W:.0f} {DRAW_H:.0f}" width="100%" style="display:block;">
        {svg_body}
        {dim_body}
        {labels}
      </svg>
      <div class="refstrip"><div class="refh">Referência do projeto — perspectivas recebidas</div>
        <div class="refgrid">
          <figure><img src="{URI1}" alt=""><figcaption>Visão da entrada — copa/café à direita, parede grafite c/ logo</figcaption></figure>
          <figure><img src="{URI2}" alt=""><figcaption>Estações de trabalho — parede direita ao fundo</figcaption></figure>
        </div></div>
    </div>
    <div class="side">
      <div class="card"><h4>Materiais / Acabamentos</h4>
        <div class="leg"><span class="sw" style="background:{C_WOOD}"></span> MDF <b>Amêndoa</b> — balcão copa</div>
        <div class="leg"><span class="sw" style="background:{C_GRAF}"></span> <b>Cinza Grafite</b> — torre, parede, nichos</div>
        <div class="leg"><span class="sw" style="background:{C_TAMPO}"></span> Tampo <b>Grafite</b> (fosco)</div>
        <div class="leg"><span class="sw" style="background:{C_MET}"></span> <b>Estante metálica</b> preta (serralheria)</div>
        <div class="leg"><span class="sw" style="background:{C_LED}"></span> Fita <b>LED 3000K</b> (quente)</div>
        <div class="spec" style="margin-top:8px;">Logo <b>PORTO VERDE</b> em relevo na parede grafite. Puxador tipo <b>cava/perfil</b>. Rodapé recuado 100 mm.</div>
      </div>
      <div class="card"><h4>Planta-chave</h4>
        <svg viewBox="0 0 220 150" width="100%">
          <rect x="20" y="10" width="90" height="130" fill="#F4EEE1" stroke="#2b2b2b" stroke-width="1.5"/>
          <rect x="24" y="14" width="82" height="40" fill="#fff" stroke="#b9b2a2" stroke-width="1" stroke-dasharray="3 2"/>
          <text x="65" y="37" font-size="7" fill="#8A8375" text-anchor="middle">reunião/janela</text>
          <rect x="46" y="66" width="40" height="46" fill="{C_WOOD}" stroke="#2b2b2b" stroke-width="1"/>
          <rect x="104" y="30" width="7" height="104" fill="{C_GRAF}" stroke="none"/>
          <text x="150" y="86" font-size="8" fill="{C_GRAF}" text-anchor="start" font-weight="700">◄ elev. 01</text>
          <text x="150" y="98" font-size="7.5" fill="#8A8375" text-anchor="start">parede direita</text>
          <text x="65" y="150" font-size="7" fill="#8A8375" text-anchor="middle">entrada ▼   ·   janela ▲</text>
        </svg>
      </div>
      <div class="tb">
        <div class="row"><div class="k">Cliente</div><div class="v">PORTO VERDE</div></div>
        <div class="row"><div class="k">Projeto</div><div class="v">Escritório comercial 40 m²</div></div>
        <div class="row"><div class="k">Desenho</div><div class="v">Elev. frontal — parede direita</div></div>
        <div class="row"><div class="k">Escala</div><div class="v">1:25 (A3) · indicativa</div></div>
        <div class="row"><div class="k">Data</div><div class="v">22/07/2026 · Rev. 01</div></div>
        <div class="row"><div class="k">Responsável</div><div class="v">Valvic Marcenaria</div></div>
      </div>
      <div class="note" style="margin-top:8px;">⚠ Medidas de referência — <b>confirmar largura da parede, pé-direito e posição da porta/WC no local</b>. Estante metálica = serralheria parceira (coordenada Valvic). Equipamentos (cafeteira, impressora) do cliente.</div>
    </div>
  </div>
</div>
</body></html>'''
open('/home/user/valvicorcamentista/.claude/skills/orcamentista-marcenaria/projetos/elevacao-escritorio.html','w',encoding='utf-8').write(HTML)
print('wrote elevacao-escritorio.html', len(HTML))
