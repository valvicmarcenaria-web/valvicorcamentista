# -*- coding: utf-8 -*-
"""ANA CAROLINA · APTO CV — proposta do rack da sala  [22/10/2026]

⭐ [Jonathan 21/10] "vamos orçar esse rack considerando o tamanho de 2.30 /
   uma versão com as portas com acabamento em palha natural e outra sem."

   → DUAS PÁGINAS, DUAS VERSÕES. A versão com palha é a do projeto — é o
     que o render da própria prancha mostra — e por isso fica no bloco
     escuro, com o número grande. A lisa vem logo abaixo, como alternativa.
   → CSS próprio, paleta do móvel: madeirado, palha e espresso.
   → IMAGENS: os dois renders vêm INCORPORADOS na folha 13/3 da prancha do
     Estúdio Gráza. São do projeto da cliente, como no Michelle e Arlei.

Números de `corte-apto-cv-rack.py`; nada digitado à mão.
⛔ Sem metragem e sem quantitativo. A ÚNICA medida citada é a largura de
   2,30 m, que é ESCOPO — foi ela que o Jonathan pediu e é o que define o
   que está sendo comprado. Auditar com --excecoes "2,30 m".
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('cv', P/'corte-apto-cv-rack.py')
cv = importlib.util.module_from_spec(spec); sys.modules['cv'] = cv
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(cv)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, OBRA = 'Ana Carolina', 'Sala de estar · Apto CV'
ARQ, ESCRIT   = 'Bruna Rezende', 'Estúdio Gráza'
DATA          = '22 de outubro de 2026'
PRAZO, VALIDADE, GARANTIA = '40 dias corridos', '7 dias úteis', '5 anos'
LARGURA = '2,30 m'
NP = 2
PALHA, LISA = cv.PV_PALHA, cv.PV_LISA

# ⛔⛔ TRAVAS. Aqui não há soma de itens para fechar — há UM móvel em DUAS
#   versões. O que pode mudar calado embaixo da folha é a base do preço.
assert PALHA == cv.PALHA['preco'](), '⛔ O PREÇO DA PALHA NÃO VEIO DO MOTOR'
assert LISA  == cv.LISA['preco'](),  '⛔ O PREÇO DA LISA NÃO VEIO DO MOTOR'
assert PALHA > LISA > 0,     '⛔ A VERSÃO COM PALHA FICOU MAIS BARATA'
assert abs(cv.MC_ALVO - 0.40) < 1e-9, f'⛔ A MC MUDOU: {cv.MC_ALVO:.3f}'
assert cv.RT_ON is True,     '⛔ A RT SAIU DA CASCATA'
assert cv.L_TOT == 230.0,    '⛔ A LARGURA NÃO É MAIS 2,30 m [Jonathan 21/10]'
assert cv.N_PORTA == 4 and cv.N_MOD == 5, '⛔ A COMPOSIÇÃO MUDOU'
# ⛔ "SE ESTÁ NO TEXTO, TEM DE ESTAR NA CONTA": a folha promete fecho-toque,
#   pistão a gás, metalon de fixação e rebaixo com palha. Se o motor perder
#   qualquer um deles, a proposta estaria vendendo o que não foi orçado.
assert cv.TOQUE > 0 and cv.BASCULA > 0,  '⛔ O FECHO-TOQUE OU O PISTÃO SUMIU'
assert cv.FIXA_M > 0,                    '⛔ A FIXAÇÃO SUSPENSA SUMIU'
assert sum(cv.PALHA['pal'].values()) > 0, '⛔ A PALHA SUMIU DA CONTA'
assert cv.ESP == 1.8, '⛔ O CORPO DEIXOU DE SER TODO EM 18 mm'

IMG = P/'img-apto-cv'
def b64(nome):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((IMG/nome).read_bytes()).decode())
HERO = b64('cv-rack.jpg')

ITENS = [
 ('Corpo', 'Suspenso, <b>sem tocar o piso</b>, em MDF madeirado no padrão '
  'que a arquiteta definir. Tampo, base, laterais e divisórias <b>todos em '
  '18 mm</b> — a estrutura inteira na espessura que a casa reserva para '
  'tampo. O interior acompanha o madeirado das frentes, não vai em branco.'),
 ('Frentes', 'Portas basculantes sobre <b>pistão a gás</b>: abrem devagar e '
  'param onde a mão solta. Sem puxador aparente — abrem por '
  '<b>fecho-toque</b>, para a frente ficar limpa de ponta a ponta.'),
 ('Nicho', 'Um módulo <b>aberto</b>, no mesmo madeirado por dentro. Em móvel '
  'aberto a caixaria <b>é</b> o acabamento: não existe face escondida.'),
 ('Fixação', 'Barra contínua de <b>metalon</b> chumbada na alvenaria por trás '
  'do painel. O móvel fica pendurado na <b>estrutura</b>, não no painel — é '
  'o que sustenta um rack suspenso carregado de equipamento.'),
 ('Fiação', 'Passagem de cabos por trás e <b>rasgo de ventilação no fundo</b>. '
  'Receiver e conversor esquentam atrás de porta fechada; o ar tem de ter '
  'por onde sair.'),
]

CSS = """
:root{
  --esp:#2B2420; --mad:#A5703F; --mad-lt:#D8B183; --palha:#D9CBAE;
  --ink:#1E1A17; --soft:#5B5349; --mut:#948B7E; --hair:#EDE6DA;
  --line:#DCD3C4; --cream:#F7F2E9; --paper:#fff;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);
     font-size:9.5pt;line-height:1.6;}
