<a id="codex-implementation-backlog"></a>
# Codex Implementation Backlog

**Status:** Executable task packets
**Rule:** One task ID per branch and review unless its packet explicitly permits otherwise

All tasks inherit these constraints: preserve unrelated changes; never commit data/secrets; use migrations, compatibility readers, and typed schemas; do not grant an agent promotion or capital authority; retain negative/failed evidence; run repository-native formatting/tests plus the named acceptance commands; publish a redacted evidence report; and obtain the named reviewer before merge.

Quantitative completion claims additionally inherit the binding
[quantitative computation ownership](../registers/QUANTITATIVE_COMPUTATION_OWNERSHIP.md)
contract. Bulletproof is the sole authoritative producer of market-data-derived,
statistical, ML, RL, portfolio, risk and execution calculations. Hermes may register,
validate, gate, schedule and replay signed receipts, but a Hermes schema, fixture,
registry or API is not sufficient completion evidence. The
[2026-08-28 ownership audit](QUANTITATIVE_OWNERSHIP_AUDIT.md) reopens every packet
whose Bulletproof-native producer and cross-repository receipt replay are absent.

## Current execution snapshot — 2026-08-24

The recently completed tranche is now reconciled across source, evidence and Book XI:

- `UI-003A`, `UI-003B` and `UI-003C` are deployed and production-observed on the Mac;
- `OPS-004` VM1/VM2 probes are active, while correlated-outage detection remains
  explicitly deferred until an independent always-on host is provisioned;
- `OPS-005` is deployed and production-observed on VM2 with two verified generations,
  an isolated restore drill and active persistent timers;
- `BT-001` through `BT-008` are implemented and validated across Bulletproof and
  Hermes; BT-008 adds the canonical publication saga and dual-memory receipt boundary.
  BT-003's compatible Hermes producer extension is also merged. These BT packages are
  source-complete and tested, but no production research run is inferred until the
  governed bridge and walking-skeleton packages exercise them end to end.
- Bulletproof's experimental backtest fast path is deprecated at canonical merge
  `e47f9f210c862a311f2e8b691f8148c393fb5ed0`. Legacy `auto` and `fast_path` values
  resolve to the classic event-driven engine and emit an explicit deprecation receipt.
  Semantics-neutral data IO and post-run batching may remain; no shortcut may alter
  causal visibility, orders, stops, fills, risk, accounting or truth artifacts.

The next laboratory package is `WS-001`. `BT-009` completed its bounded VM2
operational replay on 2026-08-24; `WS-001` remains downstream of
the completed BT-001 through BT-008 contracts and must compose them rather than introduce duplicate
engines, registries or artifact stores.

Bulletproof currently contains Bybit and Binance REST adapters, public/private
stream clients, reconciliation, durable execution artifacts, a simulated shadow
mode, demo configurations and bounded live-canary controls. This is not an
operational claim that adding API keys alone enables safe trading. Bybit demo is
the nearest qualified path; both venues still require current connector evidence,
least-privilege credentials, clock/instrument checks, continuous services,
reconciliation and kill drills. Binance private-stream and continuously running
compiled-strategy parity remain explicit gates. `SHADOW-001`, `EXEC-001..011`,
`DEMO-001` and `LIVE-001/002` own that promotion path.

This backlog is the execution queue, not the sole coverage authority. Every task must
also appear in the [Bible capability coverage plan](BIBLE_CAPABILITY_COVERAGE.md),
which maps all ten volumes and appendices to build packages, dependencies, operating
owners, and acceptance evidence. A capability mentioned only in prose is a planning
defect. CI should eventually reject an implementation-status claim when its coverage
entry has no task, evidence dossier, or explicit deferral.

## Wave 0 — Baseline and identity

### BASE-001 — Machine-verifiable implementation baseline

**Implementation status:** Completed on 2026-08-10. See [BASE-001 completion evidence](evidence/BASE-001.md).

- **Objective/requirement/citations:** Encode repository pins, runtimes, schema inventory, dirty-state guard, and claim vocabulary required by [Book X Chapter 2](../books/book-10-builders-manual/chapters/02-baseline-audit-and-system-boundaries.md) and [Book V Appendix E](../books/book-05-bulletproof-bt-laboratory/appendices/e-requirement-traceability-and-gap-register.md).
- **Repository/files:** Control plane and Bulletproof; new read-only inventory commands plus CI evidence schema.
- **Prerequisites/scope:** None; record, validate, and diff safe metadata only. **Non-goals:** changing dependencies or tests.
- **Data/access:** No raw lake reads beyond manifest metadata; no credentials.
- **Steps/interfaces:** Define `implementation-baseline-v1`; collect pins/runtime/schema/test command metadata; validate; emit digest.
- **Tests/acceptance:** Fixture repos for clean/dirty/missing lock; run schema validation and secret scan.
- **Evidence/rollback/done:** `implementation-baseline.json` and digest; additive removal is rollback; done when repeat collection is stable. **Parallelism/conflicts:** parallel with OPS-001; owns baseline schema. **Reviewer:** architecture owner.

### BASE-002 — Canonical identity and compatibility ADR

**Implementation status:** Completed on 2026-08-10. See [BASE-002 completion evidence](evidence/BASE-002.md) and [ADR-0005](../architecture/adrs/0005-canonical-identity-and-compatibility.md).

- **Objective/requirement/citations:** Map existing Hermes and Bulletproof IDs to the canonical evidence model in [RI Foundation](RESEARCH_INTELLIGENCE_FOUNDATION.md).
- **Repository/files:** Bible ADR plus control-plane schemas/migrations and Bulletproof producer contract.
- **Prerequisites/scope:** BASE-001; specify aliases, version negotiation, immutability, and deprecation. **Non-goals:** data migration or retrieval.
- **Data/access:** Synthetic fixtures only.
- **Steps/interfaces:** Inventory IDs; choose canonical owners; define JSON Schemas/OpenAPI; add compatibility fixtures.
- **Tests/acceptance:** Round-trip old/new records; reject digest mutation and unknown major versions.
- **Evidence/rollback/done:** ADR and compatibility report; rollback retains readers; complete when both repos consume fixtures. **Parallelism/conflicts:** serialized before RI/BT schema work. **Reviewer:** architecture and knowledge authorities.

### BASE-003 — Machine-verifiable Bible requirement ledger

**Implementation status:** Completed on 2026-08-10. See [BASE-003 completion evidence](evidence/BASE-003.md).

- **Objective/requirement/citations:** Convert every normative requirement, invariant, acceptance clause, appendix contract and declared non-goal in all ten volumes into a stable traceability record so planning omissions become test failures.
- **Repository/files:** Bible requirement manifest/schema, extractor/validator, coverage report, CI workflow and implementation/evidence registers.
- **Prerequisites/scope:** BASE-001/002; assign stable requirement IDs and human-review extracted semantics. **Non-goals:** treating keyword extraction as authoritative interpretation or claiming implementation from documentation alone.
- **Data/access:** Repository text and metadata only; no secrets or corpus payloads.
- **Steps/interfaces:** Enumerate chapters/appendices; identify normative statements; record owner, package, dependency, verification, evidence, status and deferral rationale; validate links and uniqueness; calculate coverage by volume and capability.
- **Tests/acceptance:** Missing chapter, unmapped requirement, duplicate ID, nonexistent task/evidence, circular dependency, false completion and stale digest fixtures must fail CI.
- **Evidence/rollback/done:** Signed/digest-bound coverage report with 100% disposition and zero orphan work packages; completion never means all requirements are implemented, only that none are unplanned. **Reviewer:** architecture owner, domain authorities and independent audit reviewer.

## Wave 1 — Research Intelligence foundation

### RI-001 — Evidence object schema kernel

**Implementation status:** Completed on 2026-08-10. See [RI-001 completion evidence](evidence/RI-001.md).

- **Objective/requirement/citations:** Implement source, edition, artifact, scientific object, claim, method, assumption, dataset, run, review, decision, belief, and episode identities from Book III and RI-F1.
- **Repository/files:** Control-plane models/schemas/migrations/services/tests; object-store adapter interface.
- **Prerequisites/scope:** BASE-002; additive schemas and compatibility readers. **Non-goals:** embeddings or UI.
- **Data/access:** Synthetic records and hashes; protected classes represented without payloads.
- **Steps/interfaces:** Migrations; strict schemas; immutable create/read APIs; audit events; access-class hook.
- **Tests/acceptance:** Migration up/down rehearsal, digest/idempotency/authorization/lineage tests, OpenAPI snapshot.
- **Evidence/rollback/done:** Migration and schema-coverage report; rollback only before canonical writes; complete at 100% object contract coverage. **Parallelism/conflicts:** owns canonical tables. **Reviewer:** Knowledge steward and DB reviewer.

### RI-002 — Quarantined scientific ingestion and recovery

**Implementation status:** Completed on 2026-08-10. See [RI-002 completion evidence](evidence/RI-002.md).

- **Objective/requirement/citations:** Implement RI-F2 document recovery with hierarchy, coordinates, tables, figures, equations, citations, confidence, and remediation.
- **Repository/files:** Dedicated ingestion package/worker, object-store adapter, RI APIs.
- **Prerequisites/scope:** RI-001; born-digital plus one scanned fixture. **Non-goals:** broad corpus import.
- **Data/access:** Licensed/public fixtures; sandbox parsers; no network by default.
- **Steps/interfaces:** Quarantine, type/malware scan, extraction, structural/object recovery, validation, atomic publish.
- **Tests/acceptance:** Golden PDF fixtures; corrupted/archive-bomb/active-content/injection cases; coordinate replay.
- **Evidence/rollback/done:** Per-stage ingestion report and retained artifact digests; failed publish leaves quarantine only. **Parallelism/conflicts:** parser adapters parallelize after object schema. **Reviewer:** Librarian and security reviewer.

### RI-003 — Hybrid retrieval and citation replay

**Implementation status:** Completed on 2026-08-10. See [RI-003 completion evidence](evidence/RI-003.md).

- **Objective/requirement/citations:** Deliver RI-F3 exact, lexical, vector, and graph-assisted retrieval with citation replay and compatibility filtering.
- **Repository/files:** RI query service, projection builders, evaluation fixtures, API client.
- **Prerequisites/scope:** RI-001 and RI-002 fixture corpus. **Non-goals:** model-authored final decisions.
- **Data/access:** Enforce access at canonical fetch and projection query.
- **Steps/interfaces:** Build projections; reciprocal-rank or declared fusion; replay endpoint; stale-index detector.
- **Tests/acceptance:** Golden relevance, exact citation, table/equation/figure, access denial, stale rebuild and deterministic filter tests.
- **Evidence/rollback/done:** Versioned evaluation report meeting declared thresholds; drop/rebuild projections for rollback. **Parallelism/conflicts:** lexical/vector builders parallelize. **Reviewer:** Independent Knowledge Evaluator.

### RI-004 — Contradiction, negative-result, belief and dossier services

**Implementation status:** Completed on 2026-08-10. See [RI-004 completion evidence](evidence/RI-004.md).

- **Objective/requirement/citations:** Implement RI-F4/F5 and Book III memory forms.
- **Repository/files:** RI schemas/services, Mission Control dossier view, worker client.
- **Prerequisites/scope:** RI-001/003; supporting/opposing evidence, supersession, frozen dossiers, episodes. **Non-goals:** automatic approval.
- **Data/access:** Redact protected evidence while preserving existence and access reason.
- **Steps/interfaces:** Belief ledger; contradiction edges; dossier compiler; episode publisher.
- **Tests/acceptance:** Negative-result recall, conflicting-edition, belief supersession, dossier freeze and cross-role access tests.
- **Evidence/rollback/done:** Replayed dossier with exact citations and opposing evidence. **Parallelism/conflicts:** owns belief semantics. **Reviewer:** Canon Curator and governance reviewer.

### RI-005 — Corpus security, observability and recovery

**Implementation status:** Completed on 2026-08-10. See [RI-005 completion evidence](evidence/RI-005.md).

- **Objective/requirement/citations:** Implement RI-F6/F7 security controls, SLOs, projection rebuild and restore proof.
- **Repository/files:** Ingestion/query services, telemetry, backups/runbooks, security fixtures.
- **Prerequisites/scope:** RI-002/003. **Non-goals:** production source surveillance.
- **Data/access:** No protected content in logs/traces; synthetic secrets and poison documents.
- **Steps/interfaces:** Policy enforcement, parser limits, injection labels, metrics, backup, rebuild, restore rehearsal.
- **Tests/acceptance:** OWASP-style indirect injection, exfiltration, denial, corrupt projection, lost queue and restore drills.
- **Evidence/rollback/done:** Security evaluation and recovery report with measured RPO/RTO. **Parallelism/conflicts:** observability and security fixtures parallelize. **Reviewer:** Security and SRE owners.

### RI-006 — Governed scientific surveillance

**Implementation status:** Completed on 2026-08-10. See [RI-006 completion evidence](evidence/RI-006.md).

- **Objective/requirement/citations:** Implement RI-F8 feeds, correction/retraction state, novelty, technique briefs, contradictions, and routing.
- **Repository/files:** RI connectors, scheduler, research-program proposal APIs, Mission Control.
- **Prerequisites/scope:** RI-003/004/005; begin with two approved primary feeds. **Non-goals:** auto-adoption or auto-trial.
- **Data/access:** Respect licenses, rate limits, allowlists, and source access classes.
- **Steps/interfaces:** Source registry, fetch receipt, novelty report, alert, proposed question, approval route.
- **Tests/acceptance:** Duplicate, retraction, poisoned abstract, outage, retry/idempotency and provenance-replay fixtures.
- **Evidence/rollback/done:** One weekly digest with citation-replayable candidates and approval events. **Parallelism/conflicts:** connector work parallel. **Reviewer:** Canon Curator and research authority.

### RI-007 — Existing-corpus migration and continuous synchronization

**Implementation status:** Production corpus reconciliation was refreshed on 2026-08-22. The retained founder-inbox ledger classifies all 269 files: 267 are canonical or duplicate-backed usable evidence and 2 remain explicitly quarantined. Governed recovery resolved four additional exceptions without weakening content-security policy; the remaining structurally unreadable Cartea edition requires replacement and paper `2505.22954v3.pdf` remains security-blocked because its extracted content contains a genuine Bash-tool instruction. The continuous Research Ingestion Recovery Steward is active on VM2. See the control-plane `docs/ri-007-validation.md` and `docs/runbooks/ri-007-pdf-recovery.md` records.

- **Objective/requirement/citations:** Move the founder inbox, legacy Hermes documents/chunks, imported prior results, and the bounded Bulletproof memory projection into the canonical RI object model without copying the raw Bulletproof lake.
- **Repository/files:** Mac Mission Control inbox, control-plane ingestion/reconciliation services, VM1 memory bridge, corpus inventory and migration tools.
- **Prerequisites/scope:** RI-002/003/005; content-addressed backfill and incremental sync. **Non-goals:** silent deletion, unrestricted filesystem crawling, or treating derived summaries as primary evidence.
- **Data/access:** Preserve source artifact, edition, coordinates, extraction provenance, classification, access class and quarantine state; never commit corpus payloads.
- **Steps/interfaces:** Inventory; digest reconcile; edition/duplicate resolution; canonical publish; projection build; incremental watch/refresh; failure remediation; supersession/deletion propagation; Bulletproof projection registration.
- **Tests/acceptance:** Mixed PDF/book fixtures, duplicate editions, renamed files, corrupt scans, interrupted migration, replay after restore, idempotent refresh and access denial.
- **Evidence/rollback/done:** Corpus coverage manifest with every eligible source classified as canonical, quarantined, duplicate, superseded or excluded; exact citation replay; restore/rebuild proof. **Reviewer:** Librarian, Knowledge Evaluator and security reviewer.

### RI-008 — Knowledge graph, projection graph and cognitive tool services

**Implementation status:** Completed and production-validated on 2026-08-14. The VM2 graph contains 623,729 nodes and 1,097,688 edges under manifest digest `e44e13f0c955cddcd09f1cb5054914ace1e79f4514116b6f15ac0654028cfeb9`. Canonical citation replay returned the exact object digest, a five-item context pack was retained under digest `d0b97135f0846c6222ac14dc5230aa0cef4a879bca4899249fafeaa3b9eac2cb`, and deterministic tool receipt `e8852557-5258-43e8-ba0c-bfdb47eef148` was retained under digest `e52d51227a71bef3ece9e429d8444f3f761db9616e7fab2c839cbba4629b1511`. The replay-path defect was corrected and deployed at control-plane merge commit `722ab7f05817be8ebfdeac9a20c84a6fd015fca4`. The RI-008 pilot now reuses a current projection and allows a bounded 30-minute rebuild instead of unconditionally rebuilding with a ten-minute client deadline.

- **Objective/requirement/citations:** Complete Book III Chapters 14 and 16: typed scientific edges, temporal/provenance/access-aware projections, graph traversal, deterministic calculators, context assembly and tool receipts.
- **Repository/files:** Canonical edge registry, graph projection builder/query API, deterministic scientific-tool service, Mission Control graph explorer.
- **Prerequisites/scope:** RI-003/004/007. **Non-goals:** graph database as a second source of truth or model-authored canonical facts.
- **Data/access:** Canonical IDs remain authoritative; protected nodes and inference paths are filtered before traversal.
- **Steps/interfaces:** Edge vocabulary and validity intervals; projection manifests; neighborhood/path/subgraph queries; claim-method-dataset-result lineage; contradiction and trial-family overlays; calculator registry; citation-bearing context packs.
- **Tests/acceptance:** Direction/temporal/access semantics, stale projection, cyclic graph, contradictory path, provenance replay, deterministic tool parity and rebuild tests.
- **Evidence/rollback/done:** Rebuildable graph whose sampled paths replay to canonical objects and whose answers include evidence/tool receipts. **Reviewer:** Canon Curator, architecture owner and independent evaluator.

### RI-009 — Domain curriculum, corpus quality and institutional brain evaluation

**Implementation status:** Completed and production-qualified on 2026-08-14. Curriculum `6470d401-da23-440c-8c48-42d3820b7614` version `1.0.0` is bound to the live systematic-research corpus and graph. Evaluation `1.0.0` was retained as a negative result after exposing missed supporting evidence and false answers to an unknown identifier. Evidence-confidence calibration was then implemented and deployed at control-plane merge commit `eb196744a08e3726e2426b4c66c286274388936b`: vector similarity cannot establish confidence alone, explicit identifiers must match, candidate calibration is bounded, and retrieval reports confidence and abstention explicitly. Immutable evaluation `1.0.1` (`b039949e-9973-4556-8296-a1daa1a8613b`) passed retrieval recall, citation fidelity, opposition recall, abstention accuracy and topic coverage at 100%, with zero cross-domain leakage. Its record digest is `61391fdbb3f5f9fcf5867baedaf0ac42785b573bd9bfa6531ecd86c9ef57f605`; curriculum readiness is `true`. See the control-plane `docs/ri-009-validation.md` record.

- **Objective/requirement/citations:** Make the senior quantitative researcher demonstrably grounded in approved domains through curriculum dossiers, coverage maps, retrieval benchmarks and belief calibration rather than persona prompting.
- **Repository/files:** Domain profiles, curriculum registry, evaluation sets, corpus-quality dashboards, agent context policy.
- **Prerequisites/scope:** RI-007/008. **Non-goals:** claiming expertise from upload volume or allowing sources to grant authority.
- **Steps/interfaces:** Domain ontology; prerequisite map; source-quality rubric; coverage/gap analysis; adversarial question sets; citation and contradiction scoring; curriculum versioning; decay/review cadence.
- **Tests/acceptance:** Held-out domain questions, opposing-evidence recall, abstention, stale/retracted source, cross-domain leakage and source-poisoning tests.
- **Evidence/rollback/done:** Versioned domain-readiness dossier meeting declared retrieval, citation, opposition, calibration and abstention thresholds. **Reviewer:** Senior research authority and Independent Knowledge Evaluator.

### RI-010 — Memory consolidation, decay, lawful deletion and supersession

**Implementation status:** Completed and production-qualified on
2026-08-21 at control-plane merges `63855851677b8b0ec0cd9a20159bf45e70bcfaa8`
and `ada05ecf86123c7aed9a820e96e586e8279079a1`, migration
`a4e7c9d21f60`. The PostgreSQL 17 rehearsal and authenticated HTTP pilot passed
consolidation, automatic supersession, retraction/restore, explicit decay,
retention-hold enforcement, independent lawful deletion, tombstone/audit
retention, dossier impact reporting, stale-projection rejection, rebuild, and
backup/restore preservation. Mission Control is deployed on Mac. On 2026-08-21
VM2 migrated to `a4e7c9d21f60`, the rebuilt API was observed healthy, and the
root-protected authenticated pilot passed all eight lifecycle checks. Retrieval
and graph projections rebuilt current and their live digests are retained in
`plans/evidence/RI-010.md`.

- **Objective/requirement/citations:** Make institutional memory lifecycle-aware without erasing audit history: superseded, retracted, corrected, expired and lawfully deleted material must stop influencing active retrieval while retained lineage proves what changed and why.
- **Repository/files:** Canonical evidence lifecycle schemas/services, corpus synchronization, retrieval and graph projection builders, dossiers, Mission Control memory operations.
- **Prerequisites/scope:** RI-004/005/007/008. **Non-goals:** silent deletion, mutable historical dossiers, or model-decided retention policy.
- **Data/access:** Retention authority and legal basis are explicit; protected payload deletion preserves non-sensitive tombstone, digest, event and dependency evidence.
- **Steps/interfaces:** Lifecycle state machine; consolidation receipts; supersession/retraction propagation; retention holds; lawful deletion workflow; projection invalidation; dossier and belief impact reports.
- **Tests/acceptance:** Duplicate consolidation, corrected edition, retraction, protected deletion, active hold, stale projection, restore and replay fixtures.
- **Evidence/rollback/done:** A digest-bound lifecycle dossier proves active retrieval excludes invalid evidence while immutable decisions and authorized audit lineage remain replayable. **Reviewer:** Knowledge steward, security/privacy authority and independent evaluator.

### RI-009B — Full Research Bible domain curriculum expansion

**Implementation status:** Completed and production-qualified on 2026-08-14. Twelve independently evaluated domains are frozen in portfolio `e9b393e0-4eee-4768-ada2-d3db2be5ffa0` version `1.0.1`, bound to corpus digest `7c5b7b86763eb993f88c69ea026929aeb4930b21f3d9a1fcbf23c71ef7b1696c` and graph manifest `e44e13f0c955cddcd09f1cb5054914ace1e79f4514116b6f15ac0654028cfeb9`. Every domain passed retrieval, citation, opposition, abstention and coverage at `1.0` with zero leakage; aggregate readiness is an all-domain conjunction. Immutable portfolio `1.0.0` retains the initial regime/risk misses, and `1.0.1` records their calibrated held-out re-evaluation. Graph readiness was changed from repeated whole-corpus hashing to a trigger-maintained epoch with a fail-closed one-time digest bootstrap. See [RI-009B Completion Evidence](evidence/RI-009B.md).

- **Objective/requirement/citations:** Extend the qualified systematic-research curriculum from its first live slice across every Research Bible competency required for institutional quantitative work: statistical inference, causal reasoning, time-series methods, backtesting validity, selection bias, portfolio construction, risk, market microstructure, regime analysis, execution, data quality, reproducibility and governance.
- **Repository/files:** Versioned curriculum specifications, evidence anchors, prerequisite graph, held-out evaluation sets, coverage/readiness service and Mission Control curriculum dossier.
- **Prerequisites/scope:** RI-009 qualified baseline; RI-011 performance work may proceed in parallel. **Non-goals:** declaring expertise from source counts, using training-set questions as evaluation, or granting execution authority from curriculum readiness.
- **Data/access:** Each domain binds only canonical authorized evidence; protected sources remain access-filtered before retrieval and evaluation.
- **Steps/interfaces:** Publish the domain taxonomy and prerequisites; register source/evidence coverage; write supporting, opposing, unknown-identifier and cross-domain-leakage cases; evaluate each domain independently; compute an aggregate readiness matrix without allowing strong domains to hide weak ones.
- **Tests/acceptance:** Held-out cases for every domain, minimum evidence diversity, citation replay, opposition recall, calibrated no-answer behavior, stale/retracted sources and adversarial cross-domain leakage. Each domain must meet declared thresholds independently.
- **Evidence/rollback/done:** Immutable per-domain evaluations and one digest-bound aggregate dossier show the senior quantitative researcher is grounded across the Bible while unqualified domains remain explicitly unavailable. **Reviewer:** Senior quantitative research authority, Independent Knowledge Evaluator and domain specialists.

### RI-011 — Production-scale retrieval and model-independent reranking evaluation

