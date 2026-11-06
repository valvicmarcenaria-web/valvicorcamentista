# -*- coding: utf-8 -*-
"""ATTOS · Costa Laguna — o PAINEL, no padrão da casa, GERADO.

⛔⛔ O QUE ESTAVA ERRADO, e por que isto existe [Jonathan, 04/11/2026]:
  "veja como é o layout das abas dos ambientes". As abas foram refeitas, e o
  Painel ficou apontando para o layout ANTIGO: a ferragem saía NEGATIVA
  (−R$ 62.019,73) e o custo direto saía R$ 0,00. Número negativo e número
  zerado lado a lado, numa planilha com cara de pronta.

⛔ E O BLOCO "A CHAPA DO PROJETO" NÃO EXISTE NO PADRÃO DA CASA. Ele era a
  minha invenção: ratear a chapa pelo PROJETO inteiro, 43 chapas, para que a
  sobra de um ambiente servisse o vizinho. O método da casa conta a chapa
  INTEIRA EM CADA ABA — 51 chapas, R$ 4.100 a mais — e a diferença vai para
  a linha "Arredondamento de chapa para número cheio" de cada aba.
  ⭐ A decisão de voltar atrás é do dono do método, não minha.

⭐ As colunas do Painel são as da casa, e a última coluna de material é
  "VIDRO, FILET. E CONSUM." — nunca "CORTE E CONSUM.", que eu havia inventado.
"""
import json, sys, pathlib, importlib.util, contextlib, io

P = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location('pl', P / 'planilha.py')
pl = importlib.util.module_from_spec(_s); sys.modules['pl'] = pl
with contextlib.redirect_stdout(io.StringIO()): _s.loader.exec_module(pl)

#   ⭐ a prancha de onde cada ambiente saiu · é o que deixa conferir a leitura
PRANCHAS = {
    '01 Hall': 'hall-01 a 03',
    '02 Jantar': 'hall-01 a 03',
    '03 Cozinha': 'cozinha-01 · cozinha-painel-01 e 02',
    '04 Gourmet': 'cozinha-01',
    '05 Escritório': 'escritorio-01 e 02',
    '06 Sala de TV': 'sala-tv-01',
    '07 Suíte': 'suite-01 e 02',
    #   ⛔⛔ O ÚNICO AMBIENTE SEM PRANCHA. A cabeceira da suíte 01 entrou
    #     por REGRA DE PREÇO do Jonathan ("20 a menos que a cabeceira da
    #     suite de casal"), não por medida — e esta célula é o lugar onde
    #     isso fica à vista de quem lê o Painel.
    '08 Suíte 01': '⛔ NENHUMA · preço por regra',
}
#   as linhas do Painel que este arquivo escreve
R_TAB = 23          # cabeçalho da tabela de ambientes
R_SUB = 2           # a linha de dados do projeto
R_KPI = 7           # os cinco números do topo
R_DIN0 = 13         # cabeçalho de ONDE ESTÁ O DINHEIRO


def refs():
    """Os endereços de cada aba, lidos do GERADOR — nunca de cabeça.
       ⛔ Era daqui que vinha a ferragem negativa: eu tinha escrito à mão os
       números de linha do layout antigo."""
    out = []
    for amb, aba in pl.ABAS:
        G, L, blocos, cr, cc, cf = pl.monta(amb, aba)
        q = f"'{aba}'!"
        ch = sorted(cr.values())
        out.append(dict(
            aba=aba, itens=len(blocos),
            #   CHAPAS: a quantidade, em número cheio, somada por cor
            chapas='+'.join(f'{q}$D${r}' for r in ch),
            #   MDF: o custo das mesmas linhas
            mdf='+'.join(f'{q}$F${r}' for r in ch),
            #   FITA: só a fita de borda · a filetagem é serviço e vai adiante
            fita=f'{q}$F${L["acab0"]}',
            ferr=f'{q}$F${L["ferr"]}',
            frete=f'{q}$F${L["frete"]}',
            #   ⭐ VIDRO, FILETAGEM E CONSUMÍVEIS: tudo que fica ENTRE a fita e
            #     a ferragem (as filetagens e o vidro, quando há) mais tudo que
            #     fica entre a ferragem e o frete (os dois cortes, consumíveis
            #     e embalagem). Escrito por INTERVALO, a aba com vidro e a sem
            #     vidro usam a mesma fórmula.
            vfc=(f'SUM({q}$F${L["acab0"] + 1}:$F${L["ferr"] - 1})'
                 f'+SUM({q}$F${L["ferr"] + 1}:$F${L["cons"] + 1})'),
            direto=f'{q}$F${L["direto"]}',
            #   ⛔ a conferência de dentro da aba, em módulo
            conf=f'{q}$I${L["f0"] + 4}',
            #   ⛔ LINHA SEM PREÇO NA BASE: o PROCV devolve "" quando a chave
            #     não existe, e a linha custa zero sem reclamar.
            zero=(f'SUMPRODUCT(({q}$K${L["blk0"]}:$K${L["blk1"]}<>"")'
                  f'*({q}$K${L["blk0"]}:$K${L["blk1"]}<>"chave na Base")'
                  f'*({q}$H${L["blk0"]}:$H${L["blk1"]}=""))'),
        ))
    return out


