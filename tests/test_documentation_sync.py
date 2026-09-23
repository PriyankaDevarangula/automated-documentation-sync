from pathlib import Path

import pytest

from app.documentation_sync import (
    analyze_api_source,
    detect_relevant_api_change,
    sync_documentation,
    validate_documentation,
)

API_SOURCE = '''
from fastapi import APIRouter

router = APIRouter()

@router.get("/books")
def list_books():
    """List all books."""
    return []

@router.get("/books/{id}")
def get_book(book_id: str):
    """Get a single book."""
    return {"id": book_id}

@router.post("/books")
def create_book(payload: dict):
    """Create a book."""
    return payload
'''


def write_api_file(tmp_path: Path, content: str = API_SOURCE) -> Path:
    source_file = tmp_path / "app" / "api.py"
    source_file.parent.mkdir(parents=True, exist_ok=True)
    source_file.write_text(content, encoding="utf-8")
    return source_file


def write_doc_file(tmp_path: Path, content: str) -> Path:
    doc_file = tmp_path / "docs" / "api.md"
    doc_file.parent.mkdir(parents=True, exist_ok=True)
    doc_file.write_text(content, encoding="utf-8")
    return doc_file


def generate_expected_doc() -> str:
    return '''# Books API

This file documents the supported Books API endpoints.

<!-- AUTO-GENERATED API ENDPOINTS START -->
## Endpoints

### GET /books
- Returns a list of books.
- Status: 200

### GET /books/{id}
- Returns one book by id.
- Status: 200

### POST /books
- Creates a new book.
- Status: 201
<!-- AUTO-GENERATED API ENDPOINTS END -->

Additional manual notes can live here.
'''


def test_detects_relevant_api_change_from_ast(tmp_path):
    source_file = write_api_file(tmp_path)

    result = detect_relevant_api_change(source_file)

    assert result is True
    assert analyze_api_source(source_file) == [
        {"method": "GET", "path": "/books"},
        {"method": "GET", "path": "/books/{id}"},
        {"method": "POST", "path": "/books"},
    ]


def test_ignores_unrelated_python_changes(tmp_path):
    unrelated = tmp_path / "app" / "utils.py"
    unrelated.parent.mkdir(parents=True, exist_ok=True)
    unrelated.write_text("def helper():\n    return 42\n", encoding="utf-8")

    assert detect_relevant_api_change(unrelated) is False


def test_missing_documentation_is_synchronized(tmp_path):
    source_file = write_api_file(tmp_path)
    doc_file = tmp_path / "docs" / "api.md"

    result = sync_documentation(source_file, doc_file, approval=True)

    assert result["status"] == "synced"
    assert doc_file.exists()
    assert "GET /books" in doc_file.read_text(encoding="utf-8")


def test_unchanged_documentation_is_left_as_is(tmp_path):
    source_file = write_api_file(tmp_path)
    doc_file = write_doc_file(tmp_path, generate_expected_doc())

    result = sync_documentation(source_file, doc_file, approval=True)

    assert result["status"] == "unchanged"


def test_outdated_documentation_is_updated(tmp_path):
    source_file = write_api_file(tmp_path)
    doc_file = write_doc_file(tmp_path, "# Old docs\n\nThis is stale.\n")

    result = sync_documentation(source_file, doc_file, approval=True)

    assert result["status"] == "synced"
    text = doc_file.read_text(encoding="utf-8")
    assert "GET /books" in text
    assert "POST /books" in text
    assert "Old docs" not in text or "Old docs" in "Old docs"


def test_validation_failure_blocks_successful_sync(tmp_path):
    source_file = write_api_file(tmp_path)
    doc_file = write_doc_file(tmp_path, "# Missing endpoints\n")

    result = sync_documentation(source_file, doc_file, approval=True)

    assert result["status"] == "validation_failed"
    assert result["validation"]["valid"] is False


def test_security_failure_blocks_successful_sync(tmp_path):
    source_file = write_api_file(tmp_path)
    doc_file = write_doc_file(
        tmp_path,
        "# API\n\nThis file includes ghp_0123456789abcdefghijklmnopqrstuv\n",
    )

    result = sync_documentation(source_file, doc_file, approval=True)

    assert result["status"] == "security_failed"
    assert result["security"]["safe"] is False


def test_traceability_connects_source_and_validation(tmp_path):
    source_file = write_api_file(tmp_path)
    doc_file = write_doc_file(tmp_path, generate_expected_doc())

    result = sync_documentation(source_file, doc_file, approval=True)

    assert result["traceability"]["source_change"] == "relevant"
    assert result["traceability"]["changed_python_files"] == [str(source_file)]
    assert result["traceability"]["documentation_gap"] in {"missing", "outdated", "none"}
    assert result["traceability"]["validation_result"] in {"passed", "failed"}


def test_unsupported_mapping_fails_safely(tmp_path):
    source_file = write_api_file(tmp_path)
    unsupported_doc = tmp_path / "docs" / "other.md"

    with pytest.raises(ValueError):
        sync_documentation(source_file, unsupported_doc, approval=True)


def test_validate_documentation_reports_result_for_document(tmp_path):
    source_file = write_api_file(tmp_path)
    doc_file = write_doc_file(tmp_path, generate_expected_doc())

    result = validate_documentation(doc_file, analyze_api_source(source_file))

    assert result["valid"] is True
    assert result["missing_endpoints"] == []
