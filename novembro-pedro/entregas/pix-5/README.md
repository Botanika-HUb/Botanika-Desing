# App de 5% no Pix: pesquisa (09/11, para 10/11)

A loja está no plano **Grow**, não no Plus, e usa o Mercado Pago.

O checkout padrão da Shopify **não dá desconto pela forma de pagamento**, porque o desconto é calculado antes de o cliente escolher como vai pagar. Desconto automático por Pix só é possível no Plus. Fora dele, os apps contornam de três jeitos: com um botão ou cupom no carrinho, com um botão próprio de Pix ou com um checkout de fora da Shopify.

| Opção | Preço | Mercado Pago | Como aplica | Nota | Problema |
|---|---|---|---|---|---|
| **Scala Payment Method Discount** | Grátis na App Store (confirmar) | Sim | No plano Grow, um botão ou cupom no carrinho, antes do pagamento | 5,0 | O cliente pode pegar o desconto e pagar no cartão. Falta saber se o app esconde o cartão |
| SavePay Pix com desconto | Grátis | Sim, com ressalva | Botão próprio de Pix com desconto | 3–4 | Aparecem dois botões de Pix (o do Mercado Pago sem desconto); suporte ruim |
| PagBrasil | Não encontrado | Não: troca de gateway | Pelo gateway | n/d | Sai o Mercado Pago |
| Yampi | 2,5% por pedido, ou R$ 147/mês + 2% | Sim | Checkout fora da Shopify | n/d | Cupons e descontos de quantidade teriam de ser refeitos lá; a Shopify desaconselha |

**Recomendação:** Scala, mas antes:
1. perguntar ao suporte se o app impede pagar no cartão depois de aplicar o desconto;
2. testar se ele soma com o cupom de influenciadora e com o desconto por quantidade (em loja de desenvolvimento ou numa cópia do tema);
3. ter a aprovação de custo do Vitor;
4. só depois mostrar "R$ X no Pix" nas páginas.

Para mostrar "R$ X no Pix" nas páginas de produto e de coleção, nenhum app confirmou que faz isso. Dá para fazer com um trecho no tema (preço × 0,95), sem custo, quando o desconto estiver valendo de verdade.

A sessão não conseguiu abrir apps.shopify.com nem o Mercado Pago, então preço e nota vieram de buscas e de páginas em cache. Confirmar na página de cada app antes de instalar.

Fontes:
- https://apps.shopify.com/scala-desconto-pix-e-boleto
- https://apps.shopify.com/discount-by-payment-method/reviews
- https://community.shopify.com/t/descontos-por-metodo-de-pagamento-como-pix-e-boleto/369321
- https://community.shopify.com/t/desconto-pix-no-checkout-do-mercado-pago/256364
- https://community.shopify.com/t/checkout-yampi-nao-funciona/315601
