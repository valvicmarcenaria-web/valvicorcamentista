const fs = require('fs');
const ROOT = '/home/user/valvicorcamentista/.claude/skills/closer-vendas/ferramentas/';

// ============ DESCRITIVO (fonte: Doc "PROPOSTA Kênia & Fábio") ============
const AMB = [
  ['Cozinha', [
    ['M18','Painel/forro','Painel fixo integrado ao gesso, com iluminação LED embutida.','Itapuã'],
    ['M19','Armário-ilha','Base com gavetão para lixeira embutida, 2 portas de giro, gavetas e gaveta porta-temperos; recorte para cooktop. Puxador cava usinada.','Areia'],
    ['M20','Torre de eletros','~10 portas de giro + gaveta + 4 básculas de vidro reflecta bronze (articulador de báscula); ventilação para forno/micro-ondas; LED inferior.','Areia + Itapuã'],
    ['M21','Cristaleira piso-teto','7 portas de giro + cristaleira em vidro reflecta bronze, prateleiras de vidro com LED.','Itapuã'],
    ['M55','Armário-ilha complementar','4 portas de giro + 4 gavetas + 4 gavetões.','Areia'],
    ['M68','Mesa','Tampo de bordas curvas.','Itapuã'],
  ]],
  ['Gourmet', [
    ['M22','Armário sob bancada','5 portas de giro + 4 gavetas + gaveta porta-espetos. Puxador cava usinada.','Areia'],
    ['M23','Prateleira iluminada','Com perfil de LED embutido.','Areia'],
    ['M24','Armário alto','Portas ripadas (frisos 2×2) com LED inferior.','Areia'],
  ]],
  ['Sala / Estar', [
    ['M13','Armário sob escada','4 portas de giro escamoteáveis.','Itapuã'],
    ['M14','Painel com porta de giro mimetizada','Tranca e chave; recorte para o elevador.','Itapuã'],
    ['M15','Painel de TV','Piso-teto.','Itapuã'],
    ['M16','Rack ripado suspenso','Cantos curvos R35, portas ripadas, puxador passante, LED 3000K.','Itapuã'],
    ['M17','Estante','4 prateleiras curvas em metalon champagne (serralheria) + LED 3000K em perfil chanfrado.','Itapuã'],
  ]],
  ['Lavabo / Circulação', [
    ['M25','Prateleira (Lavabo Piscina)','Apoio em MDF.','Itapuã'],
    ['M26','Painel com porta de giro mimetizada','Friso 1×1; recorte para elevador. Circulação.','Itapuã'],
    ['M27','Rack ripado','Cantos curvos R20, portas ripadas, puxador passante. Circulação.','Itapuã'],
  ]],
  ['Lavanderia', [
    ['M07','Armário sob bancada','7 gavetões + 2 portas de giro + 1 gaveta; vão para máquina de lavar. Puxador cava usinada.','Areia'],
    ['M08','Armário alto','6 portas de giro + 6 básculas (articulador) + 3 prateleiras curvas.','Areia + Itapuã'],
    ['M09','Armário sob bancada','Cabideiro retrátil + 2 gavetões.','Areia'],
    ['M10','Armário alto','2 nichos vazados + arara cromada.','Itapuã'],
    ['M11','Armário piso-teto','3 portas de correr (trilho), puxador slim preto.','Areia'],
  ]],
  ['Subsolo / Despensa / I.S. Subsolo', [
    ['M01','Armário sob bancada (I.S.)','3 gavetas (1 falsa) + 3 portas de giro. Puxador cava usinada.','Itapuã'],
    ['M02','Porta de correr','—','Areia'],
    ['M12','Prateleiras da despensa','6 prateleiras.','Branco TX'],
  ]],
  ['Rouparia', [
    ['M28','Armário','4 portas de giro + nicho-cofre com tranca e chave.','Branco TX'],
  ]],
  ['Quarto Hóspedes', [
    ['M03','Painel de TV com porta de correr','—','Areia'],
    ['M04','Rack suspenso','Canto curvo R35.','Itapuã'],
    ['M05','Guarda-roupa','3 portas de correr (central em espelho prata), puxador slim preto.','Areia'],
    ['M06','Cabeceira','Frisos 1×1.','Itapuã'],
  ]],
  ['Semissuíte (Banheiro)', [
    ['M35','Armário sob bancada','3 gavetas (1 falsa) + 3 portas de giro.','Areia'],
    ['M36','Espelheira com armário','2 portas de giro espelhadas + 2 fixas em espelho + LED 3000K.','Areia'],
  ]],
  ['Suíte 03', [
    ['M29','Guarda-roupa','3 portas de correr (central espelho prata), puxador slim preto.','Areia'],
    ['M30','Cabeceira curva','LED 3000K.','Areia'],
    ['M31','Sapateira','6 portas de giro + 6 gavetas.','Areia'],
    ['M32','Painel com espelho película jateada','Base em MDF.','Areia'],
    ['M33','Escrivaninha pé curvo','Caixa de tomada embutida.','Areia'],
    ['M34','Painel com porta de correr mimetizada + bandeira','—','Areia'],
  ]],
  ['Suíte 02', [
    ['M37','Guarda-roupa','3 portas de correr (central espelho prata), slim preto.','Areia'],
    ['M38','Cabeceira curva','LED 3000K.','Areia'],
    ['M39','Sapateira','6 portas de giro + 6 gavetas.','Areia'],
    ['M40','Painel com espelho película jateada','—','Areia'],
    ['M41','Escrivaninha pé curvo','Caixa de tomada embutida.','Areia'],
    ['M42','Painel com porta de correr mimetizada + bandeira','—','Areia'],
  ]],
  ['Suíte 01 (Infantil)', [
    ['M43','Guarda-roupa','3 portas de correr (central espelho prata), slim preto.','Areia'],
    ['M44','Cabeceira em "U"','LED 3000K.','Itapuã'],
    ['M45','Armário com tampo em L','Prateleiras + 3 gavetas.','Azul Profundo + Itapuã'],
    ['M46','4 baús de brinquedo','Com rodízios.','Azul Profundo + Itapuã'],
    ['M47','Escrivaninha','3 gavetas + armário 2 portas de giro, caixa de tomada.','Itapuã'],
    ['M48','Estante','Metalon preto, 3 prateleiras chanfradas com LED 3000K.','Azul Profundo'],
    ['M49','Mesa','—','Azul Profundo'],
    ['M50','Painel com porta de correr mimetizada + bandeira','Tranca e chave.','Areia'],
  ]],
  ['I.S. Suíte 01', [
    ['M51','Prateleira com LED embutido','—','Itapuã'],
    ['M52','Armário sob bancada','3 gavetas (1 falsa) + 3 gavetões.','Azul Profundo + Itapuã'],
  ]],
  ['Banho Suíte 01', [
    ['M66','Espelho cristal','Moldura preta, LED frontal 4000K.','—'],
  ]],
  ['Banho Master', [
    ['M53','Armário com porta em espelho prata','Quadro metalon 2×2 champagne + LED.','Itapuã'],
    ['M54','Armário sob bancada','Portas ripadas, 6 gavetas + 4 portas de giro.','Itapuã'],
  ]],
  ['Suíte Master', [
    ['M56','Painel curvo ripado (2×2)','Espelho película jateada com LED frontal.','Areia'],
    ['M57','Escrivaninha','2 gavetas, puxador passante.','Areia'],
    ['M58','Closet piso-teto','3 portas de correr em vidro reflecta bronze + sapateiras.','Areia'],
    ['M59','Closet piso-teto','3 portas de correr em vidro reflecta bronze, calceiro + 2 araras.','Areia'],
    ['M60','Closet piso-teto','3 portas de correr em vidro reflecta bronze, 2 gavetas calceiro + 2 araras.','Areia'],
    ['M61','Painel de TV em L','Frisos e moldura em bronze.','Itapuã'],
    ['M62','Rack','Canto curvo R20, 5 portas de giro, puxador passante.','Areia'],
    ['M63','Painel ripado (2×2)','—','Itapuã'],
    ['M64/M65','Mesas de cabeceira','Borda R5, 1 gaveta com puxador passante, caixa de tomada.','Itapuã'],
    ['M67','Painel piso-teto com porta de correr','—','Areia'],
  ]],
  ['Serralheria de Apoio', [
    ['S01','Muxarabi piso-teto (5×5)','Estrutura metálica 2×2 + 6 prateleiras, pintura Coral Cinza Intenso (Gourmet).','—'],
    ['S02','Muxarabi no teto (5×5)','Coral Cinza Intenso (Lavabo Piscina).','—'],
  ]],
];

