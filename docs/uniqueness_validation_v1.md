# Uniqueness Validation v1

## Por qu? existe esta validaci?n

JSON Schema valida la forma. Dictionary validation valida valores controlados. Pero hay errores que viven entre registros, no dentro de un solo campo.

Ejemplos claros:

- dos productos con el mismo `code`.
- dos productos con el mismo barcode activo.
- un historial de barcode apuntando a un producto que no existe.

Eso no lo resolv?s con schema sin convertirlo en una locura c?smica. Para eso existe esta validaci?n cruzada.

## Reglas validadas

? definido

### 1. Unicidad de c?digo de producto

Cada `product.code` debe ser ?nico dentro de la lista de productos validada.

### 2. Unicidad de barcode activo

Todo `barcode.value` con `status = active` debe ser ?nico entre todos los productos y unidades.

Barcodes `inactive` o `deprecated` pueden repetirse siempre que no est?n activos.

### 3. Barcode primario por unidad

Dentro de cada `unit_presentation`, puede existir como m?ximo un barcode activo con `is_primary = true`.

### 4. Historial apunta a producto/unidad existente

Cada registro de `barcode_history` debe apuntar a:

- `product_code` existente.
- `unit_code` existente dentro del producto referenciado.

### 5. Consistencia de acci?n de historial

- `deactivated`: el barcode debe existir en la unidad referenciada y su estado actual debe ser `inactive` o `deprecated`.
- `activated`: el barcode debe existir en la unidad referenciada y su estado actual debe ser `active`.
- `created`: el barcode debe existir en la unidad referenciada.
- `recycled`: se permite, pero emite warning si no existe en ning?n lado como `inactive` o `deprecated`.

## Ejemplos que deben fallar

Los ejemplos viven en:

```text
examples/uniqueness_failures/
```

Incluyen:

- `products_duplicate_code.json`: dos productos con el mismo `code`.
- `products_duplicate_active_barcode.json`: dos productos o unidades comparten el mismo barcode activo.
- `product_multiple_primary_barcodes_same_unit.json`: una unidad tiene m?s de un barcode activo primario.
- `barcode_history_unknown_product.json`: historial referencia producto inexistente.
- `barcode_history_unknown_unit.json`: historial referencia unidad inexistente en el producto.
- `barcode_history_deactivated_but_active.json`: acci?n `deactivated`, pero el barcode sigue activo.
- `barcode_history_activated_but_inactive.json`: acci?n `activated`, pero el barcode est? inactivo.

## Ejemplo que debe advertir

- `barcode_history_recycled_warning.json`: acci?n `recycled`, pero el barcode no existe como `inactive` o `deprecated` en ning?n producto.

Este caso emite `WARNING_UNIQUENESS_RULE`, no `INVALID_UNIQUENESS_RULE`.

## C?mo ejecutar

```bash
python scripts/validate_uniqueness.py
python scripts/validate_uniqueness.py --include-failures
python scripts/validate_contracts.py --include-uniqueness
python scripts/validate_contracts.py --include-failures --include-dictionaries --include-uniqueness
```

## Qu? NO valida todav?a

?? pendiente

- Historial temporal completo de barcodes.
- Orden cronol?gico de eventos.
- Reglas de reciclaje por proveedor o pa?s.
- Integraci?n con datos reales de scraper.
- Pol?ticas comerciales de activaci?n/desactivaci?n.
- Costos, precios o proveedores.
- Stock, marketing o media.

?? decisi?n tomada: esta validaci?n es de consistencia cruzada controlada para ejemplos del contrato v1. No es un motor de auditor?a hist?rico completo.

?? recomendaci?n experta: no fuerces JSON Schema a validar relaciones entre archivos. Us? scripts claros y chicos. Cada herramienta a su lugar, como en una obra bien dirigida.
