# -*- coding: utf-8 -*-
"""CHARBEL CHELALA — ⭐ O QUE AINDA PODE MOVER ESTE PREÇO, e quanto.

⛔⛔ UM ORÇAMENTO COM PREMISSA NÃO MEDIDA É UM ORÇAMENTO QUE MENTE DUAS
  VEZES: diz um número que não tem, e esconde que não tem. Este arquivo
  recalcula o projeto inteiro mexendo numa premissa de cada vez, e o que
  sai é quanto vale cada pergunta que ainda está aberta.

⭐ É assim que a dúvida vira pauta: não "falta cotar o MDF", e sim "a
  cotação do MDF vale R$ 23 mil".
"""
import subprocess, sys, os, re, shutil

AQUI = os.path.dirname(os.path.abspath(__file__))

#   ⛔⛔ E ESTE ARQUIVO JÁ MENTIU UMA VEZ, POR UM MOTIVO QUE NÃO DÁ ERRO.
#     O `__pycache__` decide se o bytecode vale comparando MTIME E TAMANHO
#     do fonte. `MC = 0.43` → `MC = 0.40` tem o MESMO COMPRIMENTO, e a troca
#     mais a volta acontecem dentro do mesmo segundo: o arquivo no disco
#     voltou ao certo e o Python continuou rodando o errado. A tabela saiu
#     com a mesa de cabeteira CUSTANDO MAIS por existir menos — que foi o
#     que denunciou. ⭐ Por isso toda medição aqui apaga o cache e roda com
#     -B: medir mexendo no fonte exige que nada lembre do fonte anterior.


def roda(env=None):
    e = dict(os.environ); e.update(env or {})
    e['PYTHONDONTWRITEBYTECODE'] = '1'
    shutil.rmtree(os.path.join(AQUI, '__pycache__'), ignore_errors=True)
    out = subprocess.run([sys.executable, '-B', 'levantamento.py'],
                         capture_output=True, text=True, env=e, cwd=AQUI)
    m = re.search(r'PREÇO · BLUM.*?R\$ ([\d.,]+)', out.stdout)
    assert m, out.stdout[-800:] + out.stderr[-800:]
    return float(m.group(1).replace('.', '').replace(',', '.'))


def patch(arquivo, velho, novo):
    """troca, mede e devolve o arquivo ao que era"""
    import io
    arquivo = os.path.join(AQUI, arquivo)
    t = io.open(arquivo, encoding='utf-8').read()
    assert t.count(velho) == 1, '⛔ ' + velho[:60]
    io.open(arquivo, 'w', encoding='utf-8').write(t.replace(velho, novo))
    try:
        return roda()
    finally:
        io.open(arquivo, 'w', encoding='utf-8').write(t)


def brl(v):
    s = ('R$ ' + f'{abs(v):,.2f}').replace(',', '§').replace('.', ',').replace('§', '.')
    return ('+' if v >= 0 else '−') + s


if __name__ == '__main__':
    p0 = roda()
    print('═' * 92)
    print('CHARBEL CHELALA · O QUE AINDA PODE MOVER O PREÇO')
    print('  preço de hoje, com as premissas de hoje:  R$ %s' %
          f'{p0:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.'))
    print('═' * 92)
    L = []

    L.append(('Os três MDF premium na linha "cor e acabamento especial" da Base '
              '(R$ 1.000 a chapa)', roda({'ESPECIAL': '1'}),
              'Caribe Dual Syncro, Fontana Magma e Cacao Matt · ⭐ A MAIOR '
              'PERGUNTA ABERTA, e é uma ligação para o fornecedor'))

    L.append(('A porta de closet a R$ 2.000 a folha em vez de R$ 1.400',
              patch('base.py', 'PORTA_VIDRO_PERFIL = 1400.0',
                    'PORTA_VIDRO_PERFIL = 2000.0'),
              'são 9 folhas de 2,57 m de altura · o R$ 1.400 da Base é de '
              'porta de espelho de 2,10 m, e esta é mais alta e com vidro'))

    L.append(('Uma mesa de cabeceira em vez de duas',
              patch('levantamento.py', 'N_CABECEIRA = 2', 'N_CABECEIRA = 1'),
              '⚠ a folha 20 desenha UMA e a chama no singular · a cama tem '
              'dois lados'))

    L.append(('O forro da suíte com 12 m² em vez de 9',
              patch('levantamento.py', 'FORRO_SUITE_M2 = 9.0',
                    'FORRO_SUITE_M2 = 12.0'),
              '⛔ A FOLHA 19 NÃO COTA ESTE FORRO · 9 m² é leitura do '
              'mapa-chave, não medida'))

    L.append(('O rodapé em MDF melamínico, pela regra da casa, em vez de inox',
              patch('base.py', 'RODAPE_INOX_M = 85.0', 'RODAPE_INOX_M = 0.0'),
              '[Jonathan, 26/10/2026] "a prancha pede base metálica; nós '
              'fazemos em MDF" · a prancha pede inox h = 2 em cinco folhas'))

    MC_ROTULO = 'A MC a 40% em vez de 43%'
    L.append((MC_ROTULO,
              patch('base.py', 'MC = 0.43', 'MC = 0.40'),
              '⭐ não é premissa, é ESCOLHA — entra aqui só para dar a escala '
              'das outras'))

    L.sort(key=lambda x: -abs(x[1] - p0))
    for nome, pv, por in L:
        print('  %-66s %14s' % (nome[:66], brl(pv - p0)))
        print('      %s' % por)
    print('─' * 92)
    #   ⛔ a MC não entra nesta soma: ela é escolha, não dúvida.
    duvida = sum(abs(pv - p0) for n, pv, _ in L if n != MC_ROTULO)
    print('  ⭐ As cinco premissas em aberto valem %s do preço — e a maior '
          'delas é\n    uma ligação para o fornecedor de chapa.'
          % f'{duvida / p0:.0%}')
    print('═' * 92)
