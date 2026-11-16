# Implementation Reference Register

## Targeted current pins - 2026-11-16

- Swarm Control Plane: `2e49cd7`, bounded requirements correction and typed dispositions;
  377 targeted backend tests passed; API and both directors deployed on VM2.
- Bulletproof BT: `72dbd592662dc1922e9c144ef69bc58ce5f45af1`, the source bound to R14/R15.
- [Book XI Chapter 12](../books/book-11-engineered-company-system/chapters/12-requirements-recovery-and-current-certification.md)
  provides exact runtime/mandate evidence, links to pinned source and audit scope.
- Public application and unrelated services were not re-audited in this pass.

The following pins are historical audits, not an assertion that production remains
on those revisions. Preserve their results and limitations rather than relabelling
them as checks run at the newer pins.

| System | Reference | Required pin | Audit status | Claim boundary |
|---|---|---|---|---|
| Bulletproof BT | `https://github.com/Chinedum-iwueke/bulletproof_bt` | `ba2a0314817607c5c79d604a0846e008c14379c2`, inspected 2026-08-08 | Audit complete with recorded upstream failures and environment limits | Current behavior is limited to inspected code, schemas, documentation, and recorded checks at this commit; target integration is a separate claim class. |
| Hermes Swarm Control Plane | `https://github.com/Chinedum-iwueke/swarm-control-plane` | behavioral audit `f8524e5f891e1bf07927d03826208ed291f508ac`; AGT-003 implementation `283fc415432fa6a124befa2eaad5c9843ed5fd8e` | Research/worker audit retained; AGT-003 passed 393 backend and 18 worker service tests plus clean PostgreSQL 16 migration | Claims distinguish inspected source, bounded tests, migration rehearsal and separately retained live pilots; no continuous reliability or autonomous self-modification is inferred. |
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

## ML-001 implementation addendum

Bulletproof commits `844306998573046bddc13d8f102eaad828592277`,
`eee98f7` and `8dbfc4eaf9c2243ed5e035df68a4ae1dff05413d` implement the
model bundle, strict temporal split contract, deterministic logistic baseline,
held-out Platt calibration, calibrated inference receipts, content-addressed artifact
store, append-only version lifecycle, activation, snapshot and rollback. Evidence
commit `0c945af` retains both model versions, the registry snapshot and pilot report.
The reproduced model digest is
`5e3b8c80a494aaedb33dd61c8484fb59ed1f89254dec52724ebae82193e175a3`;
snapshot digest is `1d738ee40118551ccfbeb3edabfea609b09a4319958fa55a3ee5772d78c3d605`;
report digest is `7e3f250ffb54d5d6e194ad07cee4a065b2bb614ac8ce52f708b99f398bb5cd69`.
The evidence grants no alpha, order, sizing, promotion or capital authority and does not
claim production inference or useful market prediction.

## PORT-001 implementation addendum

Bulletproof source commit `4eaf836d2b0f9a1de4730b2141847cc7d073e40a` adds the
canonical candidate contract, explicit evidence-registry boundary, exact-overlap
covariance, shared-dependency analysis, uncertainty-aware capacity-capped deterministic
baseline, hard portfolio constraints, named stress evaluation, explainable rejection
and public non-allocation dossier schema. Evidence commit `7e0ab6c` retains the accepted
dossier and missing-overlap, infeasible-capacity and stress-rejection paths. Candidate
set digest is `43a0bd21e8c1286b13e1c4de9010c19580e543cd9b2402cdfc0bb31b2e43b325`;
dossier digest is `3ab51287d89cfdc02a04b4ba1014a85a6716b1a55a086da43d74d4867a3378bd`;
report digest is `98964cfa2fd0afd65208330bf50f6b25c3eff99d9e0faa9723efca0a6843e555`.
The evidence is deterministic and no-capital. It grants no candidate admission,
allocation, sizing, order, execution or self-promotion authority.

## LIVE-001 pre-capital gate addendum

