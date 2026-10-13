# -*- coding: utf-8 -*-
"""APTO ORLANDO E IVONE — proposta · banho suíte master  [13/10/2026]

⭐ [Jonathan 13/10] "considere interno branco e externo em amadeirado fosco"
⭐ [Jonathan 13/10] "vamos trazer a mc para 35% e incluir a RT"

Projeto [31] APTO ORLANDO E IVONE, arquiteta Ana Maria Castro, CAU A94939-6,
Rua Passa Tempo, Belo Horizonte. Revisão 00 de 12/10/2026.

Prazo de 60 dias corridos · validade de 7 dias úteis (até 22/10) — aceite
no limite + 60 corridos cai em 21/12, ainda em 2026.

Números de `corte-orlando-ivone.py`; nada digitado à mão.
⛔⛔ Sem metragem nem quantitativo de peça. Nem o "20 cm" do puxador Zen
   Phenix: nome do modelo basta, a cota não entra.
⛔ A ÚNICA imagem é o RENDER da prancha 31_.2 — as elevações trazem cota
   dentro do desenho e metragem não vai para proposta, nem desenhada.
⛔ Classes novas levam sufixo OI.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64

P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('oi', P/'corte-orlando-ivone.py')
oi = importlib.util.module_from_spec(spec); sys.modules['oi'] = oi
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(oi)

br = lambda v: f'{v:,.0f}'.replace(',', '.')
CLIENTE, DATA = 'Orlando e Ivone', '13 de outubro de 2026'
ARQ = 'Ana Maria Castro'
PRAZO, VALIDADE = '60 dias corridos', '7 dias úteis'
NP = 2

def uri(nome):
    return ('data:image/jpeg;base64,'
            + base64.b64encode((P/'img-orlando-ivone'/nome).read_bytes()).decode())
IMG1, IMG2 = uri('render-marcenaria.jpg'), uri('render-espelheira.jpg')

ITENS = [
 ('Bancada', 'Armário da bancada', oi.PV['Armário inferior'],
  'Frente em <b>amadeirado fosco</b> e caixaria em <b>branco</b>. Portas de '
  'giro de um lado e, do outro, as gavetas — todas sobre <b>corrediça '
  'telescópica</b>, que abre a gaveta inteira. Puxador <b>Zen Phenix '
  'cromado</b>, como a arquiteta especificou.'),
 ('Espelheira', 'Armário superior, com espelho', oi.PV['Armário superior'],
  'A parede inteira sobre a bancada. <b>Folhas de espelho prata em perfil '
  'de alumínio</b>, que abrem e guardam por dentro, com prateleiras. Entre '
  'elas, as <b>peças fixas em amadeirado</b> que recebem as arandelas — e, '
  'por trás, o <b>berço e a passagem do driver</b>, como o projeto pede. '
  'Sem puxador aparente: a folha avança sobre a peça fixa e é por ali que '
  'se pega.'),
]
TOTAL = oi.TOT
# ⛔⛔ TRAVA DE SOMA: a tabela TEM de fechar com o total. Nenhum dos três
#   passes de auditoria confere aritmética — um item esquecido na lista
#   sai no PDF sem ninguém ver.
_s = sum(it[2] for it in ITENS)
assert abs(_s - TOTAL) < 0.5, (
    f'⛔ A TABELA NÃO FECHA: as linhas somam {_s:,.0f} e o total diz '
    f'{TOTAL:,.0f}. Falta ou sobra item na lista.')

CSS = (open(P/'css-proposta.css', encoding='utf-8').read() + """
/* ── Orlando e Ivone · banho suíte master ─────────────────────────────── */
/* ⛔ flex:none em TODO bloco fechado: .pad é coluna flex e um box com
      overflow:hidden ENCOLHE em silêncio quando a coluna estoura. */
.topOI{display:flex;justify-content:space-between;align-items:baseline;gap:8mm;
  padding-bottom:4.2mm;border-bottom:1px solid var(--hair);flex:none;}
.topOI .b{font-family:'Cormorant Garamond',Georgia,serif;font-size:13.5pt;
  font-weight:700;letter-spacing:.02em;}
.topOI .m{font-size:7.2pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;text-align:right;}

.leadOI{color:var(--soft);font-size:9.2pt;line-height:1.56;max-width:162mm;
  flex:none;}
.leadOI b{color:var(--ink);font-weight:600;}

.parOI{display:grid;grid-template-columns:1.22fr 1fr;gap:4mm;
  margin-top:4.4mm;flex:none;}
.parOI .phOI{border-radius:5px;overflow:hidden;line-height:0;
  border:1px solid var(--hair);}
.parOI .phOI img{display:block;width:100%;height:57mm;object-fit:cover;
  object-position:center;}
.capOI{font-size:7pt;color:var(--mut);letter-spacing:.04em;margin-top:1.6mm;
  flex:none;}

.itOI{margin-top:4.4mm;flex:none;}
.itOI .r{display:flex;gap:6mm;padding:2.4mm 0;border-top:1px solid var(--hair);}
.itOI .a{flex:none;width:26mm;font-size:6.9pt;letter-spacing:.14em;
  text-transform:uppercase;color:var(--gold);font-weight:700;padding-top:1mm;}
