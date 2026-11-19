# -*- coding: utf-8 -*-
"""PAINEL DA SALA — VISTA 2 · a proposta de TRÊS PÁGINAS.

⭐⭐ [Jonathan, 18/11/2026] "Pode montar uma proposta um pouco mais robusta,
  apresentando as etapas da empresa, apresentar a garantia. Pode ter umas 3
  páginas essa proposta. Explore mais as imagens 3D que foi enviada no chat."

E, no mesmo fôlego: "Tire a descrição de articulador AVENTOS da Blum... não
será a báscula, será a porta de giro na parte superior também. E descreva que
na região das portas pivotantes será painel liso, não ripado."

⛔ AS OITO ETAPAS E A POLÍTICA DE GARANTIA NÃO SÃO MINHAS. Saíram, palavra
  por palavra, de `proposta-aline.html` (a linha do tempo da casa) e de
  `closer-vendas/referencias/garantia.md`. Inventar o processo da empresa numa
  proposta é prometer o que a fábrica não combinou.

⚠⚠ E A GARANTIA DE 30 ANOS TEM UMA PENDÊNCIA ABERTA NA CASA: garantia.md
  avisa que "só o termo de 10 anos está desenhado; o termo de 30 anos precisa
  existir assinado antes de a proposta sair". A folha promete 30; o documento
  tem de acompanhar.
"""
import pathlib, subprocess, os, importlib.util, datetime, base64

P = pathlib.Path(__file__).resolve().parent
def _mod(n, a):
    sp = importlib.util.spec_from_file_location(n, P / a)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
b  = _mod('ps_base', 'base.py')
lv = _mod('ps_lv', 'levantamento.py')

CSS = (P.parent / 'css-brinquedoteca.css').read_text()
br = lambda v: f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')
MES = ('janeiro fevereiro março abril maio junho julho agosto setembro '
       'outubro novembro dezembro').split()
_h = datetime.date.today()
DATA = f'{_h.day} de {MES[_h.month - 1]} de {_h.year}'

#   ⭐ [Jonathan, 18/11/2026] "Explore mais as imagens 3D que foi enviada no
#     chat." São cinco: dois renders do ambiente, dois estudos 3D da própria
#     prancha (a parede inteira e o nicho de perto) e o living.
#   ⛔ Entrada de build é arquivo do REPOSITÓRIO, nunca do scratchpad.
def uri(n):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P / 'img' / n).read_bytes()).decode())
IMG = {k: uri(k + '.jpg') for k in
       ('capa', 'living', 'escada', 'rodape', '3d-parede', '3d-nicho')}
# ════════════════════════════════════════════════════════════════════════
# O DESENHO
# ════════════════════════════════════════════════════════════════════════
L, A = lv.LARG, lv.ALT
SOCULO = 15.0
MARG_E, MARG_D, TOPO, BASE_V = 17.0, 7.0, 23.0, 18.0
VB_W, VB_H = L + MARG_E + MARG_D, TOPO + A + SOCULO + BASE_V
X0, Y0 = MARG_E, TOPO
X1, Y1 = X0 + L, Y0 + A
NIC_X0, NIC_X1 = X0 + lv.R_PORTA_L, X0 + lv.RIPADO_L
NIC_Y0, NIC_Y1 = Y0 + lv.R_SUP, Y0 + lv.R_SUP + lv.NICHO_H

#   ⛔⛔ O FUNDO VERDE SAIU [Jonathan, 19/11/2026: "corrija o fundo verde,
#     não condiz com nosso padrão visual"]. Eu havia escolhido verde
#     escuro por conta própria. A identidade da casa, consolidada em
#     closer-vendas/referencias/identidade-marca.md a partir das propostas
#     reais, é OUTRA: quase-preto #1A1A1A no texto e no fundo nobre,
#     dourado mostarda #E0A521 nas faixas e títulos, dourado de documento
#     #D4AF37 / #B8860B no detalhe, creme #FDF6E3 e fundo geral BRANCO.
#   ⭐ No desenho: PRETO é a marcenaria, CINZA é o que não é nosso e as
#     cotas, DOURADO marca as duas portas mimetizadas. O dourado aparece
#     pouco e com significado — dourado em tudo não é identidade, é ruído.
TINTA = '#1A1A1A'      # quase-preto da casa
VERDE = '#8E8A80'      # ⚠ o nome é herança do CSS compartilhado; o valor
                       #   é o cinza neutro, e serve às cotas do desenho
