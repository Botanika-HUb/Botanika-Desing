const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const [cfgPath,outDir,work]=process.argv.slice(2);const cfg=JSON.parse(fs.readFileSync(cfgPath));
 fs.mkdirSync(outDir,{recursive:true});
 // o overlay carrega fontes e imagens da pasta de trabalho
 fs.copyFileSync(path.join(__dirname,'overlay_u.html'),path.join(work,'overlay_u.html'));
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+path.join(work,'overlay_u.html'));await p.evaluate(()=>document.fonts.ready);
 await p.evaluate(c=>setup(c),cfg);
 const N=Math.round(cfg.dur*30);
 for(let f=0;f<N;f++){await p.evaluate(t=>seek(t),f/30);
  await p.screenshot({path:`${outDir}/f${String(f).padStart(5,'0')}.png`,omitBackground:true});}
 await b.close();})();
