const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+__dirname+'/proposta-apto-cj.html',{waitUntil:'networkidle'});
await p.pdf({path:'proposta-apto-cj.pdf',format:'A4',printBackground:true,preferCSSPageSize:true});
await b.close();console.log('ok');})();
