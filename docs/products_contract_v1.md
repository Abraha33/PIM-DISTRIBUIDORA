# Products Contract v1

## Prop?sito de `products.json`

? definido

`products.json` es el contrato maestro del producto Envax. Su responsabilidad es integrar identidad, categor?a, atributos, unidades, nombres normalizados y bloques pendientes de m?dulos futuros.

No es un scraper, no es un motor de stock y no es un CMS de marketing. Es el plano maestro. Si mezclamos todo ac? sin reglas, despu?s nadie sabe qu? pared sostiene el techo. Ponete las pilas: primero contrato, despu?s l?gica.

## Campos top-level

? definido

- `code`: c?digo interno maestro del producto. Ejemplo: `D753200`.
- `status`: estado operativo del registro. Ejemplo: `active`.
- `is_sellable`: indica si el producto puede venderse.
- `family_id`: v?nculo opcional a una familia en `product_families.json`.
- `identity`: identidad del producto, nombre original, nombre final, referencia y marca.
- `category`: jerarqu?a comercial y categor?a final.
- `attributes`: material, color, capacidad y dimensiones.
- `unit_presentation`: escalera de presentaciones comerciales y log?sticas.
- `unit_summary`: resumen de unidad m?nima de venta y unidad m?xima de compra.
- `names`: nombres derivados para POS, log?stica, administraci?n y ecommerce.
- `commercial`: precios, costos e impuestos pendientes.
- `suppliers`: proveedores pendientes.
- `inventory_flow`: m?dulo pendiente de inventario.
- `marketing`: m?dulo pendiente de marketing.
- `media`: m?dulo pendiente de im?genes.
- `data_quality`: estado de calidad del dato.

## `code` vs `barcode`

?? decisi?n tomada

- `code` identifica el producto dentro del PIM.
- `barcode` identifica una presentaci?n escaneable de una unidad comercial.

Un producto puede tener varias presentaciones y cada presentaci?n puede tener cero, uno o varios c?digos de barras hist?ricos. Por eso los barcodes viven dentro de `unit_presentation[].barcodes` y su trazabilidad se documenta en `barcode_history`.

## Regla de `category.final`

?? decisi?n tomada

`category.final` es la categor?a que entra en los nombres finales. Debe tomar el nivel m?s espec?fico disponible y validado.

Ejemplo:

- mother: `Contenedores`
- child: `Envases Transparentes`
- grandchild: `Sello Plus`
- final: `Sello Plus`

Si existe nivel nieto confiable, `final` debe coincidir con ese nivel.

## Regla de atributos

? definido

`attributes` concentra caracter?sticas f?sicas o descriptivas normalizadas:

- `material`
- `color`
- `capacity`
- `dimensions`

?? recomendaci?n experta

Material y color deben venir de diccionarios controlados. No inventes strings en caliente porque despu?s ten?s `PET`, `P.E.T`, `Pet`, `Pl?stico PET` y una locura c?smica imposible de mantener.

## Regla de `unit_presentation`

? definido

`unit_presentation` representa la escalera de unidades del producto.

Cada entrada debe tener:

- `unit_p`
- `code`
- `name`
- `factor`
- `label`
- `is_minimum_sale_unit`
- `is_maximum_purchase_unit`
- `is_active`
- `barcodes`

El formato de etiqueta es:

```text
CODE(factor)
```

Ejemplos:

- `UND(1)`
- `PAQ(100)`
- `CJ(200)`

## Reglas de nombres

? definido

Los nombres normalizados viven en `names`:

- `pos`
- `logistics`
- `internal`
- `ecommerce_short`
- `ecommerce_long`
- `ecommerce_short_description`
- `ecommerce_description`
- `search_keywords`

?? decisi?n tomada

La referencia no entra en POS ni ecommerce short. S? entra en log?stica, internal/admin y ecommerce long.

## Regla de familia / variante

? definido

`family_id` conecta el producto con `product_families.json` cuando existe una relaci?n padre-hijo o una agrupaci?n por variantes.

Ejemplo: una familia `Bolsa 1.5 KG` puede agrupar variantes por color.

?? pendiente

Todav?a falta definir si todas las familias ser?n manuales, autom?ticas o h?bridas.

## M?dulos pendientes

?? pendiente

- `inventory_flow`: stock level, quality control f?sico y flujo de inventario.
- `marketing`: clientes objetivo, cat?logos, campa?as y promociones.
- `media`: im?genes por uso.

?? revisar despu?s

Cuando existan datos reales de scraper, stock y marketing, se deben completar los bloques pendientes sin romper el contrato `products.json v1`.
