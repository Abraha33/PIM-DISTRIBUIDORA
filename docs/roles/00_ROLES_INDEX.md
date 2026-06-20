# Roles funcionales PIM — Índice

Este índice organiza los roles técnicos estables del PIM resultante / Final JSON Product. GitHub contiene la documentación técnica estable; Obsidian queda para conversación, exploración y notas vivas.

## Tabla de roles

| Tema | Rol | Archivo | Módulo | Sección JSON | Repo |
| ---- | --- | ------- | ------ | ------------ | ---- |
| Final JSON Product / products.json | Final JSON Product Architect | [`ROLE_final_json_product_architect.md`](ROLE_final_json_product_architect.md) | `pim_master` | `products[]` completo; fronteras entre `identity`, `category`, `attributes`, `commercial`, `suppliers`, `inventory_flow`, `marketing`, `media` y eventos separados. | `PIM-DISTRIBUIDORA` como núcleo PIM dentro de Esteroides ASNO. |
| stock levels / inventory_flow | Inventory Flow | [`ROLE_inventory_flow.md`](ROLE_inventory_flow.md) | `inventory_flow` | `products[].inventory_flow` y señales/eventos operativos derivados cuando no corresponda modificar producto maestro. | `PIM-DISTRIBUIDORA`; datos operativos externos solo como insumo. |
| marketing | Marketing | [`ROLE_marketing.md`](ROLE_marketing.md) | `marketing` | `products[].marketing`. | `PIM-DISTRIBUIDORA`; campañas/canales como fuentes de contexto. |
| media / evidencia | Media | [`ROLE_media.md`](ROLE_media.md) | `media` | `products[].media`; evidencia operativa puede referenciar eventos separados cuando aplique. | `PIM-DISTRIBUIDORA`; archivos de imagen/evidencia como insumo externo. |
| compras / ingreso de compra | Purchases M1 | [`ROLE_purchases_m1.md`](ROLE_purchases_m1.md) | `purchases_m1` | `products[].suppliers`, `products[].commercial` como referencia documental; eventos de compra separados cuando aplique. | `PIM-DISTRIBUIDORA`; ASNO/Scraper_Asno solo como fuentes, no como destino de esta documentación. |
| órdenes de compra | Purchase Orders | [`ROLE_purchase_orders.md`](ROLE_purchase_orders.md) | `purchase_orders` | Eventos de orden de compra y señales relacionadas; referencias a `products[].suppliers` o `products[].inventory_flow` cuando aplique. | `PIM-DISTRIBUIDORA`; proveedores/WhatsApp como fuentes operativas. |
| recepción / evidencia | Purchase Reception | [`ROLE_purchase_reception.md`](ROLE_purchase_reception.md) | `purchase_reception` | Eventos de recepción; referencias a `products[].inventory_flow`, `products[].media` y `products[].suppliers` solo cuando corresponda. | `PIM-DISTRIBUIDORA`; evidencia física/fotos como insumo. |
| aviso productos nuevos | New Products Notice | [`ROLE_new_products_notice.md`](ROLE_new_products_notice.md) | `new_products_notice` | `products[].marketing`, `products[].commercial` como insumos de aviso; evento/notice separado para comunicación interna. | `PIM-DISTRIBUIDORA`; equipos de venta/puntos de venta como destinatarios. |
| precios comerciales | Commercial Pricing | [`ROLE_commercial_pricing.md`](ROLE_commercial_pricing.md) | `commercial_pricing` | `products[].commercial` y señales de precio sugerido/alertas comerciales. | `PIM-DISTRIBUIDORA`; mercado/competencia como fuentes externas. |
| decisión de precio de venta | Selling Price Decision | [`ROLE_selling_price_decision.md`](ROLE_selling_price_decision.md) | `selling_price_decision` | Decisión revisada sobre `products[].commercial`; historial/evento de decisión cuando aplique. | `PIM-DISTRIBUIDORA`; encargado humano como decisor final. |
| comparación de precios | Price Comparison | [`ROLE_price_comparison.md`](ROLE_price_comparison.md) | `price_comparison` | `products[].commercial`, `products[].suppliers` y señales comparativas separadas por tipo. | `PIM-DISTRIBUIDORA`; compras históricas, proveedores, mercado/competencia como fuentes. |
| inventario por voz | Voice Inventory | [`ROLE_voice_inventory.md`](ROLE_voice_inventory.md) | `voice_inventory` | Señales/eventos de captura hacia `products[].inventory_flow`; producto, cantidad, ubicación y validación antes de escribir datos consolidados. | `PIM-DISTRIBUIDORA`; captura por voz como fuente operativa futura. |
| scraper/commercial dynamic data | Scraper Commercial Dynamic Data | [`ROLE_scraper_commercial_dynamic_data.md`](ROLE_scraper_commercial_dynamic_data.md) | `asno_wappsi_scraper_integration` | `products[].commercial`, `products[].suppliers`, señales para `products[].inventory_flow` y reportes; raw preservado fuera de campos normalizados. | `PIM-DISTRIBUIDORA` documenta el contrato; Scraper_Asno puede proveer datos técnicos pero no absorbe el rol PIM. |

## Activadores rápidos

- Final JSON Product
- products.json
- stock levels
- inventory_flow
- marketing
- media
- compras
- ingreso de compra
- recepción
- evidencia
- aviso productos nuevos
- órdenes de compra
- precios comerciales
- decisión de precio de venta
- comparación de precios
- inventario por voz
- scraper/commercial dynamic data

## Decisiones de frontera

- Cada rol escribe o propone cambios solo dentro de su sección asignada del Final JSON Product.
- Los campos normalizados quedan protegidos; si hay diferencia, se genera señal o pendiente de revisión.
- Compras, órdenes, recepción, captura por voz y avisos pueden generar eventos separados cuando no corresponda modificar el producto maestro.
- Marketing, media e inventory_flow son capas especializadas, no reemplazos del contrato maestro.
- El scraper alimenta datos dinámicos y raw; no decide reglas finales.