.serif{font-family:'Cormorant Garamond',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;
      background:var(--paper);page-break-after:always;}
.page:last-of-type{page-break-after:avoid;}
.pad{padding:16mm 18mm 12mm;height:100%;display:flex;flex-direction:column;}
.pad.p2{padding-top:13mm;}
.foot{margin-top:auto;padding-top:5mm;border-top:1px solid var(--hair);
      display:flex;justify-content:space-between;font-size:7pt;
      letter-spacing:.18em;text-transform:uppercase;color:var(--mut);flex:none;}

/* ── página 1 · escura ──────────────────────────────────────────────── */
.dk{background:var(--esp);color:#F4EEE4;}
.dk .foot{border-top:1px solid rgba(255,255,255,.16);color:#8E8578;}
.mark{font-size:8.4pt;letter-spacing:.42em;text-transform:uppercase;
  color:#F0E7D7;font-weight:700;flex:none;}
.kick{font-size:7pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--mad-lt);font-weight:700;flex:none;}
.dk h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:46pt;
  line-height:.98;font-weight:600;letter-spacing:-.025em;margin:4mm 0 0;flex:none;}
.dk .sub{font-size:10.5pt;color:#C6BCAE;margin-top:4.5mm;font-weight:300;flex:none;}
.dk .sub b{color:#ECE3D4;font-weight:500;}
.hero{margin-top:6mm;height:46mm;border-radius:3px;overflow:hidden;flex:none;}
.hero img{width:100%;height:100%;object-fit:cover;object-position:16% 56%;
  display:block;}
.vrow{display:grid;grid-template-columns:32mm 1fr;gap:7mm;align-items:baseline;
  padding:4.4mm 0;border-top:1px solid rgba(255,255,255,.14);flex:none;}
.vrow .k{font-size:7pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--mad-lt);font-weight:700;padding-top:2.4mm;}
.vrow .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;
  font-weight:600;line-height:1.05;letter-spacing:-.01em;color:#fff;}
.vrow .d{color:#BEB5A7;font-size:8.8pt;line-height:1.52;margin-top:1.8mm;
  max-width:122mm;}
.vrow .d b{color:#F2EADC;font-weight:600;}
.meta{display:grid;grid-template-columns:repeat(4,1fr);gap:6mm;
  padding-top:5.5mm;border-top:1px solid rgba(255,255,255,.3);flex:none;}
.meta .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--mad-lt);font-weight:700;}
.meta .v{font-size:10.5pt;font-weight:600;margin-top:1.2mm;color:#F4EEE4;}

/* ── página 2 · clara ───────────────────────────────────────────────── */
.hd{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1.6px solid var(--ink);padding-bottom:3.2mm;flex:none;}
.hd .b{font-size:8pt;letter-spacing:.4em;text-transform:uppercase;font-weight:700;}
.hd .m{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.eye{font-size:7pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--mad);font-weight:700;margin-top:4mm;flex:none;}
.h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:21pt;
  line-height:1.04;font-weight:600;letter-spacing:-.02em;margin-top:1.6mm;flex:none;}
.h1 i{font-style:normal;color:var(--mad);}
.rows{margin-top:4.4mm;flex:none;}
.row{display:grid;grid-template-columns:24mm 1fr;gap:6mm;align-items:baseline;
  padding:2.1mm 0;border-top:1px solid var(--line);}
.row .k{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;
  font-weight:700;color:var(--mad);line-height:1;padding-top:.5mm;}
.row .d{color:var(--soft);font-size:8.4pt;line-height:1.44;}
.row .d b{color:var(--ink);font-weight:600;}

.band{margin-top:4mm;background:var(--esp);color:#F4EEE4;border-radius:3px;
  padding:4.2mm 7mm;display:flex;justify-content:space-between;
  align-items:flex-end;gap:8mm;flex:none;}
.band .lab{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--mad-lt);font-weight:700;}
.band .nm{font-family:'Cormorant Garamond',Georgia,serif;font-size:19pt;
  font-weight:600;color:#fff;line-height:1.05;margin-top:1.4mm;}
.band .s{font-size:8.4pt;color:#C2B8A9;margin-top:2mm;max-width:96mm;
  line-height:1.46;}
.band .s b{color:#F1E9DB;font-weight:600;}
.band .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:32pt;
  font-weight:700;color:#fff;line-height:.92;letter-spacing:-.025em;
  font-variant-numeric:tabular-nums;white-space:nowrap;}
.alt{margin-top:2.6mm;background:var(--cream);border-radius:3px;padding:3.6mm 7mm;
  display:flex;justify-content:space-between;align-items:flex-end;gap:8mm;
  flex:none;}
.alt .lab{font-size:7pt;letter-spacing:.24em;text-transform:uppercase;
  color:var(--mad);font-weight:700;}
.alt .nm{font-family:'Cormorant Garamond',Georgia,serif;font-size:17pt;
  font-weight:600;line-height:1.05;margin-top:1.2mm;}
.alt .s{font-size:8.2pt;color:var(--soft);margin-top:1.6mm;max-width:100mm;
  line-height:1.44;}
.alt .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:24pt;
  font-weight:700;line-height:.92;letter-spacing:-.02em;
  font-variant-numeric:tabular-nums;white-space:nowrap;}
