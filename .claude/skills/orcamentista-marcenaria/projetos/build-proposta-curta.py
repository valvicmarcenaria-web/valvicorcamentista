# -*- coding: utf-8 -*-
"""PROPOSTA CURTA (até 3 folhas) — a síntese do caderno do Michell e do Gustavo
[Jonathan, 05/11/2026, Tereza Sá e Júnia Portugal]:
  "faça uma proposta para cada uma delas com até 3 páginas, sintetize as
   informações que estruturamos nas propostas do Michel e do Gustavo"

  Folha 1 · capa e abertura  — quem, onde, a arquiteta, a promessa da casa
  Folha 2 · o projeto        — imagens, os móveis sem medida, como trabalhamos
  Folha 3 · investimento     — valores, pagamento, prazo, garantia, fronteiras

⛔ Preço só na folha 3 · sem metragem nem contagem nas descrições · nenhum
   nome de outro cliente · valores lidos de `precos_lev.py` (+ fixos.json).
uso: python3 build-proposta-curta.py tereza-sa junia-portugal
"""
import sys, os, re, html, base64, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(P))
os.environ['LINHAS'] = 'hettich'
import precos_lev as PL

CSS = (P / 'css-apresentacao.css').read_text(encoding='utf-8')
src = (P / 'build-gustavo-caderno.py').read_text(encoding='utf-8')
EXTRA = re.search(r"EXTRA = '''(.*?)'''", src, re.S).group(1)
AJUSTE = re.search(r"AJUSTE = '''(.*?)'''", src, re.S).group(1)
EXTRA += '.inv td.hi, .inv th.hi{white-space:nowrap} .pay td.d{white-space:nowrap}'
E = lambda t: html.escape(str(t))
br = lambda v: 'R$ ' + f'{v:,.2f}'.replace(',', '@').replace('.', ',').replace('@', '.')

COMUM = dict(
    arq='Ocapi Arquitetura · Dalila Souza', arq_curto='Dalila Souza', data='Novembro de 2026',
    garantia='10 anos', prazo='60 dias corridos', validade='5 dias',
    pagto=[('Na assinatura do contrato', 0.50), ('Na entrega e instalação', 0.50)],
)
CLIENTES = {
 'tereza-sa': dict(COMUM,
    nome='Tereza Sá', capa='Tereza<br>Sá', obra='Apartamento Tomé de Souza',
    sub='O escritório e o banho da suíte,<br>do desenho à instalação.',
    img_capa='banho-01', band=['escritorio-02', 'banho-02', 'banho-03'],
    ambientes=[
     ('Escritório', [
       ('Armário baixo', 'Portas de correr e gavetões, por fora e por dentro no acabamento '
        'escolhido com a arquiteta, sobre rodapé recuado que deixa o móvel leve na parede.')]),
     ('Banho suíte', [
       ('Armário superior de espelho', 'Portas de correr inteiras em espelho, com trilho oculto, '
        'puxador passante e luz embutida sob o armário, que ilumina a bancada.'),
       ('Gabinete suspenso', 'Portas de abrir e gavetões sob a bancada, com corrediça oculta '
        'Hettich de fechamento amortecido.')])],
    fora=[('Pedra', 'Bancada e nicho em super nano glass.'),
          ('Banho', 'Box, louças, metais e acessórios.'),
          ('Escritório', 'Prateleiras de vidro existentes, persiana, escrivaninha, cadeiras e '
           'boiseries.'),
          ('Banho social', 'Não faz parte desta proposta.')]),
 'junia-portugal': dict(COMUM,
    nome='Júnia Portugal', capa='Júnia<br>Portugal', obra='Banho suíte',
    sub='O gabinete do banho da suíte,<br>do desenho à instalação.',
    img_capa='banho-02', band=['banho-01', 'banho-03'],
    ambientes=[
     ('Banho suíte', [
       ('Gabinete suspenso sob a bancada', 'Por fora no acabamento escolhido com a arquiteta e '
        'por dentro em branco, com puxador cava usinado na própria frente — sem peça '
        'aparente — e prateleira interna. Fica suspenso, livre do piso molhado.')])],
    fora=[('Pedra e revestimento', 'Bancada em mármore e nicho em porcelanato.'),
          ('Banho', 'Box, cuba, metais, espelho e acessórios.'),
          ('Obra', 'Porta, alizar, pintura e instalações.')]),
}

