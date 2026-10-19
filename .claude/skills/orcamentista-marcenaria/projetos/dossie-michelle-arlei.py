# -*- coding: utf-8 -*-
"""Gera `2026-michelle-arlei.md` a partir do motor. Nada digitado à mão —
   mudou a MC, mudou a linha, mudou o miolo: roda de novo e o dossiê acerta.
   ⛔ Foi por isso que virou arquivo: na primeira versão eu gerei o dossiê
     por um script solto, e à primeira mudança de MC os números do .md
     ficaram para trás sem ninguém ver."""
import importlib.util, pathlib, sys, io, contextlib
P = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('ma', P/'corte-michelle-arlei.py')
ma = importlib.util.module_from_spec(spec); sys.modules['ma'] = ma
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(ma)
br = ma.br

DESC = {
 'M01':'Painel de TV liso e ripado + rack suspenso com quatro gavetas · Gianduia',
 'M02':'Bancada de lanche · Itapuã',
 'M03':'Prateleira iluminada · Itapuã',
 'M04':'Armário inferior em "U", seis portas de giro · Gianduia',
 'M22':'Torre quente: básculas, nicho de micro-ondas e de forno, gaveta · Itapuã',
 'M23':'Armário superior, quatro portas de giro · Gianduia',
 'M26':'Estrutura metálica preta com dois cachepôs de temperos · Itapuã',
 'M05':'Armário inferior, duas portas ripadas e gaveta de espetos · Gianduia',
 'M06':'Mesa de apoio em estrutura metálica preta, tampo e prateleira · Itapuã',
 'M07':'Armário de básculas iluminado + prateleira · Itapuã',
 'M08':'Armário inferior, seis portas de giro · Gianduia',
 'M09':'Armário de banheiro, portas de giro e gavetas · Itapuã',
 'M10':'Armário de banheiro, portas de giro e gavetas · Areia',
 'M11':'Painel liso e ripado + prateleira iluminada + escrivaninha · Brisa e Itapuã',
 'M12':'Armário suspenso, puxador fecho-toque · Brisa',
 'M13':'Cabeceira ripada iluminada · Brisa',
 'M24':'Prateleira · Itapuã',
 'M25':'Prateleira · Itapuã',
 'M14':'Baú com tampo basculante · Brisa',
 'M15':'Cabeceira iluminada · Alecrim',
 'M16':'Duas mesas de cabeceira, duas gavetas cada · Brisa',
 'M17':'Armário, três portas de giro · Brisa',
 'M18':'Painel de TV + armário superior + escrivaninha com gavetas · Brisa e Alecrim',
 'M19':'Cabeceira iluminada · Itapuã',
 'M20':'Painel de TV piso/teto com porta de correr embutida e ripado · Itapuã e Areia',
 'M21':'Closet: maleiros, cabideiros, nichos, gavetas, sapateiras e banco · Itapuã e Areia',
}
assert set(DESC) == set(ma.MOVEIS), (
    f'⛔ O MOTOR E O DOSSIÊ NÃO FALAM DOS MESMOS MÓVEIS: '
    f'{set(ma.MOVEIS) ^ set(DESC)}')

L = []; w = L.append
w('# MICHELLE E ARLEI — casa completa\n')
w('**Projeto executivo da INÉDITA ARQUITETURA** (CAU A6346-6), 11/12/2024,')
w('revisão R00, **22 pranchas A2**. Residencial completo: sala, cozinha, área')
w('gourmet, lavanderia, banho social, banho do casal, quarto do Gabriel,')
w('quarto das gêmeas e suíte master com closet.\n')
w('⛔ *"Obrigatoriamente conferir medidas no local."*\n')
w('---\n')
w('## A linha e a margem\n')
w('⭐ [Jonathan 18/10] **"vamos orçar na linha essencial com 35% de MC e com RT."**')
w('⭐ [Jonathan 19/10] **"vamos subir a MC para 38%."**\n')
w(f'MC **{ma.MC_ALVO:.0%}** · **com RT** · base **{ma.BASE*100:.2f}%** — '
  f'dentro da faixa ideal da casa ({ma.M.MC_IDEAL[0]:.0%}–{ma.M.MC_IDEAL[1]:.0%}).\n')
w('A linha Essencial, neste projeto:\n')
w('* **interior e caixaria em Branco TX** — cor só onde aparece')
w('* **corrediça telescópica** com amortecedor — é o que a prancha já pede')
w('* **dobradiça com amortecedor a R$ 12**, a nacional da casa')
w('* **fita e perfil de LED comuns**, não a linha profissional')
w('* **garantia de 2 anos**\n')
w('⚠ **O que a linha não mexe:** as cinco cores de MDF são especificação da')
w('arquiteta, peça por peça. Trocá-las não é mudar de linha, é mudar de')
w('projeto — e não foi pedido.\n')
w('---\n')
w('## ⛔⛔ Cinco cores de MDF num projeto só\n')
w('| cor | móveis |')
w('|---|---|')
w('| **Gianduia Natural**, Duratex | M01, M04, M05, M08, M23 |')
w('| **Itapuã**, Duratex | M02, M03, M06, M07, M09, M11, M19, M20, M21, M22, M24, M25, M26 |')
w('| **Areia**, Guararapes | M10, M20 (ripado), M21 (parte) |')
w('| **Brisa**, Guararapes | M11 (painel), M12, M13, M14, M16, M17, M18 |')
w('| **Alecrim**, Guararapes | M15, M18 (armário superior e escrivaninha) |\n')
w('**Cor nenhuma divide chapa com outra**, e cada par cor × espessura paga o')
w('próprio mínimo de uma chapa inteira.\n')
w('| cor · espessura | área m² | chapas | R$/chapa | R$ |')
w('|---|--:|--:|--:|--:|')
for k in sorted(ma.R['area'], key=lambda k: (k[0], k[1])):
    pr = ma.BR[k[1]] if k[0] == 'Branco TX' else ma.COR[k[1]]
    w(f'| {k[0]} · {k[1]} mm | {ma.R["area"][k]:.2f} | {ma.R["chapas"][k]:.0f} '
      f'| {pr:.0f} | {ma.R["custo_ch"][k]:.0f} |')
