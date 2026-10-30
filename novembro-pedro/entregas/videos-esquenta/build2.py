import json, subprocess, sys, os
D=os.path.dirname(os.path.abspath(__file__)); BR=D+'/../brutos'
def run(c): subprocess.run(c,check=True)
# sfx: soft pop + airy whoosh (synthesized, no third-party audio)
if not os.path.exists(D+'/pop.wav'):
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i',"aevalsrc='0.6*sin(2*PI*(520-2600*t)*t)*exp(-38*t)':s=48000:d=0.18",'-ac','2',D+'/pop.wav'])
    run(['ffmpeg','-v','error','-y','-f','lavfi','-i',"anoisesrc=d=0.45:c=pink:a=0.5:r=48000",'-af',"bandpass=f=1800:w=1400,afade=t=in:d=0.18,afade=t=out:st=0.2:d=0.25,volume=0.7",'-ac','2',D+'/whoosh.wav'])
JOBS={
 '1':dict(src='c1',keeps=[(0,4.68),(5.12,10.6),(10.85,20.7),(21.06,23.2)],
   hook=dict(lines=['Eu desconfiava de','suplemento da internet'],em=['internet'],a=0.05,b=4.5),
   tag=dict(text='Hair Botanika',a=10.31,b=14.2),offer=dict(a=14.51,b=19.9),cta=dict(a=20.01,b=22.0)),
 '2':dict(src='c2',keeps=[(0,6.5),(6.78,16.42),(16.69,23.2)],
   hook=dict(lines=['Isso sai do ar','em poucos dias'],em=['poucos','dias'],a=0.05,b=3.2),
   tag=dict(text='Creatina + Magnésio Taurato',a=8.92,b=12.1),offer=dict(a=12.22,b=18.35),cta=dict(a=18.45,b=22.5)),
 '3':dict(src='c3',keeps=[(0,4.39),(4.68,9.74),(10.02,12.16),(12.6,15.19),(15.4,19.64),(19.83,21.19),(21.72,25.18)],
   hook=dict(lines=['O empurrão que faltava','pra começar a se cuidar'],em=['empurrão'],a=0.05,b=4.25),
   tag=dict(text='Hair + Creatina',a=9.48,b=11.45),offer=dict(a=12.49,b=19.6),cta=dict(a=19.78,b=23.1)),
}
END=2.4
for k in sys.argv[1:] or JOBS:
    j=JOBS[k]; mid=f"{BR}/{j['src']}_mid.mp4"; main=sum(b-a for a,b in j['keeps']); dur=round(main+END,2)
    cfg=dict(hook=j['hook'],tag=j['tag'],offer=j['offer'],cta=j['cta'],end=round(main,3),dur=dur)
    json.dump(cfg,open(f'{D}/cfg{k}.json','w'),ensure_ascii=False)
    fr=f'{D}/frames{k}'; run(['node',D+'/render.js',f'{D}/cfg{k}.json',fr])
    inp=[]; fc=[]; n=len(j['keeps'])
    for i,(a,b) in enumerate(j['keeps']):
        inp+=['-ss',str(a),'-t',f'{b-a:.3f}','-i',mid]
        sc='scale=1080:1920' if i%2==0 else 'crop=1080:1920:54:(ih-1920)*0.3'
        fc.append(f"[{i}:v]{sc},setsar=1,setpts=PTS-STARTPTS[v{i}];[{i}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={b-a-0.03:.3f}:d=0.03[a{i}];")
    fc.append(f"color=c=0x0c298d:s=1080x1920:r=30:d={END},setsar=1,format=yuv420p[vend];anullsrc=r=48000:cl=stereo,atrim=0:{END}[aend];")
    fc.append(''.join(f'[v{i}][a{i}]' for i in range(n))+f'[vend][aend]concat=n={n+1}:v=1:a=1[vc][ac];')
    o=n; inp+=['-framerate','30','-i',fr+'/f%05d.png']
    fc.append(f"[{o}:v]format=rgba[ov];[vc][ov]overlay=0:0:format=auto,format=yuv420p[vout];")
    sfx=[('pop',j['tag']['a']),('whoosh',j['offer']['a']-0.1),('pop',j['offer']['a']+0.15),('pop',j['cta']['a']),('whoosh',main-0.1)]
    labs=[]
    for q,(nm,t) in enumerate(sfx):
        idx=o+1+q; inp+=['-i',f'{D}/{nm}.wav']; ms=int(max(0,t)*1000)
        fc.append(f"[{idx}:a]adelay={ms}|{ms},volume={0.22 if nm=='pop' else 0.3}[s{q}];"); labs.append(f'[s{q}]')
    fc.append(f"[ac]loudnorm=I=-15:TP=-2:LRA=11,aresample=48000[voz];[voz]{''.join(labs)}amix=inputs={len(labs)+1}:normalize=0:duration=first,alimiter=limit=0.89[aout]")
    out=f'{D}/Criativo{k}-editado-v2.mp4'
    run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',''.join(fc),'-map','[vout]','-map','[aout]','-r','30','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',out])
    print(out,dur)
