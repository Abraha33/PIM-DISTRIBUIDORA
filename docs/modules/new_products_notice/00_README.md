---
module: new_products_notice
status: partial
type: workflow
source: chatgpt
last_review: 2026-06-19
---

# README — New Products Notice

## ¿Qué es New Products Notice?

New Products Notice documenta el subproceso de aviso de productos nuevos o reposiciones relevantes dentro del flujo de Compras M1. Se activa después de la revisión y filtro, y su objetivo es notificar a vendedores y puntos de venta sobre novedades en el catálogo.

## Principio rector

No todo producto recibido genera aviso. Solo los marcados como `new_product_notice_candidate` después de la revisión.

## Relación con otros módulos

| Módulo | Relación |
|---|---|
| `purchases_m1` | Flujo principal; el aviso ocurre después de revisión |
| `purchase_reception` | La recepción validada permite detectar productos nuevos |
| `catalog_master` | Los productos nuevos deben eventualmente integrarse al catálogo |

## Estado actual

`partial` — Estructura y contenido base completados. Pendiente de definir canal y reglas de generación.
