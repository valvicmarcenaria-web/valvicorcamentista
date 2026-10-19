# -*- coding: utf-8 -*-
"""Regera as seções do painel, da RT e do investimento em
   `2026-sandra-duarte-rack.md` a partir do motor.

⛔ Virou arquivo pelo mesmo motivo do dossiê da Michelle: na primeira vez eu
  montei estas tabelas por script solto, e à primeira mudança de preço os
  números do .md teriam ficado para trás sem ninguém ver. O resto do dossiê
  é escrito à mão; só o trecho entre os dois marcadores é gerado.
"""
import importlib.util, pathlib, sys, io, contextlib
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('sr', P/'corte-sandra-rack.py')
sr = importlib.util.module_from_spec(spec); sys.modules['sr'] = sr
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(sr)
br, PP = sr.br, sr.PP

INI = '## ⭐ Painel de TV — item à parte'
FIM = '## ★ Em aberto'
p = P/'2026-sandra-duarte-rack.md'
s = p.read_text(encoding='utf-8')
assert s.count(INI) == 1 and s.count(FIM) == 1, '⛔ OS MARCADORES DO DOSSIÊ SUMIRAM'

novo = f'''{INI}  [Jonathan 16/10 · liso com frisos 19/10]

> *"adicione com um valor à parte um painel de TV liso de 142 cm de
> largura, apoiado no rodapé (a se validar a possibilidade de ser inteiro).
> Investimento — 2.300"*
>
> ⭐ 19/10: *"vamos atualizar o painel para ripado com ripas de 2×2 e o
> valor para R$ 7.500"*
>
> ⭐ 19/10, depois: *"vamos **voltar com o painel liso**, dessa vez
> acrescentando **dois frisos com perfil laqueado**"* — e, na sequência,
> *"pode atualizar o painel para **3.900**"*

⛔ **O preço é dele, não meu.** Abaixo eu só confiro.

| | R$ |
|---|--:|
| chapa · uma Metalic de pé | {br(PP['chapa_base'])} |
| fita · bordas do painel | {br(PP['fita_base'])} |
| ⭐ **dois frisos em perfil laqueado** | **{br(PP['friso'])}** |
| estrutura de fixação | {br(PP['fixa'])} |
| consumíveis · 6% | {br(PP['cons'])} |
| embalagem · 2% | {br(PP['emb'])} |
| **custo direto** | **{br(sr.CD_PAINEL)}** |
| ⭐ **RT do projeto inteiro** | **{br(sr.RT_TOTAL)}** |
| **a cobrir, no painel** | **{br(sr.CD_PAINEL + sr.RT_TOTAL)}** |
| **PREÇO** ⭐ dele | **R$ {br(sr.PAINEL_PV)}** |
| **MC que sobra no painel** | **{sr.MC_PAINEL*100:.1f}%** |

Os **frisos são {PP['friso']/sr.CD_PAINEL*100:.0f}% do custo direto do painel**: de R$ {br(sr.CD_SEM_FRISO)} sem
eles para R$ {br(sr.CD_PAINEL)} com eles.

★ O **perfil laqueado** está estimado em **R$ {br(sr.PERFIL_LAQ)}/m** — perfil, usinagem do
rasgo e laca. **Não está na base da casa**; vale cotar.

---

## ⭐⭐ A RT do projeto inteiro, alocada só no painel  [Jonathan 19/10]

> *"adicione também a RT do projeto completo, mas a RT precisa estar
> **alocada apenas no custo do painel**."*

A RT devida à arquiteta é **{sr.RT_RATE:.1%} do preço de venda** — 10% sobre o líquido, e
o líquido é o bruto menos a nota. Sobre o total de R$ {br(sr.TOTAL)}, dá
**R$ {br(sr.RT_TOTAL)}**.

⛔ **Isso não muda o que a arquiteta recebe.** Muda de onde o dinheiro sai:
o **rack passa a ser precificado sem RT na cascata** (base {sr.BASE*100:.2f}%) e o
**painel paga a conta dos dois**.

| | MC | R$ |
|---|--:|--:|
| Rack · MC alvo | {sr.MC_ALVO*100:.1f}% | {br(sr.PV)} |
| **Painel · MC que sobra** | **{sr.MC_PAINEL*100:.1f}%** | {br(sr.PAINEL_PV)} |
| **Conjunto** | **{sr.MC_CONJ*100:.1f}%** | **{br(sr.TOTAL)}** |

O painel carrega sozinho a RT de um projeto de R$ {br(sr.TOTAL)}, e por isso fica
com **{sr.MC_PAINEL:.1%}** em vez dos {sr.MC_ALVO:.0%} do rack. O **conjunto fecha em {sr.MC_CONJ:.1%}**.

⭐ Para o painel segurar {sr.MC_ALVO:.0%} carregando a mesma RT, o preço dele teria de
ser **R$ {br(sr.PV_PAINEL_30)}** — R$ {br(sr.PV_PAINEL_30 - sr.PAINEL_PV)} acima dos R$ {br(sr.PAINEL_PV)}.

---

## O investimento

| | R$ |
|---|--:|
| rack · sem RT | {br(sr.PV)} |
| painel de TV · liso com dois frisos | {br(sr.PAINEL_PV)} |
| **total** | **R$ {br(sr.TOTAL)}** |

---

'''
p.write_text(s[:s.index(INI)] + novo + s[s.index(FIM):], encoding='utf-8')
print(f'2026-sandra-duarte-rack.md · painel R$ {br(sr.PAINEL_PV)} · '
      f'total R$ {br(sr.TOTAL)}')
