# Fixed Terminal-Bench 2 task: `dynamo/log-report`

This directory contains the repaired Harbor task.

## Validation

The task was validated locally by:

- parsing `task.toml` with Python's TOML parser;
- running `solution/solve.sh` against the provided access log and confirming all three verifier tests pass;
- deleting `/app/report.json` and confirming all three verifier tests fail;
- compiling both Python files and syntax-checking both shell scripts.

Docker and Harbor were not available in the execution environment used for this repair, so the two official harness commands must still be run on a machine with Docker and Harbor installed:

```bash
harbor run -p log-report -a oracle
harbor run -p log-report --agent nop
```

Expected rewards are `1` for the oracle and `0` for the no-op agent.
