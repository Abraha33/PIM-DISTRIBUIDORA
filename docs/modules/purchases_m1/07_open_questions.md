---
module: purchases_m1
status: partial
type: purchasing
source: chatgpt
last_review: 2026-06-19
---

# Preguntas abiertas — Compras M1

| # | Pregunta | Contexto | Propuesta |
|---|---|---|---|
| 1 | ¿Quién toma la foto de recepción? | La evidencia fotográfica es parte del flujo, pero no está definido el rol. | Almacén, recepcionista o el mismo comprador. |
| 2 | ¿Dónde se guarda la evidencia? | Las fotos requieren almacenamiento. | Pendiente de definir (local, S3, Supabase). |
| 3 | ¿Qué se considera producto nuevo? | Un producto puede ser nuevo para PIM pero no nuevo en el mercado. | Definir regla: no existe en `products.json`. |
| 4 | ¿Qué se considera reposición relevante? | No toda reposición merece aviso. | Definir umbral: producto sin compra en los últimos N meses. |
| 5 | ¿Quién decide precio final? | El flujo marca `requires_price_decision`. | Gerente de producto, administrador o vendedor. |
| 6 | ¿Qué vendedores o puntos de venta reciben aviso? | El aviso debe llegar a los interesados. | Lista por categoría de producto o zona. |
| 7 | ¿El aviso se genera automático o requiere aprobación humana? | El flujo actual requiere revisión. | Podría ser automático para productos conocidos. |
| 8 | ¿Se deben soportar múltiples facturas por compra? | M1 es para compra simple. | Decidir si M2 soportará múltiples facturas. |
| 9 | ¿Cómo se manejan las devoluciones parciales? | No está en alcance M1. | Dejar para futura versión. |
