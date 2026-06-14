from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PRODUCTS = ROOT / "contracts" / "products.v1.example.json"
DEFAULT_FAMILIES = ROOT / "contracts" / "product_families.v1.example.json"
FAMILY_FAILURES_DIR = ROOT / "examples" / "family_failures"

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
        return as_list(load_json(DEFAULT_PRODUCTS)), as_list(load_json(DEFAULT_FAMILIES))

    data = load_json(path)
    if isinstance(data, dict) and ("products" in data or "product_families" in data):
        return as_list(data.get("products", [])), as_list(data.get("product_families", []))

    raise ValueError(f"Family validation scenario must include products and product_families: {path}")


def add(messages: RuleMessages, rule_name: str, message: str) -> None:
    messages.setdefault(rule_name, []).append(message)


def validate_family_rules(products: list[dict[str, Any]], families: list[dict[str, Any]]) -> tuple[RuleMessages, RuleMessages]:
    invalid: RuleMessages = {}
    warnings: RuleMessages = {}

    product_by_code = {product.get("code"): product for product in products}
    family_by_id = {family.get("family_id"): family for family in families}

    for product in products:
        code = product.get("code")
        family_id = product.get("family_id")
        if family_id is not None and family_id not in family_by_id:
            add(invalid, "family_id_consistency", f"product '{code}' references unknown family_id '{family_id}'")

    child_membership: dict[str, list[str]] = {}
    for family in families:
        family_id = family.get("family_id")
        parent_code = family.get("parent_code")
        children_codes = family.get("children_codes", [])

        for child_code in children_codes:
            child_membership.setdefault(child_code, []).append(family_id)
            if child_code not in product_by_code:
                add(invalid, "children_codes_consistency", f"family '{family_id}' child code '{child_code}' does not exist in products")

        if parent_code:
            if parent_code not in product_by_code:
                add(warnings, "parent_code_consistency", f"family '{family_id}' parent_code '{parent_code}' does not exist in products; family may be conceptual")

    for child_code, family_ids in child_membership.items():
        if len(family_ids) > 1:
            add(invalid, "duplicate_child_membership", f"product '{child_code}' appears as child in multiple families: {', '.join(family_ids)}")

    for family in families:
        family_id = family.get("family_id")
        for child_code in family.get("children_codes", []):
            product = product_by_code.get(child_code)
            if not product:
                continue
            if product.get("family_id") != family_id:
                add(
                    invalid,
                    "product_family_membership",
                    f"product '{child_code}' appears in family '{family_id}' but product.family_id is '{product.get('family_id')}'",
                )

    for family in families:
        family_id = family.get("family_id")
        variant_axis = family.get("variant_axis", [])
        for child_code in family.get("children_codes", []):
            product = product_by_code.get(child_code)
            if not product:
                continue
            for axis in variant_axis:
                if axis == "color":
                    color_name = product.get("attributes", {}).get("color", {}).get("name")
                    if not color_name:
                        add(warnings, "variant_axis_consistency", f"family '{family_id}' variant_axis includes color but child '{child_code}' has empty attributes.color.name")

    for product in products:
        code = product.get("code")
        is_family_parent = product.get("is_family_parent") is True
        family_id = product.get("family_id")
        is_sellable = product.get("is_sellable")

        if is_family_parent:
            if family_id is None:
                add(invalid, "family_parent_product", f"product '{code}' has is_family_parent=true but family_id is null")
            matching_family = family_by_id.get(family_id)
            if matching_family and matching_family.get("parent_code") and matching_family.get("parent_code") != code:
                add(warnings, "family_parent_product", f"product '{code}' is family parent but does not match family.parent_code '{matching_family.get('parent_code')}'")

        if is_sellable is False and not is_family_parent:
            add(warnings, "product_sellability", f"product '{code}' is not sellable and is not marked as family parent; it may be incomplete")

    return invalid, warnings


def print_rule_results(invalid: RuleMessages, warnings: RuleMessages, relative_path: str) -> None:
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

    for rule_name in rule_names:
        if rule_name in invalid:
            for message in invalid[rule_name]:
                print(f"INVALID_FAMILY_RULE: {rule_name} | {relative_path} | {message}")
        else:
            print(f"VALID_FAMILY_RULE: {rule_name}")

    for rule_name in warning_rule_names:
        if rule_name in warnings:
            for message in warnings[rule_name]:
                print(f"WARNING_FAMILY_RULE: {rule_name} | {relative_path} | {message}")
        else:
            print(f"VALID_FAMILY_RULE: {rule_name}")


def validate_default() -> bool:
    products, families = load_scenario()
    invalid, warnings = validate_family_rules(products, families)
    print_rule_results(invalid, warnings, "contracts/products.v1.example.json + contracts/product_families.v1.example.json")
    return not invalid


def validate_expected_failures() -> bool:
    has_unexpected_valid = False
    failure_files = sorted(FAMILY_FAILURES_DIR.glob("*.json"))

    if not failure_files:
        print(f"INVALID_FAMILY_RULE: family_failure_examples_exist | {FAMILY_FAILURES_DIR.relative_to(ROOT).as_posix()} | no files found")
        return False

    for failure_path in failure_files:
        products, families = load_scenario(failure_path)
        invalid, warnings = validate_family_rules(products, families)
        relative_path = failure_path.relative_to(ROOT).as_posix()

        if invalid:
            print(f"EXPECTED_INVALID_FAMILY: {relative_path}")
        elif warnings:
            print(f"EXPECTED_WARNING_FAMILY: {relative_path}")
        else:
            has_unexpected_valid = True
            print(f"UNEXPECTED_VALID_FAMILY: {relative_path}")

    return not has_unexpected_valid


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Envax PIM product family and variant relationships.")
    parser.add_argument("--include-failures", action="store_true", help="Also validate controlled family failure examples and require them to fail or warn as expected.")
    return parser.parse_args()


def run_family_validation(include_failures: bool = False) -> bool:
    default_ok = validate_default()
    failures_ok = True
    if include_failures:
        failures_ok = validate_expected_failures()
    return default_ok and failures_ok


def main() -> int:
    args = parse_args()
    return 0 if run_family_validation(include_failures=args.include_failures) else 1


if __name__ == "__main__":
    sys.exit(main())
