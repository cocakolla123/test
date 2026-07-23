import json
import re
from collections import Counter
from pathlib import Path

ACCESS_LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")
REQUEST_PATTERN = re.compile(r'"[A-Z]+ (?P<path>\S+) HTTP/\d(?:\.\d)?"')
REQUIRED_KEYS = {"total_requests", "unique_ips", "top_path"}


def expected_report_from_log() -> dict[str, int | str]:
    total_requests = 0
    unique_ips: set[str] = set()
    path_counts: Counter[str] = Counter()

    for raw_line in ACCESS_LOG_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        total_requests += 1
        unique_ips.add(line.split(maxsplit=1)[0])

        match = REQUEST_PATTERN.search(line)
        assert match is not None, f"Verifier could not parse fixture line: {line}"
        path_counts[match.group("path")] += 1

    assert path_counts, "The verifier fixture must contain at least one request."
    return {
        "total_requests": total_requests,
        "unique_ips": len(unique_ips),
        "top_path": path_counts.most_common(1)[0][0],
    }


def test_success_criterion_1_report_exists() -> None:
    """Success criterion 1: /app/report.json is created."""
    assert REPORT_PATH.is_file(), "Expected /app/report.json to exist."


def test_success_criterion_2_json_schema() -> None:
    """Success criterion 2: The report is valid JSON with the exact required keys and types."""
    data = json.loads(REPORT_PATH.read_text(encoding="utf-8"))

    assert isinstance(data, dict), "report.json must contain one JSON object."
    assert set(data) == REQUIRED_KEYS, (
        f"Expected exactly {REQUIRED_KEYS}, found {set(data)}."
    )
    assert type(data["total_requests"]) is int, "total_requests must be an integer."
    assert type(data["unique_ips"]) is int, "unique_ips must be an integer."
    assert type(data["top_path"]) is str, "top_path must be a string."


def test_success_criterion_3_values() -> None:
    """Success criterion 3: The report values correctly summarize /app/access.log."""
    data = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    expected = expected_report_from_log()
    assert data == expected, f"Expected {expected}, found {data}."