const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const totalItens = AMB.reduce((a,[,it])=>a+it.length,0);

// ---- paginação determinística em páginas A4 ----
function itemH(desc){ return 24 + Math.ceil((desc.length||1)/56)*15; }
function buildDescr(client, project, specsLine, vals = {}){
  const PAGE = 1000, FIRST = 1000 - 175;
  const pages = []; let cur = []; let rem = FIRST;
  for (const [name, items] of AMB){
    let gh = 38; for (const it of items) gh += itemH(it[3]);
    if (gh > rem && cur.length){ pages.push(cur); cur = []; rem = PAGE; }
    cur.push([name, items]); rem -= gh;
  }
  if (cur.length) pages.push(cur);

  return pages.map((groups, pi) => {
    const head = pi === 0 ? `
      <div class="descr-head">
        <div class="eyebrow">O Projeto · Descritivo Técnico</div>
        <div class="descr-title">O que vamos<br>executar para vocês.</div>
        <div class="descr-sub">${esc(client)} &nbsp;—&nbsp; ${esc(project)}</div>
        <div class="descr-specs">${specsLine}</div>
      </div>` : `
      <div class="descr-cont"><span>Descritivo técnico</span><span class="descr-cont-pg">continuação</span></div>`;
    const body = groups.map(([name, items]) => `
      <div class="amb-group">
        <div class="amb-head"><div class="amb-title">${esc(name)}</div><div class="amb-count">${items.length} ${items.length>1?'itens':'item'}</div>${vals[name]?`<div class="amb-val">R$ ${esc(vals[name])}</div>`:''}</div>
        ${items.map(([code,nm,desc,cor]) => `
          <div class="d-item">
            <div class="d-code">${esc(code)}</div>
            <div class="d-body"><span class="d-name">${esc(nm)}</span>${desc&&desc!=='—'?` — <span class="d-desc">${esc(desc)}</span>`:''}</div>
            ${cor&&cor!=='—'?`<div class="d-cor">${esc(cor)}</div>`:''}
          </div>`).join('')}
      </div>`).join('');
    return `<section class="page descr">${head}<div class="descr-body">${body}</div></section>`;
  }).join('\n');
}

