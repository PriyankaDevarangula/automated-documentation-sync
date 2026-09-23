---
mode: agent
agent: documentation-sync
---

# Documentation Sync Prompt

## Purpose
Drive the automated documentation synchronization workflow, using the repository guidance in [.github/instructions/project.instructions.md](../instructions/project.instructions.md).

## Expected Inputs
- Relevant Python source changes.
- Existing Markdown documentation.
- Available repository-local analysis, update, validation, security, or allowlist modules.
- Current approval state for documentation synchronization.

## Task to Perform
- Identify the relevant Python source change set.
- Analyze the actual source change.
- Identify associated Markdown documentation.
- Detect missing or potentially outdated documentation.
- Explain the documentation gap.
- Preserve useful existing documentation.
- Generate or update only allowed Markdown files.
- Use repository-local analysis, updater, allowlist, validation, and security modules where available.
- Validate the generated documentation.
- Perform security checks.
- Maintain traceability between the source change and documentation change.
- Prepare the documentation-only change for its documentation synchronization PR.

## Expected Output / Artifact
- Documentation updates that reflect the actual source change.
- Traceability notes linking the source change to the documentation update.
- Validation and security evidence for the documentation change.

## Important Constraints
- Python source must never be modified by this workflow.
- Never invent source behavior.
- Do not expose secrets.
- Do not bypass validation or security checks.
- Do not bypass the documentation allowlist.
- Do not create duplicate documentation PRs.
- Follow the repository’s human-approval rules.

## Human Approval Requirements
- Documentation synchronization must not proceed without the required project approval state.
- If approvals are missing, stop and report the blocker rather than proceeding.
