---
module: purchases_m1
status: partial
type: purchasing
source: chatgpt
last_review: 2026-06-19
---

# Reglas de negocio — Compras M1

## Reglas generales

1. Toda compra debe tener un `source_system` identificado.
2. El `purchase_id` debe ser único dentro del sistema de origen.
3. No puede haber dos compras con la misma combinación `invoice_number + supplier`.
4. Un producto sin `product_id_pim` es candidato a producto nuevo.
5. La evidencia debe tener al menos una foto asociada.
6. Una compra no puede pasar a `closed` sin haber pasado por `under_review`.

## Reglas de recepción

7. `quantity_received` no puede exceder `quantity_purchased` sin justificación documentada.
8. Si `quantity_received < quantity_purchased`, la compra pasa a estado `incomplete`.
9. Si la mercancía llega dañada, se registra en `review.notes` y se evalúa caso por caso.

## Reglas de precio

10. Un producto marcado como `requires_price_decision` no genera aviso hasta que se resuelva el precio.
11. Si un producto ya existe en PIM y tiene precio de venta, no requiere nueva decisión de precio a menos que el costo haya cambiado significativamente.

## Reglas de aviso

12. No todo producto recibido genera aviso. Solo los marcados como `new_product_notice_candidate`.
13. Un aviso se genera solo después de que la compra pasa por `under_review`.
14. Los productos marcados como `new_product_candidate` deben ser candidatos automáticos a `new_product_notice_candidate`.
