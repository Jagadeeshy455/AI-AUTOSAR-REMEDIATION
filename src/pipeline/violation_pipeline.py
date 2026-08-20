from pathlib import Path

from src.parser.report_parser import (
    load_report,
    get_violations
)

from src.analyzer.violation import Violation
from src.analyzer.source_context import extract_context


REPORT_PATH = Path(
    "sample_project/analysis_reports/violations.json"
)

PROJECT_ROOT = Path(".")


def build_violations() -> list[Violation]:
    """Build validated violations with source-code context."""

    report = load_report(str(REPORT_PATH))

    raw_violations = get_violations(report)

    violations = []

    for item in raw_violations:

        source_file = (
            PROJECT_ROOT
            / "sample_project"
            / item["file"]
        )

        context = extract_context(
            source_file=source_file,
            target_line=item["line"],
            context_lines=5
        )

        violation = Violation(
            id=item["id"],
            rule=item["rule"],
            severity=item["severity"],
            language=item["language"],
            file=item["file"],
            line=item["line"],
            message=item["message"],
            source_context=context
        )

        violations.append(violation)

    return violations


if __name__ == "__main__":

    violations = build_violations()

    print(f"Total violations: {len(violations)}")

    for violation in violations:

        print("\n" + "=" * 70)

        print(f"ID       : {violation.id}")
        print(f"Rule     : {violation.rule}")
        print(f"Severity : {violation.severity}")
        print(f"Language : {violation.language}")
        print(f"File     : {violation.file}")
        print(f"Line     : {violation.line}")
        print(f"Message  : {violation.message}")

        print("\nSource Context:")
        print(violation.source_context)