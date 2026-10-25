/**
 * Valvic Marcenaria · botão "Abrir ficha do projeto"
 *
 * Onde mora: dentro da planilha GESTÃO 2026 — é lá que o cliente novo entra.
 * (Serve igual na Análise anual, se você preferir abrir ficha de lá.)
 *   Extensões → Apps Script → cole este arquivo inteiro → salve.
 *   Feche e abra a planilha: aparece o menu "Valvic" na barra de cima.
 *
 * O que faz, com a linha do projeto selecionada numa aba de ano:
 *   1. duplica a "Ficha Modelo" na Custo por Projeto
 *   2. nomeia a aba com o cliente
 *   3. preenche cliente, projeto e valor de venda
 *   4. registra a aba no Painel Geral, na primeira vaga livre
 *   5. estende a Base · Comissões com o bloco de 12 ambientes daquele projeto
 *
 * Por que botão e não automático: um gatilho onEdit criaria ficha a cada linha
 * digitada errada, a cada teste, a cada cliente que não fechou. Aqui a ficha
 * nasce quando alguém decide que o projeto existe.
 *
 * Se a Custo por Projeto for recriada noutro arquivo, troque o ID abaixo.
 */

const ID_CUSTO = '1tTJXG4w7lDvIcnd0dyr219-leOPwuURqrBk6lJIr18I';

// ── mapa da ficha. Se a estrutura mudar, é aqui que se acerta ────────────
const FICHA = {
  modelo: 'Ficha Modelo',
  painel: 'Painel Geral',
  base: 'Base · Comissões',
  cliente: 'A7',          // identificação
  dataEntrada: 'F7',
  projeto: 'A9',
  vendaRealizada: 'D28',  // bloco 1
  ambLinha0: 49,          // bloco 3 · primeiro ambiente
  ambQtd: 12,
  coordenador: 'F9',      // quem coordena o projeto
  comCoord: 'D65',        // bloco 4 · comissão de coordenação
  liquido: 'D45',         // bloco 2 · receita líquida
  venda: 'A13',           // KPI do topo · valor de venda
  imposto: 'B38',         // bloco 2 · descontos sobre a venda
  maquina: 'B39',
  vendedor: 'B41',
  rt: 'B43',
  custoVenda: 'D44',
  custoTotal: 'D22',      // bloco resumo · coluna D = realizado
  margem: 'D23',
  comGestao: 'D66',       // gestão técnica · 0,5% do líquido
  gestorTecnico: 'H9',    // ao lado do coordenador, na identificação
  vendedorNome: 'D9',
  comVenda: 'D41',
  competencia: 'D10',     // linha 10 · era espaçador
  entregaSituacao: 'L9',
  faturado: 'D34',
  rtValor: 'D43',
  rtStatus: 'E43',
  colsBase: 38,           // largura da Base · Comissões
  painelLinha0: 11,       // Painel Geral · primeira vaga de projeto
  painelLinhaF: 50,
  baseLinha0: 2,          // Base · primeira linha de dados
};

/**
 * Separador de argumentos. Numa planilha em português o Google espera
 * ponto e vírgula; o Apps Script grava o texto cru, sem traduzir. Escrever
 * vírgula numa planilha pt_BR transforma a fórmula inteira em #ERROR!.
 * calibrar_() descobre qual é, escrevendo =SUM(1,2) numa aba temporária e
 * conferindo se dá 3. A aba é apagada em seguida.
 */
let SEP = ',';
let CALIBRADO = false;

function calibrar_(ss) {
  const tmp = ss.insertSheet('__teste_separador__');
  try {
    tmp.getRange(1, 1).setFormula('=SUM(1,2)');
    SpreadsheetApp.flush();
    SEP = (tmp.getRange(1, 1).getValue() === 3) ? ',' : ';';
  } catch (e) {
    SEP = ';';
  } finally {
    ss.deleteSheet(tmp);
  }
  CALIBRADO = true;
  return SEP;
}

/** Troca as vírgulas separadoras, poupando o que estiver dentro de aspas. */
function fx_(f) {
  if (SEP === ',' || typeof f !== 'string' || f.charAt(0) !== '=') return f;
  let fora = true, out = '';
  for (let i = 0; i < f.length; i++) {
    const c = f.charAt(i);
    if (c === '"') fora = !fora;
    out += (c === ',' && fora) ? SEP : c;
  }
  return out;
}