// ---- CSS do descritivo ----
const DESCR_CSS = `
    /* ===== DESCRITIVO ===== */
    .descr { background: var(--warm-wh); display: block; padding: 0; }
    .descr-head { padding: 52px 56px 18px; }
    .descr-title { font-family: var(--fd); font-size: 40px; font-weight: 400; color: var(--graphite); line-height: 1.05; margin-top: 8px; }
    .descr-sub { font-family: var(--fd); font-size: 15px; font-style: italic; color: var(--muted); margin-top: 8px; }
    .descr-specs { font-family: var(--fm); font-size: 9px; letter-spacing: .08em; color: var(--gold); text-transform: uppercase; margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--gold-20); }
    .descr-cont { padding: 48px 56px 10px; display: flex; justify-content: space-between; align-items: baseline; border-bottom: 1px solid var(--gold-20); margin: 0 56px 8px; padding: 48px 0 8px; }
    .descr-cont span { font-family: var(--fb); font-size: 9px; letter-spacing: .28em; text-transform: uppercase; color: var(--gold); }
    .descr-cont-pg { color: var(--muted) !important; }
    .descr-body { padding: 14px 56px 48px; }
    .amb-group { break-inside: avoid; page-break-inside: avoid; margin-bottom: 20px; }
    .amb-head { display: flex; align-items: baseline; gap: 12px; border-bottom: 1px solid var(--graphite-15); padding-bottom: 6px; margin-bottom: 9px; }
    .amb-title { font-family: var(--fd); font-size: 17px; font-weight: 600; color: var(--graphite); letter-spacing: .04em; text-transform: uppercase; }
    .amb-count { font-family: var(--fm); font-size: 9px; color: var(--gold); letter-spacing: .04em; }
    .amb-val { font-family: var(--fm); font-size: 10.5px; font-weight: 700; color: var(--graphite); margin-left: auto; letter-spacing: -.01em; }
    .d-item { display: flex; gap: 14px; padding: 5px 0; align-items: baseline; }
    .d-code { font-family: var(--fm); font-size: 10px; font-weight: 700; color: var(--gold); min-width: 46px; flex-shrink: 0; }
    .d-body { flex: 1; font-size: 11.5px; line-height: 1.5; }
    .d-name { font-weight: 600; color: var(--graphite); }
    .d-desc { color: var(--muted); }
    .d-cor { font-family: var(--fm); font-size: 8px; color: var(--gold); text-transform: uppercase; letter-spacing: .06em; white-space: nowrap; flex-shrink: 0; padding-top: 2px; }
    @media print { .descr { page-break-after: always; } }

    /* ===== INVESTIMENTO K&F ===== */
    .inv-warn { background: var(--gold-10); border: 1px solid var(--gold-40); border-radius: 3px; padding: 11px 16px; font-size: 11px; color: var(--graphite); margin-bottom: 20px; line-height: 1.5; }
    .inv-warn b { color: var(--gold); }
    .ver-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 22px; }
    .ver-card { border: 1px solid var(--gold-20); border-radius: 3px; padding: 18px 20px; position: relative; }
    .ver-card.hi { border: 1.5px solid var(--gold); background: var(--gold-10); }
    .ver-tag { font-size: 8px; font-weight: 600; letter-spacing: .2em; text-transform: uppercase; color: var(--gold); margin-bottom: 8px; }
    .ver-name { font-family: var(--fd); font-size: 22px; font-weight: 500; color: var(--graphite); margin-bottom: 6px; }
    .ver-desc { font-size: 10.5px; color: var(--muted); line-height: 1.5; margin-bottom: 14px; min-height: 46px; }
    .ver-price { font-family: var(--fm); font-size: 22px; font-weight: 700; color: var(--graphite); letter-spacing: -.01em; }
    .ver-card.hi .ver-price { color: var(--gold); }
    .inv-foot { font-size: 9.5px; color: var(--muted); line-height: 1.6; margin-top: 14px; padding-top: 12px; border-top: 1px solid var(--gold-20); }
`;

