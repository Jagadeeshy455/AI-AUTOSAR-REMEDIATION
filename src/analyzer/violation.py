from pydantic import BaseModel, Field


class Violation(BaseModel):
    """Represents a validated static-analysis violation."""

    id: str = Field(min_length=1)
    rule: str = Field(min_length=1)
    severity: str = Field(min_length=1)
    language: str = Field(min_length=1)
    file: str = Field(min_length=1)
    line: int = Field(gt=0)
    message: str = Field(min_length=1)
    source_context: str = ""