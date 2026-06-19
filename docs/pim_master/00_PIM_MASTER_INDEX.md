# PIM Master Index

## ¿Qué es PIM-DISTRIBUIDORA?

`PIM-DISTRIBUIDORA` es el repositorio maestro del PIM de Envax. Contiene contratos de producto, diccionarios, schemas, validadores, reportes, documentación estable y módulos PIM.

Potencia el ASNO actual.

## ¿Qué NO es PIM-DISTRIBUIDORA?

- **No es ERP.** El ERP futuro vive en `Abraha33/ERP` con Supabase, frontend, auth y RLS.
- **No es el scraper.** La extracción de datos del ASNO actual / Wappsi vive en un repo separado (Scraper ASNO).
- **No es Clientes Inteligentes.** La clasificación, scoring y segmentación de clientes vive en un repo separado.
- **No es la memoria viva.** Drive/Obsidian guarda contexto, decisiones, roles, flujos y pendientes.

## Estado actual

- `products.json v1` ya está estable como contrato maestro.
- Diccionarios, schemas y validadores existen y se ejecutan.
- Los módulos futuros deben respetar `docs/module_integration_plan.md`.

## Responsabilidades

PIM define:

- Contratos de producto (JSON con schemas)
- Diccionarios (unidades, materiales, colores)
- Validadores (estructura, diccionarios, unicidad, naming, familias, data quality)
- Reglas de negocio documentadas
- Documentación técnica estable

## Relación con otros repos del ecosistema

| Repo | Responsabilidad | Relación con PIM |
|------|----------------|------------------|
| `ERP` | ASNO nuevo / ERP futuro | Consumirá PIM en el futuro |
| Scraper ASNO | Extracción de datos del ASNO actual | PIM documenta cómo consumir su salida |
| Clientes Inteligentes | Scoring y segmentación de clientes | PIM puede definir contratos de entrada/salida |
| Drive/Obsidian | Memoria viva del ecosistema | Guía para nuevos chats, no se mezcla en el repo |

## Convenciones

- Los cambios estructurales requieren versión nueva (ej: v2).
- No se escribe lógica productiva hasta que el contrato esté sólido.
- Supabase, frontend, auth y RLS pertenecen al ERP.
- El scraper y clientes inteligentes no se copian completos aquí.

## Entradas principales

- `docs/pim_master/06_REPOS_RELACIONADOS.md` — mapa de repos relacionados
- `docs/pim_master/01_MODULES_INDEX.md` — índice de módulos PIM con estados
- `docs/modules/` — documentación de cada módulo
- `docs/roles/` — roles por módulo
- `docs/module_integration_plan.md` — plan de integración existente
