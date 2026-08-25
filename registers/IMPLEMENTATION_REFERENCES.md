# Implementation Reference Register

| System | Reference | Required pin | Audit status | Claim boundary |
|---|---|---|---|---|
| Bulletproof BT | `https://github.com/Chinedum-iwueke/bulletproof_bt` | `ba2a0314817607c5c79d604a0846e008c14379c2`, inspected 2026-08-08 | Audit complete with recorded upstream failures and environment limits | Current behavior is limited to inspected code, schemas, documentation, and recorded checks at this commit; target integration is a separate claim class. |
| Hermes Swarm Control Plane | `https://github.com/Chinedum-iwueke/swarm-control-plane` | `f8524e5f891e1bf07927d03826208ed291f508ac`, inspected 2026-08-10 | Research and worker surfaces audited; focused tests passed; production topology not requalified | Current claims cover inspected source, migrations, tests, and previously recorded pilots, not continuous service reliability. |
| Invariance public application and deployment repository | `git@github.com:Chinedum-iwueke/invariance_research.git` | `234ebb0337a27166a81aa8727259bd00ce0d1614`, baseline only on 2026-08-10 | Identity and deployment surface noted; application implementation not exhaustively audited | No application feature or production-readiness claim is made from this baseline. |
| Invariance Research Bible | This repository | Filesystem edition dated 2026-08-09; commit SHA when versioned | Corpus baseline complete | Markdown is canonical; source PDFs remain migration evidence |

For every implementation reference, record repository identity, commit, dependency lock where available, inspection date, inspected surfaces, tests run, unavailable/private material, and discrepancies between documentation and behavior.

The living cross-system synthesis is [Book XI — The Engineered Company System](../books/book-11-engineered-company-system/README.md). That book may summarize only evidence recorded here or in a linked completion/validation record; it is descriptive and does not create authority.

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

## BASE-003 implementation addendum

The Bible requirement ledger inventories all 169 chapters and 31 appendices, retains 1,075 exact normative statements with stable source-derived identities, maps them to accountable owners and the complete engineering package catalog, and derives a digest-bound zero-orphan coverage report. A strict local validator and GitHub Actions workflow reject missing authority files, newly unmapped statements, stale digests, duplicate IDs, unknown packages, missing or false evidence, unsupported deferrals, unreviewed records, circular dependencies, orphan requirements/packages, and stale reports. Exact extraction is machine-assisted and all requirement dispositions remain `planned`; changing a disposition requires domain review and separate evidence. Acceptance results are recorded in [BASE-003 Completion Evidence](../plans/evidence/BASE-003.md).

## BT-001 implementation addendum

Bulletproof commits `51e60a270bfb71351465f4b87f08ea0eca63876d` and
`8bdb68869870e9ad78f57fadb54d1881f4008bad` close the
recorded Python 3.11 collection and contract drift without introducing strategy logic
or a second engine. The commit adds a bounded dependency lock, scoped collection,
deterministic CI shards, restored historical contracts for still-implemented
strategies, durable alert output, compatibility for legacy and namespaced data paths,
and semantic determinism normalization. The declared matrix collected 1,234 tests and
completed with 1,207 passed and 27 explicitly skipped. Exact root causes, commands,
counts and claim boundaries are recorded in [BT-001 Completion Evidence](../plans/evidence/BT-001.md).

## RI-001 implementation addendum

The canonical evidence object kernel was added at control-plane commit `0322b7429616f0deb453dbcca08575d0359f1b13`. The implementation extends ADR-0005 with a distinct `object_schema_version`, covers all thirteen required object classes, and adds authenticated immutable APIs, lineage, audit, access, and object-store boundaries. Exact acceptance and migration-rehearsal results are recorded in [RI-001 Completion Evidence](../plans/evidence/RI-001.md).

## RI-002 implementation addendum

