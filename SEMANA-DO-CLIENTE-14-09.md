# Semana do Cliente — 14/09 a 19/09 · estado da Shopify

Loja: botanikabrasil.com.br · plano Shopify (não-Plus) · BRL · UTC-3
Configurado em 12/09. Tudo **programado**, com data de fim. Nada depende de alguém ligar ou desligar na mão.

---

## 1. O que está no ar (agendado)

| Item | ID | Janela (BRT) | Combina (produto / pedido / frete) |
|---|---|---|---|
| **RECOMPRA10** — cupom 10% | `DiscountCodeNode/1580102287592` | 14/09 00h01 → 20/09 00h00 | SIM / **NÃO** / SIM |
| Frete grátis ≥ R$ 199,90 | `DiscountAutomaticNode/1580105302248` | 14/09 00h01 → 20/09 00h00 | SIM / SIM / NÃO |
| 100 primeiros — frete sem mínimo | `DiscountAutomaticNode/1580105335016` | 14/09 00h01 → **14/09 23h59** | SIM / SIM / NÃO |
| Compre 4, leve 5 — Super Vitamina C | `DiscountAutomaticNode/1580105367784` | 14/09 00h01 → 20/09 00h00 | SIM / SIM / SIM |
| Escada Volume — 15% (5+ itens) | `DiscountAutomaticNode/1577084682472` | 14/09 00h01 → 20/09 00h00 | SIM / SIM / SIM |
| Escada Volume — 20% (8+ itens) | `DiscountAutomaticNode/1577084715240` | 14/09 00h01 → 20/09 00h00 | SIM / SIM / SIM |

**RECOMPRA10** é classe PRODUTO (aplicado sobre a coleção `[CUPONS] Todos os Produtos`, não sobre
"todos os produtos" — se fosse "todos os produtos" a Shopify o classificaria como classe PEDIDO e o
bloqueio contra o cupom de influenciadora deixaria de existir). Restrito ao segmento
`Clientes que compraram pelo menos uma vez` (`Segment/539907522792`). Sem limite de uso,
sem "uma vez por cliente".

## 2. Limite de 25 descontos automáticos — e o que foi feito

A loja estava em 25/25. A Shopify conta **períodos que se sobrepõem**, não o total
(confirmado na prática, e é o mesmo padrão que o Dia D usou em 09/09 com as 16 escadas).

Três bumps foram encerrados em **14/09 00h01** e **recriados já programados para voltar
em 20/09 00h00**, sem data de fim. A volta é automática — ninguém precisa religar nada.

| Bump | Encerra 14/09 00h01 | Volta 20/09 00h00 |
|---|---|---|
| Creatina → Whey 10% | `1574087000296` | `1580105433320` |
| Hair → Vitamina C 10% | `1572745773288` | `1580105466088` |
| Vit C / Ômega → TetraVit D 10% | `1573508743400` | `1580105498856` |

Continuam ativos e intocados: **Whey → Creatina**, **Tri[Mg] → TetraVit D**, **Sleep → Tri[Mg]**,
as 16 escadas por produto, os cupons de influenciadora e os cupons abertos.

---

## 3. ⚠️ REGRAS PARA A ALTERAÇÃO DO TEMA

**O cliente nunca pode ver um preço que o checkout não vai confirmar.** Cada item abaixo é um
lugar onde a vitrine pode prometer o que a loja não entrega.

### Não anunciar durante 14–19/09
- **"Leve o 2º com 10% off" para Hair → Vitamina C, Creatina → Whey e Vit C/Ômega → TetraVit D.**
  Esses três bumps estão desligados na semana. Qualquer bloco de cross-sell que os mostre precisa
  sair no dia 14 e voltar no dia 20.
- **5% no PIX — CANCELADO.** Decisão de 12/09: sai da campanha, não vai mais existir. Tem que ser
  removido de **todos** os canais: site, criativos, CRM, WhatsApp, influenciadoras, lives. O plano
  oficial em PDF ainda menciona os 5% do PIX e o acúmulo deles com os 10% de recompra — **essa parte
  do documento está vencida**.
- **Qualquer percentual somado do tipo "até 25%".** A soma da escada por produto com a escada de
  volume não foi testada. Só anunciar número que tenha sido visto num carrinho real.

### Anunciar com o texto certo
- **Compre 4, leve 5:** o BxGy da Shopify **não adiciona o item ao carrinho** — ele zera o preço de
  uma Vitamina C que já esteja lá. A copy tem que dizer, na PDP e no carrinho:
  *"adicione 1 Super Vitamina C e ela sai de graça"*. Sem isso o cliente com 4 itens não vê o brinde.
- **Frete:** R$ 199,90 vale **só** de 14/09 00h01 a 20/09 00h00. Fora dessa janela o mínimo volta a ser
  R$ 349,00 sozinho (é regra da taxa de envio, não desconto — não foi tocada).
- **100 primeiros:** o desconto expira **14/09 às 23h59 BRT**. O aviso no site tem que sair no mesmo
  minuto, senão o site promete frete grátis depois que a loja parou de dar.
- **RECOMPRA10:** só funciona para quem já tem pedido anterior. Não pode ser anunciado como cupom
  aberto — cliente novo tenta, é recusado, e abandona.

### Não acumula (se a copy disser que acumula, está errado)
- RECOMPRA10 **não** soma com cupom de influenciadora (os dois são classe PRODUTO — a Shopify
  aceita um cupom por classe). É intencional, está no plano oficial.
- RECOMPRA10 **não** soma com PALPITE12, BRASIL10, VOLTEI10, JOINGLE nem BOTANIKA (classe PEDIDO,
  bloqueados por `pedido = NÃO`).
- **Cupom de influenciadora agora acumula com a escada** (corrigido em 12/09, conforme o plano
  oficial). Consequência de margem: cliente com 8 itens e cupom de influenciadora paga
  0,80 × 0,95 = **24% off**. É o que o plano manda, mas o número é esse.
- **BOTANIKA** está com "combina com" tudo desligado: quem usa BOTANIKA perde a escada e o frete
  da semana. Estado pré-existente. As LPs anunciam esse cupom — vale revisar a copy.

---

## 4. Pendências

| Item | Situação |
|---|---|
| 5% no PIX | **Cancelado em 12/09.** Não entra na campanha. Retirar de toda a copy. |
| Brinde dos 200 primeiros (Manual + Guia da Imunidade) | **Resolvido.** Entrega via ActiveCampaign, fora da Shopify. |
| VICTORIA, JULIACOLARES e FESTEVES não acumulavam com a escada | **Corrigido em 12/09.** Os três agora combinam com desconto de produto, conforme o plano oficial. Históricos preservados (566, 70 e 20 usos). |
| "Cupom de quantidade exclusivo para cliente" | **Resolvido.** Segue a tabela atual, como o briefing manda. Nenhuma tabela nova criada. |
| Escada por produto + escada de volume: soma ou pega a melhor? | **Em aberto.** Sem teste. Enquanto não for verificado num carrinho real, não anunciar percentual somado. |
| Cupom **ANAAMARAL** | Aplica em produtos específicos, não na coleção `[CUPONS] Todos os Produtos` como os outros 20. Pode dar 5% em menos produtos do que a influenciadora anuncia. Não foi alterado — precisa de decisão. |

## 5. Reversão — dia 20/09 a loja volta sozinha

Frete grátis ≥ R$ 349 · 16 escadas por produto com teto de 10% · 6 bumps (3 deles pelos IDs
`[retomada 20/09]`) · cupons de influenciadora · cupons abertos. Nada da Semana do Cliente sobrando.
