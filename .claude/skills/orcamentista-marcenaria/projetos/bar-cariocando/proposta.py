# -*- coding: utf-8 -*-
"""BAR CARIOCANDO — a proposta, em DUAS folhas. [Jonathan, 05/11/2026]

⭐ "faça uma proposta sintetizada de apenas 2 paginas" — e duas folhas é
  outro gênero, não o caderno encurtado. Num caderno de dezoito folhas a
  casa se apresenta antes de falar de preço; em duas, o preço é a primeira
  folha e a segunda é o contrato em miniatura. ⛔ O que não cabe não vira
  letra miúda: vira linha nomeada em "o que não está nesta proposta".

⛔ Todo valor vem de `orcamento.py` na hora de gerar. Nenhum número é
  digitado aqui.
"""
import base64, importlib.util, contextlib, io, pathlib, re, sys, subprocess

AQUI = pathlib.Path(__file__).resolve().parent
CASA = AQUI.parent


def _mod(nome, arq):
    s = importlib.util.spec_from_file_location(nome, arq)
    m = importlib.util.module_from_spec(s); sys.modules[nome] = m
    with contextlib.redirect_stdout(io.StringIO()):
        s.loader.exec_module(m)
    return m


orc = _mod('orc', AQUI / 'orcamento.py')
b = orc.b
T = orc.custo(orc.M)
PV = [d / (b.BASE - b.MC) for d in T['diretos']]
TOTAL = sum(PV)

CLIENTE = 'Bar Cariocando'
ENDERECO = 'Avenida Getúlio Vargas, 1179 · Savassi · Belo Horizonte / MG'
ARQ = 'Chico Albano Arquitetura e Biri Arquitetura · prancha #104, revisão 02'
DATA = '5 de novembro de 2026'

DESC = [
 ('Balcão da cozinha', '308,5 × 36 cm',
  'Armário de duas alturas — 88 cm sob a bancada de 90 e 108 cm sob a de 110 —, '
  'com <b>dez portas de frente ripada</b> em MDF Amêndola Rústica, carcaça '
  'interna em MDF branco e <b>vinte e uma prateleiras</b> reguláveis.'),
 ('Fechamento frontal do salão', '182 × 70 cm',
  'A face que o salão vê, ripada no mesmo desenho, com os vãos das vitrines '
  'preservados.'),
 ('Revestimento ripado da porta de acesso', '70 × 115 cm',
  'Uma face, no lado do salão, sobre a folha estruturada em metalon — a '
  'estrutura é da serralheria, o revestimento é nosso.'),
]


def brl(v, c=True):
    s = f'{v:,.2f}' if c else f'{v:,.0f}'
    return 'R$ ' + s.replace(',', '§').replace('.', ',').replace('§', '.')


def b64(nome):
    f = AQUI / 'img' / (nome + '.png')
    return 'data:image/png;base64,' + base64.b64encode(f.read_bytes()).decode()


SUP = '''
/* ⛔ O CAMPO DE AREIA TEM DE ABRAÇAR O DESENHO, NÃO A FOLHA. A elevação é
   três vezes e meia mais larga que alta; num campo de 26 cm de largura ela
   fica contida pela ALTURA e sobram cinco centímetros de areia vazia de
   cada lado — que o olho lê como erro de montagem, não como respiro.
   ⭐ Então a areia é a moldura da IMAGEM: ela cresce com o desenho e para
   onde ele para. */
.band2{display:flex;justify-content:center;margin:5mm 0 0;height:58mm}
.band2 img{height:100%;width:auto;max-width:100%;object-fit:contain;
           background:var(--sand);padding:4mm 5mm;
           box-shadow:0 1mm 4mm rgba(26,23,20,.10)}
.cab{display:flex;justify-content:space-between;align-items:flex-end;
     border-bottom:1px solid var(--line);padding-bottom:3.5mm}
.cab .marca{font-size:8pt;letter-spacing:.44em;text-transform:uppercase;
            color:var(--gold);font-weight:600}
.cab .quem{text-align:right;font-size:7.6pt;color:var(--soft);line-height:1.45}
.mv{padding:3.2mm 0;align-items:baseline}
.mv .t{font-size:10.4pt}
.mv .med{color:var(--gold);font-weight:600;font-size:7.4pt;letter-spacing:.14em;
         text-transform:uppercase}
.mv .d{display:block;color:var(--soft);font-size:8.4pt;margin-top:1.2mm;
       line-height:1.5;max-width:215mm}
.tot2{display:flex;justify-content:space-between;align-items:baseline;
      border-top:1.5px solid var(--ink);margin-top:3mm;padding-top:3.5mm}
.tot2 .k{font-size:7.4pt;letter-spacing:.2em;text-transform:uppercase;
         color:var(--mut);font-weight:600}
.tot2 .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:30pt;
         font-weight:600;line-height:1;font-variant-numeric:lining-nums}
'''