**Implementation status:** Completed and production-qualified on 2026-08-14. Control-plane merge `2801e4b7aefccda286487f8ae77641c6857e4f7e` and migration `f1a6c8d42e70` deploy transactionally maintained freshness epochs/digests, authorization-scoped GIN/indexed candidate generation, bounded model-independent fusion, stage telemetry and eight-request admission control. The live 623,375-object `hybrid-retrieval-v1.1.0` projection measured 564.253 ms warm p95 against a 2,000 ms SLO and 1,228.084 ms concurrent p95 against a 5,000 ms SLO, with at most 530 hydrated candidates. Immutable evaluation `1.0.2` (`bb427da9-3fe4-4d25-a98d-e0b7e3fa08a4`) retained 100% retrieval recall, citation fidelity, opposition recall, abstention accuracy and topic coverage with zero cross-domain leakage. Benchmark digest: `091826f949083cad09c2caee688b2a04af5e63f4e10490b853e7af7a32c3fe63`; evaluation digest: `addc87a5aa691cc414f66d8a68434860776a836fc6f95ba5afe238564469a603`. See control-plane `docs/ri-011-validation.md`.

- **Objective/requirement/citations:** Preserve the qualified RI-009 behavior while making retrieval, readiness and evaluation usable at representative production scale under declared latency and resource SLOs.
- **Repository/files:** Corpus freshness state, retrieval query service, database indexes/candidate generation, reranker benchmarks, readiness service, telemetry and load fixtures.
- **Prerequisites/scope:** RI-003/005/007/009. **Non-goals:** weakening confidence/abstention thresholds, rebuilding the canonical corpus, introducing an LLM judge, or changing evidence authority.
- **Data/access:** Authorization filters execute before candidate content leaves storage; benchmarks contain no protected payloads or credentials.
- **Steps/interfaces:** Replace per-request full-corpus hashing with transactionally maintained freshness epochs/digests; perform indexed database-side candidate generation; retain bounded model-independent calibration; cache only digest-bound safe metadata; expose stage latency and candidate counts; add cancellation and concurrency limits.
- **Tests/acceptance:** Re-run immutable RI-009 cases plus broad inference, backtesting-validity, selection-bias, portfolio, microstructure and regime fixtures; benchmark cold/warm p50/p95, concurrent requests, stale writes, cancellation and fail-closed authorization. Declare SLOs before optimization and do not pass by shrinking the corpus.
- **Evidence/rollback/done:** A production-scale benchmark shows the declared latency/resource SLOs pass without regression from evaluation `1.0.1`; rollback restores the calibrated implementation and preserves all evaluation records. **Reviewer:** Independent Knowledge Evaluator, database/performance reviewer and security owner.

### RI-012 — Incremental founder-inbox synchronization and resumability

**Implementation status:** Implemented and locally tested on 2026-08-21; merge,
Mac deployment, first-index bootstrap and measured warm no-change refresh remain
required before production qualification. Mission Control now has a versioned private
index, stat-first unchanged-file fast path, content-digest rename deduplication,
atomic per-file checkpoints, exclusive refresh locking, retryable non-canonical
entries, live `sync-status`, complete cached reconciliation inventory and
change-gated projection rebuilds.

- **Objective/requirement/citations:** Make founder-inbox synchronization proportional to the changed batch rather than total historical corpus size, while preserving RI-002 quarantine, RI-005 recovery, RI-007 reconciliation and RI-010 lifecycle authority.
- **Repository/files:** Mission Control inbox synchronizer/configuration/CLI/tests, RI-007 runbook, Book XI Research Intelligence chapter.
- **Prerequisites/scope:** RI-007 and RI-010. **Non-goals:** moving or deleting founder files, weakening scanning/recovery, parallel OCR without capacity admission, or treating the local index as canonical evidence.
- **Data/access:** The private `0600` index stores file metadata, digests and API evidence identifiers but no source payloads or credentials. The API and canonical PostgreSQL evidence kernel remain authoritative.
- **Steps/interfaces:** Stat `(path,size,mtime_ns,ctime_ns)`; skip unchanged canonical entries; hash changed/new paths; reuse canonical receipts by digest after rename; upload only a true delta; checkpoint atomically after each file; persist projection invalidation across interruption; resume safely; retry quarantined/failed entries; reconcile the complete current inventory; rebuild retrieval/graph projections once only when canonical content changed; expose scanned/remaining/count status. Removed inbox paths remain visible as superseded inventory while canonical evidence is retained, so removal alone does not rebuild projections.
- **Tests/acceptance:** Unchanged refresh causes zero ingestion calls and zero projection rebuilds; renamed duplicate causes zero upload; interrupted run retains completed receipts; overlapping refresh is rejected; changed/new and quarantined files remain processable; removed files disappear from the current inventory; index permissions are `0600`; warm no-change benchmark over the live Mac inbox completes within 10 seconds excluding control-plane reconciliation latency.
- **Evidence/rollback/done:** Retain first bootstrap and second warm-refresh reports, API request counts, projection decision, index mode, interruption/resume transcript and full Mission Control test result. Rollback removes only the local derived index and restores full digest-idempotent scanning; canonical evidence and sync ledgers remain unchanged. **Reviewer:** Research Intelligence owner, performance reviewer and security owner.

### RI-013 — Bounded iterative ingestion recovery controller

**Implementation status:** Implemented and locally validated on 2026-08-22. Production deployment, dedicated Codex recovery login, role-package promotion and live terminal receipts for the two retained quarantines remain required before production qualification.

- **Objective/requirement/citations:** Make quarantine handling self-progressing through a finite set of independently validated recovery methods while preserving every scanner finding, original artifact and publication gate.

- **Repository/files:** Recovery controller, PDF structural/PDFium/OCR adapters, recovery worker, role package, systemd unit, RI-007 recovery runbook and Book XI.
- **Prerequisites/scope:** RI-002/005/007/012. **Non-goals:** scanner suppression, model-authored publication, unbounded retry, source deletion, arbitrary repair commands or automatic redaction.
- **Data/access:** Codex receives only bounded filenames, media type, stage/reason codes and method history. It receives no artifact bytes, credentials, database session, scanner controls or publication interface. Its dedicated credential is not shared with engineering or founder-planning agents.
- **Steps/interfaces:** Attempt ledger; allowlisted structural repair, independent parser and offline OCR; strict advisory schema; deterministic method validation; normal ingestion replay; terminal classification; founder-action and provenance-redaction proposal; inbox reconciliation.
- **Tests/acceptance:** Malformed/unsafe Codex advice falls back safely; no advice can publish or suppress a finding; methods run at most once; corrupt Cartea fixture reaches `replacement_required`; genuine tool-instruction fixture reaches `security_blocked`; a recovered edition publishes only through the normal pipeline; receipts retain every attempt and digest.
- **Evidence/rollback/done:** Full backend/worker tests pass, VM2 role attestation is active, both retained quarantines have terminal receipts, and Mission Control shows founder actions without counting either artifact as usable. Rollback disables Codex advice and preserves deterministic recovery plus all receipts. **Reviewer:** Research Intelligence owner, security reviewer and independent ingestion evaluator.

### RI-014 — Scientific representation fidelity and mathematical semantics

- **Status (2026-08-24):** Planned after a production audit found that publication proves bounded extraction and coordinate replay, not complete semantic fidelity. The current kernel stores equations, tables and figures as typed scientific objects with text, page/line coordinates, extraction method and confidence; it does not yet provide semantic equation trees, scoped symbol definitions, units/dimensions or multi-parser agreement.
- **Objective/requirement/citations:** Make the representation of equations, symbols, tables, figures and cross-references measurable and replayable so an accepted artifact cannot be described as fully understood merely because text extraction passed a confidence floor.
- **Repository/files:** Scientific-ingestion schemas and pipeline; canonical evidence objects; parser/OCR adapters; equation/table/figure normalizers; symbol, definition, unit and cross-reference graph edges; fidelity fixtures and operator review UI; Book XI.
- **Prerequisites/scope:** RI-001..003, RI-008 and RI-013. Preserve original bytes and current scientific objects, then add versioned derived representations for Unicode-normalized text, LaTeX/MathML-style equation ASTs where recoverable, symbol scopes, units, table cell grids, figure captions and in-document references. **Non-goals:** silently repairing an uncertain symbol, claiming mathematical equivalence from OCR text alone, or allowing an LLM to publish canonical formulae without deterministic validation.
- **Tests/acceptance:** Use born-digital, scanned and adversarial golden documents containing Greek letters, subscripts/superscripts, fractions, integrals, matrices, piecewise definitions, units, multi-page tables and caption references. Compare independent parsers and rendered source regions; require exact or explicitly tolerance-bounded replay, uncertainty at the token/cell/expression level, dimensional checks where applicable and quarantine/manual review on material disagreement. Measure precision/recall by object class and publish a corpus fidelity manifest.
- **Evidence/rollback/done:** Retain source-region images, parser outputs, normalized representations, disagreement findings, symbol/unit lineage and deterministic digests. Rollback removes only the new derived representation version. Done requires held-out fidelity thresholds and zero silent material equation/table mutation in the acceptance corpus. **Reviewer:** quantitative research, scientific-ingestion, security and independent verification owners.

### RI-015 — Institutional intelligence truth and reasoning evaluation

- **Status (2026-08-24):** Planned. Current retrieval is hybrid exact/lexical, a deterministic hashed-vector baseline and explicit graph-neighbor expansion; curricula test bounded topic coverage and replay, but these do not prove comprehensive semantic understanding or reliable multi-hop scientific reasoning.
- **Objective/requirement/citations:** Continuously measure what Hermes can retrieve, relate, calculate, cite and abstain from across the live corpus, and prevent UI labels such as `qualified` or `ready` from exceeding the evidence.
- **Repository/files:** Versioned held-out evaluation suites; curriculum and projection services; Research Copilot; graph cognitive tools; calibration/no-answer scoring; Mission Control readiness and limitation surfaces; Book XI.
- **Prerequisites/scope:** RI-009B, RI-011 and RI-014. Add domain-stratified hidden questions for direct citation, formula and table retrieval, symbol disambiguation, cross-document synthesis, contradiction, temporal supersession, negative results and multi-hop relationship reasoning. **Non-goals:** grading prose style, using self-reported LLM confidence as evidence, or treating corpus coverage as reasoning competence.
- **Tests/acceptance:** Score citation entailment, source fidelity, answer completeness, unsupported-claim rate, abstention calibration, formula/table accuracy, multi-hop path validity and latency against independent gold labels. Evaluate after every material corpus/projection/model change; fail readiness closed on stale or regressed suites; expose per-domain strengths, blind spots and representative failures without leaking hidden answers into prompts.
- **Evidence/rollback/done:** Retain immutable evaluation manifests, model/runtime identity, corpus/projection digests, item-level reviewer evidence and regression history. Rollback restores the prior evaluator while preserving failing evidence. Done requires declared thresholds across every Bible domain and explicit `not demonstrated` states wherever evidence is absent. **Reviewer:** senior quantitative researcher, statistical reviewer, adversarial auditor and founder/operator.

### RI-016 — Incremental derived-state orchestration and freshness closure

- **Status (2026-08-24):** Planned from live behavior. A changed founder-inbox batch currently performs one full retrieval rebuild; a direct UI upload performs the same rebuild immediately; unchanged refreshes skip it. The path does not rebuild the knowledge graph or rerun curriculum evaluations, leaving graph and brain-readiness surfaces stale. Retrieval and graph builders both replace their full derived tables rather than applying a delta.
- **Objective/requirement/citations:** Make canonical corpus publication invalidate, schedule, rebuild and evaluate every dependent derived state exactly once, incrementally where correctness can be proven, with durable progress and a single atomic freshness receipt.
- **Repository/files:** Corpus epoch/change ledger; retrieval and graph projectors; curriculum evaluator; ingestion/inbox/upload finalizers; operation ledger integration; Mission Control freshness state machine; recovery and rollback runbook.
- **Prerequisites/scope:** RI-012, RI-014/015 and OPS-007. Coalesce a bounded batch into one dependency DAG: canonical publication, retrieval delta/full fallback, graph delta/full fallback, affected-domain curriculum evaluation, portfolio readiness and terminal receipt. **Non-goals:** accepting a faster path without equivalence proof, hiding stale state during rebuild, or blocking canonical publication on a derived-view failure.
- **Tests/acceptance:** Prove no-change causes zero work; one added, changed, superseded, retracted and deleted object update exactly the affected rows; batch upload coalesces once; interruption resumes from durable phase receipts; concurrent publications converge; incremental output digest equals a clean full rebuild; affected curricula rerun while unaffected curricula retain valid receipts; failure remains visibly stale with retry evidence.
- **Evidence/rollback/done:** Retain before/after epochs, changed-object sets, full-versus-incremental digest parity, phase timings, resource use, curriculum impact map and UI replay. Rollback selects the current full rebuild path and preserves canonical evidence. Done requires projection and curriculum freshness to converge automatically after every accepted corpus change without manual commands. **Reviewer:** Research Intelligence, database/performance, curriculum and independent correctness owners.

## Wave 1 — Agent reliability in parallel

### OPS-001 — Approval and readiness race closure

**Implementation status:** Completed and production-activated on 2026-08-14 at control-plane merge commit `05ae2a9b4ab05113297437f1357808314595124f`. VM2 migration `d8b4f1a72c90` provides the durable founder-notification outbox. Approval gates are digest- and generation-bound, dependency-blocked gates remain waiting, successful Telegram delivery is acknowledged, failed delivery remains retryable, and stale gates/readiness messages are superseded. Approval emits `task_ready` and wakes supervised reconciliation in the same transaction. After the gateway restart, the fresh process remained active without new errors and reconciled 16 historical approval records to `waiting` with zero actionable notifications, preventing the former notification flood.

- **Objective/requirement/citations:** Eliminate missed readiness windows, duplicate approval floods, and manual reruns described by M2.
- **Repository/files:** Supervisor, Telegram gateway, proposal/approval services, worker daemon tests.
- **Prerequisites/scope:** BASE-001; durable outbox, deduplication key, readiness signal, bounded reconciliation. **Non-goals:** new task types.
- **Data/access:** No password or token in messages/logs.
- **Steps/interfaces:** Approval outbox; acknowledgement; task-ready event; supervisor wakeup; stale-message supersession.
- **Tests/acceptance:** Approve-before/after-poll races, five pending approvals, restart, duplicate delivery, expired link, lease loss.
- **Evidence/rollback/done:** Deterministic lifecycle transcript with one notification per active gate and zero manual `once` calls. **Parallelism/conflicts:** coordinate gateway and governance changes. **Reviewer:** Operations and security.

### OPS-002 — Four-domain plain-English intake pilot

- **Objective/requirement/citations:** Prove bounded engineering, infrastructure, research, and knowledge proposals from plain English.
- **Repository/files:** Founder planner, role packages, proposal schemas, Mission Control/Telegram.
- **Prerequisites/scope:** OPS-001 and RI-004 for knowledge dossiers. **Non-goals:** arbitrary commands or sudo via chat.
- **Data/access:** Use safe fixtures and rehearsed runbooks.
- **Steps/interfaces:** Parse intent; show structured proposal/diff; approve; execute; notify; publish episode.
- **Tests/acceptance:** Ambiguous, over-risk, unsupported-machine, secret-bearing and cancellation prompts.
- **Evidence/rollback/done:** Four end-to-end transcripts and episodes; no external mutation outside approved pilot. **Parallelism/conflicts:** pilots sequential by domain. **Reviewer:** Founder/operator plus domain owner.

### OPS-006 — Stateful conversational founder intake and specification compiler

- **Status (2026-08-24):** Source-complete in `swarm-control-plane` on branch `feat/ops-006-conversations`; production migration, refreshed planner attestation, channel reinstalls and live cross-channel replay remain operational gates. Canonical revisioned conversations, stale-plan rejection, schema-aware defaults, threaded Telegram controls and Mission Control Chat & Work are implemented with an automated five-turn August 23 replay.
- **Objective/requirement/citations:** Make founder intake conversational across Telegram and Mission Control while retaining structured proposals, least privilege and explicit approval. A multi-turn exchange must behave like one continuing job until the founder finishes, stops or starts another thread. The system must understand follow-ups such as “choose the best options,” “January to February 2022,” and “do the most reasonable test” as revisions to the active research request rather than unrelated control-plane work.
- **Repository/files:** Canonical conversation/session/message/revision models and migration; conversation API and event stream; channel-neutral coordinator; intent/thread classifier; specification-schema registry; default-policy registry; identifier service; proposal revision/diff service; planner prompt/policy package; audit/redaction exporter; tests, runbook and Book XI.
- **Prerequisites/scope:** OPS-001/002, GOV-002/004, AGT-002/004 and BASE-002. One founder may maintain multiple named threads, but each inbound message binds to exactly one explicit or confidently inferred thread. Thread commands/actions include create, rename, list, switch, resume, finish, stop/cancel and archive. **Non-goals:** hidden chain-of-thought retention, arbitrary shell execution, autonomous approval, secret/sudo collection, cross-thread context leakage, automatic production promotion or capital authority.
- **Conversation contract:** Persist immutable redacted `Conversation`, `ConversationMessage`, `ConversationTurn`, `SpecificationRevision` and `ConversationEvent` records. Each message binds channel identity, reply-to, thread, actor, timestamp, source digest and processing state. Maintain a bounded working summary plus canonical references; never depend on the LLM remembering earlier chat. New-thread detection combines explicit founder action, reply/thread metadata and calibrated intent continuity. Low-confidence switching asks one concise thread question rather than silently reclassifying. `/new`, `/threads`, `/switch`, `/finish`, `/stop`, `/resume` and equivalent UI actions are deterministic controls.
- **Specification contract:** Each supported task route publishes a human-readable and machine-readable schema declaring required, optional, system-generated and safety-critical fields, allowed formats, examples, defaults and why each value matters. Clarification responses must name the missing field and accepted format. For research, show fields such as repository/base reference, program and hypothesis identity, workflow, dataset/snapshot, universe, date/frequency, seed, observations/splits, costs, tier/grid, acceptance thresholds, evidence retention and authority exclusions. `program_id`, `hypothesis_id`, task number and other administrative identities are generated deterministically when omitted, previewed to the founder and editable; the founder must not be asked to invent internal identifiers unless requesting compatibility with an existing family.
- **Default-resolution contract:** Interpret explicit phrases such as “use the best option,” “choose reasonable defaults,” or “answer non-critical questions yourself” as bounded authorization to fill administrative and scientifically conventional fields from a versioned policy. Every chosen default records value, basis, confidence, source/policy version and alternatives. Never silently default hypothesis meaning, live/capital authority, credentials, destructive operations, material risk, unavailable data, lookahead rules or a choice that changes the scientific claim. When evidence cannot establish a “best” option, label the choice `reasonable_default`, not `best`, and show the uncertainty.
- **Dialogue/proposal lifecycle:** Accumulate answers into a live specification with `collecting`, `needs_clarification`, `ready_for_review`, `approved`, `executing`, `attention_required`, `succeeded`, `failed`, `stopped` and `archived` states. Ask the smallest batch of blocking questions, accept natural-language answers, show unresolved and defaulted fields, then compile an approval-ready proposal containing the normalized specification, assumptions, exact generated IDs, tier/grid size, resource estimate, risks, exclusions, acceptance tests and diff from the prior revision. Founder edits create a new digest; approval applies only to that revision. Execution progress and results stay in the same thread.
- **Tests/acceptance:** Replay the full 2026-08-23 five-message transcript and prove it yields one `bulletproof_bt` thread, one progressively completed research specification and no spurious `swarm-control-plane` tasks. Test explicit/new inferred threads, simultaneous threads, reply after restart, ambiguous switch, stale proposal, revision after approval, cancellation, resume, duplicate Telegram update, out-of-order turn, malicious context injection, secret input, oversized history, unavailable dataset, unsupported hypothesis, unsafe default, generated-ID collision and channel handoff. Golden research tests include the complete OPS-002 synthetic prompt and a terse request that omits `program_id`/`hypothesis_id`; both must compile to the same reviewable schema, with deterministic generated IDs in the latter.
- **Evidence/rollback/done:** Retain redacted conversation/event replay, specification revisions/diffs, default-decision receipts, generated-ID lineage, proposal/approval/task/result links, restart recovery and cross-channel continuation transcripts. Rollback disables conversational mutation and returns to isolated intake while preserving all conversation records and existing proposals. Done when Telegram and Mission Control can continue the same bounded job naturally from initial intent through result, the founder can explicitly control threads, clarification explains exact formats, reasonable defaults produce an approvable configuration, and no conversational convenience weakens safety or scientific validity. **Reviewer:** Founder/operator, planner owner, domain schema owner, security reviewer and independent conversation-UX evaluator.

### CHAN-002 — Threaded Telegram conversation client

- **Status/scope/reuse/gap (2026-08-24):** Production-validated through the restart-safe two-thread replay; a follow-up source increment adds general plain-English continuity and ambiguity routing and still requires the VM2 gateway package refresh and live replay. In addition to explicit thread controls, the gateway persists a monotonic post-success Telegram polling offset and message-to-conversation bindings, sorts and suppresses duplicate updates, binds replies across concurrent threads and restarts, fails closed on unknown/closed reply targets, refuses edited-message mutation, preserves long outbound text by bounded splitting, and binds clarification/review messages to their canonical conversation. The gateway reuses the restricted founder identity, durable outbox and safe approval links while the control plane remains authoritative.
- **Contracts/dependencies:** OPS-006, CHAN-001 and UI-004. Slash commands control conversation routing, not the vocabulary of work: unfamiliar engineering, infrastructure, research, knowledge or future-domain requests remain ordinary plain English and flow to the planner for structured interpretation or clarification. Display active thread and state in acknowledgements; support reply-to association plus `/new [name]`, `/continue`, `/cancel`, `/threads`, `/switch <short-id>`, `/finish`, `/stop`, `/resume <short-id>` and `/context`. A reply always continues its bound thread; consecutive messages within a bounded active session continue naturally; when a bare message could belong to a stale selected thread or new work, retain it as a private routing draft and ask whether to continue or create a new thread without requiring re-entry. Clarification messages show numbered questions, required field names, valid formats, examples and current values. Buttons may choose enumerated options or open the digest-bound review, but never carry secrets.
- **Tests/acceptance:** Automated coverage now includes bot restart state, out-of-order/duplicate updates, post-success offset commit, failed-update replay, reply without command, concurrent threads, clarification reply binding, wrong-thread approval, expired/single-use handoffs, long-message limits, edited-message immutability, unauthorized users, outage handling and notification acknowledgement/deduplication. Telegram has no dependable ordinary-message deletion update; deletion therefore cannot erase canonical history and is documented as a transport limitation. The August 23 transcript remains one research thread rather than five clarification loops.
- **Evidence/rollback/done:** Retain redacted Telegram-to-conversation mapping and restart transcript. Rollback makes the client read-only/status-only while OPS-006 records remain intact. Done when mobile dialogue can create, refine, approve, follow and close work without losing context or bypassing governance.

### UI-007 — Mission Control conversational work and task workspace

- **Status/scope/reuse/gap (2026-08-24):** Source-complete on `feat/ui-007-conversation-workspace`. The first-class Chat & Work surface now joins the canonical cross-channel transcript and live specification to planner proposals, materialized tasks, approvals, task events and digest-bound artifacts through a read-only control-plane workspace projection. New/switch/finish/stop/resume controls, accessible new-thread dialog, proposal-review handoff, bounded task/evidence inspectors and responsive desktop/mobile layouts are implemented. Backend and Mission Control suites pass 295 and 68 tests; Ruff, JavaScript syntax, diff checks and 390-pixel no-overflow/no-console-error browser validation pass. Canonical state lives in OPS-006, not browser history. Mac reinstall and one live proposal-to-evidence cross-channel replay remain production qualification gates.
- **Contracts/dependencies:** OPS-006, UI-001/002/004 and AGT-002. Provide thread list/search, new/switch/finish/stop/resume actions, message composer, streaming/polling state, specification panel, missing-field guidance, defaults/assumptions, revision diff, approval preview, execution timeline, evidence/result inspector and channel provenance. The same conversation must continue between Mac and Telegram.
- **Tests/acceptance:** Test keyboard and screen-reader conversation operation, long formulas/cards, reconnect/reload, multi-thread switching, unresolved fields, generated identifiers, default overrides, stale revisions, approval, progress, failure/recovery and exact evidence replay across desktop/mobile layouts. UI labels must distinguish planner response, proposed plan, approved work, execution and verified completion.
- **Evidence/rollback/done:** Source evidence is retained in `docs/ui-007-validation.md` and `docs/runbooks/ui-007-conversation-workspace.md`. Retain responsive screenshots, accessibility results and one cross-channel engineering, infrastructure, research and knowledge transcript. Rollback hides composer/mutations while leaving read-only conversation history and canonical task/proposal views. Done when the founder can initiate and work through governed jobs conversationally from Mission Control with the same fidelity and thread control as Telegram. Production completion is not claimed until the Mac is reinstalled and one live thread reaches proposal review, execution and registered evidence in this workspace.

### UI-003A — Citation-grounded Research Copilot

