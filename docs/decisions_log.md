# Decisions Log

Registro de decisiones del contrato PIM de Envax.

## Decisiones generales

| Fecha | Decisi?n | Motivo | Impacto |
| --- | --- | --- | --- |
| 2026-06-13 | Crear estructura inicial del repositorio `PIM-DISTRIBUIDORA` | Documentar y versionar el contrato PIM de Envax | Se separan contratos, reglas, ejemplos, datos base y casos de uso |
| 2026-06-13 | `data/products.json` ser? el contrato maestro integrado | Evitar que cada m?dulo defina productos de forma aislada | Los m?dulos deben integrarse respetando el schema maestro |
| 2026-06-13 | Separar `inventory_flow`, `marketing` y `media` | Mantener responsabilidades claras por m?dulo | Cada m?dulo tendr? schema y reglas propias |

---

## 2026-06-13 ? Nuevo enfoque oficial para inventory_flow

### Decisi?n

El m?dulo de stock del PIM de Envax se trabajar? bajo el nombre conceptual `inventory_flow`.

No ser? tratado como un simple m?dulo de stock bajo / stock alto. Ser? un sistema de decisi?n empresarial para inventario.

### Enfoque aprobado

El m?dulo se trabajar? en cuatro capas:

1. Capa empresarial
2. Capa matem?tica
3. Capa operativa / metodolog?a
4. Capa t?cnica / JSON / software

### Motivo

El inventario de Envax no solo debe controlar cantidades. Debe ayudar a tomar decisiones sobre:

- flujo de caja
- inventario b?sico
- clientes objetivo
- mercanc?a lenta
- mercanc?a dormida
- mercanc?a muerta
- riesgo f?sico
- espacio ocupado
- temporadas
- reabastecimiento
- traslado
- promoci?n
- remate
- conservaci?n estrat?gica

### Decisi?n clave

Los sensores del sistema no ser?n etiquetas decorativas.

Cada sensor debe tener:

- variable
- umbral
- c?lculo o condici?n
- resultado
- acci?n sugerida
- prop?sito empresarial

### Primer caso de uso oficial

`CASE-001 ? Stock dormido para liberar flujo de caja`

### Sensores M1 iniciales

- `rotation_sensor`
- `cashflow_sensor`
- `space_sensor`
- `strategic_stock_sensor`
- `season_opportunity_sensor`

### Regla de trabajo

Toda idea o caso real se convertir? usando este flujo:

```text
caso real
? problema detectado
? prop?sito empresarial
? variables necesarias
? sensor
? f?rmula o l?gica
? regla M1
? ticket
? documento
? JSON
? integraci?n en products.json
```

### Estado

Aprobado como enfoque de trabajo inicial para el m?dulo `inventory_flow`.
