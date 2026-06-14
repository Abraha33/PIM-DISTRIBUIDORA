from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PRODUCT_CONTRACT = ROOT / "contracts" / "products.v1.example.json"
NAMING_FAILURES_DIR = ROOT / "examples" / "naming_failures"

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


def add(messages: RuleMessages, rule_name: str, message: str) -> None:
    messages.setdefault(rule_name, []).append(message)


def component_present(name: str, components: list[str]) -> bool:
    return any(component and component in name for component in components)


def require_component(errors: RuleMessages, rule: str, field: str, name: str, component: str, label: str) -> None:
    if component and component not in name:
        add(errors, rule, f"names.{field} is missing {label}: '{component}'")


def require_material(errors: RuleMessages, rule: str, field: str, name: str, product: dict[str, Any]) -> None:
    material = product.get("attributes", {}).get("material", {})
    candidates = [material.get("abbreviation", ""), material.get("name", "")]
    if not component_present(name, candidates):
        add(errors, rule, f"names.{field} is missing material abbreviation/name: {candidates}")


def warn_optional(warnings: RuleMessages, rule: str, field: str, component: str, label: str) -> bool:
    if not component:
        add(warnings, rule, f"names.{field} cannot require {label} because source value is empty")
        return True
    return False


def active_unit_labels(product: dict[str, Any]) -> list[str]:
    return [
        unit.get("label", "")
        for unit in product.get("unit_presentation", [])
        if unit.get("is_active") is True and unit.get("label")
    ]


def required_base_components(product: dict[str, Any]) -> dict[str, str]:
    attributes = product.get("attributes", {})
    return {
        "category.final.name": product.get("category", {}).get("final", {}).get("name", ""),
        "color.name": attributes.get("color", {}).get("name", ""),
        "capacity.label": attributes.get("capacity", {}).get("label", ""),
        "dimensions.label": attributes.get("dimensions", {}).get("label", ""),
        "minimum_sale_unit.label": product.get("unit_summary", {}).get("minimum_sale_unit", {}).get("label", ""),
        "maximum_purchase_unit.label": product.get("unit_summary", {}).get("maximum_purchase_unit", {}).get("label", ""),
    }


def validate_required_base(errors: RuleMessages, rule: str, field: str, name: str, product: dict[str, Any]) -> None:
    for label, component in required_base_components(product).items():
        if label in {"capacity.label", "dimensions.label"} and not component:
            continue
        require_component(errors, rule, field, name, component, label)
    require_material(errors, rule, field, name, product)


def validate_forbidden(errors: RuleMessages, rule: str, field: str, name: str, product: dict[str, Any], forbidden: list[tuple[str, str]]) -> None:
    for label, component in forbidden:
        if component and component in name:
            add(errors, rule, f"names.{field} contains forbidden {label}: '{component}'")


def validate_unit_label_format(errors: RuleMessages, product: dict[str, Any]) -> None:
    names = product.get("names", {})
    units = product.get("unit_presentation", [])
    expected_labels = {unit.get("label") for unit in units if unit.get("label")}

    for field, name in names.items():
        if not isinstance(name, str):
            continue
        for unit in units:
            code = unit.get("code")
            factor = unit.get("factor")
            if code and factor is not None:
                malformed_pattern = rf"\b{re.escape(str(code))}x{re.escape(str(factor))}\b"
                if re.search(malformed_pattern, name):
                    add(errors, "unit_label_format_in_names", f"names.{field} contains malformed unit label for {code}: expected {code}({factor})")
        for token in re.findall(r"\b[A-Z]{2,}\([^)]*\)", name):
            if token not in expected_labels:
                add(errors, "unit_label_format_in_names", f"names.{field} contains unknown unit-like label '{token}'")


