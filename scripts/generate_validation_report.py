from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from validate_contracts import (  # noqa: E402
    FAILURE_EXAMPLES_DIR,
    VALIDATION_TARGETS,
    get_validation_errors,
    schema_for_failure_example,
)
from validate_dictionaries import (  # noqa: E402
    DICTIONARY_FAILURES_DIR,
    PRODUCT_CONTRACT,
    load_json as load_dictionary_json,
    validate_product_dictionary_rules,
)
from validate_uniqueness import (  # noqa: E402
    UNIQUENESS_FAILURES_DIR,
    load_scenario,
    validate_uniqueness_rules,
)
from validate_naming import (  # noqa: E402
    NAMING_FAILURES_DIR,
    PRODUCT_CONTRACT as NAMING_PRODUCT_CONTRACT,
    load_json as load_naming_json,
    validate_product_naming_rules,
)
from validate_families import (  # noqa: E402
    FAMILY_FAILURES_DIR,
    load_scenario as load_family_scenario,
    validate_family_rules,
)
from validate_data_quality import (  # noqa: E402
    DATA_QUALITY_FAILURES_DIR,
    PRODUCT_CONTRACT as DATA_QUALITY_PRODUCT_CONTRACT,
    load_json as load_data_quality_json,
    validate_product_data_quality,
)

REPORTS_DIR = ROOT / "reports"
JSON_REPORT_PATH = REPORTS_DIR / "pim_contract_v1_validation_report.json"
MD_REPORT_PATH = REPORTS_DIR / "pim_contract_v1_validation_report.md"


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def make_result(status: str, path: str, message: str, rule: str | None = None) -> dict[str, str]:
    result = {"status": status, "path": path, "message": message}
    if rule:
        result["rule"] = rule
    return result


def collect_schema_validation() -> tuple[str, list[dict[str, str]], list[dict[str, str]]]:
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []

    for contract_path, schema_path in VALIDATION_TARGETS:
        contract_rel = relative(contract_path)
        try:
            validation_errors = get_validation_errors(contract_path, schema_path)
        except Exception as exc:  # noqa: BLE001 - report generator must capture all audit failures
            item = make_result("fail", contract_rel, str(exc), "schema_validation")
            results.append(item)
            errors.append(item)
            continue

        if validation_errors:
            for error in validation_errors:
                field_path = ".".join(str(part) for part in error.absolute_path) or "<root>"
                item = make_result("fail", contract_rel, f"{field_path}: {error.message}", "schema_validation")
                results.append(item)
                errors.append(item)
        else:
            results.append(make_result("pass", contract_rel, "Schema validation passed.", "schema_validation"))

    return ("pass" if not errors else "fail", results, errors)


def collect_validation_failures() -> tuple[str, list[dict[str, str]], list[dict[str, str]]]:
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    failure_files = sorted(FAILURE_EXAMPLES_DIR.glob("*.json"))

    if not failure_files:
        item = make_result("fail", relative(FAILURE_EXAMPLES_DIR), "No controlled schema failure examples found.", "validation_failures")
        return "fail", [item], [item]

    for failure_path in failure_files:
        failure_rel = relative(failure_path)
        try:
            schema_path = schema_for_failure_example(failure_path)
            validation_errors = get_validation_errors(failure_path, schema_path)
        except Exception as exc:  # noqa: BLE001
            item = make_result("fail", failure_rel, f"Validator error: {exc}", "validation_failures")
            results.append(item)
            errors.append(item)
            continue

        if validation_errors:
            results.append(make_result("pass", failure_rel, "Controlled invalid example was rejected as expected.", "validation_failures"))
        else:
            item = make_result("fail", failure_rel, "Controlled invalid example passed unexpectedly.", "validation_failures")
            results.append(item)
            errors.append(item)

    return ("pass" if not errors else "fail", results, errors)


