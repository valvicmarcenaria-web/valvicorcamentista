# -*- coding: utf-8 -*-
"""ANDREA · clínica de dermatologia — folha de aditivo  [24/10/2026]

⭐ [Jonathan 24/10] "Preciso criar uma página de aditivo de orçamento para
   a cliente Andrea da clínica de dermatologia. (…) Não exponha o erro,
   vamos expor a SOLUÇÃO, que será a aplicação de laminado de alta pressão
   (fórmica) revestindo todos os painéis e portas que já estão prontos na
   fábrica. (…) aplique as imagens de forma criativa no layout."

⛔⛔ A FOLHA NÃO ACUSA NINGUÉM, E NÃO DIZ QUE ALGO ESTÁ ERRADO. Ela diz o
   que o ambiente clínico EXIGE de uma superfície e apresenta o acabamento
   que entrega isso. Nenhuma frase aqui pode ser lida como "o que está lá
   não serve" — isso é passivo contratual, não argumento de venda.
   ⛔ A decoradora parceira NÃO é citada. Em lugar nenhum.

⭐ AS TRÊS IMAGENS CONTAM O PROCESSO, não decoram: a lâmina (o quê), a
   colagem (como) e a camada (o resultado). É a faixa do meio da folha, e
   ela resume em três quadros o que a lista numerada detalha embaixo.

⛔ UMA PÁGINA, como pedido. Sem metragem e sem quantitativo: contagem só
   por extenso ("duas demãos").

Números de `corte-andrea-aditivo.py`; nada digitado à mão.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('an', P/'corte-andrea-aditivo.py')
an = importlib.util.module_from_spec(spec); sys.modules['an'] = an
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(an)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, OBRA = 'Andrea', 'Clínica de dermatologia'
DATA = '24 de outubro de 2026'
MATERIAL = 'Carvalho Mel'
ACABAMENTO = 'Top Matt'
PRAZO_MAT, PRAZO_EXEC, PRAZO_TOT = '45 a 60 dias', '30 dias', 'cerca de 90 dias'
VALIDADE = '7 dias úteis'
NP = 1
INVEST = an.PV

# ⛔⛔ TRAVAS
assert INVEST == 16500.0, '⛔ O INVESTIMENTO NÃO É MAIS O DO JONATHAN'
assert an.MC_PISO == 0.35, '⛔ O PISO DA CASA MUDOU'
# ⛔ "SE ESTÁ NO TEXTO, TEM DE ESTAR NA CONTA": a folha promete lixamento,
#   duas demãos de cola, desbaste, relaminação dos topos e instalação. Se o
#   motor perder qualquer uma dessas linhas, a folha vende o que não foi
#   orçado.
assert an.LIXA_M2 > 0 and an.COLA_LATA > 0 and an.FITA_M > 0, \
    '⛔ UMA ETAPA DO PROCESSO SUMIU DA CONTA'
assert an.MO_M2 > 0 and an.INSTALA > 0, '⛔ A MÃO DE OBRA OU A INSTALAÇÃO SUMIU'

IMG = P/'img-andrea'
def b64(nome, tipo='png'):
    return (f'data:image/{tipo};base64,'
            + base64.b64encode((IMG/nome).read_bytes()).decode())
LAMINA, COLA, CAMADA = b64('lamina.png'), b64('cola.jpg', 'jpeg'), b64('camada.png')

QUADROS = [
 (LAMINA, 'contain', 'A lâmina',
  'Laminado de alta pressão: camada contínua, <b>sem poro</b>, que cobre '
  'a face inteira da peça.'),
 (COLA, 'cover', 'A colagem',
  '<b>Duas demãos</b> de cola de contato, nos dois materiais, e prensagem '
  'feita à mão, peça por peça.'),
 (CAMADA, 'contain', 'A camada',
  'Uma pele nova aderida ao que já está pronto — <b>o móvel não é '
  'refeito</b>, é revestido.'),
]

ETAPAS = [
 ('01', 'Lixamento', 'da superfície dos painéis atuais, até gerar '
  'porosidade e aderência.'),
 ('02', 'Corte', 'das lâminas de laminado, peça a peça.'),
 ('03', 'Cola', 'em duas demãos, aplicada nos dois materiais.'),
 ('04', 'Colagem', 'delicada sobre as superfícies, com prensagem.'),
 ('05', 'Desbaste', 'das arestas, para a lâmina terminar rente.'),
 ('06', 'Relaminação', 'dos topos com fita de borda no mesmo padrão.'),
 ('07', 'Conferência', 'peça por peça e instalação no local.'),
]

CSS = """
:root{
  --esp:#1B2527; --mel:#B0833C; --mel-lt:#E6CFA4; --casca:#7E5A30;
  --clin:#F2F5F5; --ink:#15191A; --soft:#4E5A5C; --mut:#8C989A;
  --line:#DCE3E4; --paper:#fff;
}
@page{size:A4;margin:0;}
*{box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
body{margin:0;font-family:'DM Sans',Arial,sans-serif;color:var(--ink);
     font-size:9.4pt;line-height:1.58;}
.serif{font-family:'Cormorant Garamond',Georgia,serif;}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;
      background:var(--paper);}
