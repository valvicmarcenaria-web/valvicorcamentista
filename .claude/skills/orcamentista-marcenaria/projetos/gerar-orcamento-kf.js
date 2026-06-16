/* ============================================================================
 * Gerador do orçamento Kênia & Fábio — casa completa (Lavinia, jun/2026)
 * Produz o JSON importável no validacao-orcamento.html.
 *
 * Método (Fase 1 OLHAR → Fase 2 PREÇO):
 *  - Quantitativo por AMBIENTE, errando para cima (método Valvic).
 *  - Chapas por COR via área desenvolvida ÷ (5,0875 m² × aproveitamento).
 *    Aproveitamento 15/18mm ≈ 0,82 · 6mm ≈ 0,55. q fracionário por ambiente
 *    (arredondamento real é no nível do projeto = otimização geral de corte).
 *  - Fita de cor ≈ 6 m por m² de chapa 15mm (captura portas+gavetas+prateleiras);
 *    colagem (máquina) na mesma metragem.
 *  - Ferragens por contagem (dobradiça por porta; corrediça por gaveta;
 *    sistema correr por roupeiro; RO82 por porta de passagem).
 *  - Terceiros (vidros/espelhos/serralheria de apoio/estofado) por ambiente.
 *  - PEDRA NUNCA ENTRA (regra Jonathan). Marmoraria = cliente.
 *  - Encargos pela planilha real + regra Rodrigo (caixa crítico, projeto grande).
 *  - Preço (inv) calibrado para MC alvo; piso Rodrigo = 40%.
 * ========================================================================== */
const fs = require('fs');
const SEP = '¦'; // ¦
const HTML = '.claude/skills/orcamentista-marcenaria/ferramentas/validacao-orcamento.html';
const html = fs.readFileSync(HTML, 'utf8');
const lib = eval(html.match(/function defaultLib\(\)\{return (\[[\s\S]*?\]);\}/)[1]);

// --- Acrescenta as cores reais do projeto à categoria MDF (descrição clara p/ leitura) ---
const mdf = lib.find(c => c[0] === 'MDF')[1];
mdf.push(['MDF Itapuã 15mm (Duratex)', 500]);
mdf.push(['MDF Itapuã 6mm', 300]);
mdf.push(['MDF Areia 15mm (Guararapes)', 500]);
mdf.push(['MDF Areia 6mm', 300]);
mdf.push(['MDF Azul Profundo 15mm', 500]);
mdf.push(['MDF Azul Profundo 6mm', 300]);
// Branco TX usa as linhas existentes "mdf branco 15"(260) / "mdf branco 6"(190)

// Linha de serralheria de apoio em Especiais já existe ("Estrutura de serralheria",150) — usamos terc.

// --- helpers de conversão ---
const AREA_CHAPA = 5.0875;          // 2750×1850 mm
const APROV15 = 0.82, APROV6 = 0.55;
const ef15 = AREA_CHAPA * APROV15;  // m² úteis por chapa 15mm
const ef6  = AREA_CHAPA * APROV6;   // m² úteis por chapa 6mm
const chapas15 = a => a / ef15;     // FRACIONÁRIO (otimização pool por cor no projeto)
const chapas6  = a => a / ef6;

