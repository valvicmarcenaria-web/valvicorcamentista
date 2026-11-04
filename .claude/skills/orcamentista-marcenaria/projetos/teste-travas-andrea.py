# ⭐ TESTE NEGATIVO v2 — a regra do nome INVERTEU [Jonathan 27/10], e o teste
#   inverte junto: antes eu provava que o nome DERRUBA o build; agora provo
#   que a AUSÊNCIA dele derruba. O que não inverteu continua testado.
"""ANDREA · ADITIVO — teste negativo das travas da folha  [27/10/2026]

⭐⭐ POR QUE ISTO EXISTE: uma trava que nunca falhou não está provada. Este
   arquivo injeta cada violação numa cópia do build e confere que ele MORRE.

   ⛔ Já pegou um buraco de verdade: `assert PARCEIRA in texto` passava
     sempre, porque é a própria variável que gera o texto. Trava que confere
     a fonte contra ela mesma não vale nada — hoje o nome vai por extenso
     dentro da trava, como segunda testemunha.

   ⭐ E o teste inverte junto com a regra: até 26/10 eu provava que o nome da
     parceira DERRUBAVA o build; desde 27/10 [Jonathan: "vamos deixar o
     posicionamento da paula explícito na proposta"] provo o contrário — a
     ausência dele é que derruba.

   uso:  python3 -I teste-travas-andrea.py .
"""
import pathlib, subprocess, sys, shutil, re
T = pathlib.Path(__file__).resolve().parent / '_tmp-travas'
T.mkdir(exist_ok=True)
P = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
src = (P/'build-andrea-aditivo.py').read_text(encoding='utf-8')
for nome in ('corte-andrea-aditivo.py','corte-andrea-subsidio.py','motor_mc.py'):
    shutil.copy(P/nome, T/nome)
# ⛔ as imagens também: sem elas o build morre de FileNotFoundError e o
#   teste — se for ingênuo — lê isso como "trava funcionou". Ver abaixo.
if not (T/'img-andrea').exists():
    (T/'img-andrea').symlink_to(P/'img-andrea', target_is_directory=True)

ALVO = "'Camada contínua e <b>sem poro</b>, que cobre a face inteira da peça.'),"
LAMENTO_DE = """'acima do previsto no orçamento contratado, e lamento o transtorno '
        'que esta adequação representa. Por isso optei por <b>assumir '"""
LAMENTO_PARA = """'acima do previsto no orçamento contratado. Por isso optei por <b>assumir '"""
VALOR_DE = """'integralmente a diferença de custo do material, no valor de '
        f'{rs(SUBSIDIO)}</b>, concedida"""
VALOR_PARA = """'integralmente a diferença de custo do material</b>, concedida"""

veneno = lambda t: (ALVO, repr(t) + '),')
CASOS = [
 ('[acusa] palavra ERRO',       veneno('Correção de um erro de especificação.')),
 ('[acusa] DIVERGÊNCIA',        veneno('O acabamento atual está em divergência.')),
 ('[acusa] "não atualizado"',   veneno('O projeto não foi atualizado a tempo.')),
 ('[acusa] INADEQUADO',         veneno('O material atual é inadequado.')),
 ('[promete] SEM LUCRO',        veneno('Praticado apenas o custo, sem lucro.')),
 ('[expõe] METRAGEM',           veneno('Cobertura total de 15 m² de face.')),
 ('[some] o nome da parceira',  ("PARCEIRA = 'Paula Galante'",
                                 "PARCEIRA = 'A responsável'")),
 ('[some] o papel dela',        ("PAPEL    = 'Responsável pelo projeto de interiores'",
                                 "PAPEL    = ''")),
 ('[some] o VALOR que ela assume', (VALOR_DE, VALOR_PARA)),
 ('[some] o LAMENTO',           (LAMENTO_DE, LAMENTO_PARA)),
 ('[some] o valor LÍQUIDO',     ('<div class="big">{rs(LIQUIDO)}</div>',
                                 '<div class="big">sob consulta</div>')),
]
ok = 0
for rot, (de, para) in CASOS:
    if de not in src:
        print(f'  ⛔ TESTE INVÁLIDO  {rot} — a injeção não encontrou o alvo'); continue
    (T/'b.py').write_text(src.replace(de, para, 1), encoding='utf-8')
    r = subprocess.run([sys.executable, '-I', str(T/'b.py')], capture_output=True,
                       text=True, cwd=T)
    # ⛔⛔ NÃO BASTA MORRER: tem de morrer PELA TRAVA CERTA. Um build que
    #   quebra por falta de arquivo também "morre", e um teste ingênuo lê
    #   isso como sucesso — foi o que quase aconteceu aqui. Só conta a morte
    #   por AssertionError, e qualquer outra falha é denunciada em voz alta.
    m = re.findall(r'AssertionError: (.+)', r.stderr.replace('\n', ' '))
    if r.returncode == 0:
        print(f'  ⛔ PASSOU BATIDO    {rot:<32}a folha saiu com a violação dentro')
    elif not m:
        outro = [l for l in r.stderr.strip().splitlines() if l.strip()][-1:]
        print(f'  ⛔ TESTE INVÁLIDO   {rot:<32}morreu por outro motivo: '
              f'{(outro[0] if outro else "?")[:44]}')
    else:
        print(f'  ✓  {rot:<32}{m[-1][:48]}'); ok += 1
print(f'\n  {ok}/{len(CASOS)} violações barradas pelo build')
sys.exit(0 if ok == len(CASOS) else 1)
