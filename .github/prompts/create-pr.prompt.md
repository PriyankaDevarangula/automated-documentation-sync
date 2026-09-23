---
mode: agent
agent: pr-creation
---

# Create PR Prompt

## Purpose
Drive final PR creation using the repository guidance in [.github/instructions/project.instructions.md](../instructions/project.instructions.md).

## Expected Inputs
- Git status and the actual diff.
- requirements.md.
- architecture.md.
- design-review.md.
- Implementation plan when present.
- Code review findings.
- Verification evidence.

## Task to Perform
- Inspect git status.
- Inspect the actual diff.
- Read requirements.md.
- Read architecture.md.
- Read design-review.md.
- Read the implementation plan when present.
- Review code-review findings.
- Review verification evidence.
- Ensure required checks have evidence.
- Prepare an accurate PR title.
- Create a PR description containing exactly:

## Summary

2–3 sentence overview.

## Changes Made

Bulleted list of files added/modified and reasons.

## Test Evidence

Actual test/CI evidence.

## Known Limitations

Not Found, unsupported, or out-of-scope items.

## Reviewer Checklist

A practical checkbox list.

## Expected Output / Artifact
- A final PR title and description that accurately represents the implemented change and verified evidence.

## Important Constraints
- Do not invent test results.
- Do not invent CI results.
- Do not bypass human approval.
- Do not force-push.
- Do not expose credentials or tokens.
- Do not create duplicate documentation PRs.
- Do not silently modify the implementation while preparing the PR.

## Human Approval Requirements
- Only create the PR when the workflow and required approvals permit it.
- If evidence is missing or validation failed, stop and report the blocker rather than claiming readiness.