TERRA = '#B8860B'      # dourado de documento
MUT = '#8E8A80'
PEDRA = '#EDEAE2'      # bege-cinza · o travertino do nicho e o sóculo
                       # ⚠ o creme #FDF6E3 da casa é fundo de BLOCO DE TEXTO;
                       #   numa área grande de desenho vira amarelo de post-it
RIPA = '#B9B3A8'
FINO, GROSSO, FINISSIMO = 0.9, 1.7, 0.6


def _cot_h(x0, x1, y, txt, cor=VERDE):
    return (f'<path d="M{x0} {y-3.5}V{y+3.5}M{x1} {y-3.5}V{y+3.5}M{x0} {y}H{x1}" '
            f'stroke="{cor}" stroke-width="{FINISSIMO}" fill="none"/>'
            f'<text x="{(x0+x1)/2}" y="{y-5}" font-size="9.5" fill="{cor}" '
            f'text-anchor="middle" font-family="Inter,sans-serif">{txt}</text>')


def desenho():
    s = [f'<svg viewBox="0 0 {VB_W} {VB_H}" xmlns="http://www.w3.org/2000/svg">']
    #   o sóculo de pedra — fora do escopo, e o desenho diz isso
    s.append(f'<rect x="{X0}" y="{Y1}" width="{L}" height="{SOCULO}" '
             f'fill="{PEDRA}" stroke="{MUT}" stroke-width="{FINISSIMO}"/>')
    #   o painel
    s.append(f'<rect x="{X0}" y="{Y0}" width="{L}" height="{A}" '
             f'fill="#FFFFFF" stroke="{TINTA}" stroke-width="{GROSSO}"/>')
    #   ⭐ O RIPADO, RIPA A RIPA, no passo real de 4 cm. O vão de 2 cm é a
    #     sombra: é ele que se desenha, não a ripa.
    x = X0 + b.RIPA_L
    while x + b.RIPA_VAO <= X0 + lv.RIPADO_L:
        topo, alt = Y0, A
        if NIC_X0 <= x < NIC_X1:          # a ripa morre no vão do nicho
            for ty, th in ((Y0, lv.R_SUP), (NIC_Y1, Y1 - NIC_Y1)):
                s.append(f'<rect x="{x}" y="{ty}" width="{b.RIPA_VAO}" '
                         f'height="{th}" fill="{RIPA}"/>')
        else:
            s.append(f'<rect x="{x}" y="{topo}" width="{b.RIPA_VAO}" '
                     f'height="{alt}" fill="{RIPA}"/>')
        x += b.PASSO
    #   o nicho de pedra
    s.append(f'<rect x="{NIC_X0}" y="{NIC_Y0}" width="{lv.NICHO_L}" '
             f'height="{lv.NICHO_H}" fill="{PEDRA}" stroke="{MUT}" '
             f'stroke-width="{FINO}"/>')
    s.append(f'<text x="{(NIC_X0+NIC_X1)/2}" y="{(NIC_Y0+NIC_Y1)/2+3.5}" '
             f'font-size="10" fill="{MUT}" text-anchor="middle" '
             f'letter-spacing="1.6" font-family="Inter,sans-serif">'
             f'NICHO EM MÁRMORE · FORA DO ESCOPO</text>')
    #   a linha onde o ripado acaba — a decisão do Jonathan, desenhada
    s.append(f'<path d="M{NIC_X1} {Y0}V{Y1}" stroke="{TINTA}" '
             f'stroke-width="{FINO}"/>')
    #   as três portas mimetizadas
    def porta(x, w, h, rot):
        y = Y1 - h
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" '
                 f'stroke="{TERRA}" stroke-width="{FINO}" stroke-dasharray="5 3.5"/>')
        s.append(f'<path d="M{x} {Y1}L{x+w} {y}" stroke="{TERRA}" '
                 f'stroke-width="{FINISSIMO}" stroke-dasharray="3 3"/>')
        #   halo branco atrás do texto, para ele sobreviver ao ripado
        s.append(f'<text x="{x+w/2}" y="{Y1-5}" font-size="9" fill="{TERRA}" '
                 f'text-anchor="middle" letter-spacing="1.2" '
                 f'font-family="Inter,sans-serif" paint-order="stroke" '
                 f'stroke="#FFFFFF" stroke-width="4" '
                 f'stroke-linejoin="round">{rot}</text>')
    #   ⭐⭐ AS DUAS BANDAS VIRARAM ARMÁRIO [Jonathan, 18/11/2026] e o
    #     desenho tem de mostrar isso: oito folhas, não uma pele. As
    #     divisões caem dentro do vão de 2 cm do ripado — fechadas, somem —,
    #     mas numa proposta elas precisam ser vistas.
    def banda(y, h, rot):
        s.append(f'<rect x="{NIC_X0}" y="{y}" width="{lv.NICHO_L}" '
                 f'height="{h}" fill="none" stroke="{TERRA}" '
                 f'stroke-width="{FINO}" stroke-dasharray="5 3.5"/>')
        for i in range(1, b.VAOS_BANDA):
            x = NIC_X0 + lv.NICHO_L * i / b.VAOS_BANDA
            s.append(f'<path d="M{x} {y}V{y+h}" stroke="{TERRA}" '
                     f'stroke-width="{FINISSIMO}" stroke-dasharray="4 3"/>')
        s.append(f'<text x="{(NIC_X0+NIC_X1)/2}" y="{y+h/2+3}" font-size="9" '
                 f'fill="{TERRA}" text-anchor="middle" letter-spacing="1.2" '
                 f'font-family="Inter,sans-serif" paint-order="stroke" '
                 f'stroke="#FFFFFF" stroke-width="4" '
                 f'stroke-linejoin="round">{rot}</text>')
    banda(Y0, lv.R_SUP, 'ARMÁRIO SUPERIOR · 4 FOLHAS')
    banda(NIC_Y1, Y1 - NIC_Y1, 'ARMÁRIO INFERIOR · 4 FOLHAS')
    porta(X0, lv.R_PORTA_L, A, 'ARMÁRIO')
    porta(X0 + 366, 83, 210, 'PORTA')
    porta(X0 + 592, 70, 210, 'PORTA')
    #   as cotas
    s.append(_cot_h(X0, NIC_X1, Y0 - 9, 'RIPADO · 352'))
    s.append(_cot_h(NIC_X1, X1, Y0 - 9, f'LISO · {lv.LISO_L:.0f}', TERRA))
    s.append(_cot_h(X0, X1, Y1 + SOCULO + 9, '682'))
    s.append(f'<path d="M{X0-10} {Y0}H{X0-2}M{X0-10} {Y1}H{X0-2}'
             f'M{X0-6} {Y0}V{Y1}" stroke="{VERDE}" stroke-width="{FINISSIMO}" '
             f'fill="none"/>'
             f'<text x="{X0-9}" y="{(Y0+Y1)/2}" font-size="9.5" fill="{VERDE}" '
             f'text-anchor="middle" font-family="Inter,sans-serif" '
             f'transform="rotate(-90 {X0-9} {(Y0+Y1)/2})">277</text>')
    s.append('</svg>')
    return ''.join(s)



