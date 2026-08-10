# Implementation Reference Register

| System | Reference | Required pin | Audit status | Claim boundary |
|---|---|---|---|---|
| Bulletproof BT | `https://github.com/Chinedum-iwueke/bulletproof_bt` | `ba2a0314817607c5c79d604a0846e008c14379c2`, inspected 2026-08-08 | Audit complete with recorded upstream failures and environment limits | Current behavior is limited to inspected code, schemas, documentation, and recorded checks at this commit; target integration is a separate claim class. |
| Hermes Swarm Control Plane | `https://github.com/Chinedum-iwueke/swarm-control-plane` | `f8524e5f891e1bf07927d03826208ed291f508ac`, inspected 2026-08-10 | Research and worker surfaces audited; focused tests passed; production topology not requalified | Current claims cover inspected source, migrations, tests, and previously recorded pilots, not continuous service reliability. |
| Invariance public application and deployment repository | `git@github.com:Chinedum-iwueke/invariance_research.git` | `234ebb0337a27166a81aa8727259bd00ce0d1614`, baseline only on 2026-08-10 | Identity and deployment surface noted; application implementation not exhaustively audited | No application feature or production-readiness claim is made from this baseline. |
| Invariance Research Bible | This repository | Filesystem edition dated 2026-08-09; commit SHA when versioned | Corpus baseline complete | Markdown is canonical; source PDFs remain migration evidence |

For every implementation reference, record repository identity, commit, dependency lock where available, inspection date, inspected surfaces, tests run, unavailable/private material, and discrepancies between documentation and behavior.

## Bulletproof BT audit record

