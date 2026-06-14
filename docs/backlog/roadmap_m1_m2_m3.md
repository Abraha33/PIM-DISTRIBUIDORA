# Roadmap M1 / M2 / M3 — PIM Envax

Este roadmap organiza el trabajo por nivel de madurez. No define fechas cerradas; define orden lógico de construcción.

## M1 — Methodology and rules

**Goal:**

Definir propósito empresarial, variables, fórmulas, reglas, tickets y forma JSON.

Modules:

- `inventory_flow` sensors
- `marketing` methodology
- `media` methodology

## M2 — Validation and examples

**Goal:**

Agregar ejemplos, casos controlados y reglas de validación.

Posibles entregables:

- ejemplos JSON por módulo;
- casos válidos;
- casos inválidos controlados;
- validadores específicos por módulo;
- documentación de errores y advertencias.

## M3 — Integration

**Goal:**

Conectar salidas de módulos de vuelta a futuras versiones de `products.json`.

Posibles entregables:

- integración controlada de `inventory_flow`;
- integración controlada de `marketing`;
- integración controlada de `media`;
- definición de versionado posterior a v1.

## Nota de protección

`products.json v1` está cerrado y no debe modificarse directamente para experimentos de módulos.

Los módulos deben evolucionar por documentación, tickets, ejemplos y validaciones antes de integrarse en una futura versión del contrato.