// nomes exatos das linhas da lib (cor → linha)
const L = {
  itapua15: 'MDF Itapuã 15mm (Duratex)', itapua6: 'MDF Itapuã 6mm',
  areia15:  'MDF Areia 15mm (Guararapes)', areia6: 'MDF Areia 6mm',
  azul15:   'MDF Azul Profundo 15mm',     azul6:  'MDF Azul Profundo 6mm',
  branco15: 'mdf branco 15',              branco6:'mdf branco 6',
  fitaCor:  'Fita de borda - cor - mt',   fitaBco:'Fita de borda - branco tx - mt',
  colagem:  'Colagem - mt linear - máquina',
  dobr:     'Hettich Novisys',            // amortecedor padrão premium acessível
  corrTel:  'Telescópica',                // pendência: oculta? (ver dúvidas)
  ss3:      'SS150 - 3 portas',           trilhoSS3: 'Trilho SS150 - 3mt',
  desemp:   'Desempenador embutido - par',
  ro82:     'Sistema RO82',
  cava:     'Perfil cava RM195 - 3mt',    slim: 'Slim luna rometal',
  led:      'LED - fita + perfil - mt',   sensor: 'Sensor',
  supOcul:  'Suporte oculto',
};
const CAT = { // categoria de cada linha (p/ montar a chave cat¦item)
  [L.itapua15]:'MDF',[L.itapua6]:'MDF',[L.areia15]:'MDF',[L.areia6]:'MDF',
  [L.azul15]:'MDF',[L.azul6]:'MDF',[L.branco15]:'MDF',[L.branco6]:'MDF',
  [L.fitaCor]:'Cola e fita',[L.fitaBco]:'Cola e fita',[L.colagem]:'Cola e fita',
  [L.dobr]:'Dobradiças',[L.corrTel]:'Corrediças',
  [L.ss3]:'Sistema portas roupeiros',[L.trilhoSS3]:'Sistema portas roupeiros',[L.desemp]:'Sistema portas roupeiros',
  [L.ro82]:'Sistema porta de passagem',
  [L.cava]:'Puxadores',[L.slim]:'Puxadores',
  [L.led]:'Iluminação',[L.sensor]:'Iluminação',[L.supOcul]:'Suportes',
};
function qmap(items){ // items: [[linha, quant], ...] -> {cat¦linha: quant}
  const q = {};
  for (const [linha, quant] of items){
    if (!quant) continue;
    const cat = CAT[linha];
    if (!cat){ throw new Error('linha sem categoria: '+linha); }
    q[cat + SEP + linha] = +(+quant).toFixed(3);
  }
  return q;
}
const terc = (vid=0, ser=0, pin=0, est=0, laq=0) => ({vid,ser,pin,est,laq});

/* ===========================================================================
 * AMBIENTES — estimativa por ambiente (área desenvolvida em m², errando p/ cima)
 * Cada ambiente: chapas por cor + fita + colagem + ferragens + LED + terceiros.
 * As áreas vêm das dimensões confirmadas no levantamento (ver .md do projeto).
 * ======================================================================== */
const A = [];
function amb(nome, {a15={}, a6={}, fitaCor=0, fitaBco=0, dobr=0, corr=0,
                    ss3=0, desemp=0, ro82=0, cavaBars=0, slimUn=0, ledM=0,
                    sensores=0, supOcul=0, T=terc(), nota=''}){
  // a15/a6: {cor: m²}  (cor ∈ itapua/areia/azul/branco)
  const items = [];
  const map15 = {itapua:L.itapua15, areia:L.areia15, azul:L.azul15, branco:L.branco15};
  const map6  = {itapua:L.itapua6,  areia:L.areia6,  azul:L.azul6,  branco:L.branco6};
  for (const c in a15) items.push([map15[c], chapas15(a15[c])]);
  for (const c in a6 ) items.push([map6[c],  chapas6(a6[c])]);
  const fitaTotM = fitaCor + fitaBco;
  if (fitaCor) items.push([L.fitaCor, fitaCor]);
  if (fitaBco) items.push([L.fitaBco, fitaBco]);
  if (fitaTotM) items.push([L.colagem, fitaTotM]);
  if (dobr) items.push([L.dobr, dobr]);
  if (corr) items.push([L.corrTel, corr]);
  if (ss3){ items.push([L.ss3, ss3]); items.push([L.trilhoSS3, ss3]); }
  if (desemp) items.push([L.desemp, desemp]);
  if (ro82) items.push([L.ro82, ro82]);
  if (cavaBars) items.push([L.cava, cavaBars]);
  if (slimUn) items.push([L.slim, slimUn]);
  if (ledM) items.push([L.led, ledM]);
  if (sensores) items.push([L.sensor, sensores]);
  if (supOcul) items.push([L.supOcul, supOcul]);
  A.push({nome, q: qmap(items), terc: T, _nota: nota});
}

// 1) COZINHA — M18 forro, M19 ilha, M20 torre eletros, M21 cristaleira, M55, M68
amb('Cozinha', {
  a15:{areia:20, itapua:16}, a6:{areia:8, itapua:4},
  fitaCor:220, dobr:72, corr:16, cavaBars:9, ledM:12, sensores:2,
  T: terc(/*vid*/ 1595), // 4 básculas reflecta bronze R$1.120 + cristaleira R$475 (Renolfh)
  nota:'Bancadas de pedra (Preto São Gabriel) = cliente. Básculas+cristaleira vidro reflecta bronze cotados Renolfh.'
});

