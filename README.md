# PIM-DISTRIBUIDORA

Repositorio para documentar y versionar el contrato PIM de Envax.

## Objetivo

El objetivo de este repositorio es mantener un contrato claro, versionado y auditable para el PIM de Envax.

El producto final se maneja en:

- `data/products.json`

Los módulos se trabajan por separado y luego se integran al contrato maestro:

- `inventory_flow`: stock level, quality control físico y flujo de inventario.
- `marketing`: clientes objetivo, catálogos, campañas y promociones.
- `media`: imágenes por uso.
- `products.json`: contrato maestro del producto.

## Estructura

```text
PIM-DISTRIBUIDORA/
├── README.md
├── docs/
│   ├── decisions_log.md
│   ├── integration_plan.md
│   └── use_cases/
│       └── CASE-001-dormant-stock.md
├── schemas/
│   ├── products.schema.json
│   ├── inventory_flow.schema.json
│   ├── marketing.schema.json
│   └── media.schema.json
├── rules/
│   ├── inventory_rules_m1.json
│   ├── module_signals.json
│   └── risk_rules.json
├── examples/
│   └── use_case_001_dormant_stock.json
└── data/
    ├── products.json
    ├── product_families.json
    └── barcode_history.json
```

## Principio arquitectónico

`products.json` no debería convertirse en un basurero de campos sueltos. Es el contrato maestro. Cada módulo tiene su responsabilidad y su schema.

Es como una obra: el plano maestro existe, pero electricidad, plomería y estructura no se dibujan al azar arriba del mismo papel. Cada disciplina tiene su capa, y después se coordina.

