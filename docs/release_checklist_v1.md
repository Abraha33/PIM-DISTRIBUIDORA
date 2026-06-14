# Release Checklist ? PIM Contract v1

## 1. Estado general

- **Contract version:** `products.json v1`
- **Status:** ready for module integration
- **Current commit:** `83b7094`
- **Overall validation report:** `pass`
- **Errors:** `0`

Este release deja cerrado el contrato maestro v1 como base estable antes de integrar m?dulos reales.

## 2. Archivos principales cerrados

- `contracts/products.v1.example.json`
- `contracts/product_families.v1.example.json`
- `contracts/barcode_history.v1.example.json`
- `schemas/products.v1.schema.json`
- `schemas/product_families.v1.schema.json`
- `schemas/barcode_history.v1.schema.json`
- `dictionaries/unit_dictionary.json`
- `dictionaries/material_dictionary.json`
- `dictionaries/color_dictionary.json`

## 3. Validadores activos

- `scripts/validate_contracts.py`
- `scripts/validate_dictionaries.py`
- `scripts/validate_uniqueness.py`
- `scripts/validate_naming.py`
- `scripts/validate_families.py`
- `scripts/validate_data_quality.py`
- `scripts/validate_documentation_coverage.py`
- `scripts/generate_validation_report.py`

## 4. Comando completo de validaci?n final

```bash
python scripts/validate_contracts.py --include-failures --include-dictionaries --include-uniqueness --include-naming --include-families --include-data-quality --include-docs
python scripts/generate_validation_report.py
```

## 5. Qu? est? definido en v1

- `code`
- barcode por `unit_presentation`
- `identity`
- `category.final`
- `attributes`
- `unit_presentation`
- `unit_summary`
- `names`
- `family_id`
- `product_families`
- `barcode_history`
- `data_quality`
- placeholders de m?dulos pendientes

## 6. Qu? NO est? definido todav?a

- l?gica real de stock level
- f?rmulas de `inventory_flow`
- control f?sico de calidad
- reglas de marketing
- reglas de media/im?genes
- integraci?n con scraper
- l?gica real de precios, costos y proveedores
- l?gica de importaci?n/exportaci?n ERP

## 7. Reglas de protecci?n

- No modificar la estructura `products.v1` sin cambio de versi?n.
- Cualquier cambio estructural debe convertirse en `products.json v2`.
- Los m?dulos deben integrarse por medio de los placeholders existentes:
  - `inventory_flow`
  - `marketing`
  - `media`
- Los datos de scraper/commercial no deben sobrescribir campos manuales normalizados sin auditor?a expl?cita.

## 8. Pr?ximas versiones

- **v2:** integraci?n de `inventory_flow`
- **v3:** integraci?n de `marketing`
- **v4:** integraci?n de `media`
- **v5:** integraci?n de `scraper/commercial` si hace falta

## 9. Checklist final

- [x] Schema validation passes
- [x] Dictionary validation passes
- [x] Uniqueness validation passes
- [x] Naming validation passes
- [x] Family validation passes
- [x] Data quality validation passes
- [x] Documentation coverage passes
- [x] Consolidated report generated
- [ ] Inventory flow module integrated
- [ ] Marketing module integrated
- [ ] Media module integrated
- [ ] Scraper/commercial module integrated

?? **Decisi?n tomada:** `products.json v1` queda como contrato maestro estable; los m?dulos reales deben integrarse en versiones posteriores o mediante placeholders controlados.

?? **Recomendaci?n experta:** no metas l?gica de negocio en v1 despu?s de declararlo estable. Si aparece una necesidad estructural nueva, version?. El versionado es el cintur?n de seguridad del contrato.
