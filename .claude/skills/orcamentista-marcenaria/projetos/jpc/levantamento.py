# -*- coding: utf-8 -*-
"""APARTAMENTO JPC — o quantitativo dos dois banhos, peça a peça.

Fonte: pranchas PR 01 de Helena Antunes, junho de 2026. Duas folhas, dois
gabinetes suspensos. Tudo o que está aqui foi LIDO das pranchas; o que não
estava cotado está marcado com ⚠ e vai para a lista de dúvidas da proposta.

⛔⛔ A FRONTEIRA DO ESCOPO [regra 19 da casa, Jonathan 29/10/2026]:
  "pedra nao é escopo da marcenaria. espelhos, vidros e serralheria que
  estiverem na marcenaria é nosso." O teste é: sai no mesmo caminhão e é
  instalado pela mesma equipe? É nosso. Existe sem o móvel? Não é.

  · A BANCADA DE PEDRA dos dois banhos, com a cuba: FORA. Desenhada nas
    duas pranchas, hachurada como granito, e não é nossa. Não se lança nem
    a zero.
  · O ESPELHO dos dois banhos: FORA, e esta é a decisão que custou mais
    para tomar. Ele está desenhado, o CONTEÚDO da prancha diz MARCENARIA,
    e a regra manda incluir espelho "quando faz parte do móvel". Este não
    faz: está colado na parede acima da bancada, não encosta no gabinete e
    existe sem ele — como a pedra. ⚠ E não tem UMA cota em nenhuma das
    duas folhas: orçá-lo seria inventar a medida. Vai NOMEADO na proposta,
    que é o segundo dos dois únicos estados que a regra admite.
"""
import math, importlib.util, pathlib

_aqui = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location('jpc_base', _aqui / 'base.py')
b = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(b)

COR = 'MDF cor'


class Item:
    def __init__(self, nome, folha, obs=''):
        self.nome, self.folha, self.obs = nome, folha, obs
        self.pecas, self.terc, self.fer = [], [], []

    def p(self, nome, L, A, esp, qtd=1, fita=0.0, obs=''):
        self.pecas.append(dict(nome=nome, L=L, A=A, esp=esp, mat=COR,
                               qtd=qtd, fita=fita, obs=obs))
        return self

    def t(self, nome, q, unit, un='m'):
        if q: self.terc.append((nome, q, unit, un))
        return self

    def f(self, nome, q, unit):
        if q: self.fer.append((nome, q, unit))
        return self

    def caixa(self, L, A, P, div=0, prat=0, fundo=6, esp=15):
        n_lat = 2 + div
        self.p('Laterais e divisórias', P, A, esp, n_lat, A / 100)
        self.p('Tampo e base', L, P, esp, 2, L / 100)
        if fundo:
            self.p('Fundo', L, A, fundo, 1)
        if prat:
            larg = (L - n_lat * 1.5) / (div + 1)
            self.p('Prateleiras internas', larg, P - 2, esp, prat, larg / 100)
            self.f('Suporte de prateleira, jogo de 4', prat, b.SUPORTE_JOGO)
        #   ⭐ TRAVESSA DE FIXAÇÃO, e ela não está desenhada em lugar nenhum.
        #     Gabinete suspenso não se pendura no fundo de 6 mm: leva uma
        #     travessa de 18 mm aparafusada na parede, atrás do tampo. ⛔ A
        #     regra 1 da casa proíbe o sarrafo de pinus que fazia isso, e
        #     manda tirar a travessa da própria chapa.
        self.p('Travessa de fixação à parede', L, 10, 18, 1, L / 100,
               'móvel suspenso · regra 1 da casa, travessa de MDF')
        return self

    def porta(self, larg, alt, n, esp=18, cava=True):
        self.p(f'{n} × porta de abrir {larg:.2f} × {alt:.0f}'.replace('.', ','),
               larg, alt, esp, n, (larg + alt) * 2 / 100)
        self.f(b.DOBRADICA_NOME, n * b.dobradicas(alt), b.DOBRADICA)
        if cava:
            self.t('Puxador cava usinado', n * larg / 100, b.CAVA_M)
        return self

    def gaveta(self, larg, alt, prof, n, h_caixa, esp=18, cava=True):
        self.p(f'{n} × frente de gaveta {larg:.1f} × {alt:.0f}'.replace('.', ','),
               larg, alt, esp, n, (larg + alt) * 2 / 100)
        self.p(f'{n} × caixa de gaveta h = {h_caixa:.0f}',
               (larg + prof) * 2, h_caixa, 15, n, (larg + prof) * 2 / 100)
        self.p(f'{n} × fundo de gaveta', larg, prof, 6, n)
        self.f(b.CORREDICA_NOME, n, b.CORREDICA_PAR)
        if cava:
            self.t('Puxador cava usinado', n * larg / 100, b.CAVA_M)
        return self