CSS = (CASA / 'css-caderno.css').read_text(encoding='utf-8') + SUP
JS = (CASA / 'js-caderno.js').read_text(encoding='utf-8')

#   ⛔⛔ [Jonathan, 05/11/2026] "nao separe os valores pelos itens". E a
#     folha muda de natureza, não só de coluna: sem preço ao lado, a lista
#     deixa de ser orçamento e vira ESCOPO — o que entra no contrato. ⭐ Um
#     preço por peça convida a cortar uma peça; um preço só convida a
#     decidir o conjunto, que é o que esta proposta vende.
#   ⭐ E o preço do item não some do mundo: ele continua no `orcamento.py`,
#     que é onde a fábrica e a margem olham. Sai da folha do cliente.
_rows = ''
for nome, med, txt in DESC:
    _rows += (f'<div class="mv"><span class="b"></span><span>'
              f'<span class="t">{nome}</span>'
              f'<span class="med"> · {med}</span>'
              f'<span class="d"><br>{txt}</span></span></div>')

_pay = ''.join(f'<tr><td>{d}</td><td class="d">{p:.0%}</td>'
               f'<td class="d" style="color:var(--ink);font-weight:600">'
               f'{brl(TOTAL * p)}</td></tr>' for d, p in b.PARCELAS)

#   ⛔ A FOLHA 1 TAMBÉM ENTRA NO PASSE DE ENCOLHIMENTO. Sem ele o bloco do
#     investimento total caía meio centímetro abaixo da folha e o número
#     saía CORTADO AO MEIO — num documento cujo assunto é esse número.
F1 = f'''<div class="pad apertada"><div class="fitp">
 <div class="cab"><div class="marca">Valvic Marcenaria</div>
  <div class="quem"><b>{CLIENTE}</b><br>{ENDERECO}<br>{ARQ}</div></div>
 <div style="margin-top:6mm"><div class="eyebrow">Proposta de marcenaria</div>
  <div class="rule"></div>
  <div class="h1">O balcão da cozinha.</div>
  <div class="lead" style="margin-top:3mm;max-width:185mm">Três peças de
    marcenaria no detalhamento do balcão — e <b>só elas</b>. A ripa de MDF
    Amêndola Rústica atravessa as três, e é ela que dá ao balcão a cara que o
    projeto desenhou. O granito, a alvenaria, o revestimento cerâmico e a
    estrutura metálica estão nomeados na folha seguinte, fora do nosso
    escopo.</div></div>
 <div class="band2"><img src="{b64('balcao')}" alt=""></div>
 <div style="margin-top:6mm">{_rows}</div>
 <div class="tot2"><div class="k">Investimento total</div>
   <div class="v">{brl(TOTAL)}</div></div>
</div></div>'''

F2 = f'''<div class="pad apertada"><div class="fitp">
 <div class="cab"><div class="marca">Valvic Marcenaria</div>
  <div class="quem"><b>{CLIENTE}</b><br>{DATA}</div></div>
 <div style="margin-top:6mm"><div class="eyebrow">Condições</div>
  <div class="rule"></div>
  <div class="h1">Prazo, pagamento e fronteiras.</div></div>
 <div class="three" style="margin-top:6mm">
  <div>
   <div class="term"><div class="k">Validade desta proposta</div>
     <div class="v">{b.VALIDADE.capitalize()}</div>
     <div class="s">{DATA}. Depois desta data os preços são recalculados.</div></div>
   <div class="term"><div class="k">Prazo de entrega</div>
     <div class="v">{b.PRAZO}</div>
     <div class="s">Instalado. ⚠ O prazo conta da assinatura do contrato e
       pressupõe a <b>alvenaria, o granito e a estrutura metálica prontos</b>
       — a marcenaria é a última a entrar.</div></div>
   <div class="term"><div class="k">Garantia</div>
     <div class="v">{b.GARANTIA_ANOS} anos</div>
     <div class="s">Sobre a marcenaria e a ferragem de movimento. Instalação e
       regulagem, dois anos. Termo assinado na entrega.</div></div>
   <div class="term" style="border-bottom:none">
     <div class="k">Projeto executivo de marcenaria</div><div class="v">Incluso</div>
     <div class="s">Nosso detalhamento, aprovado por vocês e pela arquitetura
       antes de qualquer corte.</div></div>
  </div>
  <div>
   <div class="term"><div class="k">Formas de pagamento</div></div>
   <table class="pay">{_pay}</table>
   <div class="term" style="border-bottom:none"><div class="s">Por
     transferência bancária.</div></div>
   <div class="box" style="margin-top:4mm"><div class="t">O que está incluso</div>
    <p>Projeto executivo de marcenaria, material, usinagem, ripa, fita,
       ferragem <b>Hettich Sensys</b>, transporte, montagem e instalação por
       equipe própria.</p></div>
   <div class="box" style="margin-top:3mm"><div class="t">Um interlocutor</div>
    <p>Da aprovação à entrega, um nome para chamar. Um contrato, uma data,
       uma responsabilidade.</p></div>
  </div>
  <div class="fora">
   <div class="term"><div class="k">O que não está nesta proposta</div></div>
   <ul>
    <li><div class="k">Pedra</div><div class="v">Todo o <b>granito cinza
      andorinha</b> — bancadas, balcões de apoio, sóculos e rodabanca. É
      marmoraria.</div></li>
    <li><div class="k">Obra civil e revestimento</div><div class="v">Alvenaria
      de 9 cm, o revestimento Eliane monocolor 20×20, elétrica, piso e
      pintura.</div></li>
    <li><div class="k">Serralheria</div><div class="v">A estrutura e os
      chumbadores em <b>metalon 3×3</b>, a folha da porta de acesso e as
      prateleiras metálicas sob medida.</div></li>
    <li><div class="k">Equipamento</div><div class="v">Balcão refrigerado para
      barris de chope e a porta de enrolar.</div></li>
    <li><div class="k">A confirmar antes da produção</div><div class="v">A
      medição no local. E <b>a largura da ripa</b>: a prancha pede 4 × 3 cm
      na VISTA A e nas plantas, e 4 × 2 cm na VISTA C e no detalhe da porta.
      Unificar as três faces em 4 × 3 <b>reduz o investimento</b>; a decisão
      é da arquitetura.</div></li>
   </ul>
  </div>
 </div>
 <div class="sig"><div class="ln">{CLIENTE}</div>
   <div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div></div>'''

