---
module: purchases_m1
status: partial
type: purchasing
source: chatgpt
last_review: 2026-06-19
---

# README — Compras M1

## ¿Qué es Compras M1?

Compras M1 es el primer módulo PIM para organizar el flujo de compras alrededor del ASNO actual. Define la estructura documental para registrar, revisar y canalizar compras desde su detección hasta la notificación de productos nuevos.

## Alcance

El módulo cubre:

- Registro o detección de compra desde ASNO/Wappsi
- Identificación de proveedor, factura y productos
- Costos, cantidades e impuestos
- Recepción de mercancía con evidencia
- Revisión y filtro de la compra
- Decisión de precio (cuando aplica)
- Aviso de productos nuevos o reposiciones relevantes
- Contratos JSON preliminares para estado y trazabilidad
- Posible integración futura con ERP

## ¿Qué NO es Compras M1?

- No es un ERP transaccional.
- No reemplaza la lógica de `Scraper_Asno`.
- No define precios de venta finales.
- No gestiona órdenes de compra (ver `purchase_orders`).
- No ejecuta lógica productiva en esta fase.

## Relación con otros módulos

| Módulo | Relación |
|--------|----------|
| `purchase_reception` | Recibe evidencia y valida la llegada de mercancía |
| `new_products_notice` | Se activa después de revisión para avisar novedades |
| `commercial_pricing` | Consume decisiones de precio del flujo |
| `selling_price_decision` | Define precio de venta si aplica |
| `asno_wappsi_scraper_integration` | Fuente de datos crudos de compra |

## Estado actual

`partial` — Estructura y contenido base completados. Pendiente de validación contra datos reales del scraper.
