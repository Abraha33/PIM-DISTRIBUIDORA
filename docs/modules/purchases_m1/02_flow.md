---
module: purchases_m1
status: partial
type: purchasing
source: chatgpt
last_review: 2026-06-19
---

# Flujo funcional — Compras M1

## Diagrama de flujo

```
1. Llega factura o compra
       │
2. Se registra o detecta la compra desde ASNO/Wappsi
       │
3. Se identifican proveedor, factura y productos
       │
4. Se toma evidencia/foto de recepción
       │
5. Se revisa si la mercancía llegó completa y en buen estado
       │
6. Se compara contra productos PIM normalizados
       │
7. Se detectan productos nuevos, reposiciones relevantes o novedades
       │
8. Se define si requiere decisión de precio
       │
9. Se genera aviso para vendedores o puntos de venta interesados
       │
10. La información queda lista para alimentar PIM y, en el futuro, ERP
```

## Pasos detallados

### 1. Detección de compra

- Una factura o compra llega desde ASNO/Wappsi.
- `Scraper_Asno` extrae los datos crudos.
- `PIM-DISTRIBUIDORA` recibe la notificación o el registro.

### 2. Registro de compra

- Se crea un registro de compra M1.
- Se asigna un `purchase_m1_id`.
- Se registra la fuente (`source_system`).

### 3. Identificación

- Se identifica el proveedor (nombre, ID si existe).
- Se registra el número de factura y fecha.
- Se listan los productos comprados con códigos y nombres raw.

### 4. Evidencia de recepción

- Se toma foto de factura y/o mercancía recibida.
- Las fotos se asocian al registro como evidencia.
- Se registra fecha y hora de recepción.

### 5. Revisión de recepción

- Se valida si la mercancía llegó completa.
- Se verifica estado físico.
- Se registran diferencias (si las hay).

### 6. Comparación PIM

- Los productos raw se intentan mapear contra `products.json` (PIM normalizado).
- Los que no existan se marcan como `new_product_candidate`.

### 7. Detección de novedades

- Productos nuevos para el catálogo.
- Reposiciones relevantes (productos que no se compraban hace tiempo).
- Se marca `new_product_notice_candidate`.

### 8. Decisión de precio

- Se evalúa si el producto requiere decisión de precio de venta.
- Si aplica, se marca `requires_price_decision`.
- La decisión puede tomarla un usuario humano.

### 9. Aviso

- Se genera aviso para vendedores o puntos de venta.
- El canal puede ser WhatsApp, dashboard, reporte o ERP futuro.

### 10. Alimentación

- La compra procesada queda disponible para PIM y para ERP futuro.

## Estados del flujo

```
detected
pending_reception
received_with_evidence
under_review
approved
incomplete
rejected
requires_price_decision
ready_for_notice
closed
```

## Relación con módulos vecinos

| Paso | Módulo relacionado |
|---|---|
| 4-5 | `purchase_reception` — evidencia y validación de recepción |
| 7-9 | `new_products_notice` — aviso después de revisión |
| 8 | `selling_price_decision` — decisión de precio de venta |
