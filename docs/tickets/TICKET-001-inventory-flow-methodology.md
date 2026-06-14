# TICKET-001 — Documentar metodología de trabajo de inventory_flow

**Fecha:** 2026-06-13

## Estado

Sólido

## Tipo

Metodología / arquitectura del módulo

## Objetivo

Definir el método oficial de trabajo para construir el módulo `inventory_flow` del PIM de Envax.

Este ticket establece cómo pasar de conversaciones y casos reales del negocio a sensores, reglas, documentos, tickets y estructuras JSON implementables.

## Contexto

Envax necesita un sistema de inventario que no solo indique stock bajo o stock alto, sino que ayude a tomar decisiones empresariales.

El módulo debe detectar puntos débiles como:

- mercancía que no se mueve
- mercancía lenta
- mercancía dormida
- mercancía muerta
- capital atrapado
- espacio ocupado
- riesgo físico
- falta de inventario básico
- riesgo de no atender clientes objetivo
- oportunidad por temporada o evento

## Capas del enfoque

El módulo se trabajará en cuatro capas:

### 1. Capa empresarial

Define el propósito de negocio.

Ejemplos:

- liberar flujo de caja
- proteger inventario básico
- atender clientes objetivo
- evitar deterioro físico
- optimizar espacio
- preparar temporadas

### 2. Capa matemática

Define las fórmulas, ratios y criterios que justifican las alertas.

Ejemplos:

```text
rotation_delay_ratio = días_sin_venta / frecuencia_normal_de_venta
```

```text
cashflow_pressure = valor_inventario_quieto / capital_disponible_para_compras
```

### 3. Capa operativa

Define cómo se gestionan casos, tickets y tareas.

Flujo:

```text
caso real
→ problema
→ variables
→ sensor
→ fórmula
→ regla
→ ticket
→ documento
→ JSON
```

### 4. Capa técnica

Define cómo se guarda el resultado en estructuras JSON.

Estructura base:

```json
{
  "inventory_flow": {
    "business_purpose": "",
    "inventory_bucket": "",
    "sensors": {},
    "diagnosis": {},
    "decision": {},
    "module_signals": {}
  }
}
```

## Resultado esperado

Crear y mantener los siguientes documentos:

- `docs/inventory_flow_methodology.md`
- `docs/decisions_log.md`
- `docs/use_cases/CASE-001-dormant-stock.md`
- `schemas/inventory_flow.schema.json`
- `rules/inventory_rules_m1.json`

## Criterios de aceptación

Este ticket se considera completo cuando:

- Existe una metodología clara para trabajar el módulo.
- Se documentan las cuatro capas del enfoque.
- Se define el flujo caso → sensor → regla → JSON.
- Se registra la decisión en `decisions_log.md`.
- Se deja preparado el camino para CASE-001.

## Estado de avance

- [x] Metodología documentada en `docs/inventory_flow_methodology.md`.
- [x] Decisión registrada en `docs/decisions_log.md`.
- [x] CASE-001 preparado en `docs/use_cases/CASE-001-dormant-stock.md`.
- [ ] Schema `schemas/inventory_flow.schema.json` revisado contra la metodología M1.
- [ ] Reglas `rules/inventory_rules_m1.json` revisadas contra la metodología M1.

📌 **Decisión tomada:** este ticket documenta metodología y arquitectura del módulo; no implementa lógica de stock ni reglas automáticas.
