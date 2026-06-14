# Data Quality Validation v1

## Qu? significa `data_quality`

`data_quality` representa la calidad del dato del producto dentro del contrato PIM.

No significa calidad f?sica del producto. No habla de humedad, calor, vencimiento, rotaci?n, remates, bodega ni estado del inventario. Eso corresponde a `inventory_flow` y a futuros m?dulos de quality control f?sico.

Ac? validamos si la ficha del producto est? completa, coherente y gobernada.

## Diferencia con quality control f?sico

- `data_quality`: calidad del dato del producto.
- `quality_control`: calidad f?sica u operacional del producto.

Mezclar esas dos cosas ser?a una locura c?smica. Es como confundir el plano de una casa con la humedad de una pared. Los dos importan, pero no son lo mismo.

## Reglas validadas

? definido

- `data_quality.status` debe ser `pending`, `ready`, `needs_review` o `incomplete`.
- Si el status es `ready`, `missing_fields` debe estar vac?o.
- Si el status es `ready`, `errors` debe estar vac?o.
- Si `errors` no est? vac?o, el status no puede ser `ready`.
- Si `missing_fields` no est? vac?o, el status no puede ser `ready`.
- Si un campo core est? vac?o o null, debe aparecer en `data_quality.missing_fields`.
- `missing_fields`, `warnings` y `errors` deben ser arrays de strings.

## Campos core revisados

- `code`
- `identity.final_name`
- `category.final.name`
- `attributes.material.id`
- `attributes.color.id`
- `unit_summary.minimum_sale_unit.code`
- `unit_summary.maximum_purchase_unit.code`
- `names.pos`
- `names.logistics`
- `names.internal`
- `names.ecommerce_short`
- `names.ecommerce_long`

## Qu? es inv?lido

? fail

- Producto `ready` con `missing_fields`.
- Producto `ready` con `errors`.
- Campo core vac?o no listado en `missing_fields`.
- `missing_fields`, `warnings` o `errors` que no sean arrays de strings.

## Qu? produce warning

?? warning

- Unidad m?nima y m?xima iguales.
- `identity.reference.label` vac?o.
- `identity.brand.name` vac?o.
- `commercial.prices` vac?o.
- `commercial.costs` vac?o.
- `suppliers` vac?o.

## Por qu? precios, costos y suppliers son warning en v1

Porque esos datos dependen de scraper o integraciones comerciales futuras. En v1 el contrato puede existir sin ellos, pero conviene advertirlo para auditor?a.

## Qu? no cubre todav?a

?? pendiente

- Calidad f?sica del producto.
- Stock level.
- Rotaci?n de inventario.
- Pol?ticas de almacenamiento.
- Scraper comercial.
- Pricing real.
- Costing real.
- Supplier enrichment real.

?? decisi?n tomada: `data_quality` gobierna datos del producto, no operaciones f?sicas.

?? recomendaci?n experta: si quer?s un PIM serio, separ? calidad de dato de calidad f?sica. Si lo mezcl?s, despu?s ni el equipo de datos ni operaciones saben qui?n rompi? qu?.
