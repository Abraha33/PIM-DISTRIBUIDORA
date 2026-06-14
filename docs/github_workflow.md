# GitHub Workflow — PIM Envax

## Por qué usamos GitHub Issues

GitHub Issues será el sistema activo de trabajo para ideas, tickets, sensores, casos de uso, decisiones, bugs y validaciones.

Los documentos Markdown siguen siendo útiles para explicar metodología, contratos y decisiones, pero el trabajo vivo debe gestionarse con Issues para poder asignar estado, prioridad, módulo, milestone, relación con PRs y seguimiento visual en GitHub Projects.

## Diferencia entre Idea, Backlog, Ticket, Epic, Sensor, Use Case y Decision

- **Idea:** todavía no está lista. Vive en Icebox.
- **Backlog:** trabajo probable o deseable, pero no necesariamente listo para ejecutar.
- **Ticket:** tarea concreta con alcance, propósito, inputs y outputs.
- **Epic:** cuerpo grande de trabajo que agrupa tickets, por ejemplo `inventory_flow M1`.
- **Sensor:** ticket especializado de `inventory_flow` con variables, umbrales, fórmula o condición, resultado y propósito empresarial.
- **Use Case:** caso real operativo que motiva reglas o sensores.
- **Decision:** decisión arquitectónica o de negocio que debe recordarse.

## Cómo Issues conecta con GitHub Projects

Cada Issue debe entrar al GitHub Project `PIM Envax — Roadmap & Backlog`.

El Project permite ver el trabajo como:

- tablero por estado;
- tabla por módulo;
- roadmap por madurez;
- vista específica de `inventory_flow M1`;
- icebox de ideas.

## Cómo usar sub-issues

Un Issue grande puede dividirse en sub-issues cuando aparezcan piezas menores.

Ejemplo:

```text
TICKET-002 — Diseñar rotation_sensor con base matemática
  ├─ Sub-issue: definir variables
  ├─ Sub-issue: definir fórmula base
  ├─ Sub-issue: definir umbrales
  ├─ Sub-issue: definir JSON esperado
  └─ Sub-issue: documentar criterios de aceptación
```

Las sub-issues deben representar una capa o paso técnico pequeño, no otra idea gigante.

## Cómo usar milestones M1 / M2 / M3

- **M1 metodología:** propósito empresarial, variables, fórmulas, reglas, tickets y forma JSON.
- **M2 validación:** ejemplos, casos controlados, validadores y documentación de errores.
- **M3 integración:** conexión de salidas de módulos con futuras versiones de `products.json`.

`products.json v1` está cerrado. Los experimentos de módulos no deben modificarlo directamente.

## Workflow diario recomendado

1. Revisar el Project board.
2. Elegir un Issue en estado `Ready`.
3. Trabajarlo por las cuatro capas:
   - empresarial
   - matemática
   - operativa
   - JSON
4. Crear o actualizar documentación.
5. Linkear el PR al Issue.
6. Mover el Issue a `Review`.
7. Cerrar solo cuando se cumplan los criterios de aceptación.

## Regla de oro

Si no está en Issue, no está realmente planificado.

Si no tiene criterios de aceptación, todavía no está listo.
