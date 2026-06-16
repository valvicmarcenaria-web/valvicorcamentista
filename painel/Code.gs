// ═══════════════════════════════════════════════════════════════════
//  VALVIC · Painel Financeiro — Google Apps Script
// ═══════════════════════════════════════════════════════════════════
//
//  COMO USAR:
//  1. Abra sua planilha no Google Sheets
//  2. Extensões → Apps Script
//  3. Cole TODO este código, substituindo o conteúdo existente
//  4. Salve (Ctrl+S)
//  5. Clique em "Implementar" → "Nova implementação"
//  6. Tipo: "Web App"
//  7. Executar como: "Eu (seu email)"
//  8. Quem tem acesso: "Qualquer pessoa"
//  9. Clique em "Implementar" e copie a URL gerada
//  10. Cole a URL na tela de configuração do painel HTML
//
// ═══════════════════════════════════════════════════════════════════

const SHEET_NAME = 'Painel_Projetos';

// ── Roteador principal ──────────────────────────────────────────────

function doGet(e) {
  try {
    const action = (e.parameter && e.parameter.action) || 'getData';

    if (action === 'getData') {
      const sheet = getOrCreateSheet_();
      return jsonOk_(getProjects_(sheet));
    }

    if (action === 'updatePayment') {
      const sheet = getOrCreateSheet_();
      updatePayment_(
        sheet,
        e.parameter.id,
        parseInt(e.parameter.pag, 10),
        e.parameter.received === 'true'
      );
      return jsonOk_({ ok: true });
    }

    if (action === 'deleteProject') {
      const sheet = getOrCreateSheet_();
      deleteProject_(sheet, e.parameter.id);
      return jsonOk_({ ok: true });
    }

    return jsonOk_({ error: 'Ação desconhecida: ' + action });
  } catch (err) {
    return jsonOk_({ error: err.message });
  }
}

function doPost(e) {
  try {
    const project = JSON.parse(e.postData.contents);
    const sheet = getOrCreateSheet_();
    appendProject_(sheet, project);
    return jsonOk_({ ok: true });
  } catch (err) {
    return jsonOk_({ error: err.message });
  }
}

// ── Helpers de planilha ─────────────────────────────────────────────

function getOrCreateSheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
    const headers = [
      'id', 'cliente', 'projeto', 'investimento', 'formaPag', 'mesRef', 'anoRef',
      'p1Valor', 'p1Data', 'p1Desc', 'p1Recebido',
      'p2Valor', 'p2Data', 'p2Desc', 'p2Recebido',
      'p3Valor', 'p3Data', 'p3Desc', 'p3Recebido',
      'p4Valor', 'p4Data', 'p4Desc', 'p4Recebido',
      'p5Valor', 'p5Data', 'p5Desc', 'p5Recebido',
      'criadoEm'
    ];
    sheet.appendRow(headers);
    sheet.setFrozenRows(1);
    sheet.getRange(1, 1, 1, headers.length)
      .setBackground('#1B1208')
      .setFontColor('#C8914A')
      .setFontWeight('bold');
    sheet.setColumnWidth(1, 160);
  }
  return sheet;
}

function getProjects_(sheet) {
  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return [];
  const headers = data[0];
  return data.slice(1)
    .filter(row => row[0]) // skip empty rows
    .map(row => {
      const obj = {};
      headers.forEach((h, i) => { obj[h] = row[i]; });
      return obj;
    });
}

function appendProject_(sheet, p) {
  const row = [
    p.id || Utilities.getUuid(),
    p.cliente || '',
    p.projeto || '',
    Number(p.investimento) || 0,
    p.formaPag || '',
    p.mesRef || '',
    p.anoRef || '2026',
    Number(p.p1Valor) || '', p.p1Data || '', p.p1Desc || '', p.p1Recebido ? true : false,
    Number(p.p2Valor) || '', p.p2Data || '', p.p2Desc || '', p.p2Recebido ? true : false,
    Number(p.p3Valor) || '', p.p3Data || '', p.p3Desc || '', p.p3Recebido ? true : false,
    Number(p.p4Valor) || '', p.p4Data || '', p.p4Desc || '', p.p4Recebido ? true : false,
    Number(p.p5Valor) || '', p.p5Data || '', p.p5Desc || '', p.p5Recebido ? true : false,
    new Date().toISOString()
  ];
  sheet.appendRow(row);
}

function updatePayment_(sheet, projectId, pagIndex, received) {
  const data = sheet.getDataRange().getValues();
  // Columns: id(0) cliente(1) projeto(2) investimento(3) formaPag(4) mesRef(5) anoRef(6)
  // p1: 7,8,9,10 | p2: 11,12,13,14 | p3: 15,16,17,18 | p4: 19,20,21,22 | p5: 23,24,25,26
  const recvCol = 7 + (pagIndex * 4) + 3; // 0-indexed
  for (let i = 1; i < data.length; i++) {
    if (String(data[i][0]) === String(projectId)) {
      sheet.getRange(i + 1, recvCol + 1).setValue(received);
      return;
    }
  }
}

function deleteProject_(sheet, projectId) {
  const data = sheet.getDataRange().getValues();
  for (let i = 1; i < data.length; i++) {
    if (String(data[i][0]) === String(projectId)) {
      sheet.deleteRow(i + 1);
      return;
    }
  }
}

function jsonOk_(data) {
  return ContentService
    .createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}
