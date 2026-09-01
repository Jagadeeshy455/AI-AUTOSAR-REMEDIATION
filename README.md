# AI-Powered AUTOSAR/MISRA Remediation Automation

## Project Status

**Status:** Work in Progress — Day 1 completed  
**Current implementation:** Python prototype with a deterministic `MockAIProvider`  
**Target:** AI-assisted remediation of automotive MISRA/AUTOSAR static-analysis findings with automated validation and controlled Git workflow.

---

## 1. Project Overview

This project is a Python-based automation framework designed to reduce the manual effort involved in analyzing and remediating static-analysis findings in automotive C/C++ software.

### High-level workflow

```text
Automotive C/C++ Source Code
            |
            v
   Static Analysis Tool
            |
            v
     Violation Report
            |
            v
      Report Parser
            |
            v
   Source Context Analyzer
            |
            v
    Remediation Request
            |
            v
    AI Remediation Engine
            |
            +----------------------+
            |                      |
            v                      v
      MockAIProvider        Future Real LLM Provider
            |                      |
            +----------+-----------+
                       |
                       v
             Remediation Response
                       |
                       v
              Validation Engine
                       |
                 +-----+-----+
                 |           |
                PASS        FAIL
                 |           |
                 v           v
           Human Review   Rework/Reject
                 |
                 v
          Git Patch / PR
```

The design follows a **human-in-the-loop** approach: AI-generated changes are candidate remediations and are not blindly accepted.

---

## 2. Objectives

- Parse structured MISRA/AUTOSAR static-analysis reports.
- Identify the source file and exact violation line.
- Extract source-code context around the finding.
- Identify the target code.
- Build a structured AI remediation request.
- Generate candidate remediation proposals.
- Return explanation and confidence with each proposal.
- Require human review before acceptance.
- Keep the AI backend replaceable through provider abstraction.
- Progress toward automated patch generation, validation and controlled Git workflow automation.

---

## 3. Day 1 — Completed Scope

Day 1 established the foundation of the remediation pipeline.

Completed:

- Windows + VS Code development environment.
- Python virtual environment.
- Git repository and GitHub remote.
- Sample automotive C source-code project.
- Deliberately introduced realistic MISRA-style findings.
- JSON-based static-analysis report.
- Violation parsing.
- Source-context extraction.
- Target-code identification.
- Pydantic-based remediation request/response contracts.
- Remediation engine abstraction.
- Generic/rule-aware `MockAIProvider`.
- Candidate remediation strategies for multiple MISRA C rules.
- Confidence scoring.
- Mandatory human-review decisions.
- Git milestone-based development workflow.

---

## 4. Technology Stack

### Programming
- Python 3.13.x
- C
- JSON

### Python
- Pydantic
- Object-Oriented Programming
- File handling
- JSON parsing
- Data validation
- Modular architecture
- Provider abstraction

### Automotive / Static Analysis
- MISRA C
- AUTOSAR coding-standard concepts
- Static analysis
- C source-code remediation

### AI
- AI-assisted code remediation
- AI input/output contract design
- AI provider abstraction
- Mock AI provider
- Confidence scoring
- Human-in-the-loop workflow
- LLM integration planned for a later stage

### Development Tools
- Windows
- VS Code
- Git
- GitHub
- Python virtual environment
- PowerShell

---

## 5. Project Structure

```text
AI-AUTOSAR-REMEDIATION/
|
+-- sample_project/
|   |
|   +-- analysis_reports/
|   |   +-- violations.json
|   |
|   +-- include/
|   |   +-- sensor.h
|   |   +-- vehicle_control.h
|   |
|   +-- src/
|       +-- sensor.c
|       +-- vehicle_control.c
|
+-- src/
|   |
|   +-- analyzer/
|   |   +-- source_context.py
|   |   +-- test_violation.py
|   |
|   +-- parser/
|   |   +-- report_parser.py
|   |
|   +-- pipeline/
|   |   +-- violation_pipeline.py
|   |
|   +-- ai_engine/
|       +-- remediation.py
|       +-- remediation_engine.py
|       +-- mock_provider.py
|       +-- test_provider.py
|
+-- main.py
+-- .gitignore
+-- README.md
```

---

## 6. Sample Static-Analysis Findings

The current sample report contains four findings:

| ID | Rule | File | Line | Purpose |
|---|---|---|---:|---|
| VIOL-001 | MISRA_C_2012_10_3 | `src/sensor.c` | 26 | Explicit integer conversion |
| VIOL-002 | MISRA_C_2012_12_1 | `src/vehicle_control.c` | 52 | Explicit operator precedence |
| VIOL-003 | MISRA_C_2012_10_8 | `src/vehicle_control.c` | 40 | Explicit composite-expression conversion |
| VIOL-004 | MISRA_C_2012_8_9 | `src/sensor.c` | 3 | Reduce file-scope object to block scope |