Bulletproof source commit `e6ce17ed9b8e14e23ea54f121f1f448387ae2ecf` adds a
fail-closed live authorization boundary before exchange-adapter construction and
credential resolution. A root-owned mode-`0600` bundle must bind the exact venue,
symbols, execution window, order/loss/gross/duration/freshness limits, canonical
rollback, PORT-001 non-allocation evidence, demo and connector qualification, M8
readiness, kill rehearsal and a separate current approval. Runtime controls reject
stale or future market data and breached envelopes. The full Python 3.11 suite passed
1,304 tests with 27 declared skips. This is source and rehearsal evidence only: no
venue credential was installed, no demo or live order was sent and no signed
micro-live dossier exists. LIVE-001 therefore remains `blocked_before_capital` until
its external prerequisites and serialized capital-bearing acceptance run are real.

## OPS-003 integrated recovery addendum

Control-plane commit `30e6843f42b9e3bc1bd3d01a75a7c913e45b0686` adds a
strict recovery dossier over existing OPS-005, RI-005, projection, lease and
notification mechanisms. It verifies backup/restore identity and isolation, measured
RPO/RTO, restored corpus and derived-state lineage, citation replay, exactly-once stale
lease recovery, deduplicated notification, redacted secret rotation and a
schema-compatible runtime replacement whose canonical task output and fallback both
replay. The 229-test worker suite passes. Deterministic dossier digest
`941a484ee954fe25a8c63bd256e7bd48699ca6cbba1c3486f5d7df8f081f7f71`
records no production resource touched and no production-restore authority.

## PLAT-001 service catalog addendum

Control-plane commits `2d3927355d2cddd8a94c3adb76a5ae9adcfa4c55` and
`74adcf0` add the immutable service-catalog snapshot, activation-history and
reconciliation contracts. Catalog `1.0.0` records 12 services across VM1, VM2 and the
founder Mac and binds ownership, recovery ownership, runtime placement, interfaces,
dependencies, data classes, SLOs and runbooks. Its digest is
`793b67cf1c447887b374df53efe87bfd58bc7281ba839e9cd63402576ff9ef96`.
The deterministic report digest is
`381e1aafd02e20820aaf3b53015f44679b7ba6bf300562db410f1eef5321698a`;
318 non-health backend tests passed. This evidence proves source behavior, not VM2
activation or perfect discovery of an unobserved runtime.

## SEC-001 security assurance addendum

Control-plane merge `b881defaf83f5cf03c2a5884ac0b9a2543aa2537` adds a strict,
versioned threat model covering all 12 PLAT-001 services and deterministic adversarial
fixtures for injection, exfiltration, privilege escalation, supply-chain tampering and
capital-authority mutation. Model digest
`951e49ff0764001c94b6effda37013f45ea81314db342b60494e78387f4ba6b8` and report
digest `db7e75b91110f3a64a27ef28c3b5330a3c7ba0c602bf4883bf84dc0fac816e7a` bind the
retained evidence. Forty-two focused tests and both required GitHub checks pass. The
evidence does not claim external penetration testing or closure of the four recorded
residual risks.

## PLAT-005 unified observability addendum

Control-plane merge `8f552ba0e43144fe4888adc20a7a1f258bc480d7` and migration
`c5e8a2f41d70` add catalog-attributed SLO state, bounded metrics, capacity evidence,
generation-aware alert routing, immutable acknowledgement/silence/recovery events,
Telegram founder delivery and Mission Control status/actions. The source suite passed
323 backend, 37 gateway and 71 Mission Control tests. Retained report digest
`0f525ce1334705c8731b59b6fc909622fa7c7989541fe73262f6bf24c6479ded` records that
production deployment and the intended-environment replay were not part of source
qualification.

## PLAT-002 workload identity addendum

Control-plane PRs #126-#128 add exact-charter/package workload identities, central
wildcard-free scope enforcement, bounded credential rotation, logical secret-policy
rotation/revocation, redacted receipts and independently reviewed reduction-only
emergency access. VM2 runs migration `f3a7c1d92e60` and healthy image
`sha256:0d6be1cde4141e1fba829761e6b3ab1a1e8cd30d01b93e8461a47c22edb1a4d3`.
Fourteen credentials are covered and none are uncovered. The idempotent bootstrap
digest is `1a1cf583746e13a3bedb511f616664460ab4c9702dbbcdba85278c30e90105b0`;
the nine-check live pilot digest is
`ae388619c5987dc231974fa26fc61a5eecd6b749fb02e9efb31f3d26bfcecad0`.
See [PLAT-002 completion evidence](../evidence/PLAT-002.md). No retained record
contains a raw credential or secret value, and no identity grants capital or order
authority.

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

