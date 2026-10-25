#!/usr/bin/env python3
"""Conciliação bancária: extrato (OFX/CSV/XLSX) × lançamentos do sistema
(export do Calcme ou planilha). Gera um xlsx com Resumo, Conciliados,
So_no_banco, So_no_sistema e Possiveis_duplicados.

Casamento: mesmo valor (centavos) e data dentro de ±N dias corridos; entre
candidatos, vence o de menor distância de data e, em empate, o de descrição
mais parecida. Cada linha casa no máximo uma vez.

Uso:
  python conciliar_extrato.py --extrato extrato.ofx --sistema calcme.xlsx \
      --saida conciliacao.xlsx [--dias 3]
      [--col-data-extrato X --col-valor-extrato Y --col-desc-extrato Z]
      [--col-data-sistema X --col-valor-sistema Y --col-desc-sistema Z]
      [--sinal-sistema inverter]   # se o sistema guarda pagamentos como positivos
      [--col-tipo-sistema T --valor-saida "Pagar"]  # coluna que diz se é saída

As colunas são detectadas pelo nome (data/valor/descrição/histórico) quando
não informadas. Valores no formato brasileiro (1.234,56) são aceitos.
"""
import argparse
import difflib
import re
import sys

import pandas as pd

NOMES_DATA = ["data_caixa", "data pagamento", "data_pagamento", "dt pagamento", "pagamento",
              "data", "date", "dt", "data lançamento", "data movimento", "vencimento"]
NOMES_VALOR = ["valor", "valor pago", "valor_pago", "amount", "vlr", "valor (r$)", "montante"]
NOMES_DESC = ["descricao", "descrição", "historico", "histórico", "memo", "favorecido",
              "contraparte", "cliente/fornecedor", "lançamento", "detalhes"]


def para_numero(v):
    if pd.isna(v):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace("R$", "").replace(" ", "")
    neg = s.startswith("(") and s.endswith(")") or s.endswith("-") or s.upper().endswith("D")
    s = s.strip("()").rstrip("-").rstrip("DdCc")
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    try:
        n = float(s)
    except ValueError:
        return None
    return -abs(n) if neg else n


def ler_ofx(caminho):
    txt = open(caminho, encoding="latin-1", errors="ignore").read()
    linhas = []
    for bloco in re.findall(r"<STMTTRN>(.*?)(?:</STMTTRN>|(?=<STMTTRN>)|</BANKTRANLIST>)", txt, re.S | re.I):
        def tag(t):
            m = re.search(rf"<{t}>([^<\r\n]*)", bloco, re.I)
            return m.group(1).strip() if m else ""
        data = tag("DTPOSTED")[:8]
        linhas.append({
            "data": pd.to_datetime(data, format="%Y%m%d", errors="coerce"),
            "valor": para_numero(tag("TRNAMT").replace(",", ".")),
            "descricao": " ".join(x for x in [tag("NAME"), tag("MEMO")] if x),
            "id": tag("FITID"),
        })
    return pd.DataFrame(linhas)


def ler_tabela(caminho):
    if caminho.lower().endswith((".xlsx", ".xlsm", ".xls")):
        return pd.read_excel(caminho)
    for enc in ("utf-8-sig", "latin-1"):
        try:
            return pd.read_csv(caminho, sep=None, engine="python", encoding=enc)
        except UnicodeDecodeError:
            continue
    sys.exit(f"Não consegui ler {caminho}")


def achar_coluna(df, preferida, candidatos, papel):
    cols = {str(c).strip().lower(): c for c in df.columns}
    if preferida:
        if preferida in df.columns:
            return preferida
        if preferida.lower() in cols:
            return cols[preferida.lower()]
        sys.exit(f"Coluna '{preferida}' ({papel}) não existe. Colunas: {list(df.columns)}")
    for c in candidatos:
        if c in cols:
            return cols[c]
    for c in candidatos:
        for k, orig in cols.items():
            if c in k:
                return orig
    if papel == "descrição":
        return None
    sys.exit(f"Não achei a coluna de {papel}. Colunas: {list(df.columns)} — use --col-...")


