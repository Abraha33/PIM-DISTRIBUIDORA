# Repos relacionados — Ecosistema ASNO / PIM / ERP

## 1. ERP

Repo: `Abraha33/ERP`

Responsabilidad:
ASNO nuevo / ERP futuro.

Contiene:
- backend
- frontend
- Supabase
- auth
- RLS
- módulos operativos futuros
- base transaccional

No debe:
- redefinir contratos PIM sin coordinación
- absorber el scraper ASNO
- absorber lógica completa de clientes inteligentes

## 2. PIM-DISTRIBUIDORA

Repo: `Abraha33/PIM-DISTRIBUIDORA`

Responsabilidad:
Contrato maestro del producto, diccionarios, schemas, validadores, reportes, módulos PIM y documentación técnica estable.

Contiene:
- products.json v1
- product families
- barcode history
- dictionaries
- schemas
- validators
- module integration docs

No debe:
- contener Supabase del ERP
- contener frontend ERP
- contener scraper completo si vive en repo separado
- contener lógica completa de scoring de clientes si vive en repo separado

## 3. Scraper ASNO

Repo: pendiente confirmar nombre exacto.

Responsabilidad:
Extraer información del ASNO actual / Wappsi.

Posibles salidas:
- productos
- compras
- ventas
- inventario
- kardex
- clientes
- proveedores
- precios
- costos
- HTML/evidencia
- JSON crudo
- JSON limpio

Relación con PIM:
PIM consume, valida o documenta la salida del scraper, pero no necesariamente contiene todo su código.

## 4. Clientes Inteligentes

Repo: pendiente confirmar nombre exacto.

Responsabilidad:
Clasificación, scoring, segmentación y análisis de clientes.

Posibles salidas:
- segmentos
- score de cliente
- cliente ideal / Modelo Valeria
- frecuencia de compra
- ticket promedio
- productos preferidos
- potencial comercial
- alertas comerciales

Relación con PIM:
Puede usar productos normalizados y datos comerciales. PIM puede documentar contratos de entrada/salida, pero no debe absorber toda la lógica de análisis.

## 5. Drive / Obsidian

Responsabilidad:
Memoria viva del ecosistema.

Contiene:
- decisiones
- contexto
- roles
- flujos
- pendientes
- preguntas abiertas
- guías para nuevos chats