- **Status (2026-08-22):** Implemented, deployed and production-observed on the Mac. A live question returned four bounded claims and two canonical sources with calibrated `insufficient_evidence`; exact replay of object `011a2e4b-25ff-572f-81f8-855433a2e961` returned source content. Validation is retained in `docs/ui-003a-validation.md`.
- **Objective/requirement/citations:** Give the founder a conversational interface to canonical Research Intelligence without weakening evidence, inference, access or authority boundaries.
- **Repository/files:** Mission Control Copilot service and static workspace; canonical hybrid-retrieval, graph context-pack and coordinate-replay clients; protected Codex adapter; strict answer/claim schemas; UI and service tests; validation record and Book XI.
- **Prerequisites/scope:** RI-003, RI-004, RI-008, RI-009B and RI-011. A question performs authorized hybrid retrieval, bounded graph expansion, digest-bound context assembly and read-only ephemeral model reasoning. Every factual claim cites an exact context object; synthesis is explicitly `agent_inference`; missing evidence produces terminal abstention. **Non-goals:** unrestricted document chat, hidden chain-of-thought storage, evidence mutation, automatic hypothesis approval, task execution, strategy deployment or capital authority.
- **Data/access:** The model receives only the authorized context pack and strict output schema, never source files, database credentials, scanner controls or operator tokens. Out-of-pack citations reject the whole answer. Responses expose corpus/context/graph digests, claim evidence classes, retrieval confidence, limitations and exact replay controls.
- **Steps/interfaces:** Three-pane Research Copilot workspace; conversation turns; corpus selector; confidence and insufficiency state; claim-level citation controls; evidence rail; canonical replay inspector; bounded Codex subprocess with minimal environment, read-only ephemeral sandbox, timeout and process-group termination.
- **Tests/acceptance:** Cited answer, inference separation, no-evidence abstention without model invocation, out-of-pack citation rejection, invalid model schema, timeout/termination, credential absence, control-plane failure, exact replay, keyboard focus, reduced motion and responsive layouts. Live acceptance requires one supported, one contradictory/partial and one insufficient-evidence question against the current corpus.
- **Evidence/rollback/done:** Retain unit and browser test results, live context/corpus digests and exact replay transcript. Rollback removes the Copilot route/workspace while retaining canonical retrieval and graph services; no evidence or conversation output becomes institutional truth. **Parallelism/conflicts:** UI-003B reuses this evidence rail and graph query state; LLM-001 may replace the model adapter without changing retrieval contracts. **Reviewer:** research-intelligence owner, security owner and founder/operator.

### UI-003B — Canonical Knowledge Graph Explorer

- **Status (2026-08-22):** Completed and production-observed on the Mac. A bounded live expansion returned 50 nodes and 50 edges from the current `knowledge-graph-v1.0.0` projection, and exact canonical replay returned HTTP 200. The read-only replay call has a 120-second bound because the observed corpus-scale replay required 91.95 seconds.
- **Objective/requirement/citations:** Let the founder inspect how canonical sources, claims, methods, datasets, runs, results, reviews, decisions and beliefs connect without treating visualization state as institutional truth.
- **Repository/files:** Mission Control typed graph-query adapter and local route; SVG graph workspace; adjacency fallback; evidence replay inspector; UI/service tests; `docs/ui-003b-validation.md`; Book XI.
- **Prerequisites/scope:** RI-008 and UI-003A. Render a bounded current projection, drill into one selected node through authorized neighborhood queries, filter by direction/depth/predicate, and reuse exact canonical replay. **Non-goals:** browser-side graph authority, edge creation, projection rebuild, free-form graph query languages, model-generated edges, evidence mutation or workflow execution.
- **Data/access:** The browser receives only access-filtered graph nodes/edges and replay responses from Mission Control. Queries use UUID roots, allowlisted predicates, declared direction, depth at most five and at most 100 visible nodes. Stale projections fail closed in RI-008.
- **Steps/interfaces:** Deterministic 100-node-or-smaller SVG; categorical shapes and labels; supports/contradicts edge semantics; selected-node detail and neighbor navigation; zoom/fit; accessible adjacency list; mobile list default; Copilot citation-to-graph handoff; replay inspector; projection/query digest and truncation display.
- **Tests/acceptance:** Typed query forwarding, executable/extra-field rejection, max-node/depth bounds, empty graph, cycles, truncation, node selection, predicate filtering, exact replay, keyboard operation, visible focus, mobile/desktop layout, reduced motion and no console errors. Live acceptance requires current overview, one neighborhood expansion and one replayed selected object.
- **Evidence/rollback/done:** Retain 65-test result, lint/compile/JS checks, responsive screenshots and live corpus/query/object identities. Rollback removes the local query route and enhanced workspace while RI-008 canonical graph APIs and UI-003A remain intact. **Reviewer:** Research Intelligence owner, accessibility reviewer and founder/operator.

### UI-003C — Integrated Research Workspace

- **Status (2026-08-22):** Completed, deployed and production-observed on the Mac. Canonical citation `011a2e4b-25ff-572f-81f8-855433a2e961` expanded as the same graph root to three nodes and two edges in 0.3 seconds and replayed exactly in 22.38 seconds.
- **Objective/requirement/citations:** Give the founder one coherent research surface for grounded synthesis, canonical relationship inspection and governed corpus management while preserving every UI-003A/B evidence and authority boundary.
- **Repository/files:** Mission Control Research Workspace shell, semantic mode navigation, shared context strip, responsive styles and regression tests; `docs/ui-003c-validation.md`; Book XI.
- **Prerequisites/scope:** UI-003A and UI-003B. Integrate existing capabilities as `Ask`, `Explore` and `Library`, preserve local mode state, expose current projection/curriculum/ingestion status and carry at most eight selected canonical identities between modes. **Non-goals:** saved model memory, browser-authored collections, context-pack overrides, evidence mutation, graph writes, autonomous research execution or capital authority.
- **Data/access:** Working context contains only IDs, types, labels and digests already authorized for the browser session. It is ephemeral navigation state and never enters canonical storage or model input implicitly. Existing upload and inbox mutations retain their founder-intent gate.
- **Steps/interfaces:** Deep-linkable semantic tabs; keyboard roving focus; compact readiness strip; bounded context items with remove/clear; citation-to-context; context-to-neighborhood; hidden-panel graph restoration; responsive single-column library; explicit empty, loading and error states.
- **Tests/acceptance:** Static contract, mode restoration, arrow/Home/End keyboard behavior, context deduplication and eight-item cap, remove/clear, graph preservation, no implicit model scope, mobile/desktop layout, focus visibility, reduced motion and no console errors. Live acceptance requires one cited object to persist across Ask and Explore and replay exactly.
- **Evidence/rollback/done:** Retain automated results, screenshots, live projection/corpus/query/object identities and replay result. Rollback restores the previous sequential Knowledge page without changing UI-003A/B services or canonical state. **Reviewer:** Research Intelligence owner, accessibility reviewer and founder/operator.

### OPS-004 — Fleet observability and founder alerting

- **Status (2026-08-22):** VM1 and VM2 probes are deployed, enabled and publishing bounded observations. Independent simultaneous-outage detection is deferred until an external always-on host is available; OPS-004 is therefore operational for individual-host telemetry but not yet production-qualified for correlated VM1/VM2 loss.
- **Deferred external-watchdog work:** Provision a minimal hardened always-on VPS outside the VM1/VM2 failure domain; install the existing `invariance-swarm-fleet-watchdog` unit with a dedicated restricted credential and direct Telegram fallback; constrain network access to the two declared health targets and Telegram; define ownership, patching, backup and cost controls; then rehearse VM1 loss, VM2 loss, simultaneous loss, recovery, duplicate suppression and credential rotation. Do not place this authority on the intermittently available Mac, and do not close OPS-004 until digest-bound rehearsal evidence demonstrates simultaneous-outage detection within the declared SLO without false duplicate alerts.

- **Objective/requirement/citations:** Continuously and accurately observe VM1 and VM2 resource health and availability, surface actionable incidents in Mission Control, and notify the founder through Telegram without transient-spike noise or duplicate floods.
- **Repository/files:** Control-plane machine-observation, incident and notification schemas/services; bounded local probe; VM1/VM2 systemd units; peer and independent availability watcher; Telegram notification outbox consumer; Mission Control Fleet Health view; operator runbooks and retention policy.
- **Prerequisites/scope:** OPS-001 for durable deduplicated notifications; PLAT-001 service ownership; PLAT-005 owns common telemetry/SLO conventions. Deliver VM1-to-VM2 and VM2-to-VM1 observation first, followed by an independent always-on third observer so simultaneous VM failure remains detectable. **Non-goals:** LLM-decided alert thresholds, automatic privileged remediation, process-environment collection, or treating the sleeping Mac as an availability authority.
- **Data/access:** Probes publish signed, bounded, low-cardinality observations only. Never collect command lines, credentials, process environments or protected payloads. Raw samples have bounded retention; hourly/daily rollups and incident evidence have explicit retention classes.
- **Steps/interfaces:** Collect `MemAvailable`, swap activity, Linux PSI, CPU utilization/load per core, disk/inode capacity, I/O pressure, uptime, OOM events and approved service health every 15–30 seconds; ingest observations idempotently; evaluate sustained multi-signal thresholds; transition incidents through pending, warning, critical, acknowledged, silenced and recovered states; apply hysteresis, cooldowns and maintenance windows; deduplicate Telegram delivery; provide a VM1 fallback notifier when VM2 hosts the primary gateway; expose current state, history and evidence in Mission Control.
- **Tests/acceptance:** Simulated CPU saturation, low available memory, swap thrashing, disk/inode exhaustion, OOM, critical-service failure, packet loss, one missed probe, sustained single-host outage, both-host outage, recovery, restart, clock skew, duplicate delivery, acknowledgement, silence expiry and maintenance-window fixtures. A single spike or isolated missed heartbeat emits no alert; sustained threshold crossings emit exactly one state-change notification; escalation and recovery each emit once; secrets never appear in samples, logs or messages.
- **Evidence/rollback/done:** A retained pilot dossier proves accurate VM1 and VM2 resource readings against operating-system references, single-host outage detection within the declared SLO, independent simultaneous-outage detection, bounded false-positive rate under injected transient faults, durable incident history, Telegram warning/escalation/recovery delivery and Mission Control replay. Rollback disables probes/notifiers without deleting incident evidence. **Parallelism/conflicts:** share telemetry contracts with PLAT-005 and notification semantics with OPS-001; do not create a second alert outbox. **Reviewer:** SRE/operations owner, security owner and founder/operator.

**Implemented source boundary:** Migration `b6f2a9c41d80` adds digest-bound raw
observations, incident generations and replayable transitions. Strict agent-authenticated
probes collect aggregate `/proc`, PSI, capacity and explicit service status only. A
three-sample detector with recovery hysteresis drives the existing founder notification
outbox; Mission Control shows current fleet health; Prometheus exports sample age and
incident state. A separately deployable TCP watchdog provides the only direct Telegram
fallback and must run outside VM1/VM2. The activation dossier must still demonstrate
live value parity, Telegram delivery and simultaneous-host outage detection.

### OPS-005 — Automated control-plane backups and freshness enforcement

**Implementation status (2026-08-22):** Complete, deployed and production-observed on
VM2. The implementation provides atomic verified custom-format dumps,
versioned manifests, overlap/free-space gates, 7-daily/4-weekly/6-monthly retention,
persistent daily scheduling, a network-isolated weekly restore drill, fleet freshness
signals, OPS-004 hysteresis/deduplicated founder notifications, Mission Control age
visibility, focused failure tests, and an operator runbook. Two consecutive live
manifests are retained; a network-isolated 77-table restore recorded RPO 4.584 seconds
and RTO 326.545 seconds; the real failure/recovery lifecycle emitted one deduplicated
notification per transition; both persistent timers and the VM2 probe are active; and
the scoped no-secret scan passed. Encrypted off-host replication remains owned by
PLAT-007 rather than OPS-005.

- **Objective/requirement/citations:** Close the production gap discovered by the 2026-08-21 OPS-002 infrastructure observation, when the newest integrity-valid control-plane backup was 22 days old and correctly failed the seven-day freshness policy. Automate verified control-plane PostgreSQL backups without weakening the observation gate, and provide the near-term operating implementation required by PLAT-007.
- **Repository/files:** Versioned control-plane backup script; hardened systemd service and timer on VM2; infrastructure installer; backup inventory/retention utility; broker observation evidence; founder notification and Mission Control backup-health surfaces; recovery runbook.
- **Prerequisites/scope:** OPS-001 notification semantics and the current digest/integrity-checking broker observation. Coordinate retention, off-host replication and restore ownership with PLAT-007. **Non-goals:** embedding credentials in units, backing up only projections while omitting canonical state, silently deleting the last verified generation, treating dump creation as proof of restorability, or weakening freshness thresholds to hide scheduler failure.
- **Data/access:** Use a dedicated least-privilege backup identity or the existing reviewed container-local backup interface; secrets remain root-owned files and never enter arguments, logs or evidence. Dumps and manifests are mode-restricted, digest-bound and excluded from source control. Off-host copies are encrypted and access-audited.
- **Steps/interfaces:** Install an enabled persistent timer with bounded jitter and overlap prevention; write to a temporary file and atomically publish only after `pg_restore --list`; record size, digest, schema/migration marker, start/end time and failure category; retain at least 7 daily, 4 weekly and 6 monthly verified generations; alert once when the timer fails or the newest verified backup approaches/exceeds the seven-day SLO; expose freshness and last-success evidence; perform scheduled disposable restore drills; document manual invocation, pause, recovery and rollback.
- **Tests/acceptance:** Rehearse success, interrupted dump, zero-byte/corrupt dump, insufficient space, Docker/Postgres unavailable, permission denial, concurrent invocation, host reboot/missed timer, retention boundaries, clock skew, notification deduplication and recovery. Prove canonical tables, migrations, agent/task/event history and RI state in a disposable restore. The production observation must pass with a fresh verified backup and fail closed with a stale or corrupt one.
- **Evidence/rollback/done:** Retain unit verification, timer history, two consecutive production backup manifests, one disposable restore dossier with measured RPO/RTO, stale-backup alert and recovery transcript, and a no-secret scan. Rollback disables the timer without deleting any verified generation or observation evidence. **Parallelism/conflicts:** may begin during OPS-002; reuse OPS-004 alert transport and PLAT-007 retention/restore contracts rather than creating competing systems. **Reviewer:** database/recovery owner, SRE/operations owner and security owner.

### OPS-007 — Fleet-wide operation ledger and background-work visibility

- **Status (2026-08-25):** Completed and production-observed for the governed operation surface in `swarm-control-plane` commits `5682933`, `a8d4728`, `7270d79` and `491ae22`. Migration `b7c3e8a91d40` plus merge head `c9d4f2a71e30` add canonical operations and append-only events; every task reconciles into explicit lifecycle/heartbeat state; retrieval and graph rebuilds emit independently committed phase/unit progress, including graph digest preparation; Mission Control provides a responsive global Activity center and always-visible active count. Validation passed with `315` backend and `70` Mission Control tests, focused graph/ledger tests, migration/static SQL, JavaScript, Ruff, diff and desktop/mobile checks. VM2 is healthy at the merge head, the Mac LaunchAgent is running the installed Activity UI, and operation `c7055a10-0c15-48a5-9faf-367f091a0b54` advanced through `1,080` durable events to `succeeded`, projecting `784,223` nodes and `1,368,760` edges with fresh graph manifest `f931765a099aeda5ee3fe8c4dc8225d9843201f8916e64f702a0e5b524f2b277`. Known daemons remain represented by OPS-004 Fleet health rather than being falsely counted as active work; any future workload outside governed tasks or an instrumented reporter must add the same ledger contract before activation.
- **Objective/requirement/citations:** Ensure no material work can run on VM1, VM2, Mac or a future host without a durable, founder-visible operation record and fresh progress evidence in Mission Control.
- **Repository/files:** Canonical operation/run/phase/event schemas; worker, broker, planner, supervisor, ingestion, projection, curriculum, backup and deployment instrumentation; host process/service adapters; Mission Control global activity center; Telegram status links; Prometheus metrics; operator runbook.
- **Prerequisites/scope:** OPS-001, OPS-004 and existing task/mission/event records. Instrument all governed work first and separately surface approved systemd timers/services and detected ungoverned long-running processes as observations. **Non-goals:** capturing secrets, arbitrary command lines or process environments; inventing fake percentages; allowing UI cancellation to bypass operation-specific rollback contracts.
- **Steps/interfaces:** Assign an immutable operation ID before work starts; record initiator, authority, host, service/agent, task/mission/proposal links, input digest, phase DAG, units completed/total where measurable, heartbeat, resource envelope, logs/evidence links, retry/rollback/cancel capability and terminal receipt. Long synchronous endpoints become resumable background jobs. Mission Control provides an always-visible activity indicator plus Active, Waiting Approval, Blocked, Failed and Recently Completed views, exact error details, stale-heartbeat detection and deep links to the owning object. Unknown progress is shown as indeterminate, never fabricated.
- **Tests/acceptance:** Cover client disconnect, API restart, worker restart, host loss, duplicate submission, retry, approval wait, cancellation, non-cancellable phase, rollback, stalled heartbeat, unknown total, nested mission/task, timer job and ungoverned-process observation. A cross-machine inventory must reconcile every governed active execution with exactly one visible operation; injected hidden work must raise a visibility finding; no credentials or protected payloads appear.
- **Evidence/rollback/done:** Retain a multi-host replay proving discovery-to-terminal visibility for projection rebuild, curriculum evaluation, inbox/recovery, Bulletproof run, deployment and backup. Rollback may disable the UI but cannot delete operation history. Done requires a declared reconciliation SLO and zero unexplained active governed processes during the acceptance window. **Reviewer:** SRE/operations, Mission Control UX, security and founder/operator.

## Wave 2 — Laboratory closure and walking skeleton

### BT-001 — Bulletproof full-suite and contract-drift closure

