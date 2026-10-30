import json, subprocess, sys, os
D=os.path.dirname(os.path.abspath(__file__)); BR=D+'/../brutos'
def run(c): subprocess.run(c,check=True)
FIX={'botânica.':'Botanika.','botânica':'Botanika','botânica,':'Botanika,','Botânica,':'Botanika,','Botânica.':'Botanika.','cranell':'cranberry','crambel':'cranberry','grax':'grátis,'}
DROP={'M.','Yeah.'}
HAIR=('HAIR<br>BOTANIKA','cabelos, unhas e pele','hair.png'); CREA=('CREATINA<br>+ TAURATO','creatina + magnésio taurato','crea.png')
JOBS={
 '1':dict(src='c1',keeps=[(0,4.68),(5.12,10.6),(10.85,20.7),(21.06,23.2)],
   hook=dict(lines=['Eu desconfiava de','suplemento da','internet'],em=['internet'],a=0.0,b=2.9),
   zooms=[(0.3,1.1,.14),(9.5,10.5,.12),(14.6,15.25,.12),(21.1,22.1,.14)],
   scenes=[('prod',11.44,12.95,HAIR),('pct',17.0,18.5,None),('gift',19.5,20.75,None)],cta=(21.06,23.2)),
 '2':dict(src='c2',keeps=[(0,6.5),(6.78,16.42),(16.69,23.2)],
   hook=dict(lines=['Isso aqui sai','do ar em','poucos dias'],em=['poucos','dias'],a=0.0,b=2.7),
   zooms=[(0.55,1.7,.14),(7.55,8.35,.12),(18.55,19.45,.12),(21.95,23.1,.14)],
   scenes=[('prod',10.1,11.5,CREA),('pct',12.55,14.2,None),('gift',15.3,16.6,None)],cta=(19.7,23.2)),
 '3':dict(src='c3',keeps=[(0,4.39),(4.68,9.74),(10.02,12.16),(12.6,15.19),(15.4,19.64),(19.83,21.19),(21.72,25.18)],
   hook=dict(lines=['O empurrão','que faltava pra','se cuidar'],em=['empurrão'],a=0.0,b=3.0),
   zooms=[(3.3,4.25,.14),(8.7,9.65,.12),(19.98,20.95,.14),(21.75,22.5,.12)],
   scenes=[('pct',12.64,15.15,None),('gift',18.4,19.6,None)],cta=(21.72,25.18)),
}
END=2.4
def remap(keeps,t):
    acc=0
    for a,b in keeps:
        if t<a: return acc
        if t<=b: return acc+t-a
        acc+=b-a
    return acc
for k in sys.argv[1:] or JOBS:
    j=JOBS[k]; K=j['keeps']; R=lambda t: round(remap(K,t),3)
    main=sum(b-a for a,b in K); dur=round(main+END,2)
    words=[dict(t=R(t),w=FIX.get(w,w)) for t,w in json.load(open(f"{BR}/{j['src']}.words.json")) if w not in DROP and any(a-0.05<=t<=b for a,b in K)]
    scenes=[]
    for kind,a,b,p in j['scenes']:
        s=dict(kind=kind,a=R(a),b=R(b))
        if p: s.update(name=p[0],sub=p[1],img=p[2])
        scenes.append(s)
    cfg=dict(hook=dict(j['hook'],a=R(j['hook']['a']),b=R(j['hook']['b'])),words=words,scenes=scenes,
             hot=['12%','grátis','brinde','presente','desconto','zerar'],cta=dict(a=R(j['cta'][0]),b=R(j['cta'][1])),end=round(main,3),dur=dur)
    json.dump(cfg,open(f'{D}/cfg3_{k}.json','w'),ensure_ascii=False)
    fr=f'{D}/frames3_{k}'
    if not os.path.exists(fr+'/f00000.png'): run(['node',D+'/render3.js',f'{D}/cfg3_{k}.json',fr])
    # zoom curve (output time): smooth punch-ins on emphasis + alternating base zoom per segment to hide jump cuts
    terms=[]
    for a,b,amp in j['zooms']:
        a,b=R(a),R(b); terms.append(f"{amp}*clip((it-{a-0.12})/0.12,0,1)*clip(({b+0.25}-it)/0.25,0,1)")
    acc=0
    for i,(a,b) in enumerate(K):
        if i%2: terms.append(f"0.07*between(it,{acc:.3f},{acc+b-a:.3f})")
        acc+=b-a
    z='1+'+'+'.join(terms)
    mid=f"{BR}/{j['src']}_mid.mp4"; inp=[]; fc=[]; n=len(K)
    for i,(a,b) in enumerate(K):
        inp+=['-ss',str(a),'-t',f'{b-a:.3f}','-i',mid]
        fc.append(f"[{i}:v]setsar=1,setpts=PTS-STARTPTS[v{i}];[{i}:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.02,afade=t=out:st={b-a-0.03:.3f}:d=0.03[a{i}];")
    fc.append(''.join(f'[v{i}][a{i}]' for i in range(n))+f'concat=n={n}:v=1:a=1[vc0][ac0];')
    fc.append(f"[vc0]zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih*0.4-(ih/zoom*0.4)':d=1:s=1080x1920:fps=30,setsar=1[vz];")
    fc.append(f"color=c=0x0c298d:s=1080x1920:r=30:d={END},setsar=1[vend];anullsrc=r=48000:cl=stereo,atrim=0:{END}[aend];[vz][ac0][vend][aend]concat=n=2:v=1:a=1[vc][ac];")
    o=n; inp+=['-reinit_filter','0','-framerate','30','-i',fr+'/f%05d.png']
    fc.append(f"[{o}:v]format=rgba[ov];[vc][ov]overlay=0:0:format=auto,format=yuv420p[vout];")
    sfx=[('whoosh',s['a']-0.08) for s in scenes]+[('pop',s['a']+0.35) for s in scenes if s['kind']=='gift']+[('pop',cfg['cta']['a']),('whoosh',main-0.1)]
    labs=[]
    for q,(nm,t) in enumerate(sfx):
        idx=o+1+q; inp+=['-i',f'{D}/{nm}.wav']; ms=int(max(0,t)*1000)
        fc.append(f"[{idx}:a]adelay={ms}|{ms},volume={0.22 if nm=='pop' else 0.3}[s{q}];"); labs.append(f'[s{q}]')
    fc.append(f"[ac]loudnorm=I=-15:TP=-2:LRA=11,aresample=48000[voz];[voz]{''.join(labs)}amix=inputs={len(labs)+1}:normalize=0:duration=first,alimiter=limit=0.89[aout]")
    out=f'{D}/Criativo{k}-editado-v3.mp4'
    run(['ffmpeg','-v','error','-y']+inp+['-filter_complex',''.join(fc),'-map','[vout]','-map','[aout]','-r','30','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',out])
    print(out,dur)
