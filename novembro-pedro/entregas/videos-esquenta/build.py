import subprocess, os, sys
from PIL import Image, ImageDraw, ImageFont
B='/tmp/claude-0/-home-user-Botanika-Desing/939e42b8-9d13-56a4-bbfb-1c809580e4f3/scratchpad/brutos'
O='/tmp/claude-0/-home-user-Botanika-Desing/939e42b8-9d13-56a4-bbfb-1c809580e4f3/scratchpad/edit'
F='/usr/share/fonts/opentype/inter/'
def f(w,s): return ImageFont.truetype(F+{'black':'InterDisplay-Black.otf','xb':'InterDisplay-ExtraBold.otf','b':'InterDisplay-Bold.otf','sb':'InterDisplay-SemiBold.otf'}[w],s)
BLUE=(12,41,141,255); RED=(226,35,26,255); WHITE=(255,255,255,255); LIME=(200,241,75,255)
W,H=1080,1920

def canvas(): return Image.new('RGBA',(W,H),(0,0,0,0))
def centered(d,y,text,font,fill):
    w=d.textlength(text,font=font); d.text(((W-w)/2,y),text,font=font,fill=fill)

def pill_lines(lines, y, bg, fg, size, weight='black', pad=(34,18), gap=10):
    """stacked rounded boxes, one per line, centered"""
    im=canvas(); d=ImageDraw.Draw(im); fo=f(weight,size)
    for ln in lines:
        w=d.textlength(ln,font=fo); bb=d.textbbox((0,0),ln,font=fo); h=bb[3]-bb[1]
        x0=(W-w)/2-pad[0]; d.rounded_rectangle([x0,y,x0+w+2*pad[0],y+h+2*pad[1]],radius=22,fill=bg)
        d.text(((W-w)/2,y+pad[1]-bb[1]),ln,font=fo,fill=fg); y+=h+2*pad[1]+gap
    return im

def hook(lines,name):   # top, just below the 14% band
    pill_lines(lines,290,WHITE,BLUE,64).save(f'{O}/{name}.png')

def tag(text,name,y=1165):  # product tag
    pill_lines([text],y,BLUE,WHITE,46,'xb').save(f'{O}/{name}.png')

def offer(name):   # offer block above the 35% bottom band
    im=canvas(); d=ImageDraw.Draw(im)
    y=285
    d.rounded_rectangle([110,y,970,y+300],radius=36,fill=BLUE)
    centered(d,y+22,'ESQUENTA 11/11',f('xb',36),LIME)
    centered(d,y+68,'ATÉ 12% OFF',f('black',118),WHITE)
    centered(d,y+214,'frete grátis + cranberry de brinde',f('sb',40),WHITE)
    im.save(f'{O}/{name}.png')

def cta(name):
    pill_lines(['Toque em Comprar agora ↓'],1150,RED,WHITE,52,'black').save(f'{O}/{name}.png')