# ════════════════════════════════════════════════════════════════════════
# O CONTEÚDO
# ════════════════════════════════════════════════════════════════════════
ITENS = [
 ('Os dois armários do nicho', '302 cm, acima e abaixo da pedra',
  'Dois armários de <b>50 cm de profundidade</b> emoldurando o nicho: o '
  '<b>superior</b> — 302 × 75, a 2,17 m do piso — e o <b>inferior</b> — '
  '302 × 71 —, cada um em <b>quatro folhas de giro</b>, com caixa, prateleira '
  'e ferragem em cada vão. As oito folhas são ripadas no mesmo passo e a junta '
  'cai dentro do vão de 2 cm: fechadas, elas somem.'),
 ('Armário lateral', '50 × 277 × 50, folha inteira',
  'Coluna inteira atrás de uma única folha ripada de <b>2,77 m</b>, com cinco '
  'prateleiras. Dobradiças Blum e alma de aço contra empeno, que uma folha '
  'dessa altura pede.'),
 ('Painel liso e as duas portas de passagem', '330 cm, do nicho para a direita',
  'Do fim da pedra para a direita <b>o painel é liso, sem ripa</b> — é a '
  'região das <b>duas portas pivotantes</b>. As folhas de <b>83 × 210</b> e '
  '<b>70 × 210</b> são tamponadas em <b>42 mm</b>, com marco mimetizado e '
  'sistema pivô, e fecham alinhadas ao painel.'),
]

