const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [cfgPath,outDir,html]=process.argv.slice(2);const cfg=JSON.parse(fs.readFileSync(cfgPath));
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+html);await p.evaluate(()=>document.fonts.ready);await p.evaluate(c=>setup(c),cfg);
 await p.waitForTimeout(500);
 const N=Math.round(cfg.dur*30);
 for(let f=0;f<N;f++){await p.evaluate(t=>seek(t),f/30);
  await p.screenshot({path:`${outDir}/f${String(f).padStart(5,'0')}.png`,omitBackground:true});}
 await b.close();})();
