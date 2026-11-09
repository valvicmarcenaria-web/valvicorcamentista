# -*- coding: utf-8 -*-
"""CHARBEL CHELALA — o mesmo projeto em cada degrau da escada da casa.

⭐⭐ A PERGUNTA DO JONATHAN [09/11/2026]: "quanto ficaria o projeto na
  linha Hettich?". A Base de Custos responde: a aba Ferragens abre uma
  ESCADA DE POSICIONAMENTO com quatro degraus, e o que muda de um para o
  outro são DUAS LINHAS — a dobradiça e a corrediça — mais o pulsador.

    Silver   Bigfer Slow Click R$  4  · telescópica  R$  15  ·  2 anos
    Padrão   Bigfer Inox Click R$ 10  · Hardt P-10   R$  80  ·  5 anos
    Gold     Hettich Novisys   R$ 20  · Quadro V6    R$ 150  · 10 anos
      ou     Hettich Sensys    R$ 50  · Quadro V6    R$ 150  · 10 anos
    Blum     Blum              R$ 50  · Movento      R$ 300  · 30 anos

⛔ O QUE NÃO MUDA DE DEGRAU, e é a maior parte da conta: a dobradiça de
  porta de VIDRO (R$ 70 — porta de alumínio, é do vidraceiro), o sistema
  de correr SI Ocean 80 da SIFORMA (R$ 900), o desempenador, o botton, o
  cabideiro, a fonte de LED, a alma de aço e o puxador botão. Nenhum
  deles é Blum. ⚠ Trocar de linha mexe em TRÊS linhas de um orçamento de
  R$ 123 mil de custo direto: 104 dobradiças, 27 corrediças, 1 pulsador.

⛔⛔ E O QUE MUDA DE VERDADE É A GARANTIA. A regra da casa [Jonathan,
  29/10/2026] diz que vale o TIER MAIS BAIXO presente no projeto. Sair do
  Blum derruba a proposta inteira de 30 anos para 10 — e a folha 11,
  "a ferragem é a única parte do móvel que trabalha todo dia", foi
  escrita em cima dos 30.

⭐ POR QUE EM SUBPROCESSO, e não trocando a constante em memória:
  levantamento.py carrega base.py como um módulo PRÓPRIO, por
  spec_from_file_location, e o preço unitário entra em `it.fer` na hora
  em que o item é criado. Mexer em `base.DOBRADICA` depois disso não
  muda nada — e não mudar nada, calado, é o pior resultado possível.
  Cada degrau roda num diretório só dele, com a sua base.py.
"""
import pathlib, re, shutil, subprocess, sys, tempfile

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import base as b                                      # noqa: E402
import levantamento as lv                             # noqa: E402

#            nome                     dobradiça  corrediça  pulsador  garantia
ESCADA = [('Silver · econômico',           4.0,     15.0,     70.0,  '2 anos'),
          ('Padrão · 70% dos casos',      10.0,     80.0,     70.0,  '5 anos'),
          ('Gold · Hettich Novisys',      20.0,    150.0,     70.0, '10 anos'),
          ('Gold · Hettich Sensys',       50.0,    150.0,     70.0, '10 anos'),
          ('Blum · a linha de topo',      50.0,    300.0,    100.0, '30 anos')]

SONDA = ('import sys, pathlib\n'
         'sys.path.insert(0, str(pathlib.Path(__file__).parent))\n'
         'import levantamento as lv\n'
         'T, _ = lv.por_ambiente()\n'
         'f = sum(q * u for it, _q in T["L"] for _n, q, u in it.fer)\n'
         'print("%.6f %.6f" % (T["direto"], f))\n')


def roda(dob, cor, pul):
    """custo direto e ferragem de marca, com esta dobradiça e esta corrediça"""
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        for n in ('base.py', 'levantamento.py'):
            shutil.copy(AQUI / n, d / n)
        t = (d / 'base.py').read_text(encoding='utf-8')
        for cte, v in (('DOBRADICA', dob), ('CORREDICA_PAR', cor), ('PULSADOR', pul)):
            t, n = re.subn(r'(?m)^%s = [\d.]+' % cte, '%s = %.1f' % (cte, v), t, count=1)
            if n != 1:
                raise SystemExit('⛔ não achei a constante %s em base.py' % cte)
        (d / 'base.py').write_text(t, encoding='utf-8')
        (d / '_sonda.py').write_text(SONDA, encoding='utf-8')
        r = subprocess.run([sys.executable, str(d / '_sonda.py')],
                           capture_output=True, text=True)
        if r.returncode:
            raise SystemExit('⛔ ' + r.stderr.strip()[-400:])
        return [float(x) for x in r.stdout.split()]


BASE = 1 - 0.239125              # o que sobra do preço para custo e margem
DIA = 4000.0                     # custo fixo da fábrica, por dia de calendário


def tabela(mc):
    """⭐ A MC aqui é a REALIZADA, a que vale no preço — não a alvo da
    planilha, que sai cinco pontos abaixo por causa do piso do "Médio"."""
    P = b.PRECO_FECHADO
    print('═' * 108)
    print('CHARBEL CHELALA · A ESCADA DE LINHAS A UMA MC DE %.0f%%' % (mc * 100))
    print('  nove ambientes, 38 itens, 496 peças · a marcenaria não muda, '
          'só a ferragem de movimento')
    print('═' * 108)
    print('  %-24s %13s %14s %14s %11s %10s %8s'
          % ('LINHA', 'CUSTO DIRETO', 'PREÇO', 'MARGEM', 'EMPATE',
             'vs 625 mil', 'GARANTIA'))
    print('─' * 108)
    for nome, dob, cor, pul, gar in ESCADA:
        c, _f = roda(dob, cor, pul)
        preco = c / (BASE - mc)
        marg = preco * mc
        print('  %-24s %13s %14s %14s %8.0f d %10s %8s'
              % (nome, lv.brl(c), lv.brl(preco), lv.brl(marg), marg / DIA,
                 lv.brl(preco - P).replace('R$ ', ''), gar))
    print('─' * 108)
    print('  ⭐ PREÇO = custo direto ÷ (base de 76,09%% − MC de %.0f%%).' % (mc * 100))
    print('  ⭐ EMPATE = quantos DIAS DE FÁBRICA a margem paga, a R$ 4.000 o dia.')
    print('     ⛔ a entrega prometida ao Charbel é de 120 dias corridos.')
    print('  ⭐ vs 625 mil = a diferença contra o preço JÁ FECHADO com ele.')
    print('═' * 108)


if __name__ == '__main__':
    alvo = [float(x) / 100 for x in sys.argv[1:]] or [0.57]
    for mc in alvo:
        tabela(mc)
        print()