#   ⛔ AS OITO ETAPAS SÃO AS DA CASA, copiadas de `proposta-aline.html`. Só a
#     etapa 2 foi adaptada ao projeto, porque é a que cita o executivo.
ETAPAS = [
 ('Alinhamento', 'Entendemos o escopo e o ambiente antes de qualquer número. '
  'A visita define o que será executado.'),
 ('Detalhamento técnico', 'O executivo vira instrução de fábrica. Cada medida '
  'conferida no local, em ' + b.OBRA + '.'),
 ('Programação', 'Data de produção definida antes de iniciar, com prazo '
  'comunicado.'),
 ('Produção', 'Corte, montagem e furação com os processos acumulados em anos '
  'de fábrica.'),
 ('Acabamento', 'Borda, superfície e detalhe revisados antes de o módulo '
  'entrar em embalagem.'),
 ('Conferência', 'Cada peça testada, cada ferragem montada e verificada antes '
  'de sair da fábrica.'),
 ('Entrega e montagem', 'Equipe própria. Do caminhão ao parafuso final — sem '
  'terceirização de montagem.'),
 ('Compromisso contínuo', 'Ferragem tem garantia. Dúvida tem resposta. A '
  'relação não encerra na entrega.'),
]

ENTRADA = b.PRECO_FECHADO * b.PAGAMENTO[0][1]
SALDO = b.PRECO_FECHADO * b.PAGAMENTO[1][1]

_itens = ''.join(
  f'<div class="cj"><div class="n">{i:02d}</div>'
  f'<div><div class="t">{n} · <span style="color:var(--mut)">{s}</span></div>'
  f'<div class="d">{d}</div></div></div>'
  for i, (n, s, d) in enumerate(ITENS, 1))
_etapas = ''.join(
  f'<div class="et"><div class="n">{i:02d}</div><div class="t">{t}</div>'
  f'<div class="d">{d}</div></div>'
  for i, (t, d) in enumerate(ETAPAS, 1))

