# Compras M1 — Registro de facturas por sesión de fotos

**Estado:** BORRADOR  
**Módulo:** Compras M1  
**Tema:** Registro de facturas por sesión de fotos  
**Propósito:** guardar la lógica discutida para continuar después.

## 1. Objetivo

Diseñar el flujo para que un operario registre facturas de compra tomando fotos, con mínima interacción, y que luego el encargado pueda revisar y registrar la compra en ASNO.

## 2. Concepto principal

La unidad principal es una sesión general de captura.

Una sesión general puede contener varias facturas.

Cada factura puede tener varias fotos u hojas.

Cada factura tiene su proveedor seleccionado desde una lista.

## 3. Flujo general

1. Operario abre la aplicación.
2. Presiona Empezar.
3. Empieza a capturar una factura.
4. Toma foto de la hoja.
5. Después de cada foto decide:
   - aprobar foto
   - repetir foto
   - descartar foto
6. Puede tomar tantas fotos como hojas tenga la factura.
7. Al terminar las fotos de esa factura, puede:
   - continuar
   - reiniciar factura actual
   - agregar incidencia
8. Si continúa, selecciona proveedor.
9. Después de seleccionar proveedor, puede:
   - siguiente factura
   - terminar sesión
10. Si elige siguiente factura, repite el flujo.
11. Si elige terminar sesión, se cierra la sesión general.
12. El encargado luego ve la lista de facturas capturadas del día.

## 4. Reglas de fotos

- Cada foto debe ser confirmada por el usuario.
- Si una foto no sirve, se puede repetir.
- Reiniciar factura significa borrar o reemplazar toda la captura de la factura actual.
- Reiniciar no cierra la sesión general.
- Una factura puede tener una o muchas fotos.

## 5. Proveedor

- El proveedor se selecciona después de capturar las fotos de la factura.
- El proveedor viene de una lista ya definida.
- Si el proveedor no existe, debe poder agregarse manualmente.
- El sistema puede validar o sugerir corrección después usando OCR, historial o coincidencias, pero no debe cambiarlo automáticamente sin confirmación.

## 6. Incidencias

La incidencia es opcional y la decide el operario.

El sistema no sugiere incidencias.

Una factura puede tener una incidencia general.

Esa incidencia puede incluir varios problemas o varios productos afectados.

La incidencia debe tener como mínimo una foto de evidencia.

Puede tener varias fotos.

La incidencia debe tener nota en texto.

El texto puede venir de dictado por voz usando Wispr u otra herramienta, pero para el sistema la nota final es texto.

Luego esa nota puede normalizarse.

## 7. Tipos de incidencia

- producto dañado
- producto incompleto
- producto equivocado
- cantidad diferente
- precio diferente
- devolución
- cambio
- mercancía pendiente
- factura con error
- otro

## 8. Guía para nota de incidencia

La app puede guiar al operario con preguntas simples:

- ¿Qué pasó?
- ¿Qué producto tuvo el problema?
- ¿Cuántas unidades/cajas tienen problema?
- ¿En qué estado llegó?
- ¿Qué se debe hacer?
- ¿Ya se habló con alguien?

La guía no debe volver lento el proceso.

Modo recomendado:

1. Tipo de incidencia.
2. Fotos.
3. Nota libre en texto o dictado a texto.
4. Guardar.

## 9. Vista del encargado

El encargado ve una lista de facturas capturadas del día.

Cada factura puede mostrar:

- proveedor
- cantidad de fotos
- estado
- etiqueta “Con incidencia” si aplica

Si el encargado hace clic en la etiqueta, ve:

- tipo de incidencia
- producto o texto relacionado
- fotos de evidencia
- nota original
- nota normalizada

## 10. Roles

### Operario

- toma fotos
- confirma fotos
- reinicia factura si quedó mal
- registra incidencia si existe
- selecciona proveedor
- pasa a siguiente factura o termina sesión

### Encargado

- revisa facturas capturadas
- registra compra en ASNO
- revisa cambios de precio
- registra flete
- registra descuento
- ve incidencias
- no elimina la nota interna original del operario

## 11. ASNO

ASNO es el sistema contable destino.

ASNO no define el flujo.

El sistema propio debe:

- guardar imágenes
- organizar sesiones
- procesar OCR
- normalizar datos
- preparar la compra
- registrar en ASNO mediante bot/automatización cuando esté listo

No depender de ASNO para guardar múltiples imágenes.

## 12. Costos, descuento y prorrateo

- El descuento se registra como descuento total.
- El descuento puede venir de factura o ser digitado por el encargado.
- El prorrateo queda desactivado por defecto.
- El prorrateo debe quedar como opción configurable futura.
- Fletes y otros gastos se registran, pero no deben complicar M1 desde el inicio.

## 13. Estados sugeridos

### Sesión general

- abierta
- en_captura
- finalizada
- pendiente_revision
- procesada

### Factura capturada

- capturando
- fotos_confirmadas
- proveedor_asignado
- con_incidencia
- pendiente_revision
- lista_para_registro
- registrada_en_asno

### Incidencia

- creada
- pendiente_revision
- reportada
- resuelta
- rechazada

## 14. Decisiones tomadas

- La unidad principal es sesión general.
- La sesión general puede tener varias facturas.
- Cada factura puede tener varias fotos.
- El proveedor se selecciona por factura.
- Después del proveedor se decide siguiente factura o terminar sesión.
- Reiniciar factura reinicia toda la factura actual.
- La incidencia es manual, no sugerida por el sistema.
- La incidencia exige mínimo una foto.
- La nota de incidencia es texto.
- Wispr puede usarse para dictado a texto.
- El encargado ve etiqueta “Con incidencia”.
- ASNO recibe datos preparados, no controla el flujo.

## 15. Pendientes

- Definir estructura JSON final de `purchase_capture_session`.
- Definir estructura JSON final de `captured_invoice`.
- Definir estructura JSON final de `incident`.
- Definir botones exactos de la interfaz.
- Definir si se permite guardar factura sin proveedor.
- Definir cómo se corrige proveedor mal seleccionado.
- Definir cómo se normaliza la nota de incidencia.
- Definir qué campos mínimos necesita el bot para registrar en ASNO.
- Definir almacenamiento de imágenes en módulo media/images.

## 16. Siguiente paso recomendado

Diseñar la estructura JSON borrador para:

- `purchase_capture_session`
- `captured_invoice`
- `incident`
