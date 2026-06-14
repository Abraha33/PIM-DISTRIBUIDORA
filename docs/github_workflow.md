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

## Milestones M1 / M2 / M3

Los milestones representan entregas grandes.

- **M1 metodología:** propósito empresarial, variables, fórmulas, reglas, tickets y forma JSON.
- **M2 validación:** ejemplos, casos controlados, validadores y documentación de errores.
- **M3 integración:** conexión de salidas de módulos con futuras versiones de `products.json`.

Las capas de trabajo no son milestones. Las capas se mantienen como labels o campos del Project:

- empresarial
- matemática
- operativa
- JSON
- documentación
- técnica

`products.json v1` está cerrado. Los experimentos de módulos no deben modificarlo directamente.

## Workflow diario recomendado

1. Revisar el Project board.
2. Elegir un Issue en estado `Ready`.
3. Moverlo a `In Progress`.
4. Trabajarlo por las cuatro capas:
   - empresarial
   - matemática
   - operativa
   - JSON
5. Crear o actualizar documentación.
6. Linkear el PR al Issue cuando haya cambios en repositorio.
7. Mover el Issue a `Review`.
8. Cerrar solo cuando se cumplan los criterios de aceptación.

## Flujo diario por voz / móvil

Este flujo está pensado para trabajar desde el celular o hablando con Codex:

1. Preguntar: “¿Qué Issues están en Ready?”
2. Elegir un Issue.
3. Moverlo a `In Progress`.
4. Trabajarlo por capas:
   - empresarial
   - matemática
   - operativa
   - JSON
5. Cuando tenga salida clara, moverlo a `Review`.
6. Después de revisar y cerrar, moverlo a `Done`.
7. Si la idea todavía no está lista, moverla a `Icebox`.
8. Si falta información o decisión, moverla a `Blocked`.

## Sobre GitHub Inbox

GitHub Inbox no funciona como lista de todos los tickets del proyecto.

Inbox muestra notificaciones: menciones, asignaciones, comentarios, revisiones o actividad que GitHub considera relevante para tu usuario.

Para ver los tickets, usá:

- la pestaña **Issues** del repositorio;
- el Project `PIM Envax — Roadmap & Backlog`;
- filtros por `assignee`, `label`, `status` o `milestone`.

Si querés que un ticket te aparezca como responsabilidad directa, hay que asignártelo.

## Regla de oro

Si no está en Issue, no está realmente planificado.

Si no tiene criterios de aceptación, todavía no está listo.