Each finding contains:

```text
id
rule
severity
language
file
line
message
```

---

## 7. Current Candidate Remediations

### VIOL-001 — MISRA_C_2012_10_3

Original:

```c
scaled_value = sensor_value;
```

Candidate:

```c
scaled_value = (uint8_t)sensor_value;
```

Confidence: **0.82**  
Decision: **REVIEW_REQUIRED**

Validation should verify truncation, overflow, signedness and information-loss risks.

### VIOL-002 — MISRA_C_2012_12_1

Original:

```c
result = speed_valid == 1U && temperature_valid == 1U;
```

Candidate:

```c
result = ((speed_valid == 1U) && (temperature_valid == 1U));
```

Confidence: **0.95**  
Decision: **REVIEW_REQUIRED**

### VIOL-003 — MISRA_C_2012_10_8

Original:

```c
status = temperature + 200U;
```

Candidate:

```c
status = (uint8_t)(temperature + 200U);
```

Confidence: **0.78**  
Decision: **REVIEW_REQUIRED**

Validation should verify range, overflow, truncation, signedness and behavioral equivalence.

### VIOL-004 — MISRA_C_2012_8_9

Original:

```c
static uint16_t default_sensor_value = 250U;
```

Candidate:

```c
uint16_t get_sensor_value(void)
{
    uint16_t default_sensor_value = 250U;

    return default_sensor_value;
}
```

Confidence: **0.88**  
Decision: **REVIEW_REQUIRED**

Validation should verify references, initialization, lifetime, linkage and behavior.

---

## 8. Violation Processing Pipeline

```text
violations.json
      |
      v
Report Parser
      |
      v
Violation Model
      |
      v
Source Context Analyzer
      |
      +--> Target Code
      |
      +--> Surrounding Source Context
      |
      v
RemediationRequest
      |
      v
RemediationEngine
      |
      v
MockAIProvider
      |
      v
RemediationResponse
```

Example source context:

```text
21 |
22 | uint8_t calculate_scaled_value(uint16_t sensor_value)
23 | {
24 |     uint8_t scaled_value;
25 |
26 | >> scaled_value = sensor_value;
27 |
28 |     return scaled_value;
29 | }
```

The context is included in the remediation request so the AI layer receives more than only a rule ID.

---

## 9. AI Input Contract

The current structured request contains:

```json
{
    "violation_id": "VIOL-001",
    "language": "C",
    "rule": "MISRA_C_2012_10_3",
    "severity": "warning",
    "file": "src/sensor.c",
    "line": 26,
    "message": "A value of narrower essential type is assigned to an object of a wider essential type category.",
    "target_code": "scaled_value = sensor_value;",
    "source_context": "..."
}
```

The contract separates the remediation pipeline from the AI provider.

---

## 10. AI Output Contract

The remediation response contains:

```text
violation_id
analysis
original_code
proposed_code
explanation
confidence
requires_human_review
decision
```

Example:

```json
{
    "violation_id": "VIOL-001",
    "analysis": "Explicitly control the integer conversion between the source and destination types.",
    "original_code": "scaled_value = sensor_value;",
    "proposed_code": "scaled_value = (uint8_t)sensor_value;",
    "explanation": "The mock AI reasoner generated a candidate remediation using the supplied rule guidance. The proposal must be validated before acceptance.",
    "confidence": 0.82,
    "requires_human_review": true,
    "decision": "REVIEW_REQUIRED"
}
```

---

## 11. MockAIProvider

The current provider is a deterministic `MockAIProvider`.

It is used to develop and test the complete architecture without requiring an external AI API.

It is **generic/rule-aware**, rather than being limited to one hardcoded violation.

Current demonstrated rules:

```text
MISRA_C_2012_10_3
MISRA_C_2012_12_1
MISRA_C_2012_10_8
MISRA_C_2012_8_9
```

For findings without a deterministic strategy, the design can return analysis and validation guidance without inventing a code change, while requiring human review.

---

## 12. Safety and Human Review

AI-generated code must not directly become production automotive code.

The intended quality gates are:

```text
AI Proposal
    |
    v
Automated Validation
    |
    +--> Syntax
    +--> Build/Compile
    +--> MISRA/AUTOSAR Analysis
    +--> Regression Tests
    |
    v
Human Review
    |
    v
Git Patch / Pull Request
```

The human reviewer remains responsible for the final acceptance decision.

---

## 13. Git Workflow

The project uses Git with milestone-based commits.

Current repository state:

```text
Branch: master
Working tree: clean
Remote: origin
```

Normal workflow:

```powershell
git status
git add .
git commit -m "Meaningful milestone description"
git push
```