def normalizar(df, cdata, cvalor, cdesc, origem):
    out = pd.DataFrame({
        "data": pd.to_datetime(df[cdata], dayfirst=True, errors="coerce"),
        "valor": df[cvalor].map(para_numero),
        "descricao": df[cdesc].astype(str) if cdesc else "",
    })
    out["linha_origem"] = df.index + 2  # linha no arquivo (cabeçalho = 1)
    for c in df.columns:
        if c not in (cdata, cvalor, cdesc):
            out[f"{origem}:{c}"] = df[c].values
    sem = out["data"].isna() | out["valor"].isna()
    return out[~sem].reset_index(drop=True), out[sem]


def similar(a, b):
    a = re.sub(r"[^a-z0-9 ]", " ", str(a).lower())
    b = re.sub(r"[^a-z0-9 ]", " ", str(b).lower())
    return difflib.SequenceMatcher(None, a, b).ratio()


def conciliar(ext, sis, dias):
    ext = ext.copy()
    sis = sis.copy()
    ext["cent"] = (ext["valor"] * 100).round().astype("int64")
    sis["cent"] = (sis["valor"] * 100).round().astype("int64")
    usados_s = set()
    pares = []
    por_valor = {k: g.index.tolist() for k, g in sis.groupby("cent")}
    # extrato em ordem de data para casar de forma estável
    for i in ext.sort_values("data").index:
        cand = [j for j in por_valor.get(ext.at[i, "cent"], []) if j not in usados_s]
        melhor = None
        for j in cand:
            dd = abs((ext.at[i, "data"] - sis.at[j, "data"]).days)
            if dd > dias:
                continue
            chave = (dd, -similar(ext.at[i, "descricao"], sis.at[j, "descricao"]))
            if melhor is None or chave < melhor[0]:
                melhor = (chave, j)
        if melhor:
            j = melhor[1]
            usados_s.add(j)
            pares.append((i, j, melhor[0][0]))
    usados_e = {p[0] for p in pares}
    conc = pd.DataFrame([{
        "data_banco": ext.at[i, "data"].date(), "data_sistema": sis.at[j, "data"].date(),
        "dif_dias": d, "valor": ext.at[i, "valor"],
        "descricao_banco": ext.at[i, "descricao"], "descricao_sistema": sis.at[j, "descricao"],
        "linha_banco": ext.at[i, "linha_origem"], "linha_sistema": sis.at[j, "linha_origem"],
    } for i, j, d in pares])
    so_banco = ext.drop(index=list(usados_e)).drop(columns="cent")
    so_sis = sis.drop(index=list(usados_s)).drop(columns="cent")
    return conc, so_banco, so_sis


