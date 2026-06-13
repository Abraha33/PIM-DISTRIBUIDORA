# Validation Failures v1

Este documento registra ejemplos inv?lidos controlados para probar qu? debe rechazar el JSON Schema v1 del PIM de Envax.

La idea no es romper por romper. La idea es documentar el borde del contrato. Un contrato que solo prueba casos felices es como revisar un puente caminando despacito por el medio: fant?stico, pero no alcanza.

## Productos

### `product_missing_code.json`

- Error esperado: falta el campo requerido `code`.
- Por qu? importa: `code` identifica el producto dentro del PIM. Sin ese campo no hay identidad maestra estable.

### `product_invalid_status.json`

- Error esperado: `status` no pertenece al enum permitido: `active`, `inactive`, `pending_review`.
- Por qu? importa: evita estados inventados que despu?s rompen reportes, filtros y procesos.

### `product_missing_unit_summary.json`

- Error esperado: falta el campo requerido `unit_summary`.
- Por qu? importa: el contrato necesita saber unidad m?nima de venta y unidad m?xima de compra sin recalcularlo desde cero cada vez.

### `product_invalid_barcode_status.json`

- Error esperado: `barcode.status` no pertenece al enum permitido: `active`, `inactive`, `deprecated`.
- Por qu? importa: los c?digos de barras tienen ciclo de vida y trazabilidad. Estados libres generan ambig?edad operacional.

### `product_invalid_capacity_value.json`

- Error esperado: `attributes.capacity.value` debe ser `number` o `null`, no `string`.
- Por qu? importa: la capacidad puede usarse despu?s para b?squedas, filtros y comparaciones. Si se guarda como texto, perd?s sem?ntica.

### `product_missing_names.json`

- Error esperado: falta el campo requerido `names`.
- Por qu? importa: los nombres normalizados son salidas centrales del contrato para POS, log?stica, administraci?n y ecommerce.

## Familias de producto

### `family_missing_family_id.json`

- Error esperado: falta el campo requerido `family_id`.
- Por qu? importa: la familia necesita una clave estable para agrupar variantes sin reemplazar `products.json`.

### `family_children_codes_not_array.json`

- Error esperado: `children_codes` debe ser un array de strings.
- Por qu? importa: los hijos de una familia deben poder recorrerse y validarse como lista, no como texto pegado.

## Historial de c?digos de barras

### `barcode_history_invalid_action.json`

- Error esperado: `action` no pertenece al enum permitido: `created`, `activated`, `deactivated`, `updated`, `recycled`.
- Por qu? importa: la trazabilidad depende de acciones conocidas. Si cualquiera escribe cualquier cosa, el historial deja de servir.

### `barcode_history_missing_product_code.json`

- Error esperado: falta el campo requerido `product_code`.
- Por qu? importa: un evento de c?digo de barras debe estar asociado a un producto. Sin producto, no hay trazabilidad real.

## C?mo ejecutar estas pruebas

Validar solo contratos correctos:

```bash
python scripts/validate_contracts.py
```

Validar contratos correctos y confirmar que los inv?lidos fallen:

```bash
python scripts/validate_contracts.py --include-failures
```

## Qu? significa el resultado

- `VALID`: el contrato v?lido cumple el schema.
- `EXPECTED_INVALID`: el ejemplo inv?lido fall? como se esperaba.
- `UNEXPECTED_VALID`: el ejemplo inv?lido pas?, y eso es un problema del schema o del ejemplo.

?? decisi?n tomada: estos ejemplos negativos son documentaci?n viva del contrato. Si un cambio de schema hace que uno de estos archivos pase, hay que revisar si el contrato se relaj? por accidente.