// ---- investimento K&F (por documento) ----
function buildInv(cfg){
  return `<div class="inv-body">
    <div class="inv-warn"><b>⚠ Reajuste de tabela em julho/2026.</b> Fechando dentro da validade, vocês garantem os valores desta proposta.</div>

    <div class="ver-grid">
      <div class="ver-card hi">
        <div class="ver-tag">Recomendada</div>
        <div class="ver-name">Tudo na cor</div>
        <div class="ver-desc">Interior dos armários acompanha o amadeirado das frentes — sensação de peça maciça, contínua, sofisticada ao abrir.</div>
        <div class="ver-price">R$ ${cfg.precoCor}</div>
      </div>
      <div class="ver-card">
        <div class="ver-tag">Mais enxuta</div>
        <div class="ver-name">Branco interno</div>
        <div class="ver-desc">Interior em Branco TX — uso mais claro e funcional, amadeirado nas frentes. Mesma marcenaria e mesma ferragem.</div>
        <div class="ver-price">R$ ${cfg.precoBranco}</div>
      </div>
    </div>

    <div class="pay-block">
      <div class="pay-label">Condições de pagamento</div>
      <table class="pay-tbl">
        <tbody>
          <tr><td>40% na assinatura do contrato</td><td>entrada</td></tr>
          <tr><td>30% na entrega da 1ª etapa</td><td>ambientes definidos com vocês</td></tr>
          <tr><td>30% na entrega final</td><td>conclusão</td></tr>
        </tbody>
      </table>
    </div>

    <div class="meta-row">
      <div class="meta-card mc-navy"><div class="mc-label">Prazo de entrega</div><div class="mc-val">90–100</div><div class="mc-sub">dias · validade 3 dias</div></div>
      <div class="meta-card mc-gold"><div class="mc-label">Garantia</div><div class="mc-val">${cfg.garantia} anos</div><div class="mc-sub">ferragens ${cfg.ferragem}</div></div>
      <div class="meta-card mc-cream"><div class="mc-label">Validade dos valores</div><div class="mc-val">10</div><div class="mc-sub">dias corridos</div></div>
    </div>

    <p class="inv-foot"><b>Escopo Valvic:</b> marcenaria sob medida · ferragens · vidros e espelhos dos móveis · serralheria de apoio · iluminação LED embutida. (Pedra/marmoraria por conta do cliente.)</p>

    <div class="cta-row">
      <div>
        <h3>Qual o próximo passo?</h3>
        <p>Podemos apresentar a proposta pessoalmente e tirar todas as dúvidas. Estamos à disposição para tornar o projeto da Flávia realidade.</p>
      </div>
    </div>
  </div><!-- /inv-body -->`;
}

