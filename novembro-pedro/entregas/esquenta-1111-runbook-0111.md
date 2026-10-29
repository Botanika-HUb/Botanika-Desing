# Roteiro 01/11 00h05: ofertas do Esquenta 11/11 e cupons de novembro

## Já feito em 29/10 (agendado na Shopify)
- Os 22 descontos automáticos permanentes por quantidade ("2 potes 5%" e "3 potes 10%") terminam em **01/11 00h**.
- 16 cupons terminam em **01/11 00h**: BOTANIKA, ANOVA10, JOELHO5, ORTOP, VOLTA5, VOLTA10, RECUPERA10, RECUPERA10MAIL, RECUPERA10ZAP, LIVE8, Nova Saúde 15%, Nova Saúde frete, Newsletter Ômega 12%, NUTRIMICHELLE, AVALIAY646RF e Grupos WhatsApp Flexia+MSM.
- Fica de fora o app Upsell.com, que continua ativo.

## Por que não deu para criar tudo hoje
A Shopify aceita no máximo **25 descontos automáticos** ativos ou agendados, e a loja está com 23. As 6 regras do Esquenta só cabem depois que as 22 permanentes vencerem em 01/11 00h.

## O que criar em 01/11 00h05 (todas valem de 2026-11-02T03:00Z a 2026-11-10T23:00Z)
Todas com `combinesWith` = pedido, produto e frete **true**.

O teste de 29/10 (rascunho de pedido com cliente de teste) mostrou três coisas:
- Descontos de pedido que acumulam somam sobre a **mesma base**. Por isso 8% + 2% + 2% dá exatamente 8, 10 e 12%.
- O brinde "Compre X, ganhe Y" **não convive com desconto de produto** nos itens que liberam o brinde. Então a escada e os cupons precisam ser **descontos de pedido** (todos os itens).
- O valor mínimo do brinde é conferido depois dos descontos de produto.

| # | Tipo | Título | Regra |
|---|---|---|---|
| 1 | Automático, pedido | Esquenta 11/11 · 8% OFF | 8%, todos os itens, mínimo de 1 unidade |
| 2 | Automático, pedido | Esquenta 11/11 · +2% (3+ un.) | 2%, mínimo de 3 unidades |
| 3 | Automático, pedido | Esquenta 11/11 · +2% (5+ un.) | 2%, mínimo de 5 unidades |
| 4 | Automático, frete grátis | Esquenta 11/11 · Frete grátis acima de R$ 249 | subtotal de R$ 249 ou mais |
| 5 | Automático, compre X ganhe Y | Esquenta 11/11 · Brinde 1 cranberry (novos) | compra de R$ 400 ou mais na coleção `[CUPONS] Todos os Produtos` (gid 450958688488). Leva 1 Cranberry (produto 9633098957032) com 100% de desconto. Limite de 1 por pedido. Segmento: 0 pedidos |
| 6 | Automático, compre X ganhe Y | Esquenta 11/11 · Brinde 2 cranberries (recorrentes) | igual ao 5, mas leva 2 unidades. Segmento: 1 pedido ou mais |

Os segmentos dos itens 5 e 6 ainda precisam ser criados: "Esquenta · clientes novos (0 pedidos)" com `number_of_orders = 0` e "Esquenta · recorrentes (1+ pedidos)" com `number_of_orders >= 1`.

⚠️ **Cliente sem login:** a Shopify só reconhece o segmento depois que o cliente coloca o e-mail no checkout. Até ali, o cranberry adicionado aparece com o preço cheio no carrinho. Alternativa: deixar o brinde de 1 unidade para **todos** (sem segmento) e o de 2 unidades só para recorrentes. Isso precisa ser testado em 01/11, porque para um recorrente os dois brindes podem disputar a mesma unidade.

⚠️ **O brinde conta como unidade na escada:** quem tem 2 unidades pagas acima de R$ 400 ganha o cranberry, fica com 3 unidades e cai nos 10%. Isso precisa ser avisado ao Vitor.

## Cupons de influenciadora (53): em 01/11 00h05 passam para 2%, desconto de pedido, acumulando com tudo
- VICTORIA, BARBIERI, JULIACOLARES, DRROBSON, DRAGIOVANNAE, ANNAMACHADO, LARILESSA, DRAGRACE, DRANAI, JOINGLE, LUCCA, LUDI, LUDMILLA, BRAUHER, ELAINE, DRANAYARAALVIANO, CRISCRUZ, DRALORENA, NATH, ANNANICACIO, ISRAEL, KAMILA, ANADINIZ, CAROLSORRIA, RAFA, ISAPAEL, JUCASTRO, ISABELLE, CLEYARBS, JUDUARTEMENDES, LUISFIG, LEOSIMOES, ANGELABRUNA, SUZANA
- "Creator Botanika": Osvaldo, Larissa Lessa, Ana Amaral, Flávia Teles, FESTEVES, Raquel Cembranelli, Carlos Mateus, Eglife, Kalil, Karynne
- "Creator Club": NUTRICAROL, KEYLLAINDICA, GIUPERSONAL, GABIS, CORREDOR, DRVICTOR, KAMILLA5, MONIKNUTRI, BRUNASC

A lista ainda precisa ser conferida com a Ana (cadastro das influencers).

## Volta em 01/12
- Cupons de influenciadora voltam para 5%, com a configuração de acúmulo que tinham antes (pedido: false, produto e frete: true).
- Os 16 cupons e os 22 descontos permanentes são reativados (tirar a data de fim).
