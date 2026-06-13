# Naming Rules v1

## Principio

Los nombres del PIM deben ser consistentes, legibles y derivados de campos controlados. El nombre final no es una ocurrencia manual: es una composici?n gobernada.

## POS

? definido

Formato:

```text
category.final + material + color + capacity + dimensions + unit_min + unit_max
```

Ejemplo:

```text
Sello Plus PET Cristal 32 OZ UND(1) CJ(200)
```

La referencia no entra en POS.

## Logistics

? definido

Formato:

```text
code + reference + category.final + material + color + capacity + dimensions + unit_min + unit_max
```

Ejemplo:

```text
D753200 - Ref 753200 - Sello Plus PET Cristal 32 OZ UND(1) CJ(200)
```

## Internal / admin

? definido

Formato:

```text
code + category.final + reference + material + color + capacity + dimensions + unit_min + unit_max
```

Ejemplo:

```text
D753200 - Sello Plus Ref 753200 PET Cristal 32 OZ UND(1) CJ(200)
```

## Ecommerce short

? definido

Formato:

```text
category.final + material + color + capacity + dimensions + unit_min + unit_max
```

La referencia no entra en ecommerce short.

## Ecommerce long

? definido

Formato:

```text
category.final + brand + material + color + capacity + dimensions + Presentaciones + reference at the end
```

Ejemplo:

```text
Sello Plus Darnel PET Cristal 32 OZ - Presentaciones: UND(1), PAQ(100), CJ(200) - Ref 753200
```

## Reglas de referencia

?? decisi?n tomada

- La referencia no entra en POS.
- La referencia no entra en ecommerce short.
- La referencia s? entra en logistics.
- La referencia s? entra en internal/admin.
- La referencia s? entra en ecommerce long, al final.

## Formato de unidades

?? decisi?n tomada

El formato final de unidad es:

```text
CODE(factor)
```

Ejemplos:

- `UND(1)`
- `PAQ(100)`
- `CJ(200)`

## Limpieza obligatoria

?? decisi?n tomada

`UAP` y `P.MAYOR` no deben permanecer en los nombres finales.

Esos valores pueden existir como se?ales de origen o reglas comerciales durante el procesamiento, pero el nombre final debe usar la unidad normalizada:

- `unit_min`
- `unit_max`
- `unit_presentation[].label`

?? recomendaci?n experta

No metas reglas especiales dentro del string final. El string es salida, no fuente de verdad. La fuente de verdad es la estructura.
