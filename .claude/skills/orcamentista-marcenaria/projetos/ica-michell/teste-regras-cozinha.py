# -*- coding: utf-8 -*-
"""Testa as regras NOVAS do auditor pela violação.

⛔⛔ Regra que nunca disparou é regra que não funciona. A lição é de 28/10,
  quando um `assert PARCEIRA in texto` passou por dois dias conferindo a
  variável contra ela mesma. ⭐ E o teste negativo tem de distinguir MORTE
  POR REGRA de morte por erro de sintaxe: só vale se a mensagem esperada
  aparecer na saída.
"""
import subprocess, sys, pathlib, shutil, os
P = pathlib.Path(__file__).resolve().parent
ORIG = (P/'cozinha.py').read_text()

CASOS = [
 ('puxador E cava na mesma frente',
  "CAVA     = []",
  "CAVA     = [(I1, 'Frentes da ilha', 7, 55)]",
  'PUXADOR e CAVA'),
 ('frente provençal sem as travessas de 6 mm',
  "*provencal('Frente · porta',         I1, 69, 85, 1, VF15, VF6, 'De giro · provençal'),",
  "P('Frente · porta', I1, 69, 85, 1, VF15, (2, 2), 'De giro'),",
  'travessas deitadas'),
 ('frente provençal sem a mão de obra de moldura',
  "MOLDURA  = [(I1, 'Frentes da ilha',     7),",
  "MOLDURA  = [(I1, 'Frentes da ilha',     6),",
  'mão de obra'),
 ('báscula sem articulador',
  "BASCULAS= [(I2, 'Torre, Superior 01 e Superior 02 · fecho toque', 17)]",
  "BASCULAS= [(I2, 'Torre, Superior 01 e Superior 02 · fecho toque', 16)]",
  'articuladores'),
 ('gaveta sem corrediça',
  "*gaveta(I1, 60, 100, 18, 2, 'Gaveta'),",
  "*gaveta(I1, 60, 100, 18, 3, 'Gaveta'),",
  'pares de corrediça'),
 ('chave de chapa que não existe na Base',
  "EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'",
  "EST, FUN = 'MDF Branco Inventado 15', 'MDF Branco TX 6'",
  'chave fora da Base'),
 ('peça que não cabe na chapa',
  "P('Lateral',               I1, 110, 85, 2, VF, (1, 0),",
  "P('Lateral',               I1, 300, 300, 2, VF, (1, 0),",
  'NÃO CABE'),
]
W = 74; print('═'*W); print('TESTE NEGATIVO · as regras quebram quando devem?'); print('═'*W)
ok = 0
for nome, velho, novo, esperado in CASOS:
    assert velho in ORIG, f'⛔ âncora não encontrada: {nome}'
    (P/'cozinha.py').write_text(ORIG.replace(velho, novo, 1))
    # ⛔⛔ O BYTECODE VELHO MENTE. A invalidação do .pyc olha o mtime com
    #   granularidade de 1 segundo: duas escritas no mesmo segundo fazem o
    #   Python reaproveitar o .pyc anterior, e o caso roda com o ARQUIVO DO
    #   CASO DE ANTES. Foi assim que este teste deu "passou" para uma regra
    #   que funciona e "falhou" para duas que também funcionam.
    #   ⭐ Então: apaga o cache e proíbe escrever outro.
    shutil.rmtree(P/'__pycache__', ignore_errors=True)
    amb = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    r = subprocess.run([sys.executable, '-B', str(P/'auditor.py'), 'cozinha'],
                       capture_output=True, text=True, cwd=P, env=amb)
    saida = r.stdout + r.stderr
    pegou = r.returncode != 0 and esperado in saida
    # ⭐ a distinção que importa: morreu PELA REGRA, ou morreu de erro?
    quebrou_feio = 'Traceback' in saida and esperado not in saida
    marca = '✓' if pegou else ('⛔ MORREU DE ERRO, não pela regra' if quebrou_feio
                               else '⛔ PASSOU')
    print(f'  {marca:4} {nome}')
    if not pegou:
        print(f'       esperava "{esperado}" na saída · rc={r.returncode}')
        # ⭐ mostra TODAS as falhas, não só a última: foi olhar só a última
        #   que me fez procurar o bug no lugar errado
        for ln in saida.strip().splitlines():
            if '⛔' in ln or 'Error' in ln: print('       ' + ln.strip()[:96])
    ok += pegou
(P/'cozinha.py').write_text(ORIG)
print(f'\n  {ok}/{len(CASOS)} violações barradas')
sys.exit(0 if ok == len(CASOS) else 1)