## EXEC-003 venue identity addendum

Bulletproof source commit `ef842db13d2775c2edbf8c372224d4ad9a964814` adds the
effective-dated explicit cross-venue identity producer. Native report SHA-256
`c8d5ab670c7f465a09f86ac8af61d9092086d3ad46713a84d7590302bc4dc438` binds
mapping-schema digest `ae6a8354ad95b94daf036e8f9276ca11727d0989de201e605e98fe2faa14b74c`,
mapping digest `605c8ae33b065ff32861ac2c801743a5d7353c7c81a9bab1d1b8161f8d9872dc`
and producer receipt `082e20bd3f77516d3b2370d601b00ed6f648095313b2897b278f29edbe2008d7`.
Fourteen focused tests, the 1,366-test full suite with 28 declared skips, and Ruff pass.
The source merged through PR #285 as
`6ea7656aa744d4a9356d71854b9727535dec1230`.

Hermes commit `1d01d461208d7cbbfcc3b9d31102a42f2114f965` adds migration
`e4f8b2d05c30`, immutable mapping-schema registration, exact receipt admission and the
cross-repository replay pilot. Its backend suite passes 730 tests with two pre-existing
warnings. No artifact grants allocation, capital, order, promotion or routing authority.
The source merged through PR #224 as
`6477a0bc2b162d8142b6108ae804ecf1bf1ed012`.

On 2026-09-12 VM2 ran migration `e4f8b2d05c30` and healthy image
`sha256:efe6afd82de57d1519dc5ad78564b089e6c372aedb372c82c02054633700f2ad`.
The exact replay registered venue-identity record
`e498a6cc-58c4-4814-8839-b957c6fcb2e7` and quantitative-receipt record
`f9322c93-08f4-4aa9-abc6-348e07b21039`; report digest
`419af24787bdec980d8431d1094a9cf6be97d28486940065d0ebb90179a793e1`
retains two comparison routes and no capital or order authority.

## EXEC-004 idempotent OMS and reconciliation addendum

Bulletproof source commit `b0865ca1d2aa57acac1015d8ba088c34bf0fb2c4` adds the
authoritative command, order, fill and reconciliation producer and merged through PR
#286 as `e7100d9345ef419d0deccdee49bc1c6e4896e610`. The native pilot binds OMS
specification digest `4b102ffd35b8ce6d4b4c506d23028def8ef024ff5e721a2b3563fa86475233e2`,
receipt `4a35c72296052fbb45bce1b3a9dfb70e2a1ae5bcb753f89d19e92fe439fbd72f`,
journal `7d510e212a4f56bc84ffdb4cf48422a5c555d7414793dad36b5032cfe3f84df7`
and reconciliation `ef6435f3213e523f816fde2435365122bd0a66030c4582028f80bcbcbdfe749a`.
The full native suite passed 1,379 tests with 28 declared skips.

Hermes commit `c2604a76bffa271e44630dedbbcea751aa74767c` adds migration
`e5a9c3f16d40`, immutable OMS-schema registration and exact native-receipt admission,
and merged through PR #225 as `cdd6179291ee5acbf3fc08b69a830061a905c398`.
The backend suite passed 734 tests. On 2026-09-12 VM2 ran migration `e5a9c3f16d40`
and healthy image `sha256:63eb575d2329d84cf53be84182e336baeccf8bda5857e8b659f59c8dd0619bd7`.
The exact replay registered schema `2f823ef3-92ad-4199-bc33-b18a99cd5a48` and receipt
record `9e572f47-6fd6-4706-a7d0-79e5dd2e47d5`, retained report digest
`d2346e630f3ac0bcaa665416ee8557f5c96a4d6818e975d8a28eedcf29a412f1` and returned
`submission_allowed: true` after qualified reconciliation. No artifact grants
allocation, capital, order, promotion, routing or cancellation authority.

## EXEC-005 execution-quality calibration addendum

