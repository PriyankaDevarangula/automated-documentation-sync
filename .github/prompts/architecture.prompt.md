---
mode: agent
agent: architecture
---

# Architecture Prompt

## Purpose
Drive architecture design from approved requirements, using the repository guidance in [.github/instructions/project.instructions.md](../instructions/project.instructions.md).

## Expected Inputs
- requirements.md.
- Approved project constraints and scope.
- Any relevant design assumptions or context from the SDLC workflow.

## Task to Perform
- Read requirements.md.
- Identify system components and responsibilities.
- Define data flow and boundaries.
- Define technology choices and rationale.
- Define integration, security, validation, and error-handling boundaries.
- Document the result in architecture.md.
- Surface unresolved design decisions that require stakeholder input.

## Expected Output / Artifact
- An architecture.md that explains the system structure, responsibilities, interfaces, trade-offs, and design constraints.

## Important Constraints
- Architecture must remain consistent with approved requirements.
- Do not implement production code.
- Do not redefine requirements silently.
- Surface unresolved design decisions rather than hiding them.
- Keep the design aligned with the repository’s SDLC requirements and security expectations.

## Human Approval Requirements
- Any major design decision that materially changes approved requirements should be surfaced for review before proceeding.
- Do not bypass design review.
