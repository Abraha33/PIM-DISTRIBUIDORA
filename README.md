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

## Contract validation

Para validar los contratos JSON contra los schemas formales:

```bash
pip install -r requirements.txt
python scripts/validate_contracts.py
python scripts/validate_contracts.py --include-failures
python scripts/validate_contracts.py --include-dictionaries
python scripts/validate_contracts.py --include-failures --include-dictionaries
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

