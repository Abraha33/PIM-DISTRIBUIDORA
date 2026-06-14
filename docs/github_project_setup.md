# GitHub Project Setup — PIM Envax

## Proyecto operativo

El Project oficial es:

```text
PIM Envax — Roadmap & Backlog
```

URL:

```text
https://github.com/users/Abraha33/projects/18
```

Este Project es el tablero diario para ideas, tickets, sensores, casos de uso, decisiones, bugs y validaciones.

## Principio de organización

- **Issues** son la fuente de verdad del trabajo.
- **Project** muestra estado, módulo, prioridad, madurez y seguimiento visual.
- **Milestones** representan metas grandes de entrega.
- **Labels y campos** representan módulo, tipo, capa, prioridad y madurez.
- **Documentos Markdown** explican el sistema, pero no reemplazan los Issues activos.

## Milestones

Los milestones son objetivos de entrega, no capas de trabajo.

Ejemplos:

- `PIM Contract v1 — Released`
- `Inventory Flow M1 — Methodology`
- `Inventory Flow M2 — Validation`
- `Inventory Flow M3 — Integration`
- `Marketing M1 — Methodology`
- `Media M1 — Methodology`
- `Commercial M1 — Methodology`
- `Scraper Data M1 — Stabilization`

## Capas de trabajo

Las capas no deben usarse como milestones. Deben mantenerse como labels o campos del Project:

- `layer:empresarial`
- `layer:matematica`
- `layer:operativa`
- `layer:json`
- `layer:documentacion`
- `layer:tecnica`

Esto evita mezclar una meta de entrega con la naturaleza del trabajo.

## Status del workflow diario

El campo `Status` representa dónde está el ticket hoy.

Valores configurados:

- `Icebox`: idea guardada, todavía no lista.
- `Backlog`: trabajo probable, pero no necesariamente listo para ejecutar.
- `Ready`: listo para trabajar.
- `In Progress`: en trabajo.
- `Review`: listo para revisión.
- `Done`: terminado.
- `Blocked`: bloqueado por datos, decisión o dependencia.

Mapeo aplicado:

- `Todo` → `Backlog`
- `In Progress` → `In Progress`
- `Done` → `Done`

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

## Module values

- products_contract
- inventory_flow
- marketing
- media
- scraper_data_ingestion
- commercial

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

## Uso diario desde móvil o voz

Flujo recomendado:

1. Abrir el Project `PIM Envax — Roadmap & Backlog`.
2. Revisar la columna `Ready`.
3. Elegir un Issue concreto.
4. Moverlo a `In Progress`.
5. Trabajarlo por capas.
6. Moverlo a `Review` cuando tenga salida clara.
7. Moverlo a `Done` solo cuando cumpla criterios de aceptación.
8. Si aparece una idea nueva, crear Issue tipo `Idea / Icebox`.
9. Si falta información, mover a `Blocked`.

## Estado actual de creación

Creado en GitHub:

- Project: `PIM Envax — Roadmap & Backlog`
- URL: `https://github.com/users/Abraha33/projects/18`
- Issues iniciales agregados al Project: `#1` a `#8`
- Milestones iniciales creados.
- Issues `#1` a `#8` asignados al milestone `Inventory Flow M1 — Methodology`.
- Campo `Status` configurado con `Icebox / Backlog / Ready / In Progress / Review / Done / Blocked`.

## Nota importante sobre Inbox

GitHub Inbox no es el tablero de tickets. Inbox muestra notificaciones, menciones, asignaciones o actividad relevante para el usuario.

Para ver el trabajo activo hay que usar:

- Issues del repositorio: `https://github.com/Abraha33/PIM-DISTRIBUIDORA/issues`
- Project: `https://github.com/users/Abraha33/projects/18`

Si se quiere que un ticket aparezca como responsabilidad directa en la app móvil, conviene asignarlo al usuario.
