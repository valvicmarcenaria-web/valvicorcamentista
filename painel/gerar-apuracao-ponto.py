# -*- coding: utf-8 -*-
"""Folha de apuração de ponto e horas extras — uma folha A4 por colaborador.

    python3 painel/gerar-apuracao-ponto.py > painel/apuracao-ponto-outubro.html
"""
import importlib.util, os, datetime
_d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados-apuracao-ponto-outubro.py')
_s = importlib.util.spec_from_file_location('dados_apuracao_ponto', _d)
_m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
SAL, DIV, ADC, MES, COLABS = _m.SALARIO, _m.DIVISOR, _m.ADICIONAL, _m.MES, _m.COLABORADORES

HN = SAL / DIV
HE = HN * ADC
SEM = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']

def mi(s):
    h, m = map(int, s.split(':')); return h * 60 + m
def hm(x):
    s = '−' if x < 0 else ''; x = abs(x); return f'{s}{x//60}h{x%60:02d}'
def brl(v):
    return f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

def apura(dias):
    lin, te, td, sem_int = [], 0, 0, 0
    for d, ent, sai, alm, obs in dias:
        wd = datetime.date(2026, 10, d).weekday()
        jor = 8 * 60 if wd == 4 else 9 * 60
        if alm:
            trab = mi(sai) - mi(ent) - 60
        else:
            trab = mi(sai) - mi(ent); sem_int += 1
        if 'Saída antecipada' in obs:
            trab = mi(alm.split('-')[0]) - mi(ent)
        sal = trab - jor
        if sal > 0: te += sal
        else: td += -sal
        lin.append((d, wd, ent, sai, alm, trab, jor, sal, obs))
    return lin, te, td, sem_int

