---
mode: agent
agent: requirements
---

# Requirements Prompt

## Purpose
Drive the requirements stage from a supplied User Story, using the repository guidance in [.github/instructions/project.instructions.md](../instructions/project.instructions.md).

## Expected Inputs
- A user story or task description.
- Relevant project context or constraints.
- Any clarifying questions already provided by the user.

## Task to Perform
- Read the User Story.
- Identify ambiguity, missing information, constraints, and assumptions.
- Ask clarification questions when required.
- Wait for human answers when clarification is needed.
- Establish explicit functional requirements.
- Establish explicit non-functional requirements.
- Define scope and out-of-scope items.
- Define acceptance criteria.
- Create or update requirements.md only after clarification is sufficient.

## Expected Output / Artifact
- A completed requirements.md that captures scope, requirements, assumptions, and acceptance criteria.

## Important Constraints
- Do not implement code.
- Do not design architecture.
- Do not guess missing requirements.
- Do not silently make product decisions when clarification is required.
- Keep the requirements grounded in the supplied User Story and repository instructions.

## Human Approval Requirements
- Human clarification is required whenever key requirements are ambiguous or missing.
- Do not move forward to implementation or architecture until requirements are sufficiently clarified and approved.
