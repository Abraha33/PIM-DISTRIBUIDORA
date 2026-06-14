# Module Map M1 — PIM Envax

## Estado

M1 draft / base de trabajo.

## Principio general

`products_contract` es la columna vertebral.

Los demás módulos no deben modificar directamente `products.json v1`.

Cada módulo produce salidas que podrán integrarse después en futuras versiones del contrato.

## Módulos principales

## 1. products_contract

### Owns

- contrato maestro del producto
- estructura `products.json`
- schemas
- validadores
- diccionarios
- naming rules
- familias/variantes
- `data_quality`
- reporte consolidado

### Does not own

- stock dinámico
- rotación
- campañas
- imágenes
- scraping runtime
- precios/costos dinámicos

### Status

released v1

## 2. inventory_flow

### Owns

- stock level
- rotación
- quality control físico
- sensores de inventario
- reglas M1
- tickets operativos
- casos de uso de inventario
- flujo de caja operativo desde inventario
- estructura JSON del módulo `inventory_flow`

### Does not own

- precio final de remate
- campañas
- diseño gráfico
- extracción scraper
- contrato maestro v1

### Submodules

- `rotation_sensor`
- `cashflow_sensor`
- `space_sensor`
- `strategic_stock_sensor`
- `season_opportunity_sensor`
- `physical_quality_control`
- `inventory_tickets`
- `inventory_rules_m1`

## 3. marketing

### Owns

- clientes objetivo
- campañas
- catálogos
- promociones
- mensajes comerciales
- segmentación comercial
- conexión comercial de productos dormidos

### Does not own

- detección matemática de stock dormido
- costo/precio base
- imagen técnica del producto
- stock físico

### Submodules

- `customer_segments`
- `catalog_tags`
- `campaign_tags`
- `dormant_stock_campaigns`
- `whatsapp_sales_support`

## 4. media

### Owns

- imágenes del producto
- imagen principal
- fotos por presentación
- calidad visual
- activos para ecommerce
- activos para WhatsApp/catálogo

### Does not own

- datos técnicos del producto
- stock
- precio
- campañas
- scraper de negocio

### Submodules

- `product_images`
- `presentation_images`
- `visual_quality`
- `ecommerce_assets`
- `whatsapp_assets`

## 5. scraper_data_ingestion

### Owns

- extracción desde Wappsi
- datos raw
- datos clean
- normalización inicial
- historial de extracción
- auditorías de extracción
- control de errores del scraper

### Does not own

- decisiones comerciales
- reglas de stock
- campañas
- diseño de imágenes
- contrato maestro final sin validación

### Submodules

- `wappsi_scraper`
- `raw_products`
- `clean_products`
- `extraction_reports`
- `normalization_pipeline`

## 6. commercial

### Owns

- precios
- costos
- márgenes
- proveedores
- impuestos
- listas de precio
- historial comercial
- sugerencias de precios

### Does not own

- stock físico
- imágenes
- campañas creativas
- extracción raw
- estructura base del producto

### Submodules

- `prices`
- `costs`
- `margins`
- `suppliers`
- `taxes`
- `price_history`
- `margin_rules`

## Reglas de frontera

### 1. Stock dormido

- **Detection:** `inventory_flow`
- **Commercial action:** `marketing` / `commercial`

### 2. Remate

- **Trigger:** `inventory_flow`
- **Final price:** `commercial`
- **Campaign:** `marketing`
- **Visual asset:** `media`

### 3. Producto con imagen mala

- **Detection:** `media`
- **If missing image field:** `products_contract/data_quality`
- **If campaign affected:** `marketing`

### 4. Producto sin proveedor

- **Data issue:** `products_contract/data_quality`
- **Commercial enrichment:** `commercial`

### 5. Producto con exceso de bodega

- **Detection:** `inventory_flow`
- **Action:** `inventory_flow` ticket
- **Campaign if needed:** `marketing`

### 6. Producto de temporada

- **Detection:** `inventory_flow season_opportunity_sensor`
- **Campaign:** `marketing`
- **Pricing:** `commercial`

## Cómo asignar un ticket a módulo

Un ticket pertenece al módulo que toma la decisión principal.

Ejemplos:

- “Calcular días sin venta” → `inventory_flow`
- “Hacer promoción por stock dormido” → `marketing`
- “Definir precio de remate” → `commercial`
- “Actualizar imagen principal” → `media`
- “Extraer producto desde Wappsi” → `scraper_data_ingestion`
- “Cambiar schema products.json” → `products_contract`

## Relación con GitHub Issues

Cada Issue debe incluir:

- Module
- Type
- Layer
- Maturity
- Priority

Si un ticket toca múltiples módulos:

- elegir un módulo dueño;
- linkear issues relacionados para módulos secundarios;
- no mezclar responsabilidades en un solo issue.

## Capas de trabajo

Cada ticket importante debe clasificarse en:

- Capa empresarial
- Capa matemática
- Capa operativa
- Capa JSON
- Capa técnica/documental si hace falta

## Decision Records

Cuando la pertenencia de un caso a un módulo sea ambigua, crear un decision issue o documento.

Formato:

- Context
- Decision
- Reason
- Impact
- Related modules

## Current M1 decision

El Module Map M1 es un mapa de trabajo, no una arquitectura final permanente.

Puede evolucionar mediante decision records y casos reales.
