"""Lista os trechos de fala de um vídeo (RMS em janelas de 50 ms).
Uso: python3 bursts.py video.mp4 [limiar_dB=-38] [pausa_min=0.25]"""
import sys, struct, math, subprocess
src = sys.argv[1]; th = float(sys.argv[2]) if len(sys.argv) > 2 else -38; gap = float(sys.argv[3]) if len(sys.argv) > 3 else 0.25
d = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout
n = len(d) // 2; a = struct.unpack('<%dh' % n, d); w = 800
lv = []
for i in range(0, n, w):
    c = a[i:i + w]; r = math.sqrt(sum(x * x for x in c) / len(c)) or 1
    lv.append(20 * math.log10(r / 32768))
segs = []; cur = None; quiet = 0
for k, v in enumerate(lv):
    t = k * 0.05
    if v > th:
        if cur is None: cur = [t, t + 0.05]
        else: cur[1] = t + 0.05
        quiet = 0
    elif cur is not None:
        quiet += 0.05
        if quiet >= gap: segs.append(cur); cur = None
if cur: segs.append(cur)
segs = [s for s in segs if s[1] - s[0] >= 0.15]
for s in segs: print('%.2f %.2f' % (s[0], s[1]))