.pad{padding:14mm 17mm 13mm;height:100%;display:flex;flex-direction:column;}
.foot{margin-top:auto;padding-top:5mm;border-top:1px solid var(--line);
      display:flex;justify-content:space-between;font-size:7pt;
      letter-spacing:.18em;text-transform:uppercase;color:var(--mut);flex:none;}

.hd{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1.6px solid var(--ink);padding-bottom:3.2mm;flex:none;}
.hd .b{font-size:8pt;letter-spacing:.4em;text-transform:uppercase;font-weight:700;}
.hd .m{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.eye{font-size:7pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--mel);font-weight:700;margin-top:4.5mm;flex:none;}
.h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:25pt;
  line-height:1.03;font-weight:600;letter-spacing:-.022em;margin-top:1.8mm;
  flex:none;}
.h1 i{font-style:normal;color:var(--mel);}
.lead{margin-top:3mm;font-size:9.2pt;line-height:1.5;color:var(--soft);
  max-width:168mm;flex:none;}
.lead b{color:var(--ink);font-weight:600;}

/* ── a faixa das três imagens: lâmina · colagem · camada ───────────── */
.band{margin-top:4mm;display:grid;grid-template-columns:repeat(3,1fr);
  gap:4.5mm;flex:none;}
.q{display:flex;flex-direction:column;}
.q .ph{height:30mm;border-radius:3px;overflow:hidden;background:#fff;
  border:1px solid var(--line);display:flex;align-items:center;
  justify-content:center;}
.q .ph img{width:100%;height:100%;display:block;}
.q .ph img.contain{object-fit:contain;padding:3mm 3.5mm;}
.q .ph img.cover{object-fit:cover;object-position:46% 52%;}
.q .n{margin-top:2.6mm;display:flex;align-items:baseline;gap:2.4mm;}
.q .n .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;
  font-weight:700;line-height:1;}
.q .n .r{flex:1;height:1px;background:var(--line);}
.q .d{margin-top:1.4mm;font-size:8pt;line-height:1.44;color:var(--soft);}
.q .d b{color:var(--ink);font-weight:600;}

.sec{margin-top:4mm;font-size:7pt;letter-spacing:.28em;text-transform:uppercase;
  color:var(--mel);font-weight:700;flex:none;}
.steps{margin-top:2.6mm;display:grid;grid-template-columns:repeat(2,1fr);
  gap:0 9mm;flex:none;}
.st{display:grid;grid-template-columns:9mm 1fr;gap:3mm;align-items:baseline;
  padding:1.3mm 0;border-top:1px solid var(--line);}
.st .k{font-family:'Cormorant Garamond',Georgia,serif;font-size:13pt;
  font-weight:700;color:var(--mel);line-height:1;}
.st .d{font-size:8.3pt;line-height:1.42;color:var(--soft);}
.st .d b{color:var(--ink);font-weight:600;}

.two{margin-top:3.8mm;display:grid;grid-template-columns:1fr 1fr;gap:4.5mm;
  flex:none;}
.bx{background:var(--clin);border-radius:3px;padding:4mm 5.4mm;}
.bx .k{font-size:6.8pt;letter-spacing:.24em;text-transform:uppercase;
  color:var(--mel);font-weight:700;}
.bx .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:15.5pt;
  font-weight:600;line-height:1.1;margin-top:1.4mm;}
.bx .d{font-size:8pt;line-height:1.46;color:var(--soft);margin-top:1.8mm;}
.bx .d b{color:var(--ink);font-weight:600;}
.pz{margin-top:2.2mm;display:grid;grid-template-columns:auto 1fr;gap:1mm 3.4mm;
  font-size:8pt;color:var(--soft);}
.pz b{color:var(--ink);font-weight:600;white-space:nowrap;}

.inv{margin-top:3.8mm;background:var(--esp);color:#F2F0EB;border-radius:3px;
  padding:4.6mm 7mm;display:flex;justify-content:space-between;
  align-items:flex-end;gap:8mm;flex:none;}
.inv .lab{font-size:7.4pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--mel-lt);font-weight:700;}
.inv .s{font-size:8.6pt;color:#B7C0C1;margin-top:2.2mm;max-width:104mm;
  line-height:1.48;}
