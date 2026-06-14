# M?dulo de compra asistida por factura + PIM + scraper

## Estado

Idea / backlog / no implementado.

Este documento registra una funcionalidad futura. No define implementaci?n final, no crea scraper funcional y no automatiza decisiones comerciales todav?a.

## Problema que resuelve

El proceso de registrar compras puede consumir mucho tiempo cuando el encargado debe leer facturas o listas de proveedor, identificar productos, traducir nombres ambiguos, cargar cantidades, costos, descuentos, fletes, impuestos y luego revisar precios de venta.

La idea busca reducir trabajo manual repetitivo y errores de digitaci?n, manteniendo el control humano sobre decisiones sensibles como precios y m?rgenes.

Frase resumen:

> El cajero toma la foto; el sistema arma la compra; el encargado solo define precios.

## Flujo de usuario

1. El cajero o encargado toma una foto de una factura o lista de proveedor.
2. El sistema lee la factura mediante OCR o lectura inteligente.
3. El sistema extrae proveedor, productos, cantidades, costos, descuentos y fletes si existen.
4. El sistema compara los productos detectados contra el PIM.
5. Los productos dudosos quedan marcados para revisi?n manual.
6. El sistema prepara una compra o precompra.
7. El encargado revisa especialmente precios de venta y m?rgenes.
8. El encargado decide si el precio sube, baja o se mantiene.
9. La compra se guarda.
10. El sistema registra historial de costos y precios para comparaciones futuras.

## Flujo t?cnico conceptual

```text
Factura / lista proveedor
        ?
OCR / lectura
        ?
Normalizaci?n con PIM
        ?
Validaci?n de productos
        ?
Scraper llena compra en sistema web
        ?
Encargado revisa precios/m?rgenes
        ?
Compra guardada
        ?
Historial de costos actualizado
```

## Flujo t?cnico deseado

1. Entrada de factura o lista de proveedor como imagen, PDF o texto.
2. OCR o lectura inteligente para extraer:
   - proveedor
   - productos
   - cantidades
   - costos
   - descuentos si existen
   - fletes si existen
3. Normalizaci?n contra el PIM para traducir nombres ambiguos o incompletos al producto correcto.
4. Clasificaci?n de coincidencias:
   - coincidencia confiable
   - coincidencia dudosa
   - producto no encontrado
5. Generaci?n de una estructura de compra interna.
6. En una versi?n posterior, scraper para entrar al sistema web de compras:
   - ir a Compras
   - Agregar compra
   - seleccionar proveedor
   - agregar productos uno por uno
   - editar cada art?culo
   - configurar presentaci?n
   - unidad de medida
   - factores
   - impuestos
   - costos
   - descuentos
   - fletes/prorrateo si aplica
   - forma de pago: contado, cr?dito o anticipo
   - estado aprobado/no aprobado
7. Revisi?n humana de precios, m?rgenes y condiciones comerciales.
8. Guardado de compra.
9. Registro hist?rico para comparar costos y precios futuros.

## M?dulos involucrados

- `PIM / products.json`: identificaci?n normalizada del producto.
- `dictionaries`: unidades, materiales, colores y valores controlados cuando apliquen.
- `commercial`: precios, costos, impuestos y proveedores.
- `barcode_history`: apoyo futuro para trazabilidad si la factura contiene c?digos.
- `scraper/commercial`: carga o prellenado en sistema web externo.
- `inventory_flow`: posible impacto futuro en reabastecimiento y an?lisis de compra.
- `data_quality`: marcar dudas, inconsistencias o campos pendientes.

## Qu? automatiza

- Lectura inicial de factura o lista.
- Extracci?n de l?neas de compra.
- Normalizaci?n de nombres contra el PIM.
- Detecci?n de productos dudosos.
- Generaci?n de JSON de compra.
- Preparaci?n de datos para carga en sistema web.
- Registro hist?rico de costos y precios cuando exista el m?dulo correspondiente.

## Qu? NO debe automatizar

No debe automatizar completamente la decisi?n del precio de venta.

El sistema puede sugerir precios usando:

- costo nuevo
- costo anterior
- precio actual
- margen deseado
- precio de competencia si existe

Pero la decisi?n final debe quedar en manos del encargado.

Tambi?n debe evitar:

- sobrescribir productos normalizados sin revisi?n
- aprobar compras dudosas autom?ticamente
- modificar precios de venta sin decisi?n humana
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
- barcodes por presentaci?n
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

## Riesgos t?cnicos

- OCR con baja precisi?n por fotos borrosas o facturas mal impresas.
- Nombres de productos ambiguos o incompletos.
- Diferencias entre unidad facturada y unidad del PIM.
- Costos con descuentos, bonificaciones o fletes dif?ciles de prorratear.
- Cambios en la interfaz web del sistema de compras que rompan el scraper.
- Riesgo de actualizar precios sin revisi?n humana.
- Productos nuevos que todav?a no existen en el PIM.
- Proveedores con formatos de factura diferentes.

## Pruebas futuras

- Probar lectura con facturas reales y fotos de distinta calidad.
- Medir tasa de coincidencia contra el PIM.
- Medir cantidad de productos dudosos por proveedor.
- Validar extracci?n de cantidades y costos.
- Validar diferencias entre unidad de factura y `unit_presentation`.
- Probar generaci?n de JSON de compra sin tocar el sistema web.
- Probar scraper con una compra de un solo producto en ambiente controlado.
- Revisar errores antes de permitir carga m?ltiple.

## Posible MVP

### Primera versi?n

- Entrada manual de texto o foto procesada externamente.
- Lectura de productos, cantidades y costos.
- Match contra PIM.
- Generaci?n de JSON de compra.
- Reporte de productos dudosos.
- No llenar todav?a la web autom?ticamente.

### Segunda versi?n

- Scraper que cree una compra con 1 producto.

### Tercera versi?n

- Scraper con m?ltiples productos.
- Edici?n de presentaci?n, factor, impuestos y costos.
- Revisi?n de precios.

### Cuarta versi?n

- Descuentos.
- Fletes/prorrateo.
- Cr?dito, contado o anticipo.
- Historial de costos.
- Sugerencias de precio.

## Decisi?n de control humano

?? La automatizaci?n puede preparar informaci?n, sugerir y reducir carga manual, pero no debe reemplazar la decisi?n humana sobre precios de venta y m?rgenes.

?? Recomendaci?n experta: primero construir lectura + normalizaci?n + JSON. Despu?s scraper m?nimo. Reci?n al final pensar en carga completa. Si se automatiza todo de entrada, el riesgo operativo explota.
