# Auditoria tema × checkout — Esquenta 11/11 (01/11)

Como foi feito: cópias temporárias das 6 regras, valendo só para um cliente de teste. Os cenários foram calculados com rascunho de pedido e comparados com o que o tema mostra na prévia. No fim, as cópias, o segmento e o cliente de teste foram apagados.

| Carrinho | Checkout (Shopify) | Tema (depois da correção) |
|---|---|---|
| 1 Hair | R$ 91,45 (8%) · frete pago | R$ 91,45 · 8% · faltam R$ 157,55 pro frete |
| 3 Hair | R$ 268,39 (10%) · frete grátis | R$ 268,39 · 10% · frete grátis |
| 5 Hair + cranberry | R$ 437,36 (12%) · frete grátis · cranberry R$ 0 | R$ 437,36 · 12% · cranberry desbloqueado |
| 2 Whey | R$ 271,04 (8%) · frete grátis | R$ 271,04 · 8% · frete grátis |
| 3 Whey + cranberry | R$ 397,72 (10%) · cranberry R$ 0 | R$ 397,72 · 10% · cranberry desbloqueado |
| 4 Whey + cranberry | R$ 518,51 (**12%**: o brinde conta como 5ª unidade) | R$ 518,51 · 12% · "o cranberry de brinde conta na escada" |
| 3 Tri[Mg] | R$ 236,25 (10%) · frete **pago** | R$ 236,25 · faltam R$ 12,75 pro frete |
| 3 Hair + cupom VICTORIA | R$ 262,43 (8% + 2% + 2% de cupom) | o tema não mostra cupom; o cupom só reduz mais |
| 5 Hair + 2 cranberries (recorrente) | as 2 unidades grátis (depois da correção da regra) | o tema adiciona 2 para quem já comprou e está logado |

## O que estava diferente e foi corrigido
1. **Arredondamento:** a Shopify calcula 8% + 2% + 2% separadamente e arredonda cada parte para baixo. O tema calculava 10% de uma vez e mostrava R$ 268,38 (1 centavo a menos que o checkout). Corrigido no tema.
2. **Cranberry:** a Shopify confere os R$ 400 **antes** dos descontos. O tema conferia depois, e dizia "faltam R$ 2,28" quando o cliente já ganhava. Corrigido.
3. **O brinde conta na escada:** o cranberry entra como unidade na contagem da Shopify. Com 4 potes acima de R$ 400, o checkout dá 12%, e o tema mostrava 10%. Corrigido: o tema conta o brinde e avisa o cliente.
4. **2 cranberries para recorrentes:** duas regras de brinde não se somam na Shopify, então o 2º cranberry saía cobrado (R$ 74,20). Agora a regra dos recorrentes dá 2 unidades de uma vez. Testado: as 2 saem grátis.

## Conferido também
- Frete grátis de R$ 249 é contado **depois** dos descontos, igual ao tema.
- Estoque do cranberry: 1.255 unidades, venda bloqueada quando acabar.
- Regras ativas ou agendadas: Upsell.com (app), as 2 do 11/11 e as 6 do Esquenta. Não sobrou nenhum desconto antigo nem de teste.
