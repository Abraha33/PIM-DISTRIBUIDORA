---
module: purchases_m1
status: partial
type: purchasing
source: chatgpt
last_review: 2026-06-19
---

# Contrato JSON documental — Compras M1

> **Importante:** Este documento contiene un ejemplo documental, no un contrato productivo obligatorio. La estructura definitiva debe validarse contra la salida real de `Scraper_Asno` y los requisitos del ERP futuro.

## Ejemplo documental

```json
{
  "purchase_m1_id": "purchase_m1_example_001",
  "source_system": "ASNO/Wappsi",
  "status": "received_with_evidence",
  "supplier": {
    "supplier_id": null,
    "name": "Proveedor ejemplo"
  },
  "invoice": {
    "number": "FAC-0001",
    "date": "2026-06-20"
  },
  "reception": {
    "status": "received_with_evidence",
    "received_at": "2026-06-20T10:30:00",
    "evidence_photos": [
      {
        "type": "invoice_photo",
        "uri": "pending_storage_uri",
        "notes": "Foto de factura recibida"
      }
    ]
  },
  "items": [
    {
      "line_id": "1",
      "product_code_raw": "ASNO-001",
      "product_name_raw": "Producto ejemplo",
      "product_id_pim": null,
      "quantity_purchased": 10,
      "quantity_received": 10,
      "unit_cost": 1000.00,
      "taxes": 160.00,
      "requires_price_decision": true,
      "new_product_candidate": false,
      "new_product_notice_candidate": true
    }
  ],
  "review": {
    "review_status": "under_review",
    "reviewed_by": null,
    "notes": []
  }
}
```

## Notas sobre el ejemplo

- `supplier_id` es `null` porque el proveedor puede no estar registrado en PIM aún.
- `product_id_pim` es `null` cuando el producto no existe en `products.json`.
- `evidence_photos.uri` usa `"pending_storage_uri"` hasta definir el almacenamiento real.
- `taxes` puede ser 0 si no aplica o no está disponible.
- Los estados deben seguir la lista definida en `04_data_needed.md`.

## Pendiente de definición

- Schema JSON formal (cuando la estructura se estabilice).
- Almacenamiento de fotos/evidencia.
- Integración con el scraper para mapeo real de campos.
