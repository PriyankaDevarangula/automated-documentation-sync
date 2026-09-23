---
mode: agent
agent: verification
---

# Verification Prompt

## Purpose
Perform comprehensive verification before PR creation, using the repository guidance in [.github/instructions/project.instructions.md](../instructions/project.instructions.md).

## Expected Inputs
- requirements.md.
- architecture.md.
- Implementation under review.
- Relevant tests and documentation.
- Any available validation or security tooling configuration.

## Task to Perform
- Read requirements and architecture.
- Inspect the implementation.
- Inspect the tests.
- Run unit tests.
- Run integration tests when available.
- Validate documentation.
- Run security checks when available.
- Verify important happy paths.
- Verify important failure and edge cases.
- Report exact commands and results.
- Identify blockers and unsupported conditions.
- Never claim success without evidence.

## Expected Output / Artifact
- A verification summary with commands, results, evidence, and any blockers.

## Important Constraints
- Do not claim success without evidence.
- Do not silently modify production code to hide failures.
- Do not bypass security or validation checks.
- Keep evidence tied to the actual commands run.

## Human Approval Requirements
- If verification fails or required checks are unavailable, surface the blocker clearly and do not proceed as if the change is validated.