POS = '''
document.querySelectorAll('.pad.apertada').forEach(c => {
  const f = c.querySelector('.fitp'); if (!f) return;
  f.style.zoom = 1;
  const cs = getComputedStyle(c);
  const alt = c.clientHeight - parseFloat(cs.paddingTop) - parseFloat(cs.paddingBottom);
  const pede = f.scrollHeight;
  if (pede > alt) f.style.zoom = Math.max(.60, (alt / pede) - .012);
});
'''

HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
        f'<title>Proposta · {CLIENTE}</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@'
        '9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
        f'<style>{CSS}</style></head><body>'
        f'<div class="slide">{F1}</div><div class="slide">{F2}</div>'
        f'<script>{JS}</script><script>{POS}</script></body></html>')

SAIDA_HTML = AQUI / 'proposta-bar-cariocando.html'
SAIDA_PDF = AQUI / 'proposta-bar-cariocando.pdf'


def _qa():
    t = re.sub(r'data:image/[^"\']+', '«imagem»', HTML)
    for p in ('Attos', 'Costa Laguna', 'Gustavo', 'Michel', 'Raposo', 'R$ 0,00'):
        assert p not in t, f'⛔⛔ QA: "{p}" apareceu na proposta'
    assert brl(TOTAL) in t, '⛔ QA: o total não está impresso'
    #   ⛔⛔ E A FOLHA TEM UM PREÇO SÓ. A trava não confia na minha memória
    #     de ter tirado a coluna: ela procura cada preço de item no texto e
    #     se achar um, não sai.
    for nome, pv in zip([d[0] for d in DESC], PV):
        assert brl(pv) not in t, f'⛔⛔ QA: o preço de "{nome}" vazou para a folha'
    assert t.count('R$') == 1 + len(b.PARCELAS), \
        f'⛔⛔ QA: {t.count("R$")} valores na proposta — devia ser o total e as parcelas'
    assert b.PRAZO in t and str(b.GARANTIA_ANOS) in t, '⛔ QA: prazo ou garantia fora'
    #   ⛔ a soma das parcelas tem de dar o total, na FOLHA e não só no código
    soma = sum(TOTAL * p for _d, p in b.PARCELAS)
    assert abs(soma - TOTAL) < .01, '⛔⛔ QA: as parcelas não somam o total'
    for termo in ('granito', 'metalon', 'Hettich'):
        assert termo in t, f'⛔ QA: "{termo}" sumiu da folha de fronteiras'
    return True


if __name__ == '__main__':
    _qa()
    SAIDA_HTML.write_text(HTML, encoding='utf-8')
    r = subprocess.run(['node', str(CASA / 'render-pdf.js'),
                        str(SAIDA_HTML), str(SAIDA_PDF)],
                       env={**__import__('os').environ,
                            'NODE_PATH': '/opt/node22/lib/node_modules'},
                       capture_output=True, text=True)
    if r.returncode:
        print('⛔ render:', r.stderr[-800:]); sys.exit(1)
    import pymupdf
    d = pymupdf.open(SAIDA_PDF); rr = d[0].rect
    print(f'✓ {SAIDA_PDF.name} · {len(d)} páginas · {rr.width:.0f} x {rr.height:.0f} pt '
          f'· {SAIDA_PDF.stat().st_size/1e6:.1f} MB · total {brl(TOTAL)}')
    assert len(d) == 2, f'⛔⛔ a proposta tem de ter DUAS folhas e saiu com {len(d)}'
    d.close()