// 2) GOURMET — M22 sob bancada, M23 prateleira iluminada, M24 alto ripado
amb('Gourmet', {
  a15:{areia:9}, a6:{areia:3}, fitaCor:60, dobr:18, corr:4, cavaBars:2, ledM:4, sensores:1,
  nota:'Bancada Travertino + muxarabi (serralheiro) = cliente. Ripado 2×2 (M24) puxa fita.'
});

// 3) SALA / ESTAR — M13 sob escada, M14 elevador, M15/M16/M17 painel TV+rack, M27 rack
amb('Sala / Estar', {
  a15:{itapua:24}, a6:{itapua:8}, fitaCor:150, dobr:48, corr:4, cavaBars:5, ledM:5, sensores:1,
  T: terc(0, /*ser*/ 900), // metalon champagne 4 prateleiras curvas M17 (serralheria de apoio)
  nota:'Elevador = terceiro. Metalon champagne M17 = serralheria de apoio (nosso, com markup). Puxador passante.'
});

// 4) LAVANDERIA / SERVIÇO — M07+M08, M09, M10, M11
amb('Lavanderia', {
  a15:{areia:18, itapua:8}, a6:{areia:8, itapua:2}, fitaCor:160, dobr:60, corr:12,
  ss3:1, desemp:3, cavaBars:5, ledM:0,
  T: terc(0, /*ser*/ 300), // arara cromada + calceiro deslizante apoio
  nota:'Bancada granito Preto São Gabriel = cliente. Vão p/ máquina de lavar. M11 piso-teto 3 correr.'
});

// 5) SUBSOLO / GARAGEM / DESPENSA — M01, M02, M12, P06
amb('Subsolo / Despensa', {
  a15:{itapua:4, areia:3, branco:8}, a6:{areia:2, branco:2},
  fitaCor:42, fitaBco:48, dobr:9, corr:3, ro82:2, cavaBars:2,
  nota:'M12 prateleiras Branco TX (confirmar 18 vs 20mm). M01 sob bancada I.S. (pedra B01 = cliente). P06 + M02 portas de passagem.'
});

// 6) LAVABO PISCINA / CIRCULAÇÃO — M25 prateleira, M26 portal ripado escada
amb('Lavabo / Circulação', {
  a15:{itapua:6}, a6:{}, fitaCor:40, cavaBars:1, supOcul:4,
  T: terc(0, /*ser*/ 300), // perfil "L" no piso (serralheria)
  nota:'Portal ripado da escada (M26, pé-direito alto). Muxarabi S02 = serralheiro (cliente).'
});

// 7) SEMISSUÍTE (BANHEIRO) — M35 sob bancada, M36 espelheira  [material já validado ~R$3.445]
amb('Semissuíte (Banheiro)', {
  a15:{areia:6}, a6:{areia:3}, fitaCor:46, dobr:14, corr:3, cavaBars:2, ledM:1.5, sensores:1,
  T: terc(/*vid*/ 1056), // espelho prata ~1,76 m² (M36)
  nota:'Granito Bege Bahia = cliente. Espelheira prof. 10cm. Puxador passante + cava.'
});

// 8) BANHO MASTER — M53 armário espelho+metalon, M54 gabinete ripado
amb('Banho Master', {
  a15:{itapua:10}, a6:{itapua:4}, fitaCor:65, dobr:24, corr:6, cavaBars:3, ledM:3, sensores:1,
  T: terc(/*vid*/ 700, /*ser*/ 900), // espelho prata porta (M53) + quadro metalon 2×2 champagne
  nota:'Bancada Bege Bahia = cliente. Gabinete ripado (M54). LED nas 4 bordas (M53).'
});

// 9) I.S. SUÍTE 01 — M51 prateleira LED, M52 sob bancada, M66 espelheira cristal
amb('I.S. Suíte 01', {
  a15:{azul:5, itapua:2}, a6:{azul:3}, fitaCor:42, dobr:9, corr:6, cavaBars:2, ledM:1.5, sensores:1,
  T: terc(/*vid*/ 600), // espelho cristal moldura preta M66 (LED 4000K)
  nota:'M52 Azul Profundo + puxador Itapuã. Nicho papel. Bancada pedra = cliente.'
});

