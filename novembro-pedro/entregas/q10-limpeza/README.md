# Limpeza do Q10 do 11/11 que sobra no carrinho (OK do Pedro em 13/11)
**Problema:** quem colocou a "Coenzima Q10 · Brinde" no carrinho em 11/11 e voltou depois fecha a compra com o Q10. O `bk-1111` tem `if (!on()) return;` logo no começo: depois do fim do 11/11, o script para de rodar e nunca tira o brinde.
Casos: #8129 (12/11), #8174 (13/11) e #8180 (13/11).

**Correção:** trocar a linha `if (!on()) return;` do `snippets/bk-1111.liquid` do tema **ao vivo** pelo bloco abaixo. Ele só remove do carrinho a linha da variante 68122684457192 com `_brinde = 11/11` e não mexe em mais nada.

```js
  if (!on()) {
    /* 13/11: depois do 11/11, tira do carrinho o Q10 de brinde que sobrou de quem montou o carrinho no dia 11 */
    try {
      fetch('/cart.js', { headers: { Accept: 'application/json' } }).then(function(r){ return r.json(); }).then(function(cart){
        var up = {}, n = 0;
        (cart.items || []).forEach(function(it){ if (it.variant_id === GIFT && it.properties && it.properties._brinde === '11/11') { up[it.key] = 0; n++; } });
        if (!n) return;
        return fetch('/cart/update.js', { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' }, body: JSON.stringify({ updates: up }) })
          .then(function(){ if (/\/cart/.test(location.pathname)) location.reload(); else document.dispatchEvent(new CustomEvent('cart:refresh')); });
      }).catch(function(){});
    } catch (e) {}
    return;
  }
```
**Aplicar:**
1. Backup do bk-1111 do tema ao vivo.
2. Conferir se o bk-1111 é renderizado no layout do tema ao vivo.
3. Upload.
4. Teste na prévia: colocar o Q10 no carrinho com `_brinde=11/11` e conferir que some.
