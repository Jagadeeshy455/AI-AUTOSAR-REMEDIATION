from src.ai_engine.remediation import (
    RemediationRequest,
    RemediationResponse,
)
from src.ai_engine.rule_knowledge import (
    get_rule_guidance,
)


class RemediationEngine:
    """
    Generic remediation orchestration layer.

    Rule knowledge provides guidance, while the provider
    generates the remediation proposal.
    """

    def __init__(self, provider):
        self.provider = provider

    def generate(
        self,
        request: RemediationRequest,
    ) -> RemediationResponse:

        guidance = get_rule_guidance(request.rule)

        return self.provider.generate_remediation(
            request=request,
            guidance=guidance,
        )