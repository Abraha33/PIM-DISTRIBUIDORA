# Module Boundary Decisions — PIM Envax

## Purpose

Registrar decisiones cuando un caso podría pertenecer a más de un módulo.

Este documento evita mezclar responsabilidades y ayuda a decidir qué módulo debe ser dueño de un ticket, regla o issue.

## DEC-001 — Stock dormido

### Decision

La detección pertenece a `inventory_flow`.

La activación comercial pertenece a `marketing`.

La decisión de precio/margen pertenece a `commercial`.

## DEC-002 — Product image quality

### Decision

La calidad visual pertenece a `media`.

La ausencia de imagen como dato de producto pertenece a `products_contract/data_quality`.

## DEC-003 — Supplier data

### Decision

Proveedor faltante es una advertencia de `data_quality` en `products_contract v1`.

El enriquecimiento de proveedores y su historial pertenece a `commercial`.

## DEC-004 — Scraper output

### Decision

`scraper_data_ingestion` es dueño de salidas raw y clean de extracción.

`products_contract` es dueño únicamente de la estructura validada del contrato.

## DEC-005 — Inventory physical quality

### Decision

La calidad física del producto pertenece a `inventory_flow`.

La completitud de datos pertenece a `products_contract/data_quality`.
