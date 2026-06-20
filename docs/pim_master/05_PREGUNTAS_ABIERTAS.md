# Preguntas Abiertas — PIM-DISTRIBUIDORA

| # | Pregunta | Contexto | Propuesta |
|---|----------|----------|-----------|
| 1 | ¿Cuál es el nombre exacto del repo Scraper ASNO? | Se menciona como repo separado pero no se ha confirmado la URL. | Confirmar con el equipo. |
| 2 | ¿Cuál es el nombre exacto del repo Clientes Inteligentes? | Se menciona como repo separado pero no se ha confirmado la URL. | Confirmar con el equipo. |
| 3 | ¿Qué salidas del scraper deben convertirse en contratos PIM? | El scraper produce múltiples salidas. | Definir prioridad de contratos. |
| 4 | ¿Qué datos crudos del scraper se guardan fuera de PIM? | No todo debe pasar por PIM. | Definir límites. |
| 5 | ¿Qué datos limpios del scraper entran al PIM? | Los datos normalizados deben tener contrato. | Definir schemas de entrada. |
| 6 | ¿Qué salidas de Clientes Inteligentes necesita PIM? | PIM puede necesitar segmentos o scores. | Definir contratos de consumo. |
| 7 | ¿Modelo Valeria vive en PIM, Clientes Inteligentes o ambos? | Hay ambigüedad sobre dónde reside. | Decidir ubicación. |
| 8 | ¿Qué contrato debe existir entre PIM y Clientes Inteligentes? | Contrato de entrada/salida. | Definir schemas. |
| 9 | ¿Qué contrato debe existir entre Scraper ASNO y PIM? | Contrato de entrada/salida. | Definir schemas. |
| 10 | ¿Qué parte consumirá el ERP futuro? | El ERP consumirá PIM pero no totalmente. | Definir alcance. |
| 11 | ¿Quién toma la foto de recepción? | La evidencia fotográfica es parte del flujo. | Almacén, recepcionista o comprador. |
| 12 | ¿Dónde se guarda la evidencia (fotos)? | Las fotos requieren almacenamiento. | Pendiente de definir (local, S3, Supabase). |
| 13 | ¿Qué se considera producto nuevo? | Puede ser nuevo para PIM pero no nuevo en el mercado. | Definir regla: no existe en products.json. |
| 14 | ¿Qué se considera reposición relevante? | No toda reposición merece aviso. | Definir umbral: producto sin compra en N meses. |
| 15 | ¿Quién decide precio final en el flujo de compra? | El flujo marca requires_price_decision. | Gerente, administrador o vendedor. |
| 16 | ¿Qué vendedores o puntos de venta reciben aviso? | El aviso debe llegar a los interesados. | Lista por categoría de producto o zona. |
| 17 | ¿El aviso se genera automático o requiere aprobación humana? | El flujo actual requiere revisión. | Podría ser automático para productos conocidos. |
