# CASE-001 ? Stock dormido para liberar flujo de caja

## Caso

`CASE-001 ? dormant-stock`

## Situaci?n

Envax puede tener productos quietos, lentos o muertos que permanecen en inventario sin rotaci?n suficiente.

## Problema empresarial

El stock dormido no es solo un producto que se mueve lento. Puede representar dinero atrapado, espacio ocupado y menor capacidad para comprar mercanc?a b?sica o estrat?gica.

## Prop?sito

`release_cashflow`

Liberar flujo de caja detectando inventario d?bil que puede estar bloqueando compras m?s importantes.

## Variables necesarias

- d?as sin venta
- frecuencia normal de venta
- ventas ?ltimas 4 semanas
- ventas ?ltimos 90 d?as
- stock actual
- valor estimado del inventario
- capital disponible para compras
- espacio ocupado
- temporada cercana
- cliente objetivo relacionado

## Sensor involucrado

Sensores iniciales:

- `rotation_sensor`
- `cashflow_sensor`
- `space_sensor`
- `strategic_stock_sensor`
- `season_opportunity_sensor`

## F?rmula o l?gica

F?rmulas iniciales de referencia:

```text
rotation_delay_ratio = d?as_sin_venta / frecuencia_normal_de_venta
cashflow_pressure = valor_inventario_quieto / capital_disponible_para_compras
```

?? pendiente: los umbrales iniciales pueden usarse como hip?tesis, pero las reglas finales deben justificarse con datos reales del negocio.

## Diagn?stico

Un producto puede ser candidato a revisi?n si combina se?ales de baja rotaci?n, presi?n sobre caja, ocupaci?n de espacio y ausencia de oportunidad de temporada cercana.

## Acci?n recomendada

Definir una acci?n seg?n diagn?stico:

- revisar exhibici?n
- revisar precio
- mover a promoci?n
- agrupar con producto complementario
- liquidar parcialmente
- pausar recompra
- mantener si es estrat?gico o de temporada pr?xima

No se automatiza todav?a ninguna acci?n. Este documento define metodolog?a y caso de uso, no l?gica ejecutable.

## Se?al a otros m?dulos

Posibles se?ales futuras:

- `marketing`: candidato a campa?a, cat?logo o promoci?n.
- `commercial`: revisar precio, costo o margen cuando exista integraci?n comercial.
- `stock_policy`: ajustar pol?tica de recompra cuando exista m?dulo de reposici?n.
- `products.json`: integrar diagn?stico resumido dentro de `inventory_flow`.

## JSON esperado

Estructura conceptual esperada para futura integraci?n:

```json
{
  "inventory_flow": {
    "business_purpose": "release_cashflow",
    "inventory_bucket": "dormant_stock",
    "sensors": {
      "rotation_sensor": {},
      "cashflow_sensor": {},
      "space_sensor": {},
      "strategic_stock_sensor": {},
      "season_opportunity_sensor": {}
    },
    "diagnosis": {},
    "decision": {},
    "module_signals": {}
  }
}
```

## Pendientes

- Definir variables reales disponibles.
- Definir fuentes de datos.
- Definir umbrales iniciales como hip?tesis.
- Separar reglas M1 de reglas exploratorias.
- Crear tickets espec?ficos antes de modificar `products.json`.
- Evitar convertir etiquetas en decisiones sin c?lculo o condici?n.

?? **Decisi?n tomada:** este caso se trabajar? como decisi?n empresarial de flujo de caja, no como simple alerta de stock lento.