M = []
def novo(nome, folha, obs=''):
    it = Item(nome, folha, obs); M.append(it); return it


# ════════════════════════════════════════════════════════════════════════
# 01 · BANHO SUÍTE — prancha PR 01
# ════════════════════════════════════════════════════════════════════════
#   Planta: bancada de pedra 69,5 × 55 com cuba oval (FORA do escopo).
#   Elevação: gabinete 67,5 de largura × 63 de altura, duas portas de 33,75.
#   Vista lateral: 49,5 de profundidade, suspenso 20 cm do piso.
it = novo('Banho Suíte · gabinete suspenso sob bancada', 'PR 01',
          '67,5 × 63 × 49,5 · suspenso 20 cm do piso')
it.caixa(L=67.5, A=63, P=49.5, div=1, prat=2)
it.porta(larg=33.75, alt=63, n=2)

#   ⭐⭐ O NICHO DO PAPEL HIGIÊNICO É MARCENARIA, e é o único detalhe
#     escrito à mão nas duas pranchas: "Porta papel higiênico recuado na
#     marcenaria (profundidade 15 cm)". A vista lateral cota a boca em
#     25 × 18. Ele é um caixote de cinco peças embutido na lateral DIREITA
#     do gabinete, abrindo para o lado do vaso — come 15 cm do compartimento
#     da direita e é por isso que a prateleira de lá morre no nicho.
it.p('Nicho · fundo', 25, 18, 15, 1, (25 + 18) * 2 / 100,
     'fita na boca do nicho · 25 × 18 vazado na lateral direita')
it.p('Nicho · topo e base', 25, 15, 15, 2, 0.25)
it.p('Nicho · costados', 15, 18, 15, 2, 0.18)

# ════════════════════════════════════════════════════════════════════════
# 02 · BANHO SOCIAL — prancha PR 01
# ════════════════════════════════════════════════════════════════════════
#   Planta: bancada de pedra 90,5 × 50,5 com cuba oval (FORA do escopo).
#   Elevação: gabinete 88,5 × 63, três colunas iguais de 29,5 — duas portas
#   inteiras e uma torre de três gavetas, 15 + 15 + 33 de cima para baixo.
#   ⚠ A PROFUNDIDADE NÃO ESTÁ COTADA: não há vista lateral nesta folha.
#     Adoto 45, que é a bancada de 50,5 menos o mesmo recuo de 5,5 que a
#     suíte tem (bancada 55 → gabinete 49,5). A largura confirma a leitura:
#     lá a bancada é 69,5 e o gabinete 67,5; aqui 90,5 e 88,5 — os mesmos
#     2 cm. A arquiteta é coerente, e é nela que me apoio. Vai como dúvida
#     na proposta, para conferir na medição.
it = novo('Banho Social · gabinete suspenso sob bancada', 'PR 01',
          '88,5 × 63 × 45 · suspenso · 2 portas e 3 gavetas')