- **Status:** Completed, tested and merged on 2026-08-22 in Bulletproof commit `6a1cbbfbc69bd84281d466316e42e04698c1b3c5` (PR #263); acceptance evidence: [BT-001 completion evidence](evidence/BT-001.md).
- **Objective/requirement/citations:** Resolve every recorded collection/failure discrepancy in Book V Appendix E without weakening tests.
- **Repository/files:** Bulletproof dependencies, fixtures, hypotheses/contracts, alert writer, tests/docs.
- **Prerequisites/scope:** BASE-001; diagnose each defect as code/test/config/docs/environment. **Non-goals:** new strategy logic.
- **Data/access:** Synthetic fixtures; no lake mutation.
- **Steps/interfaces:** Commit lock/environment matrix; repair drift; bounded collection shards; publish status.
- **Tests/acceptance:** Full collection and suite by declared shards, lint/type commands, failure reproduction before fix.
- **Evidence/rollback/done:** Test matrix with zero unexplained collection errors/failures. **Parallelism/conflicts:** defect groups parallel except dependency lock. **Reviewer:** Bulletproof maintainer and independent test reviewer.

### BT-002 — Immutable dataset and availability contract

- **Status:** Completed, tested and merged on 2026-08-22 in Bulletproof commit `54220e21ad1b4b2110c00d243bd4326b7d67c76d` (PR #264); acceptance evidence: [BT-002 completion evidence](evidence/BT-002.md).
- **Objective/requirement/citations:** Close Appendix D identity, correction, membership, clock and point-in-time gaps.
- **Repository/files:** `bt.research_data`, manifests/schemas/validators/tests/docs.
- **Prerequisites/scope:** BASE-002 and BT-001; content manifests for a bounded dataset family first. **Non-goals:** rewriting raw lake.
- **Data/access:** Read-only existing lake; write new derived manifests outside source partitions.
- **Steps/interfaces:** Dataset/snapshot schemas, partition digests, provenance/correction ledger, availability policies and validators.
- **Tests/acceptance:** Duplicate/gap/clock/correction/membership/lookahead fixtures and read-only lake smoke.
- **Evidence/rollback/done:** Snapshot validation report and RI registration receipt. **Parallelism/conflicts:** schemas before validators. **Reviewer:** Data steward and statistical reviewer.

### BT-003 — Atomic digest-finalized run bundle

- **Status:** Completed, tested and merged on 2026-08-22 in Bulletproof commit `8f1418415cad4e2327f7e9a6dbb78257609f65e7` (PR #265). The compatible Hermes run producer was merged in control-plane commit `4b7f7d1685c0af5a4cb81b621f49dfeabea5eff8` (PR #79). Acceptance evidence: [BT-003 completion evidence](evidence/BT-003.md). This is a source and contract claim; production exercise belongs to BT-009/WS-001.
- **Objective/requirement/citations:** Give every canonical artifact a schema, content digest, lineage, atomic finalization and failure state.
- **Repository/files:** Bulletproof artifact writers/schemas/validation; Hermes producer endpoint.
- **Prerequisites/scope:** BASE-002, RI-001, BT-001/002. **Non-goals:** live orders.
- **Data/access:** Bounded public/synthetic fixture.
- **Steps/interfaces:** Bundle manifest; temporary/final states; compatibility; idempotent publish receipt.
- **Tests/acceptance:** Repeat run, interruption, corrupt/missing artifact, incompatible schema, duplicate publish, absolute-path/secret scan.
- **Evidence/rollback/done:** Two semantically identical bundle digests under supported environment policy and one retained failed attempt. **Parallelism/conflicts:** owns producer contract. **Reviewer:** Laboratory and Knowledge stewards.

### BT-009 — Hermes-to-Bulletproof governed research bridge

- **Status (2026-08-24):** Completed, tested, merged and operationally replayed on VM2. Bulletproof PR #272 (merge `3cc4a49ee5189894f132a315d8adcc8f9edaa3dc`) implements the governed proposal compiler and native 16-variant qualification. Control-plane PRs #91-#98 implement and harden the registry, publication, projection, memory and interruption-resume path through merge `35001f5492f33b3ac976bf2c18e7827081faf05a`. The replay retained one negative selected result, two independent reviews, a founder `retain` decision, current graph/retrieval receipts and one Bulletproof-memory publication without production or capital authority. Exact runtime evidence: [BT-009 completion evidence](evidence/BT-009.md).

- **Objective/requirement/citations:** Replace the fixed worker-local research pilot and its hard-coded hypothesis/dataset enums with an end-to-end governed bridge from any Hermes evidence-grounded research question to a prospectively registered, natively executed and fully logged Bulletproof experiment. The bridge must enforce `bulletproof_bt/docs/hypothesis_strategy_generation_prompt_instructions.md`, the hypothesis/strategy schemas, the Research Bible scientific method, and the existing no-capital authority boundary.
- **Repository/files:** Hermes Research Intelligence Director and trial registry; a dedicated hypothesis-specification role; restricted engineering mission/package generator; Bulletproof hypothesis YAML, strategy module, adapter/feature registration, tests and documentation surfaces; native hypothesis/grid runner adapter; truth-gate adapter; atomic run-bundle publisher; Bulletproof research-memory and Hermes evidence/graph publication adapters; Mission Control proposal, progress, review and dossier views.
- **Prerequisites/scope:** BASE-002/003, RI-001/003/004/010, OPS-001, BT-001/002/003. Compose BT-004 through BT-008 contracts as they qualify; do not duplicate their engine, market-model, orchestration, feature or laboratory-publication ownership. Begin with one bounded hypothesis family and immutable dataset snapshot, then generalize through typed schemas. **Non-goals:** arbitrary code from task input, direct primary-checkout edits, unregistered parameter search, self-approval, automatic research promotion, shadow/live orders, capital allocation or bypassing Bulletproof's classic execution authority.
- **Data/access:** The hypothesis/specification and execution roles receive read-only, catalog-mediated access to the complete locally available Binance and Bybit perpetual data lakes, including their declared market, funding, open-interest and availability manifests; this is full scientific availability, not permission to bypass point-in-time, coverage, provenance or leakage checks. They receive approved context packs and prior-result summaries, while protected raw bytes and credentials remain outside model prompts. Generation occurs in an isolated Git worktree with explicit allowed paths and no secrets. Execution receives digest-pinned repository code, immutable dataset/snapshot manifests, prospective experiment/trial identifiers and a bounded resource budget. Raw protected data and credentials never enter prompts, task payloads, patches, logs or run bundles.
- **Steps/interfaces:** Treat every founder research question as a request for hypothesis compilation, not as a request to squeeze the question into a fixed enum. The dedicated hypothesis-creation role first inspects the catalog and coverage/availability evidence, retrieves prior art and negative results, and produces a testable, citation-backed hypothesis card with causal feature definitions, dataset/universe/window, tier, finite grid, logging requirements, metrics, falsification criteria and expected failure modes. Present that card and any small numbered decision brief to the founder; no strategy code or trial is created before card approval. After approval, enforce the Bulletproof strategy-generation instructions to generate or reuse the hypothesis YAML, native `strategy.py` module, adapters/features, decision and state logging, tests and documentation in a bounded engineering worktree. If an approved registered strategy already matches, bind its immutable YAML/code/adapter/test digests and do not regenerate it. Run independent schema, causality, lookahead, timestamp, truth-contract, path/diff and code review gates, then present the immutable strategy/run specification and finite grid for execution approval. Treat `Tier2A`, `Tier2B` and `Tier3` as distinct typed values; resolve legacy `Tier2` according to the declared compatibility rule and show it. Reject unavailable features, unknown tiers/parameters, unbounded grids and hidden optimization. Register repository/dataset/experiment/trial digests; execute only through native classic Bulletproof; capture decisions, fills, trades, equity, performance, state features, structural buckets, failures and resource telemetry; run `validate_experiment_truth.py`; atomically finalize the bundle; ingest certified artifacts into Bulletproof memory; publish canonical evidence, citations, lineage, negative results and reviews into Hermes; record accept, reject, refine or defer without production promotion.
- **Tests/acceptance:** Cover ordinary prose with explicit tier/grid, pasted card with formatting noise and citation markers, ambiguous tier, unknown parameter, invalid grid value, excessive Cartesian product, hidden optimization language, omitted dataset/timeframe, unavailable auxiliary feature, prompt injection in evidence, duplicate family, missing/changed dataset digest, repository drift, generated path escape, arbitrary command surface, lookahead, incomplete HTF bar, forward auxiliary join, missing-bar decision, invalid stop/sizing contract, unregistered strategy, schema/test failure, unsupported fast path, classic/fast parity failure, partial/interrupted run, resource exhaustion, stale lease, truth-gate failure, corrupt bundle, duplicate publication, memory-ingestion failure and retry, cross-system digest mismatch, negative-result retention and attempted self-promotion. The mandatory golden fixture is the supplied `CSI-Gated Displacement Trend` card: it must resolve to the existing registered `l7_h1_csi_gated_displacement_trend` YAML, strategy, feature kernel and tests; preserve `d0={1.8,2.2}`, `theta={0.7,0.8}`, `k_stop={3,4}` and `k_trail={3,5}` as exactly 16 requested variants; select and visibly confirm the founder-requested tier; avoid duplicate code generation; and replay through native artifacts, required CSI/component/displacement/liquidity/trailing-stop logs, Bulletproof memory records and a Hermes dossier on a fresh client.
- **Evidence/rollback/done:** Retain the approved hypothesis/specification digest, generated patch and review receipts, repository and dataset pins, prospective registry records, bounded execution transcript, truth-gate report, atomic run-bundle digest, Bulletproof memory ingestion receipt, Hermes publication receipt, statistical/adversarial reviews and final decision episode. Done means the same registered pilot can be reproduced without manual command translation, every artifact and decision replays to its source, failed runs remain searchable, and no component can promote or trade. Rollback disables new bridge submissions while retaining registry, run, memory and dossier evidence. **Parallelism/conflicts:** specification/generation fixtures may proceed alongside BT-004/005; native orchestration must use BT-006; feature contracts use BT-007; publication uses BT-008. **Reviewer:** Senior quantitative research authority, Bulletproof maintainer, independent statistical reviewer, adversarial reviewer, security owner and founder/operator.

### WS-001 — No-capital walking-skeleton demonstration

- **Status (2026-08-24):** Completed, merged and operationally replayed against the VM2 control plane. Report `7e91e1219a6f764a2cb0c6b07b39fdd2cd27e770117a4f1c7452ea543eb807ce` composes the production-observed BT-009 valid-negative publication, six distinct canonical lifecycle objects, two independent reviews, a separately retained invalid-causality outcome and successful partial-publication compensation. No capital or order authority was introduced.
- **Objective/requirement/citations:** Execute the complete [walking skeleton](WALKING_SKELETON.md).
- **Repository/files:** Control plane, RI, Bulletproof, worker role packages, Mission Control.
- **Prerequisites/scope:** RI-001 through RI-005, OPS-001, BT-002/003/009. **Non-goals:** shadow/live mutation.
- **Data/access:** Immutable small public/synthetic snapshot; no credentials beyond service auth.
- **Steps/interfaces:** Ingest evidence; dossier; question; registered trial; bounded task; run bundle; publication; two reviews; decision; episode.
- **Tests/acceptance:** Valid negative and invalid-causality paths; exact replay from a fresh client.
- **Evidence/rollback/done:** One root dossier linking all object/event/artifact digests; compensation test for partial publication. **Parallelism/conflicts:** demonstration serialized. **Reviewer:** Founder research authority and independent audit reviewer.

## Wave 3 — Discovery, prospective evidence, and ML

### DISC-001 — Evidence-grounded daily research director

- **Status/scope/reuse/gap (2026-08-24):** Source-complete at control-plane commit `4bf9982`; reuses the existing daily scheduler, RI-006 surveillance records, program budgets and Mission Control research surface. It adds ranked evidence-grounded selection, explicit founder decisions and an append-only task-readiness trail without creating a second scheduler or granting execution authority. Production completion requires merge, migration `a8c4e1d72b90`, VM2 API deployment, Mac Mission Control reinstall and one live provenance replay.
- **Objective/requirement/citations:** Replace static mandate rotation as the sole question source with approved RI candidates while retaining deterministic scheduling.
- **Repository/files:** Daily research service, RI Director, trial registry, UI.
- **Prerequisites/scope:** RI-006 and WS-001. **Non-goals:** autonomous approval/execution.
- **Data/access:** Approved surveillance and internal evidence only.
- **Steps/interfaces:** Candidate ranking, duplicate/search-family check, budget gate, proposal, approval, task-ready event.
- **Tests/acceptance:** Static fallback, novelty tie, duplicate, stale corpus, budget exhaustion and race tests.
- **Evidence/rollback/done:** Source validation is retained in control-plane `docs/disc-001-validation.md` and the live runner is `worker/scripts/disc001_pilot.py`. A daily cycle must replay its publication, routing decision, citation, ranking, budget, question digest, founder decision and `task_ready` event. Rollback restores mandate-only selection while retaining immutable cycle events. **Parallelism/conflicts:** owns scheduler selection. **Reviewer:** Senior quantitative research authority.

### SHADOW-001 — Prospective journal and execution replay

- **Status/scope/reuse/gap (2026-08-25):** Source-complete and locally rehearsed at Bulletproof commits `b2b84bc`, `58cbc5a` and evidence commit `a6a399a`. The implementation reuses the existing shadow runtime, simulated adapter, SQLite checkpoints, reconciliation, incident recording and execution artifacts. It adds only the missing immutable prospective boundary and deterministic replay verifier. The retained no-capital pilot passed disconnect recovery, duplicate suppression, reconciliation, tamper rejection and sealed replay; all 1,279 repository tests passed with 27 expected skips. Continuous public-feed deployment, Hermes/RI publication and Mission Control shadow-session visibility remain follow-on operational work and are not implied by this completion.
- **Objective/requirement/citations:** Implement M5 immutable shadow observations and no-capital replay.
- **Repository/files:** Bulletproof execution runtime, market journal, Hermes/RI publication.
- **Prerequisites/scope:** BT-003 and admitted research candidate. **Non-goals:** venue order submission.
- **Data/access:** Public/read-only feeds; credential isolation.
- **Steps/interfaces:** Candidate pin, event journal, intents, replay fills, reconciliation, incidents.
- **Tests/acceptance:** Disconnect, duplicate/out-of-order event, clock drift, restart, replay parity and cost calibration.
- **Evidence/rollback/done:** Retained report digest `745862c57511dacc02278fd6ec8a7243e28dea36c3389df653ab4c7b937d991f` binds source commit `58cbc5ac974080f572d58c1990558ca47043d984`, and sealed journal digest `3a4dc409783061fae9e6aeb735dea96be4bb408fe084f916541e4514a66a4c46`. Rollback disables `shadow_journal.enabled`; prior shadow behavior and immutable evidence remain intact. **Parallelism/conflicts:** feed and replay adapters parallel after journal schema. **Reviewer:** Execution and risk reviewers.

### ML-001 — Reproducible model and calibration registry

- **Status/scope/reuse/gap (2026-08-25):** Source-complete and locally rehearsed at Bulletproof source commits `8443069`, `eee98f7`, `8dbfc4e` and evidence commit `0c945af`. The implementation reuses BT-002 dataset identity and BT-007 representation/split digests, NumPy, the existing deterministic artifact conventions and SQLite. It adds an ML-specific content-addressed bundle, append-only version lifecycle, held-out calibration, inference receipts, applicability/abstention behavior and independently attributed rollback. The pilot is a transparent deterministic fixture, not evidence of alpha or a deployed model service. RI canonical publication and production inference serving remain follow-on work.
- **Objective/requirement/citations:** Implement M6 model/feature/fit/calibration lineage without direct alpha or capital authority.
- **Repository/files:** Bulletproof/ML package, RI records, model artifact store.
- **Prerequisites/scope:** BT-002/003 and RI-001. **Non-goals:** live sizing.
- **Data/access:** Point-in-time registered snapshots only.
- **Steps/interfaces:** Feature/fit/model schemas, training run, calibration, uncertainty, inference receipt.
- **Tests/acceptance:** Seed/environment reproduction, leakage, shift, calibration, corrupt model and rollback.
- **Evidence/rollback/done:** Source commit `8dbfc4eaf9c2243ed5e035df68a4ae1dff05413d` reproduced model digest `5e3b8c80a494aaedb33dd61c8484fb59ed1f89254dec52724ebae82193e175a3`; registry snapshot digest `1d738ee40118551ccfbeb3edabfea609b09a4319958fa55a3ee5772d78c3d605` and report digest `7e3f250ffb54d5d6e194ad07cee4a065b2bb614ac8ce52f708b99f398bb5cd69` retain calibration, supported and shifted inference, challenger activation and rollback. Rollback retains every artifact and event while reactivating an independently approved prior digest. **Parallelism/conflicts:** feature and evaluation fixtures parallel. **Reviewer:** ML and statistical reviewers.

## Wave 4 — Capital path and resilient operations

### PORT-001 — Portfolio-candidate and deterministic risk service

- **Status/scope/reuse/gap (2026-08-25):** Source-complete and locally rehearsed at Bulletproof source commit `4eaf836d2b0f9a1de4730b2141847cc7d073e40a` and evidence commit `7e0ab6c`. The additive service reuses registered research/shadow digests, NumPy, deterministic artifact conventions and the existing portfolio-engine boundary. It adds canonical candidate normalization, exact-overlap covariance, conservative statistical/shared dependency, uncertainty-aware capacity-capped inverse-volatility construction, hard candidate/family/concentration/dependency/stress constraints and explainable rejection. It does not replace the existing portfolio runner or risk coordinator and grants no admission, allocation, capital or order authority. Live RI dossier publication and actual allocation review remain later governed work.
- **Objective/requirement/citations:** Implement Book VII candidate aggregation, dependency, capacity, constraints and stress without allocation authority.
- **Repository/files:** Portfolio/risk services, Bulletproof integration, RI dossiers.
- **Prerequisites/scope:** SHADOW-001 and optionally ML-001. **Non-goals:** live allocation.
- **Data/access:** Registered candidate/shadow evidence.
- **Steps/interfaces:** Candidate set, covariance/dependency, constraints, stress, explainable rejection.
- **Tests/acceptance:** Concentration, missing data, regime/cost/capacity stress, deterministic repeat and infeasible portfolio.
- **Evidence/rollback/done:** Report digest `98964cfa2fd0afd65208330bf50f6b25c3eff99d9e0faa9723efca0a6843e555` binds candidate-set digest `43a0bd21e8c1286b13e1c4de9010c19580e543cd9b2402cdfc0bb31b2e43b325` and non-allocated dossier digest `3ab51287d89cfdc02a04b4ba1014a85a6716b1a55a086da43d74d4867a3378bd`. The full 1,294-test suite passed with 27 expected skips; retained rejection dossiers cover missing overlap, stressed-capacity infeasibility and stress loss. Rollback removes the additive candidate service while retaining every dossier; existing portfolio execution behavior is unchanged. **Parallelism/conflicts:** owns portfolio policy schemas. **Reviewer:** Portfolio and risk authorities.

### LIVE-001 — Demo and micro-live gated canary

- **Status/scope/reuse/gap (2026-08-25):** Pre-capital source gate complete and locally validated at Bulletproof commit `e6ce17ed9b8e14e23ea54f121f1f448387ae2ecf`; operational milestone remains `blocked_before_capital`. The runtime now validates a root-owned mode-`0600`, digest-bound, expiring authorization bundle before constructing an exchange adapter or resolving credentials. It binds PORT-001 non-allocation evidence, demo qualification, connector certification, M8 readiness, kill/rollback rehearsal, exact venue/symbol/time/loss/order limits and a separately signed approval. Runtime controls reject widened limits, stale/future bars, duration, loss and gross-notional breaches, and Binance now requires its private stream. No demo or live order was placed, no credentials were requested, and no scaling authority exists. Missing work is genuine DEMO-001 venue evidence, production connector certification, real M8/kill evidence, dedicated no-withdrawal credentials, a separate founder/risk approval and the serialized micro-live/flatten/reconciliation dossier.
- **Objective/requirement/citations:** Execute M7 demo qualification and separately approved micro-live canary.
- **Repository/files:** Execution adapters, risk/kill/reconciliation, secrets and incident systems.
- **Prerequisites/scope:** SHADOW-001, PORT-001, M8 operational gates, explicit human approval. **Non-goals:** scaling.
- **Data/access:** Dedicated least-privilege venue credentials; never in prompts/artifacts.
- **Steps/interfaces:** Certification, demo, approval, hard loss/order limits, canary, kill, reconciliation, review.
- **Tests/acceptance:** Venue sandbox plus forced outage/partial fill/stale data/key rotation/kill drills.
- **Evidence/rollback/done:** Bulletproof `docs/live-001-validation.md` and 1,304 passing tests with 27 declared skips prove the source boundary only. Operational completion still requires a genuine demo dossier and separately signed micro-live dossier; rollback cancels open orders, flattens, reconciles and revokes allocation. **Parallelism/conflicts:** serialized external mutation. **Reviewer:** Production, risk and founder authority.

### OPS-003 — Disaster recovery and vendor/runtime replacement

- **Status/scope/reuse/gap (2026-08-25):** Source-complete and deterministically rehearsed at control-plane commit `30e6843f42b9e3bc1bd3d01a75a7c913e45b0686`. OPS-003 composes the existing OPS-005 control-plane backup/isolated restore, RI-005 canonical corpus restore and projection rebuild, worker stale-lease semantics and founder notification behavior. It adds one strict integrated dossier rather than new canonical stores. The dossier enforces measured RPO/RTO, backup/restore identity, migration and table checks, corpus/projection lineage, citation replay, exactly-once task recovery, notification dedupe, redacted secret rotation, schema-compatible runtime replacement, canonical-output parity and fallback. The rehearsal touched no production resource and grants no production-restore authority. Encrypted off-host retention remains PLAT-007 rather than being overclaimed here.
- **Objective/requirement/citations:** Prove M8/M9 recovery and replaceability across canonical services, projections, workers, and model runtime.
- **Repository/files:** Infrastructure automation, backups, RI, control plane, deployment docs.
- **Prerequisites/scope:** RI-005 and deployed walking skeleton. **Non-goals:** destructive production test without rehearsal/approval.
- **Data/access:** Encrypted backups and redacted evidence.
- **Steps/interfaces:** Parity rehearsal; restore canonical stores; rebuild projections; rotate secrets; replace one model/runtime; replay tasks.
- **Tests/acceptance:** Measured RPO/RTO, integrity digests, stale lease handling, notification and rollback tests.
- **Evidence/rollback/done:** Dossier digest `941a484ee954fe25a8c63bd256e7bd48699ca6cbba1c3486f5d7df8f081f7f71` binds all five recovery sections and the runtime compatibility/fallback proof. The focused 12-test suite and complete 229-test worker suite pass; secret-shaped evidence, drift, duplicate execution/notification and threshold overruns fail closed. Rollback retains prior backup/runtime generations and rebuilds only derived projections. **Parallelism/conflicts:** rehearsals parallel by service, final integrated drill serialized. **Reviewer:** SRE, security and governance.

## Deferred post-system architecture

### LLM-001 — Hybrid frontier and open-weight model architecture

- **Status/timing:** Explicitly deferred until the full system backlog and integrated operating path are complete. Codex remains the sole approved LLM reasoning runtime during the current implementation waves; this item must not introduce a provider migration or distract from system completion.
- **Objective:** Design a provider-neutral model architecture that routes difficult, novel, or high-stakes reasoning to frontier models while assigning repetitive, high-volume, privacy-sensitive, and well-evaluated tasks to suitable open-weight models.
- **Candidate open-weight scope:** Document classification, metadata extraction, embeddings, reranking, query expansion, bounded summarization, entity extraction, duplicate detection, operational-memory extraction, and other repetitive structured transformations.
- **Frontier-model scope:** Complex engineering, architecture, difficult debugging, novel quantitative reasoning, adversarial scientific review, ambiguous founder requests, and synthesis requiring the strongest available reasoning.
- **Required design controls:** Model gateway and registry; task-to-model policy; schema-constrained outputs; prompt/model/version provenance; privacy and data-egress policy; evaluation suites; shadow comparison; confidence and failure escalation to a frontier model; cost, latency, and quality telemetry; per-role budgets; rollback to Codex.
- **Authority boundary:** No model may lease tasks, grant approval, expand permissions, execute privileged infrastructure changes, promote research, or allocate capital. Existing deterministic policy, approval, broker, evidence, and audit controls remain authoritative.
- **Acceptance:** A reviewed architecture and benchmark report demonstrates which workloads can move from Codex without degrading correctness, evidence quality, security, or reliability. Migration occurs workload by workload only after shadow evaluation; Codex remains the fallback during transition.

## Complete remaining executable queue

The work-package contracts in
[Bible Capability Coverage](BIBLE_CAPABILITY_COVERAGE.md#4-engineering-work-packages)
all have dedicated executable packets below. They are active planned work, not an
ideas list, and their stated done boundaries must be met before completion is claimed.
The completed packets above retain their historical order. The remaining packets below
are now physically arranged in executable dependency order, not grouped merely by
domain. Their phase headings are authoritative. Within a phase, read top to bottom;
work may run concurrently only when its explicit dependencies are already complete.
The resulting path is foundation and authority, point-in-time data and laboratory,
discovery and predictive evidence, portfolio/risk/execution and demo certification,
resilient organization/platform surfaces, and finally separately governed capital
scaling. `LIVE-001` remains after `DEMO-001`; `LIVE-002` remains after `LIVE-001`.

The ordering audit also removed four impossible dependency cycles: AGT-001 now defines
the registry consumed by PLAT-002; CAD-002 produces scorecards consumed by EVOLVE-002;
SHADOW-002 produces monitoring evidence consumed by RISK-004; and EXEC-004 owns order
state consumed by the composed RISK-005 service. SEC-002 defines the baseline consumed
by PLAT-008 rather than depending on that downstream deployment package.

Parallel work is allowed only where the coverage dependency graph and the ownership
rules below do not conflict. Capital work cannot become executable merely because its
software prerequisites exist; its independent evidence and human approval gates remain
mandatory.

## Complete capability implementation packets

These packets close the planning gap between the capability map and the executable
backlog. `Status: planned` means that an existing component may be reused, but the
package is not complete until its own tests, evidence and rollback boundary pass.

#### Execution phase — Foundation, authority and safe interfaces

### PLAT-001 — Service catalog and dependency inventory

- **Status/scope/reuse/gap (2026-08-25):** Source-complete and deterministically validated in control-plane commits `2d3927355d2cddd8a94c3adb76a5ae9adcfa4c55` and `74adcf0`. PLAT-001 reuses Docker, systemd, launchd, role-deployment, fleet-observation and OPS-007 runtime truth surfaces. It adds immutable catalog snapshots, explicit activation history and a digest-bound reconciliation ledger; it does not become another deployment controller. The canonical v1 artifact describes 12 operational services across VM1, VM2 and the founder Mac with owner, recovery owner, placement, runtime kind, interfaces, dependencies, data classes, SLO and recovery plan. VM2 migration, registration, activation and first live reconciliation remain an operational acceptance step rather than being overclaimed here.
- **Contracts/dependencies:** BASE-002/003; schema `service-catalog-v1.0.0`, migration `a4c7e1f92b60`, catalog digest `793b67cf1c447887b374df53efe87bfd58bc7281ba839e9cd63402576ff9ef96`. Dependencies must be closed over the snapshot; missing owners, duplicate keys, unknown dependencies and self-dependencies fail admission. Runtime observations never mutate declared intent.
- **Tests/evidence/rollback/done:** 318 non-health backend tests passed and Alembic resolves to one head. Retained report `docs/evidence/plat001-report.json` in the control-plane repository has semantic digest `381e1aafd02e20820aaf3b53015f44679b7ba6bf300562db410f1eef5321698a`; its clean replay passes and adversarial replay detects an orphan daemon, stale observation and incompatible PostgreSQL interface. Reconciliation also covers missing/unhealthy services, dependency loss, wrong placement and runtime-kind drift. Rollback reactivates a retained immutable prior snapshot and records both identities; it never mutates running services. Source definition of done is met; production activation requires the separately governed VM2 replay.

### SEC-001 — System threat models and adversarial security suites

- **Status/scope/reuse/gap:** Complete in source and CI at control-plane merge `b881defaf83f5cf03c2a5884ac0b9a2543aa2537`. The strict `system-threat-model-v1.0.0` model reuses corpus scanners, package attestation, broker tickets, approval boundaries, service reconciliation and no-capital contracts. It covers every PLAT-001 catalog service across service, agent, research and capital abuse cases. The retained assurance report binds model digest `951e49ff0764001c94b6effda37013f45ea81314db342b60494e78387f4ba6b8` and report digest `db7e75b91110f3a64a27ef28c3b5330a3c7ba0c602bf4883bf84dc0fac816e7a`. This is control evidence, not a penetration-test certificate.
- **Contracts/dependencies:** BASE-002/003 and PLAT-001; every high-risk interface owns abuse cases, controls, detection and containment.
- **Tests/evidence/rollback/done:** Injection, exfiltration, privilege escalation, supply-chain tampering and capital-authority mutation fixtures fail closed; tampered fixtures make the suite fail; every threat declares owner, detection, containment, rollback and residual risk. Forty-two focused SEC-001, role-package, broker and no-capital tests pass; both GitHub baseline and security-assurance jobs pass and retain the digest-bound report for 90 days. Four residual risks remain explicit: uniform workflow-egress allowlisting, complete signed dependency provenance, independent dual-VM outage alerting and host-root compromise. Rollback disables the affected surface or deployment without deleting redacted evidence. Done is satisfied for the declared SEC-001 boundary; the named residual risks remain owned by later platform/security work.

### PLAT-005 — Unified observability, SLO and alert routing

- **Status/scope/reuse/gap:** Source-complete and CI-qualified at control-plane merge `8f552ba0e43144fe4888adc20a7a1f258bc480d7`. It reuses the active PLAT-001 catalog, OPS-004 authenticated fleet samples/incidents, OPS-005 backup freshness, PLAT-001 reconciliation, OPS-007 operation visibility and the existing founder outbox. Additive migration `c5e8a2f41d70` stores service SLO state, generation-aware routed alerts and immutable routing events; Mission Control and Telegram expose service, indicator, owner, severity, route and freshness. Production activation remains explicit until VM2 runs the migration/API and gateway refresh, the Mac client is reinstalled and one intended-environment breach/silence/recovery replay is retained.
- **Contracts/dependencies:** PLAT-001 and SEC-001; telemetry has bounded cardinality, redaction and stable service identity.
- **Tests/evidence/rollback/done:** Three consecutive breaches open one alert generation, three healthy evaluations recover it and recurrence increments generation. Missing telemetry and unmeasured restore objectives remain visible rather than green; a single health sample is labeled current evidence rather than historical uptime. Acknowledgement, bounded silence and unsilence retain events without changing the SLO verdict. Secret-shaped evidence is redacted and Prometheus labels are catalog-bounded. Validation passed 323 backend, 37 gateway and 71 Mission Control tests plus Ruff and JavaScript syntax; all three GitHub checks passed. Report digest `0f525ce1334705c8731b59b6fc909622fa7c7989541fe73262f6bf24c6479ded` correctly records `production_deployed: false`. Rollback restores the prior API/client images while retaining additive audit tables. The source/CI definition is done; intended-environment qualification is the remaining deployment step.

### GOV-001 — Decision rights, delegation and exception policy

- **Status/scope/reuse/gap (2026-08-25):** Completed, merged and production-activated from control-plane PR #117 at `12afe1afa46dda81bfbc35ed14428cb8ee9bed64`. VM2 runs migration `e6b1a4d82f90` and the rebuilt healthy API; policy `invariance-institutional-authority` version `1.0.0` is active with digest `4c3d868fc93d6f33b8d1197cd7b89d303a622a14770c2243ff2f02cb417bfacf`; and Mission Control was reinstalled and reads the policy. Existing approvals, role packages and broker gates remain authoritative execution controls. REST and Telegram task-approval surfaces now resolve authority before changing approval state.
- **Contracts/dependencies:** BASE-002/003; policy decisions bind actor, role, scope, risk, digest, expiry and separation-of-duty constraints.
- **Tests/evidence/rollback/done:** The merged source passed 333 backend and 71 Mission Control tests, eight-route OpenAPI verification, changed-file Ruff, JavaScript syntax and four GitHub checks. The live replay committed authorized record `83d483cc-d6f6-44ee-b330-4a4bf2eff5ba` with digest `cf7a3e8f23543d569e079aa135f02969c367241ebbf50399995131ff98bd2abf` and denied record `467f5f4a-6534-4c54-9ff1-ba0a6b00aa37` with reason `action-not-authorized`. Exact evidence and rollback boundaries are recorded in [GOV-001 completion evidence](../evidence/GOV-001.md).

### GOV-002 — Orthogonal lifecycle state machines

- **Status/scope/reuse/gap (2026-08-25):** Completed, merged and production-observed through control-plane PRs #118 and #119 at `caa9163af9033df903521858ca534f827c06dc39`. Migration `f7c2a9d41e80` adds separate `research`, `evidence`, `operations` and `capital` projections plus append-only transition events. Existing task, mission, evidence and trial states remain compatible source records; legacy objects are not silently backfilled or reclassified.
- **Contracts/dependencies:** GOV-001 and BASE-002; every explicit command binds the immutable subject digest, one projection, expected version, authority decision, actor, reason, evidence digests and effective time. Closed transition graphs, cross-dimension prerequisites and row locking forbid inferred promotion, stale writes and command-identity reuse with changed content. Per-dimension digest chains replay into the current projections.
- **Tests/evidence/rollback/done:** 347 backend and 71 Mission Control tests passed, including invalid transitions, orthogonality, prerequisite guards, stale versions, replay drift and timezone enforcement; five GitHub checks passed. VM2 migrated to `f7c2a9d41e80`, served the lifecycle API healthy, and the live five-event pilot produced dossier `c8d305c59298b2fb2ef00a502e704a27335a1070f3460c27b434aff1a9a6829c`: research `succeeded` and evidence `admissible` left operations `not-considered` and capital `no-authority`; only a separate command moved operations to `candidate`. Rollback restores the prior API while retaining additive events for a compatible projector. The declared definition of done is met; GOV-003 owns consequences such as promotion, demotion, quarantine and reinstatement.

### GOV-004 — Immutable audit and policy evidence export

- **Status/scope/reuse/gap (2026-08-25):** Completed, merged, deployed and production-observed through control-plane PR #123 at `dbed5adfb598d2ea74c6617b9e424a0e5a17370e`. GOV-004 reuses founder proposals, tasks, approval events, operational controls, the operation ledger, GOV-001 policies/decisions and GOV-002/003 lifecycle histories rather than creating a competing authority log. Migration `c1f4a7d92e60` adds append-only retained export bundles; VM2 runs healthy API image `sha256:55cbe0aa1ff2922a60e620f5c6244547fd104ff498074c33169190ff5665da24`.
- **Contracts/dependencies:** GOV-001/002/003; `governance-audit-export-v1.0.0` binds stable actor/action/object/policy/evidence fields, explicit redaction receipts, contiguous sequence, per-record predecessor hashes, terminal digest and an Ed25519 signature with embedded public key identity. Cross-stream references must close inside the bundle. Create/read/verify routes require orchestrator authentication, while the bundle itself verifies and reconstructs without database access.
- **Tests/evidence/rollback/done:** 370 backend tests and all six GitHub checks passed, including tamper, missing event, reorder, forged signature, clock disorder, redaction and fresh-client reconstruction. The live VM2 export retained 2,204 events at digest `0131f5db507c0f86f7b1399ad13069efc8ae0850929d91fb36da576b3d3fd6f9`, verified key `5f25132b5c88f6f76b3b453331526765f1418e1b8c9f481b654cd5bf8664852a`, reconstructed six lifecycle projections, matched its persisted copy and rejected a modified actor. Rollback restores the prior reader/API and retains the additive table and signed bundles. The definition of done is met; this export grants no execution, deployment, capital or order authority.

### AGT-001 — Agent charter, capability and grant registry

- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, deployed and production-observed through control-plane PRs #124 and #125, ending at `d4915acbcbdc259d119553cc3d7842d87649bc88`. AGT-001 reuses agent registrations and signed package deployments, adding immutable versioned charters, separately revocable time-bounded per-capability grants, digest-chained grant events and Mission Control inventory visibility. VM2 runs migration `e8b3d6f02a50` and healthy API image `sha256:1b0d10d6c5c99996fe99ff42781e36bc434a55c60b44a0f04c38c11a5d0d94f4`; Mission Control was reinstalled and live-verified on Mac.
- **Contracts/dependencies:** GOV-001/002 and PLAT-001 remain the authority and platform prerequisites. Every task lease now intersects enabled registration, active charter, newest active exact package deployment and unexpired scope/risk grant, retaining charter/package/grant/accountable-owner digests in the lease event. Package replacement, conflict, prohibition, expiry, revocation or mismatch fails closed. PLAT-002 consumes this registry for workload identities; no charter or grant implies capital allocation, order placement or live-trading authority.
- **Tests/evidence/rollback/done:** 375 backend and 71 Mission Control tests passed, scoped Ruff was clean, and a clean PostgreSQL rehearsal reached `d7a2c5e91f40`. Production exposed and closed a multiple-active-deployment ambiguity by binding grants to exact packages. The final replay allowed snapshot `7dec6c307ceef04eca76eaadd034c418767340ce3492cd97a4c6cf9d81933223`, then revocation denied the same request with snapshot `51b60b92b75b53b4c99a70cf4a4c232c76b2f640ea78e0589e93b5ec0ec5ab46`; fleet bootstrap covered 14 agents with 41 grants and an immediate replay created zero records. Rollback revokes a grant/package while retaining history. The least-privilege lease boundary is complete.

### PLAT-002 — Workload identity, authorization and secrets lifecycle

- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, deployed and production-observed through control-plane PRs #126-#129, with implementation head `832d83d4c46e9a13b76a4fec4bb618d3dbdfe057` before the evidence-only merge. PLAT-002 reuses HMAC agent credentials, root-owned secret files, GOV-001 authority and AGT-001 exact-package charters/grants. It adds immutable workload identities, central path-to-scope authorization, bounded credential overlap/finalize/rollback, logical secret-policy registration/rotation/revocation, redacted authorization receipts and reduction-only emergency grants. It does not store or distribute secret values and grants no capital or order authority.
- **Contracts/dependencies:** Each identity binds agent, exact charter/package digests, machine, control-plane audience, wildcard-free scopes, accountable owner and 90-day expiry. Authentication revalidates active charter, package deployment and the complete unexpired grant set on every request. Activation requires coverage of every non-revoked credential attached to an active package. Secret policies retain only logical references and lifecycle metadata. Emergency access requires distinct founder/reviewer identities, expires within one hour and is limited to halt, isolate or revoke actions.
- **Tests/evidence/rollback/done:** 396 backend/Mission Control tests, all seven GitHub checks, Ruff, compileall, JavaScript syntax and a zero-to-head PostgreSQL rehearsal passed. VM2 runs migration `f3a7c1d92e60` and healthy image `sha256:0d6be1cde4141e1fba829761e6b3ab1a1e8cd30d01b93e8461a47c22edb1a4d3`; Mac Mission Control runs Python 3.11.7 and exposes all 14 identities. Bootstrap digest `1a1cf583746e13a3bedb511f616664460ab4c9702dbbcdba85278c30e90105b0` proves an idempotent replay created and rebound zero records with zero uncovered credentials. Pilot digest `ae388619c5987dc231974fa26fc61a5eecd6b749fb02e9efb31f3d26bfcecad0` proves scoped allow, confused-deputy denial, redaction, secret rotate/revoke, privilege-expansion denial, reduction-only emergency revoke and credential rollback/revocation. Rollback restores only the prior scoped credential inside its overlap window. The definition of done is met.

### AGT-002 — Provenance-bearing agent context and working memory

- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, deployed and production-observed through control-plane PRs #130-#132, with implementation head `e70ef16208a75d7898f9bec9ed3ce1718fa4e28d`. AGT-002 reuses canonical RI evidence/lifecycle/graph records, task attempts, AGT-001 authority and isolated worker workspaces. It adds immutable task-attempt context manifests, exact rendered-pack replay, selection/sensitivity/expiry/prompt-position provenance, selected contradiction disclosure, digest-only scratch receipts and terminal scratch disposal. It does not add a second corpus, retain hidden chain of thought, or grant execution, capital or order authority.
- **Contracts/dependencies:** Every manifest binds task, agent, next unconsumed attempt, live charter/package/grant resolution digest, purpose, exact rendered pack digest, manifest digest and expiry. Sources must be active, unique, position-contiguous, within the task/project and explicit task access classes, and under 32 items/64 KiB by default. Protected evidence always requires a separate future disclosure path. Opt-in tasks set `governed_context_required=true`; after lease, the worker fetches the bound manifest and writes it once as mode `0600` outside the checkout before execution. Working-memory content stays inside the attempt workspace; Hermes records only digest, safe relative path, sensitivity and expiry.
- **Tests/evidence/rollback/done:** The 386-test backend suite and 32 directly affected worker tests passed, along with all seven CI gates, scoped Ruff, compileall and diff checks. Tests cover contamination, inactive/protected sources, contradictions, access bounds, ambiguous positions, oversized packs, unsafe scratch paths, integrity replay and complete/fail/release disposal. VM2 runs migration `a2d6f9c41e80` and healthy image `sha256:0bfe3e758be878a6a097f3e3700e81a140c8d75e5f2f813e08bcca67a37fb5be`. Live report `e8e6992f5850fab832990c3694e8ebaef8d88daf028d9bab6d34074f3bfccc19` proved real authority/source binding, exact replay and one discarded digest-only scratch receipt on a cancelled non-leaseable task. Rollback stops new opt-in manifests and discards workspaces/receipts while retaining canonical evidence and immutable context history. The definition of done is met.

### AGT-003 — Typed task graphs and bounded deliberation

- **Status/scope/reuse/gap (2026-08-27):** **Completed, merged, deployed and production-observed.** Control-plane PR #133 merged as `283fc415432fa6a124befa2eaad5c9843ed5fd8e`; evidence PR #134 retained the live receipt. AGT-003 reuses ordinary governed tasks, dependencies, approvals, authority snapshots, context, leases and the Mission Supervisor. It adds immutable typed DAG manifests, typed digest-bound messages, graph-level node/attempt/duration/parallelism bounds, cooperative cancellation, deadline/deadlock termination, reverse-order compensation and hash-chained graph replay. It does not retain hidden chain of thought or grant execution, deployment, capital or order authority.
- **Contracts/dependencies:** AGT-001/002 and OPS-001 remain prerequisites. Each node declares role, typed input/output, task contract, stop conditions, dependencies and optional compensation. Activation materializes normal tasks and `task_dependencies`; leasing enforces graph parallelism alongside existing machine, capability, package, grant, risk and approval checks. Running cancellation is returned by heartbeat, queued cancellation is immediate, and completion racing after cancellation is rejected. The Mission Supervisor reconciles active graphs even without further worker traffic.
- **Tests/evidence/rollback/done:** 393 backend tests and 18 restricted-worker service tests passed; clean PostgreSQL 16 migration replay reached `b3e7a1c52d90`. VM2 runs that migration and healthy image `sha256:598ed40a60b22798e7d1640e396be4c2725b4bf9fb77901cf7db134afc3a11b5`. The live two-node replay cancelled both nodes before lease, retained typed message and hash-chain evidence, and reported digest `3db36e82c88622629381137bf89ce072620489b9027f677609ee1cae8a614295` with execution/capital authority false. Tests reject cycles, missing edges, duplicate nodes and runaway attempt declarations, and cover canonical digesting and cooperative cancellation. Rollback cancels unfinished nodes and materializes declared compensation tasks for successful side effects. The definition of done is met for bounded graph orchestration.

### AGT-004 — Prompt, policy and model-output security registry

- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, deployed and production-observed through control-plane PRs #135-#136 at head `88fab852455791385346e90f5eb1f4f8d11de715`. Reuse package manifests, input validation and corpus scanning. The implementation adds immutable semantic-versioned prompt/policy bundles, exact provider/model/runtime/version bindings, trust labels, tool/data allowlists, fail-closed input/output schemas, forbidden-pattern and authority-field gates, append-only evaluation/event receipts, independent-review promotion and prior-version retirement. Model output remains `data_only` and cannot grant execution authority.
- **Contracts/dependencies:** AGT-001/002 and SEC-001; prompts bind model/runtime/version and outputs validate against schemas before becoming data or actions.
- **Tests/evidence/rollback/done:** The 397-test backend suite and idempotent replay tests pass. Adversarial coverage rejects injection, exfiltration, instruction collision, authority-bearing fields and malformed/confident outputs. Promotion requires valid-output plus all adversarial categories and an evaluator independent of the producer. VM2 runs migration `c4f8a2d61e90` and healthy API image `sha256:fdff00991e70d7e7939be8cd9ea60a53b47396630c5d820d6036038af94abeda`. Active bundle `12d23600-6ee5-401b-b43e-0f016641e046` has digest `b00090c9cef72f22eeb56b096854f48bfe81ffefcd4f7b48b2a6ff9a28cf81e3`; all five required evaluation categories passed, its nine-event chain is retained, and action authority is false. Report digest is `8fc5f2047ebce3be5d9f204e05eef1aadebc029d1c3e4bafc99f0cba9aa99c99`. Rollback retires the current version and reactivates a previously qualified digest through a new governed event. The declared definition of done is met.

### AGT-006 — Independent evaluator routing and anti-collusion

- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, deployed and production-observed through control-plane PR #138 at `ca8325afd1cf5af9aff5cee41c98ecd83140bba1`. AGT-006 reuses the existing M13 statistical reviewer and adversarial auditor rather than creating duplicate agents. It adds immutable versioned evaluator profiles, deterministic digest-bound routes, one evaluator per review kind, append-only route events, assignment completion restricted to the routed agent, and a final independence receipt. VM2 runs migration `d5a9c3e72f10` and healthy API image `sha256:c1bd88e3a5f927da5e7e0565bac095f7d7368e3ef60476bcf0bb862ff4c7a07e`.
- **Contracts/dependencies:** GOV-001 and AGT-001/003 remain prerequisites. Active profiles are derived from enabled agent registrations and exact active role-package deployments. The router hard-rejects reuse of producer/reviewer or reviewer/reviewer agent identity, package digest, or context group. Machine, provider, model family and runtime are measured correlation dimensions: they are scored, constrained by a pairwise ceiling and disclosed in receipts, never silently called independent. The assertion endpoint fails closed until all routed review digests are complete and grants no execution, promotion, deployment, capital or order authority.
- **Tests/evidence/rollback/done:** The 403-test backend suite passes; focused tests cover producer self-review, shared package/context, evaluator reuse, pairwise correlation ceilings, unavailable evaluators, routed-agent-only completion and incomplete-promotion blocking. Live route `68fd264d-f956-477a-8d8c-90946d5a7716` completed both reviews across two agents and package digests and issued receipt `9ed893dd2c37fd7cc51605416966ccbd5cd2e41a6e5b53d0a4e333f69b221d86`; the zero-shared-dimension control blocked honestly. Root-owned evidence is `/var/lib/invariance-swarm/agt006/report.json`, canonical report digest `9f5462ac1c665c1b878086d6662c309f58ab8e92247e70e4ff25f80f4eb5169a`, with action authority false. Rollback removes the API consumer while preserving additive routing evidence and blocks promotion pending governed human review. The definition of done is met.

### UI-004 — Digest-safe approval center

- **Status/scope/reuse/gap (2026-08-27):** **Completed, merged, deployed and production-observed.** Control-plane PRs #140-#142 landed the implementation, production-depth latency correction and evidence at head `8b10bc5ed23d71cda10fc34f708af0e6527ac357`. UI-004 reuses task approvals, OPS-001 notification generations, GOV-001 authority resolution and Mission Control. It adds a canonical approval-center envelope covering the full task contract, current plan/scope, risk, prerequisites, mission readiness, active authority-policy digest, notification generation, blockers and bounded effect. Mission Control renders ready, blocked and decided states, requires explicit digest acknowledgement and exposes no enabled approve command for an ineligible gate.
- **Contracts/dependencies:** The decision request must echo the exact server-computed `review_digest`. Under a row lock the API recomputes the envelope, rejects stale reviews with `approval-review-superseded`, and rejects non-actionable approvals with explicit blockers. A successful decision retains `approval_center_decision_receipt`, binding approval, task, action, actor, plan/review digests, reason digest and bounded expiry. Review links carry only an approval identifier and reopen freshly fetched read-only state; they carry no token, action or digest. Approval grants one bounded task lease, never broader execution, deployment, capital or order authority. Every pending gate is visible; only the 25 most recent decided envelopes are hydrated in the overview while historical counts and exact receipts remain complete.
- **Tests/evidence/rollback/done:** 407 backend tests and 72 Mission Control tests passed, including changed-contract, stale-digest, receipt and outbound-digest cases; JavaScript syntax and desktop browser QA passed. VM2 ran healthy at source `6235b40f660624b41d4067ab3a462e3c273944f4`; the bounded center returned 31 pending/recent envelopes in 0.858 seconds. Mac Mission Control was reinstalled and its loopback LaunchAgent recovered cleanly. It reported 16 historical pending gates, all blocked and zero actionable. The no-authority pilot rejected a stale digest, then retained rejection receipt `af6e654a27f3cb22aa0bb6913fb857965ac70317a8081ae4b52b36429e42cdcd`; report digest `043859a3074955fe5b5b68ce21488ee6bd75606267705d08f438ad7c586f52a6`. Rollback removes the new Mission Control mutation route while preserving legacy digest-bound Telegram approvals and all receipts. The stated definition of done is met.

### CHAN-001 — Restricted Telegram founder channel

- **Status/scope/reuse/gap:** Completed and production-qualified on 2026-08-27 at `swarm-control-plane` merge `4557667ce42d1d95684f931b57d557cc0bdab42b`; reuses the gateway, CHAN-002 threading, OPS-006 planner, founder outbox and digest-bound approvals.
- **Contracts/dependencies:** OPS-001/002, UI-004 and AGT-004; plain English creates proposals, non-executable requests ask questions, and secrets/sudo are prohibited.
- **Tests/evidence/rollback/done:** Forty-one gateway tests cover spoofed user, replay, flood, stale link, outage, clarification, secret non-retention and Telegram-send/control-plane-ack recovery without duplicate delivery. Hash-chained events retain only redacted classifications. The VM2 service entered `active/running`, emitted `telegram_gateway_ready`, retained zero post-activation restarts, verified its genesis audit chain and completed a founder-owned `/status` replay without creating work or authority. Rollback disables decision commands while status/alerts and durable state remain. Done.

#### Execution phase — Point-in-time data and deterministic laboratory

### DATA-001 — Point-in-time instrument and reference-data service

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** The deployed Hermes temporal identity registry remains the canonical governance slice. Completion now requires a Bulletproof-native point-in-time instrument/reference-data exporter that emits immutable identity receipts consumed and independently validated by Hermes.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, deployed and production-observed through control-plane PRs #145 and #146, ending at `24b765796550f3758faecf52965858ce726879c1`. DATA-001 reuses Bulletproof symbols, venue metadata and dataset manifests while adding one canonical temporal identity service rather than another symbol map. VM2 runs migration `e2d7a4c91b60`; the rebuilt API is healthy and exposes immutable snapshot registration/list/get plus point-in-time resolution.
- **Contracts/dependencies:** After BASE-002, expose effective-dated instrument, venue, session, corporate-action and reference-data records consumed by DATA-002, BT-004 and EXEC-001/003. Unknown or conflicting identity fails closed.
- **Tests/evidence/rollback/done:** The implementation separates market-effective from knowledge-availability clocks, binds dataset manifests to stable instrument/listing identities, rejects overlapping or unknown identity, and supports ordered immutable supersession. The full backend suite passed 418 tests; the live no-capital pilot passed stable identity, old/new symbol replay, known corporate actions, holiday closure, digest binding and unknown-identity fail-closed checks. The retained snapshot digest is `16c689717341872f0b15d0324122ddbc749d2174197d8f3f4ea7faadf75e3871`; evidence is [DATA-001 completion evidence](evidence/DATA-001.md). Consumers can roll back by pinning the prior immutable snapshot. No order or capital authority was added.

### DATA-002 — Immutable market-data catalog and availability ledger

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** The deployed Hermes catalog registry remains valid. Completion requires Bulletproof to publish authoritative content, partition, correction and knowledge-time availability receipts from its actual data lake; Hermes must verify and catalogue those receipts without reconstructing the catalog scientifically.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, deployed and production-observed through control-plane PRs #147 and #148, ending at `7169d616e80b04f44badff88d647f9e6f9e390b0`. DATA-002 reuses BT-002 content digests, partition integrity counts and correction lineage, then extends them into one canonical raw/curated catalog with effective universe membership and source-availability history. VM2 runs migration `f3e8b2c61d90`; the rebuilt API exposes immutable catalog snapshot register/list/get and point-in-time resolution.
- **Contracts/dependencies:** DATA-001 identities plus content-addressed partitions, observation/availability timestamps, correction ancestry and read-only source access; BT-006/007 and ML-002 consume only registered snapshots.
- **Tests/evidence/rollback/done:** Catalog registration verifies every venue, stable instrument and listing against the exact DATA-001 digest. Resolution proves event coverage, knowledge-time availability, effective membership, read-only access, zero duplicate/gap admission counts and latest known correction ancestry; missing, delayed, ambiguous, conflicting or future data fails closed. The full backend suite passed 429 tests and the live eight-gate pilot replayed original and corrected generations. Current catalog digest: `3c5352526ef607d02502144cf8623dc53098322c4bf84f8395e0650384aa2e07`; prior rollback digest: `981c671b9959461804701c9b9661398b2b68b873f837f5762549f16a5ab233e4`. Evidence is [DATA-002 completion evidence](evidence/DATA-002.md). No data-write, execution, order or capital authority was added.

### DATA-003 — Data quality, lineage, entitlement and lake operations

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes retains entitlement, retention, admission and recovery governance. Bulletproof must produce the authoritative lake scan, lineage, quality and availability evidence over native partitions; a Hermes metadata fixture cannot close this packet.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, deployed and production-observed through control-plane PRs #149, #150 and #151, ending at `29ff827a64d9b38fb4555939aedde0ca9603c44d`. DATA-003 reuses DATA-001 identities, the DATA-002 immutable catalog, BT-002 integrity metadata and existing backup evidence. It adds one metadata-only governance snapshot and append-only lake-operation ledger rather than duplicating source storage or catalog ownership. VM2 runs migration `a4f9c3d72e10`; the healthy API exposes admission, snapshot, event, publication-disable and verified-restore routes.
- **Contracts/dependencies:** Every snapshot binds an exact DATA-002 catalog digest plus quality SLOs, lineage edges, default-deny principal/action/purpose entitlements, storage budgets, retention holds, recovery manifests and derived publications. Admission fails closed for schema, duplicate, gap, freshness, entitlement and exhausted-capacity violations. Protected source payload is forbidden by strict schemas; source partitions remain immutable and read-only. Publication disable and restore emit digest-chained events, and exact restore requires a disabled publication, verified backup, matching catalog digest and exact object set.
- **Tests/evidence/rollback/done:** The focused DATA suite passed 41 tests and the full backend suite passed 442 tests with two warnings. The live pilot bound snapshot `0acbf36c-29d4-427d-a83b-f943b004d3ba` (`5fe1a1999733551358b09f72f32c4f67dd21c6f144de4eeb5ba0ad9edb27fc03`) to catalog `3c5352526ef607d02502144cf8623dc53098322c4bf84f8395e0650384aa2e07`, retained six append-only events and passed nine checks covering clean admission, corrupt and unknown-principal denial, retention-held deletion denial, capacity warning, disable, exact verified restore, event visibility and protected-payload absence. Rollback disables the derived publication and restores its last exact verified manifest; it never rewrites source data. Evidence is [DATA-003 completion evidence](evidence/DATA-003.md). No source-write, execution, order or capital authority was added.

### BT-004 — Event-driven causality, accounting and deterministic state

- **Status/scope/reuse/gap (2026-08-24):** Completed and merged in Bulletproof PR #267 at commit `2d315a2295d5a1aeafd6332fac4a8fa03eaa98a2`. The classic engine remains the only authority. BT-004 adds canonical two-clock event envelopes and ordering, future-information rejection, accounting invariants, digest-chained transitions, dataset/config/version/state-bound checkpoint validation, stable equal-timestamp symbol emission and a tightly bounded floating-point threshold fix. Retained evidence is `docs/bt-004-validation.md`; the pinned Python 3.11 suite passes 1,231 tests with 27 explicit skips, all CI shards pass and scoped Ruff is clean.
- **Contracts/dependencies:** Requires BT-001/002/003 and DATA-001/002. Define canonical market, decision, order, fill, funding, borrow, valuation and session events; stable tie-breaking; closed-bar visibility; point-in-time joins; cash/position/PnL invariants; seeded randomness; checkpoint/resume identity; and an explicit unsupported-mode failure. BT-005/006/009 consume this contract without bypassing it.
- **Tests/acceptance:** Add golden portfolios, differential comparisons against trusted existing runs, property tests for conservation/accounting, permutation tests for equal timestamps, future-data and incomplete-bar traps, gaps, duplicate/out-of-order events, funding boundaries, liquidation, restart and cross-process determinism. Any classic/legacy discrepancy must be explained and approved, never tolerance-hidden.
- **Evidence/rollback/done:** Retain environment and dataset pins, golden digests, differential/property/causality reports, checkpoint replay and an intentionally rejected leakage case. The completed fixture retains a fixed state digest, every equal-time event permutation, a rejected future-funding observation, accounting drift, checkpoint pin/tamper failures, transition replay, input-row permutation and full classic-engine regression receipt. Rollback removes certification admission while retaining the unchanged classic engine and all evidence; incompatible checkpoints fail closed. Done is met when identical inputs reproduce the declared state/run digest and no certified decision observes unavailable information.

### BT-005 — Calibrated market, execution-cost and diagnostic models

- **Status/scope/reuse/gap (2026-08-24):** Completed and merged in Bulletproof PR #268 at commit `d633c22207b16a9dbc3b6b809b0c16808ed9ae08`. The classic fee, spread, slippage/impact, bar-delay, fill, reconciliation and diagnostic implementations remain authoritative. BT-005 adds immutable versioned model cards and bundles with explicit capability boundaries; it does not create a parallel execution-cost engine or invent empirical calibration. Rebates, funding cashflows, borrow and capacity-constrained fills are recorded as unsupported and fail closed. Retained evidence is [BT-005 completion evidence](evidence/BT-005.md) and Bulletproof `docs/bt-005-validation.md`.
- **Contracts/dependencies:** Requires BT-004 and DATA-001/002. Every model declares applicability, calibration sample, timestamp semantics, parameters, uncertainty, fallback and incompatibilities; each run bundle binds model versions. EXEC-005 and ML-005 may extend calibration but cannot mutate past assumptions.
- **Tests/acceptance:** Cover no-fill/partial-fill, gaps, spread crossings, fee tiers, funding timestamps, unavailable borrow, extreme impact, benchmark comparison and pessimistic stress. Compare modeled outcomes with retained observed fixtures and prove worse assumptions cannot improve net results through an accounting defect.
- **Evidence/rollback/done:** Atomic finalization requires `market_model_bundle.json`, validates every card and bundle digest, and matches it to `market_model_bundle_digest` lineage. Empirical cards cannot omit their calibration digest; declared policy profiles cannot masquerade as observations. Pessimistic cost stress is monotone. Rollback pins the prior model and marks dependent results superseded if necessary. The pinned suite passes 1,237 tests with 27 explicit skips; completion does not claim that the currently unsupported funding, borrow, rebate or capacity mechanics have been implemented.

### BT-006 — Registered experiment grids, search accounting and budgets

- **Status/scope/reuse/gap (2026-08-24):** Completed in Bulletproof PR #269, merged as `83b08dbca0a8ca357337987b9972767f80769ddd`. Existing hypothesis contracts, constraint filtering, parallel execution, strict resume and resource controls remain authoritative. BT-006 adds an immutable prospective search-plan compiler, registered-manifest admission, deterministic family/trial/seed identities and a SQLite execution ledger without replacing Hermes' institutional Trial Registry. Retained evidence is [BT-006 completion evidence](evidence/BT-006.md) and Bulletproof `docs/bt-006-validation.md`.
- **Contracts/dependencies:** Requires BT-002/003/004 and RI-004. A search plan binds hypothesis, dataset, code, parameter schema/values, Cartesian count, seeds, tiers, resources, stopping rule and family ID before execution. Retries retain trial identity; expansions create a new approved plan.
- **Tests/acceptance:** Test invalid/unbounded grids, hidden optimization, duplicate trials, partial completion, resume, worker loss, budget exhaustion, deterministic ordering, family expansion and multiple-testing ledger completeness. No unregistered exploratory result may enter promotion evidence.
- **Evidence/rollback/done:** Search plans retain raw Cartesian size, exact constraint-filtered variants, excluded count, tiers, seeds, resources, budgets and stopping rules. Empty, duplicate, non-finite, over-budget and outcome-stopped plans fail closed. Retries retain trial identity and consume bounded attempts; expansions create new plan and trial identities; cancellation touches only unleased trials. Registered manifests and atomic run bundles bind plan, family, trial, seed and attempt. Rollback cancels unleased work and preserves consumed budget/history. The pinned suite passes 1,245 tests with 27 explicit skips.

### BT-007 — Representation, label, feature and fit-boundary contracts

- **Status/scope/reuse/gap (2026-08-24):** Completed in Bulletproof PR #270, merged as `476c50147eb6032425087f87049743aef9dd3977`. Existing immutable dataset snapshots, canonical research panels, state-feature builders, hypothesis schemas and classic strategy implementations remain authoritative. BT-007 adds a digest-bound representation contract, causal frame auditor, fresh-process certification CLI, BT-006 search-plan binding and mandatory BT-003 run-bundle evidence. Retained evidence is [BT-007 completion evidence](evidence/BT-007.md) and Bulletproof `docs/bt-007-validation.md`.
- **Contracts/dependencies:** Requires DATA-001/002 and BT-004; ML-002/003 and BT-009 consume versioned feature/label manifests. Each field declares source, transformation, observation/availability clock, warm-up, missingness, fit window, embargo and artifact digest.
- **Tests/acceptance:** Include future joins, revised data, incomplete higher-timeframe bars, overlap, purge/embargo, universe leakage, global normalization, missing values, fit-on-evaluation and deterministic transform fixtures.
- **Evidence/rollback/done:** Representation manifests bind dataset/code, decision and universe clocks, source fields, transformation/version/implementation digest, observation and availability clocks, warm-up, missingness, completeness, fit policy/state, label horizon and split/purge/embargo boundaries. Leakage reports reject future/revised inputs, premature labels, incomplete bars, warm-up output, undeclared missingness, duplicate identities, universe leakage, overlap and evaluation fitting. Search plans bind the representation digest; atomic bundles require the matching contract and certified report. Rollback pins an earlier transform while marking descendants stale. Done when a fresh client reconstructs and certifies every declared model/strategy input using only information available at its decision time.

### BT-008 — Laboratory API and Research Intelligence publication

- **Status/scope/reuse/gap (2026-08-24):** Completed in control-plane PR #90, merged as `0447493ce334768798aa43a630ff87f8d2961d40`, and Bulletproof PR #271, merged as `4b2b0a2d3af17264a9e88c38bec85afb22de2d1c`. BT-008 reuses the existing trial registry, BT-003 bundles, canonical evidence, RI graph/retrieval projections and Bulletproof SQLite research memory. It adds one idempotent publication saga rather than a parallel experiment or artifact registry. Retained evidence is [BT-008 completion evidence](evidence/BT-008.md), control-plane `docs/bt-008-validation.md` and Bulletproof `docs/hermes_laboratory_publication.md`.
- **Contracts/dependencies:** Requires RI-001/004/008/010 and BT-003/006/007. The API validates trial, repository, dataset, model and bundle digests; records publication/compensation state; writes canonical evidence before rebuilding derived projections; and returns dual-memory receipts.
- **Tests/acceptance:** Test duplicate and concurrent publish, corrupt/incomplete bundle, unknown trial, digest mismatch, negative/invalid outcomes, partial Hermes or Bulletproof failure, retry, supersession, deletion hold and projection rebuild failure. Citation replay must reach source data, code, configuration and reviews.
- **Evidence/rollback/done:** The API atomically retains canonical result, two independent reviews, decision, replay dossier and ordered event transcript, then accepts only current graph/retrieval receipts before a digest-bound Bulletproof memory receipt. Negative, null, invalid and inconclusive outcomes use the same path. Projection or memory failures remain resumable without deleting canonical evidence. Rollback disables new intake and rebuilds derived state from canonical records. The Hermes suite passes 301 tests; Bulletproof's deterministic CI matrix passes 1,262 tests with 27 explicit skips at the completion pins.

#### Execution phase — Discovery and predictive evidence

### DISC-002 — Observation, anomaly and opportunity mapping

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes owns the evidence ladder, review state and immutable map. Bulletproof must produce the baseline, effect, uncertainty, regime-control, cost and net-effect receipts from native datasets before an observation or opportunity map is scientifically qualified.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, deployed and production-observed through control-plane PRs #152, #153 and #154, ending at `aba734c3a346f53c3c36c4042aa33b83e5561d11`. DISC-002 reuses DISC-001 daily cycles, RI canonical evidence and DATA-002/003 catalog and admission receipts. It adds one immutable map and event service rather than another question scheduler, evidence store, backtester or signal generator. VM2 runs migration `b5d8e2f41a70`; the healthy API exposes registration, replay and event-chain routes.
- **Contracts/dependencies:** Maps form an explicit `observation -> anomaly -> mechanism -> opportunity` evidence ladder. Every revision binds a real daily cycle, exact point-in-time population, DATA-002 catalog, successful DATA-003 admission, baseline, effect, uncertainty, regime controls and canonical evidence IDs/digests. Anomaly requires a passed null control; mechanism requires a causal story, rivals and falsification; opportunity additionally requires at least two differently produced evidence objects, non-zero incremental effect and exactly reconciled positive net effect after transaction, financing and impact costs. Semantic duplicates fail closed, protected market payload is forbidden and replacement occurs only through immutable supersession.
- **Tests/evidence/rollback/done:** The focused suite passed 10 tests and the full backend suite passed 450 tests with two warnings. The live pilot rejected a cost-erased candidate, registered qualified map `358f8ec0-700e-4c39-af52-b2515b54cf7c`, and superseded it while retaining the original digest chain. Map digest: `c68df954976315f42ecce88eb974e56f0467a50aa11f457c500e9ad83eceff3a`; report digest: `fa46dcb44d1a913b72193f114cc69148dbf0a5f1e0bb4a832a60fb70cfa8db9d`. Rollback supersedes a map with a corrected or rejection revision and never deletes evidence. Completion evidence is [DISC-002 completion evidence](evidence/DISC-002.md). No source-write, strategy-execution, order or capital authority was added.

### DISC-006 — Mechanism and falsification service

- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and live-replayed through control-plane PRs #155-#161, ending at `fe817cd2234c58a4b31f5bb31e1a1acfc30e3143`. DISC-006 reuses RI dossiers/oppositions, canonical evidence, the hypothesis registry and active DISC-002 mechanism/opportunity maps. It adds immutable preregistered mechanism plans and independently evidenced evaluations rather than another hypothesis, evidence or execution store. VM2 runs migration `c6e9f3a52b80` and exposes plan/evaluation registration and replay routes.
- **Contracts/dependencies:** Every plan binds an active DISC-002 map, registered hypothesis, frozen dossier, opposition records, evidence cutoff, causal mechanism, assumptions, competing explanations/confounders and decisive tests. Prediction, null and falsification conditions must differ; every rival must be covered. Evaluations postdate registration, bind the exact plan digest, cover each test once, cite canonical evidence ID/digest pairs and state every rival outcome.
- **Tests/evidence/rollback/done:** Tautologies, uncovered rivals, absent provenance, post-hoc evidence, incomplete outcomes and digest drift fail closed. Any failed decisive test produces `falsified`; support requires every test to pass and every rival to be ruled out; all other complete records remain `unresolved`. Reassessment is immutable supersession, never deletion or conclusion mutation. The full backend suite passed 462 tests with two warnings and the focused suite passed 10 tests. The VM2 pilot retained falsified evaluation `64195922-e004-4ae9-a091-8236a89cdb22`, then superseded it with unresolved evaluation `65e61ffe-9fcf-46dd-bb51-7bc1fb02e2ee`; report digest `264960712733bbec083fa443e85930a5dcc38ecaac1a330faddd48fc68f59a7b`. Completion evidence is [DISC-006 completion evidence](evidence/DISC-006.md). No source-write, strategy-execution, order or capital authority was added.

### DISC-007 — Selection-bias and research-overfitting auditor

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes keeps the immutable audit and institutional gate. Bulletproof must natively compute and emit the complete-family multiplicity, rank/PBO and selection-adjustment receipt from its retained search ledger; the control plane may independently cross-check but cannot be the sole statistical producer.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and live-replayed through control-plane PRs #162-#165, ending at `86c7f4f38e60f5393e6f061ba7e3c7494d41ad9e`. DISC-007 reuses BT-006 complete search-family ledgers, DISC-006 mechanism evaluations and the existing research registry. It adds one immutable institutional selection audit rather than another trial runner, optimizer or result store. VM2 runs migration `d7f1a4b63c90`; the healthy API exposes authenticated audit registration and replay.
- **Contracts/dependencies:** Every audit binds a retained mechanism evaluation and canonical full-family ledger digest. The ledger contains every planned trial including failures/cancellations, exact specification digests, preregistered stopping rule, declared and observed researcher operations, winner identity and complete-family validation-split ranks. Multiplicity cannot be reduced below the planned family; alpha cannot exceed 0.05 and PBO tolerance cannot exceed 0.5. The service computes Bonferroni family-wise p, Benjamini-Hochberg discoveries, an explicitly diagnostic extreme-value selection-adjusted/deflated Sharpe and split-rank PBO. Optional stopping, favorable family truncation and undeclared researcher degrees fail closed.
- **Tests/evidence/rollback/done:** The full backend suite passed 475 tests with two warnings and the focused suite passed 13 tests covering omitted trials, invalid non-results, digest drift, correction gaming, optional stopping, metric shopping, PBO, correction and supersession. The VM2 pilot retained two completed, one failed and one cancelled trial; nominal winner p-value `0.02` became family-wise p-value `0.08` and `selection_risk_detected`. Audit `45b83a75-8831-4ced-a0f3-93a5d78e981e`, audit digest `f8bf5a21bf539e0b4e46cf4b54405d0cd4e0fcaa9d0a1c47950d43ec487dd62f`, report digest `bad4c9db76f3aceec9a06cc8652519707c517e5e223e3434f56a9867b71ed8a0`. Corrections use immutable supersession and retain all attempts. Completion evidence is [DISC-007 completion evidence](evidence/DISC-007.md). No promotion, strategy-execution, order or capital authority was added.

### DISC-003 — Representation and factor experiment language

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes may register and policy-check factor programs. The authoritative parser/compiler, unit/clock validation and executable trial-spec receipts must live in Bulletproof and feed its classic engine; the control-plane compiler is provisional validation only.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and live-replayed through control-plane PRs #166-#168, ending at `4cbe803278cf3b9d030ea05bdcca5f2e18ab5762`. DISC-003 reuses registered hypotheses, DATA point-in-time manifests and BT-007 representation contracts. It adds one closed factor-program language and immutable compiler registry rather than a second backtester, arbitrary-code generator or optimizer. VM2 runs migration `e8a2b5c74d10` and the healthy API exposes authenticated register/list/replay routes.
- **Contracts/dependencies:** Every program binds a registered hypothesis, registered point-in-time dataset-manifest digest and retained representation-contract digest. Fields declare unit, domain, clock and availability lag. Features are allowlisted expression ASTs with no imports, paths, network or dynamic evaluation; effective feature lag must be at least one decision interval, while forward observation is isolated to the explicit label. Operators are unit checked, expression depth is bounded, grids contain distinct finite values, and `maximum_trials` bounds Cartesian expansion. Canonical source, semantic, compiled and per-trial digests make aliases, replay and downstream BT-006 registration inspectable.
- **Tests/evidence/rollback/done:** The full backend suite passed 483 tests with two warnings; the hardened focused suite passed 9 tests. The live VM2 pilot bound hypothesis `7570465c-2389-4878-a936-38bb895ab1b8`, dataset manifest `f88d456ba2a2585d6c33852296cca8b5e454515cb4a623f8cb61a688110d41f6` and representation contract `dfde67369923bf5eb84d0f248e1ef9297aaf934bebed752cb5f6c3337561b798`; it rejected an unsafe current-bar control and compiled four trials under digest `09c91fd6710454f1a10acca4d9fc63cc91290495d7bbdac0619c40fb5b3de95e`. Rollback pins a prior language/compiled digest and retains immutable records. Completion evidence is [DISC-003 completion evidence](evidence/DISC-003.md). No execution, selection, promotion, order or capital authority was added.

### DISC-004 — Budgeted statistical search services

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes owns budget authorization, scheduling and the append-only campaign ledger. Bulletproof must authoritatively generate proposals from the finite trial universe and emit deterministic search-state receipts; Hermes must not become the optimizer.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and live-replayed through control-plane PRs #169-#170, ending at `513f497dd6ce7a63416899eb14b8de1fbd6a1bde`. DISC-004 reuses immutable DISC-003 trial universes and BT-006 complete-family doctrine. It adds one digest-chained campaign/proposal service rather than a runner, optimizer with hidden state, result store or alternate execution truth. VM2 runs migration `f9b3c6d85e20`; the healthy API exposes campaign, proposal, observation, cancellation and verified event-replay routes.
- **Contracts/dependencies:** Exhaustive, structured, seeded random, Bayesian surrogate and evolutionary neighborhood methods share one contract. A campaign binds the active factor-program digest, objective/direction, seed, exploration weight and fixed evaluation, batch and batch-size budgets. Proposals draw only from the compiled finite universe and bind complete prior-history digest. Every prior proposal must receive one immutable completed, failed, cancelled or invalid observation before another batch; every status consumes budget, and only completed observations may carry finite objective values. Completion requires the entire fixed evaluation budget. Operator cancellation is terminal and marks all remaining trials as non-results. The append-only event chain covers registration, proposals, observations and termination.
- **Tests/evidence/rollback/done:** The full backend suite passed 500 tests with two warnings and 16 focused tests covering five methods, seed determinism, direction-sensitive adaptation, non-result integrity, non-finite scores, universe/budget bounds, idempotency and event tampering. Live Bayesian campaign `64fa4499-4728-4db8-a1fd-570e503b075b` retained completed, failed and completed observations, then terminated at exactly three evaluations with valid event head `010acf94e119f18bf67ae7d9683465886bf2d210ab6c73013f40af224d28cef8`. Rollback disables intake and cancels active campaigns without deleting lineage. Completion evidence is [DISC-004 completion evidence](evidence/DISC-004.md). No execution, result mutation, selection, promotion, order or capital authority was added.

### DISC-005 — Constrained symbolic and program search

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes retains policy, quarantine, generator identity and proposal lineage. Bulletproof must own canonicalization, scientific compilation and admissible executable-candidate receipts; no control-plane candidate may acquire quantitative meaning before that native validation.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and live-replayed through control-plane PRs #171-#173, ending with production evidence on top of deployed commit `26b4f03ff9cef03df36cc4967cb0f5aa428b71f2`. DISC-005 reuses the DISC-003 typed factor-program compiler and active AGT-004 prompt-policy registry. It adds a bounded, immutable proposal/validation ledger rather than arbitrary code generation, a second compiler, a backtester or an optimizer with hidden state. VM2 runs migration `a0c4d7e96f30`; the healthy API exposes authenticated run, candidate, replay and quarantine routes.
- **Contracts/dependencies:** Every run binds an active DISC-003 program digest, active data-only AGT-004 policy bundle and canonical constraints digest. Constraints freeze candidate, node, depth and constant budgets plus operator, field and parameter allowlists. Generator provider/model/version/seed/candidate-index identity is digest-bound. Candidate output is parsed only as data, structurally bounded, unit/causality compiled by DISC-003 and never executed. Read-only `research.retrieve` is the sole permitted generator tool; action-bearing tools fail closed. Commutative normalization detects reordered semantic duplicates, and the same generator identity cannot emit a different proposal.
- **Tests/evidence/rollback/done:** The full backend suite passed 513 tests with two warnings and the hardened focused suite passed 14 tests covering hostile operators, tool-policy escape, unknown fields, digest drift, nondeterminism, current-bar leakage, excess complexity, semantic/base-program duplicates, budget exhaustion, quarantine and routes. Live run `f5270d24-15de-4f19-abe0-30f2a38fc7de` retained accepted, duplicate, rejected and rejected outcomes under constraints digest `469e41074848fe9b81a0b2b5db6636574228e51f5b3b4ab7197f554d243fc70f`; report digest `f9128dece18398865bb391c7545166bc1667056392de16703e3ef1083b202526`. Rollback quarantines a run without deleting its candidates or lineage. Completion evidence is [DISC-005 completion evidence](evidence/DISC-005.md). No generated code execution, result mutation, promotion, order or capital authority was added.

### DISC-008 — Bounded autonomous research sessions

- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and live-replayed through control-plane PRs #175-#176, with implementation commit `110af2b9104dd3502987af94776916cdd849e5d2`. DISC-008 reuses AGT-003 task graphs, their existing cancellation/compensation controller, AGT-006 independent evaluator routing and DISC-007 selection audits. It adds one bounded session and digest-chained supervision ledger rather than a second executor, research result store or self-approving agent loop. VM2 runs migration `b1d5e8f20a40`; the healthy API exposes authenticated registration, activation, checkpoint, reconciliation, closeout, cancellation and replay routes.
- **Contracts/dependencies:** Every session binds an unactivated risk-zero task graph, its manifest digest, an exactly ordered agenda and frozen task, attempt, duration, reconciliation, no-progress and worker-loss budgets. Authority is structurally `no_capital`; approval, scope expansion and promotion flags are literal false. Scope drift, evidence conflict, stalls, worker-loss excess and graph failure fail closed. Graph success advances only to `awaiting_closeout`. Completion requires an AGT-006 independence receipt and a canonical dossier binding the session, graph, agenda, budget, active DISC-007 audit digest and every observed positive, negative, invalid, failed or cancelled outcome.
- **Tests/evidence/rollback/done:** The full backend suite passed 528 tests with two warnings and the focused suite passed 14 tests; Ruff passed. Tests cover project/agenda/risk drift, budget mismatch, out-of-scope checkpoints, evidence conflict, worker loss, no-progress loops, premature closeout, exact independent/audit binding and route coverage. Live session `be033159-bc20-4c82-b81f-fbf016027033` retained negative, failed and invalid outcomes under graph digest `30868075b09bfd97f88121e349088b9f7c5611ceda8d91999ba6a435dc520fe5`, AGT-006 receipt `153cf0ea907329c97aaf5728507dc3806b42548b94e4d213acde032b47683104` and DISC-007 audit `f8bf5a21bf539e0b4e46cf4b54405d0cd4e0fcaa9d0a1c47950d43ec487dd62f`; report digest `bbb435dc574af12c351591d96fc9deab8b379908f8df6079f0060ad8bc601c1e`. Rollback cancels remaining graph tasks, invokes declared compensation and retains all lineage. Completion evidence is [DISC-008 completion evidence](evidence/DISC-008.md). No self-approval, scope expansion, promotion, order or capital authority was added.

### DISC-009 — Discovery portfolio and information-gain scheduler

- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and production-replayed through control-plane PRs #177-#181, ending at `6dc3c6cad0a61d0d138fe5df11e10adc05bf10ad`. DISC-009 reuses current curricula, active DISC-002 opportunity maps, active DISC-006 mechanism evaluations, current DISC-007 selection audits and completed DISC-008 sessions. It adds one immutable diversified research-attention portfolio rather than another task executor, result store or self-authorizing research loop.
- **Contracts/dependencies:** DISC-001/002/006/007/008; every candidate binds a verified canonical source, source lineage, domain and cluster, server-derived uncertainty, novelty, expected information gain, attention cost and deterministic rank. The typed policy caps total attention, selection count, domain and cluster concentration while enforcing a diversity floor. `ResearchProgram.project` is now an explicit typed compatibility boundary. Budgets allocate research attention only and confer no task creation, execution, promotion, order or capital authority.
- **Tests/evidence/rollback/done:** The full backend suite passed 542 tests with two pre-existing warnings and all GitHub CI suites passed. VM2 runs migrations `c2e6f9a31b50` and `d3f7a2b41c60`. Live portfolio `18fe8f06-ff9a-45f5-8d1c-6d8a5b41419e` selected two domains from three verified candidates, retained the excluded candidate with reason `attention_budget`, and reproduced allocation digest `a86537d6ea9c4dede83f5054789298b9c41fa7002d4e758fb8209f337b42a309` exactly. A stale selection audit was rejected rather than silently admitted. Rollback stops new portfolio creation while retaining all immutable rankings, source lineage and counterfactuals. The definition of done is met: inquiry diversity, allocation rationale, excluded alternatives and exact replay are visible in [DISC-009 completion evidence](evidence/DISC-009.md).

### ML-002 — Causal feature, label and split pipelines

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes retains immutable pipeline contracts and admissibility gates. Bulletproof must materialize features, labels, purge/embargo splits and overlap weights from native data and publish the authoritative rebuild receipt.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and production-replayed through control-plane PRs #182-#183, ending at `e53321aac27d034e284de7e151e418396803eba4`. ML-002 reuses DATA-002 immutable manifests/builds and DISC-003/BT-007 factor representation rather than creating another data lake or feature language. It adds the missing causal projection registry and independently rebuilt materialization receipt.
- **Contracts/dependencies:** DATA-002, BT-007 and ML-001; every pipeline binds the exact dataset content digest and compiled factor-program digest, typed feature availability, label horizon and end offset, train-only fitted transforms, half-open expanding walk-forward folds, purge, embargo and overlap weighting. The service computes eligible training endpoints and excluded intervals and rejects build/program manifest drift.
- **Tests/evidence/rollback/done:** 552 backend tests passed with two pre-existing warnings; all seven CI suites passed on both PRs. Tests reject insufficient purge, broken embargo, non-expanding windows, validation-fitted transforms, unknown factors, label drift, dataset-lineage drift, failed causal checks and rebuild mismatch. VM2 runs migration `e4a8c2d61f90`; live pipeline `632fd11d-2bc9-4891-8eaa-e9269a080fd0` and materialization `86247c0e-04dc-4e52-85de-3ae60aff04a4` bind the registered 1,200-row canonical build, two folds, two-bar purge/embargo, inverse-overlap weighting and matching rebuild evidence. Rollback stops new registrations and pins the last verified digest while retaining immutable records. Completion evidence is [ML-002 completion evidence](evidence/ML-002.md). No training, inference, promotion, order or capital authority was added.

### ML-003 — Model-family and regime evaluation

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes owns comparison registration, qualification policy and audit binding. Bulletproof must train/evaluate the model families, baselines, folds, regime slices and permutation controls and emit the authoritative scorecard receipt.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and production-replayed through control-plane PR #184 at `f9f6e6f0c1454f5cda39da0615e9c7ff57c32b44`. ML-003 reuses ML-001 model-bundle identities, ML-002 causal materializations, Bulletproof metrics and DISC-007 selection audits. It adds one immutable comparative scorecard rather than another trainer, model registry or promotion mechanism.
- **Contracts/dependencies:** ML-002 and DISC-007; every evaluation binds the exact materialization and current non-blocked audit, requires unconditional and linear baselines plus supervised, unsupervised, regime and meta-label families, and retains identical ordered folds, exact regime slices, class counts, primary metric, log loss, Brier score and label-permutation controls. Qualification requires incremental value over the strongest baseline, sufficient class support, a minimum score in every regime and bounded regime dispersion.
- **Tests/evidence/rollback/done:** 559 backend tests passed with two pre-existing warnings and all seven CI suites passed. Tests reject missing or weak baseline ladders, incomplete fold/regime coverage, unstable regimes, permutation leakage, class imbalance and blocked audits. VM2 runs migration `e5b9d3f72a10`; live evaluation `25e3afbc-d0dd-4008-bdc0-9777fd8bb6b8` retained six candidates, strongest baseline `0.54`, qualified three stable incremental families and replayed scorecard digest `2718faf445876f79d21443c5fa06ffd7203a5e487b53117bc66ee312426a9835` exactly. Rollback makes the affected model version ineligible while retaining the comparison. Completion evidence is [ML-003 completion evidence](evidence/ML-003.md). No training, activation, promotion, order or capital authority was added.

### ML-004 — Calibration, uncertainty and abstention

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes retains the institutional qualification/demotion gate. Bulletproof must produce held-out calibration, uncertainty, applicability and abstention receipts using its registered model artifacts; Hermes may recompute small checks only as independent validators.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and production-replayed through control-plane PR #185 at `dd367ac64c1f6dc4b7882a9265fa864f38334cfa`. ML-004 reuses ML-001's held-out calibration and inference receipts, the immutable ML-003 scorecard and an RI-004 evidence dossier. It adds an institutional qualification and demotion gate rather than a second fitter or model registry.
- **Contracts/dependencies:** ML-003 and RI-004; every assessment binds a qualified candidate, exact scorecard digest, dossier digest, complete reliability diagram, held-out calibration version, conformal or block-bootstrap coverage, applicability slices, non-causal explanation receipt and explicit abstention thresholds. Miscalibration, distribution shift, low support and excess uncertainty must reduce authority through a typed abstention receipt.
- **Tests/evidence/rollback/done:** 569 backend tests passed with two pre-existing warnings and all seven CI suites passed. Tests cover malformed reliability diagrams, unqualified candidates, miscalibration, undercoverage, misleading explanation fidelity, applicability mismatch and incorrect shift/low-support abstention. VM2 runs migration `e6c1a4f83b20`; live assessment `5560e515-7ad5-4a92-80c2-e3b1482a502b` bound ML-003 evaluation `25e3afbc-d0dd-4008-bdc0-9777fd8bb6b8` and RI-004 dossier `af32b7a6-74c9-48c4-bb87-bc7433bdc07f`, recomputed ECE `0.01`, retained empirical coverage `0.91`, verified all mandatory scenarios and replayed digest `0b79ef0dee22b7d26f0f79baf209a3d0733274a9310621d6cdd8c79d3e58b928` exactly. Rollback selects the prior independently validated ML-001 bundle or baseline while retaining immutable assessments. This fixture validates the control path, not predictive skill. Evidence: `plans/evidence/ML-004.md`.

### RL-001 — Offline-RL dataset and evaluation contract

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes retains the immutable contract and admissibility audit. Bulletproof must build the transition/episode dataset, behavior propensities, reward reconstruction and support diagnostics from DATA/SHADOW-native evidence and emit the authoritative dataset receipt.
- **Status/scope/reuse/gap (2026-08-27):** Completed, merged, migrated and production-replayed through control-plane PR #186 at `8a9c3ca65cf592fca0f4ef593ce95e4a2918c5cf`. RL-001 reuses DATA-002 immutable builds and Bulletproof's sealed SHADOW-001 journal/replay rather than storing transitions or constructing another data lake. It adds an immutable offline-RL dataset/evaluation contract and server-computed admissibility audit.
- **Contracts/dependencies:** DATA-002, BT-007 and SHADOW-001; each contract binds the dataset build, sealed journal and exact replay digests, behavior-policy identity and propensities, causally available state features, complete bounded action space and support, reward formula/horizon/rebuild, episode termination, confounders and a later-evaluation protocol. Unsupported actions must abstain, and model selection is separate from final evaluation.
- **Tests/evidence/rollback/done:** 580 backend tests passed with two pre-existing warnings and all seven CI suites passed. Tests quarantine temporal/reward leakage, missing propensities, low support and unsafe importance weights and reject reward-rebuild, action-space and digest drift. VM2 runs migration `e7d2b5a94c30`; live dataset `807c244c-7574-43c2-a80a-4c6c6ea11d25` bound DATA-002 build `72fba926-a6c3-49d5-8120-f301ba6ce9ea`, 1,000 transitions, 40 episodes and the retained SHADOW-001 digests, then replayed audit digest `cc8f51b2df32316019f14592cac2d5b034987b155f6e88bcb6200ffee32f6989` exactly. Market impact remains proxy-confounded and latent liquidity remains unobserved, explicitly prohibiting causal policy claims. Rollback quarantines the contract without mutating source builds/journals. No policy-improvement, deployment, order or capital authority exists. Evidence: `plans/evidence/RL-001.md`.

### RL-002 — Conservative off-policy proposal evaluation

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes owns proposal registration, conservative policy gates and shadow-only authority. Bulletproof must compute the off-policy estimators, intervals, effective sample size, overlap, extrapolation and adversarial stresses and publish their native receipt.
- **Status/scope/reuse/gap (2026-08-28):** Completed, merged, migrated and production-replayed through control-plane PRs #187-#188, ending at `78d4be17835b07fe8530b23768f5d2ca74d69656`. RL-002 reuses the qualified RL-001 dataset, current DISC-007 audit and qualified ML-004 candidate instead of training a policy or duplicating dataset/calibration registries. It adds an immutable conservative proposal comparison and shadow-only decision.
- **Contracts/dependencies:** RL-001, DISC-007 and ML-004; every proposal binds the target and base-candidate digests, only RL-001-permitted estimators, confidence intervals, effective sample size, importance weights, action overlap, extrapolation, reward-model rebuild and required adversarial-reward, support-trimming, weight-clipping and cost-expansion receipts. The server derives the worst lower bound and independently applies typed gates.
- **Tests/evidence/rollback/done:** 596 backend tests passed with two pre-existing warnings and all CI suites passed on both PRs. Tests reject estimator disagreement, weak effective sample size, unsafe weights, weak overlap, extrapolation, unsupported actions, reward rebuild drift, adversarial stress failure, quarantined/stale dependencies and candidate mismatch. VM2 runs migration `e8c3b6a05d40`; live evaluation `77bda11b-e6cc-4c00-a76d-6261ffbb73a1` bound RL-001 `807c244c-7574-43c2-a80a-4c6c6ea11d25`, DISC-007 `45b83a75-8831-4ced-a0f3-93a5d78e981e` and ML-004 `5560e515-7ad5-4a92-80c2-e3b1482a502b`. It retained conservative value `0.016`, estimator spread `0.007`, no failures and exact digest `b14150114e7247e06a27952496cb2ad26f03d517341486093bdddbbe2c856938`. Rollback rejects the proposal while retaining comparisons. `shadow_eligible` grants no causal-policy, deployment, order or capital authority. Evidence: `plans/evidence/RL-002.md`.

#### Execution phase — Portfolio, risk, execution and demo certification

### RISK-001 — Drawdown, tail and reverse-stress engine

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes retains scenario-pack governance, freshness checks, limits and the immutable decision dossier. Bulletproof must calculate drawdown paths, tail estimates, uncertainty and reverse-stress breach thresholds from native run/portfolio evidence and emit the authoritative risk receipt.
- **Status/scope/reuse/gap (2026-08-28):** Completed, merged and production-replayed through control-plane PRs #189-#190, ending at `de6839bea5bc2d29d7e78ab879adc29625b50d4b`. RISK-001 reuses immutable BT-004 run, BT-005 cost-model and PORT-001 candidate digests plus Bulletproof drawdown/Monte Carlo analytics. It adds the missing governed portfolio-state envelope instead of duplicating the backtest engine.
- **Contracts/dependencies:** Requests bind candidate, portfolio state, Bulletproof run, cost model and versioned scenario-pack digests; drawdown depth/duration/recovery and underwater-path identity; VaR, expected shortfall, uncertainty upper bound and method; and exactly one each of price-gap, correlation-break, liquidity-freeze, model-failure and prolonged-drawdown scenarios. Every scenario has a bounded reverse-stress breach bracket. The server derives the immutable dossier and decision, fails closed on stale evidence or any breached upper envelope, and grants no allocation, order or capital authority.
- **Tests/evidence/rollback/done:** 609 backend tests passed with two pre-existing warnings; all CI gates passed on both PRs. Thirteen focused tests cover every required failure class, stale inputs, drawdown/tail limits, digest tampering, missing/duplicate scenarios, invalid tail ordering, invalid or policy-inconsistent reverse stress, idempotency and access protection. VM2 runs migration `f2b7e1d35a80`; live assessment `b7713035-e37d-4841-8ecc-acd809409de8` was admissible with exact replay, dossier digest `1860339b7bded1a112f5579b35a985260919502c4ee4ee1c0a2884f73afeeed4`, 12% maximum drawdown, 14% tail upper bound and all five reverse-stress thresholds. Rollback restores a prior scenario pack but rechecks freshness and keeps stale packs blocked. Evidence: `plans/evidence/RISK-001.md`.

### RISK-002 — Leverage, margin, liquidation and rule engine

- **Ownership correction (2026-08-28): Closed. Native producer and live replay now satisfy this correction; the stated repository boundary remains binding.** Hermes remains the effective-dated venue-rule registry and fail-closed admission gate. Bulletproof must authoritatively apply rule tiers to position state and emit margin, funding, mark-deviation and liquidation-buffer receipts; Hermes may independently verify bounded arithmetic but cannot own the quantitative engine.
- **Status/scope/reuse/gap (2026-08-28):** Completed, merged and production-replayed through control-plane PRs #191-#192, ending at `176c1c744c161f79083aa70afa04781537d864d9`. RISK-002 reuses DATA-001 dual-clock identity, the admissible RISK-001 dossier, and Bulletproof leverage/funding/liquidation telemetry. It adds a deterministic venue-rule and margin boundary instead of duplicating execution or sizing.
- **Contracts/dependencies:** Every request binds the DATA-001 snapshot and effective listing revision, RISK-001 dossier, rule source and digest, observed/available/effective/expiry clocks, lifecycle transition, contiguous margin tiers, increments, mark and funding limits, liquidation buffer, and position-state digest. The server selects the tier and derives notional, initial/maintenance margin, PnL-adjusted equity, funding rate, mark deviation, liquidation buffer, failures and decision. Unknown, future, stale, inactive, expired, ambiguous, malformed or breached rules deny. Receipts grant no allocation, order or capital authority.
- **Tests/evidence/rollback/done:** 623 backend tests passed with two pre-existing warnings and all CI suites passed on both PRs. Fourteen focused tests cover leverage, tier bounds, price/quantity increments, mark deviation, funding, liquidation, stale/future/suspended/expired rules, dependency and digest drift, malformed tier transitions, retained temporal revisions, idempotency and route protection. VM2 runs migration `f3c8a2e46b90`; live evaluation `8ed31a3e-8dae-469b-b636-79dd68bdf682` bound DATA-001 `b771d529-cd3a-43de-b87d-02fa5307147e` and RISK-001 `b7713035-e37d-4841-8ecc-acd809409de8`, selected tier 1, retained no failures and replayed receipt `10d5294738b2188e3d5a221ee0d96cacee2c7e4d94abe3db58bf82b231164d1b` exactly. Rollback suspends or retires the affected pack and denies that venue/instrument; it never restores stale rules silently. Evidence: `plans/evidence/RISK-002.md`.

### PORT-002 — Dependency, diversification and concentration service

- **Status/scope/reuse/gap (2026-08-28):** Complete, merged, deployed and live replayed. Bulletproof merge `79caf1d334a5e80d03cf644875dfa022d09c952a` owns all dependency, diversification and concentration calculations. Hermes merge `3a2a38ba15d455263281c42d06881d7aebc601d0` adds only the authoritative producer allowlist to its immutable receipt registry; replay merge `0b30fd81eeb80ec85bfacc45fd076728a8837c0f` removes the prior fixed-batch assumption. No second portfolio engine was added to the control plane.
- **Contracts/dependencies:** The native producer binds the exact PORT-001 dossier, candidate observation window, state labels, dataset/source/configuration/artifact digests, shared exposures, freshness and overlap minima, tail quantile, cluster threshold and concentration limits. It emits overall and state-conditioned correlation with uncertainty, empirical lower-tail dependence, shared-exposure dependence, deterministic clusters, HHI/effective count, diversification ratio and correlation-convergence stress. Sparse or stale histories, inconsistent states, undefined dependence and concentration excess fail closed. The receipt grants no allocation, capital, order or promotion authority.
- **Tests/evidence/rollback/done:** Five focused producer tests cover determinism, state and tail evidence, stale/sparse histories, shared exposures, cluster and HHI limits, correlation convergence, PORT-001 digest integrity and candidate-set mismatch. The full Bulletproof suite passed 1,319 tests with 27 skips; Hermes passed 629 backend tests. Native receipt `70f4ff8045875341e8f324cd2a1f44ff22a309d4dc0362c011b5a51a1c5138be` qualified with no failures. VM2 ran the rebuilt healthy API and exactly replayed it as record `5c55f791-227a-4c40-a86a-301eec866b9e`; live replay SHA-256 `6b4a7692bb7a0846e4406f407d42ef0e43cc8d7e5437277754b1968aab61e40d`. Rollback pins the prior immutable dossier or applies conservative no-diversification bounds; it never invents diversification from missing data. Evidence: `plans/evidence/PORT-002.md`.

### PORT-003 — Construction benchmark and robust optimizer registry

- **Status/scope/reuse/gap (2026-08-28):** Complete, merged, deployed and live replayed. Bulletproof merge `866e1c1c0ab23b0bb65fa795030eabf1daedfcb1` owns the equal-weight and inverse-volatility risk-budget benchmarks, robust covariance shrinkage, deterministic projected-gradient optimizer, feasibility, rounding, sensitivity and fallback calculations. Hermes merge `ffbb9bc5e39873672d3f260c6fb8a50f07b018c3` adds only a versioned solver registry and immutable receipt verification. No optimizer mathematics or portfolio authority moved into the control plane.
- **Contracts/dependencies:** The native producer binds qualified PORT-002 and RISK-001 receipts, expected returns and uncertainty, covariance, prior weights, bounds, solver name/version/specification digest, objective parameters, increment, turnover and sensitivity limits, dataset, source, configuration and artifact digests. Impossible bounds, indefinite covariance, dependency drift, solver nondeterminism, excessive sensitivity/turnover and failure to improve the benchmark ladder fail closed or select the deterministic qualified benchmark. Receipts grant no allocation, capital, order or promotion authority.
- **Tests/evidence/rollback/done:** Seven focused tests cover deterministic improvement, fallback, singular covariance regularization, infeasible and indefinite inputs, exact rounding, immutable dependencies and unknown solvers. The full Bulletproof suite passed 1,326 tests with 27 skips; Hermes passed 633 backend tests. Native receipt `c196ca8f43a1c67c49284b111df44083ba8e076cdb75097b90844ebc5e414825` selected the robust optimizer with weights summing to one and no failures. VM2 runs migration `f5e1c7a93b20`; solver `902a8423-6732-46f3-bd1e-f90b7484a8c3` and receipt record `63ef6757-137c-4712-9d13-1b4e2b15a4cf` replayed exactly. Live evidence SHA-256 is `525f6e0027b5b66c4cece4064d07fb957b9b026821616a4a2d6d3765fba1fe22`. Rollback retires admission of the affected solver identity and selects the deterministic benchmark in Bulletproof; Hermes never invents weights. Evidence: `plans/evidence/PORT-003.md`.

### EXEC-001 — Canonical market/order event and clock service

- **Status/scope/reuse/gap (2026-08-28):** Complete, merged, deployed and live replayed. Bulletproof merge `22e0bda5d7160db49b864db2d3400596d3b814c7` extends existing typed runtime events, SQLite lifecycle journals and checkpoints with the authoritative dual-clock canonical envelope and append-only point-in-time journal. Hermes merge `8e53f9350030477899ce1849abe6d532a6920f20` adds only an immutable event-schema registry and receipt admission. It does not order events or reconstruct execution state.
- **Contracts/dependencies:** Every native event binds source, stream epoch, event identity and kind, DATA-001 instrument identity where applicable, event and receive clocks, source sequence, payload and payload digest, optional correction lineage and canonical event digest. The dossier binds admitted DATA-001/002 receipts, source/configuration/dataset/artifact digests, event schema and journal versions, replay digest, late/duplicate counts and unresolved gaps. Exact duplicates are idempotent; conflicting identity reuse, excessive future drift, unknown or cross-stream corrections and tampered dependencies fail closed. Point-in-time replay includes only events received by the requested cutoff.
- **Tests/evidence/rollback/done:** Eight focused tests cover digest integrity, duplicates, identity collision, disorder, gaps, receive-time replay, corrections, future-clock drift and dependency binding. The full Bulletproof suite passed 1,334 tests with 27 skips; Hermes passed 637 backend tests. The native `1,3,2` sequence pilot surfaced one late event, resolved the temporary gap and produced deterministic replay digest `ff486a4f97df5cd10873c12291b826d28ac42b79aed2b2ecc35bec2805c88218`. VM2 runs migration `f8c2d4a71e90`; schema `c596717e-0733-4e70-8c12-91ccb730ff8b` and receipt record `5cab237f-bc51-4a13-b8ef-c8426fd3da5d` replayed exact receipt `63e1a21d355c72b841ea7d6366859e098d369551c2623a5e805de8663a3a3a5c`. Live evidence SHA-256 is `0120133b547263428df409d5b5ffbbef5edb09fcd28b5be652e5bbbb37864bfc`. Rollback stops admitting the affected schema and rebuilds projections from the immutable journal under a prior admitted schema; it never edits history or guesses ordering. Evidence: `plans/evidence/EXEC-001.md`.

### EXEC-002 — Market-microstructure state models

- **Status/scope/reuse/gap (2026-08-28):** Complete, merged, deployed and live replayed. Bulletproof merge `adcbc0937befaf97ecefe4152b84e2cfa355abe4` owns order-book, trade-formation, basis, funding, open-interest and liquidation-state calculations. Hermes merge `6c913021057a94ea15a6472d8fdde95b8b9d0f15` adds only an immutable model registry and receipt verifier; it does not calculate market state.
- **Contracts/dependencies:** The native producer consumes validated EXEC-001 events only through the receive-time cutoff and binds valid EXEC-001 and DATA-003 receipts, source events, source/configuration/dataset/artifact digests, model version and model digest. Every field carries `observed`, `inferred` or `unavailable` status, source event IDs, limitations and uncertainty. Venue resets clear prior state; stale funding/OI becomes unavailable; liquidation proxies remain model-dependent inferred evidence rather than observed liquidation or zero.
- **Tests/evidence/rollback/done:** Nine focused tests cover observed reconstruction, crossed books, missing levels, venue resets, stale funding/OI, receive-time causality, liquidation proxies and dependency drift. The full Bulletproof suite passed 1,343 tests with 27 skips; Hermes passed 641 backend tests. Native receipt `1988100824f76b42c7efbe6267b489325a08af69490ab982d15b9f0e1648ace7` reconstructed nine observed fixture fields. VM2 runs migration `f9d3e5b82a10`; model `59a5d26a-73f9-4fc0-afe1-4cfad67f28d2` and receipt record `708a844a-5023-4123-b934-8471acd01a70` replayed exactly with state digest `808b035cde967608755aecc0ce48bb9ddf6f62c58194df22c2704aafc069bb99`. Rollback disables admission of the affected model version and requires a prior active version or abstention; it never substitutes missing evidence with zero. The fixture proves contracts and replay, not live venue continuity, microstructure alpha or order authority. Evidence: `plans/evidence/EXEC-002.md`.

### EXEC-003 — Venue identity and fragmentation service

- **Status/scope/reuse/gap:** Planned; reuse DATA-001 instrument identities, adding cross-venue equivalence, fragmentation and routing constraints.
- **Contracts/dependencies:** DATA-001 and EXEC-001/002; mappings are effective-dated and never assume symbols imply fungibility.
- **Tests/evidence/rollback/done:** Test contract differences, delistings, venue outage and incompatible settlement. Retain mapping/routing evidence. Rollback quarantines a mapping. Done when consolidated views preserve venue-specific risk.

### EXEC-004 — Idempotent order management and reconciliation

- **Status/scope/reuse/gap:** Planned; reuse any existing adapters/order states, adding canonical intent/order/fill lifecycle, idempotency and authoritative reconciliation.
- **Contracts/dependencies:** EXEC-001/003 and RISK-002; commands bind client IDs, approvals and a versioned risk-decision interface. RISK-005 composes this order-state authority with the complete admission and dynamic-risk stack; EXEC-004 does not depend on its downstream composition.
- **Tests/evidence/rollback/done:** Test disconnect, duplicate, partial fill, unknown order, cancel race and restart. Retain command/event reconciliation. Rollback freezes submissions and reconciles before recovery. Done when no ambiguous state permits a second order.

### EXEC-005 — Execution-quality calibration

- **Status/scope/reuse/gap:** Planned; reuse BT-005 and shadow fills, adding queue, latency, impact, slippage and adverse-selection calibration against observations.
- **Contracts/dependencies:** EXEC-001/002/004 and SHADOW-001; calibrations bind venue, order type, size, regime and uncertainty.
- **Tests/evidence/rollback/done:** Test sparse samples, outages, censoring and regime shift. Retain replay-to-observed scorecards. Rollback uses pessimistic bounds. Done when modeled execution meets declared prospective tolerances.

### PORT-004 — Turnover, cost, capacity and liquidity service

- **Status/scope/reuse/gap:** Planned; reuse BT-005, ML-005 and portfolio candidate outputs, adding capacity/turnover constraints with uncertainty.
- **Contracts/dependencies:** PORT-003 and EXEC-005; every capacity claim binds market, horizon, size, cost model and liquidity source.
- **Tests/evidence/rollback/done:** Test illiquidity, shocks, stale volume and scaling. Retain cost/capacity curves. Rollback caps size at conservative prior limits. Done when portfolio feasibility includes executable net capacity.

### RISK-003 — Dynamic risk budgets and regime scaling

- **Status/scope/reuse/gap:** Planned; reuse deterministic sizing and regime estimates, adding bounded budgets that decrease under uncertainty and resist procyclicality.
- **Contracts/dependencies:** RISK-001/002 and ML-004; policies declare floors, caps, hysteresis and expiry.
- **Tests/evidence/rollback/done:** Test volatility spikes, regime flip, uncertainty, feedback and stale inputs. Retain budget trajectories. Rollback uses static conservative limits. Done when uncertainty never increases authorized risk.

### SHADOW-002 — Prospective candidate monitoring and re-evaluation

- **Status/scope/reuse/gap:** Planned; reuse SHADOW-001 journal and GOV-003 lifecycle, adding degradation, incident and scheduled re-evaluation rules.
- **Contracts/dependencies:** SHADOW-001, PORT-001 and CAD-001; candidates bind health metrics, thresholds, expiry and demotion proposal. RISK-004 consumes this evidence to decide admission; monitoring does not depend on the admission decision it informs.
- **Tests/evidence/rollback/done:** Test data gaps, drift, outage, false recovery and stale evidence. Retain monitoring/review dossier. Rollback freezes candidate use. Done when deterioration cannot silently continue or promote a candidate.

### RISK-004 — Candidate admission and lifecycle authority

- **Status/scope/reuse/gap:** Planned; reuse GOV-003 and portfolio dossiers, adding separate admission, allocation, scaling, demotion and retirement decisions.
- **Contracts/dependencies:** PORT-001..004, RISK-001..003 and SHADOW-002; approvals bind limits, expiry, kill and evidence epochs.
- **Tests/evidence/rollback/done:** Test stale dossiers, conflicting authority, expiry and emergency demotion. Retain decision chain. Rollback removes allocation and preserves evidence. Done when research success alone cannot allocate capital.

### RISK-005 — Real-time deterministic risk service

- **Status/scope/reuse/gap:** Planned; reuse Bulletproof risk controls, adding a production pre-trade/portfolio service with consistent snapshots and degraded mode.
- **Contracts/dependencies:** RISK-002..004 and EXEC-001/004; deterministic allow/deny responses have latency SLO, state version and independent kill path.
- **Tests/evidence/rollback/done:** Test stale state, partition, overload, restart and limit races. Retain decision/reconciliation logs. Rollback fails closed and cancels authorization. Done when all external orders pass current hard risk checks.

### EXEC-006 — Baseline execution algorithms and scheduler

- **Status/scope/reuse/gap:** Planned; reuse order/risk interfaces, adding deterministic market/limit/TWAP/VWAP-style baselines before learned policies.
- **Contracts/dependencies:** EXEC-004/005 and RISK-005; schedules bind urgency, participation, limits and cancellation behavior.
- **Tests/evidence/rollback/done:** Test gaps, thin books, partial fills, clock drift and constraint conflict. Retain cost-risk comparisons. Rollback selects simplest certified baseline. Done when algorithms obey hard constraints under replay and demo.

### EXEC-007 — Runtime freeze, kill and human recovery

- **Status/scope/reuse/gap:** Planned; reuse existing safety controls, adding independently powered pre-trade blocks, freeze/kill semantics and recovery checklist.
- **Contracts/dependencies:** EXEC-004/006, RISK-005 and GOV-001; kill authority is independent of strategy and agent runtimes.
- **Tests/evidence/rollback/done:** Rehearse partitions, corrupt state, runaway orders and operator recovery. Retain kill/reconciliation dossier. Rollback remains fail-closed. Done when kill works during degraded dependencies and restart requires explicit reconciliation.

### EXEC-008 — Venue adapter certification and demo parity

- **Status/scope/reuse/gap:** Planned; reuse adapters and DEMO-001 environment, adding per-venue capability matrices and certification dossiers.
- **Contracts/dependencies:** EXEC-003/004/007; adapters declare supported orders, precision, clocks, errors and reconciliation.
- **Tests/evidence/rollback/done:** Run sandbox conformance, reconnect, partial fill, rejection and kill drills. Retain venue-specific dossier. Rollback revokes certification. Done when no adapter reaches micro-live without current environment evidence.

### DEMO-001 — Production-like venue demo certification

- **Status/scope/reuse/gap:** Planned; reuse EXEC-008 and shadow infrastructure, adding a governed demo environment and certification gate.
- **Contracts/dependencies:** EXEC-004..008, RISK-005 and PLAT-005; demo uses production-like controls without capital.
- **Tests/evidence/rollback/done:** Rehearse order lifecycle, reconciliation, kill, restart, limits and incidents. Retain certification dossier. Rollback revokes adapter/candidate qualification. Done when operational behavior, not simulated PnL alone, passes.

### EXEC-009 — Execution degradation feedback

- **Status/scope/reuse/gap:** Planned; reuse EXEC-005 telemetry and SHADOW-002 lifecycle, adding venue/strategy degradation incidents and bounded demotion proposals.
- **Contracts/dependencies:** EXEC-005/008 and CAD-001; alerts cannot self-modify execution or restore eligibility.

### ML-005 — Conditional cost, slippage and capacity models

- **Status/scope/reuse/gap:** Planned; reuse BT-005 and execution telemetry, adding condition-aware prospective models and uncertainty bands.
- **Contracts/dependencies:** BT-005, SHADOW-001 and EXEC-005; models remain advisory inputs to deterministic constraints.
- **Tests/evidence/rollback/done:** Test regime/size extrapolation, sparse data and adverse-selection shifts. Retain baseline comparisons and calibration lineage. Rollback uses conservative static costs. Done when prospective net estimates outperform declared baselines within uncertainty.

### ML-006 — Model drift, retraining and retirement

- **Status/scope/reuse/gap:** Planned; reuse SHADOW-002 and GOV-003, adding drift diagnosis and governed retraining proposals.
- **Contracts/dependencies:** ML-003/004 and CAD-001; retraining is a new registered trial with new artifacts, never mutation in place.
- **Tests/evidence/rollback/done:** Test drift false positives, concept shift, failed retraining and rollback. Retain comparison and retirement dossiers. Done when degraded models abstain/demote and replacements requalify independently.

### RL-003 — Learned sizing/allocation/execution sandbox

- **Status/scope/reuse/gap:** Planned; reuse RL-002, portfolio and execution simulators, adding a sandbox beneath immutable deterministic risk controls.
- **Contracts/dependencies:** RL-002, RISK-005 and EXEC-006/007; hard envelopes override every learned action.
- **Tests/evidence/rollback/done:** Test extreme actions, outage, drift and constraint conflicts. Retain override and shadow dossiers. Rollback disables learned policy. Done when the policy is reproducible, shadow-only and incapable of bypassing risk.

#### Execution phase — Organization, resilient platform and founder surfaces

### AGT-005 — Agent benchmark, calibration and release scorecard

- **Status/scope/reuse/gap:** Planned; reuse role-package versions and pilot evidence, adding role-specific golden tasks, confidence calibration and shadow release comparison.
- **Contracts/dependencies:** AGT-001/004 and GOV-004; releases bind benchmark set, thresholds, failures, cost/latency and rollback version. EVOLVE-002 later aggregates these scorecards and is not a prerequisite for producing them.
- **Tests/evidence/rollback/done:** Test regressions, distribution shift, abstention and benchmark leakage. Retain comparative scorecards. Rollback reactivates the qualified prior package. Done when each active role meets declared reliability rather than a generic pass rate.

### AGT-007 — Bounded company role catalog

- **Status/scope/reuse/gap:** Planned; reuse deployed engineering, infrastructure, knowledge, research and stewardship packages, filling production roles only from documented demand.
- **Contracts/dependencies:** AGT-001/005/006; every role declares charter, tasks, workflows, grants, machine, SLO, replacement and prohibited actions.
- **Tests/evidence/rollback/done:** Run per-role golden, denial, outage and replacement drills. Retain catalog/deployment scorecards. Rollback revokes a role package. Done when every deployed agent is inspectable and replaceable without architectural redesign.

### AGT-008 — Evidence-governed agent improvement

- **Status/scope/reuse/gap:** Planned; reuse package registry promotion states and engineering missions, adding bounded improvement proposals derived from failures and evaluations.
- **Contracts/dependencies:** AGT-004/005/006 and GOV-003; agents may propose patches/packages but cannot approve or deploy themselves.
- **Tests/evidence/rollback/done:** Test reward gaming, scope growth, self-promotion and regression. Retain proposal, rehearsal, independent review and promotion evidence. Rollback activates the prior package. Done when improvement is measurable, governed and non-self-authorizing.

### AGT-009 — Workflow distillation and governed skill registry

- **Status/scope/reuse/gap:** Planned. Reuse successful task-graph traces, runbook packages, role packages, operational notes and AGT-008 improvement proposals. Add a bounded compiler that identifies genuinely repeated workflows, removes task-specific state and secrets, proposes reusable typed skill packages, and registers versioned lifecycle evidence. It must not convert one-off success, hidden chain-of-thought, unreviewed model text or an execution transcript containing credentials into a skill.
- **Contracts/dependencies:** AGT-003/004/005/006/008, GOV-001/003/004, SEC-001 and EVOLVE-001. A skill candidate binds source task/result/event digests, recurrence evidence, typed inputs/outputs, preconditions, allowed capabilities/tools/data classes, target machines, budgets, stop/compensation rules, prohibited actions, deterministic steps, bounded model-assisted steps, tests, owner, compatibility range, expiry and rollback version. Lifecycle is `draft -> rehearsed -> approved -> deployed -> deprecated/retired`; the proposing agent cannot review, approve, deploy or expand its own grants.
- **Steps/interfaces:** Detect repeated successful and failed patterns; cluster only provenance-compatible traces; produce a generalized workflow diff and secret/context scrub receipt; compile a declarative skill/runbook package; run historical replay, negative fixtures, security scanning, deterministic parity and sandbox rehearsal; route independent evaluation; present a founder-readable capability/grant diff; promote the exact digest; resolve it through the normal package registry; measure later executions against the baseline; propose revision or retirement on drift. Expose candidates, evidence, versions, active deployments, failures and provenance in Mission Control.
- **Tests/evidence/rollback/done:** Test false recurrence, memorized task data, secret leakage, prompt injection, excessive permissions, non-deterministic steps, reward gaming, scope expansion, self-approval, incompatible runtime, regression, failed upgrade and retirement. Retain trace-selection manifest, sanitized source map, compiled package digest, golden/negative/replay results, independent review, founder decision and deployment receipts. Rollback revokes the new deployment and activates the previously approved digest without deleting history. Done when a fresh compatible agent can reuse an approved skill on a new task within declared tolerances, every output replays to source evidence, and neither the authoring agent nor generated skill can acquire undeclared authority.

### PLAT-003 — Signed artifact and package supply chain

- **Status/scope/reuse/gap:** Planned; reuse role-package signing and promotion states, adding SBOM, provenance, vulnerability/policy gates and artifact verification.
- **Contracts/dependencies:** PLAT-001/002 and AGT-005; build outputs bind source, builder, dependencies, digest and promotion evidence.
- **Tests/evidence/rollback/done:** Test tamper, unsigned artifact, vulnerable dependency and stale attestation. Retain SBOM/signature/rehearsal. Rollback revokes artifact. Done when only verified rehearsed artifacts can deploy.

### GOV-003 — Promotion, demotion, quarantine and retirement

- **Status/scope/reuse/gap (2026-08-25):** Completed, merged and production-observed through control-plane PRs #120 through #122, ending at `f63ea4f07f3b8e50595256fffdd577bff29af9ab`. GOV-003 reuses the active GOV-001 `candidate-maturity`, evidence, research, capital and emergency rights plus GOV-002 projections. Migrations `a8d3f1c52b90` and `b9e4c2d63a10` add consequence dossiers and reconcile effective supersession; they do not add a fifth maturity state or make legacy decisions authoritative.
- **Contracts/dependencies:** GOV-001/002 and RI-010; closed typed promotion, demotion, quarantine, retirement and reinstatement commands bind one projection, subject digest, optimistic version, fresh SHA-256 evidence, accountable actor, independent originator/evaluator where consequential, bounded expiry, exact rollback state and affected descendants. Reversal, expiry and supersession append linked records; nothing deletes history or mutates another lifecycle dimension.
- **Tests/evidence/rollback/done:** 361 backend and 71 Mission Control tests passed with six GitHub checks, Ruff, Python 3.9 pilot compilation and JavaScript validation; the final atomic-linkage hotfix separately passed 35 focused governance tests and all six checks. VM2 runs final image `sha256:0e3b6a5eba547e975275e514e3584d5fccb4fb0961ff8350431a7e810d7c266c` at migration head `b9e4c2d63a10`; Mission Control exposes all eight retained pilot decisions. The no-capital production replay promoted/reversed and short-expiry-promoted operations, quarantined/reinstated evidence and retired/reinstated operations. The final dossier `ed1208a8afd4aa0e69ef00923f35d946846af8165491a08aeed02f35774ae827` restored research `succeeded`, evidence `admissible`, operations `candidate`, capital `no-authority`; migration reconciliation marked prior quarantine and retirement `superseded`. The live expiry retained `9ba826ec9c2004bac2605652305705f930f74690bdcaaeeef992e56247c67d09` as `expired` and linked `84e503926f5070f543ed0b2199c161a4cb278ba5d572b51112910a4a096dcf4f` as its rollback. The declared definition of done is met; automatic cadence-driven expiry invocation belongs to CAD-001.

### PLAT-004 — Deployment controller, canary and rollback

- **Status/scope/reuse/gap:** Planned; reuse deployment architect, runbook packages and manifests, adding a general source-to-environment controller.
- **Contracts/dependencies:** PLAT-001..003 and GOV-003; deployments bind approved artifact, target, preflight, canary, health and rollback.
- **Tests/evidence/rollback/done:** Test interruption, health failure, incompatible migration and stale approval. Retain provenance/canary/rollback dossier. Done when VM1-to-GitHub-to-VM2/Mac deployment and recovery are reproducible.

### CAD-001 — Event-driven institutional operating cadence

- **Status/scope/reuse/gap:** Planned; reuse schedulers, outbox and Mission Supervisor, adding governed daily, weekly, monthly and quarterly review definitions.
- **Contracts/dependencies:** OPS-001 and GOV-002; cadence instances have due windows, dedupe keys, prerequisites, owners and missed-run reconciliation.
- **Tests/evidence/rollback/done:** Test reboot, delay, duplicate ticks, backlog and clock shift. Retain schedule/reconciliation receipts. Rollback pauses future instances. Done when missed reviews catch up once without duplicate action.

### CAD-002 — Scorecards, retrospectives and policy learning

- **Status/scope/reuse/gap:** Planned; reuse operational notes, dossiers and metrics, adding governed scorecards and postmortem-to-proposal lineage.
- **Contracts/dependencies:** CAD-001 and GOV-001/004; metrics produce evidence and proposals, never authority. EVOLVE-002 consumes these scorecards; CAD-002 does not depend on its own downstream consumer.
- **Tests/evidence/rollback/done:** Test gaming, missing denominators, stale metrics and self-authorization. Retain scorecard and accepted/rejected learning lineage. Rollback retires a metric version. Done when institutional learning is attributable without automating policy consent.

### PLAT-006 — Incident command and postmortem system

- **Status/scope/reuse/gap:** Planned; reuse operational notes, alerts and approvals, adding severity, command roles, timeline, evidence capture and recovery actions.
- **Contracts/dependencies:** PLAT-005, GOV-004 and CAD-002; incident actions bind authority and never rewrite history.
- **Tests/evidence/rollback/done:** Simulate service, data, security and agent incidents. Retain timeline/postmortem/action closure. Rollback pauses unsafe automation. Done when incidents close with accountable recovery and governed learning.

### PLAT-007 — Company-wide backup and disaster recovery

- **Status/scope/reuse/gap:** Planned; reuse OPS-005 verified local backups and RI recovery, adding encrypted off-host retention and integrated recovery for every canonical store.
- **Contracts/dependencies:** PLAT-001/002/005 and OPS-005; policies bind RPO/RTO, retention, encryption, owner and restore procedure.
- **Tests/evidence/rollback/done:** Rehearse loss/corruption and restore on intended machines. Retain off-host manifests and measured drills. Rollback never deletes last verified generation. Done when control plane, RI and application recover across a disaster boundary.

### SEC-002 — Host, container and network hardening

- **Status/scope/reuse/gap:** Planned; reuse systemd sandboxes, private networks, firewall and secret files, adding intended-machine baselines and vulnerability lifecycle.
- **Contracts/dependencies:** PLAT-001/002/003/005; baselines declare ports, users, capabilities, mounts, patches and exceptions. PLAT-008 must satisfy this baseline; SEC-002 does not depend on the deployment package it constrains.
- **Tests/evidence/rollback/done:** Test drift, exposed port, vulnerable image, permission and recovery. Retain scans and patch drill. Rollback restores known-good configuration. Done when VM1, VM2 and Mac meet versioned least-exposure baselines.

### PLAT-008 — VM2 application and infrastructure operations

- **Status/scope/reuse/gap:** Planned; reuse deployment architect, Postgres/app runbooks, TLS, Caddy and backups, generalizing typed Docker, database, Redis, storage, certificate and DNS packages.
- **Contracts/dependencies:** PLAT-003/004/007 and SEC-002; packages declare target profiles, rehearsal, approvals, rollback and ownership.
- **Tests/evidence/rollback/done:** Run VM2-parity rehearsal, cutover, rotation and restore drills. Retain package/promotion dossiers. Rollback restores prior release/network/certificate state. Done when end-to-end operations no longer require ad hoc commands.

### PLAT-009 — Storage, retention and cleanup lifecycle

- **Status/scope/reuse/gap:** Planned; reuse RI lawful deletion, workspace cleanup and backup retention, adding quotas and lifecycle policy across artifacts, logs and caches.
- **Contracts/dependencies:** RI-010, DATA-003 and PLAT-007; canonical evidence, holds and last verified backups are protected.
- **Tests/evidence/rollback/done:** Test disk pressure, interrupted cleanup, retention hold and accidental canonical target. Retain deletion manifests. Rollback restores reversible tiers. Done when storage growth is forecast, bounded and auditable.

### UI-001 — Mission Control operating model and global state

- **Status/scope/reuse/gap:** Planned; reuse the current dashboard and APIs, adding one truthful projection of proposals, approvals, execution, evidence, incidents and authority.
- **Contracts/dependencies:** GOV-002/004 and PLAT-001/005; every status links to canonical state, freshness and source.
- **Tests/evidence/rollback/done:** Test stale/partial APIs, conflicting states, empty/error views and keyboard workflows. Retain founder task-test evidence. Rollback serves read-only last-known state. Done when the founder cannot confuse intent, approval, work and completion.

### UI-002 — Complete agent inspector

- **Status/scope/reuse/gap:** Planned; reuse current fleet/package views, adding charter, responsibilities, effective grants, conflicts, health, evidence and replacement history.
- **Contracts/dependencies:** AGT-001/005/007 and PLAT-002; display computed permissions, not descriptive labels alone.
- **Tests/evidence/rollback/done:** Test revoked/stale/conflicting deployments and inaccessible details. Retain UI/API replay and accessibility evidence. Rollback is read-only. Done when a profile answers exactly what an agent may do, where and under whose authority.

### UI-003 — Unified research intelligence workbench

- **Status/scope/reuse/gap:** Partially delivered through UI-003A/B/C. Complete the umbrella by integrating corpus, graph, dossiers, trials, daily agenda, lifecycle and source-to-result replay in one coherent workspace.
- **Contracts/dependencies:** RI-003/004/008/009/010 and BT-008; views use canonical IDs/digests and never imply graph proximity is evidence.
- **Tests/evidence/rollback/done:** Test citation replay, stale projections, no-answer, contradictions, trial family and lifecycle changes. Retain Mac task tests. Rollback disables write actions while preserving exploration. Done when a fresh founder session replays question through sources, trials, reviews and decision.

### UI-005 — Operations, incident and recovery console

- **Status/scope/reuse/gap:** Planned; reuse fleet, backup and service health surfaces, adding SLOs, deployments, incidents, runbooks and recovery evidence.
- **Contracts/dependencies:** PLAT-001/004..008 and OPS-004/005; read-only by default, mutations become typed approvals and brokered operations.
- **Tests/evidence/rollback/done:** Test stale telemetry, partial outage, rollback and inaccessible service. Retain operator task evidence. Rollback removes mutation controls. Done when service truth and recovery ownership are visible without terminal archaeology.

### UI-006 — Accessible responsive founder experience

- **Status/scope/reuse/gap:** Planned; reuse Mission Control design system, completing keyboard, screen-reader, focus, responsive and long-content behavior on Mac/desktop.
- **Contracts/dependencies:** UI-001..005; shared components preserve status/risk semantics and stable layout.
- **Tests/evidence/rollback/done:** Run accessibility automation, keyboard paths, zoom/mobile widths and founder usability tasks. Retain screenshots/results. Rollback retains prior accessible component. Done when critical workflows remain understandable and operable across supported viewports.

### WS-002 — Degraded-mode and partial-publication compensation

- **Status/scope/reuse/gap:** Planned; reuse WS-001, outbox and BT-008 compensation, adding whole-company behavior under dependency loss.
- **Contracts/dependencies:** WS-001, GOV-002 and PLAT-005/007; each workflow declares authoritative state, retry and compensation.
- **Tests/evidence/rollback/done:** Inject partitions during approval, execution and publication. Retain fault/recovery replay. Rollback reconstructs from canonical events. Done when no outage creates split-brain authority or orphan canonical state.

### EXEC-011 — Canonical venue telemetry, trade replay and Mission Control observability

- **Status/scope/reuse/gap:** Planned. Reuse Bulletproof's Binance/Bybit REST and private-stream adapters, SQLite execution state, JSONL order/fill/incident artifacts, reconciliation engine and session summaries. Add the missing governed bridge that continuously captures demo/live venue events and converts them into the same canonical decision, intent, order, fill, position, cash, fee, funding, margin and trade-episode semantics used by the classic backtest engine. Do not claim that an API-key environment file alone constitutes readiness.
- **Contracts/dependencies:** EXEC-001..009, SHADOW-001, BT-003/005/008, PLAT-005/007, UI-001 and UI-007. Every event binds venue/environment/account pseudonym, instrument identity, exchange/source/receive clocks, sequence or cursor, raw protected reference, normalization version and correction/reconciliation lineage. Secrets remain root-owned and never enter events, logs, prompts, artifacts or Mission Control.
- **Steps/interfaces:** Add versioned venue capability matrices and credential templates; doctor/certification gates; durable per-venue demo/live collectors; append-only raw event journal; deterministic canonical projections; periodic REST-to-stream reconciliation; trade-episode compiler compatible with backtest reporting; immutable export/replay bundles; Hermes publication receipts; and Mission Control execution views for shadow/demo/live environment, health, lag, positions, orders, fills, fees/funding, PnL, incidents, reconciliation and replay provenance. Shadow runs on VM1 against public/read-only market feeds until an explicitly approved deployment profile moves it; demo/live collectors and order services run on hardened VM2.
- **Tests/evidence/rollback/done:** Test duplicate/out-of-order/missing events, reconnect cursor loss, timestamp drift, partial fills, cancel races, funding/fee corrections, contract changes, process restart, API outage, private-stream staleness, REST disagreement, redaction, backtest-versus-venue episode replay and UI freshness. Retain certification and replay dossiers for Binance demo, Bybit demo, then separate micro-live canaries. Rollback revokes the venue profile, freezes submissions, preserves the journal and rebuilds projections. Done only when a fresh client can reproduce balances, positions and completed trade episodes to declared tolerances and Mission Control visibly distinguishes simulated shadow, venue demo and capital-bearing live state. **Reviewer:** Execution, risk, security, data and founder authorities.
- **Tests/evidence/rollback/done:** Test noisy metrics, outage, recovery and alert dedupe. Retain incident/review chain. Rollback keeps conservative execution settings. Done when degradation triggers accountable review before continued use.

### EXEC-010 — Asset-class expansion qualification

- **Status/scope/reuse/gap:** Planned; reuse DATA, BT, risk and execution contracts, adding a mandatory dossier for each new market's mechanics.
- **Contracts/dependencies:** DATA-001..003, BT-004/005 and EXEC-001..009; qualification is asset/venue specific.
- **Tests/evidence/rollback/done:** Cover sessions, settlement, corporate actions, margin, liquidity and adapter behavior. Retain full qualification dossier. Rollback disables the new market. Done when expansion cannot inherit unsupported assumptions from crypto or another asset class.

### EVOLVE-001 — Schema, role and model migration/retirement

- **Status/scope/reuse/gap:** Planned; reuse compatibility ADRs, migrations and package registry, adding cross-version evidence replay and retirement.
- **Contracts/dependencies:** BASE-002, GOV-003 and PLAT-003/004; migrations are versioned, reversible where possible and preserve canonical history.
- **Tests/evidence/rollback/done:** Test old evidence, mixed versions, failed migration and replacement. Retain compatibility/replay report. Rollback restores prior reader/runtime. Done when replacement loses neither lineage nor authority semantics.

### EVOLVE-002 — Company reliability and scientific-throughput scorecards

- **Status/scope/reuse/gap:** Planned; reuse fleet, trial, incident and calibration evidence, adding balanced reliability, safety and scientific-quality measures.
- **Contracts/dependencies:** CAD-002, AGT-005 and PLAT-005; metrics cannot reward volume, confidence theater or concealed negatives.
- **Tests/evidence/rollback/done:** Test gaming, missing data and perverse incentives. Retain scorecard lineage and governance decisions. Rollback retires the metric. Done when improvement claims are calibrated to reliability and evidence quality.

#### Execution phase — Separately governed capital scaling

### LIVE-002 — Evidence-gated scaling and multi-candidate production

- **Status/scope/reuse/gap:** Planned and separately governed; reuse LIVE-001 canary, adding expiring scale decisions and multi-candidate limits.
- **Contracts/dependencies:** LIVE-001, PORT-004, RISK-004/005, EXEC-008/009 and PLAT-005/007; no automatic scaling.
- **Tests/evidence/rollback/done:** Test concentration, degradation, outage, loss limit and emergency kill. Retain founder/risk approvals and production dossier. Rollback reduces allocation or exits under deterministic controls. Done when scaling has current independent evidence and bounded loss.

## Shared-surface rules

- RI-001 owns canonical evidence schemas; no concurrent task may invent alternatives.
- BT-003 owns the run-bundle producer contract; RI ingestion consumes it.
- OPS-001 owns approval outbox/readiness semantics; domain pilots consume them.
- DISC-001 owns question selection; the Trial Registry owns search accounting.
- PORT-001 owns candidate/risk policy schemas; LIVE-001 may not bypass them.

The precise recommended next task is **OPS-002**, proving four bounded
plain-English proposal paths now that approval/readiness, qualified retrieval,
curriculum breadth, and production-qualified lifecycle-aware memory exist.
