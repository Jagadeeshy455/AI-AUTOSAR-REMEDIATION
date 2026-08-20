import json
from pathlib import Path


def load_report(report_path: str) -> dict:
    """Load a static-analysis JSON report."""

    path = Path(report_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Report not found: {report_path}"
        )

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_violations(report: dict) -> list[dict]:
    """Return violations from the analysis report."""

    return report.get("violations", [])


if __name__ == "__main__":
    report = load_report(
        "sample_project/analysis_reports/violations.json"
    )

    violations = get_violations(report)

    print(f"Total violations: {len(violations)}")

    for violation in violations:
        print(
            f"{violation['id']} | "
            f"{violation['rule']} | "
            f"{violation['file']} | "
            f"Line {violation['line']}"
        )