CSS_X = '''
/* ── A PALETA DA CASA ────────────────────────────────────
   ⛔ css-brinquedoteca.css é COMPARTILHADO com outras propostas: mexer
   nele mudaria a folha de outros clientes. Então eu redefino os valores
   aqui, só nesta proposta. Os NOMES das variáveis continuam os de lá. */
:root{
  --tinta:#1A1A1A; --verde:#1A1A1A; --verde-lt:#6B6B6B;
  --terra:#B8860B; --papel:#FFFFFF; --linha:#E6E2D8; --mut:#8E8A80;
  --ouro:#E0A521; --ouro-dc:#D4AF37; --creme:#FDF6E3;
}
.cv{color:var(--creme);}
.cv .sel{color:var(--ouro);}

/* ── capa ───────────────────────────────────────────────────────────── */
.cv .ph{flex:none;height:152mm;}
.cv .ph img{object-position:left center;}
.cv .pe{padding:14mm 19mm 12mm;}
.cv .nm{font-size:31pt;line-height:1.06;letter-spacing:-.028em;margin-top:4mm;}
.cv .nm em{font-style:italic;color:var(--ouro-dc);}
.cv .sub{margin-top:6mm;color:#CFC9BD;font-size:9.4pt;max-width:128mm;
  line-height:1.6;}
.cv .fat{display:grid;grid-template-columns:repeat(3,1fr);gap:0 8mm;
  margin-top:9mm;}
.cv .fat .k{font-size:6.2pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--ouro);font-weight:600;}
.cv .fat .v{font-family:'Fraunces',Georgia,serif;font-size:15pt;font-weight:300;
  color:var(--creme);margin-top:2mm;line-height:1.15;
  font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1,'onum' 0;}
.cv .fat .v small{display:block;font-family:'Inter',sans-serif;font-size:7.2pt;
  color:#A8A29A;margin-top:1.4mm;letter-spacing:0;}
.cv .rod{display:flex;justify-content:space-between;margin-top:8mm;
  padding-top:4mm;border-top:1px solid rgba(255,255,255,.14);font-size:6.6pt;
  letter-spacing:.24em;text-transform:uppercase;color:var(--ouro);}
/* ── miolo ──────────────────────────────────────────────────────────── */
.in{padding:13mm 19mm 5mm;}
h2.tt{font-size:21pt;line-height:1.12;margin-top:3mm;letter-spacing:-.018em;}
h2.tt em{font-style:italic;color:var(--verde);}
.lead{font-size:8.6pt;color:var(--verde-lt);margin-top:3.5mm;max-width:150mm;
  line-height:1.6;}
.lead b{color:var(--tinta);font-weight:500;}
.des{width:162mm;margin:5mm auto 1mm;}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:0 5mm;margin-top:3.6mm;}
.duo .ph{aspect-ratio:1.66/1;position:relative;}
.duo .ph img{width:100%;height:100%;object-fit:cover;}
.duo .ph span{position:absolute;left:0;bottom:0;background:var(--verde);
  color:#DCD6CA;font-size:5.6pt;letter-spacing:.2em;text-transform:uppercase;
  padding:1.2mm 2.4mm;}
.cj{padding:1.9mm 0;grid-template-columns:7mm 1fr;}
.cj .t{font-size:9.4pt;}
.cj .d{font-size:7.1pt;line-height:1.42;margin-top:.9mm;max-width:154mm;}
.nota{margin-top:3.5mm;padding:3.4mm 5mm;background:var(--creme);
  border-left:2px solid var(--terra);border-radius:2px;}
.nota .k{font-size:6.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--terra);font-weight:600;}
.nota .t{font-size:7.2pt;line-height:1.5;color:var(--verde-lt);margin-top:1.8mm;}
.nota .t b{color:var(--tinta);font-weight:600;}
/* ── etapas ─────────────────────────────────────────────────────────── */
.etapas{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm 6mm;
  margin-top:6mm;}
.et .n{font-family:'Fraunces',Georgia,serif;font-size:15pt;font-weight:300;
  color:var(--terra);line-height:1;}
.et .t{font-size:8.4pt;font-weight:600;margin-top:1.8mm;letter-spacing:-.005em;}
.et .d{font-size:7pt;line-height:1.45;color:var(--verde-lt);margin-top:1.4mm;}
/* ── garantia ───────────────────────────────────────────────────────── */
.gar{margin-top:7mm;display:grid;grid-template-columns:40mm 1fr;gap:0 8mm;
  align-items:start;padding-top:5mm;border-top:1.4px solid var(--tinta);}
.gar .big{font-family:'Fraunces',Georgia,serif;font-size:40pt;font-weight:300;
  line-height:.92;letter-spacing:-.03em;color:var(--verde);
  font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1,'onum' 0;}
.gar .big span{display:block;font-family:'Inter',sans-serif;font-size:6.6pt;
  letter-spacing:.26em;text-transform:uppercase;color:var(--verde-lt);
  font-weight:600;margin-top:2.5mm;}
.gar .tx{font-size:7.6pt;line-height:1.55;color:var(--verde-lt);}
.gar .tx b{color:var(--tinta);font-weight:600;}
.gar .tx + .tx{margin-top:2.6mm;}
/* ── investimento e condições ───────────────────────────────────────── */
.tot{margin-top:6mm;background:var(--verde);color:var(--creme);padding:4mm 6mm;
  display:flex;align-items:center;justify-content:space-between;}
.tot .k{font-size:6.6pt;letter-spacing:.3em;text-transform:uppercase;
  color:#A8A29A;font-weight:500;}
.tot .t{font-size:8.8pt;color:#D8D2C6;margin-top:1.6mm;}
.tot .t b{color:#fff;font-weight:500;}
.tot .gv{font-size:7.4pt;color:#A8A29A;margin-top:1.4mm;}
.tot .gv b{color:#fff;font-weight:500;}
.tot .v{font-family:'Fraunces',Georgia,serif;font-size:26pt;font-weight:300;
  letter-spacing:-.025em;white-space:nowrap;padding-left:8mm;
  font-variant-numeric:lining-nums;font-feature-settings:'lnum' 1,'onum' 0;}
.gr{grid-template-columns:repeat(4,1fr);gap:0 6mm;margin-top:4mm;}
.gr .k{font-size:6.1pt;letter-spacing:.24em;}
.gr .v{font-size:7pt;line-height:1.44;margin-top:1.2mm;}
.fora{margin-top:4mm;padding:3.6mm 5mm;}
.fora .k{font-size:6.4pt;}
.lst{font-size:7pt;line-height:1.4;margin-top:2.2mm;}
.lst li{margin-bottom:1mm;}
.fecho{margin-top:auto;padding-top:6mm;display:grid;
  grid-template-columns:1fr 1fr;gap:0 7mm;align-items:center;}
.fecho .ph{aspect-ratio:2.33/1;}
.fecho .ph img{width:100%;height:100%;object-fit:cover;}
.fecho .k{font-size:6.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--terra);font-weight:600;}
.fecho .d{font-size:7.6pt;line-height:1.55;color:var(--verde-lt);margin-top:2.2mm;}
.fecho .d b{color:var(--tinta);font-weight:600;}
.pe2{margin-top:auto;padding-top:3mm;font-size:6.2pt;letter-spacing:.18em;}
.pe2 span{white-space:nowrap;}
'''

