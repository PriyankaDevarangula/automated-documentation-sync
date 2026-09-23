"""Minimal documentation synchronization workflow for the approved API docs use case."""

from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Any, Dict, List

ALLOWED_DOC_PATH = Path("docs/api.md")
SUPPORTED_API_PATHS = {"/books", "/books/{id}"}
SUPPORTED_METHODS = {"GET", "POST"}


def _normalize_path(path: str) -> str:
    return path.strip()


def _endpoint_signature(method: str, path: str) -> str:
    return f"{method.upper()} {path}"


def analyze_api_source(source_path: str | Path) -> List[Dict[str, str]]:
    """Parse the API router AST and return supported endpoints only."""
    path = Path(source_path)
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    endpoints: List[Dict[str, str]] = []

    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue

        if not node.decorator_list:
            continue

        for decorator in node.decorator_list:
            if not isinstance(decorator, ast.Call):
                continue
            func = decorator.func
            if not isinstance(func, ast.Attribute):
                continue
            if func.attr not in {"get", "post"}:
                continue
            if not isinstance(decorator.args[0], ast.Constant):
                continue
            route = str(decorator.args[0].value)
            if route not in {"/books", "/books/{id}", "/books"}:
                continue
            endpoints.append({"method": func.attr.upper(), "path": route})

    if not endpoints:
        return []

    seen = set()
    deduped: List[Dict[str, str]] = []
    for endpoint in endpoints:
        key = (endpoint["method"], endpoint["path"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(endpoint)
    return deduped


def detect_relevant_api_change(source_path: str | Path) -> bool:
    """Return True only for supported API behavior changes."""
    path = Path(source_path)
    if not path.exists():
        return False

    endpoints = analyze_api_source(path)
    if not endpoints:
        return False

    relevant_paths = {"/books", "/books/{id}", "/books"}
    for endpoint in endpoints:
        if endpoint["path"] in relevant_paths:
            return True
    return False


def _doc_content_for_endpoints(endpoints: List[Dict[str, str]]) -> str:
    blocks = [
        "# Books API",
        "",
        "This file documents the supported Books API endpoints.",
        "",
        "<!-- AUTO-GENERATED API ENDPOINTS START -->",
        "## Endpoints",
        "",
    ]

    for endpoint in endpoints:
        method = endpoint["method"]
        path = endpoint["path"]
        if method == "GET" and path == "/books":
            blocks.extend([
                "### GET /books",
                "- Returns a list of books.",
                "- Status: 200",
                "",
            ])
        elif method == "GET" and path == "/books/{id}":
            blocks.extend([
                "### GET /books/{id}",
                "- Returns one book by id.",
                "- Status: 200",
                "",
            ])
        elif method == "POST" and path == "/books":
            blocks.extend([
                "### POST /books",
                "- Creates a new book.",
                "- Status: 201",
                "",
            ])

    blocks.extend([
        "<!-- AUTO-GENERATED API ENDPOINTS END -->",
        "",
        "Additional manual notes can live here.",
        "",
    ])
    return "\n".join(blocks)


def _is_allowed_doc_path(doc_path: str | Path) -> bool:
    normalized = str(Path(doc_path)).replace("\\", "/")
    return normalized.endswith("/docs/api.md") or normalized.endswith("docs/api.md")


def _replace_generated_api_block(existing: str, expected: str) -> str:
    """Replace only the generated endpoint block while preserving surrounding manual notes."""
    start_marker = "<!-- AUTO-GENERATED API ENDPOINTS START -->"
    end_marker = "<!-- AUTO-GENERATED API ENDPOINTS END -->"
    if start_marker not in existing or end_marker not in existing:
        return expected

    before, remainder = existing.split(start_marker, 1)
    _, after = remainder.split(end_marker, 1)
    expected_start = expected.split(start_marker, 1)[0]
    expected_body = expected.split(start_marker, 1)[1].split(end_marker, 1)[0]
    expected_tail = expected.split(end_marker, 1)[1]

    if expected_start != "":
        expected_block = expected_start + start_marker + expected_body + end_marker + expected_tail
    else:
        expected_block = start_marker + expected_body + end_marker

    return before + expected_block + after


def validate_documentation(doc_path: str | Path, endpoints: List[Dict[str, str]]) -> Dict[str, Any]:
    """Validate documentation against expected API endpoints."""
    path = Path(doc_path)
    if not path.exists():
        return {"valid": False, "missing_endpoints": [endpoint["method"] + " " + endpoint["path"] for endpoint in endpoints], "reason": "missing document"}

    text = path.read_text(encoding="utf-8")
    expected = {_endpoint_signature(endpoint["method"], endpoint["path"]) for endpoint in endpoints}
    observed = set()
    for match in re.finditer(r"(?im)^\s*###?\s*(GET|POST)\s+(/books(?:/\{id\})?)\s*$", text):
        observed.add(f"{match.group(1).upper()} {match.group(2)}")
    missing = sorted(expected - observed)
    valid = not missing
    return {"valid": valid, "missing_endpoints": missing, "reason": "ok" if valid else "missing required endpoint sections"}


def _security_check(text: str) -> Dict[str, Any]:
    patterns = [
        r"gh[pousr]_[A-Za-z0-9]{20,}",
        r"AKIA[0-9A-Z]{16}",
        r"xox[baprs]-[A-Za-z0-9-]+",
    ]
    leaks = []
    for pattern in patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        leaks.extend(matches)
    return {"safe": not leaks, "issues": leaks}


def _is_malformed_existing_document(text: str) -> bool:
    """Return True for structurally invalid minimal docs that should not be overwritten."""
    content = text.strip()
    if not content:
        return False

    non_empty_lines = [line.strip() for line in content.splitlines() if line.strip()]
    if len(non_empty_lines) <= 1:
        return True

    markers = [
        "<!-- AUTO-GENERATED API ENDPOINTS START -->",
        "## Endpoints",
        "### GET /books",
        "### POST /books",
    ]
    return any(marker in content for marker in markers)


def sync_documentation(source_path: str | Path, doc_path: str | Path, approval: bool = False) -> Dict[str, Any]:
    """Synchronize the approved docs for the Books API without modifying Python source files."""
    source_file = Path(source_path)
    doc_file = Path(doc_path)

    if not approval:
        return {
            "status": "approval_required",
            "reason": "human approval is required before documentation synchronization",
            "traceability": {
                "source_change": "unknown",
                "changed_python_files": [str(source_file)],
                "documentation_gap": "unknown",
                "validation_result": "not_run",
                "workflow_result": "approval_required",
            },
        }

    if not _is_allowed_doc_path(doc_file):
        raise ValueError(f"Unsupported documentation target: {doc_file}. Only docs/api.md is allowed.")

    if source_file.suffix != ".py":
        raise ValueError("API source must be a Python file.")

    endpoints = analyze_api_source(source_file)
    if not endpoints:
        return {
            "status": "not_relevant",
            "reason": "no supported API endpoints detected",
            "traceability": {
                "source_change": "not_relevant",
                "changed_python_files": [str(source_file)],
                "documentation_gap": "none",
                "validation_result": "not_run",
                "workflow_result": "not_relevant",
            },
        }

    if not detect_relevant_api_change(source_file):
        return {
            "status": "not_relevant",
            "reason": "source change does not affect the supported API contract",
            "traceability": {
                "source_change": "not_relevant",
                "changed_python_files": [str(source_file)],
                "documentation_gap": "none",
                "validation_result": "not_run",
                "workflow_result": "not_relevant",
            },
        }

    doc_file.parent.mkdir(parents=True, exist_ok=True)
    expected_doc = _doc_content_for_endpoints(endpoints)
    existing = doc_file.read_text(encoding="utf-8") if doc_file.exists() else ""
    gap = "missing" if not existing else "outdated"

    if existing.strip():
        security = _security_check(existing)
        if not security["safe"]:
            return {
                "status": "security_failed",
                "reason": "sensitive material detected in documentation",
                "validation": validate_documentation(doc_file, endpoints),
                "security": security,
                "traceability": {
                    "source_change": "relevant",
                    "changed_python_files": [str(source_file)],
                    "documentation_gap": gap,
                    "validation_result": "not_run",
                    "workflow_result": "security_failed",
                },
            }

        normalized_existing = existing.replace("\r\n", "\n").strip()
        normalized_expected = expected_doc.replace("\r\n", "\n").strip()
        if normalized_existing == normalized_expected:
            validation = validate_documentation(doc_file, endpoints)
            return {
                "status": "unchanged",
                "reason": "documentation already matches the API definition",
                "validation": validation,
                "security": security,
                "traceability": {
                    "source_change": "relevant",
                    "changed_python_files": [str(source_file)],
                    "documentation_gap": "none",
                    "validation_result": "passed",
                    "workflow_result": "unchanged",
                },
            }

        validation = validate_documentation(doc_file, endpoints)
        if validation["valid"]:
            gap = "none"
            return {
                "status": "unchanged",
                "reason": "documentation already matches the API definition",
                "validation": validation,
                "security": security,
                "traceability": {
                    "source_change": "relevant",
                    "changed_python_files": [str(source_file)],
                    "documentation_gap": gap,
                    "validation_result": "passed",
                    "workflow_result": "unchanged",
                },
            }

        if _is_malformed_existing_document(existing):
            return {
                "status": "validation_failed",
                "reason": validation["reason"],
                "validation": validation,
                "security": security,
                "traceability": {
                    "source_change": "relevant",
                    "changed_python_files": [str(source_file)],
                    "documentation_gap": gap,
                    "validation_result": "failed",
                    "workflow_result": "validation_failed",
                },
            }

    updated_doc = _replace_generated_api_block(existing, expected_doc) if existing.strip() else expected_doc
    doc_file.write_text(updated_doc, encoding="utf-8")
    validation = validate_documentation(doc_file, endpoints)
    security = _security_check(doc_file.read_text(encoding="utf-8"))

    if not security["safe"]:
        return {
            "status": "security_failed",
            "reason": "sensitive material detected in documentation",
            "validation": validation,
            "security": security,
            "traceability": {
                "source_change": "relevant",
                "changed_python_files": [str(source_file)],
                "documentation_gap": gap,
                "validation_result": "failed" if not validation["valid"] else "passed",
                "workflow_result": "security_failed",
            },
        }

    if not validation["valid"]:
        return {
            "status": "validation_failed",
            "reason": validation["reason"],
            "validation": validation,
            "security": security,
            "traceability": {
                "source_change": "relevant",
                "changed_python_files": [str(source_file)],
                "documentation_gap": gap,
                "validation_result": "failed",
                "workflow_result": "validation_failed",
            },
        }

    return {
        "status": "synced",
        "reason": "documentation synchronized and validated",
        "validation": validation,
        "security": security,
        "traceability": {
            "source_change": "relevant",
            "changed_python_files": [str(source_file)],
            "documentation_gap": gap,
            "validation_result": "passed",
            "workflow_result": "synced",
        },
    }
