from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PRODUCTS = ROOT / "contracts" / "products.v1.example.json"
DEFAULT_BARCODE_HISTORY = ROOT / "contracts" / "barcode_history.v1.example.json"
UNIQUENESS_FAILURES_DIR = ROOT / "examples" / "uniqueness_failures"

RuleMessages = dict[str, list[str]]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def load_scenario(path: Path | None = None) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if path is None:
        return as_list(load_json(DEFAULT_PRODUCTS)), as_list(load_json(DEFAULT_BARCODE_HISTORY))

    data = load_json(path)
    if isinstance(data, dict) and ("products" in data or "barcode_history" in data):
        return as_list(data.get("products", [])), as_list(data.get("barcode_history", []))

    if isinstance(data, list):
        return data, []

    return [data], []


def add(messages: RuleMessages, rule_name: str, message: str) -> None:
    messages.setdefault(rule_name, []).append(message)


def iter_barcodes(products: list[dict[str, Any]]):
    for product in products:
        product_code = product.get("code")
        for unit in product.get("unit_presentation", []):
            unit_code = unit.get("code")
            for barcode in unit.get("barcodes", []):
                yield product_code, unit_code, barcode


def find_product(products: list[dict[str, Any]], product_code: str) -> dict[str, Any] | None:
    for product in products:
        if product.get("code") == product_code:
            return product
    return None


def find_unit(product: dict[str, Any], unit_code: str) -> dict[str, Any] | None:
    for unit in product.get("unit_presentation", []):
        if unit.get("code") == unit_code:
            return unit
    return None


def find_barcode_in_unit(unit: dict[str, Any], barcode_value: str) -> dict[str, Any] | None:
    for barcode in unit.get("barcodes", []):
        if barcode.get("value") == barcode_value:
            return barcode
    return None


def barcode_exists_anywhere_with_status(products: list[dict[str, Any]], barcode_value: str, statuses: set[str]) -> bool:
    for _, _, barcode in iter_barcodes(products):
        if barcode.get("value") == barcode_value and barcode.get("status") in statuses:
            return True
    return False


def validate_uniqueness_rules(products: list[dict[str, Any]], barcode_history: list[dict[str, Any]]) -> tuple[RuleMessages, RuleMessages]:
    invalid: RuleMessages = {}
    warnings: RuleMessages = {}

    codes_seen: dict[str, int] = {}
    for index, product in enumerate(products):
        code = product.get("code")
        if code in codes_seen:
            add(invalid, "product_code_uniqueness", f"product[{index}].code '{code}' duplicates product[{codes_seen[code]}].code")
        else:
            codes_seen[code] = index

    active_barcodes: dict[str, tuple[str, str]] = {}
    for product_code, unit_code, barcode in iter_barcodes(products):
        value = barcode.get("value")
        if barcode.get("status") != "active":
            continue
        current_location = (product_code, unit_code)
        if value in active_barcodes:
            previous_product, previous_unit = active_barcodes[value]
            add(
                invalid,
                "active_barcode_uniqueness",
                f"active barcode '{value}' appears in {previous_product}/{previous_unit} and {product_code}/{unit_code}",
            )
        else:
            active_barcodes[value] = current_location

    for product in products:
        product_code = product.get("code")
        for unit in product.get("unit_presentation", []):
            unit_code = unit.get("code")
            active_primary = [
                barcode.get("value")
                for barcode in unit.get("barcodes", [])
                if barcode.get("status") == "active" and barcode.get("is_primary") is True
            ]
            if len(active_primary) > 1:
                add(
                    invalid,
                    "primary_barcode_per_unit",
                    f"{product_code}/{unit_code} has multiple active primary barcodes: {', '.join(active_primary)}",
                )

    for index, history in enumerate(barcode_history):
        product_code = history.get("product_code")
        unit_code = history.get("unit_code")
        barcode_value = history.get("barcode")
        action = history.get("action")

        product = find_product(products, product_code)
        if product is None:
            add(invalid, "barcode_history_references_existing_product_unit", f"barcode_history[{index}].product_code '{product_code}' does not exist")
            continue

        unit = find_unit(product, unit_code)
        if unit is None:
            add(invalid, "barcode_history_references_existing_product_unit", f"barcode_history[{index}].unit_code '{unit_code}' does not exist in product '{product_code}'")
            continue

        barcode = find_barcode_in_unit(unit, barcode_value)

        if action == "deactivated":
            if barcode is None:
                add(invalid, "barcode_history_action_consistency", f"deactivated barcode '{barcode_value}' does not exist in {product_code}/{unit_code}")
            elif barcode.get("status") not in {"inactive", "deprecated"}:
                add(invalid, "barcode_history_action_consistency", f"deactivated barcode '{barcode_value}' current status is '{barcode.get('status')}', expected inactive or deprecated")
        elif action == "activated":
            if barcode is None:
                add(invalid, "barcode_history_action_consistency", f"activated barcode '{barcode_value}' does not exist in {product_code}/{unit_code}")
            elif barcode.get("status") != "active":
                add(invalid, "barcode_history_action_consistency", f"activated barcode '{barcode_value}' current status is '{barcode.get('status')}', expected active")
        elif action == "created":
            if barcode is None:
                add(invalid, "barcode_history_action_consistency", f"created barcode '{barcode_value}' does not exist in {product_code}/{unit_code}")
        elif action == "recycled":
            if not barcode_exists_anywhere_with_status(products, barcode_value, {"inactive", "deprecated"}):
                add(warnings, "barcode_history_recycled_warning", f"recycled barcode '{barcode_value}' has no inactive/deprecated prior record in product barcodes")

    return invalid, warnings