HTML = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Painel da Sala · Proposta Valvic</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}{CSS_X}</style></head><body>

<!-- ─────────────────────────────── 1 · CAPA ─────────────────────────── -->
<div class="pg cv"><div class="in">
  <div class="ph"><img src="{IMG['capa']}" alt=""></div>
  <div class="pe">
    <div class="sel">Proposta de marcenaria · Sala</div>
    <h1 class="nm disp">Painel ripado sob medida,<br>
      <em>emoldurando o nicho de travertino.</em></h1>
    <div class="sub"><b>6,82 m</b> de parede em <b>MDF Gianduia Trama</b>, com
      <b>três armários mimetizados</b> e <b>duas portas de passagem</b> que
      desaparecem no ripado.</div>
    <div class="fat">
      <div><div class="k">Obra</div><div class="v">{b.OBRA}
        <small>conferência técnica e instalação inclusas</small></div></div>
      <div><div class="k">Entrega</div><div class="v">{b.PRAZO_DIAS} dias
        <small>corridos, da assinatura</small></div></div>
      <div><div class="k">Garantia</div><div class="v">{b.GARANTIA_ANOS} anos
        <small>sobre marcenaria e ferragem</small></div></div>
    </div>
    <div class="rod"><span>Valvic Marcenaria</span>
      <span>{DATA} · validade de {b.VALIDADE_DIAS} dias</span></div>
  </div>
</div></div>

<!-- ─────────────────────────────── 2 · O PAINEL ─────────────────────── -->
<div class="pg"><div class="in">
  <div class="sel">O painel · executivo SALA · VISTA 2</div>
  <h2 class="tt disp">Seis metros e oitenta e dois,<br>
    <em>num plano só.</em></h2>
  <div class="lead">O ripado corre da esquerda <b>até onde a pedra termina</b>,
    em 352 cm. Dali para a direita o painel é <b>liso</b> — é a região das duas
    portas pivotantes. A pedra, o sóculo e o rodapé são da marmoraria; o vão
    sai da fábrica pronto para recebê-los.</div>

  <div class="des">{desenho()}</div>

  <div class="duo">
    <div class="ph"><img src="{IMG['3d-parede']}" alt=""><span>A parede inteira · estudo 3D</span></div>
    <div class="ph"><img src="{IMG['3d-nicho']}" alt=""><span>O nicho de travertino</span></div>
  </div>

  {_itens}

  <div class="nota">
    <div class="k">Atenção · o que esta proposta acrescenta ao executivo</div>
    <div class="t"><b>Os armários não aparecem nas pranchas.</b> O executivo
    desenha o painel como superfície contínua: os <b>três armários</b> — nove
    folhas ao todo, acima e abaixo do nicho e na coluna lateral — são acréscimo
    desta proposta, com caixa, prateleira e ferragem em cada vão. As nove folhas
    <b>abrem por toque, com Blum Tip-on</b>, sem puxador aparente, para que o
    ripado corra inteiro de ponta a ponta.</div>
  </div>

  <div class="pe2"><span>Valvic Marcenaria</span>
    <span>{b.OBRA} · {DATA}</span></div>
</div></div>

