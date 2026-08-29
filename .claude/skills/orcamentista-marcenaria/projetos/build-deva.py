# -*- coding: utf-8 -*-
"""DEVA VEÍCULOS (IVECO) — PROPOSTA, 4 páginas A4.

Valores de `corte-deva.py`. [Jonathan 25/08] MC 35% COM RT · logos fora.

  Investimento .................... R$ 72.400
  Setor Comercial ................. R$ 31.600
  Setor Vendas .................... R$ 40.800

REGISTRO TÉCNICO, não narrativo [Jonathan 25/08]: uma linha por conjunto, com
o que ele é e o que leva. Sem narrativa de benefício.

REGRAS DA CASA (`referencias/proposta-comercial.md`):
  1. ⛔ nenhuma cota de móvel no texto
  2. ⛔ nenhuma explicação de formação de preço

⚠ PRAZO e PAGAMENTO são PREMISSAS minhas — o Jonathan ainda não fechou.
⛔ MONTAGEM fora do custo (equipe é salário fixo), dentro do escopo entregue.
"""
import subprocess, re

CLIENTE  = 'DEVA Veículos'
OBRA     = 'Concessionária IVECO · setores Comercial e Vendas'
ARQ      = 'Beatriz Fernandez Gontijo · Ofício Planejamento e Consultoria'
DATA     = '25 de agosto de 2026'
VALIDADE = '15 dias corridos'
PRAZO    = 'Até 75 dias corridos'

# ── valores lidos DO MOTOR, não transcritos à mão ─────────────────────────
_out = subprocess.run(['python3', 'projetos/corte-deva.py'],
                      capture_output=True, text=True, check=True).stdout
def _n(pat):
    return int(re.search(pat, _out).group(1).replace('.', ''))
INV = _n(r'FECHADO · MC 35% COM RT \.+ R\$ ([\d.]+)')
COM = _n(r'Setor Comercial\s+R\$ ([\d.]+)')
VEN = _n(r'Setor Vendas\s+R\$ ([\d.]+)')
assert COM + VEN == INV, (COM, VEN, INV)

# conjunto → (setor, nome curto, descrição técnica, valor lido do motor)
def _v(nome):
    m = re.search(re.escape(nome) + r'\s+[\d.,]+ m²\s+R\$ ([\d.]+)', _out)
    assert m, f'não achei o valor de {nome!r} no relatório do motor'
    return int(m.group(1).replace('.', ''))