const COLS_AMB = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'];


function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('Valvic')
    .addItem('Abrir ficha do cliente selecionado', 'abrirFicha')
    .addSeparator()
    .addItem('Reconstruir a Base · Comissões', 'reconstruirBase')
    .addToUi();
}


function abrirFicha() {
  const ui = SpreadsheetApp.getUi();
  const aba = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const linha = aba.getActiveRange().getRow();

  // Funciona na aba onde o cliente novo de fato nasce:
  //   Pagamentos 2026   — a aba de ano depois da migração
  //   2026, 2025, …     — as abas de ano como ainda estão na Análise anual
  //
  // A aba "Clientes" saiu: ela era um segundo lugar para digitar o mesmo
  // cliente, e ficou com as quatro colunas de cadastro vazias nos 47. O
  // telefone e o número do projeto moram agora na própria linha do pagamento.
  const nomeAba = aba.getName();
  if (!/^(Pagamentos )?20\d\d$/.test(nomeAba)) {
    ui.alert('Selecione a linha do cliente numa aba de pagamentos — '
             + '"Pagamentos 2026", por exemplo.');
    return;
  }

  const cliente = String(aba.getRange(linha, 1).getValue() || '').trim();
  const projeto = String(aba.getRange(linha, 2).getValue() || '').trim();
  const valor = aba.getRange(linha, 3).getValue();
  const data1 = aba.getRange(linha, 10).getValue();

  if (!cliente || !valor) {
    ui.alert('Essa linha não tem cliente e investimento.\n\n' +
             'Selecione uma linha de projeto, não uma linha divisora de mês.');
    return;
  }

  const destino = SpreadsheetApp.openById(ID_CUSTO);
  if (destino.getSheetByName(cliente)) {
    ui.alert('Já existe uma aba chamada "' + cliente + '" na Custo por Projeto.\n\n' +
             'Se for outro projeto do mesmo cliente, mude o nome na coluna Cliente ' +
             'antes de abrir a ficha.');
    return;
  }

  const painel = destino.getSheetByName(FICHA.painel);
  if (!painel) {
    // Sem esta guarda o primeiraVaga_ estourava com TypeError cru, e quem
    // aperta o botão via erro de script em vez de mensagem.
    ui.alert('Não achei a aba "' + FICHA.painel + '" na Custo por Projeto.\n\n'
             + 'É dela que sai a próxima vaga de projeto. Confira o nome da aba '
             + 'antes de abrir ficha nova.');
    return;
  }
  const vaga = primeiraVaga_(painel);
  if (vaga < 0) {
    ui.alert('O Painel Geral está com as ' +
             (FICHA.painelLinhaF - FICHA.painelLinha0 + 1) +
             ' vagas de projeto ocupadas. Libere uma antes de abrir ficha nova.');
    return;
  }

  const r = ui.alert('Abrir ficha do projeto?',
    'Cliente: ' + cliente + '\n' +
    'Projeto: ' + (projeto || '(em branco)') + '\n' +
    'Valor: ' + valor + '\n\n' +
    'Vai criar a aba na Custo por Projeto, registrar no Painel Geral e estender a base.',
    ui.ButtonSet.OK_CANCEL);
  if (r !== ui.Button.OK) return;

  // 1 · duplica o modelo e nomeia
  const modelo = destino.getSheetByName(FICHA.modelo);
  const nova = modelo.copyTo(destino).setName(cliente);
  nova.setFrozenRows(0);
  nova.setFrozenColumns(0);
  destino.setActiveSheet(nova);
  destino.moveActiveSheet(destino.getSheets().length - 1);

  // 2 · preenche o que já se sabe
  nova.getRange(FICHA.cliente).setValue(cliente);
  if (projeto) nova.getRange(FICHA.projeto).setValue(projeto);
  nova.getRange(FICHA.vendaRealizada).setValue(valor);
  let notaData = 'Data de entrada em branco — preencha na ficha.';
  if (data1 instanceof Date) {
    nova.getRange(FICHA.dataEntrada).setValue(data1);
    notaData = 'Data de entrada preenchida com a data do 1º pagamento — confira.';
  }

  // 3 · registra no Painel Geral
  painel.getRange(vaga, 2).setValue(cliente);

  // 4 · estende a base
  //
  // O índice do bloco é a POSIÇÃO DA ABA, não a linha do Painel Geral. O
  // atualizar-tudo escreve a Base varrendo as abas na ordem em que estão na
  // planilha; se aqui se usasse a linha do registro, o bloco de doze linhas
  // deste projeto cairia num slot diferente do que o atualizarTudo vai usar
  // na próxima rodada — e as catorze individuais, que leem a Base por posição,
  // mostrariam o número de outro projeto até alguém rodar o script.
  calibrar_(destino);
  const FIXAS = ['Instruções', FICHA.painel, FICHA.modelo, 'Listas', FICHA.base];
  const abas = destino.getSheets().map(function (x) { return x.getName(); })
                      .filter(function (x) { return FIXAS.indexOf(x) < 0; });
  const i = abas.indexOf(cliente);
  if (i < 0 || i > FICHA.painelLinhaF - FICHA.painelLinha0) {
    ui.alert('A ficha foi criada, mas não consegui estender a base.\n\n'
             + 'Rode o atualizarTudo no script: ele refaz a Base inteira.');
    return;
  }
  escreverBlocoBase_(destino, i, cliente);

  SpreadsheetApp.flush();
  ui.alert('Ficha criada.',
    'A aba "' + cliente + '" existe na Custo por Projeto, registrada na linha ' +
    vaga + ' do Painel Geral.\n\n' + notaData + '\n\n' +
    'Falta preencher na ficha: vendedor, coordenador, entrega prevista e os ambientes.',
    ui.ButtonSet.OK);
}


