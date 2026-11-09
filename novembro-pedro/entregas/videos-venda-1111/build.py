"""Vídeos de venda do 11/11 (brutos da Mafe, 09/11).

Um vídeo = uma gravação (sem misturar tomadas de gravações diferentes).
Corta as pausas e o "Roteiro X" do começo, mantém a fala na ordem e põe:
  - faixa fixa no topo;
  - destaques (tags) com "pop", sincronizados com cada trecho da fala;
  - motions: contador de % (0 → 40), contador de R$ (0 → 500), relógio 23:59 com os dois-pontos piscando;
  - foto do produto citado (recorte), entrando de baixo para cima;
  - cartão final com a oferta.

Uso: python3 build.py specs.json R1,R6 [saida_dir]
Os recortes dos produtos ficam em CUT_DIR (PNG com fundo transparente).
"""
import json, os, subprocess, sys

PAD_IN, PAD_OUT = 0.06, 0.12
W, H = 1080, 1920
CARD = 2.6
FPS = 30
CUT_DIR = os.environ.get('CUT_DIR', '/tmp/claude-0/-home-user-Botanika-Desing/939e42b8-9d13-56a4-bbfb-1c809580e4f3/scratchpad/cut')

ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Tag,DejaVu Sans,70,&H00FFFFFF,&H00FFFFFF,&H002B13E3,&H002B13E3,1,0,0,0,100,100,0,0,3,18,0,5,80,80,0,1
Style: Top,DejaVu Sans,54,&H00FFFFFF,&H00FFFFFF,&H000F0B0B,&H000F0B0B,1,0,0,0,100,100,2,0,3,14,0,8,80,80,150,1
Style: Big,DejaVu Sans,200,&H00FFFFFF,&H00FFFFFF,&H002B13E3,&H00000000,1,0,0,0,100,100,0,0,1,12,6,5,40,40,0,1
Style: Lbl,DejaVu Sans,58,&H00FFFFFF,&H00FFFFFF,&H000F0B0B,&H000F0B0B,1,0,0,0,100,100,3,0,3,12,0,5,40,40,0,1
Style: CardBig,DejaVu Sans,118,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,0,0,5,60,60,0,1
Style: CardRed,DejaVu Sans,78,&H00FFFFFF,&H00FFFFFF,&H002B13E3,&H002B13E3,1,0,0,0,100,100,0,0,3,20,0,5,60,60,0,1
Style: CardSmall,DejaVu Sans,50,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,0,0,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

POP = '{\\pos(%d,%d)\\fad(60,140)\\fscx55\\fscy55\\t(0,150,\\fscx112\\fscy112)\\t(150,260,\\fscx100\\fscy100)}'
TAG_Y = 1500   # destaques: faixa de baixo
FX_Y = 1230    # motions grandes: acima do destaque


def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return '%d:%02d:%05.2f' % (h, m, s)


def money(n):
    return 'R$ ' + '{:,}'.format(n).replace(',', '.')


def fx_events(fx, a, b):
    """Eventos ASS de um motion entre a e b (segundos na linha do tempo final)."""
    ev = []
    kind = fx['type']
    a += fx.get('delay', 0.0)
    if kind in ('pct', 'money', 'num'):
        to = fx['to']; ramp = 0.55; steps = int(ramp * FPS / 2)
        lbl = fx.get('label', {'pct': 'ATÉ', 'money': 'ACIMA DE', 'num': ''}[kind])
        fmt = lambda n: ('%d%%' % n) if kind == 'pct' else (money(n) if kind == 'money' else str(n))
        if lbl:
            ev.append((a, b, 'Lbl', '{\\pos(540,%d)\\fad(80,120)}%s' % (FX_Y - 150, lbl)))
        for k in range(steps):
            p = (k + 1) / steps; val = int(round(to * p * (2 - p)))
            t0 = a + k * ramp / steps; t1 = a + (k + 1) * ramp / steps
            ev.append((t0, t1, 'Big', '{\\pos(540,%d)}%s' % (FX_Y, fmt(val))))
        final = fx.get('final', ('%d%% OFF' % to) if kind == 'pct' else fmt(to))
        ev.append((a + ramp, b, 'Big', '{\\pos(540,%d)\\fscx118\\fscy118\\t(0,160,\\fscx100\\fscy100)\\fad(0,140)}%s' % (FX_Y, final)))
        if fx.get('sub'):
            ev.append((a + ramp, b, 'Lbl', '{\\pos(540,%d)\\fad(120,120)}%s' % (FX_Y + 150, fx['sub'])))
    elif kind == 'clock':
        lbl = fx.get('label', 'SÓ ATÉ')
        ev.append((a, b, 'Lbl', '{\\pos(540,%d)\\fad(80,120)}%s' % (FX_Y - 150, lbl)))
        t = a; on = True
        while t < b:
            t1 = min(b, t + 0.5)
            txt = fx.get('time', '23:59') if on else fx.get('time', '23:59').replace(':', ' ')
            pre = '{\\pos(540,%d)\\fscx65\\fscy65\\t(0,180,\\fscx100\\fscy100)}' % FX_Y if t == a else '{\\pos(540,%d)}' % FX_Y
            ev.append((t, t1, 'Big', pre + txt))
            t = t1; on = not on
    return ev