- **Repository:** [Chinedum-iwueke/bulletproof_bt](https://github.com/Chinedum-iwueke/bulletproof_bt)
- **Pinned commit:** [`ba2a0314817607c5c79d604a0846e008c14379c2`](https://github.com/Chinedum-iwueke/bulletproof_bt/commit/ba2a0314817607c5c79d604a0846e008c14379c2), committed 2026-08-08 15:27:33 UTC
- **Inspection date:** 2026-08-08
- **Packaging baseline:** project version `0.1.0`; Python `>=3.11`; direct dependencies declared in `pyproject.toml`; no lock file was used as audit evidence.
- **Inspected surfaces:** root README, source tree, test tree, JSON schemas, documentation, configuration examples, orchestration tree, research contracts, public API modules, commit diff, and selected engine, data, execution, risk, portfolio, artifact, experiment, validation, and live-readiness implementations.
- **Inventory at the pin:** 843 Python files, 347 test modules, 23 JSON schemas, and 117 documentation files.
- **Checks:** Python 3.12 byte-compilation of `src`, `tests`, and `schemas` passed. A focused 55-test set covering engine smoke, execution, accounting and cost reconciliation, strict higher-timeframe no-lookahead, delayed-order margin reservation, order-side consistency, audit harness, portfolio engine, Bybit retry behavior, and live controls passed in 4.51 seconds. Full collection found 1,077 tests but initially stopped on 35 errors: 33 PyArrow-dependent collection paths, one missing `jsonschema` dependency, and one repository test fixture with a mutable dataclass default under Python 3.12. `jsonschema` was installed. A broad `--continue-on-collection-errors` run was interrupted after 267.51 seconds because an integration case ceased producing progress; at that point 135 tests passed, 7 failed, and 34 collection errors remained. The 7 failures reproduced in 3.63 seconds. Two independent hash-verified PyArrow downloads truncated near 11 MB and failed published-wheel hash verification; integrity checks were not bypassed. Ruff installation was stopped after prolonged transfer, so no lint result is claimed. QG-011 assesses fidelity of this audit record, not upstream suite passage.
- **Unavailable material:** private branches, private services, venue credentials, live accounts, proprietary datasets, and production operating evidence were not available. The audit therefore proves neither live profitability nor production fitness.

### 2026-08-10 validation and data-lake addendum

- **Audit host:** Linux `5.15.0-185-generic` x86_64; system Python 3.10.12; Bulletproof audit virtual environment Python 3.11.15, pytest 9.0.2; Git 2.34.1; Node 24.14.0; Docker 29.4.3.
- **Working tree boundary:** `src/bt/research_data/jobs/materialize.py` was already modified locally and was not changed by this audit.
- **Compile:** `.venv/bin/python -m compileall -q src schemas` passed in 2.44 seconds.
- **Focused validation:** 50 engine, execution, accounting, resampling, deterministic artifact, run-contract, truth-validation, and portfolio tests passed in 2.85 seconds.
- **Bounded collection:** `.venv/bin/python -m pytest --collect-only -q` did not finish within 120 seconds and emitted no completed collection report. The earlier 1,077-test collection and its recorded failures remain the latest completed broad inventory; no full-pass claim is made.
- **Lake scope:** Read-only inspection covered directory conventions and schemas/aggregates from instrument, coverage, fetch-state, stable-universe, and volatile-membership manifests. It did not exhaustively scan raw rows or certify point-in-time correctness. Safe findings are in [Book V Appendix D](../books/book-05-bulletproof-bt-laboratory/appendices/d-research-data-lake-audit.md).
- **Integrity:** No dependency checksum was bypassed; no lake file was mutated; no raw or sensitive sample was added to the Bible.

## Hermes Swarm and Research Intelligence audit record

- **Repository pin:** `f8524e5f891e1bf07927d03826208ed291f508ac` on `main`, inspected 2026-08-10. A pre-existing `.gitignore` modification was not changed.
- **Inspected surfaces:** agent/task/governance/research models, schemas, routes, services and migrations; restricted worker policies, workspaces, executors, memory bridge and API client; daily research service; role-package and deployment documentation; M1-M15 validation records; Mission Control and Telegram architecture.
- **Validation:** backend application byte-compilation passed. With a mode-0600, audit-only placeholder PostgreSQL secret file (no production credential), 28 focused registry, knowledge, intelligence, role, and daily-research tests passed in 3.17 seconds. Eleven worker research experiment, memory bridge, and memory-sync tests passed in 1.11 seconds.
- **Verified current/partial capabilities:** authenticated agents and leases; capability/machine/risk/workflow policies; worktree isolation; lifecycle/audit events; approvals and supervision; immutable source/snapshot/hypothesis/experiment/trial/result/review/decision records; document/chunk ingestion; lexical knowledge and similar-hypothesis search; retrieval evaluations; domain profiles and intelligence-run records; bounded read-only Bulletproof memory export; daily program scheduling.
- **Consequential boundaries:** document/chunk storage is not the complete scientific-object model; search is not a production hybrid retrieval/citation-replay system; graph and belief services are absent; comprehensive protected-evidence policy, corpus prompt-injection evaluation, projection rebuild/restore proof, and journal surveillance are targets. Daily questions currently rotate through the static approved program mandate; `awaiting_brief` means the cycle has not yet been linked to a registered hypothesis/task.
- **Deployment boundary:** Historical VM1/VM2/Mac pilot documents were inspected as recorded evidence. Live services, credentials, backups, and production recovery were not exercised in this audit, so their present health is `unknown` here.

## BASE-001 implementation addendum

The machine-verifiable baseline contract was added at control-plane commit `92e01fb70441e31b753e606636f13acb3d8d3351` and Bulletproof commit `5a70e9857b2ec617b794fc1661f91dbd8a148da9`. These commits add evidence tooling and do not supersede the behavioral audit pins above. Exact acceptance results and inherited failures are recorded in [BASE-001 Completion Evidence](../plans/evidence/BASE-001.md).

## BASE-002 implementation addendum

The canonical identity contract was added at control-plane commit `d26484f1da3f73697b4748326912c9879b05fef1` and Bulletproof commit `45790daaa62d8c8737317c0a869099b5747781c6`. [ADR-0005](../architecture/adrs/0005-canonical-identity-and-compatibility.md) is authoritative for ownership, alias, immutability, version-negotiation, deprecation, and rollback semantics. Acceptance results are recorded in [BASE-002 Completion Evidence](../plans/evidence/BASE-002.md).

## RI-001 implementation addendum

The canonical evidence object kernel was added at control-plane commit `0322b7429616f0deb453dbcca08575d0359f1b13`. The implementation extends ADR-0005 with a distinct `object_schema_version`, covers all thirteen required object classes, and adds authenticated immutable APIs, lineage, audit, access, and object-store boundaries. Exact acceptance and migration-rehearsal results are recorded in [RI-001 Completion Evidence](../plans/evidence/RI-001.md).

## RI-002 implementation addendum

Quarantined scientific ingestion and structural recovery were added at control-plane commit `4cf32f54bbb3787fb17fc08eabcb0da3cd4ca596`. The implementation retains digest-addressed source artifacts, applies strict type, active-content, malware, expansion, injection, offline OCR, and confidence gates, and atomically publishes canonical source, edition, artifact, and scientific objects only after validation. Exact test, rejection, coordinate-replay, and PostgreSQL migration evidence is recorded in [RI-002 Completion Evidence](../plans/evidence/RI-002.md).

## RI-003 implementation addendum

Canonical hybrid retrieval and citation replay were added at control-plane commit `55d40357e82a2cbdd2181acf7097742589e6966f`. The implementation builds disposable projections for exact identity/text, lexical terms, deterministic local vectors, and canonical lineage neighbors, combines declared channels using deterministic reciprocal-rank fusion, and re-authorizes every result against its canonical object before returning text or coordinates. Exact relevance, access, staleness, client, replay, and PostgreSQL rehearsal evidence is recorded in [RI-003 Completion Evidence](../plans/evidence/RI-003.md).

## RI-004 implementation addendum

Institutional contradiction, negative-result, belief, episode, and frozen-dossier services were added at control-plane commit `d26f6a5`. The implementation preserves opposition comparability and immutable review history, separates valid negative evidence from invalid attempts, versions belief revisions through canonical supersession, publishes shared episodes, freezes digest-bound dossiers with exact citation replay paths, and exposes a read-only Mission Control inspector. Exact contract, access, replay, and PostgreSQL rehearsal evidence is recorded in [RI-004 Completion Evidence](../plans/evidence/RI-004.md).

### Verified implementation facts

1. `BacktestEngine` implements a bar-driven loop connecting a historical feed, universe, strategy, risk engine, execution model, portfolio accounting, audit hooks, and artifact writers.
2. Core event types enforce timezone-aware UTC timestamps. Data validation checks required columns, ordering, duplicates, OHLC consistency, and related contract conditions; resampling tests exercise closed-bucket higher-timeframe visibility.
3. Risk and execution are separate modules. The risk path resolves stops, position size, notional and margin constraints, and rejection reasons; the execution path models fills and costs from explicit configuration.
4. The classic engine owns one strategy, one risk engine, one execution model, and one portfolio per run. A separate `portfolio_engine` runs isolated strategy sleeves, aggregates portfolio artifacts, applies allocation and coordinator checks, and exposes demo/live-readiness entry points.
5. The portfolio live-readiness runner requires explicit confirmation for `live` mode, persists state, and emits lifecycle events. Its inspected `run_once` path does not route an order through the declared execution-adapter protocol; it is not evidence of complete live portfolio execution.
6. Required run artifacts include resolved configuration, decisions, fills, equity, trades, performance, bucket performance, and run status. Benchmark and other diagnostics are conditional. Artifact manifests record presence and schema metadata.
7. Deterministic serialization is implemented for selected JSON outputs. End-to-end tests compare repeated outputs after excluding explicitly variable manifest fields. Accordingly, “identical outputs” is a scoped semantic guarantee, not byte identity for every file in a run directory.
8. Experiment support includes manifest rows, grid expansion and execution, parallel scheduling, hypothesis contracts, dataset extraction, cleanup, and truth validation. Truth checks cover missing evidence, notional and risk consistency, duplicate truth columns, and source timestamps later than entry.
9. The repository contains paper/demo and Bybit execution-runtime surfaces with safety, recovery, idempotency, reconciliation, and adapter tests. Static inspection and unit tests do not substitute for credentialed venue certification or observed production behavior.
10. Public JSON schemas cover research briefs, hypotheses, experiment plans, strategy specifications, lifecycle events, artifact queries, trade episodes, qualification, Pine interchange, and related interfaces. Schema presence does not prove that every producer and consumer is wired end to end.

### Documentation discrepancies and claim boundaries

- The root README labels multi-strategy blending, portfolio allocation engines, and web dashboards out of scope, while the pinned tree contains `bt.portfolio_engine`, portfolio documentation and tests, dashboard-oriented services, and dashboard orchestration. Book V treats the code and tests as evidence of later slices and preserves the README statement as stale scope documentation.
- `docs/multi_strategy_portfolio_plan.md` is written partly as a future plan although the described package, allocation policies, runner, safety gate, artifacts, CLI surfaces, documentation, and focused tests are present. Implemented items are classified from their code and tests, not from the document’s tense.
- The root README’s blanket claims that every layer is deterministic and version-stable are broader than the inspected proof. Several artifacts have explicit schema versions, while other contracts rely on tests and documentation; timestamps and absolute run paths are deliberately variable in manifests.
- Tick-level simulation, order-book modeling, full exchange matching semantics, market impact, and credentialed production operation were not established by the audit. These remain extensions, Book VIII concerns, or deferred capabilities.

### Test discrepancies observed at the pin

- `tests/exec/test_live_startup_gate_phase6.py` cannot collect under Python 3.12 because `_FakeRuntime.portfolio` uses a mutable `_FakePortfolio()` dataclass default instead of `default_factory`.
- `test_alert_serialization_and_file_channel` reads the JSONL file immediately after `AlertEmitter.emit`, but `FileAlertChannel` writes through a buffered `JsonlWriter` without flushing or closing; the observed file is empty at read time.
- The hypothesis runtime-override test expects only the signal timeframe for ordinary strategies, while `l2_h4_prior_day_extreme_traps.yaml` materializes both `1d` and `5m` resamplers.
- Tests reference absent contract files for L1-H10A, L1-H10B, and L1-H2B.
- L1-H1 and L1-H1C grid tests disagree with the checked-in contracts: L1-H1 materializes only `tp_enabled: true`, and L1-H1C materializes 32 variants rather than the asserted 54.
- These failures show drift among tests, hypothesis YAML, and runtime behavior. They limit current claims about repository-wide regression closure but do not negate the separately passing focused engine, accounting, causality, risk-reservation, portfolio, and adapter tests.
