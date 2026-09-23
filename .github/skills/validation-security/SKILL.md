---
name: validation-security
description: "Use when validating repository changes safely, checking documentation, tests, and security-sensitive conditions before claiming completion."
---

# Validation and Security

## Purpose
Provide a reusable capability for validating repository changes safely and reporting evidence without overstating results.

## Use When
- You need to verify implementation or documentation quality.
- A review or PR workflow requires validation evidence.
- Documentation synchronization or implementation changes need verification before completion.
- Security-sensitive checks are required before a change is considered successful.

## Inputs
- The implementation, documentation, or change under review.
- Relevant requirements, architecture, or change context.
- Available repository validation and security tooling.
- Repository guidance in [.github/instructions/project.instructions.md](../../instructions/project.instructions.md).

## Procedure
1. Identify the relevant validation scope, including tests and documentation checks.
2. Run the relevant unit and integration tests when appropriate.
3. Validate documentation content and required structure or wording where applicable.
4. Check for secret exposure, credentials, tokens, or other sensitive content in changed artifacts.
5. Verify important happy paths and meaningful edge or failure scenarios.
6. Record the exact commands, outputs, and results used for evidence.
7. Stop when required validation or security checks fail.
8. Report blockers clearly rather than claiming success without evidence.

## Expected Outputs
- Validation evidence from relevant tests and checks.
- Documentation validation status.
- Security check status and any blockers or red flags.
- A clear statement of what passed and what failed.

## Important Constraints
- Never expose secrets or sensitive values.
- Never claim success without evidence.
- Never bypass required validation or security checks.
- Never hide failures by silently modifying the implementation.
- Keep evidence tied to the actual commands run and their outputs.

## Human Approval Requirements
- If validation or security checks fail, report the blocker and do not proceed as if the change is validated.
- This skill is reusable across verification, documentation-sync, and PR-related workflows without replacing required human approval or review.
