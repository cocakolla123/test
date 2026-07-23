# Terminal-Bench 2 Harbor Task Repair

This repository contains the corrected `dynamo/log-report` Terminal-Bench 2 task in [`log-report/`](./log-report).

The task parses `/app/access.log` and produces `/app/report.json` with:

- `total_requests`
- `unique_ips`
- `top_path`

## Defects repaired

- Changed `artifacts` from an incorrect string/path to the top-level array `["/app/report.json"]`.
- Pinned the approved Python base image by SHA-256 digest.
- Removed the leaked `environment/solution_hint.py` from the agent build context.
- Replaced the gameable existence-only verifier with three tests aligned one-to-one with the instruction criteria.
- Updated `tests/test.sh` to write `/logs/verifier/reward.txt` and `/logs/verifier/ctrf.json` without installing anything at verification time.
- Rewrote `instruction.md` with an absolute output path, exact JSON schema, and numbered success criteria.

## Verification

Run from the repository root with Docker and Harbor installed:

```bash
harbor run -p log-report -a oracle
harbor run -p log-report --agent nop
```

Verified locally on macOS with Docker Desktop and Harbor:

| Agent | Trials | Exceptions | Reward | CTRF summary |
|---|---:|---:|---:|---|
| `oracle` | 1 | 0 | `1.0` | 3 passed, 0 failed |
| `nop` | 1 | 0 | `0.0` | 0 passed, 3 failed |

The GitHub Actions workflow also runs both Harbor commands and validates their reward and CTRF outputs.