Bulletproof source commit `d6cde7665385732d0f49deafbaac324161da33d9` adds the
point-in-time execution calibration producer and merged through PR #287 as
`97d20db19b81054b729c0fb11a2ca1657aa4c632`. Native receipt
`fc819372f8cedde7a1e4ad99162eb9d2e5d5a59d4432e8f26c7575d9581be434` binds
calibration digest `e1aa6787a920c155159c39f0c56746ae96f3f0826034e6bc22b6ebec540687d9`
and empirical bundle digest `e46c1ea0e0a0e826673496cbe1a023022ee7059db62314c04469b5358d26fbdf`.
Fifteen focused tests and every required CI shard passed. The supported local suite
passed 1,394 tests with 28 declared skips; five volatile-panel failures reproduce in
the untouched EXEC-004 checkout under the same shared environment.

Hermes source commit `7bd40a980d93c22c800f26ed0d217e00798d3385` adds migration
`f6b2d8a47e50`, immutable schema registration and exact native-receipt admission, and
merged through PR #226 as `5906127939090b30a114efdf1d9d243d85fdebde`. Its backend
suite passed 738 tests. VM2 runs the migration and healthy rebuilt image
`sha256:6e2199467f35b38b010d11130d6c2d23f78b674fa5bf2417dad43fd437a39bc7`.
The exact credentialed cross-repository replay registered schema `88d60d24-441c-4019-8c1f-5d3d79cbe761`
and receipt `a08d562a-09bd-465b-86ed-534255fbcc96`, reproduced every native digest and
retained report digest `f061249f89d4823597480491ebf9aa327d70f2dddbba200ce67d617961163fd5`.
No live-stratum qualification or execution authority is inferred from the fixture.

## PORT-004 turnover, cost, capacity and liquidity addendum

Bulletproof source commit `159a79b7ee1bbf19e6208c8b5216fb0046178d44` adds the
authoritative PORT-004 producer and merged through PR #288 as
`ccddacee049dbc97d6bba5912f623a4d8345a8bd`. Native receipt `8c2dc060...` binds
schema `4f2d3384...` and capacity dossier `ef30b343...`. Fourteen focused tests and
all required CI shards passed; the supported local suite passed 1,408 tests with 28
declared skips and the five previously reproduced volatile-panel baseline failures.

Hermes source commit `75ed1eb9cbdae2d128e011d83aae3484747b59b7` adds migration
`a7c3e9b58f60`, immutable schema registration and exact receipt admission, and merged
through PR #227 as `6097eb39a02ad1f6ca0849783d3731d4fc29480d`. Its backend suite
passed 742 tests. VM2 runs healthy image `sha256:5b9d598d6fa1dbaf3a00673b51ff4f5742d90a168379acf1587750f6876b4183`.
The credentialed replay registered schema `1ceb8bc7-49ff-4627-ba15-0a25d978cbe5`
and quantitative receipt `b4999dba-e29d-44d9-9a27-19c3be0bf0c6`, reproduced the
native digests and retained report digest `de5d0965038cca501fd15477951a0e9af1e6f4d8605dccced8ffcb483c8e9edd`.
Deterministic fixture capacity is not a live venue capacity claim or capital authority.

## RISK-003 dynamic risk budget addendum

Bulletproof source commit `f5d80f97b318ba14f84863595cc8e0740dca0de6` adds the
authoritative causal dynamic-budget producer and merged through PR #289 as
`24ea8c5d44a76ed85097a14aacdfdadfb6fc97a6`. Seventeen focused tests, every CI
shard and the full 1,430-test suite with 28 declared skips passed. Native receipt
`e21533c0fa1a2242c16005f4daba206134af5aadb13ea69107789cc4643fde61` binds
schema `bd876f5de05e0a90a06f29ae3db1a29b1e16c736af4dcc5f897afdf31d05b367`
and budget trajectory `6c27f2da9713157cc58ad45f9bda4f4519b24703ff68c74201fdb1d5cf752f0b`.