def endcard(name):
    im=Image.new('RGBA',(W,H),BLUE); d=ImageDraw.Draw(im)
    lg=Image.open(B+'/logo.png').convert('RGBA'); r,g,b,a=lg.split()
    white=Image.new('RGBA',lg.size,WHITE); white.putalpha(a); lg=white.resize((560,int(560*lg.size[1]/lg.size[0])))
    im.alpha_composite(lg,((W-560)//2,420))
    centered(d,620,'ESQUENTA 11/11',f('xb',54),LIME)
    centered(d,700,'ATÉ 12%',f('black',190),WHITE)
    centered(d,900,'OFF',f('black',120),WHITE)
    for i,(t,fo) in enumerate([('8% em 1 un. · 10% a partir de 3 · 12% a partir de 5',f('sb',36)),
                               ('Frete grátis acima de R$ 249',f('sb',40)),
                               ('Cranberry de brinde acima de R$ 400',f('sb',40))]):
        centered(d,1070+i*62,t,fo,WHITE)
    d.rounded_rectangle([250,1290,830,1400],radius=55,fill=RED)
    centered(d,1316,'SÓ ATÉ 10/11',f('black',56),WHITE)
    im.convert('RGB').save(f'{O}/{name}.png')

def render(src, keeps, overlays, out, end='end'):
    mid=src.replace('.mp4','_mid.mp4')
    if not os.path.exists(mid):
        subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vf','scale=1188:2112,fps=30','-c:v','libx264','-preset','veryfast','-crf','14','-c:a','pcm_s16le' if False else 'aac','-b:a','256k',mid],check=True)
    inputs=[]; fc=[]; n=len(keeps)
    for i,(a,b) in enumerate(keeps):
        inputs+=['-ss',str(a),'-t',f'{b-a:.3f}','-i',mid]
        sc='scale=1080:1920' if i%2==0 else 'crop=1080:1920:54:(ih-1920)*0.3'
        fc.append(f"[{i}:v]{sc},setsar=1,setpts=PTS-STARTPTS[v{i}];[{i}:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b-a-0.03:.3f}:d=0.03[a{i}];")
    e=n; inputs+=['-loop','1','-framerate','30','-t','2.2','-i',f'{O}/{end}.png']
    fc.append(f"[{e}:v]format=yuv420p,setsar=1[vend];anullsrc=r=48000:cl=stereo,atrim=0:2.2[aend];")
    fc.append(''.join(f'[v{i}][a{i}]' for i in range(n))+f'[vend][aend]concat=n={n+1}:v=1:a=1[vc][ac];')
    last='vc'
    for j,(png,t0,t1) in enumerate(overlays):
        k=n+1+j; inputs+=['-loop','1','-framerate','30','-t',f'{t1-t0:.2f}','-i',f'{O}/{png}.png']
        fc.append(f"[{k}:v]format=rgba,fade=t=in:st=0:d=0.18:alpha=1,fade=t=out:st={t1-t0-0.15:.2f}:d=0.15:alpha=1,setpts=PTS-STARTPTS+{t0}/TB[o{j}];"
                  f"[{last}][o{j}]overlay=0:0:eof_action=pass[x{j}];")
        last=f'x{j}'
    filt=''.join(fc)+f"[{last}]format=yuv420p[vout];[ac]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]"
    cmd=['ffmpeg','-v','error','-y']+inputs+['-filter_complex',filt,'-map','[vout]','-map','[aout]','-r','30',
         '-c:v','libx264','-preset','medium','-crf','19','-profile:v','high','-pix_fmt','yuv420p','-c:a','aac','-b:a','192k','-movflags','+faststart',out]
    subprocess.run(cmd,check=True)

def remap(keeps,t):
    acc=0
    for a,b in keeps:
        if t<=b: return acc+max(0,t-a)
        acc+=b-a
    return acc
def job(src,keeps,ov,out):
    total=sum(b-a for a,b in keeps)
    o=[(p,round(remap(keeps,t0),2),round(min(remap(keeps,t1),total),2)) for p,t0,t1 in ov]
    print(out,round(total+2.2,1),o); render(src,keeps,o,out)
if __name__=='__main__':
    hook(['Eu desconfiava de','suplemento da internet'],'h1')
    hook(['Isso sai do ar','em poucos dias'],'h2')
    hook(['O empurrão que faltava','pra começar a se cuidar'],'h3')
    tag('Hair Botanika','t_hair'); tag('Creatina + Magnésio Taurato','t_crea'); tag('Hair + Creatina','t_duo')
    offer('offer'); cta('cta'); endcard('end')
    which=sys.argv[1:] or ['1','2','3']
    if '1' in which: job(B+'/c1.mp4',[(0,4.68),(5.12,10.6),(10.85,20.7),(21.06,23.2)],
        [('h1',0,4.6),('t_hair',11.0,15.0),('offer',15.2,20.7),('cta',21.06,23.2)],O+'/Criativo1-editado.mp4')
    if '2' in which: job(B+'/c2.mp4',[(0,6.5),(6.78,16.42),(16.69,23.2)],
        [('h2',0,3.2),('t_crea',9.2,12.5),('offer',12.5,19.0),('cta',19.0,23.2)],O+'/Criativo2-editado.mp4')
    if '3' in which: job(B+'/c3.mp4',[(0,4.39),(4.68,9.74),(10.02,12.16),(12.6,15.19),(15.4,19.64),(19.83,21.19),(21.72,25.18)],
        [('h3',0,4.3),('t_duo',10.05,12.1),('offer',13.5,21.1),('cta',21.72,25.18)],O+'/Criativo3-editado.mp4')
