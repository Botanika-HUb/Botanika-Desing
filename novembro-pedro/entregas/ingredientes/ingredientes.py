"""Ingredientes de cada produto, do PDF "BOTANIKA_COMPLETO" (catálogo GSA, recebido em 07/11).
Gravado no campo custom.ingredientes de cada produto. Formato: uma linha por cartão, "Título|texto";
"selo|texto" vira uma etiqueta. Texto igual ao do rótulo; só corrigi o que a extração do PDF quebrou
(palavras hifenizadas, "fi" perdido em "gelificante"/"purificada", "edulcorantes" repetido no Cappuccino)."""
import json
G = 'selo|Não contém glúten'
F = {
 'q10': ['Fórmula|Coenzima Q10, estabilizante celulose microcristalina, antiumectantes estearato de magnésio e dióxido de silício',
         'Cápsula|Gelificante gelatina, umectante glicerina, veículo água destilada e carbonato de cálcio', G],
 'nac': ['Fórmula|N-acetil L-cisteína, estabilizante celulose microcristalina, antiumectantes estearato de magnésio e dióxido de silício',
         'Cápsula|Gelificante gelatina, umectante glicerina, veículo água purificada e corantes dióxido de titânio, amarelo crepúsculo FCF, azorrubina, azul brilhante FCF e amarelo quinoleína'],
 'xarope': ['Fórmula|Água, agente de massa sorbitol, acetilcisteína, aroma idêntico ao natural de morango, reguladores de acidez hidróxido de sódio e ácido fosfórico, espessante goma guar, conservantes benzoato de sódio e sorbato de potássio', G],
 'cranberry': ['Fórmula|Cranberry em pó (Vaccinium macrocarpon Aiton), estabilizante celulose microcristalina, antiumectantes estearato de magnésio e dióxido de silício',
         'Cápsula|Gelificante gelatina, umectante glicerol e veículo água destilada, corantes dióxido de titânio, amarelo crepúsculo FCF, azorrubina (carmoisina), azul brilhante FCF e amarelo quinoleína', G],
 'msm': ['Fórmula|Metilsulfonilmetano (MSM), estabilizante celulose microcristalina, antiumectantes estearato de magnésio e dióxido de silício',
         'Cápsula|Gelificante gelatina, umectante glicerol, veículo água purificada e corantes dióxido de titânio, amarelo crepúsculo FCF, azorrubina (carmoisina), azul brilhante FCF e amarelo quinoleína', G],
 'hair': ['Fórmula|L-metionina, acetato de DL-alfa-tocoferol (vitamina E), L-cisteína, ácido ortosilícico estabilizado em cloreto de colina (silício), bisglicinato de zinco, L-selenometionina, bisglicinato ferroso, D-pantotenato de cálcio (vitamina B5), riboflavina (vitamina B2), licopeno de tomate, cloridrato de tiamina (vitamina B1), D-biotina (vitamina B7), iodeto de potássio (iodo), acetato de retinol (vitamina A), estabilizante celulose microcristalina e antiumectantes estearato de magnésio e dióxido de silício',
         'Cápsula|Gelificante gelatina, umectante glicerol, veículo água destilada e carbonato de cálcio'],
 'tri': ['Fórmula|Malato de magnésio, bisglicinato de magnésio, sais de magnésio do ácido cítrico, estabilizante celulose microcristalina, antiumectantes estearato de magnésio e dióxido de silício',
         'Cápsula|Gelificante gelatina, umectante glicerina e veículo água destilada'],
 'creatina': ['Fórmula|Creatina monohidratada, taurato de magnésio e antiumectante dióxido de silício'],
 'sleep': ['Fórmula|Taurato de magnésio, inositol, glicina, camomila em pó (Matricaria recutita L.), lavanda em pó (Lavandula officinalis), taurina, triptofano, maçã em pó (Pyrus malus), melatonina, acidulante ácido cítrico, aroma natural de laranja, corante natural de cúrcuma e edulcorantes glicosídeos de esteviol e taumatina'],
 'vitc': ['Fórmula|Ácido ascórbico (vitamina C), extrato de própolis, quercetina, estabilizante celulose microcristalina, antiumectantes estearato de magnésio e dióxido de silício',
         'Cápsula|Gelificante gelatina, veículo água e carbonato de cálcio'],
 'tetra': ['Fórmula|D-alfa-tocoferol (vitamina E), acetato de retinol (vitamina A), colecalciferol (vitamina D3), menaquinona-7 (vitamina K2) e veículo triglicerídeos de cadeia média (TCM)'],
 'superomega': ['Fórmula|Óleo de peixe 33/22, coenzima Q10, acetato de DL-alfa-tocoferol (vitamina E)',
         'Cápsula|Água purificada, gelificante gelatina, umectantes glicerol e sorbitol, corante carmim e dióxido de titânio'],
 'flexia': ['Fórmula|Sulfato de glucosamina com cloreto de potássio, sulfato de condroitina produzido a partir da fermentação de Escherichia coli, metilsulfonilmetano (MSM), extrato de rizomas de Curcuma longa, colágeno de frango com colágeno tipo II não desnaturado, estabilizante celulose microcristalina, antiumectantes estearato de magnésio e dióxido de silício',
         'Cápsula|Gelificante gelatina, emulsificante glicerina e veículo água destilada, corantes dióxido de titânio, amarelo crepúsculo FCF, azorrubina (carmoisina), azul brilhante FCF e amarelo quinoleína', G],
 'wchoc': ['Fórmula|Proteína de soro do leite concentrada, colágeno hidrolisado C-PURE, cacau em pó, aroma natural de chocolate, espessante goma guar e edulcorantes glicosídeos de esteviol e taumatina', G, 'selo|Contém lactose'],
 'wcap': ['Fórmula|Proteína de soro do leite concentrada, colágeno hidrolisado C-PURE, cacau em pó, aroma natural de cappuccino, espessante goma guar e edulcorantes glicosídeos de esteviol e taumatina', G, 'selo|Contém lactose'],
 'wsem': ['Fórmula|Proteína de soro do leite concentrada, colágeno hidrolisado C-PURE, espessante goma guar e edulcorantes glicosídeos de esteviol e taumatina', G, 'selo|Contém lactose'],
}
def kit(*parts):  # kit: um cartão por produto, com fórmula e cápsula juntas
    out = []
    for name, key in parts:
        f = [l.split('|', 1)[1] for l in F[key] if l.startswith('Fórmula|')][0]
        c = [l.split('|', 1)[1] for l in F[key] if l.startswith('Cápsula|')]
        out.append(f'{name}|{f}' + (f'. Cápsula: {c[0][0].lower() + c[0][1:]}' if c else ''))
    return out