# ⛔ SEM UMA ÚNICA COTA. Onde a dimensão importa, ela é dita em palavras.
ITENS = [
 ('Comercial', 'EX01 · Painel do balcão comercial', 'Painel do balcão',
  'Painel de parede em MDF branco e amadeirado, com divisão diagonal e recorte '
  'previsto para aplicação da marca. Fita de LED 5 W · 3000 K embutida na '
  'marcenaria. Rodapé recuado com perfil em inox. Estrutura niveladora '
  'ancorada à parede.'),
 ('Comercial', 'EX01 · Balcão comercial', 'Balcão comercial',
  'Balcão de atendimento com bancada operacional interna. Tampo e frentes em '
  'MDF branco; frente e lateral em MDF amadeirado escalonado. Lateral com '
  'fundo falso para transferência das tomadas. Fita de LED embutida. Rodapé '
  'recuado com perfil em inox.'),
 ('Comercial', 'EX02 · Painel de TV', 'Painel de TV',
  'Painel de parede em MDF amadeirado com frisos usinados de 1 cm. Rack de '
  'apoio suspenso em laminado branco. Rodapé recuado com perfil em alumínio '
  'polido. Estrutura niveladora ancorada à parede.'),
 ('Comercial', 'EX02 · Balcão café', 'Balcão café',
  'Bancada e rodabanca em MDF TX branco sobre armário com seis portas de giro '
  'e prateleiras internas. Puxador em cava usinada. Rodapé recuado com perfil '
  'em inox.'),
 ('Comercial', 'EX02 · Bancada da janela', 'Bancada da janela',
  'Bancada em MDF amadeirado sobre estrutura de metalon interna, com saia '
  'frontal e laterais no mesmo material.'),
 ('Vendas', 'EX03 · Painel da recepção', 'Painel da recepção',
  'Painéis de parede em MDF amadeirado e branco, com divisão diagonal e '
  'recorte previsto para aplicação da marca. Vão previsto para o televisor. '
  'Fita de LED embutida. Rodapé recuado com perfil em inox.'),
 ('Vendas', 'EX03 · Balcão da recepção', 'Balcão da recepção',
  'Balcão de atendimento em U, com bancada operacional interna. Tampos e '
  'frentes em MDF branco; frentes e laterais em MDF amadeirado. Montantes com '
  'fundo falso para distribuição das tomadas. Porta baixa de acesso em vidro '
  'temperado, de correr. Fita de LED embutida.'),
 ('Vendas', 'EX04 · Painel e expositor', 'Painel e expositor',
  'Painel de parede em MDF amadeirado com reforço estrutural para o televisor. '
  'Expositor suspenso em MDF amadeirado, com cinco portas de giro em vidro '
  'incolor, fechamento lateral em vidro fixo e montante interno vertical em '
  'vidro.'),
 ('Vendas', 'EX04 · Espaço café', 'Espaço café',
  'Nicho em MDF amadeirado com cantos arredondados e moldura em MDF branco. '
  'Bancada em MDF branco sobre armário em MDF amadeirado com quatro portas de '
  'giro. Ponto de água previsto para o filtro. Rodapé recuado com perfil em '
  'inox.'),
]
ITENS = [(s, k, n, d, _v(k)) for s, k, n, d in ITENS]
assert sum(i[4] for i in ITENS) == INV, (sum(i[4] for i in ITENS), INV)

ESPEC = [
 ('Chapa',       'MDF BP nos padrões branco e amadeirado indicados em projeto'),
 ('Borda',       'Fita ABS aplicada em coladeira automática'),
 ('Ferragem',    'Dobradiça com amortecimento'),
 ('Iluminação',  'Fita de LED 5 W · 3000 K em perfil de alumínio, embutida na '
                 'marcenaria conforme as pranchas'),
 ('Vidro',       'Temperado incolor nas portas do expositor e na porta de '
                 'acesso do balcão da recepção'),
 ('Serralheria', 'Estrutura de metalon interna na bancada da janela'),
 ('Arremates',   'Rodapé e recuos com perfil em inox; perfil em alumínio '
                 'polido no painel de TV; bit de 1 cm no encontro com a '
                 'alvenaria'),
 ('Fixação',     'Estrutura niveladora ancorada à alvenaria, com sarrafeamento '
                 'por trás dos painéis'),
 ('Produção',    'Corte e usinagem em CNC própria, laminação de borda em '
                 'coladeira automática, instalação e montagem por equipe '
                 'própria da Valvic'),
]

PAGTO = [
    ('Entrada de 30% + saldo em até 10× no cartão', '—'),
    ('Entrada de 50% + saldo em até 8× no cartão',  '3%'),
    ('Entrada de 70% + saldo em até 6× no cartão',  '5%'),
    ('Entrada de 70% + saldo por transferência',    '7%'),
]

# ⚠ O PRIMEIRO ITEM É O MAIS IMPORTANTE DESTA PROPOSTA.
FORA = [
 ('Painel em marcenaria padrão IVECO',
  'A planta do setor de vendas indica esse painel e remete a detalhe '
  'específico, que <strong>não veio no pacote de pranchas</strong>. Será '
  'orçado assim que a prancha for emitida.'),
 ('Aplicação da marca IVECO nos painéis',
  'Os painéis preveem o recorte e o reforço para receber a marca; o '
  'fornecimento e a aplicação são da montadora.'),
 ('Televisores', 'Prevemos o vão, o reforço e o passa-cabo.'),
 ('Forro modular mineral acústico', ''),
 ('Divisórias de vidro existentes e o reforço delas',
  'A prancha pede reforço na divisória para fixação do expositor — é serviço '
  'da obra.'),
 ('Estrutura interna do dry wall', ''),
 ('Pontos elétrico, de rede e de água', 'A iluminação embutida NA marcenaria é '
  'nossa; os pontos são da obra.'),
 ('Alvenaria, gesso, revestimento e pintura', ''),
]