Quarantined scientific ingestion and structural recovery were added at control-plane commit `4cf32f54bbb3787fb17fc08eabcb0da3cd4ca596`. The implementation retains digest-addressed source artifacts, applies strict type, active-content, malware, expansion, injection, offline OCR, and confidence gates, and atomically publishes canonical source, edition, artifact, and scientific objects only after validation. Exact test, rejection, coordinate-replay, and PostgreSQL migration evidence is recorded in [RI-002 Completion Evidence](../plans/evidence/RI-002.md).

## RI-003 implementation addendum

Canonical hybrid retrieval and citation replay were added at control-plane commit `55d40357e82a2cbdd2181acf7097742589e6966f`. The implementation builds disposable projections for exact identity/text, lexical terms, deterministic local vectors, and canonical lineage neighbors, combines declared channels using deterministic reciprocal-rank fusion, and re-authorizes every result against its canonical object before returning text or coordinates. Exact relevance, access, staleness, client, replay, and PostgreSQL rehearsal evidence is recorded in [RI-003 Completion Evidence](../plans/evidence/RI-003.md).

## RI-004 implementation addendum

Institutional contradiction, negative-result, belief, episode, and frozen-dossier services were added at control-plane commit `d26f6a5f94e83291f2150c4785f45f203746c35a`. The implementation preserves opposition comparability and immutable review history, separates valid negative evidence from invalid attempts, versions belief revisions through canonical supersession, publishes shared episodes, freezes digest-bound dossiers with exact citation replay paths, and exposes a read-only Mission Control inspector. Exact contract, access, replay, and PostgreSQL rehearsal evidence is recorded in [RI-004 Completion Evidence](../plans/evidence/RI-004.md).

## RI-005 implementation addendum

Corpus security, observability, backup, and recovery services were added at control-plane commit `c7f9462a16c76de7fdcc7e60faf314c0dac7a56c`. The implementation treats content and metadata as non-authoritative data, emits bounded security findings without protected material, exports aggregate corpus metrics and explicit SLO state, creates digest-bound portable metadata backups, refuses restore over a populated project, reconstructs derived retrieval projections, repairs stale queue state, and records accountable digest-bound recovery evidence. Exact adversarial tests, migration results, citation replay, and measured PostgreSQL 17 RPO/RTO are recorded in [RI-005 Completion Evidence](../plans/evidence/RI-005.md).

## RI-006 implementation addendum

Governed scientific surveillance was added at control-plane commit `3cdeedbd48bace2e3309b171ed0f52897be68188`. The implementation registers rights-aware HTTPS feed allowlists, records digest-bound success and failure receipts, preserves corrections and retractions, rejects instruction-bearing abstracts, compares novelty against canonical RI memory, produces bounded technique briefs and questions, records append-only approval-required routing events, freezes weekly digests, and exposes read-only Mission Control provenance replay. Exact contract, migration and isolated rehearsal evidence is recorded in [RI-006 Completion Evidence](../plans/evidence/RI-006.md).

## RI-007 implementation addendum

Existing-corpus migration and continuous synchronization were introduced in control-plane PR 29, with operational recovery and duplicate/remediation fixes through PRs 31-33. The source supplies a coverage ledger, digest-idempotent legacy Hermes and Mac inbox reconciliation, bounded Bulletproof-memory synchronization, projection rebuilding, and replay validation without importing the raw Bulletproof lake. As of 2026-08-13 the founder-inbox reconciliation is still running; source completion is recorded, but production completion remains gated on a retained coverage manifest with zero unexplained failures. Detailed evidence belongs to the control-plane `docs/ri-007-validation.md` record.

## RI-008 implementation addendum

Typed knowledge-graph, projection-graph, context-pack and cognitive-tool services were implemented at control-plane commit `d90f472` in PR 34. The source defines typed scientific predicates, temporal validity, canonical provenance and access filtering, deterministic graph rebuilds and queries, contradiction/trial-family overlays, citation-bearing context packs, deterministic calculator/tool receipts, and a read-only Mission Control graph inspector. Validation recorded 224 backend and 44 Mission Control tests. Merge, VM2 migration, live-corpus graph rebuild and digest-bound pilot evidence were not re-observed for this snapshot, so no live-deployment claim is made.