// ============ CONFIGS DOS 2 DOCUMENTOS ============
const CLIENT = 'Kênia & Fábio';
const PROJECT = 'Casa Completa · 3 pavimentos · Arquiteta Inédita / Flávia';
const DEPO = {
  txt: 'Eu estou apaixonada... e não é só pela beleza... mas o comprometimento e dedicação desde o orçamento, até execução e entrega. Indico de olhos fechados!!! Muitíssimo obrigada...',
  autor: 'Graciene', proj: 'Vale dos Cristais', cap: 'Projeto executado · Vale dos Cristais',
  url: 'https://lh3.googleusercontent.com/d/1MsmhniA_z1HXRBw_bQ7D-VgujrDDxLNH=w1600'
};

// Valores por ambiente (fonte: Lavinia, rateio proporcional ao custo, arredondado a R$500)
// Referência: versão "Tudo na cor" de cada linha (V2 para Premium, V4 para Essencial)
const VALS_PREMIUM = {
  'Cozinha':                           '43.500',
  'Gourmet':                           '12.500',
  'Sala / Estar':                      '23.500',
  'Lavabo / Circulação':               '6.500',
  'Lavanderia':                        '28.500',
  'Subsolo / Despensa / I.S. Subsolo': '11.500',
  'Rouparia':                          '6.000',
  'Quarto Hóspedes':                   '21.000',
  'Semissuíte (Banheiro)':             '12.500',
  'Suíte 03':                          '32.000',
  'Suíte 02':                          '28.500',
  'Suíte 01 (Infantil)':               '33.500',
  'I.S. Suíte 01':                     '13.500',
  'Banho Master':                      '18.000',
  'Suíte Master':                      '68.000',
};
const VALS_ESSENCIAL = {
  'Cozinha':                           '39.000',
  'Gourmet':                           '12.000',
  'Sala / Estar':                      '23.000',
  'Lavabo / Circulação':               '6.500',
  'Lavanderia':                        '26.500',
  'Subsolo / Despensa / I.S. Subsolo': '11.000',
  'Rouparia':                          '6.000',
  'Quarto Hóspedes':                   '20.500',
  'Semissuíte (Banheiro)':             '12.000',
  'Suíte 03':                          '30.000',
  'Suíte 02':                          '26.500',
  'Suíte 01 (Infantil)':               '32.000',
  'I.S. Suíte 01':                     '12.500',
  'Banho Master':                      '17.000',
  'Suíte Master':                      '65.500',
};

