# -*- coding: utf-8 -*-
"""ANDREA · clínica de dermatologia — folha de aditivo  [v2 · 26/10/2026]

⭐ [Jonathan 24/10] "Preciso criar uma página de aditivo de orçamento para
   a cliente Andrea da clínica de dermatologia. (…) Não exponha o erro,
   vamos expor a SOLUÇÃO, que será a aplicação de laminado de alta pressão
   (fórmica) revestindo todos os painéis e portas que já estão prontos na
   fábrica. (…) aplique as imagens de forma criativa no layout."

⭐⭐ v2 · [Paula Galante → Jonathan, 26/10] a parceira pediu estrutura de
   valor em três linhas, e pediu para APARECER como quem absorve a
   diferença: "Quero sim que a cliente saiba o quanto lamentei por este
   inconveniente e que estou arcando com parte do valor".

     01  execução de marcenaria sob medida ................  R$ 16.500,00
     02  subsídio técnico ................................ − R$ 10.560,00
         VALOR LÍQUIDO A PAGAR PELA CONTRATANTE ..........   R$  5.940,00

⛔⛔ A FOLHA NÃO ACUSA NINGUÉM, E NÃO DIZ QUE ALGO ESTÁ ERRADO. A regra do
   Jonathan continua valendo: expor a solução, nunca o erro. O que mudou é
   que agora o GESTO da parceira aparece — o gesto, não a falha.
   ⛔ Nem o nome dela nem a palavra "designer de ambientes" acusam: a folha
     diz que o memorial HOMOLOGADO especifica este acabamento (fato, não
     culpa) e que a responsável pelo projeto optou por absorver a
     diferença (gesto). Ninguém errou; o documento está sendo cumprido.

⭐ AS TRÊS IMAGENS CONTAM O PROCESSO, não decoram: a lâmina (o quê), a
   colagem (como) e a camada (o resultado).

⛔ UMA PÁGINA. Sem metragem e sem quantitativo: contagem só por extenso.

Números de `corte-andrea-aditivo.py` e `corte-andrea-subsidio.py`; nada
digitado à mão. As travas no fim do arquivo leem o HTML pronto.
"""
import pathlib, subprocess, importlib.util, sys, io, contextlib, os, base64, re

P = pathlib.Path(__file__).resolve().parent
def carrega(nome, mod):
    spec = importlib.util.spec_from_file_location(mod, P/nome)
    m = importlib.util.module_from_spec(spec); sys.modules[mod] = m
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
    return m
an  = carrega('corte-andrea-aditivo.py',  'an')
sub = carrega('corte-andrea-subsidio.py', 'sub')

br  = lambda v: f'{v:,.0f}'.replace(',', '.')
rs  = lambda v: ('− ' if v < 0 else '') + 'R$ ' + \
      f'{abs(v):,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')

CLIENTE, OBRA = 'Andrea', 'Clínica de dermatologia'
DATA = '26 de outubro de 2026'
MATERIAL, ACABAMENTO = 'Carvalho Mel', 'Top Matt'
PRAZO_MAT, PRAZO_EXEC, PRAZO_TOT = '45 a 60 dias', '30 dias', 'cerca de 90 dias'
VALIDADE = '7 dias úteis'
NP = 1
EXECUCAO, SUBSIDIO, LIQUIDO = sub.EXECUCAO, sub.SUBSIDIO, sub.LIQUIDO

# ⛔⛔ TRAVAS DE NÚMERO
assert EXECUCAO == 16500.00, '⛔ O INVESTIMENTO NÃO É MAIS O DO JONATHAN'
assert SUBSIDIO == 10560.00, '⛔ O SUBSÍDIO NÃO É MAIS O DA PAULA'
assert LIQUIDO  ==  5940.00, '⛔ O LÍQUIDO NÃO FECHA EM 5.940'
assert EXECUCAO - SUBSIDIO == LIQUIDO, '⛔ A TABELA DE VALOR NÃO SOMA'
assert an.MC_PISO == 0.35, '⛔ O PISO DA CASA MUDOU'
# ⛔ "SE ESTÁ NO TEXTO, TEM DE ESTAR NA CONTA": a folha promete lixamento,
#   duas demãos de cola, desbaste, relaminação dos topos e instalação. Se o
#   motor perder qualquer uma dessas linhas, a folha vende o que não foi
#   orçado.
assert an.LIXA_M2 > 0 and an.COLA_LATA > 0 and an.FITA_M > 0, \
    '⛔ UMA ETAPA DO PROCESSO SUMIU DA CONTA'
