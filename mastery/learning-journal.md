# Learning Journal

The journal records changes in understanding, not a list of completed tickets. Add one
dated entry for each substantial laboratory cycle and one monthly synthesis.

## Entry template

### Date and subject

**Assistance level:** `L0` / `L1` / `L2` / `L3` / `L4` / `L5`<br>
**Safety level:** `S0` / `S1` / `S2` / `S3` / separately authorized<br>
**Repositories and commits:**<br>
**Model assistance used:**

#### What I believed before

State the mental model and predictions before inspection or execution.

#### Evidence inspected

List source symbols, tests, runtime records, and references.

#### What I can now explain

Explain the mechanism without relying on labels such as “agent,” “memory,” or
“orchestrator” unless their behavior is defined.

#### Where I was wrong

Record incorrect predictions and why they failed.

#### Design decision

State alternatives, chosen path, constraints, and rejected options.

#### Implementation and test evidence

Link commits, fixtures, traces, and experiment results.

#### Remaining uncertainty

Identify untested behavior, assumptions, and next falsification step.

#### Teach-back questions

Write three questions another engineer should be able to answer.

## Initial entry: Architectural reconnaissance

### 2026-10-25 — What the system actually is

**Assistance level:** `L0`<br>
**Safety level:** `S0`<br>
**Evidence:** [`ARCHITECTURAL_RECONNAISSANCE_2026-10-25.md`](../architecture/ARCHITECTURAL_RECONNAISSANCE_2026-10-25.md)

#### Current lesson

Invariance Research is a hybrid distributed system. PostgreSQL-backed deterministic
control loops coordinate specialized model and non-model workers; Bulletproof owns
native scientific execution; the Bible owns institutional rules and as-built claims;
Mission Control projects operational state. No single LLM is the orchestration brain.

#### Important correction

A running service, successful task, or visible activity item is not equivalent to a
terminal scientific backtest. Likewise, a scientifically valid result does not grant
capital authority.

#### Remaining uncertainty

The founder's independent command of the task lifecycle, context construction,
distributed recovery, and reviewer-independence assumptions must be established by
the diagnostics rather than inferred from prior delivery.