w(f'| **total** | **{sum(ma.R["area"].values()):.2f}** '
  f'| **{sum(ma.R["chapas"].values()):.0f}** | | **{sum(ma.R["custo_ch"].values()):.0f}** |\n')
w(f'A **sobra** comprada e não usada é **R$ {br(ma.R["sobra"])}** — '
  f'{ma.R["sobra"]/sum(ma.R["custo_ch"].values()):.0%} da chapa. É o preço de')
w('cinco famílias de cor num projeto só.\n')
w('---\n')
w('## Móvel a móvel\n')
for am in ma.AMBS:
    w(f'### {am}\n')
    w('| | móvel | custo | **preço** |')
    w('|---|---|--:|--:|')
    for mv in [m for m in ma.MOVEIS if ma.AMB_DE[m] == am]:
        w(f'| {mv} | {DESC[mv]} | {br(ma.R["CD"][mv])} | **{br(ma.R["PV"][mv])}** |')
    w(f'| | **subtotal** | | **R$ {br(ma.PV_AMB[am])}** |\n')
w('---\n')
w('## O investimento\n')
w('| ambiente | R$ |')
w('|---|--:|')
for am in ma.AMBS: w(f'| {am} | {br(ma.PV_AMB[am])} |')
w(f'| **custo direto** | **{br(ma.R["CD_TOT"])}** |')
w(f'| **INVESTIMENTO TOTAL** | **R$ {br(ma.TOTAL)}** |\n')
_srt = ma.M.base(parcelas=0, rt=False, vendedor=False)
_sem = sum(round(ma.R['CD'][mv]/(_srt-ma.MC_ALVO)/10)*10 for mv in ma.MOVEIS)
_p35 = sum(round(ma.R['CD'][mv]/(ma.BASE-0.35)/10)*10 for mv in ma.MOVEIS)
w(f'⭐ **A RT de 10% vale R$ {br(ma.TOTAL-_sem)}**: sem ela a casa sairia a')
w(f'**R$ {br(_sem)}**.\n')
w(f'⭐ **A 35% a casa sairia a R$ {br(_p35)}** — os três pontos de MC valem')
w(f'**R$ {br(ma.TOTAL-_p35)}**.\n')
w(f'⭐ **Interior na cor** em vez de Branco TX levaria o total a')
w(f'**R$ {br(ma.R_C["TOT"])}** — R$ {br(ma.R_C["TOT"]-ma.TOTAL)} a mais, '
  f'{(ma.R_C["TOT"]-ma.TOTAL)/ma.TOTAL:.0%}.\n')
w('---\n')
w('## ★ Em aberto\n')
w('1. ⛔⛔ **A prateleira M03 tem 3,23 m e a chapa tem 2,75.** Não existe peça')
w('   inteira nessa medida: ou vai com **emenda**, ou vira **duas**')
w('   prateleiras com encontro aparente. É escolha de projeto — decidir com')
w('   a arquiteta antes de produzir.')
w('2. ⛔ **Ripa de 2 × 2 cm.** A prancha pede ripa quadrada de 2 cm; cortada')
w('   de chapa de 18 mm ela fica **18 × 20**, não 20 × 20. Para 20 cheios é')
w('   sarrafo ou chapa de 25 — e muda o preço dos ripados.')
w('3. ⛔ **Pé-direito divergente dentro da própria prancha:** a planta de')
w('   layout traz **PD = 260** e a de paginação de piso traz **270**. Os')
w('   móveis de piso/teto (M11, M20, M21) dependem disso.')
w('4. ⚠ **As bancadas B01…B05 são marmoraria**, granito preto São Gabriel —')
w('   não são marcenaria e **não estão neste preço**.')
w('5. ⚠ **M16:** a prancha detalha uma mesa de cabeceira e as vistas mostram')
w('   duas (são duas camas). **Orçei duas.**')
w(f'6. ★ **Serralheria** (M06, M20, M26 e o rodapé em perfil L) estimada a')
w(f'   R$ {br(ma.SERRALHA_M)}/m e R$ {br(ma.RODAPE_M)}/m — **cotar**.')
w('7. ⚠ **Eletrodomésticos são dos clientes.** A prancha manda *"compatibilizar')
w('   armário com forno e micro-ondas comprados pelos clientes, não executar')
w('   sem essa compatibilização"*.')
w('8. ⚠ **Pontos elétricos a transferir para a marcenaria** (arandela da sala,')
w('   tomadas da cozinha, ar-condicionado dos quartos) — compatibilizar com a')
w('   planta elétrica antes do corte.\n')
w('---\n')
w('## As imagens\n')
w('`projetos/img-michelle-arlei/` — 15 renders por ambiente, do caderno da')
w('Inédita. ⚠ Cada um traz uma **tarja preta** com o nome do ambiente e a')
w('marca do render; **cortar antes de usar em proposta**.\n')
(P/'2026-michelle-arlei.md').write_text('\n'.join(L), encoding='utf-8')
print(f'2026-michelle-arlei.md · MC {ma.MC_ALVO:.0%} · R$ {br(ma.TOTAL)}')
