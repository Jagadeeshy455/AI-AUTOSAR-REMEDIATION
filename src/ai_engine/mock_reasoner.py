from src.ai_engine.remediation import RemediationRequest
from src.ai_engine.rule_knowledge import RuleGuidance


class MockReasoner:
    """
    Simulates AI reasoning for automotive coding-rule remediation.

    This is intentionally deterministic so the project can be
    developed and tested without an external AI API.
    """

    def generate(
        self,
        request: RemediationRequest,
        guidance: RuleGuidance | None,
    ) -> dict:

        if guidance is None:
            return {
                "proposed_code": None,
                "analysis": (
                    f"No rule guidance is available for "
                    f"{request.rule}."
                ),
                "confidence": 0.0,
                "decision": "REVIEW_REQUIRED",
            }

        rule = request.rule
        target = request.target_code.strip()

        # MISRA C:2012 Rule 10.3
        if rule == "MISRA_C_2012_10_3":

            if target == "scaled_value = sensor_value;":
                return {
                    "proposed_code": (
                        "scaled_value = (uint8_t)sensor_value;"
                    ),
                    "analysis": (
                        "Explicitly control the integer conversion "
                        "between the source and destination types."
                    ),
                    "confidence": 0.82,
                    "decision": "REVIEW_REQUIRED",
                }

        # MISRA C:2012 Rule 12.1
        if rule == "MISRA_C_2012_12_1":

            if (
                "&&" in target
                and "==" in target
            ):
                proposed = target.replace(
                    "speed_valid == 1U && temperature_valid == 1U",
                    "((speed_valid == 1U) && "
                    "(temperature_valid == 1U))",
                )

                return {
                    "proposed_code": proposed,
                    "analysis": (
                        "Make operator precedence explicit "
                        "through parentheses."
                    ),
                    "confidence": 0.95,
                    "decision": "REVIEW_REQUIRED",
                }

        # MISRA C:2012 Rule 10.8
        if rule == "MISRA_C_2012_10_8":

            if target == "status = temperature + 200U;":
                return {
                    "proposed_code": (
                        "status = "
                        "(uint8_t)(temperature + 200U);"
                    ),
                    "analysis": (
                        "Explicitly control the composite "
                        "expression conversion."
                    ),
                    "confidence": 0.78,
                    "decision": "REVIEW_REQUIRED",
                }

        # MISRA C:2012 Rule 8.9
        if rule == "MISRA_C_2012_8_9":

            if target.startswith(
                "static uint16_t default_sensor_value"
            ):
                return {
                    "proposed_code": (
                        "Move the object into get_sensor_value():\n\n"
                        "uint16_t get_sensor_value(void)\n"
                        "{\n"
                        "    uint16_t default_sensor_value = 250U;\n"
                        "\n"
                        "    return default_sensor_value;\n"
                        "}"
                    ),
                    "analysis": (
                        "The file-scope object appears to be used "
                        "only by get_sensor_value(). Its scope can "
                        "potentially be reduced to block scope."
                    ),
                    "confidence": 0.88,
                    "decision": "REVIEW_REQUIRED",
                }

        # Generic fallback
        return {
            "proposed_code": None,
            "analysis": (
                f"The rule {rule} was identified, but the available "
                "source context is insufficient to safely generate "
                "a deterministic remediation."
            ),
            "confidence": 0.0,
            "decision": "REVIEW_REQUIRED",
        }