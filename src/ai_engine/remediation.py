from pathlib import Path

from pydantic import BaseModel, Field

from src.analyzer.violation import Violation
from src.analyzer.source_context import extract_target_line


class RemediationRequest(BaseModel):
    """Structured input sent to the AI remediation engine."""

    violation_id: str = Field(min_length=1)
    language: str = Field(min_length=1)
    rule: str = Field(min_length=1)
    severity: str = Field(min_length=1)
    file: str = Field(min_length=1)
    line: int = Field(gt=0)
    message: str = Field(min_length=1)
    target_code: str = Field(min_length=1)
    source_context: str = Field(min_length=1)


class RemediationResponse(BaseModel):
    """Structured remediation proposal returned by the AI."""

    violation_id: str = Field(min_length=1)
    analysis: str = Field(min_length=1)
    original_code: str = Field(min_length=1)
    proposed_code: str | None = None
    explanation: str = Field(min_length=1)
    confidence: float = Field(ge=0.0, le=1.0)
    requires_human_review: bool = True
    decision: str = Field(min_length=1)

def create_remediation_request(
    violation: Violation
) -> RemediationRequest:
    """Convert a validated violation into an AI remediation request."""

    source_file = (
        Path("sample_project") / violation.file
    )

    target_code = extract_target_line(
        source_file=source_file,
        target_line=violation.line
    )

    return RemediationRequest(
        violation_id=violation.id,
        language=violation.language,
        rule=violation.rule,
        severity=violation.severity,
        file=violation.file,
        line=violation.line,
        message=violation.message,
        target_code=target_code,
        source_context=violation.source_context
    )