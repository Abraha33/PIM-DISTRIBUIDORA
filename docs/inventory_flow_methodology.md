# Inventory Flow Methodology

Fecha de inicio del enfoque: 2026-06-13

## Objetivo

Este documento define la metodolog?a de trabajo para el m?dulo `inventory_flow` del PIM de Envax.

El m?dulo no debe tratar el inventario ?nicamente como cantidades de stock bajo o stock alto. Su objetivo es construir un sistema de decisi?n empresarial que permita detectar inventario d?bil, inventario estrat?gico, inventario b?sico, oportunidades de temporada, riesgos f?sicos y necesidades de reabastecimiento.

## Enfoque general

El m?dulo `inventory_flow` se trabajar? en cuatro capas:

1. Capa empresarial
2. Capa matem?tica
3. Capa operativa / metodolog?a
4. Capa t?cnica / JSON / software

Cada idea, caso de uso o problema real debe ser clasificado dentro de estas capas antes de convertirse en regla o estructura JSON.

---

## 1. Capa empresarial

Esta capa responde:

?Qu? decisi?n de negocio queremos mejorar?

Prop?sitos principales:

* Liberar flujo de caja.
* Proteger inventario b?sico.
* Atender clientes objetivo.
* Evitar mercanc?a muerta.
* Evitar da?o f?sico del producto.
* Optimizar espacio en bodega y punto de venta.
* Preparar temporadas y eventos.
* Evitar agotados de productos importantes.

Ejemplo:

Un producto que no se mueve no se analiza solo como ?producto lento?. Se analiza como inventario que puede estar atrapando dinero, ocupando espacio y reduciendo la capacidad del negocio para comprar mercanc?a importante.

---

## 2. Capa matem?tica

Esta capa responde:

?Con qu? c?lculo se justifica una alerta o decisi?n?

La metodolog?a evita tomar decisiones con n?meros arbitrarios. Los umbrales iniciales pueden usarse como hip?tesis, pero las reglas finales deben justificarse con datos del negocio.

Ejemplos de f?rmulas iniciales:

```text
rotation_delay_ratio = d?as_sin_venta / frecuencia_normal_de_venta
```

```text
cashflow_pressure = valor_inventario_quieto / capital_disponible_para_compras
```

Variables matem?ticas importantes:

* d?as sin venta
* frecuencia normal de venta
* ventas ?ltimas 4 semanas
* ventas ?ltimos 90 d?as
* stock actual
* valor estimado del inventario
* capital disponible para compras
* tiempo de reabastecimiento
* espacio ocupado
* riesgo f?sico
* temporada cercana
* cliente objetivo relacionado

---

## 3. Capa operativa / metodolog?a

Esta capa responde:

?C?mo pasamos de una conversaci?n o caso real a una regla implementable?

Flujo oficial de trabajo:

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

Tipos de tickets:

* Ticket s?lido: ya se puede ejecutar.
* Ticket exploratorio: falta informaci?n para cerrarlo.
* Ticket bloqueado: depende de otro ticket.
* Ticket de integraci?n: conecta el m?dulo con `products.json`.

---

## 4. Capa t?cnica / JSON / software

Esta capa responde:

?C?mo se guarda todo en una estructura programable?

Estructura base esperada:

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

El m?dulo `inventory_flow` no reemplaza a `products.json`. Se integra dentro del producto final como una secci?n especializada.

---

## M?todo de an?lisis por caso

Cada caso de uso debe documentarse as?:

```text
Caso:
Situaci?n:
Problema empresarial:
Prop?sito:
Variables necesarias:
Sensor involucrado:
F?rmula o l?gica:
Diagn?stico:
Acci?n recomendada:
Se?al a otros m?dulos:
JSON esperado:
Pendientes:
```

---

## Primer caso de uso

CASE-001 ? Stock dormido para liberar flujo de caja

Prop?sito principal:

```text
release_cashflow
```

Objetivo:

Detectar productos quietos, lentos o muertos que pueden estar ocupando espacio y atrapando dinero que podr?a usarse para abastecer productos b?sicos o estrat?gicos para clientes objetivo.

Sensores iniciales:

* rotation_sensor
* cashflow_sensor
* space_sensor
* strategic_stock_sensor
* season_opportunity_sensor

---

## Principio rector

No se toman decisiones solo por etiquetas.

Cada etiqueta debe venir de:

```text
variable + umbral + c?lculo o condici?n + prop?sito empresarial
```

Ejemplo:

No basta decir:

```text
prioridad alta
```

Debe justificarse:

```text
prioridad alta porque se activaron sensores de rotaci?n, caja, espacio y no existe temporada cercana.
```
