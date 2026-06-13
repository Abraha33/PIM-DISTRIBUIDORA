from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PRODUCT_CONTRACT = ROOT / "contracts" / "products.v1.example.json"
DICTIONARY_FAILURES_DIR = ROOT / "examples" / "dictionary_failures"
UNIT_DICTIONARY = ROOT / "dictionaries" / "unit_dictionary.json"
MATERIAL_DICTIONARY = ROOT / "dictionaries" / "material_dictionary.json"
COLOR_DICTIONARY = ROOT / "dictionaries" / "color_dictionary.json"

RuleErrors = dict[str, list[str]]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def normalize_factor(value: int | float) -> str:
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def load_dictionaries() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    units = {item["code"]: item for item in load_json(UNIT_DICTIONARY)}
    materials = {item["id"]: item for item in load_json(MATERIAL_DICTIONARY)}
    colors = {item["id"]: item for item in load_json(COLOR_DICTIONARY)}
    return units, materials, colors


def add_error(errors: RuleErrors, rule_name: str, message: str) -> None:
    errors.setdefault(rule_name, []).append(message)


def validate_product_dictionary_rules(product: dict[str, Any]) -> RuleErrors:
    units, materials, colors = load_dictionaries()
    errors: RuleErrors = {}

    material = product.get("attributes", {}).get("material", {})
    material_id = material.get("id")
    if material_id not in materials:
        add_error(
            errors,
            "material_id_exists",
            f"attributes.material.id '{material_id}' does not exist in dictionaries/material_dictionary.json",
        )
    elif material.get("abbreviation") != materials[material_id].get("abbreviation"):
        add_error(
            errors,
            "material_abbreviation_matches_dictionary",
            (
                f"attributes.material.abbreviation '{material.get('abbreviation')}' does not match "
                f"dictionary abbreviation '{materials[material_id].get('abbreviation')}' for id '{material_id}'"
            ),
        )

    color = product.get("attributes", {}).get("color", {})
    color_id = color.get("id")
    if color_id not in colors:
        add_error(
            errors,
            "color_id_exists",
            f"attributes.color.id '{color_id}' does not exist in dictionaries/color_dictionary.json",
        )
    elif color.get("name") != colors[color_id].get("name"):
        add_error(
            errors,
            "color_name_matches_dictionary",
            (
                f"attributes.color.name '{color.get('name')}' does not match "
                f"dictionary name '{colors[color_id].get('name')}' for id '{color_id}'"
            ),
        )

    unit_presentation = product.get("unit_presentation", [])
    product_unit_codes = set()
    for index, unit in enumerate(unit_presentation):
        code = unit.get("code")
        factor = unit.get("factor")
        label = unit.get("label")
        product_unit_codes.add(code)

        if code not in units:
            add_error(
                errors,
                "unit_presentation_codes_exist",
                f"unit_presentation[{index}].code '{code}' does not exist in dictionaries/unit_dictionary.json",
            )

        expected_label = f"{code}({normalize_factor(factor)})"
        if label != expected_label:
            add_error(
                errors,
                "unit_presentation_labels_match_code_factor",
                f"unit_presentation[{index}].label '{label}' should be '{expected_label}'",
            )

    unit_summary = product.get("unit_summary", {})
    for summary_name in ("minimum_sale_unit", "maximum_purchase_unit"):
        summary_unit = unit_summary.get(summary_name, {})
        summary_code = summary_unit.get("code")

        if summary_code not in units:
            add_error(
                errors,
                "unit_summary_codes_exist",
                f"unit_summary.{summary_name}.code '{summary_code}' does not exist in dictionaries/unit_dictionary.json",
            )

        if summary_code not in product_unit_codes:
            add_error(
                errors,
                "unit_summary_codes_in_unit_presentation",
                f"unit_summary.{summary_name}.code '{summary_code}' is not present in product unit_presentation[].code",
            )

    return errors


def print_rule_results(errors: RuleErrors, relative_path: str) -> None:
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

    for rule_name in rule_names:
        if rule_name in errors:
            for error in errors[rule_name]:
                print(f"INVALID_DICTIONARY_RULE: {rule_name} | {relative_path} | {error}")
        else:
            print(f"VALID_DICTIONARY_RULE: {rule_name}")


def validate_default_product() -> bool:
    product = load_json(PRODUCT_CONTRACT)
    errors = validate_product_dictionary_rules(product)
    print_rule_results(errors, PRODUCT_CONTRACT.relative_to(ROOT).as_posix())
    return not errors


def validate_expected_failures() -> bool:
    has_unexpected_valid = False
    failure_files = sorted(DICTIONARY_FAILURES_DIR.glob("*.json"))

    if not failure_files:
        print(f"INVALID_DICTIONARY_RULE: dictionary_failure_examples_exist | {DICTIONARY_FAILURES_DIR.relative_to(ROOT).as_posix()} | no files found")
        return False

    for failure_path in failure_files:
        product = load_json(failure_path)
        errors = validate_product_dictionary_rules(product)
        relative_path = failure_path.relative_to(ROOT).as_posix()

        if errors:
            print(f"EXPECTED_INVALID_DICTIONARY: {relative_path}")
        else:
            has_unexpected_valid = True
            print(f"UNEXPECTED_VALID_DICTIONARY: {relative_path}")

    return not has_unexpected_valid


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Envax PIM dictionary consistency rules.")
    parser.add_argument(
        "--include-failures",
        action="store_true",
        help="Also validate controlled dictionary failure examples and require them to fail.",
    )
    return parser.parse_args()


def run_dictionary_validation(include_failures: bool = False) -> bool:
    valid_product_ok = validate_default_product()
    expected_failures_ok = True

    if include_failures:
        expected_failures_ok = validate_expected_failures()

    return valid_product_ok and expected_failures_ok


def main() -> int:
    args = parse_args()
    return 0 if run_dictionary_validation(include_failures=args.include_failures) else 1


if __name__ == "__main__":
    sys.exit(main())
