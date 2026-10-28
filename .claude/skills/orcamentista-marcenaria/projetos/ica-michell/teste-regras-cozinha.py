# -*- coding: utf-8 -*-
"""Testa as regras NOVAS do auditor pela violação, em qualquer ambiente.

⛔⛔ Regra que nunca disparou é regra que não funciona. A lição é de 28/10,
  quando um `assert PARCEIRA in texto` passou por dois dias conferindo a
  variável contra ela mesma. ⭐ E o teste negativo tem de distinguir MORTE
  POR REGRA de morte por erro de sintaxe: só vale se a mensagem esperada
  aparecer na saída.
"""
import subprocess, sys, pathlib, shutil, os
P = pathlib.Path(__file__).resolve().parent
ORIG = {n: (P/f'{n}.py').read_text() for n in ('cozinha', 'banhogourmet')}

# ⭐ cada caso é (ambiente, nome, âncora, mutação, mensagem esperada). O
#   ambiente entrou quando as regras passaram a nascer fora da Cozinha: o
#   pulsador e a perda de serra da ripa vieram do Banho Gourmet, e regra que
#   só se testa no arquivo onde não nasceu é regra meio testada.
CASOS = [
 ('cozinha', 'puxador E cava na mesma frente',
  "CAVA     = []",
  "CAVA     = [(I1, 'Frentes da ilha', 7, 55)]",
  'PUXADOR e CAVA'),
 # ⭐ o caso trocou de alvo quando o método mudou: não há mais travessa
 #   para faltar, mas há a RÉGUA para voltar — e é o que esta mutação faz.
 ('cozinha', 'moldura provençal encolhida para régua, em vez de peça inteira',
  "*provencal('Frente · porta',         I1, 69, 85, 1, VF15, VF6, 'De giro · provençal'),",
  "P('Frente · porta', I1, 69, 85, 1, VF15, (2, 2), 'De giro'),\n"
  " P('Frente · porta · moldura usinada', I1, 69, 7, 1, VF6, (0, 0), 'régua'),",
  'não régua'),
 ('cozinha', 'frente provençal sem a mão de obra de moldura',
  "MOLDURA  = [(I1, 'Frentes da ilha',     7),",
  "MOLDURA  = [(I1, 'Frentes da ilha',     6),",
  'mão de obra'),
 ('cozinha', 'báscula sem articulador',
  "BASCULAS= [(I2, 'Torre, Superior 01 e Superior 02 · fecho toque', 17)]",
  "BASCULAS= [(I2, 'Torre, Superior 01 e Superior 02 · fecho toque', 16)]",
  'articuladores'),
 ('cozinha', 'gaveta sem corrediça',
  "*gaveta(I1, 60, 100, 18, 2, 'Gaveta'),",
  "*gaveta(I1, 60, 100, 18, 3, 'Gaveta'),",
  'pares de corrediça'),
 ('cozinha', 'chave de chapa que não existe na Base',
  "EST, FUN = 'MDF Branco TX 15', 'MDF Branco TX 6'",
  "EST, FUN = 'MDF Branco Inventado 15', 'MDF Branco TX 6'",
  'chave fora da Base'),
 ('cozinha', 'peça que não cabe na chapa',
  "P('Lateral',               I1, 110, 85, 2, VF, (1, 0),",
  "P('Lateral',               I1, 300, 300, 2, VF, (1, 0),",
  'NÃO CABE'),
 # ⭐ as regras novas de 28/10, as duas nascidas no Banho Gourmet
 ('banhogourmet', 'pulsador E cava na mesma frente',
  "CAVA     = []",
  "CAVA     = [(I1, 'Portas ripadas', 2, 37)]",
  'PULSADOR e CAVA'),
 ('banhogourmet', 'porta ripada sem modo nenhum de abrir',
  "2, 'un', 'Pulsador')]",
  "2, 'un', 'Fecho-de-toque')]",
  'sem NENHUM modo de'),
 ('banhogourmet', 'chave de OUTRAS que não existe na Base',
  "2, 'un', 'Pulsador')]",
  "2, 'un', 'Pulsadorr')]",
  'chave de OUTRAS fora da Base'),
]
W = 74; print('═'*W); print('TESTE NEGATIVO · as regras quebram quando devem?'); print('═'*W)
ok = 0
for amb, nome, velho, novo, esperado in CASOS:
    assert velho in ORIG[amb], f'⛔ âncora não encontrada em {amb}: {nome}'
    (P/f'{amb}.py').write_text(ORIG[amb].replace(velho, novo, 1))
    # ⛔⛔ O BYTECODE VELHO MENTE. A invalidação do .pyc olha o mtime com
    #   granularidade de 1 segundo: duas escritas no mesmo segundo fazem o
    #   Python reaproveitar o .pyc anterior, e o caso roda com o ARQUIVO DO
    #   CASO DE ANTES. Foi assim que este teste deu "passou" para uma regra
    #   que funciona e "falhou" para duas que também funcionam.
    #   ⭐ Então: apaga o cache e proíbe escrever outro.
    shutil.rmtree(P/'__pycache__', ignore_errors=True)
    ambiente = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    r = subprocess.run([sys.executable, '-B', str(P/'auditor.py'), amb],
                       capture_output=True, text=True, cwd=P, env=ambiente)
    saida = r.stdout + r.stderr
    pegou = r.returncode != 0 and esperado in saida
    # ⭐ a distinção que importa: morreu PELA REGRA, ou morreu de erro?
    quebrou_feio = 'Traceback' in saida and esperado not in saida
    marca = '✓' if pegou else ('⛔ MORREU DE ERRO, não pela regra' if quebrou_feio
                               else '⛔ PASSOU')
    print(f'  {marca:4} {amb:13} {nome}')
    if not pegou:
        print(f'       esperava "{esperado}" na saída · rc={r.returncode}')
        # ⭐ mostra TODAS as falhas, não só a última: foi olhar só a última
        #   que me fez procurar o bug no lugar errado
        for ln in saida.strip().splitlines():
            if '⛔' in ln or 'Error' in ln: print('       ' + ln.strip()[:96])
    ok += pegou
for n, txt in ORIG.items(): (P/f'{n}.py').write_text(txt)
print(f'\n  {ok}/{len(CASOS)} violações barradas')
sys.exit(0 if ok == len(CASOS) else 1)
