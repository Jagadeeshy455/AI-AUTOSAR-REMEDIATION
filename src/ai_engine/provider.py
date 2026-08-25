from abc import ABC, abstractmethod

from src.ai_engine.remediation import (
    RemediationRequest,
    RemediationResponse,
)


class AIProvider(ABC):

    @abstractmethod
    def generate_remediation(
        self,
        request: RemediationRequest,
        guidance=None,
    ) -> RemediationResponse:
        """Generate a remediation proposal."""
        raise NotImplementedError