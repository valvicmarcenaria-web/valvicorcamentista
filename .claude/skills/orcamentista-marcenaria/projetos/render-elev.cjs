const {chromium}=require('/opt/node22/lib/node_modules/playwright');
(async()=>{
  const b=await chromium.launch();const p=await b.newPage();
  await p.goto('file://'+__dirname+'/elevacao-escritorio.html',{waitUntil:'networkidle'});
  await p.pdf({path:'elevacao-escritorio.pdf',width:'420mm',height:'297mm',printBackground:true,preferCSSPageSize:true});
  await p.setViewportSize({width:1587,height:1123});
  await p.screenshot({path:'/tmp/elev_preview.png',fullPage:true});
  await b.close();console.log('ok');
})();
