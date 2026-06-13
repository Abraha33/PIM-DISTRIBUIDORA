# Reporte de Validaci?n PIM Contract v1

## Estado general

? pass

- Contrato: `products.json v1`
- Repositorio: `PIM-DISTRIBUIDORA`
- Generado: `2026-06-13T18:58:56.258854+00:00`

## Resumen

| Capa | Estado |
| --- | --- |
| Validaci?n de schema | ? pass |
| Ejemplos inv?lidos controlados | ? pass |
| Validaci?n de diccionarios | ? pass |
| Fallos controlados de diccionario | ? pass |
| Validaci?n de unicidad | ? pass |
| Fallos controlados de unicidad | ? pass |
| Advertencias | ?? 1 |
| Errores | ? 0 |

## Validaci?n de schema

- ? pass `schema_validation` ? `contracts/products.v1.example.json` ? Schema validation passed.
- ? pass `schema_validation` ? `contracts/product_families.v1.example.json` ? Schema validation passed.
- ? pass `schema_validation` ? `contracts/barcode_history.v1.example.json` ? Schema validation passed.

## Ejemplos inv?lidos controlados

- ? pass `validation_failures` ? `examples/validation_failures/barcode_history_invalid_action.json` ? Controlled invalid example was rejected as expected.
- ? pass `validation_failures` ? `examples/validation_failures/barcode_history_missing_product_code.json` ? Controlled invalid example was rejected as expected.
- ? pass `validation_failures` ? `examples/validation_failures/family_children_codes_not_array.json` ? Controlled invalid example was rejected as expected.
- ? pass `validation_failures` ? `examples/validation_failures/family_missing_family_id.json` ? Controlled invalid example was rejected as expected.
- ? pass `validation_failures` ? `examples/validation_failures/product_invalid_barcode_status.json` ? Controlled invalid example was rejected as expected.
- ? pass `validation_failures` ? `examples/validation_failures/product_invalid_capacity_value.json` ? Controlled invalid example was rejected as expected.
- ? pass `validation_failures` ? `examples/validation_failures/product_invalid_status.json` ? Controlled invalid example was rejected as expected.
- ? pass `validation_failures` ? `examples/validation_failures/product_missing_code.json` ? Controlled invalid example was rejected as expected.
- ? pass `validation_failures` ? `examples/validation_failures/product_missing_names.json` ? Controlled invalid example was rejected as expected.
- ? pass `validation_failures` ? `examples/validation_failures/product_missing_unit_summary.json` ? Controlled invalid example was rejected as expected.

## Validaci?n de diccionarios

- ? pass `material_id_exists` ? `contracts/products.v1.example.json` ? Dictionary rule passed.
- ? pass `color_id_exists` ? `contracts/products.v1.example.json` ? Dictionary rule passed.
- ? pass `unit_presentation_codes_exist` ? `contracts/products.v1.example.json` ? Dictionary rule passed.
- ? pass `unit_summary_codes_exist` ? `contracts/products.v1.example.json` ? Dictionary rule passed.
- ? pass `unit_summary_codes_in_unit_presentation` ? `contracts/products.v1.example.json` ? Dictionary rule passed.
- ? pass `material_abbreviation_matches_dictionary` ? `contracts/products.v1.example.json` ? Dictionary rule passed.
- ? pass `color_name_matches_dictionary` ? `contracts/products.v1.example.json` ? Dictionary rule passed.
- ? pass `unit_presentation_labels_match_code_factor` ? `contracts/products.v1.example.json` ? Dictionary rule passed.

## Fallos controlados de diccionario

- ? pass `dictionary_failures` ? `examples/dictionary_failures/product_invalid_color_id.json` ? Controlled dictionary failure was rejected as expected.
- ? pass `dictionary_failures` ? `examples/dictionary_failures/product_invalid_material_id.json` ? Controlled dictionary failure was rejected as expected.
- ? pass `dictionary_failures` ? `examples/dictionary_failures/product_invalid_unit_code.json` ? Controlled dictionary failure was rejected as expected.
- ? pass `dictionary_failures` ? `examples/dictionary_failures/product_invalid_unit_label.json` ? Controlled dictionary failure was rejected as expected.
- ? pass `dictionary_failures` ? `examples/dictionary_failures/product_unit_summary_not_in_unit_presentation.json` ? Controlled dictionary failure was rejected as expected.

## Validaci?n de unicidad

- ? pass `product_code_uniqueness` ? `contracts/products.v1.example.json + contracts/barcode_history.v1.example.json` ? Uniqueness rule passed.
- ? pass `active_barcode_uniqueness` ? `contracts/products.v1.example.json + contracts/barcode_history.v1.example.json` ? Uniqueness rule passed.
- ? pass `primary_barcode_per_unit` ? `contracts/products.v1.example.json + contracts/barcode_history.v1.example.json` ? Uniqueness rule passed.
- ? pass `barcode_history_references_existing_product_unit` ? `contracts/products.v1.example.json + contracts/barcode_history.v1.example.json` ? Uniqueness rule passed.
- ? pass `barcode_history_action_consistency` ? `contracts/products.v1.example.json + contracts/barcode_history.v1.example.json` ? Uniqueness rule passed.

## Fallos controlados de unicidad

- ? pass `uniqueness_failures` ? `examples/uniqueness_failures/barcode_history_activated_but_inactive.json` ? Controlled uniqueness failure was rejected as expected.
- ? pass `uniqueness_failures` ? `examples/uniqueness_failures/barcode_history_deactivated_but_active.json` ? Controlled uniqueness failure was rejected as expected.
- ?? warning `uniqueness_failures` ? `examples/uniqueness_failures/barcode_history_recycled_warning.json` ? Controlled warning example emitted a warning as expected.
- ? pass `uniqueness_failures` ? `examples/uniqueness_failures/barcode_history_unknown_product.json` ? Controlled uniqueness failure was rejected as expected.
- ? pass `uniqueness_failures` ? `examples/uniqueness_failures/barcode_history_unknown_unit.json` ? Controlled uniqueness failure was rejected as expected.
- ? pass `uniqueness_failures` ? `examples/uniqueness_failures/product_multiple_primary_barcodes_same_unit.json` ? Controlled uniqueness failure was rejected as expected.
- ? pass `uniqueness_failures` ? `examples/uniqueness_failures/products_duplicate_active_barcode.json` ? Controlled uniqueness failure was rejected as expected.
- ? pass `uniqueness_failures` ? `examples/uniqueness_failures/products_duplicate_code.json` ? Controlled uniqueness failure was rejected as expected.

## Advertencias

- ?? warning `uniqueness_failures` ? `examples/uniqueness_failures/barcode_history_recycled_warning.json` ? Controlled warning example emitted a warning as expected.

## Errores

- ? pass ? Sin hallazgos.

## Siguiente paso recomendado

Agregar validaci?n de consistencia de naming contra docs/naming_rules_v1.md sin implementar l?gica comercial.