.itOI .t{flex:1;}
.itOI .n{font-weight:600;font-size:10pt;}
.itOI .d{color:var(--soft);font-size:8.4pt;line-height:1.5;margin-top:1mm;}
.itOI .d b{color:var(--ink);font-weight:600;}

.tecOI{display:grid;grid-template-columns:repeat(2,1fr);gap:2.8mm 7mm;
  margin-top:4mm;padding-top:3.2mm;border-top:1px solid var(--hair);flex:none;}
.tecOI .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.tecOI .d{color:var(--soft);font-size:8.3pt;margin-top:1mm;line-height:1.5;}
.tecOI .d b{color:var(--ink);}

table.invOI{width:100%;border-collapse:collapse;margin-top:3.6mm;font-size:9pt;}
table.invOI th{font-size:6.9pt;letter-spacing:.17em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding:0 0 2.2mm;text-align:left;}
table.invOI th.r,table.invOI td.r{text-align:right;}
table.invOI td{padding:2.6mm 0;border-top:1px solid var(--hair);vertical-align:top;}
table.invOI td.a{font-size:6.9pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold);font-weight:700;width:30mm;padding-top:3.2mm;}
table.invOI td.i{font-weight:600;}
table.invOI tr.tot td{border-top:1.6px solid var(--ink);padding-top:3.2mm;
  font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;font-weight:700;}
table.invOI tr.tot td.a,table.invOI tr.tot td.i{font-family:inherit;
  font-size:9.6pt;}

.valOI{margin-top:5mm;padding:4mm 5.5mm;background:var(--ink);color:#fff;
  border-radius:4px;display:flex;align-items:baseline;gap:6mm;flex:none;}
.valOI .k{flex:none;font-size:7.2pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold-lt);font-weight:700;}
.valOI .d{flex:none;font-family:'Cormorant Garamond',Georgia,serif;
  font-size:14.5pt;font-weight:700;}
.valOI .t{flex:1;font-size:8.1pt;color:#D7D0C3;line-height:1.5;text-align:right;}

.escOI{margin-top:5mm;flex:none;}
.escOI .ttl{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--mut);font-weight:700;padding-bottom:1.6mm;}
.escOI .l{display:flex;justify-content:space-between;align-items:baseline;
  gap:6mm;padding:1.8mm 0;border-top:1px solid var(--hair);font-size:8.5pt;
  color:var(--soft);}
.escOI .l .x{flex:none;font-size:8pt;letter-spacing:.1em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}

.cndOI{display:grid;grid-template-columns:repeat(4,1fr);gap:5mm;margin-top:5mm;
  padding-top:3.4mm;border-top:1px solid var(--hair);flex:none;}
