---
module: purchase_reception
status: partial
type: inventory
source: chatgpt
last_review: 2026-06-19
---

# Flujo funcional — Purchase Reception

## Diagrama de flujo

```
1. Compra en estado pending_reception
       │
2. Llega mercancía
       │
3. Se toma evidencia/foto de factura y productos
       │
4. Se cuentan y verifican cantidades
       │
5. Se inspecciona estado físico
       │
6. Se registra resultado
       │
7. Compra pasa a received_with_evidence
```

## Relación con Compras M1

La recepción es activada por el flujo de Compras M1 cuando una compra está en estado `pending_reception`. Los datos de recepción se almacenan en el objeto `reception` del contrato de compra M1.

## Estados de recepción

| Estado | Descripción |
|---|---|
| `pending_reception` | Compra detectada, mercancía no recibida |
| `received_with_evidence` | Mercancía recibida con evidencia fotográfica |
| `incomplete` | Cantidad recibida menor a la comprada |
| `rejected` | Mercancía rechazada por daño o error |

## Datos generados

- Fotos de evidencia (`evidence_photos`)
- Fecha y hora de recepción (`received_at`)
- Cantidad recibida por producto (`quantity_received`)
- Notas de novedades o daños