DATA = {
 'coenzima-q10-botanika': F['q10'], 'nac-botanika': F['nac'], 'nac-xarope-40mg-120ml-morango-botanika': F['xarope'],
 'cranberry-botanika': F['cranberry'], 'msm-botanika': F['msm'], 'hair-botanika': F['hair'], 'tri-mg-complex': F['tri'],
 'creatina-monohidratada-magnesio-taurato': F['creatina'], 'sleep-inositol': F['sleep'], 'super-vitamina-c': F['vitc'],
 'tetravit-d': F['tetra'], 'super-omega-3-coq10': F['superomega'], 'flexia-botanika': F['flexia'],
 'whey-balance-chocolate': F['wchoc'], 'whey-balance-910g-chocolate-botanika': F['wchoc'],
 'whey-balance-455g-cappuccino-botanika': F['wcap'], 'whey-balance-sem-sabor': F['wsem'],
 'kit-da-imunidade': kit(('TetraVit D', 'tetra'), ('Super Ômega 3 + CoQ10', 'superomega'), ('Super Vitamina C', 'vitc')),
 'kit-sono-relaxamento': kit(('Sleep Inositol', 'sleep'), ('Tri[Mg] Complex', 'tri')),
 'kit-completo-nac-msm-coq10-cranberry': kit(('NAC', 'nac'), ('MSM', 'msm'), ('Coenzima Q10', 'q10'), ('Cranberry', 'cranberry')),
 'kit-whey-balance-creatina-taurato': kit(('Whey Balance Chocolate', 'wchoc'), ('Whey Balance Cappuccino', 'wcap'), ('Whey Balance Sem Sabor', 'wsem'), ('Creatina + Magnésio Taurato', 'creatina')),
}
if __name__ == '__main__':
    import sys
    ids = json.load(open(sys.argv[1]))
    mf = [dict(ownerId=ids[h], namespace='custom', key='ingredientes', type='multi_line_text_field', value='\n'.join(v)) for h, v in DATA.items()]
    print(json.dumps({'m': mf}, ensure_ascii=False))