// 10) QUARTO HÓSPEDES — M03+M04 painel TV, M05 guarda-roupa, M06 cabeceira
amb('Quarto Hóspedes', {
  a15:{areia:10, itapua:8}, a6:{areia:5, itapua:1}, fitaCor:110, dobr:6, corr:4,
  ss3:1, desemp:3, slimUn:3, cavaBars:2, ledM:0,
  T: terc(/*vid*/ 1080), // espelho prata porta central M05 (~1,8 m²)
  nota:'M05 3 portas correr (central espelho prata), slim preto H30. M06 cabeceira frisos 1×1.'
});

// 11) ROUPARIA — M28 armário piso-teto + nicho-cofre
amb('Rouparia', {
  a15:{branco:8}, a6:{branco:3}, fitaBco:50, dobr:12, cavaBars:2,
  nota:'Branco TX. Nicho-cofre (cofre = terceiro do cliente). Tranca + chave.'
});

// 12) SUÍTE 03 — M29 closet, M30 cabeceira curva, M31 sapateira, M32 cortineiro+espelho, M33 escrivaninha, M34 painel/porta
amb('Suíte 03', {
  a15:{areia:18}, a6:{areia:8}, fitaCor:115, dobr:10, corr:14,
  ss3:2, desemp:6, ro82:1, slimUn:3, cavaBars:4, ledM:4, sensores:2,
  T: terc(/*vid*/ 1380), // espelho prata closet M29 (~1080) + espelho película jateada M32 (~300)
  nota:'M29+M30 = 6 portas correr (1 espelho). Sapateira + escrivaninha pé curvo. M34/P06 passagem.'
});

// 13) SUÍTE 02 — M37 closet, M38 cabeceira, M39 sapateira, M40 cortineiro+espelho, M41 escrivaninha, M42 painel/porta
amb('Suíte 02', {
  a15:{areia:18}, a6:{areia:8}, fitaCor:115, dobr:10, corr:14,
  ss3:1, desemp:3, ro82:1, slimUn:3, cavaBars:4, ledM:4, sensores:2,
  T: terc(/*vid*/ 1380), // espelho prata closet M37 + película jateada M40
  nota:'Espelho-irmã da Suíte 03. M37 3 correr (espelho). M40 espelho jateado. M42/P06 passagem.'
});

// 14) SUÍTE 01 (INFANTIL) — M43 GR, M44 cabeceira U, M45 escrivaninha L, M46 baús, M47 escrivaninha, M48 estante metalon, M49 mesa, M50 painel/porta
amb('Suíte 01 (infantil)', {
  a15:{areia:8, itapua:6, azul:8}, a6:{areia:4, azul:3}, fitaCor:140, dobr:12, corr:10,
  ss3:1, desemp:3, ro82:1, slimUn:3, cavaBars:3, ledM:2, sensores:1,
  T: terc(/*vid*/ 1080, /*ser*/ 600, /*pin*/0, /*est*/ 1500), // espelho prata M43 + metalon preto M48 + estofado linho M44
  nota:'Multicor (Areia+Itapuã+Azul Profundo). Baús c/ rodízios. M44 painel estofado linho cinza (confirmar escopo tapeçaria). M48 estante metalon preto.'
});

// 15) SUÍTE MASTER — M56..M65 + M67 (painel curvo, escrivaninha, 3 closets reflecta bronze, painel TV L, racks, cabeceiras, painel porta)
amb('Suíte Master', {
  a15:{areia:22, itapua:14}, a6:{areia:10, itapua:2}, fitaCor:220, dobr:30, corr:12,
  ro82:1, cavaBars:6, ledM:8, sensores:2,
  T: terc(/*vid*/ 12750, /*ser*/ 0), // 3 closets vidro reflecta bronze+estrutura bronze (~3.800 c/u) + espelho bronze M61 (~1.350)
  nota:'AMBIENTE ÂNCORA. M58/M59/M60 = 3 closets piso-teto 3 portas correr vidro reflecta bronze c/ estrutura metálica bronze (vidraçaria+serralheria de apoio, nosso c/ markup). Cabeceira/mesa/painel = Travertino (cliente). Painel TV em L c/ espelho bronze moldura bronze (M61).'
});

