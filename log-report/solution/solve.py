#!/usr/bin/env python3
import json
import re
from collections import Counter
from pathlib import Path

INPUT_PATH = Path("/app/access.log")
OUTPUT_PATH = Path("/app/report.json")
REQUEST_PATTERN = re.compile(r'"[A-Z]+ (?P<path>\S+) HTTP/\d(?:\.\d)?"')


def main() -> None:
    total_requests = 0
    unique_ips: set[str] = set()
    path_counts: Counter[str] = Counter()

    for raw_line in INPUT_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue

        total_requests += 1
        unique_ips.add(line.split(maxsplit=1)[0])

        match = REQUEST_PATTERN.search(line)
        if match is None:
            raise ValueError(f"Could not parse request path from log line: {line}")
        path_counts[match.group("path")] += 1

    if not path_counts:
        raise ValueError("No requests found in /app/access.log")

    report = {
        "total_requests": total_requests,
        "unique_ips": len(unique_ips),
        "top_path": path_counts.most_common(1)[0][0],
    }
    OUTPUT_PATH.write_text(json.dumps(report) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
