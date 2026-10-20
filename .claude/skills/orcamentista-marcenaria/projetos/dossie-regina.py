# -*- coding: utf-8 -*-
"""Gera `2026-regina-home-office.md` a partir do motor. Nada à mão."""
import importlib.util, pathlib, sys, io, contextlib
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('rg', P/'corte-regina-home-office.py')
rg = importlib.util.module_from_spec(spec); sys.modules['rg'] = rg
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(rg)
br = rg.br
DESC = {
 'Mesa': '2,30 × 0,80 × 0,75, tampo com espessura visual de 5 cm, apoiado no '
         'gaveteiro e numa lateral',
 'Gaveteiro': 'três gavetas pequenas e uma gaveta arquivo, corrediça oculta, '
              'puxador cava',
 'Móvel do PC': 'nicho acoplado sob o tampo para o computador',
 'Painel': '2,30 × 1,05, espessura visual de 5 cm, com os recortes das tomadas',
 'Prateleira': '2,30 × 0,25, espessura visual de 5 cm, sobre suporte oculto',
}
assert set(DESC) == set(rg.MOVEIS), f'⛔ {set(DESC) ^ set(rg.MOVEIS)}'
L = []; w = L.append
w('# REGINA — home office\n')
w('Briefing por **WhatsApp**, com uma imagem de referência (20/10/2026).\n')
w('> mesa 2,30 comprimento · 0,80 largura · 0,75 altura')
w('> 3 gavetas pequena e uma gaveta arquivo')
w('> móvel para acoplar o PC (compoutador)')
w('> painel no fundo com previsão de tomadas elétricas')
w('> prateleira para finalizar o painel')
w('> painel de 230 × 105 cm e prateleira de 230 × 25 cm, com **espessura')
w('> visual de 5 cm**\n')
w('⭐ [Jonathan 20/10] **"MDF melamínico, corrediça oculta da rede, sem RT e')
w('uma margem de contribuição de 35%."**\n')
w(f'MC **{rg.MC_ALVO:.0%}** · **sem RT** · base **{rg.BASE*100:.2f}%**\n')
w('---\n')
w('## ⛔⛔ "Espessura visual de 5 cm" não é peça de 5 cm\n')
w('**MDF não existe em 50 mm**, e colar três chapas para chegar lá seria')
w('jogar dinheiro fora. A peça é uma **caixa**: face em 18 mm e **testeira')
w('de 5 cm** nas bordas que aparecem, com sarrafo de alma por dentro. O')
w('cliente vê 5 cm; a peça pesa o que pesa uma de 18.\n')
_vis = sum(c*l*q/1e4 for mv, esp, d, c, l, q, cor, fc in rg.PCS
           if d.startswith('Testeira'))
_tres = sum(c*l*q/1e4 for mv, esp, d, c, l, q, cor, fc in rg.PCS
            if d == 'Face')*2
w(f'São **{_vis:.2f} m² de testeira** — e é isso que se vê. Pela leitura')
w(f'literal seriam **mais {_tres:.2f} m² de MDF de cor**, cerca de')
w(f'**R$ {br(-(-_tres/(rg.CH_M2*rg.APROV)//1)*rg.COR[18])} só de chapa**, antes de fita e de mão de obra.\n')
w('---\n')
w('## O que cabe na chapa\n')
w('A chapa é **2,75 × 1,85** e as três peças grandes têm 2,30 de')
w('comprimento: mesa, painel e prateleira. **Todas cabem inteiras, sem')
w('emenda.**\n')
w('| cor · espessura | área m² | chapas | R$ |')
w('|---|--:|--:|--:|')
for k in sorted(rg.area, key=lambda k: (k[0], k[1])):
    w(f'| {k[0]} · {k[1]} mm | {rg.area[k]:.2f} | {rg.chapas[k]:.0f} '
      f'| {br(rg.custo_ch[k])} |')
