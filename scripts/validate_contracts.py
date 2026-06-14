from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from validate_dictionaries import run_dictionary_validation
from validate_uniqueness import run_uniqueness_validation
from validate_naming import run_naming_validation
from validate_families import run_family_validation
from validate_data_quality import run_data_quality_validation
from validate_documentation_coverage import run_documentation_coverage_validation

ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    (
        ROOT / "contracts" / "products.v1.example.json",
        ROOT / "schemas" / "products.v1.schema.json",
    ),
    (
        ROOT / "contracts" / "product_families.v1.example.json",
        ROOT / "schemas" / "product_families.v1.schema.json",
    ),
    (
        ROOT / "contracts" / "barcode_history.v1.example.json",
        ROOT / "schemas" / "barcode_history.v1.schema.json",
    ),
]

FAILURE_EXAMPLES_DIR = ROOT / "examples" / "validation_failures"

FAILURE_SCHEMA_BY_PREFIX = {
    "product_": ROOT / "schemas" / "products.v1.schema.json",
    "family_": ROOT / "schemas" / "product_families.v1.schema.json",
    "barcode_history_": ROOT / "schemas" / "barcode_history.v1.schema.json",
}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_validation_errors(contract_path: Path, schema_path: Path):
    contract = load_json(contract_path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return sorted(validator.iter_errors(contract), key=lambda error: list(error.path))


def schema_for_failure_example(path: Path) -> Path:
    file_name = path.name
    for prefix, schema_path in FAILURE_SCHEMA_BY_PREFIX.items():
        if file_name.startswith(prefix):
            return schema_path
    raise ValueError(f"No schema mapping found for failure example: {path}")


def validate_valid_contracts() -> bool:
    has_errors = False

    for contract_path, schema_path in VALIDATION_TARGETS:
        relative_contract = contract_path.relative_to(ROOT).as_posix()

        try:
            errors = get_validation_errors(contract_path, schema_path)

            if errors:
                has_errors = True
                for error in errors:
                    path = ".".join(str(part) for part in error.absolute_path) or "<root>"
                    print(f"INVALID: {relative_contract} | {path}: {error.message}")
            else:
                print(f"VALID: {relative_contract}")
        except Exception as exc:  # noqa: BLE001 - command line validator must report any failure clearly
            has_errors = True
            print(f"INVALID: {relative_contract} | {exc}")

    return not has_errors


def validate_expected_failures() -> bool:
    has_unexpected_valid = False

    failure_files = sorted(FAILURE_EXAMPLES_DIR.glob("*.json"))
    if not failure_files:
        print(f"INVALID: {FAILURE_EXAMPLES_DIR.relative_to(ROOT).as_posix()} | no failure examples found")
        return False

    for failure_path in failure_files:
        relative_failure = failure_path.relative_to(ROOT).as_posix()

        try:
            schema_path = schema_for_failure_example(failure_path)
            errors = get_validation_errors(failure_path, schema_path)
            if errors:
                print(f"EXPECTED_INVALID: {relative_failure}")
            else:
                has_unexpected_valid = True
                print(f"UNEXPECTED_VALID: {relative_failure}")
        except Exception as exc:  # noqa: BLE001 - command line validator must report any failure clearly
            has_unexpected_valid = True
            print(f"UNEXPECTED_VALID: {relative_failure} | validator error: {exc}")

    return not has_unexpected_valid


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Envax PIM contract examples.")
    parser.add_argument(
        "--include-failures",
        action="store_true",
        help="Also validate controlled invalid examples and require them to fail.",
    )
    parser.add_argument(
        "--include-dictionaries",
        action="store_true",
        help="Also validate controlled dictionary consistency rules.",
    )
    parser.add_argument(
        "--include-uniqueness",
        action="store_true",
        help="Also validate uniqueness and barcode consistency rules.",
    )
    parser.add_argument(
        "--include-naming",
        action="store_true",
        help="Also validate product naming rules.",
    )
    parser.add_argument(
        "--include-families",
        action="store_true",
        help="Also validate product family and variant relationship rules.",
    )
    parser.add_argument(
        "--include-data-quality",
        action="store_true",
        help="Also validate product data_quality governance rules.",
    )
    parser.add_argument(
        "--include-docs",
        action="store_true",
        help="Also validate documentation coverage for validators.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    valid_contracts_ok = validate_valid_contracts()
    expected_failures_ok = True
    dictionary_validation_ok = True
    uniqueness_validation_ok = True
    naming_validation_ok = True
    family_validation_ok = True
    data_quality_validation_ok = True
    documentation_coverage_ok = True

    if args.include_failures:
        expected_failures_ok = validate_expected_failures()

    if args.include_dictionaries:
        dictionary_validation_ok = run_dictionary_validation(include_failures=args.include_failures)

    if args.include_uniqueness:
        uniqueness_validation_ok = run_uniqueness_validation(include_failures=args.include_failures)

    if args.include_naming:
        naming_validation_ok = run_naming_validation(include_failures=args.include_failures)

    if args.include_families:
        family_validation_ok = run_family_validation(include_failures=args.include_failures)

    if args.include_data_quality:
        data_quality_validation_ok = run_data_quality_validation(include_failures=args.include_failures)

    if args.include_docs:
        documentation_coverage_ok = run_documentation_coverage_validation()

    return 0 if valid_contracts_ok and expected_failures_ok and dictionary_validation_ok and uniqueness_validation_ok and naming_validation_ok and family_validation_ok and data_quality_validation_ok and documentation_coverage_ok else 1


if __name__ == "__main__":
    sys.exit(main())
