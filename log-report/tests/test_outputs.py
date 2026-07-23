import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
EXPECTED_REPORT = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def test_success_criterion_1_report_exists() -> None:
    """Success criterion 1: /app/report.json is created."""
    assert REPORT_PATH.is_file(), "Expected /app/report.json to exist."


def test_success_criterion_2_json_schema() -> None:
    """Success criterion 2: The report is valid JSON with the exact required keys and types."""
    data = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    assert isinstance(data, dict), "report.json must contain one JSON object."
    assert set(data) == set(EXPECTED_REPORT), (
        f"Expected exactly {set(EXPECTED_REPORT)}, found {set(data)}."
    )
    assert type(data["total_requests"]) is int, "total_requests must be an integer."
    assert type(data["unique_ips"]) is int, "unique_ips must be an integer."
    assert type(data["top_path"]) is str, "top_path must be a string."


def test_success_criterion_3_values() -> None:
    """Success criterion 3: The report contains the exact expected values."""
    data = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    assert data == EXPECTED_REPORT, f"Expected {EXPECTED_REPORT}, found {data}."