CSS = """
:root{ --navy:#0E2038; --navy2:#16314F; --gold:#C2A05A; --goldsoft:#d8bd80;
  --goldbg:#F6EDD6; --ink:#1b2733; --muted:#6c7785; --linha:#dfe4ea;
  --red:#B0413F; --blue:#2F5D8C; --ok:#2F7D4F; }
@page{ size:A4 portrait; margin:0 }
*{ box-sizing:border-box }
body{ margin:0; background:#8a8f96; font-family:'Inter',system-ui,sans-serif; color:var(--ink) }
.sheet{ width:210mm; height:297mm; margin:0 auto; background:#fff; position:relative;
  padding:11mm 13mm 10mm; display:flex; flex-direction:column;
  page-break-after:always; overflow:hidden }
.sheet:last-child{ page-break-after:auto }
@media print{ body{ background:#fff } .sheet{ margin:0 } }

.topo{ display:flex; justify-content:space-between; align-items:flex-end;
  border-bottom:2px solid var(--navy); padding-bottom:5px; margin-bottom:8px }
.marca{ font-family:'Cormorant Garamond',serif; font-size:24px; font-weight:700;
  color:var(--navy); letter-spacing:.5px; line-height:1 }
.marca small{ display:block; font-family:'Inter',sans-serif; font-size:7px; font-weight:600;
  letter-spacing:2.4px; text-transform:uppercase; color:var(--gold); margin-top:3px }
.doc{ text-align:right }
.doc h1{ margin:0; font-family:'Cormorant Garamond',serif; font-size:19px; font-weight:600; color:var(--navy) }
.doc .m{ font-size:7.5px; color:var(--muted); letter-spacing:.4px; margin-top:2px }

.ident{ display:grid; grid-template-columns:1.4fr 1fr 1fr 1fr 1fr; gap:5px; margin-bottom:7px }
.ident .c{ border:1px solid var(--linha); border-top:2px solid var(--gold); border-radius:2px; padding:5px 8px }
.ident .r{ font-size:6.5px; letter-spacing:1.2px; text-transform:uppercase; color:var(--muted) }
.ident .v{ font-size:10.5px; font-weight:700; color:var(--navy); margin-top:2px }

.nota{ background:var(--goldbg); border-left:3px solid var(--gold); border-radius:2px;
  padding:5px 9px; font-size:8px; line-height:1.45; color:var(--navy2); margin-bottom:7px }

.faixa{ background:var(--navy); color:var(--goldsoft); font-size:8px; font-weight:600;
  letter-spacing:1.8px; text-transform:uppercase; padding:4px 9px; margin:0 0 5px; border-radius:2px }

table.tb{ width:100%; border-collapse:collapse; font-size:8.5px }
table.tb th{ background:var(--navy2); color:var(--goldsoft); font-size:6.5px; font-weight:600;
  letter-spacing:.8px; text-transform:uppercase; padding:3px 6px; text-align:left }
table.tb td{ border-bottom:1px solid var(--linha); padding:3.5px 6px; vertical-align:middle }
table.tb tr:nth-child(odd) td{ background:#f7f9fb }
.num{ text-align:right; font-variant-numeric:tabular-nums }
.mono{ font-family:'JetBrains Mono',monospace; font-size:8px }
.pos{ color:var(--ok); font-weight:700 } .neg{ color:var(--red); font-weight:700 }
.ob{ font-size:7.5px; color:var(--red) }
tr.alerta td{ background:#fdf3f3 !important }
tr.tot td{ background:var(--goldbg) !important; font-weight:700; color:var(--navy);
  border-bottom:1px solid var(--gold) }
tr.liq td{ background:var(--navy) !important; color:#fff; font-weight:700; font-size:10px }
tr.liq td.num{ color:var(--goldsoft); font-size:12.5px }

.aberto{ border:1px solid var(--linha); border-left:3px solid var(--blue); border-radius:2px;
  padding:6px 10px; margin-top:7px; font-size:8px; line-height:1.5; color:#45525f }
.aberto b{ color:var(--navy) }
.aberto .t{ font-size:8.5px; font-weight:700; color:var(--navy); display:block; margin-bottom:2px }

.assina{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; margin-top:auto; padding-top:9px }
.assina > div{ border-top:1px solid var(--ink); padding-top:3px; text-align:center }
.assina .n{ font-size:8px; font-weight:700; color:var(--navy) }
.assina .s{ font-size:7px; color:var(--muted) }
.rodape{ margin-top:9px; border-top:1px solid var(--linha); padding-top:3px;
  display:flex; justify-content:space-between; font-size:6.5px; color:var(--muted);
  letter-spacing:.5px; text-transform:uppercase }
"""

