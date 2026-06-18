/* Gerador do orçamento Júnior (Lagoa Santa) — 2 versões (A tudo na cor / B branco interno).
   Fase-1 (cotas ±15%). Importável no validacao-orcamento.html. RT=0 (sem RT). */
const fs = require('fs');
const U15 = 5.0875*0.82, U6 = 5.0875*0.55;

// Biblioteca (preços de compra) — cores do Júnior + Hettich + especiais
const lib = [
 ["MDF", [
   ["mdf branco 6",190],["mdf branco 15",260],["mdf branco 18",320],
   ["MDF cor 15mm (Metallic Suede/Cacao/Areia/Chiaro/Volakas)",500],
   ["MDF cor 6mm",300],["MDF cor 18mm",600],
   ["MDF Ripado Chumbo 18mm (Berneck)",600],
   ["MDF 30mm louçaria (prat+montante)",800],
 ]],
 ["Cola e fita", [
   ["Colagem - mt linear - máquina",2.5],["Colagem - mt linear - manual",4],
   ["Fita de borda - cor - mt",3],["Fita de borda - branco tx - mt",2],
 ]],
 ["Dobradiças", [["Hettich c/ amortecedor",18],["Hettich Sensys",25]]],
 ["Corrediças", [["Hettich oculta soft",150],["Hettich telescópica",40]]],
 ["Puxadores", [["Perfil cava - mt",40]]],
 ["Iluminação", [["LED - fita + perfil - mt",130],["Fonte/driver",80],["Sensor",50]]],
 ["Serralheria/metais", [["Metalon - barra (porta passagem)",100],
   ["Perfil alumínio base - mt",15],["Serralheria cozinha (item)",900]]],
];

// Ambientes: [nome, cor, dev15(m2), share_fechado, terc{vid,ser,est}, led_mt, base_mt, portas_pass, ripado_mt]
const A = [
 ["Cozinha","Metallic Suede",58.4,0.55,{vid:3000,ser:3400,est:0},18,2,0,0],
 ["Sala de TV","Cacao/Areia",28.4,0.40,{vid:800,ser:0,est:0},4,4,2,40],
 ["Quarto de serviço","Itapuã",15.8,0.60,{vid:0,ser:0,est:0},2,0,0,60],
 ["Louçaria + Lavabo","Metallic Suede/Areia",31.4,0.40,{vid:600,ser:0,est:0},6,0,0,0],
 ["Despensa","Metallic Suede",24.2,0.50,{vid:400,ser:0,est:0},4,0,0,0],
 ["Suíte 1","Metallic Suede",30.4,0.20,{vid:1500,ser:0,est:1800},8,4,2,0],
 ["Suíte 2","Metallic/Cacao/Ripado",54.8,0.20,{vid:1500,ser:0,est:1500},8,4,4,150],
 ["Suíte 3","Cacao/Ripado",39.6,0.20,{vid:1500,ser:0,est:1500},8,4,4,150],
 ["Suíte Master","Metallic/Cacao/Volakas/Itapuã",84.0,0.15,{vid:3000,ser:0,est:1800},16,6,4,120],
];

function ambiente(row, branco){
 const [nome,cor,dev15,fech,terc,led,base,pp,rip]=row;
 const ch15 = dev15/U15;
 const ch15cor = branco ? ch15*(1-fech*0.30) : ch15;
 const ch15br  = branco ? ch15*fech*0.30 : 0;
 const fundo6  = (dev15*0.45)/U6;
 let fita = dev15*5.5*1.15 + rip;   // ripado entra régua a régua (extra)
 const q = {
  "MDF¦MDF cor 15mm (Metallic Suede/Cacao/Areia/Chiaro/Volakas)": +ch15cor.toFixed(2),
  "MDF¦mdf branco 6": +fundo6.toFixed(2),
  "Cola e fita¦Fita de borda - cor - mt": Math.round(fita),
  "Cola e fita¦Colagem - mt linear - máquina": Math.round(fita),
  "Dobradiças¦Hettich c/ amortecedor": Math.round(dev15*0.55),
  "Corrediças¦Hettich oculta soft": Math.round(dev15*0.22),
  "Puxadores¦Perfil cava - mt": Math.round(dev15*0.30),
  "Iluminação¦LED - fita + perfil - mt": led,
  "Iluminação¦Fonte/driver": Math.max(1,Math.round(led/6)),
 };
 if (ch15br>0) q["MDF¦mdf branco 15"]= +ch15br.toFixed(2);
 if (rip>0)    q["MDF¦MDF Ripado Chumbo 18mm (Berneck)"]= +(rip/ (U15) *0.06).toFixed(2)+0.5; // ripas (aprox)
 if (nome.startsWith("Louçaria")) q["MDF¦MDF 30mm louçaria (prat+montante)"]=2.5;
 if (base>0)   q["Serralheria/metais¦Perfil alumínio base - mt"]=base;
 if (pp>0)     q["Serralheria/metais¦Metalon - barra (porta passagem)"]=pp*2;
 if (nome==="Cozinha") q["Serralheria/metais¦Serralheria cozinha (item)"]=1;
 return {nome, q, terc:{vid:terc.vid,ser:terc.ser,pin:0,est:terc.est,laq:0}};
}

function build(versaoNome, inv, branco){
 return {
  cliente:"Júnior (Bouganville)", projeto:"Casa Completa — Lagoa Santa",
  versao: versaoNome, inv, mcAlvo:42,
  p:{nf:7,parc:7,vend:5,rt:0,vis:250,outv:0,prog:0.8,coord:1,marc:2.5,serra:0.5,manut:0.5,log:4500,erro:2},
  lib,
  ambientes: A.map(r=>ambiente(r,branco)),
  ativo:0, collapsed:{}, theme:"dark",
  diretrizes:`ORÇAMENTO JÚNIOR (Lagoa Santa) — ${versaoNome}. Fase-1 (cotas ±15%, refinar ambiente a ambiente). `+
   `Ferragens HETTICH (sem versão Hardt). RT=0 (sem RT). Louçaria prat+montante 30mm. `+
   `Interno: ${branco?'BRANCO TX nos armários fechados (closets de vidro reflecta bronze ficam na cor)':'TUDO NA COR'}. `+
   `Portas de passagem = 2x MDF15 + 2 metalon. Perfil de alumínio na base de painéis no chão. `+
   `Pagamento: 30% entrada + 4 boletos (60/90/120/150). Validade 22/06/2026. `+
   `[Vitor, NÃO expor] valorizar mobiliário na cor — a casa é pra vender.`
 };
}

const vB = build("B — Branco interno (fechados)", 370000, true);
const vA = build("A — Tudo na cor", 395000, false);
fs.writeFileSync("projetos/orcamento-junior-vB-branco-interno.json", JSON.stringify(vB,null,2));
fs.writeFileSync("projetos/orcamento-junior-vA-tudo-na-cor.json", JSON.stringify(vA,null,2));
console.log("OK — 2 arquivos gerados.");
console.log("Ambientes:", A.length);
