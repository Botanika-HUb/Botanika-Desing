# Auditoria de descontos — Botanika — 17/09/2026

Levantamento completo das regras de desconto ativas e de como elas se
comportam **de verdade**. Nada foi alterado para produzir este documento.

Método: além de ler a configuração, cada combinação foi **simulada** com
`draftOrderCalculate` (a mesma engine de desconto do checkout) e conferida
contra os pedidos reais do dia.

---

## 1. A regra que explica tudo

**Cada unidade do carrinho recebe UM desconto, e só um.**

Escada por produto, brinde e cupom disputam as mesmas unidades. Quem pega
primeiro, trava. Não existe configuração na Shopify que faça dois descontos
somarem na mesma unidade.

### Escada e brinde são mutuamente exclusivos

| carrinho simulado | escada ligada? | brinde |
|---|---|---|
| 5 potes, nenhum repetido — R$ 556,66 | não | ✅ Vit C R$ 0,00 |
| 3 Hair + TetraVit + Vit C — R$ 504,84 | sim (Hair 10%) | ❌ cobrada |
| 3 Hair + TetraVit + Ômega + Vit C — R$ 667,96 | sim (Hair 10%) | ❌ cobrada |

O brinde é um BxGy: ele **consome** 4 unidades como pré-requisito. Se a escada
já pegou essas unidades, não sobra pré-requisito e o brinde não dispara.

Testado também trocar o pré-requisito de **quantidade** para **valor**
(`Spend R$300, get 1 free`): **não resolve**. Mesmo com R$ 369,76 em itens
livres no carrinho, o brinde continuou sem entrar enquanto a escada do Hair
estava aplicando.

### Por que "só pedido grande"

Pedido grande = mais chance de ter 2+ do mesmo produto = escada liga = brinde
morre. Pedido pequeno de unidades avulsas = escada não liga = brinde entra.

Medido:

| | bruto | desconto |
|---|---|---|
| 5 potes avulsos | R$ 556,66 | **R$ 89,52** |
| 6 potes, 3 iguais | R$ 667,96 | **R$ 29,82** |

**Quem gasta mais ganha menos.** É o inverso do que a campanha promete.

---

## 2. O tema piora o problema

`snippets/botanika-semana-gift-sync.liquid` adiciona a Super Vitamina C ao
carrinho **sozinho** ao bater 4 unidades elegíveis, e escreve na tela:

> 🎁 Super Vitamina C adicionada automaticamente
> "O desconto de 100% da promoção será aplicado automaticamente."

Quando o desconto não dispara (o caso do pedido grande), a loja **cobra por um
produto que a cliente não escolheu**. Não é desconto que faltou: é cobrança
indevida. Foi o que geraram as reclamações de Adriana, Eli e Igor.

A lista `eligible` do script ainda inclui `9558490448104` (Kit da Imunidade),
que **não está** na lista do desconto — dá para bater 4 unidades com um produto
que o brinde nem aceita.

---

## 3. Cupons — 30 códigos ativos

### 3.1 Influenciadores — 20 códigos, 5%, classe PRODUTO

VICTORIA · BARBIERI · JULIACOLARES · DRROBSON · DRAGIOVANNAE · ANNAMACHADO ·
JOELHO5 · ORTOP · OSVALDO · LARISSALESSA · ANAAMARAL · FLAVIATELES · FESTEVES ·
CEMBRANELLI · LUDMILLA · OSÓRIO · DREGLIFE · DRGIBRAN · COLHER · LARILESSA

Todos: 5%, coleção "[CUPONS] Todos os Produtos" (16 produtos), `combinesWith`
tudo `true`, **sem data de fim**.

**Problema medido:** o cupom só pega as linhas que a escada não pegou.

Carrinho 3 Hair + TetraVit + Vit C com JULIACOLARES:
- Hair (o item mais caro, R$ 298,20) → fica só com a escada, cupom não entra
- TetraVit e Vit C → 5% do cupom
- **O cupom entregou R$ 10,32 num pedido de R$ 504,84** (2%)

**Pior:** em carrinho onde o brinde dispara, o cupom entrega **R$ 0,00**.
Simulado: 5 potes avulsos, com e sem JULIACOLARES — desconto idêntico
(R$ 89,52). O código foi completamente ignorado, mas a venda conta como
atribuída à influenciadora.

### 3.2 Códigos públicos empilháveis — risco aberto

`JOINGLE` (5%, ORDEM) e `BOTANIKA` (5%, ORDEM) têm `combinesWith.orderDiscounts:
true` — **empilham entre si**.

Aconteceu hoje no **#4562**: cliente usou os dois e levou 10% OFF.

### 3.3 Códigos que matam a escada

