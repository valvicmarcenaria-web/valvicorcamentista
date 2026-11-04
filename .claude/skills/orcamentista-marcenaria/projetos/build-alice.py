# -*- coding: utf-8 -*-
"""ALICE — proposta · MDF MELAMÍNICO  [08/10/2026]

⭐ [Jonathan 08/10] "mudança de planos. Será tudo em melamínico mesmo."
   Cai o compensado naval; fica a versão melamínico do `corte-alice.py`.

Projeto DET_ALICE R00 (06/10/2026), arquiteta Alícia Vasconcelos.
Prazo de 60 dias corridos · validade até sábado, 10 de outubro —
semana de fechamento da agenda do ano.

Números de `corte-alice.py`; nada digitado à mão.
⛔⛔ Sem metragem nem quantitativo. Espessura (15/18 mm) é especificação.
⛔ Classes novas levam sufixo AL.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('al', P/'corte-alice.py')
al = importlib.util.module_from_spec(spec); sys.modules['al'] = al
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(al)
COR, BRANCO = al.COR, al.BRANCO    # ⭐ os dois cenários de interno

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, DATA = 'Alice', '8 de outubro de 2026'
ARQUITETA = 'Alícia Vasconcelos'
PRAZO, VALIDADE = '60 dias corridos', 'Sábado, 10 de outubro'
NP = 2

# ── o escopo, ambiente a ambiente ─────────────────────────────────────────
DESC = {
 'Cozinha · armário inferior':
   'Armário sob a bancada com porta de giro, gavetas e a gaveta de temperos. '
   'Puxador ponto preto e <b>portas com abertura de 180°</b>.',
 'Cozinha · armário superior':
   'Armário suspenso com portas de giro, prateleiras internas e puxador '
   'ponto preto. <b>Rodateto recuado</b> no encontro com o forro.',
 'Área de serviço · armário sob bancada':
   'Armário sob a bancada com portas de giro, prateleira interna e puxador '
   'ponto preto.',
 'Banheiro · armário sob bancada':
   'Armário sob a bancada com <b>porta basculante</b> e gaveta, puxador '
   'ponto preto.',
 'Banheiro · armário-espelho':
   'Armário com <b>espelho colado na porta</b>, prateleiras internas e '
   '<b>puxador passante</b> usinado na própria peça.',
 'Sala de estar · prateleiras':
   'Prateleiras com ponta arredondada, em <b>suporte invisível chumbado na '
   'parede</b> — sem mão-francesa e sem parafuso à vista.',
 'Quarto · roupeiro':
   'Roupeiro do piso ao forro com maleiro, portas de giro em <b>18 mm</b>, '
   'prateleiras, gavetas, <b>sapateira deslizante</b>, cabideiro e '
   '<b>cabideiro deslizante para calças</b>.',
}
CURTO = {
 'Cozinha · armário inferior':            ('Cozinha', 'Armário sob a bancada'),
 'Cozinha · armário superior':            ('',        'Armário suspenso'),
 'Área de serviço · armário sob bancada': ('Área de serviço', 'Armário sob a bancada'),
 'Banheiro · armário sob bancada':        ('Banheiro', 'Armário sob a bancada'),
 'Banheiro · armário-espelho':            ('',        'Armário-espelho'),
 'Sala de estar · prateleiras':           ('Sala de estar', 'Prateleiras suspensas'),
 'Quarto · roupeiro':                     ('Quarto',  'Roupeiro'),
}

CSS = (open(P/'css-proposta.css', encoding='utf-8').read() + """
/* ── Alice · melamínico ───────────────────────────────────────────────── */
/* ⛔ flex:none em TODO bloco fechado: .pad é coluna flex e um box com
      overflow:hidden ENCOLHE em silêncio quando a coluna estoura. */
.topAL{display:flex;justify-content:space-between;align-items:baseline;gap:8mm;
  padding-bottom:4.2mm;border-bottom:1px solid var(--hair);flex:none;}
.topAL .b{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;
  font-weight:700;letter-spacing:.02em;}
.topAL .m{font-size:7.2pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;text-align:right;}

.leadAL{color:var(--soft);font-size:9.2pt;line-height:1.56;max-width:160mm;
  flex:none;}
.leadAL b{color:var(--ink);font-weight:600;}

.itAL{margin-top:4.2mm;flex:none;}
.itAL .r{display:flex;gap:6mm;padding:2.6mm 0;border-top:1px solid var(--hair);}
.itAL .a{flex:none;width:30mm;font-size:6.9pt;letter-spacing:.14em;
  text-transform:uppercase;color:var(--gold);font-weight:700;padding-top:.8mm;}