/**
 * Reescreve a Base · Comissões inteira a partir do que está no Painel Geral.
 * Use quando a base e os projetos saírem de sincronia — por exemplo depois de
 * renomear uma aba à mão, ou de apagar um projeto.
 */
function reconstruirBase() {
  const ui = SpreadsheetApp.getUi();
  const r = ui.alert('Reconstruir a Base · Comissões?',
    'Reescreve as fórmulas da base a partir dos projetos registrados no Painel ' +
    'Geral. Não apaga nada das fichas nem das planilhas individuais.',
    ui.ButtonSet.OK_CANCEL);
  if (r !== ui.Button.OK) return;

  const destino = SpreadsheetApp.openById(ID_CUSTO);
  calibrar_(destino);
  const painel = destino.getSheetByName(FICHA.painel);
  const nomes = painel.getRange(FICHA.painelLinha0, 2,
                                FICHA.painelLinhaF - FICHA.painelLinha0 + 1, 1).getValues();
  let n = 0, avisos = [];
  for (let i = 0; i < nomes.length; i++) {
    // SEM trim: dez abas têm espaço no fim do nome e getSheetByName é literal.
    const nome = String(nomes[i][0] || '');
    if (!nome) { limparBlocoBase_(destino, i); continue; }
    if (!destino.getSheetByName(nome)) {
      // Nome escrito no Painel Geral sem aba correspondente. NÃO apaga: pode
      // ser a aba renomeada à mão, e apagar o bloco levaria junto o trabalho
      // de quem lançou os ambientes. Só avisa.
      avisos.push('linha ' + (FICHA.painelLinha0 + i) + ': "' + nome + '"');
      continue;
    }
    escreverBlocoBase_(destino, i, nome);
    n++;
  }
  SpreadsheetApp.flush();
  ui.alert('Base reconstruída com ' + n + ' projeto(s).'
    + (avisos.length ? '\n\nSem aba correspondente, nada foi apagado:\n'
                       + avisos.join('\n') : ''));
}


// ── auxiliares ──────────────────────────────────────────────────────────

/** Primeira linha livre do Painel Geral, ou -1 se não houver. */
function primeiraVaga_(painel) {
  const n = FICHA.painelLinhaF - FICHA.painelLinha0 + 1;
  const v = painel.getRange(FICHA.painelLinha0, 2, n, 1).getValues();
  for (let i = 0; i < n; i++) {
    if (!String(v[i][0] || '').trim()) return FICHA.painelLinha0 + i;
  }
  return -1;
}

