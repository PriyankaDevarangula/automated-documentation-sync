---
name: pr-preparation
description: "Use when preparing accurate, traceable PR content from the actual diff, implementation, and validation evidence."
---

# PR Preparation

## Purpose
Provide a reusable capability for preparing accurate, traceable PR content without inventing evidence or bypassing required approval.

## Use When
- A completed implementation or documentation-only change is ready for PR preparation.
- You need to summarize the actual change and corresponding evidence.
- The repo requires a final PR description with structured sections and a reviewer checklist.
- Documentation-sync changes need traceability and documentation-only scoping.

## Inputs
- Git status and the actual diff.
- Changed files and the implementation or documentation under review.
- requirements.md, architecture.md, design-review.md, and implementation plan when present.
- Code review findings and verification evidence.
- Repository guidance in [.github/instructions/project.instructions.md](../../instructions/project.instructions.md).

## Procedure
1. Inspect git status and the actual diff.
2. Identify the changed files and summarize the actual implementation or documentation updates.
3. Collect validation evidence and any relevant test/CI results.
4. Identify known limitations, unsupported items, and out-of-scope considerations.
5. Prepare a practical reviewer checklist.
6. Maintain source PR/documentation PR traceability when applicable.
7. Ensure documentation-sync PRs remain documentation-only plus explicitly required traceability data.
8. Assemble a final PR title and description aligned to the real evidence.

## Expected Outputs
- A PR title and description with these sections:
  - Summary
  - Changes Made
  - Test Evidence
  - Known Limitations
  - Reviewer Checklist
- A concise summary of the actual implementation and validation evidence.
- Traceability notes where the project requires them.

## Important Constraints
- Never invent test or CI results.
- Never expose credentials, tokens, or sensitive values.
- Never bypass required approval or validation.
- Never create duplicate documentation PRs.
- Never force-push.
- Keep the PR grounded in the actual diff and evidence.

## Human Approval Requirements
- Do not create or finalize a PR when approval or required validation is missing.
- Any blocker or unresolved risk should be clearly documented instead of being hidden or assumed away.