.cndOI .k{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.cndOI .d{color:var(--soft);font-size:8pt;margin-top:1mm;line-height:1.44;}
.cndOI .d b{color:var(--ink);}

.notaOI{margin-top:4.4mm;padding-left:4mm;border-left:2.5px solid var(--gold-lt);
  font-size:7.9pt;color:var(--soft);line-height:1.52;flex:none;}
.notaOI b{color:var(--ink);}
.notaOI .h{font-size:7pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;margin-bottom:1.2mm;}
""")

def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria</span>'
            f'<span>{CLIENTE} · banho suíte master</span><span>{n} / {NP}</span></div>')

itens = ''.join(
    f'<div class="r"><div class="a">{a}</div><div class="t">'
    f'<div class="n">{n}</div><div class="d">{d}</div></div></div>'
    for a, n, _p, d in ITENS)

linhas = ''.join(
    f'<tr><td class="a">{a}</td><td class="i">{n}</td>'
    f'<td class="r">R$ {br(p)}</td></tr>' for a, n, p, _d in ITENS)

p1 = f"""<div class="page"><div class="pad">
  <div class="topOI">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>

  <div style="margin-top:6mm;" class="eyebrow">Banho suíte master</div>
  <div class="h-sec serif" style="font-size:24pt;">Dois móveis —<br>
    <em>e o banheiro inteiro muda.</em></div>
  <div class="rule"></div>
  <div class="leadOI">Orlando, Ivone, o projeto da arquiteta
  <b>{ARQ}</b> chegou resolvido. A marcenaria dele são <b>dois móveis</b>:
  o armário que sustenta a bancada e a <b>espelheira</b> que toma a parede
  inteira acima dela — e é ela que faz o banheiro parecer o dobro do que é.</div>

  <div class="parOI">
    <div class="phOI"><img src="{IMG1}" alt=""></div>
    <div class="phOI"><img src="{IMG2}" alt=""></div>
  </div>
  <div class="capOI">As imagens do projeto da {ARQ}</div>

  <div class="itOI">{itens}</div>

  <div class="tecOI">
    <div><div class="k">Chapa resistente à umidade</div><div class="d">
      É banheiro: embaixo de cuba e ao lado de box. A caixaria inteira vai
      em <b>MDF Ultra</b>, de miolo resistente à umidade. O projeto não
      pedia — nós fazemos assim porque é o que <b>sustenta a garantia</b>.</div></div>
    <div><div class="k">Branco por dentro, madeira por fora</div><div class="d">
      Por fora, o <b>amadeirado fosco</b> do projeto. Por dentro, branco:
      armário de banheiro é fundo e cheio, e no branco se <b>enxerga o que
      está guardado</b>.</div></div>
    <div><div class="k">Espelho e alumínio</div><div class="d">
      O <b>espelho prata</b> e o <b>perfil de alumínio</b> das folhas são
      fornecimento nosso, montados e alinhados por nós. Folha de espelho
      <b>não perdoa desalinho</b> — por isso ela sai da nossa bancada, e
      não da obra.</div></div>
    <div><div class="k">Sequência de obra</div><div class="d">
      O sóculo é alvenaria e a bancada é da marmoraria. Entramos
      <b>depois do sóculo pronto e nivelado</b>; a pedra é medida sobre o
      armário já instalado. São <b>duas idas</b>: o armário antes da pedra,
      a espelheira depois.</div></div>
  </div>
  {foot(1)}
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="topOI">
    <div class="b">Valvic Marcenaria</div>
    <div class="m">Proposta comercial<br>{CLIENTE} · {DATA}</div>
  </div>

  <div style="margin-top:6mm;" class="eyebrow">O investimento</div>
  <div class="h-sec serif" style="font-size:25pt;">Peça a peça.</div>
  <div class="rule"></div>

  <table class="invOI">
    <thead><tr><th></th><th></th><th class="r">Investimento</th></tr></thead>
    <tbody>{linhas}
      <tr class="tot"><td class="a"></td><td class="i">Investimento total</td>
        <td class="r">R$ {br(TOTAL)}</td></tr>
    </tbody>
  </table>

  <div class="valOI">
    <div class="k">Entrega</div>
    <div class="d">Ainda em 2026</div>
    <div class="t">Estamos fechando a agenda de produção do ano —<br>
    e há uma vaga que serve para este banheiro.</div>
  </div>

  <div class="escOI">
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

  <div class="cndOI">
    <div><div class="k">Prazo</div><div class="d">
      <b>{PRAZO}</b>, contados do aceite e da medição no local.</div></div>
    <div><div class="k">Garantia</div><div class="d">
      <b>10 anos</b> sobre estrutura e ferragens.</div></div>
    <div><div class="k">Execução</div><div class="d">
      Do corte à instalação, com <b>equipe própria</b> da casa.</div></div>
    <div><div class="k">Validade</div><div class="d">
      <b>{VALIDADE}</b> a partir desta data.</div></div>
  </div>

  <div class="notaOI">
    <div class="h">O que está e o que não está nesta proposta</div>
    <b>Está:</b> os dois móveis, com a ferragem, o espelho prata e o perfil
    de alumínio das folhas, a medição no local, a entrega e a instalação.<br>
    <b>Não está:</b> a bancada, a rodabanca, a testeira, o acabamento do
    sóculo e o nicho do box — todos de <b>marmoraria</b>; o <b>sóculo em
    alvenaria</b>; o <b>box de correr</b>; as <b>louças, metais e
    acessórios</b> especificados no projeto; as <b>arandelas, o driver e a
    instalação elétrica</b> — nossa é a usinagem da passagem e o berço na
    peça fixa; o <b>porcelanato e as soleiras</b>.<br>
    O projeto está na <b>revisão 00</b>, marcada como estudo para análise.
    Alteração de desenho depois do aceite é revista em conjunto.</div>
  <div class="sig">
    <div class="ln">Valvic Marcenaria</div>
    <div class="ln">De acordo · {CLIENTE}</div>
  </div>
  {foot(2)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" '
        'rel="stylesheet"><style>' + CSS + '</style></head><body>'
        + p1 + p2 + '</body></html>')

(P/'proposta-orlando-ivone.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
R = pathlib.Path('/tmp/r.js')
if not R.exists():          # ⛔ /tmp some em reinício de container
    R.write_text("""const { chromium } = require('playwright');
(async () => {
  const out = process.argv[2];
  const browser = await chromium.launch({
    executablePath: process.env.PW_CHROME || undefined,
    args: ['--no-sandbox', '--font-render-hinting=none'] });
  const page = await browser.newPage();
  await page.goto('file:///tmp/in.html', { waitUntil: 'networkidle' });
  try { await page.evaluate(() => document.fonts.ready); } catch (e) {}
  await page.waitForTimeout(1200);
  await page.pdf({ path: out, format: 'A4', printBackground: true,
                   margin: {top:'0',right:'0',bottom:'0',left:'0'} });
  await browser.close();
})();""")
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
subprocess.run(['node', str(R), str(P/'proposta-orlando-ivone.pdf')],
               check=True, env=env)
print(f'proposta-orlando-ivone.pdf · {NP} páginas')
for _, n, p, _d in ITENS: print(f'  {n:<32} R$ {br(p):>8}')
print(f'  {"INVESTIMENTO":<32} R$ {br(TOTAL):>8}'
      f'   MC {(oi.BASE - oi.CD/TOTAL)*100:.1f}%  ·  com RT')
