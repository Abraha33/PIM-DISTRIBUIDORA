# Módulos PIM — Índice y Estados

## Estado por módulo

| Módulo | Estado |
|--------|--------|
| catalog_master | sólido |
| product_normalization | parcial |
| dictionaries | sólido |
| families_variants | sólido/parcial |
| barcode_history | sólido |
| data_quality | sólido/parcial |
| inventory_flow | draft |
| marketing | draft |
| media | draft |
| purchases_m1 | partial |
| purchase_orders | draft |
| purchase_reception | partial |
| new_products_notice | partial |
| commercial_pricing | draft |
| selling_price_decision | draft |
| price_comparison | draft/documental |
| voice_inventory | draft/documental |
| asno_wappsi_scraper_integration | draft |
| smart_customers_integration | draft |
| modelo_valeria | draft |
| physical_quality | draft |

## Módulos funcionales obligatorios para el Final JSON Product

- `inventory_flow`
- `marketing`
- `media`
- `purchases_m1`
- `purchase_orders`
- `purchase_reception`
- `new_products_notice`
- `commercial_pricing`
- `selling_price_decision`
- `price_comparison`
- `voice_inventory`
- `asno_wappsi_scraper_integration`
- `smart_customers_integration`

## Leyenda

- **sólido**: contrato/documentación base completa. Puede requerir ajustes menores.
- **parcial**: existe base pero faltan secciones.
- **sólido/parcial**: núcleo sólido con áreas pendientes de detalle.
- **draft**: recién iniciado, estructura básica, contenido mínimo.
- **draft/documental**: rol definido como documentación estable; todavía no implica implementación ni schema productivo.

## Convención

Los módulos marcados como draft deben avanzar a parcial antes de integrar lógica productiva. Ningún módulo automático debe escribir fuera de su sección asignada sin revisión explícita.
