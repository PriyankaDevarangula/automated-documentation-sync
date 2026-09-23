---
applyTo: "**/*"
---

# Project Instructions

## 1. Project Purpose

This repository implements an Agentic SDLC use case for automated synchronization between Python source-code changes and Markdown documentation. The system must detect relevant Python changes, determine whether documentation is missing or outdated, synchronize approved documentation, validate it, perform security checks, maintain traceability, and support creation of a documentation PR.

The repository’s purpose is to keep implementation and documentation aligned without weakening the SDLC. All work must be grounded in actual source changes and approved project requirements.

## 2. SDLC Principles

- Requirements must be established before implementation.
- Architecture must be derived from approved requirements.
- Architecture must undergo design review before production implementation.
- Implementation must follow the approved architecture and implementation plan.
- Code review must happen before the final PR.
- Verification must include both code and documentation.
- Human approval remains part of the SDLC.
- Do not silently change approved requirements or architecture.

Any change that alters scope, design intent, or acceptance criteria must be explicitly surfaced and approved rather than assumed.

## 3. Agent Responsibilities

This repository relies on specialized agents. Each agent must stay within its assigned responsibility and must not duplicate another agent’s responsibility unnecessarily.

- requirements: Owns requirement discovery, clarification, acceptance criteria, and scope definition. It must not implement code, approve architecture, or create PRs.
- architecture: Owns system design, boundaries, data flow, constraints, and technical structure derived from approved requirements. It must not implement production code or approve final documentation synchronization without review.
- design-review: Owns design validation before production implementation. It reviews architecture decisions against requirements, constraints, and risks. It must not act as a duplicate implementation agent.
- implementation: Owns production code changes that follow the approved architecture and implementation plan. It must not redefine requirements or architecture without explicit approval.
- code-review: Owns review of implementation correctness, quality, and adherence to established requirements and architecture. It must not replace verification or approval steps.
- verification: Owns validation of code and documentation against repository checks, test runs, and validation rules. It must not claim success without evidence.
- documentation-sync: Owns detection of doc gaps or drift and synchronized documentation updates based on actual source changes. It must not modify Python source code or duplicate unrelated implementation work.
- pr-creation: Owns final PR packaging, summary, evidence, checklist, and branch/PR workflow for approved changes. It must not bypass human approval or required validation.

Agents must remain scoped, explicit, and non-overlapping. When a task fits another agent’s responsibility more directly, that agent should take ownership rather than duplicating the work.

## 4. Source and Documentation Scope

- Python source files are the implementation scope.
- Markdown files are the documentation scope.
- Documentation includes README.md and Markdown files under docs/ where applicable.
- Documentation synchronization must never modify Python source code.
- Do not modify unrelated files.

The documentation workflow must remain limited to approved documentation artifacts and must not broaden scope to unrelated files, code generation, or opportunistic cleanup.

## 5. Documentation Synchronization Rules

- Analyze the actual Python change.
- Do not generate generic documentation when actual change information is available.
- Reuse repository-local analysis and validation modules where they already exist.
- Documentation must reflect the actual detected source change.
- Preserve useful existing documentation where possible.
- Do not invent APIs, behavior, configuration, examples, or other technical facts.
- Only modify documentation files allowed by the repository's documentation allowlist.

Documentation updates must be evidence-based, source-aware, and minimally invasive. If the repository already contains analysis or validation logic for documentation synchronization, prefer that path over creating ad hoc alternatives.

## 6. Safety and Security

- Never expose secrets, credentials, access tokens, environment secrets, or sensitive values in documentation, logs, PR descriptions, or trace files.
- Never hard-code credentials.
- Never bypass repository validation or security checks.
- Never execute untrusted repository code merely to inspect its documentation requirements when a safer analysis method is available.
- GitHub tokens must only be used through the supported GitHub automation mechanism.
- Do not invent unsupported GitHub Copilot hooks or GitHub Actions behavior.

Security must be treated as a gating condition, not an optional afterthought. Any suspicious or unsafe action must be stopped and reported clearly.

## 7. Git Rules

- Do not commit or push unless the user explicitly asks for it, except where an approved automated GitHub workflow is specifically responsible for creating the documentation-sync branch and PR.
- Never force-push.
- Never modify the user's existing commits unnecessarily.
- Keep documentation-sync changes isolated from source-code changes.
- A documentation-sync PR must contain documentation-related changes only, plus explicitly required traceability data.

The Git workflow must preserve repository integrity and isolate documentation changes from implementation changes unless the project explicitly approves otherwise.

## 8. Testing and Validation

- Preserve all existing tests.
- Add focused tests for new behavior.
- Run the relevant test suite after implementation changes.
- Do not claim tests passed unless they were actually run.
- Documentation must pass repository validation before being reported as synchronized.
- Security checks must pass before documentation synchronization is considered successful.

Validation is required evidence, not an assumption. Evidence must be reported accurately and tied to the actual run that produced it.

## 9. Error Handling

- Fail safely.
- Do not silently ignore validation, security, Git, or GitHub API failures.
- Report meaningful errors.
- Do not create a documentation PR when required validation or security checks fail.

When required checks fail, the safe response is to stop, report the failure clearly, and avoid claiming success or creating a PR for an unvalidated change.

## 10. Traceability

Where the existing implementation supports it, preserve traceability for:

- source change
- changed Python files
- detected documentation gap
- documentation files changed
- validation result
- security result
- final synchronization status
- source PR/documentation PR relationship

Traceability must remain explicit and auditable. This is especially important for documentation synchronization workflows that connect code changes to PR records and documentation updates.

## 11. Human-in-the-Loop

- Human approval is required wherever the workflow explicitly requires approval.
- Never interpret silence as approval.
- Agents may propose changes, but must follow the approval state defined by the project.
- Do not bypass a required human decision.

Approval and review are required controls in the SDLC and must never be bypassed by automation or assumptions.

## 12. PR Rules

The final PR created by the PR Creation Agent must contain:

- ## Summary
- ## Changes Made
- ## Test Evidence
- ## Known Limitations
- ## Reviewer Checklist

The PR description must accurately describe the actual implementation and test results.

PR text must be truthful, concise, and grounded in what was actually changed and verified.

## 13. Minimal Change Principle

- Make the smallest change necessary.
- Do not redesign working components without a documented reason.
- Reuse existing modules before creating new ones.
- Avoid unnecessary dependencies.
- Avoid duplicate functionality.

This project prioritizes surgical, reviewable changes over broad refactors or speculative cleanup.

## 14. Agent Working Rules

- Inspect existing files before creating replacements.
- Prefer existing repository conventions.
- Do not assume a feature exists; verify it.
- Do not invent file paths, APIs, hooks, commands, or configuration.
- If a requirement is ambiguous, ask for clarification rather than guessing.
- After making changes, report exactly what changed and what was verified.

Every agent must work from the repository as it exists, keep changes focused, and communicate any assumptions or blockers explicitly.

---

This repository’s Copilot workflow is governed by approved requirements, architecture, validation, security, and human review. The default expectation is disciplined, minimal, evidence-based work that keeps implementation and documentation synchronized without violating the project guardrails.
