# Pending Modules

Este documento registra los m?dulos pendientes del PIM de Envax.

## inventory_flow

?? pendiente

Responsabilidad futura:

- stock level
- flujo de inventario
- existencias por bodega
- variantes de inventario
- relaci?n con unidad base
- inventario d?bil
- inventario estrat?gico
- inventario b?sico
- oportunidades de temporada
- riesgos f?sicos
- necesidades de reabastecimiento

El stock level no se define todav?a con f?rmulas finales. Se reserva el bloque en el contrato y se desarrolla despu?s.

La metodolog?a oficial est? documentada en `docs/inventory_flow_methodology.md`.

## marketing

?? pendiente

Responsabilidad futura:

- clientes objetivo
- cat?logos
- campa?as
- promociones
- keywords comerciales
- descripciones ecommerce

Las descripciones y keywords quedan vac?as hasta que exista el m?dulo de marketing.

## media

?? pendiente

Responsabilidad futura:

- im?genes por uso
- imagen principal
- im?genes de cat?logo
- im?genes de campa?a
- im?genes t?cnicas
- im?genes de empaque

Las im?genes quedan vac?as hasta que exista el m?dulo `media`.

## scraper / commercial

?? pendiente

Los precios, costos y proveedores se completar?n despu?s de incorporar datos del scraper.

No se crea scraper en esta etapa.

## stock_policy

?? pendiente

Responsabilidad futura:

- reglas de reposici?n
- m?nimos y m?ximos
- pol?ticas por unidad
- alertas operativas

No se crean f?rmulas de stock finales en esta etapa.

## quality_control

?? pendiente

Responsabilidad futura:

- control f?sico del producto
- estado de calidad
- bloqueos por da?o, vencimiento o revisi?n
- trazabilidad de inspecciones

El control de calidad es un m?dulo separado y no debe mezclarse con marketing ni con nombres de producto.

## Decisi?n general

?? decisi?n tomada

`products.json v1` reserva bloques para los m?dulos pendientes, pero no implementa la l?gica interna de esos m?dulos.

Primero el contrato. Despu?s las automatizaciones. Si lo hacemos al rev?s, construimos una casa sin planos y despu?s lloramos cuando no entra la escalera.
