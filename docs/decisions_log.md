# Decisions Log

Registro de decisiones del contrato PIM de Envax.

| Fecha | Decisión | Motivo | Impacto |
| --- | --- | --- | --- |
| 2026-06-13 | Crear estructura inicial del repositorio `PIM-DISTRIBUIDORA` | Documentar y versionar el contrato PIM de Envax | Se separan contratos, reglas, ejemplos, datos base y casos de uso |
| 2026-06-13 | `data/products.json` será el contrato maestro integrado | Evitar que cada módulo defina productos de forma aislada | Los módulos deben integrarse respetando el schema maestro |
| 2026-06-13 | Separar `inventory_flow`, `marketing` y `media` | Mantener responsabilidades claras por módulo | Cada módulo tendrá schema y reglas propias |

