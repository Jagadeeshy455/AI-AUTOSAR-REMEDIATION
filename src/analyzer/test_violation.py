from violation import Violation


violation = Violation(
    id="VIOL-001",
    rule="MISRA_C_2012_10_3",
    severity="warning",
    file="src/sensor.c",
    line=26,
    message="Test violation",
    source_context="scaled_value = sensor_value;"
)

print(violation)
print()
print(f"Rule: {violation.rule}")
print(f"File: {violation.file}")
print(f"Line: {violation.line}")