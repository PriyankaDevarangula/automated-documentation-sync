---
mode: agent
agent: code-review
---

# Code Review Prompt

## Purpose
Perform the capstone’s structured code review using the repository guidance in [.github/instructions/project.instructions.md](../instructions/project.instructions.md).

## Expected Inputs
- requirements.md.
- architecture.md.
- The implementation under review.
- Relevant tests and repository context.

## Task to Perform
Review the implementation against the following areas:

### Correctness
- Does each component behave as specified?

### Security
- Are secrets excluded and inputs handled safely?

### Error Handling
- Are failures, missing files, empty repositories, and external/API failures handled?

### Test Coverage
- Are happy paths and important edge cases covered?

### Code Clarity
- Are names and logic understandable?

### DRY
- Is there duplicated logic that should be shared?

### Dependency Safety
- Are dependency versions and known risks considered?

- Identify concrete findings.
- Identify affected files.
- Explain impact.
- Suggest focused remediation.
- Distinguish findings from assumptions.
- Do not claim tests passed without evidence.

## Expected Output / Artifact
- A structured review with concrete findings, file references, impact, and remediation suggestions.

## Important Constraints
- Do not make broad refactors automatically.
- Do not replace the verification agent.
- Keep suggestions focused and evidence-based.
- Do not silently assume behavior without checking the requirements and implementation.

## Human Approval Requirements
- Escalate unresolved design or security issues for human review when they materially affect the approved scope or risk profile.