On 2026-08-14 VM2 was observed at migration head `9b3e6f8a2c10` with a live graph of 623,729 nodes and 1,097,688 edges under manifest digest `e44e13f0c955cddcd09f1cb5054914ace1e79f4514116b6f15ac0654028cfeb9`. The deterministic mean tool produced receipt digest `e52d51227a71bef3ece9e429d8444f3f761db9616e7fab2c839cbba4629b1511`. The citation/context pilot then reproduced a production-scale parameter-limit defect before creating its context receipt. Control-plane commit `e9b3db4` bounds traversal by frontier and adds regression coverage; deployment and replay of that fix remain the final RI-008 gate.

## RI-009 implementation addendum

Domain curriculum and institutional-brain evaluation source was added at control-plane commit `e9b3db4`. It binds curricula to canonical source/evidence identities and exact corpus/graph digests, validates acyclic prerequisite maps and quality rubrics, executes held-out retrieval cases, and retains measured citation, opposition, abstention, leakage and coverage evidence. The full backend suite passed 234 tests and Mission Control passed 44 tests. The migration head is `c4a8e2d71f30`. Production migration and a passing live systematic-research curriculum dossier remain separate evidence gates.

On 2026-08-14 systematic-research curriculum `6470d401-da23-440c-8c48-42d3820b7614` was production-qualified. Evaluation `1.0.1` retained complete measured retrieval, citation, opposition, abstention and topic coverage with zero cross-domain leakage after the failed `1.0.0` result drove explicit confidence/no-answer calibration. RI-011 evaluation `1.0.2` later reproduced those measures after the latency architecture changed.

## RI-010 implementation addendum

Evidence-memory consolidation, decay, lawful deletion and supersession were added at control-plane merge `63855851677b8b0ec0cd9a20159bf45e70bcfaa8`, with the clean-room response-contract correction at `ada05ecf86123c7aed9a820e96e586e8279079a1`. The implementation records a materialized lifecycle state plus immutable lifecycle, consolidation, deletion and impact evidence; requires digest equality for consolidation; propagates declared successors transactionally; makes retraction and expiry reversible; enforces retention holds and independent deletion approval; tombstones protected payloads without erasing identity or lineage; excludes inactive evidence from retrieval and graph projections; invalidates stale projections; and preserves lifecycle records through corpus backup schema `corpus-backup-v1.1.0`. PostgreSQL 17 migration and authenticated clean-room HTTP evidence passed. VM2 migrated to `a4e7c9d21f60`, its rebuilt API was healthy, and the protected authenticated production pilot passed all eight checks on 2026-08-21. Exact live dossier and projection evidence is recorded in [RI-010 Completion Evidence](../plans/evidence/RI-010.md).

## RI-011 implementation addendum

Production-scale retrieval optimization was deployed at control-plane merge `2801e4b7aefccda286487f8ae77641c6857e4f7e` and Alembic head `f1a6c8d42e70`. It replaces request-time corpus hashing with trigger-maintained freshness epochs/digests, applies authorization before indexed candidate generation, bounds hydration and graph expansion, exposes stage telemetry, limits concurrent searches, and preserves model-independent RI-009 calibration. The live 623,375-object benchmark passed at 564.253 ms warm p95 and 1,228.084 ms concurrent p95; evaluation `1.0.2` remained qualified. Exact failed-run, SLO, evaluation, rollback and test evidence is recorded in [RI-011 Completion Evidence](../plans/evidence/RI-011.md).

## RI-009B implementation addendum

