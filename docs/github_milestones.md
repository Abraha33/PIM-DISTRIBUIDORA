# GitHub Milestones — PIM Envax

## Qué es un milestone en este proyecto

Un milestone representa una **entrega grande** del PIM Envax.

No es una tarea pequeña, no es una idea suelta y no es una capa técnica. Es una meta de trabajo que agrupa varios Issues relacionados.

En este proyecto:

- GitHub Projects es el tablero diario.
- GitHub Issues son los registros concretos de trabajo.
- Labels y campos describen módulo, tipo, prioridad, capa y estado.
- Milestones agrupan los Issues por entrega grande.

## Diferencia entre Issue, Project, Label/Campo y Milestone

### Issue

Un Issue es una unidad de trabajo o registro:

- idea;
- ticket;
- sensor;
- caso de uso;
- decisión;
- bug;
- validación.

Ejemplo:

```text
TICKET-002 — Diseñar rotation_sensor con base matemática
```

### Project

El Project es el tablero operativo diario.

Sirve para ver:

- qué está en `Icebox`;
- qué está en `Backlog`;
- qué está `Ready`;
- qué está `In Progress`;
- qué está en `Review`;
- qué está `Done`;
- qué está `Blocked`.

### Label / Campo

Los labels y campos describen la naturaleza del Issue.

Ejemplos:

- `module:inventory_flow`
- `type:sensor`
- `layer:matematica`
- `priority:high`
- `maturity:m1`

### Milestone

Un milestone responde:

```text
¿A qué entrega grande pertenece este Issue?
```

Ejemplo:

```text
Flujo de Inventario M1
```

## Regla principal

Los milestones son entregas grandes.

No deben usarse para:

- ideas sueltas;
- conversaciones;
- subtareas;
- capas de trabajo;
- estados del día a día;
- tickets individuales;
- experimentos sin dirección.

Las capas como `empresarial`, `matematica`, `operativa`, `json`, `documentacion` o `tecnica` deben ir como labels o campos, no como milestones.

## Milestones principales actuales

### 1. Contrato final JSON v1

Define la estructura final base del JSON del PIM:

- campos;
- contratos de datos;
- normalización;
- formato estable para productos.

Este milestone contiene trabajo relacionado con la base contractual del PIM y decisiones que protegen la estructura principal.

Issue inicial asignado:

- `#8 TICKET-000 — Definir Module Map M1 del PIM Envax`

Decisión:

`TICKET-000` queda en `Contrato final JSON v1` porque define límites de módulos y protege la estructura del contrato maestro antes de profundizar en módulos.

### 2. Flujo de Inventario M1

Primera versión metodológica del flujo de inventario:

- stock;
- rotación;
- inventario dormido;
- sensores;
- decisiones operativas;
- quality control físico;
- señales para otros módulos.

Issues iniciales asignados:

- `#1 EPIC-001 — inventory_flow M1`
- `#2 TICKET-001 — Documentar metodología de trabajo de inventory_flow`
- `#3 TICKET-002 — Diseñar rotation_sensor con base matemática`
- `#4 TICKET-003 — Diseñar cashflow_sensor`
- `#5 TICKET-004 — Diseñar space_sensor`
- `#6 TICKET-005 — Diseñar strategic_stock_sensor`
- `#7 TICKET-006 — Diseñar season_opportunity_sensor`

### 3. Ingreso de Compras M1

Primera versión del flujo de entrada de compras:

- foto o factura;
- proveedor;
- productos;
- cantidades;
- costos;
- descuentos si existen;
- fletes si existen;
- relación con productos del sistema.

Este milestone prepara el camino para el futuro módulo de compra asistida por factura + PIM + scraper.

### 4. Comparación de Precios M1

Primera versión del flujo para comparar precios:

- costo actual;
- costo histórico;
- competencia;
- web;
- llamadas;
- proveedor;
- señales de mercado.

Este milestone no decide automáticamente precios de venta. Solo organiza la comparación y las señales necesarias.

### 5. Decisión de Precio de Venta M1

Primera versión del flujo para decidir precio de venta:

- subir;
- bajar;
- mantener;
- revisar margen;
- pedir validación.

Regla importante:

La decisión final del precio de venta debe quedar en manos del encargado humano. El sistema puede sugerir, pero no debe reemplazar esa decisión.

## Milestones técnicos existentes

Además de los milestones principales, pueden existir milestones técnicos o históricos del proyecto, por ejemplo:

- `Inventory Flow M2 — Validation`
- `Inventory Flow M3 — Integration`
- `Marketing M1 — Methodology`
- `Media M1 — Methodology`
- `Commercial M1 — Methodology`
- `Scraper Data M1 — Stabilization`

Estos no reemplazan los milestones principales. Se mantienen como entregas futuras o especializadas cuando el trabajo lo justifique.

## Cuándo crear un nuevo milestone

Crear un nuevo milestone solo cuando exista una entrega grande y clara.

Buenas razones:

- aparece un módulo nuevo con varias tareas;
- una fase completa necesita agrupar muchos Issues;
- hay una entrega revisable por negocio;
- se necesita separar M1, M2 o M3 de un flujo importante.

Malas razones:

- una idea todavía está verde;
- apareció una subtarea;
- hay una conversación pendiente;
- se necesita marcar prioridad;
- se necesita marcar estado.

Para esas cosas se usan Issues, labels, campos del Project o Icebox.

## Milestones en el flujo móvil

Desde el celular, el trabajo diario se revisa principalmente en el Project:

```text
PIM Envax — Roadmap & Backlog
```

El Project muestra qué hacer hoy.

El milestone muestra a qué entrega grande pertenece cada ticket.

Ejemplo:

```text
Issue: TICKET-002 — Diseñar rotation_sensor con base matemática
Status: Ready
Milestone: Flujo de Inventario M1
```

En la práctica:

1. Revisás el Project.
2. Elegís un Issue `Ready`.
3. Mirás su milestone para entender a qué entrega aporta.
4. Lo movés a `In Progress`.
5. Cuando termina, pasa a `Review` o `Done`.

## Regla de protección

No se debe crear un milestone por cada conversación.

No se debe crear un milestone por cada subtarea.

No se debe usar milestone como estado.

Milestone = entrega grande.

Issue = trabajo concreto.

Project = tablero operativo.

Label/Campo = clasificación.