.itAL .t{flex:1;}
.itAL .n{font-weight:600;font-size:9.4pt;}
.itAL .d{color:var(--soft);font-size:8.3pt;line-height:1.5;margin-top:.8mm;}
.itAL .d b{color:var(--ink);font-weight:600;}

.tecAL{display:grid;grid-template-columns:repeat(2,1fr);gap:4mm 7mm;
  margin-top:5mm;padding-top:4mm;border-top:1px solid var(--hair);flex:none;}
.tecAL .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.tecAL .d{color:var(--soft);font-size:8.3pt;margin-top:1mm;line-height:1.5;}
.tecAL .d b{color:var(--ink);}

table.invAL{width:100%;border-collapse:collapse;margin-top:3mm;font-size:9pt;}
table.invAL th{font-size:6.9pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding:0 0 2.2mm;text-align:left;}
table.invAL th.r,table.invAL td.r{text-align:right;}
table.invAL td{padding:1.35mm 0;border-top:1px solid var(--hair);
  vertical-align:top;}
table.invAL td.a{font-size:6.9pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold);font-weight:700;width:34mm;padding-top:2.4mm;}
table.invAL td.i{font-weight:600;}
table.invAL tr.tot td{border-top:1.6px solid var(--ink);padding-top:2.4mm;
  font-family:'Cormorant Garamond',Georgia,serif;font-size:20pt;font-weight:700;}
table.invAL tr.tot td.a,table.invAL tr.tot td.i{font-family:inherit;
  font-size:9.6pt;}

.escAL{margin-top:3.6mm;flex:none;}
.escAL .ttl{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding-bottom:1.6mm;}
.escAL .l{display:flex;justify-content:space-between;align-items:baseline;
  gap:6mm;padding:1.35mm 0;border-top:1px solid var(--hair);font-size:8.5pt;
  color:var(--soft);}
.escAL .l .x{flex:none;font-size:8pt;letter-spacing:.1em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}

.invAL th.g,.invAL td.g{color:var(--gold);}
.invAL tr.tot td.g{color:var(--gold);}
.duasAL{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-top:4mm;
  flex:none;}
.duasAL > div{border:1.2px solid var(--line);border-radius:5px;padding:3.6mm;}
.duasAL > div.g{border-color:var(--gold);background:rgba(201,169,106,.07);}
.duasAL .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.duasAL .d{color:var(--soft);font-size:8.3pt;margin-top:1.4mm;line-height:1.5;}
.duasAL .d b{color:var(--ink);font-weight:600;}
.valAL{margin-top:4mm;padding:3.6mm 5.5mm;background:var(--ink);color:#fff;
  border-radius:4px;display:flex;align-items:baseline;gap:6mm;flex:none;}
.valAL .k{flex:none;font-size:7.2pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold-lt);font-weight:700;}
.valAL .d{flex:none;font-family:'Cormorant Garamond',Georgia,serif;
  font-size:14.5pt;font-weight:700;}