ETAPAS = [('Medição', 'Nossa equipe mede a obra no local: o projeto passa a conversar com a parede real.'),
          ('Detalhamento e fábrica', 'Cada decisão de execução é fechada antes de cortar; corte, usinagem e montagem acontecem na nossa fábrica.'),
          ('Conferência', 'O móvel é montado e testado aqui antes de sair: porta regulada, gaveta corrida, luz acesa.'),
          ('Instalação e termo', 'Equipe própria instala, nivela e regula. O termo de garantia é assinado na entrega.')]


def proposta(pasta):
    C = CLIENTES[pasta]
    B, T = PL.tabela(P / pasta, 400.0, 0.10, 0.03)
    H = T['hettich']
    IMG = {p.stem: 'data:image/jpeg;base64,' + base64.b64encode(p.read_bytes()).decode()
           for p in (P / f'img-{pasta}').glob('*.jpg')}
    S = []
    def folha(corpo, dark=False, rodape=True, n=[0]):
        n[0] += 1
        f = (f'<div class="foot"><span>Valvic&nbsp;·&nbsp;{E(C["nome"])}</span>'
             f'<span>{n[0]:02d}</span></div>') if rodape else ''
        S.append(f'<div class="slide{" dark" if dark else ""}">{corpo}{f}</div>')

    # ── 01 · capa e abertura ────────────────────────────────────────────
    folha(f'''<div class="cv">
 <div class="cv-l" style="padding-bottom:22mm">
  <div class="cv-brand">Valvic Marcenaria</div>
  <div class="cv-nome">{C['capa']}</div>
  <div class="cv-s">{C['sub']}</div>
  <p style="color:#CFC6B4;font-size:8.6pt;line-height:1.55;margin:6mm 0 0;max-width:86mm">
   Um projeto da <b style="color:#F6F1E7">{E(C['arq'])}</b>, executado por uma empresa só:
   medimos, detalhamos, fabricamos, montamos e instalamos. Um contrato, uma data, um nome
   para chamar.</p>
  <div class="cv-meta">
   <div><div class="k">Projeto</div><div class="v">{E(C['arq_curto'])}</div></div>
   <div><div class="k">Obra</div><div class="v">{E(C['obra'])}</div></div>
   <div><div class="k">Garantia</div><div class="v">{E(C['garantia'])} · Hettich</div></div>
   <div><div class="k">Data</div><div class="v">{E(C['data'])}</div></div>
  </div>
 </div>
 <div class="cv-r"><img src="{IMG[C['img_capa']]}" alt=""></div>
</div>''', dark=True, rodape=False)

    # ── 02 · o projeto ──────────────────────────────────────────────────
    band = ''.join(f'<img src="{IMG[i]}" alt="" style="flex:1;min-width:0">' for i in C['band'])
    amb = ''.join(f'''<div class="eyebrow" style="margin:{0 if i == 0 else 4}mm 0 2mm">{E(a)}</div>
      {''.join(f"""<div class="mv"><span class="b"></span><span><span class="t">{E(t)}</span>
       <span class="d">{E(d)}</span></span></div>""" for t, d in its)}'''
                  for i, (a, its) in enumerate(C['ambientes']))
    et = ''.join(f'''<div class="pe"><div class="pe-n">{i:02d}</div><div class="pe-t">{E(t)}</div>
      <div class="pe-l">{E(d)}</div></div>''' for i, (t, d) in enumerate(ETAPAS, 1))
    folha(f'''<div class="ambw">
 <div class="band" style="height:78mm;display:flex;gap:2mm">{band}<div class="tag">O projeto</div></div>
 <div class="low" style="display:block;padding:7mm 18mm 17mm"><div class="fitw">
  <div style="display:grid;grid-template-columns:1.15fr 1fr;gap:0 12mm">
   <div><h2 class="h2" style="margin:0 0 4mm">O que a Valvic executa.</h2>{amb}</div>
   <div><h2 class="h2" style="margin:0 0 4mm">Como trabalhamos.</h2>{et}
    <div class="amb-nota" style="margin-top:3mm"><div class="t">Uma arquiteta responsável</div>
     <p>Da aprovação à entrega, vocês falam com uma arquiteta nossa, que conversa com a
      {E(C['arq_curto'])} na mesma linguagem técnica e responde pelo resultado.</p></div></div>
  </div></div></div></div>''')
    N0 = len(S) + 1

    # ── 03 · investimento e condições ───────────────────────────────────
    rows = ''.join(f'<tr><td class="l">{E(x[0])} · {E(x[1])}</td><td class="hi">{br(v)}</td></tr>'
                   for x, v in H['pv'].items())
    pay = ''.join(f'<tr><td>{E(r)}</td><td class="d">{p*100:.0f}%</td>'
                  f'<td class="d" style="padding-left:4mm">{br(H["venda"] * p)}</td></tr>'
                  for r, p in C['pagto'])
    fora = ''.join(f'<li><div class="k">{E(k)}</div><div class="v">{E(v)}</div></li>' for k, v in C['fora'])
    folha(f'''<div class="pad" style="padding-bottom:20mm">
 <div class="eyebrow">Investimento e condições</div><div class="rule"></div>
 <h1 class="h1" style="margin:0 0 4mm">O investimento, e o que vem com ele.</h1>
 <div class="three" style="grid-template-columns:1.25fr 1fr .9fr;margin-top:3mm">
  <div>
   <table class="inv"><tr><th class="l">Item</th><th class="hi">Investimento</th></tr>{rows}
    <tr class="tot"><td class="l">Total · linha Hettich</td><td class="hi">{br(H['venda'])}</td></tr></table>
   <div class="box" style="margin-top:5mm"><div class="t">O que está incluso</div>
    <p>Projeto executivo de marcenaria, material, usinagem, ferragem Hettich, iluminação
     embutida quando indicada, transporte, montagem e instalação.</p></div>
  </div>
  <div>
   <table class="pay" style="width:100%"><tr><td colspan="3" style="border:none;padding-bottom:2mm">
    <span class="eyebrow">Pagamento</span></td></tr>{pay}</table>
   <div style="font-size:7.4pt;color:var(--mut);margin-top:2mm">Por transferência bancária.</div>
   <div class="term" style="margin-top:4mm"><div class="k">Entrega</div><div class="v">{E(C['prazo'])}</div>
    <div class="s">Contados a partir da medição técnica no local.</div></div>
   <div class="term"><div class="k">Garantia</div><div class="v">{E(C['garantia'])}</div>
    <div class="s">Sobre a marcenaria e a ferragem Hettich, em termo assinado na entrega.
     Instalação e regulagem, dois anos. Retorno em 24 horas e visita em até três dias úteis.</div></div>
   <div class="term"><div class="k">Validade desta proposta</div><div class="v">{E(C['validade'])}</div></div>
  </div>
  <div class="fora"><div class="eyebrow" style="margin-bottom:3mm">O que não está nesta proposta</div>
   <ul>{fora}</ul></div>
 </div>
 <div class="sig"><div class="ln">{E(C['nome'])}</div><div class="ln">Valvic Marcenaria · Vargas Decor LTDA</div></div>
</div>''')

    HTML = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
            f'<title>Proposta · {E(C["nome"])}</title>'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
            'family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:opsz,wght@'
            '9..40,400;9..40,500;9..40,600;9..40,700&display=swap">'
            f'<style>{CSS}{EXTRA}</style></head><body>' + ''.join(S)
            + f'<script>{AJUSTE}caber();</script></body></html>')

    # ── as travas ───────────────────────────────────────────────────────
    assert len(S) <= 3, '⛔ a proposta curta tem até três folhas'
    assert 'R$' not in ''.join(S[:N0 - 1]), '⛔ preço antes da folha de investimento'
    _t = re.sub(r'<[^>]+>', ' ', re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '', ''.join(S)))
    for c in ('Michell', 'Jéssica', 'Gustavo', 'Phillip', 'Giselle', 'Rafael', 'Janaina', 'Iara',
              *(n for k, v in CLIENTES.items() if k != pasta for n in v['nome'].split())):
        assert c not in _t, f'⛔ vestígio de outro cliente: {c}'
    assert not [c for c in '⭐⛔⚠' if c in ''.join(S)]
    _d = re.sub(r'<[^>]+>', ' ', re.sub(r'data:[^"]+', '', S[1]))
    assert not re.search(r'\d+\s*(cm|mm|m²|m\b)', _d), '⛔ medida na descrição'
    assert not re.search(r'\b(\d+|duas|dois|três|quatro|cinco)\s+(portas?|gavet\w+|prateleiras?)', _d, re.I)
    assert abs(sum(p for _, p in C['pagto']) - 1) < 1e-9

    out = P / pasta / f'proposta-{pasta}.html'
    out.write_text(HTML, encoding='utf-8')
    pdf = out.with_suffix('.pdf')
    subprocess.run(['node', str(P / 'render-pdf.js'), str(out), str(pdf)], check=True,
                   env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    print(f'{pdf.name} · {len(S)} folhas · {pdf.stat().st_size // 1024} kB · {br(H["venda"])}')


if __name__ == '__main__':
    for p in sys.argv[1:] or CLIENTES:
        proposta(p)