.pay{margin-top:3.4mm;display:flex;justify-content:space-between;
  align-items:baseline;gap:6mm;padding-top:3.4mm;
  border-top:1.6px solid var(--ink);font-size:10pt;color:var(--soft);flex:none;}
.pay b{color:var(--ink);font-weight:600;}
.pay .x{flex:none;font-size:7pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--mad);font-weight:700;}
.strip{margin-top:3.4mm;padding-top:2.8mm;border-top:1px solid var(--line);
  display:flex;justify-content:space-between;gap:5mm;font-size:8.4pt;
  color:var(--soft);flex:none;}
.strip span{white-space:nowrap;}
.strip b{color:var(--ink);font-weight:600;}
.strip .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--mad);font-weight:700;}
.notes{margin-top:3.4mm;display:grid;grid-template-columns:1fr 1fr;gap:4mm;
  flex:none;}
.notes .bx{background:var(--cream);border-radius:3px;padding:3.6mm 5mm;}
.notes .bx.w{background:#fff;border:1px solid var(--line);}
.notes .k{font-size:6.8pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--mad);font-weight:700;}
.notes .d{color:var(--soft);font-size:7.4pt;line-height:1.36;margin-top:1.4mm;}
.notes .d b{color:var(--ink);font-weight:600;}
"""

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · rack da sala</span><span>{n} / {NP}</span></div>')

p1 = f"""<div class="page dk"><div class="pad">
  <div class="mark">Valvic Marcenaria</div>
  <div style="height:9mm;flex:none;"></div>
  <div class="kick">Proposta comercial</div>
  <h1>O rack<br>da sala.</h1>
  <div class="sub"><b>{CLIENTE}</b> · {OBRA}<br>
    Projeto <b>{ESCRIT}</b> · {ARQ}</div>

  <div class="hero"><img src="{HERO}" alt=""></div>

  <div class="vrow" style="margin-top:6mm;">
    <div class="k">Garantia</div>
    <div><div class="t serif">Cinco anos.</div>
      <div class="d">A mesma do restante do apartamento, em termo nosso.
      Estrutura e ferragens, com <b>equipe própria</b> do corte à
      instalação — não faria sentido este móvel ter outra regra.</div></div>
  </div>
  <div class="vrow">
    <div class="k">O móvel</div>
    <div><div class="t serif">Suspenso, e<br>pendurado na estrutura.</div>
      <div class="d">Um rack que não toca o piso precisa de alguém
      segurando. Aqui é uma <b>barra contínua de metalon chumbada na
      alvenaria</b> por trás do painel: o peso vai para a parede, não para
      o painel de madeirado.</div></div>
  </div>
  <div class="vrow">
    <div class="k">A frente</div>
    <div><div class="t serif">Palha natural,<br>contida pelo filete.</div>
      <div class="d">A palhinha é <b>assentada em rebaixo usinado na
      própria face da porta</b>, com um filete de madeirado contornando as
      quatro bordas. Ela fica <b>presa em todo o perímetro</b>, não só
      colada na superfície — é o detalhe que decide se a frente continua
      inteira no quinto ano.</div></div>
  </div>

  <div class="meta">
    <div><div class="k">Prazo</div><div class="v">{PRAZO}</div></div>
    <div><div class="k">Garantia</div><div class="v">{GARANTIA}</div></div>
    <div><div class="k">Execução</div><div class="v">Equipe própria</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
  </div>
  {foot(1)}
