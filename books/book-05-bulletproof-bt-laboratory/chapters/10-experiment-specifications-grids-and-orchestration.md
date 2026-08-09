<a id="b5-c10"></a>
# Chapter 10 — Experiment Specifications, Grids, and Orchestration

An experiment is more than a collection of runs. It is a registered family with a finite search space, execution policy, resource envelope, completion rule, and interpretable history.

## 10.1 Current grid machinery

The pinned experiment package validates experiment configuration, expands parameter grids, encodes parameter assignments, writes and reads manifest rows, executes local grids, supports parallel grid operation, tracks status, shares read-only data plans, controls resources, schedules deterministic waves, and records cleanup.

Each manifest row represents a resolved parameter assignment and status-bearing run attempt. Grid runners write run-status information even around failures so orchestration does not erase unsuccessful branches. Parallel hardening tests cover failure resilience, local overlays, resource controls, causal parity, and deterministic scheduling for their exercised paths.

## 10.2 Search history

The manifest must include every material attempted assignment, not only completed or selected runs. It records proposed order, canonical parameters, trial identity, attempt identity, state transitions, start and finish, worker and environment class, output location, failure taxonomy, and protected-evidence exposure.

Adaptive search adds proposer state, acquisition or selection rule, observations available before each proposal, and stopping decision. A final table of scores cannot reconstruct an adaptive path.

## 10.3 Concurrency

Parallelism may change scientific behavior through random streams, floating reduction order, cache races, resource exhaustion, or inconsistent shared data. Deterministic waves reduce scheduling variability but do not remove every concurrency source.

Workers receive immutable trial specifications and write isolated attempt directories. Shared caches are content-addressed and read-only after publication. The orchestrator alone performs state transitions through compare-and-set or equivalent idempotent semantics. A duplicate delivery must not create a duplicate scientific trial.

## 10.4 Failure and retry

Retry policy classifies transient infrastructure errors separately from deterministic scientific invalidity. A retry preserves the trial identity, receives a new attempt identity, and never overwrites the failed attempt bundle. Repeated deterministic failures stop rather than consume the full budget.

Partial success is not experiment completion unless the registered completion rule permits it. Missing parameter regions can bias selection and must appear in summaries.

## 10.5 Cleanup

The repository contains an experiment cleanup workflow that can extract compact research datasets, retain curated reference runs, prune heavy logs, and optionally remove unretained run folders while writing cleanup audit artifacts. Cleanup changes the evidence surface and therefore requires policy.

The target institution keeps immutable primary evidence for promoted, disputed, anomalous, or representative runs; content-addressed source inputs; compact canonical datasets for the full search; deletion manifests; and retention justification. Dry-run planning precedes deletion. Book X owns storage lifecycle implementation.

> **Laboratory rule B5-LR10 — Scheduling must not select the science**  
> Worker order, retry timing, cache availability, and resource contention may affect elapsed time but must not silently determine which scientific result is retained or reported.

## Source note

Current statements derive from pinned experiment manifest, grid, parallel scheduling, resource-control, shared-data, status, and cleanup modules and their tests. Search interpretation remains in Book IV.
