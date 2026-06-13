# Dictionary Validation v1

## Por qu? existe esta validaci?n

JSON Schema valida estructura: campos requeridos, tipos y enums. Eso est? buen?simo, pero no alcanza para un PIM serio.

Un producto puede tener `attributes.material.id` como string y aun as? apuntar a un material inexistente. T?cnicamente pasa el schema, pero conceptualmente est? mal. Ah? entra la validaci?n de diccionarios.

Esto es integridad referencial del contrato. No es l?gica de negocio. No calcula stock, no genera campa?as y no scrapea nada.

## Diccionarios usados

? definido

- `dictionaries/unit_dictionary.json`
- `dictionaries/material_dictionary.json`
- `dictionaries/color_dictionary.json`

## Campos validados

? definido

### Material

- `attributes.material.id` debe existir en `material_dictionary.json`.
- `attributes.material.abbreviation` debe coincidir con la abreviatura del diccionario cuando el id existe.

### Color

- `attributes.color.id` debe existir en `color_dictionary.json`.
- `attributes.color.name` debe coincidir con el nombre del diccionario cuando el id existe.

### Unidades

- `unit_presentation[].code` debe existir en `unit_dictionary.json`.
- `unit_summary.minimum_sale_unit.code` debe existir en `unit_dictionary.json`.
- `unit_summary.maximum_purchase_unit.code` debe existir en `unit_dictionary.json`.
- Los c?digos de `unit_summary` tambi?n deben existir dentro de `unit_presentation[].code` del producto.
- `unit_presentation[].label` debe respetar el formato `CODE(factor)`.

Ejemplo:

```text
code = CJ
factor = 200
label = CJ(200)
```

## Errores que detecta

? definido

- Material inexistente.
- Color inexistente.
- Unidad inexistente.
- Unidad resumen que existe en el diccionario pero no est? en las presentaciones del producto.
- Abreviatura de material inconsistente con el diccionario.
- Nombre de color inconsistente con el diccionario.
- Label de unidad mal formado.

## Ejemplos inv?lidos controlados

Los ejemplos negativos viven en:

```text
examples/dictionary_failures/
```

Incluyen:

- `product_invalid_material_id.json`
- `product_invalid_color_id.json`
- `product_invalid_unit_code.json`
- `product_unit_summary_not_in_unit_presentation.json`
- `product_invalid_unit_label.json`

## C?mo ejecutar

Validar producto v?lido contra diccionarios:

```bash
python scripts/validate_dictionaries.py
```

Validar producto v?lido y confirmar que los ejemplos inv?lidos fallen:

```bash
python scripts/validate_dictionaries.py --include-failures
```

Ejecutar junto con schema validation:

```bash
python scripts/validate_contracts.py --include-dictionaries
python scripts/validate_contracts.py --include-failures --include-dictionaries
```

## Qu? NO valida todav?a

?? pendiente

- Jerarqu?a real de categor?as.
- Unicidad global de c?digos de producto.
- Unicidad global de barcodes.
- F?rmulas de stock.
- Pol?ticas de inventario.
- Quality control f?sico.
- Reglas comerciales de marketing.
- Existencia real de im?genes.
- Integraci?n con scraper.

?? decisi?n tomada: esta validaci?n solo controla coherencia contra diccionarios. No reemplaza validadores de dominio futuros.

?? recomendaci?n experta: separ? validaci?n estructural, validaci?n referencial y reglas de negocio. Si met?s todo en el mismo balde, despu?s no sab?s si fall? el plano, el material o el alba?il.