assert an.MO_M2 > 0 and an.INSTALA > 0, '⛔ A MÃO DE OBRA OU A INSTALAÇÃO SUMIU'

IMG = P/'img-andrea'
b64 = lambda n, t='png': (f'data:image/{t};base64,'
                          + base64.b64encode((IMG/n).read_bytes()).decode())
LAMINA, COLA, CAMADA = b64('lamina.png'), b64('cola.jpg', 'jpeg'), b64('camada.png')

QUADROS = [
 (LAMINA, 'contain', 'A lâmina',
  'Camada contínua e <b>sem poro</b>, que cobre a face inteira da peça.'),
 (COLA, 'cover', 'A colagem',
  '<b>Duas demãos</b> de cola nos dois materiais e prensagem à mão, peça '
  'por peça.'),
 (CAMADA, 'contain', 'A camada',
  'Uma pele nova sobre o que já está pronto: <b>o móvel não é refeito</b>, '
  'é revestido.'),
]

ETAPAS = [
 ('01', 'Lixamento', 'da superfície atual, até gerar poro e aderência.'),
 ('02', 'Corte', 'das lâminas de laminado, peça a peça.'),
 ('03', 'Cola', 'em duas demãos, aplicada nos dois materiais.'),
 ('04', 'Colagem', 'delicada sobre as superfícies, com prensagem.'),
 ('05', 'Desbaste', 'das arestas, para a lâmina terminar rente.'),
 ('06', 'Relaminação', 'dos topos com fita de borda no padrão.'),
 ('07', 'Conferência', 'peça por peça e instalação no local.'),
]

# ── ⭐⭐ AS DUAS LINHAS DE VALOR ────────────────────────────────────────
#   ⛔ a linha 02 credita o GESTO sem nomear falha nem pessoa, e diz que o
#     subsídio é liquidado direto junto à Valvic — o que a transforma, no
#     papel, em crédito contra terceiro e não em desconto concedido.
LINHAS = [
 ('01', 'Execução de marcenaria sob medida', 'Revestimento de <b>todos os '
  'painéis e portas</b> conforme o memorial homologado — material, '
  'aplicação e instalação no local.', EXECUCAO),
 ('02', 'Subsídio técnico', 'Adequação de custo à homologação do projeto, '
  'liquidada <b>diretamente junto à Valvic</b>.', -SUBSIDIO),
]

# ⭐ A OBSERVAÇÃO — a redação da Paula, reescrita para não acusar ninguém.
#   ⛔ o que saiu: "o material de menor custo indicado pela designer de
#     ambientes, mas o mesmo não foi atualizado no projeto aprovado pela
#     prefeitura". Numa folha da Valvic isso é a Valvic registrando, por
#     escrito e no documento que a cliente guarda, que a parceira falhou.
#   ⭐ o que entrou: o memorial homologado ESPECIFICA este acabamento (fato)
#     e a responsável pelo projeto OPTOU por absorver a diferença (gesto).
OBS = ('O acabamento especificado no memorial homologado está acima do '
       'previsto no orçamento contratado. A responsável pelo projeto de '
       'interiores optou por <b>absorver integralmente a diferença de custo '
       'do material</b>, concedida como subsídio técnico nesta proposta.')

# ⛔⛔ O "SEM VISAR LUCRO" NÃO ENTRA. A Paula pediu; a conta não permite.
#   A R$ 16.500 a MC é de 35% a 43% na faixa provável de área — não é custo.
#   ⭐ O que é VERDADE e diz quase o mesmo: o aditivo foi orçado sem RT e
#     sem comissão de vendedor, por ser adequação de contrato em curso. Base
#     84,88% contra 67,30% de serviço avulso: 17,6 pontos, −35% de preço.
COND = ('Valor praticado em <b>condição especial de adequação</b>, por se '
        'tratar de obra em andamento — sem o acréscimo aplicado a serviço '
        'avulso. Pagamento conforme o <b>contrato vigente</b>.')

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
.pad{padding:12mm 16mm 11mm;height:100%;display:flex;flex-direction:column;}
.foot{margin-top:auto;padding-top:3.4mm;border-top:1px solid var(--line);
      display:flex;justify-content:space-between;font-size:7pt;
      letter-spacing:.18em;text-transform:uppercase;color:var(--mut);flex:none;}