CSS = open('projetos/css-proposta.css', encoding='utf-8').read() + """
.cj{padding:3.4mm 0;border-bottom:1px solid var(--hair);}
.cj:last-child{border-bottom:none;}
.cj-h{display:flex;align-items:baseline;gap:4mm;}
.cj-n{font-family:'Cormorant Garamond',Georgia,serif;font-size:15pt;
  color:var(--gold-lt);font-weight:600;line-height:1;min-width:8mm;}
.cj-t{font-size:10.8pt;font-weight:700;letter-spacing:-.005em;}
.cj-q{margin-left:auto;font-size:9.8pt;font-weight:700;white-space:nowrap;}
.cj-d{color:var(--soft);font-size:8.8pt;margin:1.4mm 0 0 12mm;}
.set{font-size:7pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--gold);font-weight:700;margin:7mm 0 1mm;}
.set:first-child{margin-top:0;}
.esp{padding:2.6mm 0;border-bottom:1px solid var(--hair);display:grid;
  grid-template-columns:30mm 1fr;gap:5mm;}
.esp:last-child{border-bottom:none;}
.esp .k{font-size:7.2pt;letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);font-weight:700;padding-top:.6mm;}
.esp .v{color:var(--soft);font-size:8.8pt;}
.set-tot{display:grid;grid-template-columns:1fr 1fr;gap:6mm;margin-top:6mm;}
.set-tot .c{border:1px solid var(--line);border-radius:2px;padding:5mm 5.5mm;}
.set-tot .k{font-size:6.9pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--gold);font-weight:700;}
.set-tot .v{font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;
  font-weight:600;line-height:1.1;margin-top:1.5mm;}
"""

def brl(v): return f'{v:,.0f}'.replace(',', '.')
NP = 4
def foot(n):
    return (f'<div class="foot"><span>Valvic Marcenaria · {CLIENTE}</span>'
            f'<span>{OBRA}</span><span>{n} / {NP}</span></div>')
def bloco(setor):
    out = f'<div class="set">Setor {setor}</div>'
    for i, (s, k, nome, d, v) in enumerate(ITENS, 1):
        if s != setor: continue
        pr = k.split(' · ')[0]          # EX01… — referência da prancha
        out += (f'<div class="cj"><div class="cj-h">'
                f'<div class="cj-n">{i:02d}</div>'
                f'<div class="cj-t">{nome}</div>'
                f'<div class="cj-q">R$ {brl(v)}</div></div>'
                f'<div class="cj-d">{d} '
                f'<span style="color:var(--mut)">Prancha {pr}.</span>'
                f'</div></div>')
    return out

p1 = f"""<div class="page cover"><div class="pad">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div style="margin-top:auto">
    <div class="eyebrow">Proposta de marcenaria planejada</div>
    <div class="rule"></div>
    <div class="cv-t">{CLIENTE}</div>
    <div class="cv-s">{OBRA}<br>
    Nove conjuntos, sobre o projeto executivo de<br>{ARQ}</div>
  </div>
  <div class="cv-meta">
    <div><div class="k">Conjuntos</div><div class="v">9, em 2 setores</div></div>
    <div><div class="k">Prazo de entrega</div><div class="v">{PRAZO}</div></div>
    <div><div class="k">Validade</div><div class="v">{VALIDADE}</div></div>
  </div>
</div></div>"""

