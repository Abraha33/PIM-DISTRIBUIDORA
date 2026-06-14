# Módulo de compra asistida por factura + PIM + scraper

## Estado

Idea / backlog / no implementado.

Este documento registra una funcionalidad futura. No define implementación final, no crea scraper funcional y no automatiza decisiones comerciales todavía.

## Problema que resuelve

El proceso de registrar compras puede consumir mucho tiempo cuando el encargado debe leer facturas o listas de proveedor, identificar productos, traducir nombres ambiguos, cargar cantidades, costos, descuentos, fletes, impuestos y luego revisar precios de venta.

La idea busca reducir trabajo manual repetitivo y errores de digitación, manteniendo el control humano sobre decisiones sensibles como precios y márgenes.

Frase resumen:

> El cajero toma la foto; el sistema arma la compra; el encargado solo define precios.

## Flujo de usuario

1. El cajero o encargado toma una foto de una factura o lista de proveedor.
2. El sistema lee la factura mediante OCR o lectura inteligente.
3. El sistema extrae proveedor, productos, cantidades, costos, descuentos y fletes si existen.
4. El sistema compara los productos detectados contra el PIM.
5. Los productos dudosos quedan marcados para revisión manual.
6. El sistema prepara una compra o precompra.
7. El encargado revisa especialmente precios de venta y márgenes.
8. El encargado decide si el precio sube, baja o se mantiene.
9. La compra se guarda.
10. El sistema registra historial de costos y precios para comparaciones futuras.

## Flujo técnico conceptual

```text
Factura / lista proveedor
        ↓
OCR / lectura
        ↓
Normalización con PIM
        ↓
Validación de productos
        ↓
Scraper llena compra en sistema web
        ↓
Encargado revisa precios/márgenes
        ↓
Compra guardada
        ↓
Historial de costos actualizado
```

## Flujo técnico deseado

1. Entrada de factura o lista de proveedor como imagen, PDF o texto.
2. OCR o lectura inteligente para extraer:
   - proveedor
   - productos
   - cantidades
   - costos
   - descuentos si existen
   - fletes si existen
3. Normalización contra el PIM para traducir nombres ambiguos o incompletos al producto correcto.
4. Clasificación de coincidencias:
   - coincidencia confiable
   - coincidencia dudosa
   - producto no encontrado
5. Generación de una estructura de compra interna.
6. En una versión posterior, scraper para entrar al sistema web de compras:
   - ir a Compras
   - Agregar compra
   - seleccionar proveedor
   - agregar productos uno por uno
   - editar cada artículo
   - configurar presentación
   - unidad de medida
   - factores
   - impuestos
   - costos
   - descuentos
   - fletes/prorrateo si aplica
   - forma de pago: contado, crédito o anticipo
   - estado aprobado/no aprobado
7. Revisión humana de precios, márgenes y condiciones comerciales.
8. Guardado de compra.
9. Registro histórico para comparar costos y precios futuros.

## Módulos involucrados

- `PIM / products.json`: identificación normalizada del producto.
- `dictionaries`: unidades, materiales, colores y valores controlados cuando apliquen.
- `commercial`: precios, costos, impuestos y proveedores.
- `barcode_history`: apoyo futuro para trazabilidad si la factura contiene códigos.
- `scraper/commercial`: carga o prellenado en sistema web externo.
- `inventory_flow`: posible impacto futuro en reabastecimiento y análisis de compra.
- `data_quality`: marcar dudas, inconsistencias o campos pendientes.

## Qué automatiza

- Lectura inicial de factura o lista.
- Extracción de líneas de compra.
- Normalización de nombres contra el PIM.
- Detección de productos dudosos.
- Generación de JSON de compra.
- Preparación de datos para carga en sistema web.
- Registro histórico de costos y precios cuando exista el módulo correspondiente.

## Qué NO debe automatizar

No debe automatizar completamente la decisión del precio de venta.

El sistema puede sugerir precios usando:

- costo nuevo
- costo anterior
- precio actual
- margen deseado
- precio de competencia si existe

Pero la decisión final debe quedar en manos del encargado.

También debe evitar:

- sobrescribir productos normalizados sin revisión
- aprobar compras dudosas automáticamente
- modificar precios de venta sin decisión humana
- asumir equivalencias de producto con baja confianza
- cargar fletes o descuentos sin trazabilidad

## Datos necesarios del PIM

- `code`
- `identity.original_name`
- `identity.final_name`
- `identity.reference`
- `identity.brand`
- `category.final`
- `attributes`
- `unit_presentation`
- `unit_summary`
- barcodes por presentación
- `suppliers`
- `commercial.prices`
- `commercial.costs`
- `data_quality`

## Estados sugeridos del proceso

- `factura_recibida`
- `factura_leida`
- `proveedor_detectado`
- `productos_detectados`
- `productos_validados_con_pim`
- `productos_dudosos`
- `compra_prellenada`
- `pendiente_revision_precios`
- `precios_revisados`
- `compra_guardada`
- `error_revision_manual`

## Riesgos técnicos

- OCR con baja precisión por fotos borrosas o facturas mal impresas.
- Nombres de productos ambiguos o incompletos.
- Diferencias entre unidad facturada y unidad del PIM.
- Costos con descuentos, bonificaciones o fletes difíciles de prorratear.
- Cambios en la interfaz web del sistema de compras que rompan el scraper.
- Riesgo de actualizar precios sin revisión humana.
- Productos nuevos que todavía no existen en el PIM.
- Proveedores con formatos de factura diferentes.

## Pruebas futuras

- Probar lectura con facturas reales y fotos de distinta calidad.
- Medir tasa de coincidencia contra el PIM.
- Medir cantidad de productos dudosos por proveedor.
- Validar extracción de cantidades y costos.
- Validar diferencias entre unidad de factura y `unit_presentation`.
- Probar generación de JSON de compra sin tocar el sistema web.
- Probar scraper con una compra de un solo producto en ambiente controlado.
- Revisar errores antes de permitir carga múltiple.

## Posible MVP

### Primera versión

- Entrada manual de texto o foto procesada externamente.
- Lectura de productos, cantidades y costos.
- Match contra PIM.
- Generación de JSON de compra.
- Reporte de productos dudosos.
- No llenar todavía la web automáticamente.

### Segunda versión

- Scraper que cree una compra con 1 producto.

### Tercera versión

- Scraper con múltiples productos.
- Edición de presentación, factor, impuestos y costos.
- Revisión de precios.

### Cuarta versión

- Descuentos.
- Fletes/prorrateo.
- Crédito, contado o anticipo.
- Historial de costos.
- Sugerencias de precio.

## Decisión de control humano

📌 La automatización puede preparar información, sugerir y reducir carga manual, pero no debe reemplazar la decisión humana sobre precios de venta y márgenes.

🧠 Recomendación experta: primero construir lectura + normalización + JSON. Después scraper mínimo. Recién al final pensar en carga completa. Si se automatiza todo de entrada, el riesgo operativo explota.