</div></div>"""

rows = ''.join(f'<div class="row"><div class="k">{k}</div>'
               f'<div class="d">{d}</div></div>' for k, d in ITENS)

p2 = f"""<div class="page"><div class="pad p2">
  <div class="hd"><div class="b">Valvic Marcenaria</div>
    <div class="m">{CLIENTE} · {DATA}</div></div>
  <div class="eye">O móvel · duas versões</div>
  <div class="h1 serif">O rack de {LARGURA} da parede da TV,<br>
    em cinco módulos — <i>quatro portas e um nicho</i>.</div>


  <div class="rows">{rows}</div>

  <div class="band">
    <div><div class="lab">A versão do projeto</div>
      <div class="nm serif">Portas em palha natural</div>
      <div class="s">Palhinha indiana <b>assentada em rebaixo usinado na
      face da porta</b>, com filete de madeirado nas quatro bordas. É a
      frente que o render do projeto mostra.</div></div>
    <div class="big">R$ {br(PALHA)}</div>
  </div>

  <div class="alt">
    <div><div class="lab">Sem a palha</div>
      <div class="nm serif">Portas lisas</div>
      <div class="s">A mesma porta, sem o rebaixo e sem a tela: folha
      inteiriça no madeirado, com fita de borda nas quatro arestas. Mesmo
      corpo, mesma ferragem, mesma garantia.</div></div>
    <div class="v">R$ {br(LISA)}</div>
  </div>

  <div class="pay">
    <div><b>50%</b> de entrada + <b>50%</b> na entrega</div>
    <div class="x">condição única</div>
  </div>

  <div class="strip">
    <span><span class="k">Prazo</span> <b>{PRAZO}</b></span>
    <span><span class="k">Garantia</span> <b>{GARANTIA}</b></span>
    <span><span class="k">Execução</span> <b>Equipe própria</b></span>
    <span><span class="k">Validade</span> <b>{VALIDADE}</b></span>
  </div>

  <div class="notes">
    <div class="bx"><div class="k">O que não está incluso</div>
      <div class="d">O <b>painel de madeirado da parede</b>, que já está
      contratado — este rack é item à parte e soma a ele. A
      <b>televisão, os equipamentos</b> e o cabeamento. <b>Ponto de tomada,
      circuito e interruptor</b>, que são elétrica de obra. <b>Alvenaria,
      pintura e forro.</b></div></div>
    <div class="bx w"><div class="k">A confirmar antes da produção</div>
      <div class="d">A prancha manda <b>conferir todas as medidas no
      local</b> — medimos antes de cortar. O <b>padrão do madeirado</b>,
      que o projeto deixa "à definir". E <b>amostra da palha</b> antes de
      aplicar: fibra natural tem variação de tom de rolo para rolo, e é com
      a amostra na mão que se escolhe.</div></div>
  </div>
  {foot(2)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + '</body></html>')

(P/'proposta-apto-cv-rack.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-apto-cv-rack.pdf')],
               check=True, env=env)
print(f'proposta-apto-cv-rack.pdf · {NP} páginas')
print(f'  linha Essencial · garantia {GARANTIA} · MC {cv.MC_ALVO:.0%} · com RT')
print(f'  custo direto · com palha   R$ {br(cv.PALHA["cd"]):>7}')
print(f'  custo direto · lisa        R$ {br(cv.LISA["cd"]):>7}')
print(f'  A · portas em palha        R$ {br(PALHA):>7}')
print(f'  B · portas lisas           R$ {br(LISA):>7}')
print(f'  diferença                  R$ {br(PALHA-LISA):>7}  '
      f'({(PALHA-LISA)/LISA*100:+.0f}%)')
print(f'  pagamento                  50% de entrada + 50% na entrega')
