from dataclasses import dataclass


@dataclass(frozen=True)
class RuleGuidance:
    """Knowledge associated with a coding-standard rule."""

    rule: str
    description: str
    remediation_guidance: str
    validation_guidance: str


RULE_GUIDANCE: dict[str, RuleGuidance] = {

    "MISRA_C_2012_10_3": RuleGuidance(
        rule="MISRA_C_2012_10_3",
        description=(
            "Controls assignments and conversions between "
            "different essential type categories."
        ),
        remediation_guidance=(
            "Analyze the source and destination essential types. "
            "Where appropriate, use an explicit and safe conversion "
            "while preserving the intended value range and behavior."
        ),
        validation_guidance=(
            "Verify that the conversion cannot introduce unintended "
            "truncation, overflow, sign changes, or loss of information."
        ),
    ),

    "MISRA_C_2012_12_1": RuleGuidance(
        rule="MISRA_C_2012_12_1",
        description=(
            "Requires operator precedence to be made explicit "
            "where necessary for clarity and safety."
        ),
        remediation_guidance=(
            "Analyze the expression and add parentheses where they "
            "make the intended evaluation order explicit."
        ),
        validation_guidance=(
            "Verify that the resulting expression preserves the "
            "original intended evaluation semantics."
        ),
    ),

    "MISRA_C_2012_10_8": RuleGuidance(
        rule="MISRA_C_2012_10_8",
        description=(
            "Controls casts of composite expressions to ensure "
            "type conversion is explicit and well-defined."
        ),
        remediation_guidance=(
            "Analyze the composite expression and use an explicit "
            "conversion only when it is appropriate for the intended "
            "range and essential type."
        ),
        validation_guidance=(
            "Verify range, overflow, truncation, signedness, and "
            "behavioral equivalence after the proposed conversion."
        ),
    ),

    "MISRA_C_2012_8_9": RuleGuidance(
        rule="MISRA_C_2012_8_9",
        description=(
            "Addresses objects that are only used within one "
            "function and may therefore have narrower scope."
        ),
        remediation_guidance=(
            "Determine whether the object has file scope and whether "
            "its references are limited to a single function. If so, "
            "consider moving the object to the appropriate block scope."
        ),
        validation_guidance=(
            "Verify that all references remain valid and that moving "
            "the object does not change initialization, lifetime, "
            "linkage, or program behavior."
        ),
    ),
}


def get_rule_guidance(rule: str) -> RuleGuidance | None:
    """Return guidance for a known rule."""

    return RULE_GUIDANCE.get(rule)