def build(spec, key, out_dir):
    v = spec[key]
    src = v['src']
    segs = [(max(0, a - PAD_IN), b + PAD_OUT) for a, b in v['segs']]
    starts, t = [], 0.0
    for a, b in segs:
        starts.append(t); t += b - a
    total = t
    span = lambda i: (starts[i], starts[i] + segs[i][1] - segs[i][0])
    ev = []
    if v.get('top'):
        ev.append((0, total, 'Top', v['top']))
    for i, txt in v.get('tags', {}).items():
        a, b = span(int(i))
        ev.append((a + 0.05, b, 'Tag', (POP % (540, TAG_Y)) + txt))
    for fx in v.get('fx', []):
        a, b = span(fx['i'])
        ev += fx_events(fx, a, b)
    c0 = total
    ev += [
        (c0, c0 + CARD, 'CardSmall', '{\\pos(540,560)\\fad(150,0)}SÓ HOJE · 11/11'),
        (c0, c0 + CARD, 'CardBig', '{\\pos(540,760)\\fad(150,0)\\fscx70\\fscy70\\t(0,200,\\fscx100\\fscy100)}ATÉ 40% OFF'),
        (c0 + 0.15, c0 + CARD, 'CardRed', '{\\pos(540,960)\\fad(150,0)}FRETE GRÁTIS EM TUDO'),
        (c0 + 0.3, c0 + CARD, 'CardSmall', '{\\pos(540,1130)\\fad(150,0)}Coenzima Q10 de brinde'),
        (c0 + 0.3, c0 + CARD, 'CardSmall', '{\\pos(540,1200)\\fad(150,0)}acima de R$ 500'),
        (c0 + 0.45, c0 + CARD, 'CardSmall', '{\\pos(540,1400)\\fad(150,0)}Termina hoje às 23h59'),
    ]
    ass = os.path.join(out_dir, key + '.ass')
    with open(ass, 'w') as f:
        f.write(ASS_HEAD)
        for a, b, st, txt in ev:
            f.write('Dialogue: 0,%s,%s,%s,,0,0,0,,%s\n' % (ts(a), ts(b), st, txt))

    # 1) corta cada trecho do bruto em 4K para 1080p (um por vez, para não estourar a memória)
    tmp = os.path.join(out_dir, '_' + key); os.makedirs(tmp, exist_ok=True)
    lst = []
    for i, (a, b) in enumerate(segs):
        f = os.path.join(tmp, '%02d.mp4' % i)
        if not os.path.exists(f) or os.environ.get('RECUT'):
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '%.3f' % a, '-i', src, '-t', '%.3f' % (b - a),
                            '-vf', 'scale=%d:%d,setsar=1,fps=%d' % (W, H, FPS),
                            '-af', 'afade=t=in:d=0.02,afade=t=out:st=%.3f:d=0.03,aresample=48000' % max(0, b - a - 0.03),
                            '-c:v', 'libx264', '-preset', 'fast', '-crf', '16', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', f], check=True)
        lst.append("file '%s'" % f)
    open(os.path.join(tmp, 'list.txt'), 'w').write('\n'.join(lst) + '\n')

    # 2) produtos citados: recorte entrando de baixo (0,3 s) e saindo com fade
    prods = v.get('prods', [])
    inputs = ['-f', 'concat', '-safe', '0', '-i', os.path.join(tmp, 'list.txt')]
    fc = '[0:v]tpad=stop_mode=clone:stop_duration=%.2f,' % CARD
    fc += "eq=brightness='if(gte(t,%.3f),-0.32,0)':eval=frame[base];" % total
    last = 'base'
    for k, p in enumerate(prods):
        a, b = span(p['i'])
        t0 = a + p.get('at', 0.0); t1 = min(b, t0 + p.get('dur', 2.4)) if p.get('dur') else b
        d = max(0.6, t1 - t0)
        hgt = p.get('h', 560); x = p.get('x', 700); y = p.get('y', 760)
        inputs += ['-loop', '1', '-t', '%.3f' % d, '-i', os.path.join(CUT_DIR, p['img'] + '.png')]
        n = k + 1
        fc += ('[%d:v]scale=-1:%d,format=rgba,fade=t=in:st=0:d=0.18:alpha=1,fade=t=out:st=%.3f:d=0.2:alpha=1,'
               'setpts=PTS-STARTPTS+%.3f/TB[p%d];' % (n, hgt, max(0, d - 0.2), t0, k))
        fc += ("[%s][p%d]overlay=x=%d-overlay_w/2:y='%d+max(0,1-(t-%.3f)/0.3)*160':eof_action=pass:enable='between(t,%.3f,%.3f)'[o%d];"
               % (last, k, x, y, t0, t0, t0 + d, k))
        last = 'o%d' % k
    fc += "[%s]subtitles='%s'[outv];" % (last, ass)
    fc += '[0:a]apad=pad_dur=%.2f[outa]' % CARD
    out = os.path.join(out_dir, '%s.mp4' % v.get('name', key))
    cmd = ['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', fc, '-map', '[outv]', '-map', '[outa]',
           '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', '-r', str(FPS),
           '-c:a', 'aac', '-b:a', '160k', '-t', '%.3f' % (total + CARD), '-movflags', '+faststart', out]
    subprocess.run(cmd, check=True)
    print(out, round(total + CARD, 2), 's')


if __name__ == '__main__':
    spec = json.load(open(sys.argv[1]))
    out_dir = sys.argv[3] if len(sys.argv) > 3 else '.'
    os.makedirs(out_dir, exist_ok=True)
    for k in sys.argv[2].split(','):
        build(spec, k, out_dir)
