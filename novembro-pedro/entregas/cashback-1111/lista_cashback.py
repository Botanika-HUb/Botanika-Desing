"""Lista do cashback 11/11: 100 primeiros pedidos pagos, 15% dos produtos (sem frete).

Entrada: TSV (sem cabeçalho) com as colunas
  pedido, createdAt(UTC), status, cancelledAt, teste, email, customerId, subtotal
subtotal = currentSubtotalPriceSet (produtos já com desconto, sem frete, já descontando reembolso).

Uso:  python3 lista_cashback.py pedidos.tsv saida.csv [limite=100] [pct=15]
Gera o CSV por cliente e um resumo. NÃO aplica nada na loja: as tags só entram com o OK do Pedro.
Os dados de clientes (e-mails) ficam fora do repositório (scratchpad).
"""
import csv
import sys
from collections import OrderedDict

src, out = sys.argv[1], sys.argv[2]
LIM = int(sys.argv[3]) if len(sys.argv) > 3 else 100
PCT = float(sys.argv[4]) if len(sys.argv) > 4 else 15

rows = [r for r in csv.reader(open(src), delimiter='\t') if r]
rows.sort(key=lambda r: r[1])
fora = {'nao_pago': [], 'cancelado': [], 'teste': [], 'sem_cliente': []}
ok = []
for nome, criado, st, canc, teste, email, cid, sub in rows:
    if canc:
        fora['cancelado'].append(nome)
    elif teste.lower() in ('true', '1', 'sim'):
        fora['teste'].append(nome)
    elif st != 'PAID':
        fora['nao_pago'].append(f'{nome} ({st})')
    elif not cid:
        fora['sem_cliente'].append(nome)
    else:
        ok.append((nome, criado, email, cid, float(sub)))

top = ok[:LIM]
cli = OrderedDict()
for nome, criado, email, cid, sub in top:
    c = cli.setdefault(cid, {'email': email, 'pedidos': [], 'base': 0.0})
    c['pedidos'].append(nome)
    c['base'] += sub
for c in cli.values():
    c['centavos'] = round(c['base'] * PCT)  # reais * (pct/100) * 100 centavos
    c['tag'] = f"cashback-1111-{c['centavos']}"

with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['cliente_id', 'email', 'pedidos', 'base_R$', 'cashback_R$', 'tag'])
    for cid, c in cli.items():
        w.writerow([cid, c['email'], ' '.join(c['pedidos']), f"{c['base']:.2f}",
                    f"{c['centavos'] / 100:.2f}", c['tag']])

tot = sum(c['centavos'] for c in cli.values()) / 100
print(f'Pedidos lidos: {len(rows)} | válidos: {len(ok)} | usados: {len(top)} (limite {LIM})')
for k, v in fora.items():
    if v:
        print(f'  fora ({k}): {len(v)} -> {", ".join(v)}')
if top:
    print(f'Do {top[0][0]} ao {top[-1][0]} | clientes: {len(cli)} | cashback total: R$ {tot:.2f}')
rep = [c for c in cli.values() if len(c['pedidos']) > 1]
if rep:
    print('Clientes com mais de 1 pedido (somados):',
          '; '.join('+'.join(c['pedidos']) for c in rep))
