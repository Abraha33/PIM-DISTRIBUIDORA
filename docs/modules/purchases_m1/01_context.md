---
module: purchases_m1
status: partial
type: purchasing
source: chatgpt
last_review: 2026-06-19
---

# Contexto — Compras M1

## Lugar en el ecosistema

Compras M1 pertenece a `PIM-DISTRIBUIDORA` y es el módulo de entrada para el flujo de compras. Actúa como capa de organización entre la extracción técnica (Scraper_Asno) y los procesos aguas abajo (recepción, aviso, precios, ERP).

## Separación de responsabilidades

| Componente | Responsabilidad |
|---|---|
| `PIM-DISTRIBUIDORA` | Define contratos, datos limpios, reglas y documentación del módulo |
| `Scraper_Asno` | Extrae compras, productos, proveedores, costos y evidencia desde ASNO/Wappsi |
| `ERP` | Consumirá el flujo cuando el ERP nuevo madure |
| Usuario humano | Revisa evidencia, valida recepción, define precios si aplica |
| Vendedores / puntos de venta | Reciben aviso de productos nuevos o mercancía relevante |

## ¿Por qué M1?

"M1" significa "primer nivel de madurez de compras". No pretende cubrir todos los casos de una compra compleja (múltiples facturas, pagos parciales, logística inversa). Se enfoca en el caso base:

- Compra simple con un proveedor y una factura.
- Productos identificables por código o nombre.
- Recepción única con evidencia fotográfica.
- Revisión humana para filtrar antes de notificar.

## Principio rector

El módulo no ejecuta lógica productiva. Documenta, organiza y prepara el flujo para que los repositorios de ejecución (Scraper_Asno, ERP futuro) puedan consumir la definición sin ambigüedad.
