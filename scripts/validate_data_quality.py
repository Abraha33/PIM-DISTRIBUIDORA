from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PRODUCT_CONTRACT = ROOT / "contracts" / "products.v1.example.json"
DATA_QUALITY_FAILURES_DIR = ROOT / "examples" / "data_quality_failures"

RuleMessages = dict[str, list[str]]
ALLOWED_STATUS = {"pending", "ready", "needs_review", "incomplete"}
CORE_FIELDS = [
    "code",
    "identity.final_name",
    "category.final.name",
    "attributes.material.id",
    "attributes.color.id",
    "unit_summary.minimum_sale_unit.code",
    "unit_summary.maximum_purchase_unit.code",
    "names.pos",
    "names.logistics",
    "names.internal",
    "names.ecommerce_short",
    "names.ecommerce_long",
]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def add(messages: RuleMessages, rule_name: str, message: str) -> None:
    messages.setdefault(rule_name, []).append(message)


def get_path(data: dict[str, Any], dotted_path: str) -> Any:
    current: Any = data
    for part in dotted_path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def is_empty(value: Any) -> bool:
    return value is None or value == ""


def is_array_of_strings(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value)


def validate_product_data_quality(product: dict[str, Any]) -> tuple[RuleMessages, RuleMessages]:
    invalid: RuleMessages = {}
    warnings: RuleMessages = {}
    dq = product.get("data_quality", {})

    status = dq.get("status")
    missing_fields = dq.get("missing_fields")
    dq_warnings = dq.get("warnings")
    dq_errors = dq.get("errors")

    if status not in ALLOWED_STATUS:
        add(invalid, "data_quality_status_allowed", f"data_quality.status '{status}' is not allowed")

    for field_name, value in (("missing_fields", missing_fields), ("warnings", dq_warnings), ("errors", dq_errors)):
        if not is_array_of_strings(value):
            add(invalid, "data_quality_arrays_are_strings", f"data_quality.{field_name} must be an array of strings")

    safe_missing_fields = missing_fields if isinstance(missing_fields, list) else []
    safe_errors = dq_errors if isinstance(dq_errors, list) else []

    if status == "ready" and safe_missing_fields:
        add(invalid, "ready_requires_no_missing_fields", "data_quality.status is ready but missing_fields is not empty")
    if status == "ready" and safe_errors:
        add(invalid, "ready_requires_no_errors", "data_quality.status is ready but errors is not empty")
    if safe_errors and status == "ready":
        add(invalid, "errors_prevent_ready", "data_quality.errors is not empty, so status cannot be ready")
    if safe_missing_fields and status == "ready":
        add(invalid, "missing_fields_prevent_ready", "data_quality.missing_fields is not empty, so status cannot be ready")

    for field_path in CORE_FIELDS:
        value = get_path(product, field_path)
        if is_empty(value) and field_path not in safe_missing_fields:
            add(invalid, "missing_core_fields_are_listed", f"core field '{field_path}' is empty/null but is not listed in data_quality.missing_fields")

    min_code = get_path(product, "unit_summary.minimum_sale_unit.code")
    max_code = get_path(product, "unit_summary.maximum_purchase_unit.code")
    if min_code and max_code and min_code == max_code:
        add(warnings, "same_min_max_unit", "unidad m?nima y m?xima iguales")

    if is_empty(get_path(product, "identity.reference.label")):
        add(warnings, "reference_label_empty", "identity.reference.label is empty")
    if is_empty(get_path(product, "identity.brand.name")):
        add(warnings, "brand_name_empty", "identity.brand.name is empty")
    if get_path(product, "commercial.prices") == []:
        add(warnings, "prices_empty_v1", "commercial.prices is empty; prices come from scraper later in v1")
    if get_path(product, "commercial.costs") == []:
        add(warnings, "costs_empty_v1", "commercial.costs is empty; costs come from scraper later in v1")
    if product.get("suppliers") == []:
        add(warnings, "suppliers_empty_v1", "suppliers is empty; suppliers come from scraper later in v1")

    return invalid, warnings


def print_rule_results(invalid: RuleMessages, warnings: RuleMessages, relative_path: str) -> None:
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

    for rule_name in rule_names:
        if rule_name in invalid:
            for message in invalid[rule_name]:
                print(f"INVALID_DATA_QUALITY_RULE: {rule_name} | {relative_path} | {message}")
        else:
            print(f"VALID_DATA_QUALITY_RULE: {rule_name}")

    for rule_name in warning_rule_names:
        if rule_name in warnings:
            for message in warnings[rule_name]:
                print(f"WARNING_DATA_QUALITY_RULE: {rule_name} | {relative_path} | {message}")
        else:
            print(f"VALID_DATA_QUALITY_RULE: {rule_name}")


def validate_file(path: Path) -> tuple[RuleMessages, RuleMessages]:
    products = as_list(load_json(path))
    all_invalid: RuleMessages = {}
    all_warnings: RuleMessages = {}
    for index, product in enumerate(products):
        invalid, warnings = validate_product_data_quality(product)
        for rule, messages in invalid.items():
            for message in messages:
                add(all_invalid, rule, f"product[{index}]: {message}")
        for rule, messages in warnings.items():
            for message in messages:
                add(all_warnings, rule, f"product[{index}]: {message}")
    return all_invalid, all_warnings


def validate_default() -> bool:
    invalid, warnings = validate_file(PRODUCT_CONTRACT)
    print_rule_results(invalid, warnings, PRODUCT_CONTRACT.relative_to(ROOT).as_posix())
    return not invalid


def validate_expected_failures() -> bool:
    has_unexpected_valid = False
    failure_files = sorted(DATA_QUALITY_FAILURES_DIR.glob("*.json"))
    if not failure_files:
        print(f"INVALID_DATA_QUALITY_RULE: data_quality_failure_examples_exist | {DATA_QUALITY_FAILURES_DIR.relative_to(ROOT).as_posix()} | no files found")
        return False

    for failure_path in failure_files:
        invalid, warnings = validate_file(failure_path)
        relative_path = failure_path.relative_to(ROOT).as_posix()
        if invalid:
            print(f"EXPECTED_INVALID_DATA_QUALITY: {relative_path}")
        elif warnings:
            print(f"EXPECTED_WARNING_DATA_QUALITY: {relative_path}")
        else:
            has_unexpected_valid = True
            print(f"UNEXPECTED_VALID_DATA_QUALITY: {relative_path}")
    return not has_unexpected_valid


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Envax PIM data_quality governance rules.")
    parser.add_argument("--include-failures", action="store_true", help="Also validate controlled data_quality failure examples and require them to fail or warn as expected.")
    return parser.parse_args()


def run_data_quality_validation(include_failures: bool = False) -> bool:
    default_ok = validate_default()
    failures_ok = True
    if include_failures:
        failures_ok = validate_expected_failures()
    return default_ok and failures_ok


def main() -> int:
    args = parse_args()
    return 0 if run_data_quality_validation(include_failures=args.include_failures) else 1


if __name__ == "__main__":
    sys.exit(main())
