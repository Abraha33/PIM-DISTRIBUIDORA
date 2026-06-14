# GitHub Milestones — PIM Envax

## Propósito

Los milestones sirven para agrupar Issues alrededor de una meta grande de entrega.

En PIM Envax, un milestone no representa una capa de trabajo. Representa una fase de avance del producto o de un módulo.

## Por qué las capas no son milestones

Las capas:

- empresarial
- matemática
- operativa
- JSON
- documentación
- técnica

describen la naturaleza del trabajo dentro de un Issue.

Un milestone, en cambio, describe una entrega completa. Por ejemplo: `Inventory Flow M1 — Methodology`.

Si usáramos capas como milestones, mezclaríamos dos preguntas distintas:

1. ¿Qué tipo de trabajo es?
2. ¿A qué entrega pertenece?

Por eso:

- las capas van como labels o campos del Project;
- los milestones van como objetivos de entrega.

## Milestones recomendados

### PIM Contract v1 — Released

Entrega validada y taggeada del contrato maestro de producto `products.json v1`.

### Inventory Flow M1 — Methodology

Define metodología, sensores, reglas, tickets, casos de uso y estructura JSON para `inventory_flow M1`.

### Inventory Flow M2 — Validation

Agrega ejemplos, reglas de validación y casos controlados para `inventory_flow`.

### Inventory Flow M3 — Integration

Conecta las salidas de `inventory_flow` con futuras versiones de `products.json`.

### Marketing M1 — Methodology

Define clientes objetivo, lógica de campañas, tags de catálogo y metodología de activación comercial.

### Media M1 — Methodology

Define estructura de imágenes, reglas de calidad visual y manejo de media del producto.

### Commercial M1 — Methodology

Define precios, costos, márgenes, proveedores, impuestos e historial comercial.

### Scraper Data M1 — Stabilization

Estabiliza outputs de scraper/data ingestion, datasets raw/clean y reportes de extracción.

## Relación entre Milestones, Issues y Project

- **Issue:** contiene el trabajo concreto.
- **Milestone:** agrupa Issues por meta de entrega.
- **Project:** muestra el estado operativo diario.

Ejemplo:

```text
Issue: TICKET-002 — Diseñar rotation_sensor con base matemática
Milestone: Inventory Flow M1 — Methodology
Project Status: Ready
Module: inventory_flow
Layer: matematica
Type: sensor
```

## Uso de Inventory Flow M1 — Methodology

Este milestone agrupa los Issues iniciales de `inventory_flow`:

- `EPIC-001 — inventory_flow M1`
- `TICKET-001 — Documentar metodología de trabajo de inventory_flow`
- `TICKET-002 — Diseñar rotation_sensor con base matemática`
- `TICKET-003 — Diseñar cashflow_sensor`
- `TICKET-004 — Diseñar space_sensor`
- `TICKET-005 — Diseñar strategic_stock_sensor`
- `TICKET-006 — Diseñar season_opportunity_sensor`
- `TICKET-000 — Definir Module Map M1 del PIM Envax`

`TICKET-000` queda dentro del milestone porque el mapa de módulos habilita el trabajo ordenado de `Inventory Flow M1`.

## Regla práctica

Un Issue pertenece al milestone de la entrega que ayuda a completar.

Si un Issue toca varios módulos:

1. elegir un módulo dueño;
2. asignar el milestone de la entrega principal;
3. crear Issues relacionados para los módulos secundarios si hace falta;
4. no mezclar responsabilidades en un solo ticket gigante.
