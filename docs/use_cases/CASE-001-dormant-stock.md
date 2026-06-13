# CASE-001 — Dormant Stock

## Contexto

Envax necesita detectar productos con stock dormido para tomar decisiones comerciales, operativas o de depuración de inventario.

## Problema

Un producto puede existir en inventario, pero no moverse durante un período prolongado. Si ese dato no se modela explícitamente, marketing, ventas y operaciones trabajan a ciegas.

## Objetivo

Identificar productos con riesgo de stock dormido usando señales del módulo `inventory_flow`.

## Señales iniciales

- `stock_level`
- `last_movement_date`
- `days_without_movement`
- `physical_quality_status`
- `inventory_flow_status`
- `risk_level`

## Resultado esperado

El producto debe poder marcarse con una señal de riesgo sin romper el contrato maestro.

Ejemplo:

```json
{
  "inventory_flow": {
    "stock_level": 120,
    "days_without_movement": 180,
    "risk_level": "high"
  }
}
```

## Regla base

Si `days_without_movement` supera el umbral definido en `rules/risk_rules.json`, el producto debe marcarse como candidato a revisión.

