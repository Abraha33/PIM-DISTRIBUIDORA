# Documentation Coverage v1

## Por qu? existe

La cobertura documental existe para asegurar que cada validador importante del contrato PIM tenga una documentaci?n asociada y f?cil de encontrar.

Un validador sin documentaci?n es deuda t?cnica disfrazada. Funciona hoy, pero ma?ana nadie sabe por qu? existe, qu? cubre o qu? NO cubre. Y ah? empiezan los cambios a ciegas, hermano.

## Scripts que deben estar documentados

? definido

- `scripts/validate_contracts.py`
- `scripts/validate_dictionaries.py`
- `scripts/validate_uniqueness.py`
- `scripts/validate_naming.py`
- `scripts/validate_families.py`
- `scripts/validate_data_quality.py`
- `scripts/generate_validation_report.py`

## Documentos esperados

? definido

- `docs/schema_contracts_v1.md` o `README.md` para `validate_contracts.py`.
- `docs/dictionary_validation_v1.md` para `validate_dictionaries.py`.
- `docs/uniqueness_validation_v1.md` para `validate_uniqueness.py`.
- `docs/naming_validation_v1.md` para `validate_naming.py`.
- `docs/family_validation_v1.md` para `validate_families.py`.
- `docs/data_quality_validation_v1.md` para `validate_data_quality.py`.
- `docs/validation_report_v1.md` para `generate_validation_report.py`.

Cada documento debe mencionar el nombre del script relacionado.

## README

`README.md` debe mencionar los comandos principales:

```bash
python scripts/validate_contracts.py
python scripts/validate_dictionaries.py
python scripts/validate_uniqueness.py
python scripts/validate_naming.py
python scripts/validate_families.py
python scripts/validate_data_quality.py
python scripts/generate_validation_report.py
```

## C?mo ejecutar

```bash
python scripts/validate_documentation_coverage.py
python scripts/validate_contracts.py --include-docs
```

## Qu? no cubre

?? pendiente

- Calidad del contenido t?cnico de cada documento.
- Ortograf?a.
- Completitud sem?ntica profunda.
- Sincronizaci?n exacta l?nea por l?nea entre c?digo y documentaci?n.
- Reglas de negocio.

?? decisi?n tomada: esta validaci?n comprueba cobertura documental m?nima, no reemplaza revisi?n t?cnica humana.

?? recomendaci?n experta: documentaci?n sin validaci?n se pudre. Validaci?n sin documentaci?n se vuelve magia negra. Necesit?s las dos.
