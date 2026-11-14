# Briefing: corrigir a atribuição de canal no dash do AllianceOS (Botanika)

**Tarefa no Alliance:** "REUNIÃO DE KPI 12/11 — Revisar o dash e corrigir os canais que puxam errado"
**Responsável:** Pedro Lage · **Prazo:** sáb 14/11, 18h · **Prioridade:** alta
**Link:** https://alliance-os-sooty.vercel.app/?task=mcp-1794500690417-0-a1150#tasks

## O problema (da reunião de KPI de 12/11)
- O dash está atribuindo venda ao canal errado. Tráfego, CRM, orgânico e influenciadoras aparecem com vendas que não são deles.
- A divisão da meta por fonte, que é a base do planejamento, está apoiada em número falso.
- É a correção mais urgente da reunião: outras tarefas dependem dela.

## O que entregar
1. Comparar o que o dash mostra com a origem real das vendas em **pelo menos uma campanha fechada**. Sugestão: **11/11**, de 10/11 às 20h a 11/11 às 23h59 BRT.
2. Achar **onde** a atribuição quebra: UTM, integração, regra de classificação ou cadastro de canal.
3. **Escrever na tarefa** o que estava errado e o que foi corrigido, para saber se pode voltar a acontecer.
4. Corrigir, para que o dash mostre a venda no canal certo já na próxima reunião de KPI.

## Dados de referência do 11/11 (Shopify, conferidos em 12/11)
- **581 pedidos**, R$ 255,2 mil brutos, **R$ 207,3 mil líquidos**, ticket de R$ 357.
- Pico: 21h a 23h59, com 166 pedidos e R$ 60,5 mil.
- Use estes totais para validar se o dash soma certo antes de olhar a divisão por canal.

## Onde está a origem real de cada pedido (Shopify)
Cada pedido guarda as UTMs em **`customAttributes`** (note attributes) do pedido, gravadas pelo tema (`botanika-utm-capture`). Exemplos reais:

| Pedido | Atributos | Canal correto |
|---|---|---|
| #7668 | utm_source=whatsapp_org, utm_medium=grupos, utm_campaign=esquenta_1111_nov26, utm_content=grupo_vip | WhatsApp (grupos, orgânico/CRM) |
| #8012 | utm_source=whatsapp_api, utm_medium=api, utm_campaign=dia_d_1111, utm_content=base_total | WhatsApp API (CRM) |
| #7829 | utm_source=FB, utm_medium="[VID 1] [Envolvimento 180D]…\|<id>", utm_campaign="DIA D 11.11 \| VENDAS \| ABO\|<id>", utm_content=AD030_…, utm_term=Instagram_Feed, fbclid=… | Tráfego pago Meta |
| #8129 | utm_source=google, utm_medium=cpc, utm_term=botanika, **gclid E fbclid**, utm_id=<id de campanha Meta> | ⚠️ ambíguo: veio do Google, mas carrega fbclid e utm_id do Meta |
| #7947 | só `_ab_quem_levou` (sem UTM) | sem origem: direto/orgânico |

Outros sinais disponíveis no pedido:
- **Cupom** (`discountApplications` / códigos): os cupons de influenciadoras (60 códigos, 2%) devem puxar o canal **Influenciadoras**, mesmo se a UTM disser outra coisa.
- **RedTrack:** embed no tema, com o domínio de rastreamento `att.trk.botanikabrasil.com.br` e atribuição lastpaid. Pode ser uma segunda fonte de verdade para o pago.
- **UTMIFY:** também recebe as vendas e tem a sua própria atribuição.

## Hipóteses para checar (onde provavelmente quebra)
1. **utm_source fora do padrão:** existem "FB", "facebook", "ig", "google", "whatsapp_org", "whatsapp_api"… A regra de classificação pode não mapear todas e jogar o resto em outro balde.
2. **Pedidos sem UTM:** o plano do Bernardo diz que cerca de 70% dos pedidos chegam sem origem. Ver em que canal o dash coloca esses pedidos; se vão para "Tráfego" ou "CRM", infla esse canal.
3. **Prioridade entre sinais:** pedido com cupom de influenciadora **e** UTM de tráfego, ou com gclid **e** fbclid. Qual vence? Precisa de uma regra única e escrita.
4. **Pedidos não pagos:** Pix expirado e cancelados contando venda no canal (só no 11/11 teve vários Pix expirados).
5. **Fonte diferente por canal:** parte do dash vem da Shopify e parte da UTMIFY ou do Meta. Pode haver dupla contagem ou janela de atribuição diferente.
6. **Fuso horário:** pedidos de 21h a 23h59 BRT caem no dia seguinte em UTC. Na campanha 11/11 isso move cerca de R$ 60 mil de dia.

## Regras de negócio (Botanika)
- Fonte da verdade de pedido e valor: **Shopify** (`currentSubtotalPriceSet` = produtos já com desconto, sem frete e já descontando reembolso).
- Só pedidos **pagos**, sem teste e sem cancelados.
- Canais da meta: Tráfego (pago), CRM (WhatsApp API, e-mail, grupos), Orgânico, Influenciadoras.
- Não mexer em dado de cliente nem em pedido. A correção é **só no dash e na regra de classificação**.

## Depois de corrigir
- Registrar na tarefa: o que estava errado, a regra nova e os números do 11/11 por canal, antes e depois.
- Avisar o Pedro para revisar antes da próxima reunião de KPI.
