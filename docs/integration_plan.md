# Integration Plan

## Objetivo

Integrar datos de inventario, marketing e imágenes en el contrato maestro `data/products.json` sin perder trazabilidad ni mezclar responsabilidades.

## Fase 1 — Contrato maestro base

- Definir estructura mínima de producto.
- Definir identificadores estables.
- Definir relación con familias y códigos de barras.

## Fase 2 — Inventory Flow

Responsabilidad del módulo:

- stock level
- quality control físico
- estado de flujo de inventario
- señales de riesgo operativo

Salida esperada:

- bloque `inventory_flow` dentro de cada producto en `products.json`.

## Fase 3 — Marketing

Responsabilidad del módulo:

- clientes objetivo
- catálogos
- campañas
- promociones
- contenido comercial

Salida esperada:

- bloque `marketing` dentro de cada producto en `products.json`.

## Fase 4 — Media

Responsabilidad del módulo:

- imágenes por uso
- imagen principal
- imágenes para catálogo
- imágenes para campañas
- imágenes técnicas o de empaque

Salida esperada:

- bloque `media` dentro de cada producto en `products.json`.

## Fase 5 — Validación

- Validar `products.json` contra `schemas/products.schema.json`.
- Validar cada bloque modular contra su schema correspondiente.
- Registrar cambios relevantes en `docs/decisions_log.md`.