.hd{display:flex;justify-content:space-between;align-items:baseline;
  border-bottom:1.6px solid var(--ink);padding-bottom:3mm;flex:none;}
.hd .b{font-size:8pt;letter-spacing:.4em;text-transform:uppercase;font-weight:700;}
.hd .m{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--mut);font-weight:700;}
.eye{font-size:7pt;letter-spacing:.3em;text-transform:uppercase;
  color:var(--mel);font-weight:700;margin-top:3mm;flex:none;}
.h1{font-family:'Cormorant Garamond',Georgia,serif;font-size:22pt;
  line-height:1.03;font-weight:600;letter-spacing:-.022em;margin-top:1.2mm;
  flex:none;}
.h1 i{font-style:normal;color:var(--mel);}
.lead{margin-top:2.4mm;font-size:8.6pt;line-height:1.44;color:var(--soft);
  max-width:170mm;flex:none;}
.lead b{color:var(--ink);font-weight:600;}

/* ── a faixa das três imagens: lâmina · colagem · camada ───────────── */
.band{margin-top:3mm;display:grid;grid-template-columns:repeat(3,1fr);
  gap:4.5mm;flex:none;}
.q{display:flex;flex-direction:column;}
.q .ph{height:21mm;border-radius:3px;overflow:hidden;background:#fff;
  border:1px solid var(--line);display:flex;align-items:center;
  justify-content:center;}
.q .ph img{width:100%;height:100%;display:block;}
.q .ph img.contain{object-fit:contain;padding:1.2mm 2.2mm;}
.q .ph img.cover{object-fit:cover;object-position:46% 52%;}
.q .n{margin-top:2.2mm;display:flex;align-items:baseline;gap:2.4mm;}
.q .n .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:14pt;
  font-weight:700;line-height:1;}
.q .n .r{flex:1;height:1px;background:var(--line);}
.q .d{margin-top:1.2mm;font-size:7.8pt;line-height:1.4;color:var(--soft);}
.q .d b{color:var(--ink);font-weight:600;}

.sec{margin-top:2.8mm;font-size:7pt;letter-spacing:.28em;text-transform:uppercase;
  color:var(--mel);font-weight:700;flex:none;}
.steps{margin-top:1.6mm;display:grid;grid-template-columns:repeat(2,1fr);
  gap:0 9mm;flex:none;}
.st{display:grid;grid-template-columns:8mm 1fr;gap:2.6mm;align-items:baseline;
  padding:.8mm 0;border-top:1px solid var(--line);}
.st .k{font-family:'Cormorant Garamond',Georgia,serif;font-size:12pt;
  font-weight:700;color:var(--mel);line-height:1;}
.st .d{font-size:8pt;line-height:1.38;color:var(--soft);}
.st .d b{color:var(--ink);font-weight:600;}

.two{margin-top:2.8mm;display:grid;grid-template-columns:1fr 1fr;gap:4.5mm;
  flex:none;}
.bx{background:var(--clin);border-radius:3px;padding:2.6mm 4.4mm;}
.bx .k{font-size:6.8pt;letter-spacing:.24em;text-transform:uppercase;
  color:var(--mel);font-weight:700;}
.bx .t{font-family:'Cormorant Garamond',Georgia,serif;font-size:13pt;
  font-weight:600;line-height:1.1;margin-top:1.2mm;}
.bx .d{font-size:7.8pt;line-height:1.42;color:var(--soft);margin-top:1.2mm;}
.bx .d b{color:var(--ink);font-weight:600;}
.pz{margin-top:1.5mm;display:grid;grid-template-columns:auto 1fr;gap:.6mm 3.2mm;
  font-size:7.8pt;color:var(--soft);}
.pz b{color:var(--ink);font-weight:600;white-space:nowrap;}

/* ── ⭐⭐ O BLOCO DE VALOR: duas linhas e o líquido ─────────────────── */
.inv{margin-top:3.2mm;background:var(--esp);color:#F2F0EB;border-radius:3px;
  padding:3mm 5.6mm 3.2mm;flex:none;}