p2 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Escopo</div>
  <div class="rule"></div>
  <h2 class="h-sec">O que está sendo proposto.</h2>
  <p class="lead" style="margin-top:4mm">O levantamento foi feito sobre as
  quatro pranchas executivas — planta, vistas e seções de cada conjunto. O que
  está descrito abaixo é o que será executado.</p>
  <div style="margin-top:6mm">{bloco('Comercial')}</div>
  {foot(2)}
</div></div>"""

p3 = f"""<div class="page"><div class="pad">
  {bloco('Vendas')}
  <div class="set-tot">
    <div class="c"><div class="k">Setor Comercial</div>
      <div class="v">R$ {brl(COM)}</div></div>
    <div class="c"><div class="k">Setor Vendas</div>
      <div class="v">R$ {brl(VEN)}</div></div>
  </div>
  <table class="inv" style="margin-top:6mm">
    <tr class="tot"><td class="l">Investimento total</td>
      <td class="hi">R$ {brl(INV)}</td></tr>
  </table>
  <div class="box" style="margin-top:5mm"><div class="t">O que está dentro do valor</div>
  <p>Projeto de detalhamento para produção, fornecimento de material, produção
  em CNC e coladeira automática próprias, vidros temperados, perfis de inox e
  alumínio, serralheria da bancada da janela, iluminação em LED, transporte,
  entrega na obra e <strong>instalação e montagem por equipe própria da
  Valvic</strong>.</p></div>
  {foot(3)}
</div></div>"""

esp = ''.join(f'<div class="esp"><div class="k">{k}</div><div class="v">{v}</div>'
              f'</div>' for k, v in ESPEC)
fora = ''.join(f'<li><div class="k">{k}</div>'
               + (f'<div class="v">{v}</div>' if v else '') + '</li>'
               for k, v in FORA)

p4 = f"""<div class="page"><div class="pad">
  <div class="eyebrow">Especificação técnica</div>
  <div class="rule"></div>
  <h2 class="h-sec">Condições e especificação.</h2>
  <div style="margin-top:5mm">{esp}</div>
  <div class="two" style="margin-top:8mm">
    <div>
      <table class="pay">
        <tr><td colspan="2" style="border:none;padding-bottom:1.4mm">
          <span class="eyebrow">Formas de pagamento</span></td></tr>
        {''.join(f'<tr><td>{c}</td><td class="d">{d}</td></tr>' for c, d in PAGTO)}
      </table>
      <div class="term" style="margin-top:3mm"><div class="k">Prazo de entrega</div>
        <div class="v">{PRAZO}</div>
        <div class="s">Contados da aprovação e da medição em obra.</div></div>
      <div class="term"><div class="k">Conferência de medidas</div>
        <div class="v">Visita técnica antes do corte</div>
        <div class="s">Nada vai para a CNC antes da nossa medição no local.</div></div>
      <div class="term"><div class="k">Validade da proposta</div>
        <div class="v">{VALIDADE}</div></div>
    </div>
    <div class="fora">
      <div class="eyebrow">Não incluso nesta proposta</div>
      <div class="rule"></div>
      <ul>{fora}</ul>
    </div>
  </div>
  <div class="sig">
    <div class="ln">Valvic Marcenaria</div>
    <div class="ln">{CLIENTE}</div>
  </div>
  {foot(4)}
</div></div>"""

HTML = ('<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8">'
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:'
        'wght@400;500;600&family=DM+Sans:wght@300;400;500;600;700&display=swap" '
        f'rel="stylesheet"><style>{CSS}</style></head><body>{p1}{p2}{p3}{p4}</body></html>')

OUT_H, OUT_P = 'projetos/proposta-deva.html', 'projetos/proposta-deva.pdf'
open(OUT_H, 'w', encoding='utf-8').write(HTML)
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
subprocess.run(['node', '/tmp/r.js', OUT_P], check=True)
print(f'{OUT_H} · {OUT_P}')
print(f'  Comercial R$ {brl(COM)} + Vendas R$ {brl(VEN)} = R$ {brl(INV)}')