def duplicados(df, origem, dias=5):
    df = df.sort_values("data")
    achados = []
    for _, g in df.groupby((df["valor"] * 100).round()):
        if len(g) < 2:
            continue
        g = g.sort_values("data")
        datas = g["data"].tolist()
        for k in range(1, len(g)):
            if (datas[k] - datas[k - 1]).days <= dias:
                for idx in (k - 1, k):
                    r = g.iloc[idx]
                    achados.append({"origem": origem, "data": r["data"].date(), "valor": r["valor"],
                                    "descricao": r["descricao"], "linha_origem": r["linha_origem"]})
    return pd.DataFrame(achados).drop_duplicates()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--extrato", required=True)
    ap.add_argument("--sistema", required=True)
    ap.add_argument("--saida", required=True)
    ap.add_argument("--dias", type=int, default=3)
    for o in ("extrato", "sistema"):
        for p in ("data", "valor", "desc"):
            ap.add_argument(f"--col-{p}-{o}")
    ap.add_argument("--sinal-sistema", choices=["manter", "inverter"], default="manter")
    ap.add_argument("--col-tipo-sistema")
    ap.add_argument("--valor-saida", help="valor da coluna tipo que indica saída (ex.: Pagar, D, Despesa)")
    a = ap.parse_args()

    if a.extrato.lower().endswith(".ofx"):
        ext_raw = ler_ofx(a.extrato)
        ext_raw.index = range(len(ext_raw))
        ext, ext_bad = normalizar(ext_raw, "data", "valor", "descricao", "banco")
    else:
        df = ler_tabela(a.extrato)
        ext, ext_bad = normalizar(
            df, achar_coluna(df, a.col_data_extrato, NOMES_DATA, "data"),
            achar_coluna(df, a.col_valor_extrato, NOMES_VALOR, "valor"),
            achar_coluna(df, a.col_desc_extrato, NOMES_DESC, "descrição"), "banco")

    df = ler_tabela(a.sistema)
    sis, sis_bad = normalizar(
        df, achar_coluna(df, a.col_data_sistema, NOMES_DATA, "data"),
        achar_coluna(df, a.col_valor_sistema, NOMES_VALOR, "valor"),
        achar_coluna(df, a.col_desc_sistema, NOMES_DESC, "descrição"), "sistema")
    if a.col_tipo_sistema:
        tipo = df.loc[sis["linha_origem"] - 2, a.col_tipo_sistema].astype(str).str.strip().str.lower().values
        saida = (a.valor_saida or "").strip().lower()
        sis["valor"] = [-abs(v) if t == saida else abs(v) for v, t in zip(sis["valor"], tipo)]
    elif a.sinal_sistema == "inverter":
        sis["valor"] = -sis["valor"]

    conc, so_banco, so_sis = conciliar(ext, sis, a.dias)
    dup = pd.concat([duplicados(ext, "banco"), duplicados(sis, "sistema")], ignore_index=True)

    resumo = pd.DataFrame([
        ("Período do extrato", f"{ext['data'].min():%d/%m/%Y} a {ext['data'].max():%d/%m/%Y}" if len(ext) else "-"),
        ("Linhas no extrato", len(ext)),
        ("Linhas no sistema", len(sis)),
        ("Conciliados", len(conc)),
        ("Só no banco (não lançados no sistema)", len(so_banco)),
        ("Só no sistema (não aparecem no banco)", len(so_sis)),
        ("Σ extrato (variação)", round(ext["valor"].sum(), 2)),
        ("Σ sistema", round(sis["valor"].sum(), 2)),
        ("Σ só no banco", round(so_banco["valor"].sum(), 2)),
        ("Σ só no sistema", round(so_sis["valor"].sum(), 2)),
        ("Diferença Σ extrato − Σ sistema", round(ext["valor"].sum() - sis["valor"].sum(), 2)),
        ("Possíveis duplicados (mesmo valor ≤ 5 dias)", len(dup)),
        ("Linhas ignoradas sem data/valor (banco/sistema)", f"{len(ext_bad)}/{len(sis_bad)}"),
        ("Tolerância de data (dias)", a.dias),
        ("Atenção", "Sistema fora do período do extrato aparece em 'só no sistema' — filtre o período antes."),
    ], columns=["Item", "Valor"])

    with pd.ExcelWriter(a.saida, engine="openpyxl") as w:
        resumo.to_excel(w, sheet_name="Resumo", index=False)
        conc.to_excel(w, sheet_name="Conciliados", index=False)
        so_banco.assign(data=so_banco["data"].dt.date).to_excel(w, sheet_name="So_no_banco", index=False)
        so_sis.assign(data=so_sis["data"].dt.date).to_excel(w, sheet_name="So_no_sistema", index=False)
        dup.to_excel(w, sheet_name="Possiveis_duplicados", index=False)
        for ws in w.book.worksheets:
            for c in ws.columns:
                ws.column_dimensions[c[0].column_letter].width = min(
                    45, max(10, *(len(str(x.value or "")) for x in c[:200])))
    print(resumo.to_string(index=False))
    print(f"\nArquivo: {a.saida}")


if __name__ == "__main__":
    main()
