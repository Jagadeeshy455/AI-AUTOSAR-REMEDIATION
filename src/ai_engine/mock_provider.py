from src.ai_engine.provider import AIProvider
from src.ai_engine.remediation import (
    RemediationRequest,
    RemediationResponse,
)
from src.ai_engine.mock_reasoner import MockReasoner


class MockAIProvider(AIProvider):
    """
    Simulates an external AI remediation provider.

    No API key is required.
    """

    def __init__(self):
        self.reasoner = MockReasoner()

    def generate_remediation(
        self,
        request: RemediationRequest,
        guidance=None,
    ) -> RemediationResponse:

        result = self.reasoner.generate(
            request=request,
            guidance=guidance,
        )

        if guidance is not None:
            explanation = (
                "The mock AI reasoner generated a candidate "
                "remediation using the supplied rule guidance. "
                "The proposal must be validated before acceptance."
            )
        else:
            explanation = (
                "No rule guidance was available. "
                "Human review is required."
            )

        return RemediationResponse(
            violation_id=request.violation_id,
            analysis=result["analysis"],
            original_code=request.target_code,
            proposed_code=result["proposed_code"],
            explanation=explanation,
            confidence=result["confidence"],
            requires_human_review=True,
            decision=result["decision"],
        )