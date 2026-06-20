---
module: purchases_m1
status: partial
type: purchasing
source: chatgpt
last_review: 2026-06-19
---

# Datos necesarios — Compras M1

## Campos mínimos del registro de compra

| Campo | Tipo | Descripción |
|---|---|---|
| `purchase_m1_id` | string | Identificador único del registro en PIM |
| `source_system` | string | Sistema de origen (ASNO/Wappsi) |
| `supplier` | object | Datos del proveedor |
| `invoice_number` | string | Número de factura |
| `purchase_date` | date | Fecha de compra/factura |
| `received_date` | datetime | Fecha y hora de recepción |
| `items` | array | Lista de productos comprados |
| `reception` | object | Estado de recepción y evidencia |
| `review` | object | Estado de revisión y notas |
| `status` | string | Estado actual del flujo |

## Campos de cada item (producto)

| Campo | Tipo | Descripción |
|---|---|---|
| `product_code_raw` | string | Código del producto en sistema de origen |
| `product_name_raw` | string | Nombre del producto en sistema de origen |
| `product_id_pim` | string \| null | ID del producto en PIM si existe |
| `quantity_purchased` | number | Cantidad facturada/comprada |
| `quantity_received` | number | Cantidad recibida |
| `unit_cost` | number | Costo unitario |
| `taxes` | number | Impuestos asociados |
| `requires_price_decision` | boolean | Si requiere decisión de precio |
| `new_product_candidate` | boolean | Si es candidato a producto nuevo |
| `new_product_notice_candidate` | boolean | Si debe generar aviso |

## Campos de recepción

| Campo | Tipo | Descripción |
|---|---|---|
| `status` | string | Estado de recepción |
| `received_at` | datetime | Momento de recepción |
| `evidence_photos` | array | Lista de fotos de evidencia |

## Campos de cada foto de evidencia

| Campo | Tipo | Descripción |
|---|---|---|
| `type` | string | Tipo (invoice_photo, merchandise_photo) |
| `uri` | string | Ubicación de la foto |
| `notes` | string | Notas sobre la evidencia |

## Campos de revisión

| Campo | Tipo | Descripción |
|---|---|---|
| `review_status` | string | Estado de revisión |
| `reviewed_by` | string \| null | Quién revisó |
| `notes` | array | Notas de revisión |

## Estados sugeridos

```
detected                     — compra detectada, sin recepción
pending_reception            — pendiente de recibir mercancía
received_with_evidence       — recibida con evidencia fotográfica
under_review                 — en revisión/filtro
approved                     — revisión aprobada
incomplete                   — recepción incompleta (faltante)
rejected                     — compra rechazada
requires_price_decision      — pendiente de definición de precio
ready_for_notice             — lista para generar aviso
closed                       — flujo completado
```
