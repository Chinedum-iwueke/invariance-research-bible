# Implementation Reference Register

| System | Reference | Required pin | Audit status | Claim boundary |
|---|---|---|---|---|
| Bulletproof BT | `https://github.com/Chinedum-iwueke/bulletproof_bt` | `ba2a0314817607c5c79d604a0846e008c14379c2`, inspected 2026-08-08 | Audit complete with recorded upstream failures and environment limits | Current behavior is limited to inspected code, schemas, documentation, and recorded checks at this commit; target integration is a separate claim class. |
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