.valAL .t{flex:1;font-size:8.1pt;color:#D7D0C3;line-height:1.5;text-align:right;}

.cndAL{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:3.6mm;
  padding-top:2.6mm;border-top:1px solid var(--hair);flex:none;}
.cndAL .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndAL .d{color:var(--soft);font-size:8pt;margin-top:1mm;line-height:1.44;}
.cndAL .d b{color:var(--ink);}
.notaAL{margin-top:3.2mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:7.9pt;color:var(--soft);line-height:1.5;flex:none;}
.notaAL b{color:var(--ink);}
""")

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · marcenaria completa</span>'
            f'<span>{n} / {NP}</span></div>')

itens = ''.join(
    f'<div class="r"><div class="a">{CURTO[k][0]}</div><div class="t">'
    f'<div class="n">{CURTO[k][1]}</div><div class="d">{DESC[k]}</div>'
    f'</div></div>' for k in al.AMBS)

linhas = ''
for k in al.AMBS:
    amb, nome = CURTO[k]
    linhas += (f'<tr><td class="a">{amb}</td><td class="i">{nome}</td>'
               f'<td class="r">R$ {br(COR["PV"][k])}</td>'
               f'<td class="r g">R$ {br(BRANCO["PV"][k])}</td></tr>')

p1 = f"""<div class="page"><div class="pad">
  <div class="topAL">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>

  <div style="margin-top:6mm;" class="eyebrow">Apartamento</div>
  <div class="h-sec serif" style="font-size:26pt;">A casa inteira,<br>
    <em>de uma vez só.</em></div>
  <div class="rule"></div>
  <div class="leadAL">Alice, o detalhamento da <b>{ARQUITETA}</b> chegou
  completo — cozinha, área de serviço, banheiro, sala e quarto, com cada
  gaveta e cada prateleira já desenhadas. Esta proposta executa esse
  caderno <b>inteiro</b>, em <b>MDF melamínico</b>, sem dividir a obra em
  etapas: uma medição, uma produção, uma instalação.</div>

  <div class="itAL">{itens}</div>

  <div class="tecAL">
    <div><div class="k">Estrutura</div><div class="d">
      <b>MDF melamínico de 15 mm</b>, com <b>18 mm nas portas do roupeiro</b>
      — a espessura que evita empeno em porta alta. Fita de borda em todas
      as bordas aparentes.</div></div>
    <div><div class="k">Ferragem</div><div class="d">
      <b>Amortecedor em todas as ferragens</b> e <b>corrediça telescópica</b>
      em todas as gavetas, como o projeto pede.</div></div>
    <div><div class="k">Rodateto recuado</div><div class="d">
      Em <b>todos</b> os armários que chegam ao forro, no encontro desenhado
      pela arquiteta — a marcenaria morre no gesso sem fresta.</div></div>
    <div><div class="k">Medição</div><div class="d">
      <b>No local, antes do corte.</b> O caderno adverte em todas as
      pranchas: conferir medidas no local.</div></div>
  </div>
  {foot(1)}
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="topAL">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>

  <div style="margin-top:5mm;" class="eyebrow">O investimento</div>
  <div class="h-sec serif" style="font-size:23pt;">Ambiente a ambiente.</div>
  <div class="rule"></div>

  <table class="invAL">
    <thead><tr><th></th><th></th>
      <th class="r">Interno na cor</th>
      <th class="r g">Interno branco</th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td class="a"></td><td class="i">Investimento total</td>
        <td class="r">R$ {br(COR['TOT'])}</td>
        <td class="r g">R$ {br(BRANCO['TOT'])}</td></tr>
    </tbody>
  </table>

  <div class="duasAL">
    <div><div class="k">Interno na cor</div><div class="d">
      O <b>mesmo padrão por dentro e por fora</b>: abre a porta e o armário
      continua. É o acabamento que o caderno desenha.</div></div>
    <div class="g"><div class="k">Interno branco</div><div class="d">
      Frentes e peças aparentes na cor, <b>caixaria em Branco TX</b>. Clareia
      o interior, facilita enxergar o que está guardado — e economiza
      <b>R$ {br(COR['TOT'] - BRANCO['TOT'])}</b>.</div></div>
  </div>

  <div class="valAL">
    <div class="k">Válida até</div>
    <div class="d">{VALIDADE}</div>
    <div class="t">Estamos fechando a agenda de produção do ano —<br>
    e há uma vaga reservada para a sua obra.</div>
  </div>

  <div class="escAL">
    <div class="ttl">Condições de pagamento</div>
    <div class="l"><div>30% de entrada + restante em até 10× no cartão</div>
      <div class="x">sem desconto</div></div>
    <div class="l"><div>50% de entrada + restante em até 8× no cartão</div>
      <div class="x">−3%</div></div>
    <div class="l"><div>70% de entrada + restante em até 6× no cartão</div>
      <div class="x">−5%</div></div>
    <div class="l"><div>70% de entrada + saldo por transferência</div>
      <div class="x">−7%</div></div>
  </div>

  <div class="cndAL">
    <div><div class="k">Prazo</div><div class="d">
      <b>{PRAZO}</b>, contados do aceite e da medição final.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>10 anos</b> sobre estrutura e ferragens.</div></div>
    <div><div class="k">Execução</div><div class="d">
      Do corte à instalação, com <b>equipe própria</b> da casa.</div></div>
    <div><div class="k">Projeto</div><div class="d">
      Executado sobre o caderno <b>DET_ALICE R00</b>.</div></div>
  </div>

  <div class="notaAL"><b>A definir com a arquiteta:</b> o padrão amadeirado
  do melamínico, o cenário de interno e o acabamento do puxador rasgo. <b>Não inclusos:</b>
  bancadas e cubas, eletrodomésticos, espelhos além do armário do banheiro,
  iluminação, elétrica e hidráulica, gesso, pintura e revestimentos.</div>
  {foot(2)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + '</body></html>')

(P/'proposta-alice.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', '/tmp/r.js', str(P/'proposta-alice.pdf')],
               check=True, env=env)
print(f'proposta-alice.pdf · {NP} páginas')
print(f'  Interno na cor     R$ {br(COR["TOT"])}'
      f'   MC {(COR["BASE"]-COR["CD"]/COR["TOT"])*100:.1f}%')
print(f'  Interno branco     R$ {br(BRANCO["TOT"])}'
      f'   MC {(BRANCO["BASE"]-BRANCO["CD"]/BRANCO["TOT"])*100:.1f}%')
print(f'  economia           R$ {br(COR["TOT"]-BRANCO["TOT"])}')
print(f'  Prazo          {PRAZO}')
print(f'  Validade       {VALIDADE}')
