# -*- coding: utf-8 -*-
"""Phillip e Giselle · CUSTO DE MATERIAL por ambiente, nas três linhas.
⛔ Sem preço final [Jonathan, 04/11/2026]: só o custo direto levantado."""
import importlib, sys, os, subprocess, json
# ⭐ [Jonathan, 04/11/2026] "não precisa ter os banheiros": a03 e a07 saem
#   (os arquivos ficam no repositório) e o banho do Mateus sai do a08.
#   ⛔ [Jonathan, 06/11/2026] "tire todos os itens do QUARTO DO MATEUS": o
#     a05 sai (o arquivo fica no repositório). O CLOSET do Mateus fica.
#   ⭐ e VOLTOU, só com o painel da porta oculta [Jonathan, 06/11/2026]
AMBS = ['a01_quarto_casal', 'a02_closet_casal', 'a04_rouparia',
        'a05_quarto_mateus', 'a06_quarto_ana',
        'a08_closet_banho_mateus', 'a09_closet_ana', 'a10_circulacao']
# ⭐ SERVIÇO AVULSO — valor de VENDA fixo, fora do custo direto e da MC.
AVULSO = [('Usinagem do painel existente da sala do térreo, para tentar recuperar '
           'o rodapé com perfil de aço inox escovado', 1900.0,
           'sem garantia de efetividade')]
FRETE = 5 * 200.0     # ⭐ revisão 04/11: ~20 chapas por viagem (régua do Gustavo)
if os.environ.get('LINHA') and __name__ == '__main__':
    import motor as M
    for a in AMBS: importlib.import_module(a)
    R = M.calcula(FRETE)
    R['amb'] = M.custo_por_ambiente(R)
    cm, fm = M.custo_por_movel(R)
    R['movel'] = {f'{a}||{m}': v for (a, m), v in cm.items()}
    R['mov'] = {f'{a}||{m}': v for (a, m), v in fm.items()}
    print(json.dumps({k: v for k, v in R.items() if k not in ('area', 'fita')}))
elif __name__ == '__main__':
    import motor as M
    out = {}
    for L in ('telescopica', 'hettich', 'blum'):
        r = subprocess.run([sys.executable, __file__], env=dict(os.environ, LINHA=L),
                           capture_output=True, text=True, check=True)
        out[L] = json.loads(r.stdout)
    t = out['hettich']
    print(f"{'Ambiente':26s}{'Telescópica':>15s}{'Hettich':>15s}{'Blum':>15s}")
    for a in t['amb']:
        print(f"{a:26s}" + ''.join(f"{M.brl(out[L]['amb'][a]):>15s}" for L in out))
    for k, lab in (('chapa', 'Chapas MDF'), ('fita_r', 'Fita + filetagem'),
                   ('outras', 'Ferragem, LED, sistemas, terceir.'), ('corte', 'Corte'),
                   ('consum', 'Consumíveis 6%'), ('frete', 'Frete'), ('emb', 'Embalagem 2%'),
                   ('CD', 'CUSTO DIRETO')):
        print(f"{lab:26s}" + ''.join(f"{M.brl(out[L][k]):>15s}" for L in out))
    print('chapas:', sum(t['chapas'].values()), '· peças:', t['npecas'])
    for d, v, obs in AVULSO: print(f'AVULSO (venda) {M.brl(v)} · {d} · {obs}')