<!-- ───────────────── 3 · PROCESSO, GARANTIA E INVESTIMENTO ──────────── -->
<div class="pg"><div class="in">
  <div class="sel">Como trabalhamos</div>
  <h2 class="tt disp">Oito etapas, e nenhuma<br>
    <em>terceirizada na montagem.</em></h2>

  <div class="etapas">{_etapas}</div>

  <div class="gar">
    <div><div class="big">{b.GARANTIA_ANOS}<span>anos de garantia</span></div></div>
    <div>
      <div class="tx">A escada de garantia da Valvic <b>sobe com a ferragem</b>,
        e este projeto é <b>Blum de ponta a ponta</b> — dobradiça e pulsador.
        São <b>200 mil ciclos de ensaio</b> na dobradiça: abrir e fechar vinte
        vezes por dia durante vinte e sete anos.</div>
      <div class="tx"><b>O prazo é nosso, não do fabricante.</b> A garantia é
        sobre a marcenaria: quem responde é a casa que desenhou, produziu e
        instalou. <b>Instalações e regulagens: 2 anos.</b> Atendimento com
        retorno em <b>24 horas</b> e visita em até <b>3 dias úteis</b>, sem
        custo dentro do prazo. O termo é assinado na entrega, junto do guia de
        conservação.</div>
    </div>
  </div>

  <div class="tot">
    <div><div class="k">Investimento · o painel completo</div>
      <div class="t"><b>R$ {br(ENTRADA)}</b> na assinatura ·
        <b>R$ {br(SALDO)}</b> na entrega</div>
      <div class="gv">Preço <b>com conferência técnica e instalação em
        {b.OBRA}</b> — deslocamento, equipe e estadia inclusos.</div></div>
    <div class="v">R$ {br(b.PRECO_FECHADO)}</div>
  </div>

  <div class="gr">
    <div><div class="k">Conferência técnica</div><div class="v">
      Antes do corte, <b>no local</b>. É ela que transforma a cota da prancha em
      medida de fábrica — e é nossa.</div></div>
    <div><div class="k">Entrega e instalação</div><div class="v">
      <b>{b.PRAZO_DIAS} dias corridos</b> da assinatura, com instalação em
      {b.OBRA} por <b>equipe própria</b>.</div></div>
    <div><div class="k">Abertura e ferragem</div><div class="v">
      Nove folhas de armário <b>por toque, com Blum Tip-on</b>. Dobradiças
      <b>Blum</b>; as duas de passagem são pivotantes.</div></div>
    <div><div class="k">Validade</div><div class="v">
      <b>{b.VALIDADE_DIAS} dias corridos</b> para esta proposta. Depois disso
      os valores são reconfirmados com a fábrica.</div></div>
  </div>

  <div class="fora"><div class="k">O que não está nesta proposta</div>
  <ul class="lst">
    <li><b>Toda a pedra.</b> O nicho de <b>131 × 302 em mármore travertino
      romano</b>, o sóculo em alvenaria revestido e o rodapé de 15 cm.</li>
    <li><b>A iluminação do nicho.</b> A prancha pede <i>prever</i> fita de LED
      3000 K: deixamos o rasgo e a passagem; a fita, a fonte e o acionamento
      são do elétrico.</li>
    <li><b>A janela 202 × 175</b> em vidro laminado com estrutura metálica, e
      toda a <b>alvenaria, elétrica e revestimento</b> — inclusive os pontos de
      fixação na parede.</li>
  </ul></div>

  <div class="fecho">
    <div class="ph"><img src="{IMG['rodape']}" alt=""></div>
    <div class="tx"><div class="k">O próximo passo</div>
      <div class="d">Com a proposta aprovada, marcamos a <b>conferência técnica
      em {b.OBRA}</b> e a partir dela nasce o plano de corte. Estamos à
      disposição para apresentar o projeto pessoalmente e responder o que
      for preciso.</div></div>
  </div>

  <div class="pe2"><span>Valvic Marcenaria</span>
    <span>{b.OBRA} · {DATA} · validade de {b.VALIDADE_DIAS} dias</span></div>
</div></div>
</body></html>'''

SAIDA = P / 'proposta-painel-sala.html'
PDF = P / 'Painel da Sala · Proposta Valvic.pdf'
SAIDA.write_text(HTML, encoding='utf-8')
subprocess.run(['node', str(P.parent / 'render-pdf.js'), str(SAIDA), str(PDF)],
               check=True, env=dict(os.environ,
                                    NODE_PATH='/opt/node22/lib/node_modules'))
print(f'  {"PAINEL DA SALA · proposta de três páginas":<44}')
print(f'    {"PREÇO FECHADO":<32}{"R$ " + br(b.PRECO_FECHADO):>16}')
print(f'    {"custo direto":<32}{"R$ " + br(lv.DIRETO):>16}')
print(f'    {"MC lida · com RT":<32}{lv.MC*100:>15.2f}%')
print(f'    {"MC lida · sem RT":<32}{lv.MC_SEM_RT*100:>15.2f}%')
print(f'    {"garantia":<32}{str(b.GARANTIA_ANOS) + " anos":>16}')
print(f'  → {PDF}')