Estes têm `combinesWith` **tudo falso** — quem usa perde todas as escadas:

| código | valor | classe |
|---|---|---|
| LIVE8 | 8% | ORDEM |
| VOLTA5 | 5% | ORDEM |
| VOLTA10 | 10% | ORDEM |
| RECUPERA10MAIL | 10% | ORDEM |
| RECUPERA10ZAP | 10% | ORDEM |
| ALUNO10 | 10% | ORDEM |

Medido com LIVE8 no carrinho 3 Hair + TetraVit + Vit C: a escada de 10% do Hair
**desapareceu** (R$ 298,20 cheio) e entrou 8% na ordem.

**LIVE8 está ATIVO e sem data de fim**, embora o planejamento diga que não
deveria rodar durante a campanha.

### 3.4 RECOMPRA10 substitui a escada

Classe PRODUTO, 10%, segmento "Clientes que compraram pelo menos uma vez".
No **#4566** de hoje ele aplicou 10% em todas as linhas e a escada do Hair
**não apareceu** — o cupom ocupou as unidades. Como os dois valem 10%, o
cliente não perdeu; mas o desconto que a PDP prometeu não é o que consta.

### 3.5 PIX — promessa sem lastro

A PDP, o carrinho e o painel do drawer anunciam **"+5% OFF adicional no PIX"**
em três arquivos do tema. Varredura completa dos automáticos e de todos os
cupons ativos: **não existe nenhum desconto de PIX na loja.**

---

## 4. Automáticos ativos

| desconto | status | observação |
|---|---|---|
| 16 × [ESCADA] por produto (5% em 2un, 10% em 3un) | ACTIVE, sem fim | funcionam sempre |
| [SEMANA DO CLIENTE] Compre 4, leve 5 | ACTIVE até 20/09 | só dispara sem escada no carrinho |
| [SEMANA DO CLIENTE] Frete grátis acima de R$ 199,90 | ACTIVE até 20/09 | reativado em 16/09 |
| 3 × [BUMP] [retomada 20/09] | SCHEDULED | voltam sozinhos |

Cota: a loja está no teto de 25 automáticos. Contagem manual não é confiável —
a única forma de saber é tentar a operação.

---

## 5. O que aconteceu hoje (17/09, 13 pedidos)

R$ 4.960,12 bruto · R$ 474,78 em descontos · R$ 4.287,23 líquido · AOV R$ 345

Quatro pedidos com comportamento inconsistente:

**#4562** — R$ 783,06 em 7 potes. Vitamina C **cobrada** (brinde não entrou,
a escada do Hair travou). Cliente usou JOINGLE **e** BOTANIKA juntos = 10%.

**#4566** — RECOMPRA10 aplicou 10% e a escada do Hair sumiu. Vitamina C cobrada.

**#4569** — R$ 918,32. O brinde **entrou** (Vit C R$ 0,00), mas comeu as escadas
do Ômega (2un) e do TetraVit (2un): **o cliente perdeu R$ 28,02** que a PDP
prometia.

**#4571** — R$ 509,22. Brinde entrou, escada do Hair (2un) perdida:
**R$ 9,94** que a PDP prometia.

Ou seja: nos dois sentidos. Ora o brinde não entra e a cliente é cobrada por um
pote que o site colocou; ora o brinde entra e come o desconto de quantidade que
a página anunciou.

### Campanha até agora

| dia | pedidos | bruto | descontos | líquido | AOV |
|---|---|---|---|---|---|
| 14/09 | 50 | R$ 17.912 | R$ 2.090 | R$ 15.847 | R$ 316 |
| 15/09 | 52 | R$ 18.610 | R$ 2.003 | R$ 15.611 | R$ 319 |
| 16/09 | 46 | R$ 14.963 | R$ 1.796 | R$ 13.591 | R$ 286 |
| 17/09 | 13 | R$ 4.960 | R$ 475 | R$ 4.287 | R$ 345 |
| **total** | **161** | **R$ 56.446** | **R$ 6.364** | **R$ 49.337** | **R$ 306** |

---

## 6. Resumo dos achados

1. Escada e brinde nunca somam. Não é bug de configuração — é como a Shopify
   aloca desconto por unidade. Nenhum ajuste de parâmetro resolve.
2. O tema adiciona um produto pago ao carrinho prometendo que é grátis.
3. Quanto maior o pedido, menor o desconto — inverso da promessa.
4. Cupom de influenciador entrega pouco ou nada, e a comissão corre igual.
5. JOINGLE + BOTANIKA empilham: 10% para quem souber os dois códigos.
6. Seis códigos matam todas as escadas. LIVE8 entre eles, ativo sem data de fim.
7. PIX 5% é anunciado em três lugares e não existe.

**Nada neste documento foi alterado na loja.**
