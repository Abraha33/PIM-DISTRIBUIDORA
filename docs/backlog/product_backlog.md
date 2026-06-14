# Product Backlog — PIM Envax

Este backlog registra trabajo accionable para el proyecto PIM Envax. No reemplaza los tickets: el backlog ordena intención y prioridad; el ticket define alcance concreto, entradas, salidas y criterios de aceptación.

| ID | Módulo | Tipo | Prioridad | Estado | Descripción | Dependencias | Resultado esperado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PB-001 | inventory_flow | sensor | alta | ready | Diseñar `rotation_sensor` con base matemática. | inventory_flow methodology draft. | fórmula, variables, regla M1, ticket y JSON base. |
| PB-002 | inventory_flow | sensor | media | pending | Diseñar `cashflow_sensor` para detectar inventario que presiona caja. | rotation_sensor M1. | fórmula, variables, regla M1, ticket y JSON base. |
| PB-003 | inventory_flow | sensor | media | pending | Diseñar `space_sensor` para detectar inventario que ocupa espacio crítico. | rotation_sensor M1. | fórmula, variables, regla M1, ticket y JSON base. |
| PB-004 | marketing | module | pendiente | icebox | Definir conexión entre productos, clientes objetivo, campañas y catálogos. | products.json v1. | metodología marketing M1. |
| PB-005 | media | module | pendiente | icebox | Definir estructura para imágenes, activos visuales y calidad visual del producto. | products.json v1. | metodología media M1. |

## Estados sugeridos

- `icebox`: idea o trabajo todavía inmaduro.
- `pending`: trabajo probable, pero con dependencias abiertas.
- `ready`: listo para convertirse en ticket o iniciar trabajo.
- `in_progress`: en ejecución.
- `done`: completado.
- `blocked`: bloqueado por información, decisión o dependencia externa.