def print_rule_results(invalid: RuleMessages, warnings: RuleMessages, relative_path: str) -> None:
    rule_names = [
        "product_code_uniqueness",
        "active_barcode_uniqueness",
        "primary_barcode_per_unit",
        "barcode_history_references_existing_product_unit",
        "barcode_history_action_consistency",
    ]

    for rule_name in rule_names:
        if rule_name in invalid:
            for error in invalid[rule_name]:
                print(f"INVALID_UNIQUENESS_RULE: {rule_name} | {relative_path} | {error}")
        else:
            print(f"VALID_UNIQUENESS_RULE: {rule_name}")

    for rule_name, messages in warnings.items():
        for warning in messages:
            print(f"WARNING_UNIQUENESS_RULE: {rule_name} | {relative_path} | {warning}")


def validate_default() -> bool:
    products, barcode_history = load_scenario()
    invalid, warnings = validate_uniqueness_rules(products, barcode_history)
    print_rule_results(invalid, warnings, "contracts/products.v1.example.json + contracts/barcode_history.v1.example.json")
    return not invalid


def validate_expected_failures() -> bool:
    has_unexpected_valid = False
    failure_files = sorted(UNIQUENESS_FAILURES_DIR.glob("*.json"))

    if not failure_files:
        print(f"INVALID_UNIQUENESS_RULE: uniqueness_failure_examples_exist | {UNIQUENESS_FAILURES_DIR.relative_to(ROOT).as_posix()} | no files found")
        return False

    for failure_path in failure_files:
        products, barcode_history = load_scenario(failure_path)
        invalid, warnings = validate_uniqueness_rules(products, barcode_history)
        relative_path = failure_path.relative_to(ROOT).as_posix()

        if invalid:
            print(f"EXPECTED_INVALID_UNIQUENESS: {relative_path}")
        elif warnings:
            print(f"EXPECTED_WARNING_UNIQUENESS: {relative_path}")
        else:
            has_unexpected_valid = True
            print(f"UNEXPECTED_VALID_UNIQUENESS: {relative_path}")

    return not has_unexpected_valid


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Envax PIM uniqueness and barcode consistency rules.")
    parser.add_argument(
        "--include-failures",
        action="store_true",
        help="Also validate controlled uniqueness failure examples and require them to fail or warn as expected.",
    )
    return parser.parse_args()


def run_uniqueness_validation(include_failures: bool = False) -> bool:
    default_ok = validate_default()
    failures_ok = True
    if include_failures:
        failures_ok = validate_expected_failures()
    return default_ok and failures_ok


def main() -> int:
    args = parse_args()
    return 0 if run_uniqueness_validation(include_failures=args.include_failures) else 1


if __name__ == "__main__":
    sys.exit(main())