/* ===========================================================================
 * ENCARGOS (S.p) — planilha real + regra Rodrigo (jun/2026, caixa crítico)
 * ======================================================================== */
const p = {
  nf: 7,      // nota fiscal (real)
  parc: 7,    // parcelamento máquina/cartão (entrada 40% reduz, mantém 7)
  vend: 5,    // comissão Vitor (closer) em projeto grande
  rt: 10,     // RT arquiteta (Inédita/Flávia) — CONFIRMAR se há parceria (ver dúvidas)
  vis: 250,   // visita
  outv: 0,
  prog: 0.8, coord: 1, marc: 2.5,   // comissões de produção (~4,3% ≈ 5%)
  serra: 0.5, manut: 0.5,
  log: 2000,  // logística da casa inteira (3 pavimentos, vários carretos)
  erro: 2,    // contingência (cobre arredondamento de chapa no pool por cor)
};

/* ===== Cálculo idêntico ao app (compute/suggest) ===== */
function materialAmb(a){ let s=0; lib.forEach(cat=>cat[1].forEach(it=>{ s += (a.q[cat[0]+SEP+it[0]]||0)*it[1]; })); return s; }
function materialTotal(){ return A.reduce((s,a)=>s+materialAmb(a),0); }
function tercAmb(a){ return a.terc.vid+a.terc.ser+a.terc.pin+a.terc.est+a.terc.laq; }
function tercTotal(){ return A.reduce((s,a)=>s+tercAmb(a),0); }
function compute(inv){
  const material=materialTotal(), tc=tercTotal();
  const liq=inv*(1-(p.nf+p.parc)/100);
  const venda=inv*(p.nf+p.vend)/100 + liq*p.rt/100 + inv*p.parc/100 + p.vis + p.outv;
  const operac=liq*(p.prog+p.coord+p.marc)/100 + inv*(p.serra+p.manut)/100 + p.log;
  const erro=inv*p.erro/100;
  const custo=material+tc+venda+operac+erro;
  const mc=inv-custo; const mcPct=inv>0?mc/inv*100:0;
  return {material,tc,venda,operac,erro,custo,mc,mcPct,liq};
}
function suggest(mcAlvo){
  const material=materialTotal(), tc=tercTotal();
  const fixedR=material+tc+p.log+p.vis+p.outv;
  const liqF=1-(p.nf+p.parc)/100;
  const a=(p.nf+p.parc+p.vend+p.erro+p.serra+p.manut)/100;
  const b=(p.prog+p.coord+p.marc+p.rt)/100;
  const mc=mcAlvo/100;
  const denom=1-a-liqF*b-mc;
  return denom>0?fixedR/denom:0;
}

const MC_ALVO = 42;                 // alvo (âncora); piso Rodrigo = 40%
let inv = Math.round(suggest(MC_ALVO)/100)*100;   // arredonda p/ centena
let r = compute(inv);

/* ===== Alocação de preço por ambiente (proporcional a material+terc) ===== */
const baseTot = A.reduce((s,a)=>s+materialAmb(a)+tercAmb(a),0);
const aloc = A.map(a=>{
  const base=materialAmb(a)+tercAmb(a);
  return {nome:a.nome, material:materialAmb(a), terc:tercAmb(a), base,
          preco: Math.round(inv*base/baseTot/100)*100};
});

/* ===== Notas (diretrizes internas + recado Rodrigo) ===== */
const diretrizes =
`ORÇAMENTO CASA COMPLETA — Kênia & Fábio (arq. Inédita/Flávia). ~60 módulos, 3 pavimentos, 15 ambientes.
Levantamento Fase 1 (estimativa que erra p/ cima) — refinar com plano de corte real antes de produção.
REGRA JONATHAN: pedra/marmoraria NUNCA entra (cliente). Bancadas, sóculos e escadas de pedra = fora.
Escopo Valvic: MDF + ferragens + vidros/espelhos dos móveis + serralheria de apoio + LED embutido.
Chapas lançadas FRACIONÁRIAS por ambiente (q) — o arredondamento real é no pool por cor (otimização geral):
  Itapuã/Areia/Azul = "MDF cor" R$500/15mm, R$300/6mm; Branco TX R$260/15mm, R$190/6mm.
Confirmar antes do corte: (1) corrediça telescópica vs oculta (custo/garantia); (2) M12 18 vs 20mm;
(3) RT da arquiteta (10% líq. embutido — se não houver parceria, MC sobe ~+4 pts).`;

