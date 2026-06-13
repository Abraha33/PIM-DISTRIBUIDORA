# Schema Contracts v1

## Qu? es JSON Schema

JSON Schema es una especificaci?n para describir y validar la forma de un documento JSON.

En este repositorio se usa para comprobar que los contratos de ejemplo del PIM de Envax tengan los campos obligatorios, tipos correctos y valores permitidos.

Dicho simple: el schema es el plano t?cnico. No construye la casa, pero te dice si la pared est? donde el plano dice que tiene que estar.

## Schemas creados

? definido

- `schemas/products.v1.schema.json`: valida `contracts/products.v1.example.json`.
- `schemas/product_families.v1.schema.json`: valida `contracts/product_families.v1.example.json`.
- `schemas/barcode_history.v1.schema.json`: valida `contracts/barcode_history.v1.example.json`.

## C?mo validar

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar validaci?n:

```bash
python scripts/validate_contracts.py
```

Salida esperada:

```text
VALID: contracts/products.v1.example.json
VALID: contracts/product_families.v1.example.json
VALID: contracts/barcode_history.v1.example.json
```

Si un contrato no cumple, el script imprime:

```text
INVALID: ruta/al/archivo.json | campo: detalle del error
```

## Qu? valida el schema

? definido

- Campos requeridos.
- Tipos b?sicos: string, number, integer, boolean, array, object, null.
- Enums definidos para estados.
- Estructura esperada de identidad, categor?a, atributos, unidades, nombres, m?dulos pendientes y calidad de datos.
- Formato `date` en `barcode_history.date`.

## Qu? NO valida el schema

?? pendiente

El schema no valida l?gica de negocio compleja. Esto es intencional.

No valida todav?a:

- jerarqu?a real entre `category.mother`, `category.child`, `category.grandchild` y `category.final`.
- si `category.final` coincide efectivamente con la ?ltima categor?a disponible.
- f?rmulas de stock.
- pol?ticas de inventario.
- reglas de quality control f?sico.
- l?gica de marketing.
- reglas de media o im?genes.
- integraci?n con scraper.
- existencia real de c?digos en diccionarios.
- unicidad global de barcodes.

## Decisi?n arquitect?nica

?? decisi?n tomada

La validaci?n v1 se limita a estructura y contrato. No mete reglas operativas todav?a.

?? recomendaci?n experta

No conviertas JSON Schema en un monstruo que intente resolver toda la empresa. Para eso despu?s se crean validadores de dominio, pipelines de calidad y tests espec?ficos. Cada herramienta a su laburo, hermano.
