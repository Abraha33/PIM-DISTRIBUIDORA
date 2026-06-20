# Decisiones Cerradas — PIM-DISTRIBUIDORA

Las siguientes decisiones están cerradas y no deben reabrirse sin justificación documentada.

| # | Decisión | Justificación |
|---|----------|---------------|
| 1 | `PIM-DISTRIBUIDORA` no es ERP. | ERP tiene su propio repo con Supabase, frontend, auth y RLS. |
| 2 | Supabase pertenece a `ERP`. | El ERP futuro administra su propia base de datos. |
| 3 | `PIM-DISTRIBUIDORA` no es el repo principal del scraper si Scraper ASNO vive separado. | Cada repo tiene responsabilidad única. |
| 4 | `PIM-DISTRIBUIDORA` no es el repo principal de Clientes Inteligentes si ese análisis vive separado. | No mezclar responsabilidades de análisis de clientes. |
| 5 | `PIM-DISTRIBUIDORA` documenta contratos e integraciones. | No ejecuta lógica productiva de otros repos. |
| 6 | `products.json v1` está estable. | Contrato maestro base completado y validado. |
| 7 | Si hay cambio estructural, debe ser v2. | Preservar integridad del contrato v1. |
| 8 | Los módulos automáticos no sobrescriben campos protegidos sin auditoría. | Evitar corrupción de datos maestros. |
| 9 | Scraper ASNO produce datos; PIM valida/normaliza/contrata. | Separación clara de responsabilidades. |
| 10 | Clientes Inteligentes analiza clientes; PIM puede proveer productos/datos normalizados. | PIM es fuente de verdad de producto, no de análisis comercial. |
| 11 | Compras M1 pertenece a PIM-DISTRIBUIDORA. | El módulo es documentación de contrato y flujo, no ejecución transaccional. |
| 12 | La extracción técnica de compras vive en Scraper_Asno. | Separación de responsabilidades: PIM documenta, scraper extrae. |
| 13 | La recepción con evidencia es parte del flujo de Compras M1. | No es un proceso separado; está integrado. |
| 14 | El aviso de productos nuevos ocurre después de revisión/filtro. | Evita notificaciones prematuras de mercancía no validada. |
| 15 | ERP no se modifica en esta fase de Compras M1. | El ERP futuro consumirá cuando esté maduro. |