/** Nome de aba dentro de fórmula: aspas simples dobradas. */
function ref_(nome) {
  return "'" + String(nome).replace(/'/g, "''") + "'";
}

/** Escreve as 12 linhas da base do projeto que ocupa o índice i. */
function escreverBlocoBase_(destino, i, nomeAba) {
  const base = destino.getSheetByName(FICHA.base);
  const r0 = FICHA.baseLinha0 + i * FICHA.ambQtd;
  const ab = ref_(nomeAba);
  const linhas = [];

  for (let j = 0; j < FICHA.ambQtd; j++) {
    const r = r0 + j;
    const fr = FICHA.ambLinha0 + j;
    // Nome do projeto como TEXTO e cliente lido da própria ficha. Antes os dois
    // vinham do Painel Geral, e essa dependência prendia o painel dentro da
    // Custo por Projeto: mover o painel quebrava a Base inteira. Igual ao que
    // o atualizar-tudo escreve — os dois têm de escrever a MESMA fórmula, ou a
    // ficha criada pelo botão sai diferente da ficha refeita pelo script.
    const guarda = j === 0 ? ab + '!$A$7' : '$C' + r;
    const linha = [
      '=IF(' + guarda + '="","","' + String(nomeAba).replace(/"/g, '""') + '")',
      '=IF(' + guarda + '="","",' + ab + '!$A$7)',
    ];
    COLS_AMB.forEach(function (c) {
      linha.push('=IF(' + ab + '!$' + c + '$' + fr + '="","",' + ab + '!$' + c + '$' + fr + ')');
    });
    linha.push('=IF($C' + r + '="","",IF(' + ab + '!$F$7="","",' + ab + '!$F$7))');
    // Coordenação e totais do projeto entram SÓ na primeira linha do bloco.
    // Repetidos nas doze, o SUMIFS das planilhas individuais os multiplicaria
    // por doze — foi assim que a comissão do coordenador se perdeu antes.
    if (j === 0) {
      linha.push(cel_(ab, FICHA.coordenador, r, true));
      linha.push(cel_(ab, FICHA.comCoord, r, false));
      linha.push(cel_(ab, FICHA.liquido, r, false));
      linha.push(cel_(ab, FICHA.venda, r, false));
      linha.push(cel_(ab, FICHA.imposto, r, false));
      linha.push(cel_(ab, FICHA.maquina, r, false));
      linha.push(cel_(ab, FICHA.rt, r, false));
      linha.push(cel_(ab, FICHA.vendedor, r, false));
      linha.push(cel_(ab, FICHA.custoVenda, r, false));
      linha.push(cel_(ab, FICHA.custoTotal, r, false));
      linha.push(cel_(ab, FICHA.margem, r, false));
      linha.push(cel_(ab, FICHA.gestorTecnico, r, true));
      linha.push(cel_(ab, FICHA.comGestao, r, false));
      linha.push(cel_(ab, FICHA.vendedorNome, r, true));
      linha.push(cel_(ab, FICHA.comVenda, r, false));
      linha.push(cel_(ab, FICHA.competencia, r, true));
      linha.push(cel_(ab, FICHA.entregaSituacao, r, true));
      linha.push(cel_(ab, FICHA.faturado, r, false));
      linha.push(cel_(ab, FICHA.rtValor, r, false));
      linha.push(cel_(ab, FICHA.rtStatus, r, true));
    } else {
      linha.push('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                 '', '', '', '');
    }
    linhas.push(linha);
  }
  if (!CALIBRADO) {
    // Já aconteceu: fórmula gravada com vírgula numa planilha que quer ponto e
    // vírgula, e a ficha inteira vira #ERROR! sem nenhum aviso. Melhor parar.
    throw new Error('fórmula escrita sem calibrar o separador.');
  }
  base.getRange(r0, 1, FICHA.ambQtd, linhas[0].length)
      .setFormulas(linhas.map(function (lin) { return lin.map(fx_); }));
}

/** Célula do projeto trazida para a base, com o endereço absoluto certo. */
function cel_(ab, ref, r, texto) {
  // guarda é o CLIENTE da ficha, não o ambiente: projeto com venda e sem
  // ambiente lançado precisa aparecer nos painéis
  const abs = '$' + ref.charAt(0) + '$' + ref.slice(1);
  const vazio = texto ? '""' : '0';
  return '=IF(' + ab + '!$A$7="","",IF(' + ab + '!' + abs + '="",' + vazio +
         ',' + ab + '!' + abs + '))';
}

/** Limpa o bloco de um índice que não tem projeto. */
function limparBlocoBase_(destino, i) {
  const base = destino.getSheetByName(FICHA.base);
  const r0 = FICHA.baseLinha0 + i * FICHA.ambQtd;
  base.getRange(r0, 1, FICHA.ambQtd, FICHA.colsBase).clearContent();
}
