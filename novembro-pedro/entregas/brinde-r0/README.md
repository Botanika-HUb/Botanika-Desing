# Cupom único de influenciadora + brinde a R$ 0 (05/11)

**Problema:** pedidos com 2 cupons de influenciadora (#6990, #7074 e #7127, três dias seguidos).

**Causa raiz:**
- O cupom e o Esquenta eram os dois "desconto no pedido", e precisavam combinar entre si. Assim, 2 cupons também combinavam.
- Qualquer trava por desconto de produto caía no brinde "compre X, ganhe Y", que bloqueia desconto de produto nos itens comprados.

**Solução (testada em 05/11):**
1. **57 cupons de influenciadora** passaram a ser desconto de produto (coleção "[CUPONS] Todos os Produtos"), combinando com pedido e frete, mas **não com outro desconto de produto**. Resultado: 2 cupons digitados = **só 1 aplica**.
   - 55 cupons de 2% e 2 de 5% (DRALUIZA e GABIFLORONUTRI, mantidos em 5% até o Vitor decidir).
2. **O brinde deixou de ser desconto.** Produtos a R$ 0, ocultos (UNLISTED) e publicados na loja virtual:
   - "Cranberry · Brinde": produto 15425724154088, variante 68122684424424;
   - "Coenzima Q10 · Brinde": produto 15425724186856, variante 68122684457192.
3. **Temas:** a lógica do brinde ficou em `bk-bf-skin` (Esquenta e Week) e em `bk-1111` (11/11):
   - qualquer linha do brinde conta como brinde;
   - fora do mínimo, o tema zera o brinde;
   - várias linhas de brinde viram uma só.
4. **Descontos apagados:**
   - 2 de brinde do Esquenta: 1594328088808 e 1594328187112;
   - Q10 do 11/11: 1593617449192;
   - 2 de brinde da Week: 1595622260968 e 1595622293736.

**Temas:**

| Tema | ID | Papel |
|---|---|---|
| ✅ NO AR — Esquenta (brinde R$0, cupom único) | 168360411368 | publicado pelo Pedro em 05/11 |
| 11/11 · TEMA EXCLUSIVO | 168318599400 | já atualizado |
| ESQUENTA BOTANIKA WEEK | 168321417448 | já atualizado |

Os temas antigos foram renomeados "🗑️ APAGAR". Nenhum deles tem o brinde novo, então não devem ser publicados.

**Testes (05/11):**

| Cenário | Resultado |
|---|---|
| DRANAI + JOINGLE | só 1 cupom aplica, e soma com o Esquenta 8% |
| JULIACOLARES + VICTORIA com 5 Hair | só 1 cupom, Esquenta 12% e cranberry grátis |
| Cupom sozinho | ok |

Na prévia do tema:

| Carrinho | O que o tema faz |
|---|---|
| 5 Hair | coloca o brinde |
| 2 Hair | tira o brinde |
| brinde colocado à mão abaixo do mínimo | remove |

**Atenção:**
- (a) Os cupons novos criados pelo Creator Club nascem no formato antigo (desconto no pedido) e voltam a acumular. É preciso converter os novos ou mudar o Creator Club.
- (b) O estoque do brinde não é controlado. A expedição separa o pote normal.
- (c) O RECUPERA5 continua como estava (não combina com outros descontos de pedido nem de produto).
- (d) O desconto do Upsell.com (app) é de produto. Quando ele aparecer, a Shopify escolhe a melhor combinação.