def monta():
    X = refs()
    r0 = R_TAB
    linhas, G = {}, []

    def col(k, i):
        """A coluna k da tabela, na linha do ambiente i."""
        return f'{chr(ord("B") + i)}{r0 + 1 + k}'

    # ── a tabela de ambientes ───────────────────────────────────────────
    T = [['AMBIENTE', 'PRANCHAS', 'ITENS', 'CHAPAS', 'MDF', 'FITA',
          'FERRAGEM', 'FRETE', 'VIDRO, FILET. E CONSUM.', 'CUSTO DIRETO']]
    for i, x in enumerate(X):
        T.append([x['aba'], PRANCHAS[x['aba']], x['itens'],
                  f'={x["chapas"]}', f'={x["mdf"]}', f'={x["fita"]}',
                  f'={x["ferr"]}', f'={x["frete"]}', f'={x["vfc"]}',
                  f'={x["direto"]}'])
    a, z = r0 + 1, r0 + len(X)
    T.append(['TOTAL DO QUE ESTÁ LEVANTADO', '11 pranchas A3']
             + [f'=SUM({c}{a}:{c}{z})' for c in 'DEFGHIJK'])
    tot = r0 + len(X) + 1
    #   ⭐ as duas linhas da casa, depois do TOTAL
    T.append(['⭐ CONFERÊNCIA   ·   a soma das colunas de material tem de dar '
              'o CUSTO DIRETO, e a soma dos módulos das sete abas tem de dar '
              'zero', '', '', '', '', '', '', '', '',
              f'=F{tot}+G{tot}+H{tot}+I{tot}+J{tot}-K{tot}'])
    T.append(['⛔ LINHAS QUE SAEM ZERO   ·   item lançado sem preço na Base · '
              'enquanto isto não for zero, o custo direto é um PISO',
              '', '', '', '', '', '', '', '',
              '=' + '+'.join(x['zero'] for x in X)])
    linhas['tab'] = (r0, r0 + len(T) - 1)

    # ── ONDE ESTÁ O DINHEIRO · espelha as COLUNAS da tabela ─────────────
    D = [['LINHA', '', '', '', '', 'VALOR', '% DO CUSTO']]
    for nome, c in (('MDF — chapa, em número cheio e por cor · ⛔ contada '
                     'INTEIRA em CADA aba, que é a regra da casa', 'F'),
                    ('Fita de borda', 'G'),
                    ('Ferragem, terceirizados e iluminação', 'H'),
                    ('Frete do projeto · R$ 200 a viagem', 'I'),
                    ('Vidro, filetagem, corte, consumíveis e embalagem', 'J')):
        D.append([nome, '', '', '', '', f'={c}{tot}',
                  f'=IFERROR(G{R_DIN0 + len(D)}/$G${R_DIN0 + 6};"")'])
    D.append(['CUSTO DIRETO DO LEVANTADO', '', '', '', '', f'=K{tot}',
              f'=IFERROR(G{R_DIN0 + 6}/$G${R_DIN0 + 6};"")'])
    linhas['din'] = (R_DIN0, R_DIN0 + len(D) - 1)

    # ── os cinco números do topo ────────────────────────────────────────
    K = [[f'=D{tot}&" ambiente(s)"', '', f'=E{tot}&" itens de móvel"', '',
          f'=F{tot}&" chapas"', '', f'=K{tot}',
          '', "='Preço e Comissões'!$C$49"]]
    #   ⛔ a contagem de ambiente é a de LINHAS da tabela, não a da coluna D:
    #     D é ITENS. Corrige abaixo, com o número de abas.
    K[0][0] = f'="{len(X)} ambiente(s)"'
    K[0][2] = f'=D{tot}&" itens de móvel"'
    K[0][4] = f'=E{tot}&" chapas"'
    return T, D, K, linhas, tot


if __name__ == '__main__':
    T, D, K, L, tot = monta()
    #   ⛔⛔ O NÚMERO DO MOTOR MORA NA PAINEL!G37 E É DIGITADO À MÃO.
    #     Em 04/11/2026 ele envelheceu: dizia R$ 70.767,00 e o motor já
    #     estava em R$ 75.681,91, então a conferência acusava R$ 4.914,89
    #     de erro onde não havia erro nenhum. ⭐ Enquanto esta linha não
    #     for gerada, o print abaixo existe para que quem rodar o arquivo
    #     VEJA o número que precisa ir para lá.
    print(f'\n⛔ Painel!G37 (digitado à mão) tem de dizer: '
          f'=K31-I31-{round(pl.lv.custo()["direto"] * 100):d}/100')
    _n = f'{pl.lv.custo()["direto"]:,.2f}'.replace(',', '§') \
        .replace('.', ',').replace('§', '.')
    print(f'   e a frase do B37, "R$ {_n}"')
    print(f'tabela {L["tab"][0]}–{L["tab"][1]} · TOTAL na {tot}')
    for nome, M, r in (('tab', T, R_TAB), ('din', D, R_DIN0), ('kpi', K, R_KPI)):
        (P / f'_pn-{nome}.json').write_text(json.dumps(M, ensure_ascii=False))
        print(f'  {nome:<4} B{r}:K{r + len(M) - 1}  {len(M)} linhas')