def dictionary_rule_results(errors_by_rule: dict[str, list[str]], path: str) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rule_names = [
        "material_id_exists",
        "color_id_exists",
        "unit_presentation_codes_exist",
        "unit_summary_codes_exist",
        "unit_summary_codes_in_unit_presentation",
        "material_abbreviation_matches_dictionary",
        "color_name_matches_dictionary",
        "unit_presentation_labels_match_code_factor",
    ]
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []

    for rule_name in rule_names:
        if rule_name in errors_by_rule:
            for message in errors_by_rule[rule_name]:
                item = make_result("fail", path, message, rule_name)
                results.append(item)
                errors.append(item)
        else:
            results.append(make_result("pass", path, "Dictionary rule passed.", rule_name))

    return results, errors


def collect_dictionary_validation() -> tuple[str, list[dict[str, str]], list[dict[str, str]]]:
    product = load_dictionary_json(PRODUCT_CONTRACT)
    product_rel = relative(PRODUCT_CONTRACT)
    rule_errors = validate_product_dictionary_rules(product)
    results, errors = dictionary_rule_results(rule_errors, product_rel)
    return ("pass" if not errors else "fail", results, errors)


def collect_dictionary_failures() -> tuple[str, list[dict[str, str]], list[dict[str, str]]]:
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    failure_files = sorted(DICTIONARY_FAILURES_DIR.glob("*.json"))

    if not failure_files:
        item = make_result("fail", relative(DICTIONARY_FAILURES_DIR), "No controlled dictionary failure examples found.", "dictionary_failures")
        return "fail", [item], [item]

    for failure_path in failure_files:
        failure_rel = relative(failure_path)
        product = load_dictionary_json(failure_path)
        rule_errors = validate_product_dictionary_rules(product)
        if rule_errors:
            results.append(make_result("pass", failure_rel, "Controlled dictionary failure was rejected as expected.", "dictionary_failures"))
        else:
            item = make_result("fail", failure_rel, "Controlled dictionary failure passed unexpectedly.", "dictionary_failures")
            results.append(item)
            errors.append(item)

    return ("pass" if not errors else "fail", results, errors)


def uniqueness_rule_results(invalid: dict[str, list[str]], warnings: dict[str, list[str]], path: str) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    rule_names = [
        "product_code_uniqueness",
        "active_barcode_uniqueness",
        "primary_barcode_per_unit",
        "barcode_history_references_existing_product_unit",
        "barcode_history_action_consistency",
    ]
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    warning_items: list[dict[str, str]] = []

    for rule_name in rule_names:
        if rule_name in invalid:
            for message in invalid[rule_name]:
                item = make_result("fail", path, message, rule_name)
                results.append(item)
                errors.append(item)
        else:
            results.append(make_result("pass", path, "Uniqueness rule passed.", rule_name))

    for rule_name, messages in warnings.items():
        for message in messages:
            item = make_result("warning", path, message, rule_name)
            results.append(item)
            warning_items.append(item)

    return results, errors, warning_items