Hermes source commit `a987a9f` adds migration `b8d4f0c69a71`, immutable policy-schema
registration and exact receipt admission, and merged through PR #228 as
`3d0535787e434837fd8fdcda0049e460401e970d`. Its full backend suite passed 746
tests. VM2 runs that migration and healthy rebuilt image
`sha256:b9dd898a560585c6179217f05175c5a6cb7a5491a77d19291637f3ef392939cc`.
The credentialed replay registered schema `e16641dc-8267-4f0f-9610-99433cc66f83`
and quantitative receipt `261a8c36-2126-4c80-9e52-f8429b15acb1`, reproduced every
native digest and retained report digest
`475d6bcbf40da4a3307c84b0e4f2b88cb01dec6882eea3cc018e208ac4485d9b`.
No RISK-003 artifact grants allocation, capital, order or promotion authority.

## SHADOW-002 prospective monitoring addendum

Bulletproof source commit `8524f95f2fdebdac361c40ce0e990ba26ef35491` adds the
authoritative prospective monitoring producer and merged through PR #290 as
`87645886038ba8803d9540cf602e79da894182ce`. Twenty-five focused tests, every CI
shard and the full 1,451-test suite with 28 declared skips passed. Native receipt
`3a967a39f60b5d36f77645ecfd333b60252a2d50d887534035ab42cf15e071df` binds
schema `1676a85b16c310f8b117c30618e99d0791c7ca8472c9069b008a1b9abf559d4a`,
monitoring dossier `0068cd261e651fa8a290998d669bc7e5a8b16402ee2baf334c11e591a5b09e56`
and SHADOW-001 replay `7b56e39a83529c6a7c1f9be00f8ef583975060b52d9401d4d28eea2454a778d1`.

Hermes source commit `b4bb884f8107258b6d1cb43aac0dced9785f24fc` adds migration
`c9f5a1d72b80`, immutable schema registration and exact receipt admission, and merged
through PR #229 as `6891a1261bb80c1e1fd5c94572a34da7ccc188a4`. Its full backend
suite passed 750 tests. VM2 runs that migration and healthy rebuilt image
`sha256:af2cb3734af40a1d9c39841df42e24e035d903bfe939340f97b97515179f0f87`.
The credentialed replay registered schema `2d5ca3f3-333f-4317-ab73-80c74cd4ae36`
and quantitative receipt `4073a8a1-b652-4edd-b7d0-a61445b95537`, reproduced every
native digest and retained report digest
`8aaa934cc04e40a371966588717790dd3828dddce8cdac881b0e86227dc7e87e`.
It proves deployed fail-closed monitoring, not completion of a sustained genuine
candidate shadow interval or any capital, order or lifecycle authority.

## RISK-004 candidate admission addendum

Bulletproof source `ecad17a36167845c7035b1302847b4455130e045` merged through PR
#291 as `24c25839bcc22178cee1c1bb06153bf1e12c06f8`. Hermes source `17ceffc`
merged through PR #230 as `9b1d68991dfec574769aa54b7ccbf43eddeb75b9`. The full
suites passed 1,458 Bulletproof tests with 28 declared skips and 754 Hermes backend
tests. VM2 runs migration `d1a6b4e83c90`, healthy image
`sha256:060e7cd322a923c168b5f30dca4ee446dd816a63aa84f8ea1447054844e445e6`
and active schema `2b4748c2-3052-4e3b-a706-e17698216324` with digest
`c3740311dcdd619a6b9e9fa2b1cebc3a4be3962beed52a9a9103997b1d424cc6`.
No candidate, allocation or capital decision was created by deployment.

## ALPHA-013 hybrid cognitive-authoring addendum

On 2026-11-09 a production-systemd rehearsal exercised GitHub Copilot CLI as the
primary bounded patch author, with Codex reserved for a correction pass, independent
code review and infrastructure-unavailability fallback. The author ran in a disposable
worktree with shell and network tools denied. The successful rehearsal attested only
`apply_patch`, `glob`, `rg` and `view`,
selected model `gpt-6-luna`, did not invoke fallback and retained report digest
`c972634b810edfeb3019706256fab25fee98336d51bc9f0fbed04becfa5d5879`.

The implementation was merged to `swarm-control-plane` `main` by PR `#426` at commit
`37e6c14335cb28057b9b20a9d0c9f7423a2e135b`. The runtime boundary and validation are
documented in `swarm-control-plane/docs/alpha-013-copilot-hybrid-authoring.md`. No
authoring provider receives merge, scientific-promotion, order or capital authority.
This receipt does not establish installation on a named production machine.