Control-plane PRs 48-51 introduced twelve pinned Research Bible curricula, separate support/opposition evaluation queries, immutable aggregate portfolios and constant-time graph freshness epochs. Production portfolio `e9b393e0-4eee-4768-ada2-d3db2be5ffa0` version `1.0.1` qualified all twelve domains under digest `ec1393d67ea1259cec6288023f30ea4a9acf47547566ce73a7c74665a0224f49`. The initial `1.0.0` gap portfolio is retained. Exact scope, metrics, digests, test totals and limitations are recorded in [RI-009B Completion Evidence](../plans/evidence/RI-009B.md).

## BT-008 implementation addendum

Control-plane PR #90 (`0447493ce334768798aa43a630ff87f8d2961d40`) and Bulletproof
PR #271 (`4b2b0a2d3af17264a9e88c38bec85afb22de2d1c`) implement the governed laboratory
publication boundary. Hermes atomically binds registered trials and reviewed results
to canonical run, result, review, decision and dossier evidence, then records current
graph/retrieval and Bulletproof-memory consumer receipts through a replayable state
machine. Bulletproof validates the BT-003 bundle before submission and records only an
idempotent derived memory row. Exact tests, authority limits and rollback behavior are
recorded in [BT-008 Completion Evidence](../plans/evidence/BT-008.md).

## BT-009 implementation addendum

Bulletproof PR #272 (`3cc4a49ee5189894f132a315d8adcc8f9edaa3dc`) and
control-plane PRs #91-#98 (`35001f5492f33b3ac976bf2c18e7827081faf05a`) compose
the founder-approved proposal, prospective registry, native classic execution, truth
gate, atomic bundle, independent review, canonical publication, current projections and
Bulletproof-memory receipt. The 2026-08-24 VM2 replay completed bridge
`649158a6-10a4-5ae6-9872-00e0ff1e4aa4` and publication
`5cbafb3e-f3e7-5f1a-9678-278368d971fe` across 16 registered variants. The selected
result was negative and retained; production and capital authority remained prohibited.
Exact operational receipts are recorded in
[BT-009 Completion Evidence](../plans/evidence/BT-009.md).

## SHADOW-001 implementation addendum

Bulletproof commits `b2b84bc904cfda65b5237dd61051b1a6fa4bf5d4` and
`58cbc5ac974080f572d58c1990558ca47043d984` add the digest-pinned, hash-chained
prospective shadow journal, deterministic replay verifier, execution-artifact wiring,
failure fixtures and bounded pilot. Evidence commit `a6a399a` retains the sealed
journal and report. The report digest is
`745862c57511dacc02278fd6ec8a7243e28dea36c3389df653ab4c7b937d991f`; the journal
digest is `3a4dc409783061fae9e6aeb735dea96be4bb408fe084f916541e4514a66a4c46`.
The pinned Python 3.11 suite passed 1,279 tests with 27 expected skips. This evidence
proves bounded no-capital journal/replay behavior, not continuous feed deployment,
venue certification, Hermes publication or capital authority.

## RI-012 and RI-013 implementation addendum

Incremental founder-inbox reconciliation, checkpoint/resume and finalize-only behavior
were deployed before this snapshot. The settled 2026-08-22 run recorded 267 usable
canonical or duplicate-backed files and two terminal quarantines, then rebuilt retrieval
and graph projections once. Control-plane PR 75, merged as `8268bd4`, added the bounded
iterative recovery controller, independent parser/OCR sequence and advisory-only Codex
identity. Its deterministic scanner and normal publication path retain authority.

Control-plane PRs 76-78, represented on `main` at
`603b074c1b191c5228ca6676fe739f4eb6afbbfd`, added the read-only blocked-artifact
register, excluded subordinate rejected editions from independent recovery, corrected
the Mission Control lifecycle response envelope and deployed the register to VM2 and
the Mac. The live register returned exactly one `replacement_required` and one
`security_blocked` original. The post-recovery projection recorded 761,444 retrieval
objects and a 762,232-node, 1,331,231-edge graph. Control-plane automated validation at
the register gate passed 283 backend tests and 56 Mission Control tests; changed-file
Ruff and JavaScript syntax checks passed.

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