def collect_uniqueness_validation() -> tuple[str, list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    products, barcode_history = load_scenario()
    invalid, warnings = validate_uniqueness_rules(products, barcode_history)
    path = "contracts/products.v1.example.json + contracts/barcode_history.v1.example.json"
    results, errors, warning_items = uniqueness_rule_results(invalid, warnings, path)
    return ("pass" if not errors else "fail", results, errors, warning_items)


def collect_uniqueness_failures() -> tuple[str, list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    warning_items: list[dict[str, str]] = []
    failure_files = sorted(UNIQUENESS_FAILURES_DIR.glob("*.json"))

    if not failure_files:
        item = make_result("fail", relative(UNIQUENESS_FAILURES_DIR), "No controlled uniqueness failure examples found.", "uniqueness_failures")
        return "fail", [item], [item], []

    for failure_path in failure_files:
        failure_rel = relative(failure_path)
        products, barcode_history = load_scenario(failure_path)
        invalid, warnings = validate_uniqueness_rules(products, barcode_history)
        if invalid:
            results.append(make_result("pass", failure_rel, "Controlled uniqueness failure was rejected as expected.", "uniqueness_failures"))
        elif warnings:
            warning = make_result("warning", failure_rel, "Controlled warning example emitted a warning as expected.", "uniqueness_failures")
            results.append(warning)
            warning_items.append(warning)
        else:
            item = make_result("fail", failure_rel, "Controlled uniqueness failure passed unexpectedly.", "uniqueness_failures")
            results.append(item)
            errors.append(item)

    return ("pass" if not errors else "fail", results, errors, warning_items)


def naming_rule_results(invalid: dict[str, list[str]], warnings: dict[str, list[str]], path: str) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    rule_names = [
        "pos_name_components",
        "pos_name_forbidden_components",
        "logistics_name_components",
        "internal_name_components",
        "ecommerce_short_components",
        "ecommerce_short_forbidden_components",
        "ecommerce_long_components",
        "unit_label_format_in_names",
    ]
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    warning_items: list[dict[str, str]] = []

    for rule_name in rule_names:
        if rule_name in invalid:
            for message in invalid[rule_name]:
                item = make_result("fail", path, message, rule_name)
                results.append(item)
                errors.append(item)
        else:
            results.append(make_result("pass", path, "Naming rule passed.", rule_name))

    for rule_name, messages in warnings.items():
        for message in messages:
            item = make_result("warning", path, message, rule_name)
            results.append(item)
            warning_items.append(item)

    return results, errors, warning_items


def collect_naming_validation() -> tuple[str, list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    product = load_naming_json(NAMING_PRODUCT_CONTRACT)
    invalid, warnings = validate_product_naming_rules(product)
    results, errors, warning_items = naming_rule_results(invalid, warnings, relative(NAMING_PRODUCT_CONTRACT))
    return ("pass" if not errors else "fail", results, errors, warning_items)


def collect_naming_failures() -> tuple[str, list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    warning_items: list[dict[str, str]] = []
    failure_files = sorted(NAMING_FAILURES_DIR.glob("*.json"))

    if not failure_files:
        item = make_result("fail", relative(NAMING_FAILURES_DIR), "No controlled naming failure examples found.", "naming_failures")
        return "fail", [item], [item], []

    for failure_path in failure_files:
        failure_rel = relative(failure_path)
        product = load_naming_json(failure_path)
        invalid, warnings = validate_product_naming_rules(product)
        if invalid:
            results.append(make_result("pass", failure_rel, "Controlled naming failure was rejected as expected.", "naming_failures"))
        elif warnings:
            warning = make_result("warning", failure_rel, "Controlled naming warning emitted a warning as expected.", "naming_failures")
            results.append(warning)
            warning_items.append(warning)
        else:
            item = make_result("fail", failure_rel, "Controlled naming failure passed unexpectedly.", "naming_failures")
            results.append(item)
            errors.append(item)

    return ("pass" if not errors else "fail", results, errors, warning_items)




def family_rule_results(invalid: dict[str, list[str]], warnings: dict[str, list[str]], path: str) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    rule_names = [
        "family_id_consistency",
        "children_codes_consistency",
        "product_family_membership",
        "duplicate_child_membership",
        "family_parent_product",
    ]
    warning_rule_names = [
        "parent_code_consistency",
        "variant_axis_consistency",
        "product_sellability",
    ]
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    warning_items: list[dict[str, str]] = []

    for rule_name in rule_names:
        if rule_name in invalid:
            for message in invalid[rule_name]:
                item = make_result("fail", path, message, rule_name)
                results.append(item)
                errors.append(item)
        else:
            results.append(make_result("pass", path, "Family rule passed.", rule_name))

    for rule_name in warning_rule_names:
        if rule_name in warnings:
            for message in warnings[rule_name]:
                item = make_result("warning", path, message, rule_name)
                results.append(item)
                warning_items.append(item)
        else:
            results.append(make_result("pass", path, "Family warning rule passed.", rule_name))

    return results, errors, warning_items


def collect_family_validation() -> tuple[str, list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    products, families = load_family_scenario()
    invalid, warnings = validate_family_rules(products, families)
    path = "contracts/products.v1.example.json + contracts/product_families.v1.example.json"
    results, errors, warning_items = family_rule_results(invalid, warnings, path)
    return ("pass" if not errors else "fail", results, errors, warning_items)


def collect_family_failures() -> tuple[str, list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    warning_items: list[dict[str, str]] = []
    failure_files = sorted(FAMILY_FAILURES_DIR.glob("*.json"))

    if not failure_files:
        item = make_result("fail", relative(FAMILY_FAILURES_DIR), "No controlled family failure examples found.", "family_failures")
        return "fail", [item], [item], []

    for failure_path in failure_files:
        failure_rel = relative(failure_path)
        products, families = load_family_scenario(failure_path)
        invalid, warnings = validate_family_rules(products, families)
        if invalid:
            results.append(make_result("pass", failure_rel, "Controlled family failure was rejected as expected.", "family_failures"))
        elif warnings:
            warning = make_result("warning", failure_rel, "Controlled family warning emitted a warning as expected.", "family_failures")
            results.append(warning)
            warning_items.append(warning)
        else:
            item = make_result("fail", failure_rel, "Controlled family failure passed unexpectedly.", "family_failures")
            results.append(item)
            errors.append(item)

    return ("pass" if not errors else "fail", results, errors, warning_items)



def data_quality_rule_results(invalid: dict[str, list[str]], warnings: dict[str, list[str]], path: str) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    rule_names = [
        "data_quality_status_allowed",
        "ready_requires_no_missing_fields",
        "ready_requires_no_errors",
        "errors_prevent_ready",
        "missing_fields_prevent_ready",
        "missing_core_fields_are_listed",
        "data_quality_arrays_are_strings",
    ]
    warning_rule_names = [
        "same_min_max_unit",
        "reference_label_empty",
        "brand_name_empty",
        "prices_empty_v1",
        "costs_empty_v1",
        "suppliers_empty_v1",
    ]
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    warning_items: list[dict[str, str]] = []

    for rule_name in rule_names:
        if rule_name in invalid:
            for message in invalid[rule_name]:
                item = make_result("fail", path, message, rule_name)
                results.append(item)
                errors.append(item)
        else:
            results.append(make_result("pass", path, "Data quality rule passed.", rule_name))

    for rule_name in warning_rule_names:
        if rule_name in warnings:
            for message in warnings[rule_name]:
                item = make_result("warning", path, message, rule_name)
                results.append(item)
                warning_items.append(item)
        else:
            results.append(make_result("pass", path, "Data quality warning rule passed.", rule_name))

    return results, errors, warning_items


def collect_data_quality_validation() -> tuple[str, list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    product = load_data_quality_json(DATA_QUALITY_PRODUCT_CONTRACT)
    invalid, warnings = validate_product_data_quality(product)
    results, errors, warning_items = data_quality_rule_results(invalid, warnings, relative(DATA_QUALITY_PRODUCT_CONTRACT))
    return ("pass" if not errors else "fail", results, errors, warning_items)


def collect_data_quality_failures() -> tuple[str, list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    results: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    warning_items: list[dict[str, str]] = []
    failure_files = sorted(DATA_QUALITY_FAILURES_DIR.glob("*.json"))

    if not failure_files:
        item = make_result("fail", relative(DATA_QUALITY_FAILURES_DIR), "No controlled data_quality failure examples found.", "data_quality_failures")
        return "fail", [item], [item], []

    for failure_path in failure_files:
        failure_rel = relative(failure_path)
        product = load_data_quality_json(failure_path)
        invalid, warnings = validate_product_data_quality(product)
        if invalid:
            results.append(make_result("pass", failure_rel, "Controlled data_quality failure was rejected as expected.", "data_quality_failures"))
        elif warnings:
            warning = make_result("warning", failure_rel, "Controlled data_quality warning emitted a warning as expected.", "data_quality_failures")
            results.append(warning)
            warning_items.append(warning)
        else:
            item = make_result("fail", failure_rel, "Controlled data_quality failure passed unexpectedly.", "data_quality_failures")
            results.append(item)
            errors.append(item)

    return ("pass" if not errors else "fail", results, errors, warning_items)

def build_report() -> dict[str, Any]:
    schema_status, schema_results, schema_errors = collect_schema_validation()
    validation_failures_status, validation_failures_results, validation_failures_errors = collect_validation_failures()
    dictionary_status, dictionary_results, dictionary_errors = collect_dictionary_validation()
    dictionary_failures_status, dictionary_failures_results, dictionary_failures_errors = collect_dictionary_failures()
    uniqueness_status, uniqueness_results, uniqueness_errors, uniqueness_warnings = collect_uniqueness_validation()
    uniqueness_failures_status, uniqueness_failures_results, uniqueness_failures_errors, uniqueness_failures_warnings = collect_uniqueness_failures()
    naming_status, naming_results, naming_errors, naming_warnings = collect_naming_validation()
    naming_failures_status, naming_failures_results, naming_failures_errors, naming_failures_warnings = collect_naming_failures()
    family_status, family_results, family_errors, family_warnings = collect_family_validation()
    family_failures_status, family_failures_results, family_failures_errors, family_failures_warnings = collect_family_failures()
    data_quality_status, data_quality_results, data_quality_errors, data_quality_warnings = collect_data_quality_validation()
    data_quality_failures_status, data_quality_failures_results, data_quality_failures_errors, data_quality_failures_warnings = collect_data_quality_failures()

    all_errors = (
        schema_errors
        + validation_failures_errors
        + dictionary_errors
        + dictionary_failures_errors
        + uniqueness_errors
        + uniqueness_failures_errors
        + naming_errors
        + naming_failures_errors
        + family_errors
        + family_failures_errors
        + data_quality_errors
        + data_quality_failures_errors
    )
    all_warnings = uniqueness_warnings + uniqueness_failures_warnings + naming_warnings + naming_failures_warnings + family_warnings + family_failures_warnings + data_quality_warnings + data_quality_failures_warnings
    overall_status = "fail" if all_errors else "pass"

    return {
        "contract_version": "products.json v1",
        "repository": "PIM-DISTRIBUIDORA",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "overall_status": overall_status,
        "summary": {
            "schema_validation": schema_status,
            "validation_failures": validation_failures_status,
            "dictionary_validation": dictionary_status,
            "dictionary_failures": dictionary_failures_status,
            "uniqueness_validation": uniqueness_status,
            "uniqueness_failures": uniqueness_failures_status,
            "naming_validation": naming_status,
            "naming_failures": naming_failures_status,
            "family_validation": family_status,
            "family_failures": family_failures_status,
            "data_quality_validation": data_quality_status,
            "data_quality_failures": data_quality_failures_status,
            "warnings_count": len(all_warnings),
            "errors_count": len(all_errors),
        },
        "results": {
            "schema_validation": schema_results,
            "validation_failures": validation_failures_results,
            "dictionary_validation": dictionary_results,
            "dictionary_failures": dictionary_failures_results,
            "uniqueness_validation": uniqueness_results,
            "uniqueness_failures": uniqueness_failures_results,
            "naming_validation": naming_results,
            "naming_failures": naming_failures_results,
            "family_validation": family_results,
            "family_failures": family_failures_results,
            "data_quality_validation": data_quality_results,
            "data_quality_failures": data_quality_failures_results,
            "warnings": all_warnings,
            "errors": all_errors,
        },
        "next_recommended_step": "Agregar validaci?n de cobertura documental entre docs/ y scripts sin implementar l?gica comercial.",
    }


def status_label(status: str) -> str:
    if status == "pass":
        return "? pass"
    if status == "warning":
        return "?? warning"
    return "? fail"


def render_items(items: list[dict[str, str]]) -> str:
    if not items:
        return "- ? pass ? Sin hallazgos."

    lines = []
    for item in items:
        rule = f" `{item['rule']}`" if "rule" in item else ""
        lines.append(f"- {status_label(item['status'])}{rule} ? `{item['path']}` ? {item['message']}")
    return "\n".join(lines)


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    results = report["results"]

    return f"""
# Reporte de Validaci?n PIM Contract v1

## Estado general

{status_label(report['overall_status'])}

- Contrato: `{report['contract_version']}`
- Repositorio: `{report['repository']}`
- Generado: `{report['generated_at']}`

## Resumen

| Capa | Estado |
| --- | --- |
| Validaci?n de schema | {status_label(summary['schema_validation'])} |
| Ejemplos inv?lidos controlados | {status_label(summary['validation_failures'])} |
| Validaci?n de diccionarios | {status_label(summary['dictionary_validation'])} |
| Fallos controlados de diccionario | {status_label(summary['dictionary_failures'])} |
| Validaci?n de unicidad | {status_label(summary['uniqueness_validation'])} |
| Fallos controlados de unicidad | {status_label(summary['uniqueness_failures'])} |
| Validaci?n de nombres | {status_label(summary['naming_validation'])} |
| Fallos controlados de nombres | {status_label(summary['naming_failures'])} |
| Validaci?n de familias y variantes | {status_label(summary['family_validation'])} |
| Fallos controlados de familias y variantes | {status_label(summary['family_failures'])} |
| Validaci?n de data_quality | {status_label(summary['data_quality_validation'])} |
| Fallos controlados de data_quality | {status_label(summary['data_quality_failures'])} |
| Advertencias | ?? {summary['warnings_count']} |
| Errores | ? {summary['errors_count']} |

## Validaci?n de schema

{render_items(results['schema_validation'])}

## Ejemplos inv?lidos controlados

{render_items(results['validation_failures'])}

## Validaci?n de diccionarios

{render_items(results['dictionary_validation'])}

## Fallos controlados de diccionario

{render_items(results['dictionary_failures'])}

## Validaci?n de unicidad

{render_items(results['uniqueness_validation'])}

## Fallos controlados de unicidad

{render_items(results['uniqueness_failures'])}

## Validaci?n de nombres

{render_items(results['naming_validation'])}

## Fallos controlados de nombres

{render_items(results['naming_failures'])}

## Validaci?n de familias y variantes

{render_items(results['family_validation'])}

## Fallos controlados de familias y variantes

{render_items(results['family_failures'])}

## Validaci?n de data_quality

{render_items(results['data_quality_validation'])}

## Fallos controlados de data_quality

{render_items(results['data_quality_failures'])}

## Advertencias

{render_items(results['warnings'])}

## Errores

{render_items(results['errors'])}

## Siguiente paso recomendado

{report['next_recommended_step']}
""".strip() + "\n"


def write_json_report(report: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    JSON_REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_markdown_report(report: dict[str, Any]) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    MD_REPORT_PATH.write_text(render_markdown(report), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate consolidated Envax PIM contract v1 validation report.")
    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument("--json-only", action="store_true", help="Generate only the JSON report.")
    output_group.add_argument("--md-only", action="store_true", help="Generate only the Markdown report.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report()

    if not args.md_only:
        write_json_report(report)
        print(f"REPORT_JSON: {relative(JSON_REPORT_PATH)}")

    if not args.json_only:
        write_markdown_report(report)
        print(f"REPORT_MD: {relative(MD_REPORT_PATH)}")

    print(f"OVERALL_STATUS: {report['overall_status']}")
    return 0 if report["overall_status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