.inv .s b{color:#EFEDE7;font-weight:600;}
.inv .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:32pt;
  font-weight:700;color:#fff;line-height:.9;letter-spacing:-.028em;
  font-variant-numeric:tabular-nums;white-space:nowrap;}
.strip{margin-top:3.6mm;padding-top:2.8mm;border-top:1px solid var(--line);
  display:flex;justify-content:space-between;gap:5mm;font-size:8.2pt;
  color:var(--soft);flex:none;}
.strip span{white-space:nowrap;}
.strip b{color:var(--ink);font-weight:600;}
.strip .k{font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;
  color:var(--mel);font-weight:700;}
"""

quadros = ''.join(
 f'<div class="q"><div class="ph"><img class="{fit}" src="{src}" alt=""></div>'
 f'<div class="n"><div class="t serif">{tit}</div><div class="r"></div></div>'
 f'<div class="d">{d}</div></div>' for src, fit, tit, d in QUADROS)

steps = ''.join(f'<div class="st"><div class="k">{k}</div>'
                f'<div class="d"><b>{t}</b> {d}</div></div>'
                for k, t, d in ETAPAS)

HTML = f"""<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<div class="page"><div class="pad">
  <div class="hd"><div class="b">Valvic Marcenaria</div>
    <div class="m">{CLIENTE} · {DATA}</div></div>

  <div class="eye">Aditivo de orçamento</div>
  <div class="h1 serif">A superfície que<br>a <i>clínica</i> pede.</div>

  <div class="lead">Em ambiente clínico a marcenaria não é só móvel: é
  <b>superfície de protocolo</b>. Ela encosta, recebe produto e é
  higienizada todos os dias. Este aditivo leva <b>todos os painéis e
  portas já produzidos</b> a um acabamento em <b>laminado de alta
  pressão</b> — uma lâmina contínua, não porosa e impermeável, que aguenta
  a limpeza diária sem abrir, manchar ou perder o aspecto. <b>O projeto,
  as medidas e as ferragens permanecem exatamente como estão</b>: muda a
  face.</div>

  <div class="band">{quadros}</div>

  <div class="sec">Como é feito</div>
  <div class="steps">{steps}</div>

  <div class="two">
    <div class="bx"><div class="k">O acabamento</div>
      <div class="t serif">{MATERIAL}, {ACABAMENTO}.</div>
      <div class="d">Laminado de alta pressão no padrão <b>{MATERIAL}</b>,
      acabamento <b>{ACABAMENTO}</b> — superfície supermatte, de toque seco
      e baixo brilho, que não marca dedo. <b>Mediante disponibilidade do
      padrão junto ao fornecedor.</b></div></div>
    <div class="bx"><div class="k">O prazo</div>
      <div class="t serif">{PRAZO_TOT.capitalize()}.</div>
      <div class="pz">
        <b>{PRAZO_MAT}</b><span>para o fornecedor entregar o material.</span>
        <b>{PRAZO_EXEC}</b><span>de execução, contados do recebimento.</span>
      </div>
      <div class="d">Os dois prazos correm <b>em sequência</b>, não em
      paralelo: a aplicação só começa com a lâmina em casa.</div></div>
  </div>

  <div class="inv">
    <div><div class="lab">Investimento</div>
      <div class="s">Material, aplicação e <b>instalação no local</b>,
      em todos os painéis e portas. Condições de pagamento conforme o
      <b>contrato vigente</b>.</div></div>
    <div class="big">R$ {br(INVEST)}</div>
  </div>

  <div class="strip">
    <span><span class="k">Execução</span> <b>Equipe própria</b></span>
    <span><span class="k">Material</span> <b>{MATERIAL} {ACABAMENTO}</b></span>
    <span><span class="k">Prazo total</span> <b>{PRAZO_TOT}</b></span>
    <span><span class="k">Validade</span> <b>{VALIDADE}</b></span>
  </div>

  <div class="foot"><span>Valvic Marcenaria</span>
    <span>{CLIENTE} · {OBRA}</span><span>1 / {NP}</span></div>
</div></div>
</body></html>"""

(P/'aditivo-andrea-laminacao.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'aditivo-andrea-laminacao.pdf')],
               check=True, env=env)
print(f'aditivo-andrea-laminacao.pdf · {NP} página')
print(f'  material          {MATERIAL} {ACABAMENTO} (mediante disponibilidade)')
print(f'  prazo             {PRAZO_MAT} de material + {PRAZO_EXEC} de execução')
print(f'                    = {PRAZO_TOT}')
print(f'  INVESTIMENTO      R$ {br(INVEST)}  ⭐ preço do Jonathan')
print(f'  ⚠ cobre até       {an.A_PISO:.1f} m² de face no piso da casa '
      f'({an.MC_PISO:.0%})')
