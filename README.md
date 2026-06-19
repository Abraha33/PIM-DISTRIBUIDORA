# PIM-DISTRIBUIDORA

## Prop?sito

`PIM-DISTRIBUIDORA` es el repositorio maestro para documentar y versionar el PIM de Envax.

El objetivo es guardar contratos limpios, ejemplos versionados y diccionarios base para que la informaci?n de producto pueda crecer sin mezclar responsabilidades.

## Versi?n actual

- Contrato principal: `products.json v1`
- Ejemplo maestro: `contracts/products.v1.example.json`
- Estado actual: contrato base completado; m?dulos de stock, marketing e im?genes pendientes.

## Archivos principales

- `contracts/products.v1.example.json`: ejemplo del contrato maestro de producto.
- `contracts/product_families.v1.example.json`: ejemplo de agrupaci?n padre-hijo / familia de producto.
- `contracts/barcode_history.v1.example.json`: ejemplo de trazabilidad de c?digos de barras.
- `dictionaries/unit_dictionary.json`: diccionario de unidades de presentaci?n.
- `dictionaries/material_dictionary.json`: diccionario de materiales.
- `dictionaries/color_dictionary.json`: diccionario de colores.

## M?dulos

- `modules/inventory_flow`: futuro m?dulo para stock level, quality control f?sico y flujo de inventario.
- `modules/marketing`: futuro m?dulo para clientes objetivo, cat?logos, campa?as y promociones.
- `modules/media`: futuro m?dulo para im?genes por uso.

## Estado actual

? Contrato base `products.json v1` definido.  
? Diccionarios iniciales creados.  
? Ejemplos versionados creados.  
?? `inventory_flow` pendiente.  
?? `marketing` pendiente.  
?? `media` pendiente.  
?? scraper/commercial pendiente.  
?? stock_policy pendiente.  
?? quality_control pendiente.

## Regla principal

`products.json` es el contrato maestro del producto. Los m?dulos pueden evolucionar por separado, pero la integraci?n final debe respetar el contrato maestro y las reglas documentadas.

No se debe construir l?gica de negocio, scrapers, f?rmulas de stock ni campa?as desde este repositorio en esta etapa. Primero se solidifica el contrato. Despu?s se automatiza. Es as? de f?cil.

## Relación con otros repos del ecosistema

`PIM-DISTRIBUIDORA` forma parte de un ecosistema más grande:

- `ERP`: ASNO nuevo / ERP futuro.
- Scraper ASNO: extracción de datos desde ASNO actual / Wappsi.
- Clientes Inteligentes: clasificación y scoring de clientes.
- Drive/Obsidian: memoria viva del proyecto.

Este repo no reemplaza esos repos. Define contratos, diccionarios, validadores, documentación estable y módulos PIM.

Entrada principal:

`docs/pim_master/00_PIM_MASTER_INDEX.md`

Mapa de repos relacionados:

`docs/pim_master/06_REPOS_RELACIONADOS.md`

## Contract validation

Para validar los contratos JSON contra los schemas formales:

```bash
pip install -r requirements.txt
python scripts/validate_contracts.py
python scripts/validate_contracts.py --include-failures
python scripts/validate_contracts.py --include-dictionaries
python scripts/validate_contracts.py --include-uniqueness
python scripts/validate_contracts.py --include-failures --include-dictionaries --include-uniqueness
```

- `python scripts/validate_contracts.py` valida los ejemplos correctos de `contracts/`.
- `python scripts/validate_contracts.py --include-failures` tambi?n verifica que los ejemplos inv?lidos controlados de `examples/validation_failures/` sean rechazados por el schema.
- `python scripts/validate_contracts.py --include-dictionaries` agrega validaci?n de consistencia contra diccionarios controlados.

La validaci?n actual cubre estructura, campos requeridos, tipos, enums principales y consistencia b?sica de diccionarios de `products.json v1`.

## Dictionary validation

La validaci?n por schema revisa estructura. La validaci?n de diccionarios revisa valores controlados.

```bash
pip install -r requirements.txt
python scripts/validate_dictionaries.py
python scripts/validate_dictionaries.py --include-failures
python scripts/validate_contracts.py --include-dictionaries
```

