# Issue Taxonomy — PIM Envax

## Epic

Un Epic es un cuerpo grande de trabajo que agrupa varios tickets o sensores.

Ejemplo:

```text
EPIC-001 — inventory_flow M1
```

## Ticket

Un Ticket es una tarea concreta lista para trabajar.

Debe tener:

- contexto;
- problema;
- propósito empresarial;
- inputs;
- outputs;
- criterios de aceptación;
- fuera de alcance.

## Sub-issue

Una sub-issue es una pieza menor dentro de un ticket.

Normalmente representa:

- una capa;
- una validación;
- una parte técnica;
- una investigación puntual;
- una documentación específica.

## Idea

Una Idea todavía no está lista.

Debe quedarse en Icebox hasta tener contexto suficiente para pasar a backlog o convertirse en ticket.

## Use Case

Un Use Case es un caso real de negocio que motiva reglas, sensores o decisiones.

Ejemplo:

```text
CASE-001 — Stock dormido para liberar flujo de caja
```

## Decision

Una Decision registra una decisión permanente que debe recordarse.

Debe explicar:

- contexto;
- decisión;
- razón;
- alternativas;
- impacto.

## Bug

Un Bug es algo roto o inconsistente.

Puede afectar documentación, validadores, schemas, reglas, ejemplos o integración futura.

## Validation

Una Validation es un chequeo que protege el contrato o un módulo.

Ejemplos:

- JSON Schema validation;
- dictionary validation;
- naming validation;
- documentation coverage;
- futura validación de `inventory_flow`.