def folha(nome, dias, nota, i, tot):
    lin, te, td, sem_int = apura(dias)
    vhe = te / 60 * HE
    vdef = td / 60 * HN
    liq = SAL + vhe - vdef
    dsr = vhe / 26 * 5
    vint = sem_int * HE
    corpo = []
    for d, wd, ent, sai, alm, trab, jor, sal, obs in lin:
        cls = ' class="alerta"' if obs else ''
        o = f'<br><span class="ob">{obs}</span>' if obs else ''
        sc = 'pos' if sal > 0 else ('neg' if sal < 0 else '')
        corpo.append(
          f'<tr{cls}><td class="mono">{d:02d}/10</td><td>{SEM[wd]}{o}</td>'
          f'<td class="mono">{ent}</td><td class="mono">{sai}</td>'
          f'<td class="mono">{alm if alm else "—"}</td>'
          f'<td class="num mono">{hm(trab)}</td><td class="num mono">{hm(jor)}</td>'
          f'<td class="num mono {sc}">{hm(sal) if sal else "0h00"}</td>'
          f'<td class="num">{brl(sal/60*HE) if sal>0 else "—"}</td></tr>')

    extras = ''
    if td:
        extras += (f'<tr><td colspan="7">Horas abaixo da jornada — {hm(td)} pela hora normal</td>'
                   f'<td class="num mono neg">{hm(-td)}</td><td class="num">− {brl(vdef)}</td></tr>')
    return f'''<div class="sheet">
  <div class="topo">
    <div class="marca">valvic<small>Marcenaria</small></div>
    <div class="doc"><h1>Apuração de Ponto e Horas Extras</h1>
      <div class="m">{nome} · {MES} · uso restrito · folha {i} de {tot}</div></div>
  </div>

  <div class="ident">
    <div class="c"><div class="r">Colaborador</div><div class="v">{nome}</div></div>
    <div class="c"><div class="r">Salário</div><div class="v">R$ {brl(SAL)}</div></div>
    <div class="c"><div class="r">Hora normal</div><div class="v">R$ {brl(HN)}</div></div>
    <div class="c"><div class="r">Hora extra +50%</div><div class="v">R$ {brl(HE)}</div></div>
    <div class="c"><div class="r">Dias apurados</div><div class="v">{len(lin)}</div></div>
  </div>

  <div class="nota"><b>Jornada contratual:</b> segunda a quinta 07:00–17:00 e sexta 07:00–16:00,
  com 1 h de intervalo — 9 h de segunda a quinta, 8 h na sexta, 44 h semanais.
  Hora extra apurada com adicional de 50 %, divisor 220.<br>{nota}</div>

  <div class="faixa">Apuração diária</div>
  <table class="tb">
    <tr><th style="width:38px">Dia</th><th style="width:110px">Sem.</th><th style="width:38px">Entr.</th>
        <th style="width:38px">Saída</th><th style="width:70px">Intervalo</th>
        <th style="width:44px" class="num">Trab.</th><th style="width:40px" class="num">Jorn.</th>
        <th style="width:46px" class="num">Saldo</th><th style="width:52px" class="num">R$ extra</th></tr>
{chr(10).join(corpo)}
    <tr class="tot"><td colspan="7">Horas extras do mês — {hm(te)}</td>
        <td class="num mono">{hm(te)}</td><td class="num">{brl(vhe)}</td></tr>
{extras}
  </table>

  <div class="faixa" style="margin-top:7px">Valor a receber</div>
  <table class="tb">
    <tr><td>Salário do mês</td><td class="num" style="width:90px">R$ {brl(SAL)}</td></tr>
    <tr><td>Horas extras — {hm(te)} × R$ {brl(HE)}</td><td class="num">R$ {brl(vhe)}</td></tr>
    {'<tr><td>Horas abaixo da jornada — ' + hm(td) + ' × R$ ' + brl(HN) + '</td><td class="num">− R$ ' + brl(vdef) + '</td></tr>' if td else ''}
    <tr class="liq"><td>Total a receber</td><td class="num">R$ {brl(liq)}</td></tr>
  </table>

  <div class="aberto"><span class="t">Verbas em aberto — decisão da direção, não somadas acima</span>
  <b>DSR sobre as horas extras:</b> R$ {brl(dsr)} — a hora extra foi habitual no mês e, pela Súmula 172 do TST,
  integra o descanso semanal remunerado. Base: {hm(te)} ÷ 26 dias úteis × 5 domingos e feriado.
  {'<br><b>Intervalo intrajornada suprimido:</b> R$ ' + brl(vint) + ' — ' + str(sem_int) + ' dia(s) sem a hora de almoço. O art. 71 § 4º da CLT manda indenizar o período suprimido com acréscimo de 50 %.' if sem_int else ''}</div>

  <div class="assina">
    <div><div class="n">{nome}</div><div class="s">Ciente da apuração · ___/___/______</div></div>
    <div><div class="n">Conferido</div><div class="s">Karla · ___/___/______</div></div>
    <div><div class="n">Autorizado</div><div class="s">Jonathan ou Paulo</div></div>
  </div>

  <div class="rodape"><span>Valvic Marcenaria · Vargas Decor Ltda</span>
    <span>Apuração de ponto · {nome} · {MES}</span></div>
</div>'''

print('''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Apuração de ponto — outubro/2026</title>
__FONTES__
<style>%s</style>
</head>
<body>
%s
</body>
</html>''' % (CSS, '\n'.join(
    folha(n, d, nt, i, len(COLABS)) for i, (n, d, nt) in enumerate(COLABS, 1))))
