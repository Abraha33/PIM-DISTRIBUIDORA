from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

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


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    has_errors = False

    for contract_path, schema_path in VALIDATION_TARGETS:
        relative_contract = contract_path.relative_to(ROOT).as_posix()

        try:
            contract = load_json(contract_path)
            schema = load_json(schema_path)
            validator = Draft202012Validator(schema, format_checker=FormatChecker())
            errors = sorted(validator.iter_errors(contract), key=lambda error: list(error.path))

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

    return 1 if has_errors else 0


if __name__ == "__main__":
    sys.exit(main())
