# -*- coding: utf-8 -*-
"""PAINEL DA SALA — VISTA 2 · a proposta de uma página.

⭐ [Jonathan, 17/11/2026] "vamos vender por 53.000 esse projeto / deixe claro
  na proposta que é com a conferencia tecnica e instalação em Governador
  Valadares" e, logo depois, "alias, por 49.800".

⭐⭐ O DESENHO SAI DAS MESMAS COTAS QUE O ORÇAMENTO USA. O ripado é
  desenhado ripa a ripa, no passo real de 4 cm, e PARA onde a pedra acaba —
  que foi a decisão dele. O cliente vê a diferença entre o trecho ripado e
  o liso sem precisar ler uma linha.
"""
import pathlib, subprocess, os, importlib.util, datetime

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

TINTA, VERDE, TERRA, MUT, PEDRA = '#16211B', '#2C4034', '#B0704E', '#8E8A80', '#EDEAE2'
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
# A FOLHA
# ════════════════════════════════════════════════════════════════════════
ITENS = [
 ('Painel ripado', '352 cm, até onde a pedra termina',
  'Ripado em <b>MDF Gianduia Trama</b>, ripa de 2 cm e vão de 2 cm, sobre base '
  'da mesma cor — porque o vão tem 2 cm de profundidade e o fundo é visto. '
  'São <b>162 ripas</b> e <b>292 m de fita filetada</b> nas duas faces de cada uma.'),
 ('Porta do armário', '50 × 277, mimetizada no ripado',
  'Folha inteira, ripada na mesma trama e na mesma linha das ripas do painel: '
  'fechada, ela <b>não existe</b>. Dobradiças Hettich Sensys e alma de aço contra '
  'empeno, que 2,77 m de altura pedem.'),
 ('Painel liso e as duas portas de passagem', '330 cm, do nicho para a direita',
  'Face melamínica lisa, sem ripa. As duas folhas de passagem — <b>83 × 210</b> e '
  '<b>70 × 210</b> — são <b>tamponadas em 42 mm</b>, com marco mimetizado e '
  'sistema pivô, e fecham alinhadas ao painel.'),
 ('Estrutura de fixação', 'montantes e travessas',
  'Montantes a cada 60 cm e três fiadas de travessa, em MDF, chumbados na '
  'alvenaria — é o que mantém 6,82 m de painel num plano só.'),
]
linhas = ''.join(
  f'<div class="cj"><div class="n">{i:02d}</div>'
  f'<div><div class="t">{n} · <span style="color:var(--mut)">{s}</span></div>'
  f'<div class="d">{d}</div></div></div>'
  for i, (n, s, d) in enumerate(ITENS, 1))

ENTRADA = b.PRECO_FECHADO * b.PAGAMENTO[0][1]
SALDO = b.PRECO_FECHADO * b.PAGAMENTO[1][1]

HTML = f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Painel da Sala · Proposta Valvic</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{CSS}
.in{{padding:12mm 19mm 7mm;}}
.ttl{{font-size:22pt;margin-top:3mm;line-height:1.1;}}
.sub1{{font-size:8.4pt;color:var(--verde-lt);margin-top:3.2mm;}}
.sub1 b{{color:var(--tinta);font-weight:500;}}
.des{{width:134mm;margin:5mm auto 0;}}
.des svg{{width:100%;height:auto;display:block;}}
.cj{{padding:1.8mm 0;grid-template-columns:7mm 1fr;}}
.cj .t{{font-size:9.4pt;}}
.cj .d{{font-size:7.1pt;line-height:1.44;margin-top:.9mm;max-width:148mm;}}
.tot{{margin-top:4mm;background:var(--verde);color:#F4F2EC;padding:4mm 6mm;
  display:flex;align-items:center;justify-content:space-between;}}
