# Validation Report v1

## Por qu? existe el reporte consolidado

El PIM de Envax ya tiene varias capas de validaci?n:

- schema validation
- ejemplos inv?lidos controlados
- dictionary validation
- uniqueness validation
- naming validation
- family/variant validation
- data_quality validation
- documentation coverage validation

Cada capa sirve para algo distinto. El reporte consolidado existe para auditar el estado completo del contrato `products.json v1` en un solo lugar.

Esto no crea l?gica de negocio. No scrapea, no calcula stock, no arma campa?as y no gestiona im?genes. Es auditor?a del contrato, nada m?s. Y eso importa, porque sin auditor?a despu?s nadie sabe si el contrato est? sano o si simplemente ?parece? sano.

## Qu? validaciones incluye

? definido

- Validaci?n de schema para ejemplos v?lidos.
- Confirmaci?n de que los ejemplos inv?lidos de schema sean rechazados.
- Validaci?n contra diccionarios controlados.
- Confirmaci?n de que los fallos controlados de diccionario sean rechazados.
- Validaci?n de unicidad y consistencia de barcodes.
- Confirmaci?n de que los fallos controlados de unicidad sean rechazados.
- Validaci?n de reglas de nombres.
- Confirmaci?n de que los fallos controlados de nombres sean rechazados.
- Validaci?n de familias y variantes.
- Confirmaci?n de que los fallos controlados de familias sean rechazados.
- Validaci?n de gobernanza `data_quality`.
- Confirmaci?n de que los fallos controlados de `data_quality` sean rechazados.
- Validaci?n de cobertura documental para scripts y README.
- Advertencias no bloqueantes.
- Estado final consolidado.

## C?mo generar el reporte

```bash
python scripts/generate_validation_report.py
```

Tambi?n se puede generar solo JSON o solo Markdown:

```bash
python scripts/generate_validation_report.py --json-only
python scripts/generate_validation_report.py --md-only
```

## Archivos generados

```text
reports/pim_contract_v1_validation_report.json
reports/pim_contract_v1_validation_report.md
```

## C?mo leer pass / warning / fail

- `? pass`: la validaci?n pas?.
- `?? warning`: hay una advertencia controlada; no bloquea el reporte.
- `? fail`: hay un error que rompe el contrato o una expectativa de validaci?n.

## Qu? no cubre todav?a

?? pendiente

- Reglas comerciales reales.
- F?rmulas de stock.
- Quality control f?sico real.
- Scraper e integraci?n comercial.
- Costos, precios y proveedores.
- Marketing y media reales.
- Auditor?a hist?rica completa.

?? decisi?n tomada: el reporte consolida validaciones existentes; no reemplaza las validaciones individuales.

?? recomendaci?n experta: manten? el reporte como una foto de auditor?a. Si empieza a decidir negocio, se convierte en otro m?dulo y se ensucia el contrato. Cada cosa en su capa, loco.

## Script relacionado

Este documento acompa?a a `scripts/generate_validation_report.py`.
