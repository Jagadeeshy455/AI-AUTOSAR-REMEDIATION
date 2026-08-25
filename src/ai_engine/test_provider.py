from src.ai_engine.mock_provider import MockAIProvider
from src.ai_engine.remediation import (
    create_remediation_request,
)
from src.ai_engine.remediation_engine import (
    RemediationEngine,
)
from src.pipeline.violation_pipeline import build_violations


def main():

    violations = build_violations()

    provider = MockAIProvider()

    engine = RemediationEngine(provider)

    print(f"Violations loaded: {len(violations)}")

    for violation in violations:

        request = create_remediation_request(
            violation
        )

        response = engine.generate(request)

        print("\n" + "=" * 70)

        print(f"Violation ID : {response.violation_id}")
        print(f"Rule         : {request.rule}")
        print(f"File         : {request.file}")
        print(f"Line         : {request.line}")

        print("\nOriginal Code:")
        print(response.original_code)

        print("\nProposed Code:")
        print(
            response.proposed_code
            if response.proposed_code
            else "<No proposal>"
        )

        print("\nAnalysis:")
        print(response.analysis)

        print("\nExplanation:")
        print(response.explanation)

        print(
            f"\nConfidence   : {response.confidence}"
        )

        print(
            "Human Review : "
            f"{response.requires_human_review}"
        )

        print(
            f"Decision     : {response.decision}"
        )


if __name__ == "__main__":
    main()