it.caixa(L=88.5, A=63, P=45, div=2, prat=0)
it.porta(larg=29.5, alt=63, n=2)
#   ⚠ A PRANCHA NÃO DESENHA PRATELEIRA NENHUMA NESTE GABINETE, e a suíte
#     desenha. Não é esquecimento meu: a coluna da esquerda fica sob a cuba
#     e o sifão ocupa o vão. Sigo o desenho e escrevo a oferta na proposta —
#     prateleira interna é ajuste de centavos na conferência de medidas.
it.gaveta(larg=29.5, alt=15, prof=40, n=2, h_caixa=13)
it.gaveta(larg=29.5, alt=33, prof=40, n=1, h_caixa=20)


# ════════════════════════════════════════════════════════════════════════
# O CUSTO
# ════════════════════════════════════════════════════════════════════════
def _levanta(it):
    area, fita, pecas = {}, 0.0, 0
    for p in it.pecas:
        k = (p['mat'], p['esp'])
        area[k] = area.get(k, 0.0) + p['L'] * p['A'] / 10000 * p['qtd']
        pecas += p['qtd']
        fita += p['fita'] * p['qtd']
    return dict(area=area, fita=fita, pecas=pecas,
                c_terc=sum(q * u for _n, q, u, _un in it.terc),
                c_fer=sum(q * u for _n, q, u in it.fer))


def custo(itens, arredonda=True):
    """⭐⭐ O ARREDONDAMENTO DE CHAPA É DO PROJETO, NÃO DO ITEM.
    A sobra do arredondamento é RATEADA pela área, que é o que a causa.
    Assim a soma dos itens É o custo do projeto, por construção."""
    L = [(it, _levanta(it)) for it in itens]
    area = {}
    for _it, q in L:
        for k, a in q['area'].items():
            area[k] = area.get(k, 0.0) + a
    rend = b.CHAPA_M2 * b.APROV
    #   ⭐ `arredonda=False` paga a chapa FRACIONÁRIA — não é como a casa
    #     compra, é a pergunta "quanto deste custo é sobra que fica no
    #     galpão e vai ser usada no próximo job?". Ver `cenarios.py`.
    chapas = {k: (math.ceil(a / rend) if arredonda else a / rend)
              for k, a in area.items()}
    preco = {k: b.PRECO[f'{k[0]} {k[1]}'] for k in area}
    c_chapa = sum(n * preco[k] for k, n in chapas.items())
    sobra = {k: chapas[k] * preco[k] - area[k] / rend * preco[k] for k in area}
    n_chapas, n_pecas = sum(chapas.values()), sum(q['pecas'] for _i, q in L)

    def _item(q):
        ch = sum(a / rend * preco[k] + sobra[k] * (a / area[k])
                 for k, a in q['area'].items())
        corte = (n_chapas * b.CORTE_CHAPA * (q['pecas'] / n_pecas)
                 + q['pecas'] * b.CORTE_PECA)
        fita = q['fita'] * b.FITA_COR * b.FITA_PERDA
        #   ⛔ A BASE DA EMBALAGEM É A MESMA DO CONSUMÍVEL MAIS TUDO O MAIS.
        #     No Charbel esta linha divergiu da soma da seção e a aba não
        #     fechava por R$ 455. Aqui ela está escrita uma vez só.
        cons = (ch + fita) * b.CONSUMIVEIS
        return (ch + fita + corte + cons + q['c_terc'] + q['c_fer']) * (1 + b.EMBALAGEM)

    c_fita = sum(q['fita'] for _i, q in L) * b.FITA_COR * b.FITA_PERDA
    diretos = [_item(q) for _it, q in L]
    #   ⭐ O FRETE É DO JOB e tem de cair DENTRO dos itens, senão a soma dos
    #     itens deixa de ser o custo do projeto. Rateio pelo custo direto.
    c_frete = b.VIAGENS * b.FRETE_VIAGEM
    soma = sum(diretos)
    diretos = [d + c_frete * (d / soma) for d in diretos]
    return dict(area=area, chapas=chapas, preco=preco, c_chapa=c_chapa,
                pecas=n_pecas, n_chapas=n_chapas,
                fita=sum(q['fita'] for _i, q in L), c_fita=c_fita,
                c_corte=n_chapas * b.CORTE_CHAPA + n_pecas * b.CORTE_PECA,
                c_cons=(c_chapa + c_fita) * b.CONSUMIVEIS,
                c_terc=sum(q['c_terc'] for _i, q in L),
                c_fer=sum(q['c_fer'] for _i, q in L),
                c_frete=c_frete, diretos=diretos, direto=sum(diretos), L=L)


