# Module Integration Plan ? PIM Contract v1

## Objetivo

Este documento define c?mo deben integrarse los m?dulos futuros dentro de `products.json` sin romper el contrato maestro v1.

La regla principal es simple: cada m?dulo debe escribir ?nicamente en su secci?n asignada, salvo revisi?n expl?cita.

## Orden recomendado de integraci?n

1. `inventory_flow`
2. `marketing`
3. `media`
4. `scraper/commercial`

Este orden protege el contrato: primero se entiende el flujo operativo del producto, despu?s su comunicaci?n comercial, luego sus activos visuales y finalmente la integraci?n autom?tica de datos comerciales.

## 1. inventory_flow

`inventory_flow` debe actualizar ?nicamente la secci?n:

```text
products[].inventory_flow
```

Responsabilidades futuras:

- stock level
- flujo de inventario
- se?ales de reabastecimiento
- riesgo operativo
- calidad f?sica cuando corresponda al flujo de inventario
- diagn?stico de inventario d?bil, b?sico o estrat?gico

No debe modificar:

- `identity`
- `category`
- `attributes`
- `names`
- `marketing`
- `media`

## 2. marketing

`marketing` debe actualizar ?nicamente la secci?n:

```text
products[].marketing
```

Responsabilidades futuras:

- clientes objetivo
- etiquetas de cat?logo
- etiquetas de campa?a
- keywords comerciales
- descripciones ecommerce
- promociones planificadas

No debe modificar datos normalizados del producto salvo revisi?n expl?cita.

## 3. media

`media` debe actualizar ?nicamente la secci?n:

```text
products[].media
```

Responsabilidades futuras:

- im?genes principales
- im?genes por uso
- im?genes de cat?logo
- im?genes de campa?a
- im?genes t?cnicas
- relaci?n entre imagen y presentaci?n del producto

No debe usar im?genes para redefinir identidad, categor?a o atributos del producto.

## 4. scraper/commercial

`scraper/commercial` debe actualizar principalmente:

```text
products[].commercial
products[].suppliers
```

Puede alimentar:

- precios
- costos
- impuestos comerciales
- proveedores
- datos comerciales externos

Debe preservar los campos manuales normalizados salvo revisi?n expl?cita:

- `identity`
- `category`
- `attributes`
- `names`
- `unit_presentation`
- `unit_summary`

## Regla de protecci?n de campos normalizados

Los m?dulos autom?ticos no deben sobrescribir campos normalizados manualmente sin auditor?a.

Campos protegidos:

- `code`
- `identity`
- `category`
- `attributes`
- `unit_presentation`
- `unit_summary`
- `names`
- `family_id`

Si un m?dulo detecta una diferencia, debe generar una se?al o pendiente de revisi?n, no sobrescribir silenciosamente.

## Integraci?n con products.json

Cada integraci?n debe seguir este flujo:

```text
m?dulo separado
? validaci?n del m?dulo
? revisi?n de impacto
? actualizaci?n de secci?n asignada
? validaci?n completa del contrato
? reporte consolidado
```

## Qu? no se implementa en este documento

- f?rmulas reales de stock
- reglas de marketing
- reglas de im?genes
- scraper
- importaci?n/exportaci?n ERP
- automatizaciones

?? **Decisi?n tomada:** los m?dulos se integran como capas especializadas dentro de `products.json`, no como reemplazos del contrato maestro.

?? **Recomendaci?n experta:** si un m?dulo quiere tocar todo, el m?dulo est? mal dise?ado. Un m?dulo sano tiene frontera clara. Sin frontera, no hay arquitectura: hay barro.
