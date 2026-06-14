# Reporte de Validaci?n PIM Contract v1

## Estado general

? pass

- Contrato: `products.json v1`
- Repositorio: `PIM-DISTRIBUIDORA`
- Generado: `2026-06-14T03:46:47.025728+00:00`

## Resumen

| Capa | Estado |
| --- | --- |
| Validaci?n de schema | ? pass |
| Ejemplos inv?lidos controlados | ? pass |
| Validaci?n de diccionarios | ? pass |
| Fallos controlados de diccionario | ? pass |
| Validaci?n de unicidad | ? pass |
| Fallos controlados de unicidad | ? pass |
| Validaci?n de nombres | ? pass |
| Fallos controlados de nombres | ? pass |
| Validaci?n de familias y variantes | ? pass |
| Fallos controlados de familias y variantes | ? pass |
| Advertencias | ?? 4 |
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

## Validaci?n de nombres

- ? pass `pos_name_components` ? `contracts/products.v1.example.json` ? Naming rule passed.
- ? pass `pos_name_forbidden_components` ? `contracts/products.v1.example.json` ? Naming rule passed.
- ? pass `logistics_name_components` ? `contracts/products.v1.example.json` ? Naming rule passed.
- ? pass `internal_name_components` ? `contracts/products.v1.example.json` ? Naming rule passed.
- ? pass `ecommerce_short_components` ? `contracts/products.v1.example.json` ? Naming rule passed.
- ? pass `ecommerce_short_forbidden_components` ? `contracts/products.v1.example.json` ? Naming rule passed.
- ? pass `ecommerce_long_components` ? `contracts/products.v1.example.json` ? Naming rule passed.
- ? pass `unit_label_format_in_names` ? `contracts/products.v1.example.json` ? Naming rule passed.

## Fallos controlados de nombres

- ? pass `naming_failures` ? `examples/naming_failures/product_ecommerce_long_missing_presentaciones.json` ? Controlled naming failure was rejected as expected.
- ? pass `naming_failures` ? `examples/naming_failures/product_ecommerce_long_missing_unit_label.json` ? Controlled naming failure was rejected as expected.
- ? pass `naming_failures` ? `examples/naming_failures/product_ecommerce_short_contains_reference.json` ? Controlled naming failure was rejected as expected.
- ? pass `naming_failures` ? `examples/naming_failures/product_internal_missing_reference.json` ? Controlled naming failure was rejected as expected.
- ? pass `naming_failures` ? `examples/naming_failures/product_invalid_unit_label_in_name.json` ? Controlled naming failure was rejected as expected.
- ? pass `naming_failures` ? `examples/naming_failures/product_logistics_missing_code.json` ? Controlled naming failure was rejected as expected.
- ? pass `naming_failures` ? `examples/naming_failures/product_logistics_missing_reference.json` ? Controlled naming failure was rejected as expected.
- ? pass `naming_failures` ? `examples/naming_failures/product_pos_contains_brand.json` ? Controlled naming failure was rejected as expected.
- ? pass `naming_failures` ? `examples/naming_failures/product_pos_contains_reference.json` ? Controlled naming failure was rejected as expected.
- ? pass `naming_failures` ? `examples/naming_failures/product_pos_missing_material.json` ? Controlled naming failure was rejected as expected.

## Validaci?n de familias y variantes

- ? pass `family_id_consistency` ? `contracts/products.v1.example.json + contracts/product_families.v1.example.json` ? Family rule passed.
- ? pass `children_codes_consistency` ? `contracts/products.v1.example.json + contracts/product_families.v1.example.json` ? Family rule passed.
- ? pass `product_family_membership` ? `contracts/products.v1.example.json + contracts/product_families.v1.example.json` ? Family rule passed.
- ? pass `duplicate_child_membership` ? `contracts/products.v1.example.json + contracts/product_families.v1.example.json` ? Family rule passed.
- ? pass `family_parent_product` ? `contracts/products.v1.example.json + contracts/product_families.v1.example.json` ? Family rule passed.
- ? pass `parent_code_consistency` ? `contracts/products.v1.example.json + contracts/product_families.v1.example.json` ? Family warning rule passed.
- ? pass `variant_axis_consistency` ? `contracts/products.v1.example.json + contracts/product_families.v1.example.json` ? Family warning rule passed.
- ? pass `product_sellability` ? `contracts/products.v1.example.json + contracts/product_families.v1.example.json` ? Family warning rule passed.

## Fallos controlados de familias y variantes

- ? pass `family_failures` ? `examples/family_failures/family_child_code_unknown.json` ? Controlled family failure was rejected as expected.
- ?? warning `family_failures` ? `examples/family_failures/family_parent_code_missing_warning.json` ? Controlled family warning emitted a warning as expected.
- ?? warning `family_failures` ? `examples/family_failures/family_variant_axis_missing_child_attribute_warning.json` ? Controlled family warning emitted a warning as expected.
- ? pass `family_failures` ? `examples/family_failures/product_child_family_id_mismatch.json` ? Controlled family failure was rejected as expected.
- ? pass `family_failures` ? `examples/family_failures/product_child_in_multiple_families.json` ? Controlled family failure was rejected as expected.
- ? pass `family_failures` ? `examples/family_failures/product_family_id_unknown.json` ? Controlled family failure was rejected as expected.
- ? pass `family_failures` ? `examples/family_failures/product_family_parent_without_family_id.json` ? Controlled family failure was rejected as expected.
- ?? warning `family_failures` ? `examples/family_failures/product_not_sellable_not_family_parent_warning.json` ? Controlled family warning emitted a warning as expected.

## Advertencias

- ?? warning `uniqueness_failures` ? `examples/uniqueness_failures/barcode_history_recycled_warning.json` ? Controlled warning example emitted a warning as expected.
- ?? warning `family_failures` ? `examples/family_failures/family_parent_code_missing_warning.json` ? Controlled family warning emitted a warning as expected.
- ?? warning `family_failures` ? `examples/family_failures/family_variant_axis_missing_child_attribute_warning.json` ? Controlled family warning emitted a warning as expected.
- ?? warning `family_failures` ? `examples/family_failures/product_not_sellable_not_family_parent_warning.json` ? Controlled family warning emitted a warning as expected.

## Errores

- ? pass ? Sin hallazgos.

## Siguiente paso recomendado

Agregar validaci?n de reglas de calidad de datos (`data_quality`) sin implementar l?gica comercial.
