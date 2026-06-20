# Module Integration Plan — PIM Contract v1

## Objetivo

Este documento define cómo deben integrarse los módulos futuros dentro de `products.json` sin romper el contrato maestro v1.

La regla principal es simple: cada módulo debe escribir únicamente en su sección asignada, salvo revisión explícita. Si un módulo necesita tocar otra sección, debe generar una señal, una pregunta abierta o un evento separado. No se sobrescribe silenciosamente.

## Principios obligatorios

- Cada módulo escribe solo en su sección asignada del Final JSON Product.
- `raw` no se destruye: se conserva como evidencia/fuente para auditoría y trazabilidad.
- Los campos normalizados están protegidos.
- Los módulos automáticos generan señales, alertas o pendientes; no sobrescriben sin revisión.
- Compras y órdenes pueden generar eventos separados; no necesariamente modifican el producto maestro.
- Marketing, media e inventory_flow son capas especializadas, no reemplazos del contrato maestro.
- El scraper alimenta datos dinámicos y reportes; no decide reglas finales.
- `products.json v1` se mantiene compatible hasta que exista una decisión explícita de cambio de contrato.

## Orden recomendado de integración

1. `inventory_flow`
2. `marketing`
3. `media`
4. `purchases_m1`
5. `purchase_orders`
6. `purchase_reception`
7. `new_products_notice`
8. `commercial_pricing`
9. `selling_price_decision`
10. `price_comparison`
11. `voice_inventory`
12. `asno_wappsi_scraper_integration`

Este orden protege el contrato: primero se entiende el flujo operativo del producto, después su comunicación comercial, luego sus activos visuales y finalmente las capas de compra, pricing, captura e integración automática.

## 1. inventory_flow

`inventory_flow` debe actualizar únicamente la sección:

```text
products[].inventory_flow
```

Responsabilidades futuras:

- stock level
- flujo de inventario
- rotación
- caja operativa
- espacio físico
- temporada
- inventario estratégico
- riesgo físico
- señales de reabastecimiento
- diagnóstico de inventario débil, básico o estratégico

No debe modificar:

- `identity`
- `category`
- `attributes`
- `names`
- `marketing`
- `media`
- `commercial`

## 2. marketing

`marketing` debe actualizar únicamente la sección:

```text
products[].marketing
```

Responsabilidades futuras:

- clientes objetivo
- segmentos
- etiquetas de catálogo
- etiquetas de campaña
- keywords comerciales
- descripciones ecommerce
- promociones planificadas
- mensajes para WhatsApp, historias y campañas

No debe decidir stock ni precios finales.

## 3. media

`media` debe actualizar únicamente la sección:

```text
products[].media
```

Responsabilidades futuras:

- imágenes principales
- imágenes por uso
- imágenes de catálogo
- imágenes de campaña
- imágenes técnicas
- evidencia fotográfica cuando se referencia desde eventos
- relación entre imagen y presentación del producto

Debe separar foto de evidencia vs imagen comercial. No debe usar imágenes para redefinir identidad, categoría o atributos del producto.

## 4. purchases_m1

`purchases_m1` documenta ingreso de compra, factura, proveedor, costos, fletes, descuentos, pago e incidencias.

Puede alimentar referencias en:

```text
products[].suppliers
products[].commercial
```

Pero compras puede existir como evento separado cuando el dato pertenece a una compra específica y no al producto maestro.

No reemplaza ASNO ni ERP.

## 5. purchase_orders

`purchase_orders` trabaja faltantes, cotización, orden de compra, proveedor, WhatsApp y revisión humana.

Debe generar eventos o documentos de orden de compra. Puede leer señales de:

```text
products[].inventory_flow
products[].suppliers
```

No debe confirmar compras ni modificar producto maestro sin revisión.

## 6. purchase_reception

`purchase_reception` trabaja llegada de mercancía, evidencia, recepción parcial/completa, incidencias y validación.

Puede generar señales hacia:

```text
products[].inventory_flow
products[].media
products[].suppliers
```

La evidencia no convierte automáticamente una imagen en asset comercial. Primero se clasifica.

## 7. new_products_notice

`new_products_notice` prepara avisos internos para vendedores y puntos de venta cuando un producto es nuevo o reabastecido.

Puede leer:

```text
products[].marketing
products[].commercial
products[].media
```

No todo producto recibido genera aviso. El aviso debe pasar por criterio humano o marca explícita como candidato.

## 8. commercial_pricing

`commercial_pricing` trabaja margen, competencia, precio sugerido y alertas comerciales.

Debe actualizar o proponer datos en:

```text
products[].commercial
```

El resultado es una sugerencia o alerta, no una decisión final.

## 9. selling_price_decision

`selling_price_decision` toma las señales de pricing y registra la decisión del encargado.

El sistema sugiere; el encargado decide.

No debe existir aprobación automática de precio final sin revisión humana.

## 10. price_comparison

`price_comparison` separa dos mundos que NO son lo mismo:

1. Comparación interna de compra: costo anterior vs costo nuevo.
2. Precios comerciales: mercado, competencia y precio de venta.

Puede leer `suppliers`, `commercial` y eventos de compra, pero debe entregar comparaciones separadas.

## 11. voice_inventory

`voice_inventory` diseña captura por voz:

```text
voz → producto → cantidad → ubicación → validación
```

La transcripción cruda no es inventario validado. Si hay ambigüedad, genera pendiente de revisión.

## 12. asno_wappsi_scraper_integration

`scraper/commercial` debe alimentar principalmente:

```text
products[].commercial
products[].suppliers
```

También puede alimentar señales para:

```text
products[].inventory_flow
reports
```

Debe preservar los campos manuales normalizados salvo revisión explícita:

- `identity`
- `category`
- `attributes`
- `names`
- `unit_presentation`
- `unit_summary`

El scraper alimenta; no decide reglas finales.

## Regla de protección de campos normalizados

Los módulos automáticos no deben sobrescribir campos normalizados manualmente sin auditoría.

Campos protegidos:

- `code`
- `identity`
- `category`
- `attributes`
- `unit_presentation`
- `unit_summary`
- `names`
- `family_id`

Si un módulo detecta una diferencia, debe generar una señal o pendiente de revisión, no sobrescribir silenciosamente.

## Integración con products.json

Cada integración debe seguir este flujo:

```text
módulo separado
→ preservación de raw/fuente
→ validación del módulo
→ revisión de impacto
→ actualización de sección asignada o evento separado
→ validación completa del contrato
→ reporte consolidado
```

## Qué no se implementa en este documento

- fórmulas reales de stock
- reglas finales de marketing
- reglas finales de imágenes
- scraper productivo
- importación/exportación ERP
- automatizaciones
- cambios de schema productivo

**Decisión tomada:** los módulos se integran como capas especializadas dentro de `products.json`, no como reemplazos del contrato maestro.

**Recomendación experta:** si un módulo quiere tocar todo, el módulo está mal diseñado. Un módulo sano tiene frontera clara. Sin frontera, no hay arquitectura: hay barro.