.inv .cap{font-size:6.8pt;letter-spacing:.26em;text-transform:uppercase;
  color:var(--mel-lt);font-weight:700;}
.ln{display:grid;grid-template-columns:6.4mm 1fr auto;gap:0 4mm;
  align-items:baseline;padding:1.4mm 0;
  border-top:1px solid rgba(230,207,164,.22);margin-top:1.8mm;}
.ln + .ln{margin-top:0;}
.ln .i{font-family:'Cormorant Garamond',Georgia,serif;font-size:12pt;
  font-weight:700;color:var(--mel-lt);line-height:1;}
.ln .t{font-size:7.6pt;line-height:1.36;color:#AFB9BB;}
.ln .t em{font-style:normal;display:block;font-size:9pt;font-weight:600;
  color:#EFEDE7;letter-spacing:-.004em;margin-bottom:.5mm;}
.ln .t b{color:#DDE2E2;font-weight:600;}
.ln .v{font-size:11pt;font-weight:600;color:#EFEDE7;
  font-variant-numeric:tabular-nums;white-space:nowrap;}
.ln .v.neg{color:var(--mel-lt);}
.tot{margin-top:2.2mm;padding-top:2.2mm;border-top:1.4px solid var(--mel);
  display:flex;justify-content:space-between;align-items:flex-end;gap:8mm;}
.tot .lab{font-size:7.4pt;letter-spacing:.2em;text-transform:uppercase;
  color:var(--mel-lt);font-weight:700;line-height:1.3;}
.tot .big{font-family:'Cormorant Garamond',Georgia,serif;font-size:27pt;
  font-weight:700;color:#fff;line-height:.86;letter-spacing:-.03em;
  font-variant-numeric:tabular-nums;white-space:nowrap;}

.cond{margin-top:2mm;padding-top:1.8mm;
  border-top:1px solid rgba(230,207,164,.22);font-size:7.1pt;line-height:1.38;
  color:#A7B2B4;}
.cond b{color:#D6DBDB;font-weight:600;}
.obs{margin-top:2.8mm;flex:none;}
.ob{background:var(--clin);border-radius:3px;padding:2.6mm 4.6mm;}
.ob .k{font-size:6.6pt;letter-spacing:.24em;text-transform:uppercase;
  color:var(--mel);font-weight:700;}
.ob .d{font-size:7.8pt;line-height:1.44;color:var(--soft);margin-top:1.3mm;}
.ob .d b{color:var(--ink);font-weight:600;}

.strip{margin-top:2.6mm;padding-top:2.2mm;border-top:1px solid var(--line);
  display:flex;justify-content:space-between;gap:5mm;font-size:8pt;
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

linhas = ''.join(
 f'<div class="ln"><div class="i">{i}</div>'
 f'<div class="t"><em>{tit}</em>{d}</div>'
 f'<div class="v{" neg" if v < 0 else ""}">{rs(v)}</div></div>'
 for i, tit, d, v in LINHAS)

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
  higienizada todos os dias. É o que o <b>memorial descritivo
  homologado</b> especifica para estas superfícies — e é o que este aditivo
  entrega: <b>todos os painéis e portas já produzidos</b> levados a
  acabamento em <b>laminado de alta pressão</b>: lâmina contínua e não
  porosa, que aguenta a limpeza diária sem abrir nem manchar. <b>O projeto,
  as medidas e as ferragens permanecem como estão</b> — muda a face.</div>

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
      <div class="d">Os dois correm <b>em sequência</b>, não em paralelo: a
      aplicação começa com a lâmina em casa.</div></div>
  </div>

  <div class="inv">
    <div class="cap">Composição do investimento</div>
    {linhas}
    <div class="tot">
      <div class="lab">Valor líquido a pagar pela contratante</div>
      <div class="big">{rs(LIQUIDO)}</div>
    </div>
    <div class="cond">{COND}</div>
  </div>

  <div class="obs">
    <div class="ob"><div class="k">Observação</div>
      <div class="d">{OBS}</div></div>
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

# ══ ⛔⛔ AS TRAVAS DE LINGUAGEM — leem a folha pronta ═══════════════════
texto = re.sub(r'<[^>]+>', ' ', HTML.split('</style>')[1])
texto = re.sub(r'\s+', ' ', texto)

#  ⛔ a folha não acusa, não nomeia a parceira e não promete o que a conta
#    não sustenta. Qualquer uma destas palavras na folha é passivo.
PROIBIDO = [
 (r'\berr[oa]s?\b',            'acusa: fala de ERRO'),
 (r'\bequívocos?\b|\bequivocos?\b', 'acusa: fala de EQUÍVOCO'),
 (r'\bfalh[ao]s?\b',           'acusa: fala de FALHA'),
 (r'\bengan[oa]s?\b',          'acusa: fala de ENGANO'),
 (r'\bdivergênc|\bdivergiu\b|\bdivergente\b', 'acusa: fala de DIVERGÊNCIA'),
 (r'\bincorret|\binadequad|\bimprópri', 'acusa: diz que o que está lá não serve'),
 (r'\bPaula\b|\bGalante\b',    '⛔ NOMEIA A PARCEIRA'),
 (r'\bdecorador|\bdesigner de ambientes\b', '⛔ IDENTIFICA A PARCEIRA pelo papel'),
 (r'não foi atualizad|não atualizad', 'acusa: aponta documento não atualizado'),
 (r'sem lucro|sem visar lucro|apenas o custo|a preço de custo',
  '⛔ PROMETE "SEM LUCRO" — a R$ 16.500 a MC é de 35% a 43%, não é custo'),
 (r'\d+\s*m²|\d+\s*m2|metro quadrado', '⛔ PÕE METRAGEM NA FOLHA'),
 (r'\bchapas?\b|\bfit[ao]s de borda\b.*\bmetros\b', '⛔ PÕE QUANTITATIVO'),
]
falhas = [m for rx, m in PROIBIDO if re.search(rx, texto, re.I)]
assert not falhas, '⛔⛔ A FOLHA VIOLOU A REGRA:\n  · ' + '\n  · '.join(falhas)

#  ⭐ e o que TEM de estar: os três valores, conferidos no texto renderizado
for rot, v in (('execução', EXECUCAO), ('subsídio', SUBSIDIO), ('líquido', LIQUIDO)):
    assert rs(v).replace('− ', '') in texto, f'⛔ O VALOR DE {rot.upper()} SUMIU DA FOLHA'
assert '− R$ 10.560,00' in texto, '⛔ O SUBSÍDIO PERDEU O SINAL DE ABATIMENTO'
assert 'homologad' in texto, '⛔ A ÂNCORA DO MEMORIAL HOMOLOGADO SUMIU'
assert 'absorver integralmente' in texto, '⛔ O GESTO DA PARCEIRA SUMIU DA FOLHA'

(P/'aditivo-andrea-laminacao.html').write_text(HTML, encoding='utf-8')
open('/tmp/in.html', 'w', encoding='utf-8').write(HTML)
env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules',
           PW_CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
r = subprocess.run(['node', '/tmp/r2.js', str(P/'aditivo-andrea-laminacao.pdf')],
                   check=True, env=env, capture_output=True, text=True)
med = [l for l in r.stdout.splitlines() if l.startswith('MEDIDA')]
print(f'aditivo-andrea-laminacao.pdf · {NP} página')
print(f'  material          {MATERIAL} {ACABAMENTO} (mediante disponibilidade)')
print(f'  prazo             {PRAZO_MAT} + {PRAZO_EXEC} = {PRAZO_TOT}')
print(f'  01 execução       {rs(EXECUCAO)}  ⭐ preço do Jonathan, intocado')
print(f'  02 subsídio       {rs(-SUBSIDIO)}  ⭐ o gesto da parceira')
print(f'  LÍQUIDO           {rs(LIQUIDO)}  ← o número grande da folha')
print(f'  ✓ travas de linguagem: {len(PROIBIDO)} regras, nenhuma violada')
if med:
    import json
    for m in json.loads(med[0][7:]):
        s, o = m['slack'], m['over']
        ok = o <= 0.05 and s >= 3.0
        print(f'  {"✓" if ok else "⛔"} folga vertical  {s:+.1f} mm'
              + ('' if o <= 0.05 else f'  ⛔ ESTOURO DE {o:.1f} mm')
              + ('' if s >= 3.0 else '  ⚠ APERTADO: menos de 3 mm de respiro'))