def validate_product_naming_rules(product: dict[str, Any]) -> tuple[RuleMessages, RuleMessages]:
    errors: RuleMessages = {}
    warnings: RuleMessages = {}
    names = product.get("names", {})
    identity = product.get("identity", {})
    reference_label = identity.get("reference", {}).get("label", "")
    brand_name = identity.get("brand", {}).get("name", "")
    code = product.get("code", "")

    pos = names.get("pos", "")
    validate_required_base(errors, "pos_name_components", "pos", pos, product)
    validate_forbidden(errors, "pos_name_forbidden_components", "pos", pos, product, [("reference", reference_label), ("brand", brand_name)])

    logistics = names.get("logistics", "")
    validate_required_base(errors, "logistics_name_components", "logistics", logistics, product)
    require_component(errors, "logistics_name_components", "logistics", logistics, code, "code")
    if not warn_optional(warnings, "logistics_name_optional_reference", "logistics", reference_label, "reference.label"):
        require_component(errors, "logistics_name_components", "logistics", logistics, reference_label, "reference.label")

    internal = names.get("internal", "")
    validate_required_base(errors, "internal_name_components", "internal", internal, product)
    require_component(errors, "internal_name_components", "internal", internal, code, "code")
    if not warn_optional(warnings, "internal_name_optional_reference", "internal", reference_label, "reference.label"):
        require_component(errors, "internal_name_components", "internal", internal, reference_label, "reference.label")

    ecommerce_short = names.get("ecommerce_short", "")
    validate_required_base(errors, "ecommerce_short_components", "ecommerce_short", ecommerce_short, product)
    validate_forbidden(errors, "ecommerce_short_forbidden_components", "ecommerce_short", ecommerce_short, product, [("reference", reference_label), ("brand", brand_name)])

    ecommerce_long = names.get("ecommerce_long", "")
    validate_required_base(errors, "ecommerce_long_components", "ecommerce_long", ecommerce_long, product)
    if not warn_optional(warnings, "ecommerce_long_optional_brand", "ecommerce_long", brand_name, "brand.name"):
        require_component(errors, "ecommerce_long_components", "ecommerce_long", ecommerce_long, brand_name, "brand.name")
    if not warn_optional(warnings, "ecommerce_long_optional_reference", "ecommerce_long", reference_label, "reference.label"):
        require_component(errors, "ecommerce_long_components", "ecommerce_long", ecommerce_long, reference_label, "reference.label")
    require_component(errors, "ecommerce_long_components", "ecommerce_long", ecommerce_long, "Presentaciones:", "word Presentaciones:")
    for label in active_unit_labels(product):
        require_component(errors, "ecommerce_long_components", "ecommerce_long", ecommerce_long, label, "active unit label")

    validate_unit_label_format(errors, product)
    return errors, warnings


def print_rule_results(errors: RuleMessages, warnings: RuleMessages, relative_path: str) -> None:
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
    for rule_name in rule_names:
        if rule_name in errors:
            for message in errors[rule_name]:
                print(f"INVALID_NAMING_RULE: {rule_name} | {relative_path} | {message}")
        else:
            print(f"VALID_NAMING_RULE: {rule_name}")
    for rule_name, messages in warnings.items():
        for message in messages:
            print(f"WARNING_NAMING_RULE: {rule_name} | {relative_path} | {message}")


def validate_file(path: Path) -> tuple[RuleMessages, RuleMessages]:
    products = as_list(load_json(path))
    all_errors: RuleMessages = {}
    all_warnings: RuleMessages = {}
    for index, product in enumerate(products):
        errors, warnings = validate_product_naming_rules(product)
        for rule, messages in errors.items():
            for message in messages:
                add(all_errors, rule, f"product[{index}]: {message}")
        for rule, messages in warnings.items():
            for message in messages:
                add(all_warnings, rule, f"product[{index}]: {message}")
    return all_errors, all_warnings


def validate_default() -> bool:
    errors, warnings = validate_file(PRODUCT_CONTRACT)
    print_rule_results(errors, warnings, PRODUCT_CONTRACT.relative_to(ROOT).as_posix())
    return not errors


def validate_expected_failures() -> bool:
    has_unexpected_valid = False
    failure_files = sorted(NAMING_FAILURES_DIR.glob("*.json"))
    if not failure_files:
        print(f"INVALID_NAMING_RULE: naming_failure_examples_exist | {NAMING_FAILURES_DIR.relative_to(ROOT).as_posix()} | no files found")
        return False
    for failure_path in failure_files:
        errors, warnings = validate_file(failure_path)
        relative_path = failure_path.relative_to(ROOT).as_posix()
        if errors:
            print(f"EXPECTED_INVALID_NAMING: {relative_path}")
        elif warnings:
            print(f"EXPECTED_WARNING_NAMING: {relative_path}")
        else:
            has_unexpected_valid = True
            print(f"UNEXPECTED_VALID_NAMING: {relative_path}")
    return not has_unexpected_valid


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Envax PIM product naming rules.")
    parser.add_argument("--include-failures", action="store_true", help="Also validate controlled naming failure examples and require them to fail.")
    return parser.parse_args()


def run_naming_validation(include_failures: bool = False) -> bool:
    default_ok = validate_default()
    failures_ok = True
    if include_failures:
        failures_ok = validate_expected_failures()
    return default_ok and failures_ok


def main() -> int:
    args = parse_args()
    return 0 if run_naming_validation(include_failures=args.include_failures) else 1


if __name__ == "__main__":
    sys.exit(main())
