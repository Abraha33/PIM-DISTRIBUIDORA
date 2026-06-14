from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

RuleMessages = dict[str, list[str]]

SCRIPT_DOC_COVERAGE = [
    ("validate_contracts.py", [ROOT / "docs" / "schema_contracts_v1.md", README]),
    ("validate_dictionaries.py", [ROOT / "docs" / "dictionary_validation_v1.md"]),
    ("validate_uniqueness.py", [ROOT / "docs" / "uniqueness_validation_v1.md"]),
    ("validate_naming.py", [ROOT / "docs" / "naming_validation_v1.md"]),
    ("validate_families.py", [ROOT / "docs" / "family_validation_v1.md"]),
    ("validate_data_quality.py", [ROOT / "docs" / "data_quality_validation_v1.md"]),
    ("generate_validation_report.py", [ROOT / "docs" / "validation_report_v1.md"]),
]

README_COMMANDS = [
    "python scripts/validate_contracts.py",
    "python scripts/validate_dictionaries.py",
    "python scripts/validate_uniqueness.py",
    "python scripts/validate_naming.py",
    "python scripts/validate_families.py",
    "python scripts/validate_data_quality.py",
    "python scripts/generate_validation_report.py",
]


def add(messages: RuleMessages, rule_name: str, message: str) -> None:
    messages.setdefault(rule_name, []).append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def validate_documentation_coverage() -> tuple[RuleMessages, RuleMessages]:
    invalid: RuleMessages = {}
    warnings: RuleMessages = {}

    for script_name, doc_paths in SCRIPT_DOC_COVERAGE:
        script_path = ROOT / "scripts" / script_name
        if not script_path.exists():
            add(invalid, "script_exists", f"scripts/{script_name} does not exist")
            continue

        existing_docs = [path for path in doc_paths if path.exists()]
        if not existing_docs:
            expected = ", ".join(path.relative_to(ROOT).as_posix() for path in doc_paths)
            add(invalid, "script_has_documentation", f"scripts/{script_name} has no expected documentation file. Expected one of: {expected}")
            continue

        mentions_script = any(script_name in read_text(path) for path in existing_docs)
        if not mentions_script:
            docs = ", ".join(path.relative_to(ROOT).as_posix() for path in existing_docs)
            add(invalid, "documentation_mentions_script", f"documentation for scripts/{script_name} does not mention script name. Checked: {docs}")

    readme_text = read_text(README)
    if not README.exists():
        add(invalid, "readme_exists", "README.md does not exist")
    else:
        for command in README_COMMANDS:
            if command not in readme_text:
                add(invalid, "readme_mentions_validation_commands", f"README.md does not mention command: {command}")

    docs_dir = ROOT / "docs"
    if not docs_dir.exists():
        add(warnings, "docs_directory_exists", "docs/ directory does not exist")

    return invalid, warnings


def print_rule_results(invalid: RuleMessages, warnings: RuleMessages) -> None:
    rule_names = [
        "script_exists",
        "script_has_documentation",
        "documentation_mentions_script",
        "readme_exists",
        "readme_mentions_validation_commands",
    ]
    warning_rule_names = ["docs_directory_exists"]

    for rule_name in rule_names:
        if rule_name in invalid:
            for message in invalid[rule_name]:
                print(f"INVALID_DOC_COVERAGE_RULE: {rule_name} | {message}")
        else:
            print(f"VALID_DOC_COVERAGE_RULE: {rule_name}")

    for rule_name in warning_rule_names:
        if rule_name in warnings:
            for message in warnings[rule_name]:
                print(f"WARNING_DOC_COVERAGE_RULE: {rule_name} | {message}")
        else:
            print(f"VALID_DOC_COVERAGE_RULE: {rule_name}")


def run_documentation_coverage_validation() -> bool:
    invalid, warnings = validate_documentation_coverage()
    print_rule_results(invalid, warnings)
    return not invalid


def parse_args() -> argparse.Namespace:
    return argparse.ArgumentParser(description="Validate Envax PIM validation documentation coverage.").parse_args()


def main() -> int:
    parse_args()
    return 0 if run_documentation_coverage_validation() else 1


if __name__ == "__main__":
    sys.exit(main())
