---
name: requirements-management
description: "Use when turning a User Story into clear, approved requirements; clarifying ambiguous scope or acceptance criteria before implementation begins."
---

# Requirements Management

## Purpose
Provide a reusable capability for turning a supplied User Story into clear, approved requirements that are ready for architecture and implementation.

## Use When
- You need to interpret a User Story or task.
- Requirements are vague, incomplete, or missing acceptance criteria.
- The repo needs explicit functional and non-functional requirements before implementation.
- Scope or out-of-scope items must be clarified before work proceeds.

## Inputs
- The supplied User Story or task description.
- Project context and any relevant constraints.
- Existing requirements and documentation when present.
- Repository guidance in [.github/instructions/project.instructions.md](../../instructions/project.instructions.md).

## Procedure
1. Read the supplied User Story carefully.
2. Identify ambiguities, missing information, constraints, assumptions, and acceptance criteria gaps.
3. Formulate targeted clarification questions for the human when required.
4. Incorporate the human’s answers and record any explicit decisions or assumptions.
5. Define functional requirements and non-functional requirements.
6. Identify scope and out-of-scope items.
7. Define acceptance criteria and any required verification conditions.
8. Produce or update requirements.md only after the requirements are sufficiently clarified.
9. Keep requirements explicit and grounded in evidence.

## Expected Outputs
- A clarified requirements.md or equivalent requirements artifact.
- A clear list of functional requirements, non-functional requirements, scope boundaries, and acceptance criteria.
- Explicitly recorded assumptions, decisions, and unresolved questions when needed.

## Important Constraints
- Never guess unresolved requirements.
- Do not implement production code.
- Do not design the architecture.
- Do not create a PR as part of this skill.
- Do not silently make product decisions when clarification is required.
- Respect the repository instructions and keep the work focused on the supplied problem.

## Human Approval Requirements
- Human clarification is required whenever key requirements are ambiguous or missing.
- Do not move forward to architecture or implementation until requirements are sufficiently clarified and approved.