.tot .k{{font-size:6.6pt;letter-spacing:.3em;text-transform:uppercase;
  color:#A9BFAF;font-weight:500;}}
.tot .t{{font-size:8.8pt;color:#D3DDD5;margin-top:1.6mm;}}
.tot .t b{{color:#fff;font-weight:500;}}
.tot .gv{{font-size:7.6pt;color:#A9BFAF;margin-top:1.4mm;}}
.tot .gv b{{color:#fff;font-weight:500;}}
.tot .v{{font-family:'Fraunces',Georgia,serif;font-size:25pt;font-weight:300;
  letter-spacing:-.025em;white-space:nowrap;padding-left:8mm;}}
.gr{{grid-template-columns:repeat(4,1fr);gap:0 6mm;margin-top:4mm;}}
.gr .k{{font-size:6.1pt;letter-spacing:.24em;}}
.gr .v{{font-size:7.1pt;line-height:1.42;margin-top:1.2mm;}}
.fora{{margin-top:3.5mm;padding:4mm 5.5mm;}}
.fora .k{{font-size:6.4pt;}}
.lst{{font-size:7pt;line-height:1.4;margin-top:2.2mm;}}
.lst li{{margin-bottom:1mm;}}
.pe2{{margin-top:auto;padding-top:3mm;font-size:6.2pt;letter-spacing:.18em;}}
.pe2 span{{white-space:nowrap;}}
</style></head><body>

<div class="pg"><div class="in">
  <div class="sel">Proposta de marcenaria · Sala</div>
  <h1 class="ttl disp">Uma parede de 6,82 m —<br>
    <em>e três portas que ela esconde.</em></h1>
  <div class="sub1">Executivo <b>SALA · VISTA 2</b> (1/50) e <b>NICHO RIPADO</b>
    (1/30, pág. 18) · obra em <b>{b.OBRA}</b></div>

  <div class="des">{desenho()}</div>

  {linhas}

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
      Antes do corte, <b>no local, em {b.OBRA}</b>. É ela que transforma a
      cota da prancha em medida de fábrica — e é nossa.</div></div>
    <div><div class="k">Entrega e instalação</div><div class="v">
      <b>{b.PRAZO_DIAS} dias corridos</b> da assinatura. <b>Instalação em
      {b.OBRA}</b> por equipe própria, com deslocamento e estadia já no
      preço.</div></div>
    <div><div class="k">Acabamento</div><div class="v">
      <b>MDF Gianduia Trama · Duratex</b>, conforme o executivo. Fita de borda
      na mesma cor em toda face aparente, inclusive nas duas faces de cada
      ripa.</div></div>
    <div><div class="k">Garantia</div><div class="v">
      <b>10 anos</b> sobre marcenaria e ferragem — o prazo da linha Hettich,
      que é a ferragem deste projeto.</div></div>
  </div>

  <div class="fora"><div class="k">O que não está nesta proposta</div>
  <ul class="lst">
    <li><b>Toda a pedra.</b> O nicho de <b>131 × 302 em mármore travertino
      romano</b>, o sóculo em alvenaria revestido e o rodapé de 15 cm. O painel
      é entregue com o vão pronto para recebê-los.</li>
    <li><b>A iluminação do nicho.</b> A prancha pede <i>prever</i> fita de LED
      3000 K: deixamos o rasgo e a passagem; a fita, a fonte e o acionamento
      são do elétrico.</li>
    <li><b>A janela 202 × 175</b> em vidro laminado com estrutura metálica.</li>
    <li><b>Alvenaria, elétrica e revestimento</b>, inclusive os pontos de
      fixação na parede.</li>
  </ul></div>

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
print(f'  {"PAINEL DA SALA · proposta de uma página":<44}')
print(f'    {"PREÇO FECHADO":<32}{"R$ " + br(b.PRECO_FECHADO):>16}')
print(f'    {"custo direto":<32}{"R$ " + br(lv.DIRETO):>16}')
print(f'    {"  logística de " + b.OBRA:<32}{"R$ " + br(b.CUSTO_GV):>16}')
print(f'    {"MC lida · com RT":<32}{lv.MC*100:>15.2f}%')
print(f'    {"MC lida · sem RT":<32}{lv.MC_SEM_RT*100:>15.2f}%')
print(f'  → {PDF}')