GitHub repository:

```text
https://github.com/Jagadeeshy455/AI-AUTOSAR-REMEDIATION
```

Secrets such as API keys must never be committed to the repository.

---

## 14. Day 1 Milestones

### Step 1 — Environment and Project Setup
- Windows development environment.
- VS Code.
- Python virtual environment.
- Git repository and GitHub remote.
- Project entry point.

### Step 2 — Sample Automotive Codebase
Created:

```text
sample_project/
├── analysis_reports/
│   └── violations.json
├── include/
│   ├── sensor.h
│   └── vehicle_control.h
└── src/
    ├── sensor.c
    └── vehicle_control.c
```

### Step 3 — Violation and Source Context Analysis
Implemented:
- Violation parsing.
- File/line tracking.
- Source-context extraction.
- Target-code identification.

### Step 4 — Pipeline Integration
The pipeline successfully processes four findings and prints:
- ID
- Rule
- Severity
- Language
- File
- Line
- Message
- Source context

### Step 5 — AI Input/Output Contract
Implemented structured Pydantic models for remediation requests and responses.

### Step 6 — Remediation Engine
Implemented:
- `RemediationEngine`
- AI provider abstraction
- Structured remediation request
- Structured remediation response
- Test execution

### Step 7 — Realistic Mock AI Remediation Engine
Enhanced the provider to:
- Handle multiple violation types.
- Generate candidate remediation where deterministic guidance is available.
- Provide analysis.
- Provide explanation.
- Provide confidence.
- Require human review.
- Return a review decision.

**Day 1 completed.**

---

## 15. Current Limitations

This is a prototype and is **not yet production-ready**.

Current limitations:

- No real LLM API is connected.
- Automated patch application is not implemented yet.
- Automated compile/build validation is not implemented yet.
- Automated MISRA/AUTOSAR re-analysis is not implemented yet.
- Regression-test orchestration is not implemented yet.
- Git patch/PR automation is planned but not implemented yet.

These are intentionally planned for subsequent milestones.

---

## 16. Planned Next Steps

### Day 2 — Production-Style AI Provider

Planned:

1. Production-style AI provider interface.
2. Prompt contract.
3. Structured prompt generation.
4. Real AI provider abstraction.
5. Mock provider compatibility with the same contract.
6. AI response validation.
7. Confidence/safety decision engine.

### Later stages

```text
AI Response Validation
        |
        v
Patch Generation
        |
        v
Safe Patch Application
        |
        v
Before/After Diff
        |
        v
Compilation
        |
        v
MISRA/AUTOSAR Re-analysis
        |
        v
Regression Tests
        |
        v
Git Branch
        |
        v
Commit / Pull Request
        |
        v
Human Review
```

---

## 17. End-to-End Example

For `VIOL-001`:

```text
1. Static analyzer reports MISRA_C_2012_10_3 at sensor.c:26.
2. Python parser loads the finding.
3. Source-context analyzer extracts the relevant code.
4. Target code is identified:
   scaled_value = sensor_value;
5. A RemediationRequest is created.
6. RemediationEngine sends it to the AI provider.
7. MockAIProvider generates:
   scaled_value = (uint8_t)sensor_value;
8. The response includes analysis, explanation, confidence and review status.
9. Future validation will compile and re-run static analysis.
10. If validation succeeds, a controlled Git patch/PR can be generated.
11. A human reviewer makes the final acceptance decision.
```

---

## 18. Interview Explanation

> I am developing a Python-based AI-assisted automation framework for remediating MISRA and AUTOSAR static-analysis findings in automotive C/C++ software. The system parses static-analysis reports, extracts source context, identifies target code, creates a structured remediation request and sends it through an AI-provider abstraction. The current prototype uses a deterministic MockAIProvider to generate candidate fixes, explanations and confidence scores. The architecture is designed so a real LLM provider can be integrated without changing the core pipeline. The next stages are automated response validation, patch generation, compilation/static-analysis verification and controlled Git workflow automation, with human review retained as a quality gate.

---

## 19. Key Engineering Concepts Demonstrated

- Python automation
- Python OOP
- Pydantic data validation
- JSON processing
- Static-analysis report processing
- Source-code context extraction
- AI provider abstraction
- Rule-aware remediation
- Structured AI contracts
- Confidence scoring
- Human-in-the-loop design
- Git-based development
- MISRA C
- AUTOSAR concepts
- Testable modular architecture
- Incremental milestone-based development

---

## 20. Disclaimer

This repository is an engineering prototype for demonstrating AI-assisted static-analysis remediation concepts.

AI-generated remediation proposals must be validated against the actual project requirements, compiler/toolchain, MISRA/AUTOSAR configuration, safety requirements and regression tests before being accepted into production automotive software.