const DOCS = [
  {
    out: 'proposta-kenia-fabio-premium.html', tmpl: 'proposta-excellence.html',
    sk: 'valvic_kf_premium', badge: 'Premium · Hettich', ferragem: 'Hettich',
    garantia: '10', precoCor: '359.000', precoBranco: '345.000',
    specsLine: 'Ferragens Hettich · MDF 18mm · Amadeirado Itapuã / Areia · Laca · Garantia 10 anos',
    vals: VALS_PREMIUM,
  },
  {
    out: 'proposta-kenia-fabio-essencial.html', tmpl: 'proposta-essencial.html',
    sk: 'valvic_kf_essencial', badge: 'Essencial · Hardt', ferragem: 'Hardt',
    garantia: '5', precoCor: '340.000', precoBranco: '317.000',
    specsLine: 'Ferragens Hardt · MDF 18mm · Amadeirado Itapuã / Areia · Laca · Garantia 5 anos',
    vals: VALS_ESSENCIAL,
  },
];

for (const cfg of DOCS){
  let html = fs.readFileSync(ROOT + cfg.tmpl, 'utf8');

  // 1) injeta CSS do descritivo + investimento antes do </style>
  html = html.replace('</style>', DESCR_CSS + '\n  </style>');

  // 2) reordena: linha do tempo (p4) vem ANTES do descritivo
  //    extrai p4, remove-o do lugar original, injeta antes do descritivo na posição de p3
  const descrPages = buildDescr(CLIENT, PROJECT, cfg.specsLine, cfg.vals);
  const p4Match = html.match(/<section class="page" id="p4">[\s\S]*?<\/section>/);
  const p4Html = p4Match ? p4Match[0] : '';
  html = html.replace(/<section class="page" id="p4">[\s\S]*?<\/section>/, '');
  html = html.replace(/<section class="page" id="p3">[\s\S]*?<\/section>/, p4Html + '\n' + descrPages);

  // 3) substitui o conteúdo do investimento
  html = html.replace(/<div class="inv-body">[\s\S]*?<\/div><!-- \/inv-body -->/, buildInv(cfg));

  // 4) DEFAULTS K&F
  const defaults = `const DEFAULTS = {
    NOME_CLIENTE:   '${CLIENT}',
    PROJETO:        '${PROJECT}',
    DATA_PROPOSTA:  '17/06/2026',
    FERRAGEM:       '${cfg.ferragem}',
    MATERIAL:       'MDF 18mm',
    ACABAMENTO:     'Amadeirado + Laca',
    DEPOIMENTO:     '${DEPO.txt}',
    DEP_AUTOR:      '${DEPO.autor}',
    DEP_PROJETO:    '${DEPO.proj}',
    DEP_CAPTION:    '${DEPO.cap}',
    PRAZO:          '90',
    GARANTIA_ANOS:  '${cfg.garantia}',
    HERO_URL:       'https://lh3.googleusercontent.com/d/1tIPkB_fxt1DYWHcj3-s5tdVyM7jocaTa=w1600',
    P2_URL:         'https://lh3.googleusercontent.com/d/1SQriQN8H4RD2yjHQoLm84HQ65DCoQE1p=w1600',
    P4_URL:         'https://lh3.googleusercontent.com/d/1-viTHOJ1WZz9fJTX4PmUoADpZcf1ZOVR=w1600',
    P5_URL:         '${DEPO.url}',
  };`;
  html = html.replace(/const DEFAULTS = \{[\s\S]*?\};/, defaults);

  // 5) storage key, badge, título, meta-ref
  html = html.replace(/const SK = '[^']*';/, `const SK = '${cfg.sk}';`);
  html = html.replace(/<span class="badge">[^<]*<\/span>/, `<span class="badge">${cfg.badge}</span>`);
  html = html.replace(/<title>[^<]*<\/title>/, `<title>Valvic — Proposta Kênia &amp; Fábio (${cfg.badge})</title>`);
  html = html.replace(/<div class="meta-ref">[^<]*<\/div>/, `<div class="meta-ref">Ref. ${cfg.badge}</div>`);

  fs.writeFileSync(ROOT + cfg.out, html);
  console.log('OK', cfg.out, '· descritivo:', totalItens, 'itens');
}
