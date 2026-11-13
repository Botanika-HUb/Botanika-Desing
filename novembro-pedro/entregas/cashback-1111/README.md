# Cashback 11/11: lista dos 100 pedidos (para 12/11, 9h)

## Regra
- **Quem entra:** os 100 primeiros pedidos **pagos** do 11/11, por ordem de criação.
  - Ficam fora os cancelados, os de teste e os não pagos (Pix expirado ou pendente).
- **Quanto:** 15% dos produtos já com desconto, sem frete.
  - A base é o `currentSubtotalPriceSet`, que já desconta reembolsos.
- **Mais de um pedido:** quando a mesma cliente tem vários pedidos entre os 100, os valores são somados e ela recebe uma única tag.
- **Como o crédito chega:** com a tag `cashback-1111-<centavos>`, o Flow "Cashback 11/11" lança o crédito de loja.
  - Validade: 30/11 às 23h59.
  - A cliente recebe um e-mail.
- **Nada é aplicado sem o OK do Pedro.**

## Passo a passo (12/11)
1. Buscar os pedidos na Shopify (Admin GraphQL, só leitura). Pegar todas as páginas.
   - Janela: de 10/11 às 20h a 11/11 às 23h59 (Brasília). A consulta está na seção abaixo.
   - Campos: `name createdAt test cancelledAt displayFinancialStatus email customer{id} currentSubtotalPriceSet{shopMoney{amount}}`.
2. Salvar um TSV no scratchpad, nunca no repositório, porque tem e-mails de clientes.
   - Colunas: `pedido, createdAt, status, cancelledAt, teste, email, customerId, subtotal`.
3. Rodar `python3 lista_cashback.py pedidos.tsv lista.csv 100 15`.
4. Mandar ao Pedro o resumo: quantos pedidos ficaram fora e por quê, o primeiro e o último pedido, o total de cashback e quem tem pedidos somados.
5. Com o OK, aplicar as tags (`tagsAdd` na cliente) e conferir no Flow se os créditos entraram.

## Teste feito em 09/11 (pedidos de 08/11, só leitura)
- 51 pedidos lidos: 44 válidos e 7 fora, todos por Pix expirado. Quando a mesma cliente tinha 2 Pix expirados e 1 pago, só o pago entrou.
- Com o limite em 20, a lista parou no 20º pedido pago.
- Testes com pedidos falsos:
  - cancelado: ficou fora;
  - de teste: ficou fora;
  - repetido da mesma cliente: foi somado, com uma tag só.
- Os dados do teste ficaram fora do repositório.

## Definido pela ficha da oferta do 11/11 (v5, Vitor, 05/11)
- **Janela:** do acesso antecipado em 10/11 às 20h até 11/11 às 23h59.
  - A ficha diz que "os 100 pedidos devem acabar no acesso antecipado".
  - Na consulta: `created_at:>='2026-11-10T23:00:00Z' AND created_at:<'2026-11-12T03:00:00Z'`.
- **100 pedidos, e não 100 clientes.** Quando a mesma cliente faz mais de um pedido, cada pedido ocupa uma vaga, e o valor é somado numa tag só.