w(f'| **total** | **{sum(rg.area.values()):.2f}** '
  f'| **{sum(rg.chapas.values()):.0f}** | **{br(sum(rg.custo_ch.values()))}** |\n')
w(f'⚠ A **sobra** comprada e não usada é **R$ {br(rg.sobra)}** — '
  f'{rg.sobra/sum(rg.custo_ch.values()):.0%} da chapa. O painel de 2,30 ×')
w('1,05 come metade de uma folha e deixa um **L** que não serve para outra')
w('peça de 2,30. É o preço de um móvel comprido num ambiente pequeno.\n')
w('---\n')
w('## Móvel a móvel\n')
w('| móvel | | custo | **preço** |')
w('|---|---|--:|--:|')
for mv in rg.MOVEIS:
    w(f'| **{mv}** | {DESC[mv]} | {br(rg.CD[mv])} | **{br(rg.PV[mv])}** |')
w(f'| | **custo direto** | **{br(rg.CD_TOT)}** | |')
w(f'| | **INVESTIMENTO** | | **R$ {br(rg.TOTAL)}** |\n')
w('---\n')
w('## ★ Em aberto\n')
w('1. ⚠ **A cor não veio.** A imagem é amadeirada; orçei **MDF melamínico de')
w(f'   cor** (R$ {br(rg.COR[18])} a chapa de 18) com caixaria em Branco TX. Amadeirado')
w('   de linha especial muda o preço — confirmar o padrão.')
_t = [(c, l, q) for mv, esp, d, c, l, q, cor, fc in rg.PCS
      if mv == 'Mesa' and d.startswith('Testeira')]
_dcd = (sum(c*l*q/1e4*rg.taxa[('Cor', 18)] for c, l, q in _t)
        + sum(2*(c+l)*q/100*0.4*rg.FITA_COR for c, l, q in _t))*1.06*(1+rg.M.EMBALAGEM)
_dpv = round(_dcd/(rg.BASE - rg.MC_ALVO)/10)*10
w('2. ⚠ **A espessura da mesa não veio.** A cliente deu os 5 cm visuais para')
w('   o **painel** e a **prateleira**. Adotei o mesmo no tampo da mesa, que é')
w(f'   o que a imagem mostra. Com tampo liso de 18 mm a mesa cairia')
w(f'   **R$ {br(_dpv)}**, de R$ {br(rg.PV["Mesa"])} para R$ {br(rg.PV["Mesa"]-_dpv)}.')
w('3. ⚠ **"Previsão de tomadas elétricas":** os **recortes** no painel são')
w('   nossos; a **tomada, o ponto e o circuito** são da elétrica. Se a')
w('   cliente quiser **caixa de tomada embutida** na marcenaria, é item à')
w('   parte (a base da casa traz R$ 260).')
w('4. ⚠ **Como a mesa se apoia.** Orçei com o **gaveteiro de um lado e uma')
w('   lateral do outro**, amarrados por travessa. Se a cliente quiser a mesa')
w('   **flutuando na parede**, entra estrutura metálica e o preço muda.')
w(f'5. ★ **"Corrediça oculta da rede"** — orçada a **R$ {br(rg.CORR_OC)} o par**, a')
w('   oculta de distribuição nacional. A Hettich sai a R$ 190.')
w('   ⚠ Garantia da oculta na casa: **5 anos** (a telescópica dá 2).')
w('6. ⚠ **O áudio de 6 segundos** que veio depois do briefing não foi')
w('   transcrito para mim, e **a mensagem seguinte foi apagada**. Se houver')
w('   escopo ali, não está neste preço.')
w('7. ⛔ **Medir no local antes de cortar.** As três peças de 2,30 cabem')
w('   inteiras na chapa, mas só se a parede confirmar os 2,30.\n')
(P/'2026-regina-home-office.md').write_text('\n'.join(L), encoding='utf-8')
print(f'2026-regina-home-office.md · R$ {br(rg.TOTAL)}')
