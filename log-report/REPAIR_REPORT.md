# Repair report

The original task had the following authoring defects:

1. `task.toml` declared `artifacts` as a string and pointed to `/app/out.json`, while the task produces `/app/report.json`. It is now a top-level TOML array containing the exact output path.
2. The environment used a floating base image and copied `solution_hint.py` into the agent image. The approved Python base is now pinned by digest, and only `access.log` is copied into the image.
3. The original verifier checked only that the report existed and was non-empty. The replacement verifier checks file creation, exact JSON schema and types, and the exact aggregate values.
4. The original verifier wrote its reward to the wrong path and did not generate CTRF output. `tests/test.sh` now writes both `/logs/verifier/reward.txt` and `/logs/verifier/ctrf.json`.
5. The original instructions did not state the absolute output path or JSON schema. The replacement instructions contain three numbered, unambiguous success criteria, each mapped to one verifier test.
6. Runtime internet access was unnecessary and is now disabled.

Four-way path consistency is `/app/report.json` in `instruction.md`, `task.toml`, `solution/solve.py`, and `tests/test_outputs.py`.
