---
mode: agent
agent: design-review
---

# Design Review Prompt

## Purpose
Perform the formal design review before implementation, using the repository guidance in [.github/instructions/project.instructions.md](../instructions/project.instructions.md).

## Expected Inputs
- requirements.md.
- architecture.md.
- Any relevant implementation constraints or project context.

## Task to Perform
- Read requirements.md and architecture.md.
- Review correctness.
- Review security.
- Review error handling.
- Review maintainability.
- Review testing considerations.
- Identify risks, design gaps, and missing decisions.
- Document findings in design-review.md.
- Distinguish findings from agreed design decisions.
- Identify architecture changes that should be made before implementation.

## Expected Output / Artifact
- design-review.md with concrete findings, risks, and recommendations.

## Important Constraints
- Do not implement production code.
- Do not silently rewrite requirements.
- Do not declare implementation complete.
- Keep findings separate from decisions already accepted by the project.

## Human Approval Requirements
- Recommendations that materially change the approved design should be surfaced for review and approval before implementation proceeds.
