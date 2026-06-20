---
module: new_products_notice
status: partial
type: workflow
source: chatgpt
last_review: 2026-06-19
---

# Flujo funcional — New Products Notice

## Diagrama de flujo

```
1. Compra en estado under_review o approved
       │
2. Se identifican items con new_product_notice_candidate = true
       │
3. Se filtran según reglas de producto nuevo vs reposición
       │
4. Se prepara contenido del aviso
       │
5. Se define canal y destinatarios
       │
6. Se genera y envía el aviso
       │
7. Compra pasa a closed o ready_for_notice
```

## Reglas de activación

- Un aviso se genera solo si la compra pasó por `under_review`.
- Un producto marcado como `new_product_candidate` es automáticamente candidato a aviso.
- Reposiciones relevantes (producto sin compra en N meses) pueden generar aviso si se configura.

## Contenido del aviso

- Nombre del producto
- Código raw (ASNO/Wappsi)
- Costo unitario
- Cantidad recibida
- Foto de evidencia (si aplica)
- Fecha de recepción

## Canales posibles

| Canal | Estado |
|---|---|
| WhatsApp | Pendiente de definir |
| Dashboard PIM | Pendiente de definir |
| Reporte periódico | Pendiente de definir |
| ERP futuro | Futuro |

## Pendiente de definición

- Canal concreto de envío.
- Destinatarios específicos.
- Frecuencia del aviso (inmediato, diario, semanal).
- Template del mensaje.
