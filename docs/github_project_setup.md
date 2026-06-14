# GitHub Project Setup — PIM Envax

## Proyecto recomendado

Crear un GitHub Project con el nombre:

```text
PIM Envax — Roadmap & Backlog
```

Este Project debe ser el tablero operativo para ideas, tickets, sensores, casos de uso, decisiones, bugs y validaciones.

## Vistas recomendadas

- **Board by Status:** tablero Kanban por estado.
- **Table by Module:** tabla agrupada por módulo.
- **Roadmap by Maturity:** vista por M1 / M2 / M3.
- **Inventory Flow M1:** vista filtrada para `module:inventory_flow` y `maturity:m1`.
- **Ideas Icebox:** vista filtrada para `type:idea` o `status:icebox`.

## Campos recomendados

- Status
- Module
- Layer
- Type
- Maturity
- Priority
- Sensor
- Ticket ID
- Business Value
- Blocked By

## Status values

- Icebox
- Backlog
- Ready
- In Progress
- Review
- Done
- Blocked

## Module values

- products_contract
- inventory_flow
- marketing
- media
- scraper
- commercial

## Layer values

- empresarial
- matematica
- operativa
- json
- documentacion
- tecnica

## Type values

- idea
- epic
- ticket
- sensor
- use_case
- decision
- bug
- validation

## Maturity values

- M1 metodologia
- M2 validacion
- M3 integracion

## Nota operativa

GitHub Issues contiene el trabajo. GitHub Projects muestra el trabajo.

No conviene duplicar estados en documentos Markdown si el Issue ya existe. Los docs explican; los Issues operan.

## Estado de creaci?n

Creado en GitHub:

- Project: `PIM Envax ? Roadmap & Backlog`
- URL: https://github.com/users/Abraha33/projects/18
- Issues iniciales agregados al Project: #1 a #8

Campos creados con GitHub CLI:

- Module
- Layer
- Type
- Maturity
- Priority
- Sensor
- Ticket ID
- Business Value
- Blocked By

Nota: el campo `Status` existe por defecto en GitHub Projects con opciones iniciales de GitHub. Si se requiere el set exacto `Icebox / Backlog / Ready / In Progress / Review / Done / Blocked`, ajustarlo manualmente desde la UI del Project.
