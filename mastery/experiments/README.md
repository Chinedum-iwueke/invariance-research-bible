# Mastery Experiment Registry

## Required record

Every experiment receives an immutable ID and records:

- question and falsifiable hypothesis;
- architecture under test;
- deterministic and/or simpler baseline;
- task dataset and provenance;
- controlled model, tool, budget, and environment variables;
- primary and secondary metrics;
- sample rationale;
- failure and stop criteria;
- artifact and environment manifest;
- results, uncertainty, anomalies, and negative findings;
- conclusion and decision; and
- independent reproduction status.

## Initial proposed experiments

| ID | Question | Status | Registry owner |
|---|---|---|---|
| `MASTERY-EXP-001` | Can two engineers reconstruct the same task from current telemetry? | Proposed | Founder |
| `MASTERY-EXP-002` | Does a specialized research-agent path outperform one well-tooled agent? | Proposed | Founder |
| `MASTERY-EXP-003` | Does typed plan compilation prevent duplicate or invalid graph materialization? | Proposed | Founder |
| `MASTERY-EXP-004` | Does the hybrid control plane converge under duplicate, delay, crash, and restart? | Proposed | Founder |
| `MASTERY-EXP-005` | Which scheduler maximizes verified terminals per constrained resource? | Proposed | Founder |

Results belong under `evaluations/experiment-results/` and remain visible when the
hypothesis is rejected.
