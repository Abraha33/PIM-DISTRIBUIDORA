# Naming Validation v1

## Por qu? existe

La validaci?n de nombres existe para comprobar que los nombres ya presentes en `products.json v1` respeten las reglas documentadas en `docs/naming_rules_v1.md`.

Esto no genera nombres. No es un motor comercial. No es scraper. No es marketing. Es control de contrato: mirar el nombre final y verificar que no se haya colado basura o que no falte una pieza clave.

## Nombres validados

? definido

- `names.pos`
- `names.logistics`
- `names.internal`
- `names.ecommerce_short`
- `names.ecommerce_long`

## Componentes requeridos

### POS

Debe incluir:

- `category.final.name`
- material por `attributes.material.abbreviation` o `attributes.material.name`
- `attributes.color.name`
- `attributes.capacity.label` si no est? vac?o
- `attributes.dimensions.label` si no est? vac?o
- `unit_summary.minimum_sale_unit.label`
- `unit_summary.maximum_purchase_unit.label`

No debe incluir:

- `identity.reference.label`
- `identity.brand.name`

### Logistics

Debe incluir:

- `code`
- `identity.reference.label`
- `category.final.name`
- material
- color
- capacidad si existe
- dimensiones si existen
- unidad m?nima
- unidad m?xima

### Internal/admin

Debe incluir:

- `code`
- `category.final.name`
- `identity.reference.label`
- material
- color
- capacidad si existe
- dimensiones si existen
- unidad m?nima
- unidad m?xima

### Ecommerce short

Debe incluir los mismos componentes base que POS.

No debe incluir:

- `identity.reference.label`
- `identity.brand.name`

### Ecommerce long

Debe incluir:

- `category.final.name`
- `identity.brand.name` si no est? vac?o
- material
- color
- capacidad si existe
- dimensiones si existen
- la palabra `Presentaciones:`
- todos los labels activos de `unit_presentation`
- `identity.reference.label` al final o cerca del final si no est? vac?o

## Fallos controlados

Los ejemplos viven en:

```text
examples/naming_failures/
```

Incluyen casos como:

- POS sin material.
- POS con referencia prohibida.
- POS con marca prohibida.
- Logistics sin c?digo.
- Logistics sin referencia.
- Internal sin referencia.
- Ecommerce short con referencia prohibida.
- Ecommerce long sin `Presentaciones:`.
- Ecommerce long sin una unidad activa.
- Nombre con unidad malformada como `CJx200`.

## Qu? no cubre todav?a

?? pendiente

- Generaci?n autom?tica de nombres.
- Orden exacto de todos los componentes.
- Normalizaci?n tipogr?fica avanzada.
- Sin?nimos comerciales.
- Reglas de marketing.
- Reglas espec?ficas por categor?a.

?? decisi?n tomada: esta capa valida nombres existentes, pero no los produce.

?? recomendaci?n experta: validar antes de generar es como revisar que el plano actual no se caiga antes de pedirle a alguien que construya cien planos nuevos. Es disciplina, no burocracia.

## Script relacionado

```bash
scripts/validate_naming.py
```