def brl(v):
    return 'R$ ' + f'{v:,.2f}'.replace(',', '§').replace('.', ',').replace('§', '.')


T = custo(M)
DIRETO = T['direto']
#   ⭐⭐ A MC É LIDA DO PREÇO, não escolhida: MC = BASE − custo ÷ preço.
MC = b.BASE - DIRETO / b.PRECO_FECHADO
PRECO = DIRETO / (b.BASE - MC)
assert abs(PRECO - b.PRECO_FECHADO) < 0.01, PRECO

#   ⭐ O RATEIO DOS R$ 6.700 entre os dois banhos é pelo custo direto, e o
#     último item absorve o centavo do arredondamento — para que a soma da
#     tabela da proposta seja o preço fechado, e não "quase".
_brutos = [d / DIRETO * b.PRECO_FECHADO for d in T['diretos']]
RATEIO = [round(v, 2) for v in _brutos[:-1]]
RATEIO.append(round(b.PRECO_FECHADO - sum(RATEIO), 2))
assert abs(sum(RATEIO) - b.PRECO_FECHADO) < 1e-9, RATEIO


if __name__ == '__main__':
    print(f'\n  APARTAMENTO JPC · dois banhos · linha {b.LINHA}\n')
    for (it, q), d, pv in zip(T['L'], T['diretos'], RATEIO):
        print(f'  {it.nome}')
        print(f'     {it.obs}')
        for p in it.pecas:
            m = f"{p['qtd']} × {p['L']:.1f} × {p['A']:.1f} × {p['esp']}"
            print(f'       {p["nome"]:<42}{m:>22}')
        for n, qt, u in it.fer:
            print(f'       {n:<42}{qt:>6} × {brl(u):>12}')
        for n, qt, u, un in it.terc:
            print(f'       {n:<42}{qt:>6.2f} {un} × {brl(u):>9}')
        print(f'       {"custo direto (já com frete rateado)":<42}{brl(d):>22}')
        print(f'       {"preço de venda no rateio":<42}{brl(pv):>22}\n')

    print('  ── o custo do projeto ' + '─' * 44)
    for k, n in sorted(T['chapas'].items()):
        print(f'     {k[0]} {k[1]} mm · {T["area"][k]:6.2f} m²'
              f'{n:>4} chapa(s) × {brl(T["preco"][k]):>12}'
              f'{brl(n * T["preco"][k]):>14}')
    for rot, v in [('Fita de borda · %.2f m' % T['fita'], T['c_fita']),
                   ('Corte · %d chapas, %d peças' % (T['n_chapas'], T['pecas']),
                    T['c_corte']),
                   ('Consumíveis · 6%', T['c_cons']),
                   ('Ferragem Hettich', T['c_fer']),
                   ('Usinagem de cava', T['c_terc']),
                   ('Frete · %d viagens' % b.VIAGENS, T['c_frete'])]:
        print(f'     {rot:<44}{brl(v):>26}')
    _emb = DIRETO - T['c_frete'] - (T['c_chapa'] + T['c_fita'] + T['c_corte']
                                    + T['c_cons'] + T['c_fer'] + T['c_terc'])
    print(f'     {"Embalagem · 2%":<44}{brl(_emb):>26}')
    print(f'     {"CUSTO DIRETO":<44}{brl(DIRETO):>26}')
    print('\n  ── o fechamento ' + '─' * 50)
    print(f'     {"BASE da cascata (RT 10%, sem vendedor)":<44}'
          f'{b.BASE*100:>24.4f}%')
    print(f'     {"MC LIDA do preço":<44}{MC*100:>24.4f}%')
    print(f'     {"PREÇO":<44}{brl(PRECO):>26}')
    print(f'     {"margem de contribuição":<44}'
          f'{brl(b.PRECO_FECHADO * b.BASE - DIRETO):>26}')
