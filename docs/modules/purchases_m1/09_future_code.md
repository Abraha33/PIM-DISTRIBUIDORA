---
module: purchases_m1
status: partial
type: purchasing
source: chatgpt
last_review: 2026-06-19
---

# Código futuro — Compras M1

> Esta sección describe posibles implementaciones futuras. No es código productivo.

## Posibles validadores

Cuando el contrato JSON se estabilice, se podrían crear:

- `validate_purchases_m1.py` — valida estructura del contrato de compra.
- `validate_purchase_flow.py` — valida transiciones de estado válidas.

## Posible integración con scripts existentes

El módulo podría integrarse con la suite de validación actual:

```bash
python scripts/validate_contracts.py --include-purchases-m1
```

Esto requeriría:

1. Definir schema JSON formal en `schemas/`.
2. Crear validador específico.
3. Agregar flag `--include-purchases-m1` al script principal.

## Posible dashboard

Un dashboard futuro de Compras M1 podría mostrar:

- Compras detectadas vs completadas.
- Productos nuevos pendientes de aviso.
- Compras con `requires_price_decision` sin resolver.
- Tiempo promedio de ciclo (detección → cierre).

## Contratos JSON futuros

Cuando la estructura se estabilice:

1. Mover el ejemplo de `05_json_contract.md` a `contracts/` como `purchases_m1.v1.example.json`.
2. Crear schema asociado en `schemas/`.
3. Actualizar validadores para cubrir el nuevo contrato.

## Orden sugerido de implementación

1. Confirmar datos reales del scraper.
2. Ajustar contrato JSON documental.
3. Crear schema formal.
4. Crear validador.
5. Integrar con script de validación general.
6. Construir dashboard si aplica.
