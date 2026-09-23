---
mode: agent
agent: implementation
---

# Implementation Prompt

## Purpose
Implement the approved design while following repository requirements and guardrails in [.github/instructions/project.instructions.md](../instructions/project.instructions.md).

## Expected Inputs
- requirements.md.
- architecture.md.
- design-review.md.
- impl-plan.md when present.
- Relevant repository files for inspection.

## Task to Perform
- Read requirements.md.
- Read architecture.md.
- Read design-review.md.
- Read impl-plan.md when present.
- Inspect the existing repository before changing files.
- Implement only approved functionality.
- Write or update tests for the changed behavior.
- Reuse existing modules before creating duplicate functionality.
- Keep changes minimal and reviewable.
- Run the relevant tests.
- Report exactly what changed and what tests were run.

## Expected Output / Artifact
- A minimal implementation that matches the approved requirements and architecture.
- Relevant test updates or additions.
- A brief summary of code changes and verification evidence.

## Important Constraints
- Do not silently change requirements.
- Do not silently redesign architecture.
- Do not modify unrelated files.
- Do not commit or push unless explicitly instructed.
- Do not bypass validation or security checks.

## Human Approval Requirements
- Only implement approved work and any required follow-up changes explicitly permitted by the design and review workflow.
- Do not proceed outside the approved implementation scope.
