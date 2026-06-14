# Family Validation v1

## Por qu? existe

La validaci?n de familias existe para comprobar que `products.json v1` y `product_families.json v1` se referencien de forma coherente.

`product_families` no reemplaza al contrato maestro. Es una capa de agrupaci?n para productos relacionados, variantes y posibles padres conceptuales. Si esa capa queda floja, despu?s termin?s con productos hu?rfanos o familias que apuntan a c?digos inexistentes. Eso no es arquitectura, es una obra sin columnas.

## Para qu? sirve `product_families.json`

? definido

- Agrupar productos relacionados.
- Declarar hijos con `children_codes`.
- Declarar un posible `parent_code`.
- Declarar ejes de variante con `variant_axis`, por ejemplo `color`.

## C?mo conecta `family_id`

Un producto puede tener `family_id`.

Si lo tiene:

- ese `family_id` debe existir en `product_families`.
- si el producto aparece en `children_codes`, su `family_id` debe coincidir con la familia que lo contiene.

## Reglas inv?lidas

? fail

- Producto con `family_id` inexistente.
- Familia con `children_codes` que no existen en productos.
- Producto listado como hijo, pero con `family_id` distinto.
- Producto listado como hijo en m?s de una familia.
- Producto con `is_family_parent = true` y `family_id = null`.

## Advertencias

?? warning

- `parent_code` no existe en productos. Puede ser agrupaci?n conceptual.
- `variant_axis` incluye `color`, pero el hijo no tiene `attributes.color.name`.
- Producto con `is_sellable = false` y sin ser `is_family_parent`; puede estar incompleto.

## Qu? no valida todav?a

?? pendiente

- Estrategia comercial de variantes.
- Herencia de atributos desde padre a hijos.
- Reglas por categor?a.
- L?gica de stock, marketing o media.
- Precios, costos o proveedores.
- Generaci?n autom?tica de familias.

?? decisi?n tomada: esta capa valida relaciones, no decide estrategia comercial.

?? recomendaci?n experta: familia es estructura, no magia. Si quer?s variantes robustas ma?ana, hoy necesit?s relaciones limpias y auditables.
