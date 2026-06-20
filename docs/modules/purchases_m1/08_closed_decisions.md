---
module: purchases_m1
status: partial
type: purchasing
source: chatgpt
last_review: 2026-06-19
---

# Decisiones cerradas — Compras M1

| # | Decisión | Justificación |
|---|---|---|
| 1 | Compras M1 pertenece a `PIM-DISTRIBUIDORA`. | El módulo es documentación de contrato y flujo, no ejecución transaccional. |
| 2 | La extracción técnica vive en `Scraper_Asno`. | Separación de responsabilidades: PIM documenta, scraper extrae. |
| 3 | La recepción con evidencia es parte del flujo. | No es un proceso separado; está integrado en Compras M1. |
| 4 | El aviso de productos nuevos ocurre después de revisión/filtro. | Evita notificaciones prematuras de mercancía no validada. |
| 5 | ERP no se modifica en esta fase. | El ERP futuro consumirá cuando esté maduro. |
| 6 | Compras M1 no gestiona precios de venta. | Los precios de venta pertenecen a `selling_price_decision`. |
| 7 | No se soportan múltiples facturas por compra en M1. | M1 es para el caso base de compra simple. |
| 8 | Los estados del flujo son secuenciales pero no obligatorios. | Una compra puede saltar estados si aplica. |
