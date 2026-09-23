---
name: documentation-sync
description: "Use when synchronizing Markdown documentation with actual Python source changes and preparing a documentation-only change for review."
---

# Documentation Sync

## Purpose
Provide a reusable capability for synchronizing Markdown documentation with actual Python source changes while preserving traceability, validation, and security requirements.

## Use When
- A Python change may require matching Markdown documentation updates.
- Documentation is missing, outdated, or inconsistent with implementation.
- You need to prepare a documentation-only change for an eventual documentation synchronization PR.
- The repo requires evidence-based documentation updates using repository-local analysis and validation modules.

## Inputs
- Relevant Python source changes.
- Existing Markdown documentation and any documentation allowlist constraints.
- Available repository-local analysis, updater, validation, or security modules.
- Current approval state for documentation synchronization.
- Repository guidance in [.github/instructions/project.instructions.md](../../instructions/project.instructions.md).

## Procedure
1. Identify the relevant Python change set and affected files.
2. Analyze the actual source change rather than relying on assumptions.
3. Identify the associated Markdown documentation and determine whether it is missing or potentially outdated.
4. Explain the documentation gap in explicit terms.
5. Preserve useful existing documentation and avoid broad rewrites.
6. Generate or update only the allowed Markdown files required by the source change.
7. Use repository-local analysis, updater, allowable validation, and security modules when available.
8. Validate the final Markdown content.
9. Run relevant security checks before declaring the update ready.
10. Maintain traceability between the source change and the documentation change.
11. Prepare the change for the documentation-sync PR workflow without altering Python source.

## Expected Outputs
- Minimal, evidence-based Markdown updates aligned with the actual Python change.
- A clear explanation of the documentation gap and why the update was needed.
- Traceability notes linking source changes to the updated documentation.
- Validation and security evidence for the documentation change.

## Important Constraints
- Never modify Python source code in this workflow.
- Never invent technical behavior, APIs, configuration, examples, or source semantics.
- Never expose secrets, credentials, tokens, or sensitive values.
- Never bypass the documentation allowlist or repository validation/security checks.
- Never create duplicate documentation PRs.
- Do not modify unrelated files.
- Follow the repository’s human-approval rules.

## Human Approval Requirements
- Do not treat approval as granted when approval is required.
- If required approval is missing, stop and report the blocker instead of proceeding.
- This skill supports the eventual automated documentation-sync PR workflow without replacing required review or approval steps.