const rodrigo =
`Rodrigo (jun/2026, caixa CRÍTICO): projeto grande (>R$80k) -> MC mínima 40% + ENTRADA 40% antes de produção,
parcelas vinculadas a etapas de entrega. Alvo deste orçamento = ${MC_ALVO}% (margem p/ Vitor negociar até o piso 40%).
NÃO ceder abaixo de 40%. Sem entrada real, não fecha. Encargos com NF 7%, parcelamento 7%, comissão Vitor 5%, RT 10%.
ANCORAGEM (Vitor): apresentar o TOTAL da casa primeiro (âncora); só então abrir por ambiente. Pacote completo
otimiza corte/frete -> melhor custo por m² que ambiente avulso. Suíte Master é o ambiente de maior valor (âncora interna).`;

const duvidas = [
  {texto:'Corrediça: telescópica reforçada c/ amortecedor (padrão) ou oculta? Muda custo (40 vs 70/par) e garantia.', para:'Jonathan', cat:'sistema', status:'aberta', decisao:''},
  {texto:'Prateleiras da despensa (M12): manter 20mm do projeto ou padronizar 18mm Valvic?', para:'Jonathan', cat:'material', status:'aberta', decisao:''},
  {texto:'RT da arquiteta (Inédita/Flávia): há parceria com RT de 10%? Se não, retirar (MC sobe ~+4 pts).', para:'Jonathan', cat:'acabamento', status:'aberta', decisao:''},
  {texto:'Painel estofado em linho cinza (M44, cabeceira em U): tapeçaria por conta da Valvic (markup) ou direto do cliente?', para:'Arquiteto', cat:'acabamento', status:'aberta', decisao:''},
];

/* ===== Estado final (formato do app) ===== */
const S = {
  cliente:'Kênia & Fábio', projeto:'Casa Completa', versao:'001',
  inv, mcAlvo:MC_ALVO, p, lib,
  ambientes:A.map(a=>({nome:a.nome, q:a.q, terc:a.terc})),
  ativo:0, collapsed:{}, theme:'dark',
  diretrizes, rodrigo, duvidas,
};

const out='.claude/skills/orcamentista-marcenaria/projetos/orcamento-kenia-fabio-casa-completa.json';
fs.writeFileSync(out, JSON.stringify(S,null,2));

/* ===== Relatório no console ===== */
console.log('=== ORÇAMENTO KÊNIA & FÁBIO — CASA COMPLETA ===');
console.log('Ambientes:', A.length, '| Material total: R$', Math.round(r.material).toLocaleString('pt-BR'),
            '| Terceiros: R$', Math.round(r.tc).toLocaleString('pt-BR'));
console.log('Custo total: R$', Math.round(r.custo).toLocaleString('pt-BR'),
            '('+(r.custo/inv*100).toFixed(1)+'% do inv.)');
console.log('PREÇO (inv): R$', inv.toLocaleString('pt-BR'),
            '| MC: R$', Math.round(r.mc).toLocaleString('pt-BR'), '=', r.mcPct.toFixed(1)+'%');
console.log('Material % do inv.:', (r.material/inv*100).toFixed(1)+'%  | Terc %:', (r.tc/inv*100).toFixed(1)+'%');
console.log('\n--- Alocação por ambiente (proporcional a material+terc) ---');
aloc.sort((x,y)=>y.preco-x.preco).forEach(x=>{
  console.log((x.nome+':').padEnd(26), 'R$', String(x.preco.toLocaleString('pt-BR')).padStart(9),
              ' (mat', Math.round(x.material).toLocaleString('pt-BR'),
              x.terc?'+ terc '+Math.round(x.terc).toLocaleString('pt-BR'):'', ')');
});
const somaAloc=aloc.reduce((s,x)=>s+x.preco,0);
console.log('SOMA alocada: R$', somaAloc.toLocaleString('pt-BR'), '(vs inv', inv.toLocaleString('pt-BR')+')');
console.log('\nArquivo gerado:', out);
// expõe alocação p/ uso posterior
fs.writeFileSync('/tmp/aloc-kf.json', JSON.stringify({inv,mc:r.mcPct,material:r.material,terc:r.tc,aloc},null,2));