- `python scripts/validate_dictionaries.py` valida que el producto ejemplo use materiales, colores y unidades existentes en `/dictionaries`.
- `python scripts/validate_dictionaries.py --include-failures` confirma que los ejemplos inv?lidos de `examples/dictionary_failures/` sean rechazados.
- `python scripts/validate_contracts.py --include-dictionaries` ejecuta validaci?n estructural y validaci?n de diccionarios juntas.

## Uniqueness validation

La validaci?n por schema revisa forma. La validaci?n de diccionarios revisa valores controlados. La validaci?n de unicidad revisa consistencia cruzada entre productos y c?digos de barras.

```bash
python scripts/validate_uniqueness.py
python scripts/validate_uniqueness.py --include-failures
python scripts/validate_contracts.py --include-uniqueness
```

- `python scripts/validate_uniqueness.py` valida unicidad de `product.code`, unicidad de barcodes activos, barcode primario por unidad y consistencia b?sica de `barcode_history`.
- `python scripts/validate_uniqueness.py --include-failures` confirma que los ejemplos controlados de `examples/uniqueness_failures/` fallen o emitan warnings esperados.
- `python scripts/validate_contracts.py --include-uniqueness` ejecuta schema validation y validaci?n de unicidad juntas.

## Consolidated validation report

Para generar un reporte consolidado de auditor?a del contrato PIM v1:

```bash
python scripts/generate_validation_report.py
```

Outputs:

```text
reports/pim_contract_v1_validation_report.json
reports/pim_contract_v1_validation_report.md
```

Este reporte resume todas las capas de validaci?n: schema, ejemplos inv?lidos controlados, diccionarios, fallos de diccionario, unicidad y consistencia de barcodes.

No crea l?gica de negocio, scraper, stock, marketing ni media. Es una foto auditable del estado del contrato.



## Naming validation

La validaci?n de nombres revisa que los nombres existentes del producto sigan `docs/naming_rules_v1.md`.

```bash
python scripts/validate_naming.py
python scripts/validate_naming.py --include-failures
python scripts/validate_contracts.py --include-naming
```

Esta validaci?n no genera nombres todav?a. Solo valida los nombres ya presentes en el contrato `products.v1.example.json`.


## Family and variant validation

La validaci?n de familias revisa consistencia entre `contracts/products.v1.example.json` y `contracts/product_families.v1.example.json`.

```bash
python scripts/validate_families.py
python scripts/validate_families.py --include-failures
python scripts/validate_contracts.py --include-families
```

Esta validaci?n no implementa l?gica comercial de variantes. Solo valida relaciones: `family_id`, `children_codes`, `parent_code`, membres?a de hijos, duplicados y advertencias de variante.


## Data quality validation

La validaci?n de `data_quality` revisa gobernanza de datos del producto.

```bash
python scripts/validate_data_quality.py
python scripts/validate_data_quality.py --include-failures
python scripts/validate_contracts.py --include-data-quality
```

`data_quality` no valida calidad f?sica del producto. Calidad f?sica, almacenamiento, humedad, calor, rotaci?n y pol?ticas de stock pertenecen al m?dulo `inventory_flow`.


## Documentation coverage validation

La validaci?n de cobertura documental revisa que cada validador importante tenga documentaci?n asociada y que `README.md` mencione los comandos principales.

```bash
python scripts/validate_documentation_coverage.py
python scripts/validate_contracts.py --include-docs
```

Esta validaci?n no revisa reglas de negocio. Ayuda a mantener el contrato mantenible y auditable.

Comandos principales cubiertos:

```bash
python scripts/validate_contracts.py
python scripts/validate_dictionaries.py
python scripts/validate_uniqueness.py
python scripts/validate_naming.py
python scripts/validate_families.py
python scripts/validate_data_quality.py
python scripts/generate_validation_report.py
```

## PIM Contract v1 release status

`products.json v1` est? listo como contrato maestro base para integraci?n futura de m?dulos.

Documentos de release:

- `docs/release_checklist_v1.md`
- `docs/module_integration_plan.md`

Comando actual de validaci?n final:

```bash
python scripts/validate_contracts.py --include-failures --include-dictionaries --include-uniqueness --include-naming --include-families --include-data-quality --include-docs
python scripts/generate_validation_report.py
```

Este estado no implementa l?gica real de stock, marketing, media, scraper, precios, costos o proveedores. Solo cierra el contrato v1 y define c?mo deben integrarse los m?dulos despu?s.

