# -*- coding: utf-8 -*-
"""PAINEL DA SALA — o que cada decisão e cada dúvida custa, em reais.

⭐ Roda o levantamento inteiro em cada cenário, em SUBPROCESSO num diretório
  temporário, porque `base.py` é lido como módulo próprio e trocar uma
  constante em memória não muda nada — e não mudar nada, calado, é o pior
  resultado possível.
"""
import subprocess, sys, pathlib, tempfile, shutil, re, os

P = pathlib.Path(__file__).resolve().parent
SONDA = ('import importlib.util,pathlib,sys\n'
         'd=pathlib.Path(__file__).resolve().parent\n'
         'sp=importlib.util.spec_from_file_location("lv",d/"levantamento.py")\n'
         'm=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)\n'
         'print("%.2f" % m.DIRETO)\n')


def roda(subs=(), env=None):
    """subs: lista de (regex, troca) aplicados a base.py antes de rodar."""
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        for f in ('base.py', 'levantamento.py'):
            shutil.copy(P / f, d / f)
        if subs:
            t = (d / 'base.py').read_text()
            for pat, rep in subs:
                t, n = re.subn(pat, rep, t, count=1, flags=re.M)
                assert n == 1, pat          # ⛔ troca que não pega é erro
            (d / 'base.py').write_text(t)
        (d / '_s.py').write_text(SONDA)
        r = subprocess.run([sys.executable, '-I', str(d / '_s.py')],
                           capture_output=True, text=True,
                           env=dict(os.environ, **(env or {})))
        assert r.returncode == 0, r.stderr[-900:]
        return float(r.stdout.strip())


def brl(v):
    return f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')


BASE = roda()
print(f'\n  PAINEL DA SALA · VISTA 2 — O QUE CADA DECISÃO CUSTA')
print(f'\n  CUSTO DIRETO COMO ORÇADO{brl(BASE):>52}\n')

LINHAS = [
 ('A ORDEM DO JONATHAN · ripado só até a pedra', None, None, None),
 ('  se o ripado corresse os 682 inteiros',
  [(r'^LISO_L_RIPADO = .*$', '')], None, 'ripado_tudo'),
 ('AS DÚVIDAS QUE AINDA TÊM PREÇO', None, None, None),
 ('  Gianduia Trama for padrão especial (R$ 1.000 a chapa)',
  None, {'ESPECIAL': '1'}, None),
 ('  a ripa de 2 cm entrar na coladeira (R$ 2,50)',
  None, {'RIPA_NA_MAQUINA': '1'}, None),
 ('  a dobradiça cair para Novisys (R$ 20)',
  [(r'^DOBRADICA = 50\.0$', 'DOBRADICA = 20.0')], None, None),
 ('  a dobradiça cair para Bigfer Inox Click (R$ 10)',
  [(r'^DOBRADICA = 50\.0$', 'DOBRADICA = 10.0')], None, None),
 ('  a base do ripado sair em 18 e não em 15',
  [(r'^SUBSTRATO_ESP_MM = 15$', 'SUBSTRATO_ESP_MM = 18')], None, None),
 ('  os montantes forem a cada 75 cm e não a cada 60',
  None, None, 'montantes'),
]

for rot, subs, env, especial in LINHAS:
    if subs is None and env is None and especial is None:
        print(f'  {rot}'); continue
    if especial == 'ripado_tudo':
        v = roda_tudo = None
        continue
    if especial == 'montantes':
        continue
    v = roda(subs or (), env)
    print(f'  {rot:<54}{brl(v):>14}{("+ " if v > BASE else "− ") + brl(abs(v-BASE)):>16}')

#   ⭐ os dois cenários que mexem no levantamento, não na base
import importlib.util, copy
sp = importlib.util.spec_from_file_location('lv', P / 'levantamento.py')
lv = importlib.util.module_from_spec(sp); sp.loader.exec_module(lv)

_t = [copy.deepcopy(i) for i in lv.M]
_x = lv.Item('Ripado sobre os 330 do liso', '')
_x.ripado(lv.LISO_L, lv.ALT, 'Ripado do trecho liso')
_t.append(_x)
v = lv.custo(_t)['direto']
print(f'\n  {"se o ripado corresse os 682 inteiros":<54}{brl(v):>14}'
      f'{"+ " + brl(v - BASE):>16}')

_t = [copy.deepcopy(i) for i in lv.M]
for i in _t:
    for p in i.pecas:
        if p['nome'].startswith('Montantes'):
            p['qtd'] = 10
v = lv.custo(_t)['direto']
print(f'  {"se os montantes forem a cada 75 cm":<54}{brl(v):>14}'
      f'{"− " + brl(BASE - v):>16}')
