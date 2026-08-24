<a id="codex-implementation-backlog"></a>
# Codex Implementation Backlog

**Status:** Executable task packets
**Rule:** One task ID per branch and review unless its packet explicitly permits otherwise

All tasks inherit these constraints: preserve unrelated changes; never commit data/secrets; use migrations, compatibility readers, and typed schemas; do not grant an agent promotion or capital authority; retain negative/failed evidence; run repository-native formatting/tests plus the named acceptance commands; publish a redacted evidence report; and obtain the named reviewer before merge.

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

The next laboratory package is `BT-009`. `WS-001` remains downstream of
the completed BT-001 through BT-008 contracts and must compose them rather than introduce duplicate
engines, registries or artifact stores.

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

- **Status (2026-08-22):** Dependency audit started. BT-009 is not implementation-complete and must not be represented as executable: BT-004, BT-005, BT-006, BT-007 and BT-008 still own unqualified market-model, engine-truth, orchestration, feature-lineage and dual-memory publication contracts required by this bridge. Complete those packages first, then implement BT-009 as composition. The deprecated fast path is excluded from its execution architecture; classic native Bulletproof execution is authoritative.

- **Objective/requirement/citations:** Replace the fixed worker-local research pilot and its hard-coded hypothesis/dataset enums with an end-to-end governed bridge from any Hermes evidence-grounded research question to a prospectively registered, natively executed and fully logged Bulletproof experiment. The bridge must enforce `bulletproof_bt/docs/hypothesis_strategy_generation_prompt_instructions.md`, the hypothesis/strategy schemas, the Research Bible scientific method, and the existing no-capital authority boundary.
- **Repository/files:** Hermes Research Intelligence Director and trial registry; a dedicated hypothesis-specification role; restricted engineering mission/package generator; Bulletproof hypothesis YAML, strategy module, adapter/feature registration, tests and documentation surfaces; native hypothesis/grid runner adapter; truth-gate adapter; atomic run-bundle publisher; Bulletproof research-memory and Hermes evidence/graph publication adapters; Mission Control proposal, progress, review and dossier views.
- **Prerequisites/scope:** BASE-002/003, RI-001/003/004/010, OPS-001, BT-001/002/003. Compose BT-004 through BT-008 contracts as they qualify; do not duplicate their engine, market-model, orchestration, feature or laboratory-publication ownership. Begin with one bounded hypothesis family and immutable dataset snapshot, then generalize through typed schemas. **Non-goals:** arbitrary code from task input, direct primary-checkout edits, unregistered parameter search, self-approval, automatic research promotion, shadow/live orders, capital allocation or bypassing Bulletproof's classic execution authority.
- **Data/access:** The hypothesis/specification and execution roles receive read-only, catalog-mediated access to the complete locally available Binance and Bybit perpetual data lakes, including their declared market, funding, open-interest and availability manifests; this is full scientific availability, not permission to bypass point-in-time, coverage, provenance or leakage checks. They receive approved context packs and prior-result summaries, while protected raw bytes and credentials remain outside model prompts. Generation occurs in an isolated Git worktree with explicit allowed paths and no secrets. Execution receives digest-pinned repository code, immutable dataset/snapshot manifests, prospective experiment/trial identifiers and a bounded resource budget. Raw protected data and credentials never enter prompts, task payloads, patches, logs or run bundles.
- **Steps/interfaces:** Treat every founder research question as a request for hypothesis compilation, not as a request to squeeze the question into a fixed enum. The dedicated hypothesis-creation role first inspects the catalog and coverage/availability evidence, retrieves prior art and negative results, and produces a testable, citation-backed hypothesis card with causal feature definitions, dataset/universe/window, tier, finite grid, logging requirements, metrics, falsification criteria and expected failure modes. Present that card and any small numbered decision brief to the founder; no strategy code or trial is created before card approval. After approval, enforce the Bulletproof strategy-generation instructions to generate or reuse the hypothesis YAML, native `strategy.py` module, adapters/features, decision and state logging, tests and documentation in a bounded engineering worktree. If an approved registered strategy already matches, bind its immutable YAML/code/adapter/test digests and do not regenerate it. Run independent schema, causality, lookahead, timestamp, truth-contract, path/diff and code review gates, then present the immutable strategy/run specification and finite grid for execution approval. Treat `Tier2A`, `Tier2B` and `Tier3` as distinct typed values; resolve legacy `Tier2` according to the declared compatibility rule and show it. Reject unavailable features, unknown tiers/parameters, unbounded grids and hidden optimization. Register repository/dataset/experiment/trial digests; execute only through native classic Bulletproof; capture decisions, fills, trades, equity, performance, state features, structural buckets, failures and resource telemetry; run `validate_experiment_truth.py`; atomically finalize the bundle; ingest certified artifacts into Bulletproof memory; publish canonical evidence, citations, lineage, negative results and reviews into Hermes; record accept, reject, refine or defer without production promotion.
- **Tests/acceptance:** Cover ordinary prose with explicit tier/grid, pasted card with formatting noise and citation markers, ambiguous tier, unknown parameter, invalid grid value, excessive Cartesian product, hidden optimization language, omitted dataset/timeframe, unavailable auxiliary feature, prompt injection in evidence, duplicate family, missing/changed dataset digest, repository drift, generated path escape, arbitrary command surface, lookahead, incomplete HTF bar, forward auxiliary join, missing-bar decision, invalid stop/sizing contract, unregistered strategy, schema/test failure, unsupported fast path, classic/fast parity failure, partial/interrupted run, resource exhaustion, stale lease, truth-gate failure, corrupt bundle, duplicate publication, memory-ingestion failure and retry, cross-system digest mismatch, negative-result retention and attempted self-promotion. The mandatory golden fixture is the supplied `CSI-Gated Displacement Trend` card: it must resolve to the existing registered `l7_h1_csi_gated_displacement_trend` YAML, strategy, feature kernel and tests; preserve `d0={1.8,2.2}`, `theta={0.7,0.8}`, `k_stop={3,4}` and `k_trail={3,5}` as exactly 16 requested variants; select and visibly confirm the founder-requested tier; avoid duplicate code generation; and replay through native artifacts, required CSI/component/displacement/liquidity/trailing-stop logs, Bulletproof memory records and a Hermes dossier on a fresh client.
- **Evidence/rollback/done:** Retain the approved hypothesis/specification digest, generated patch and review receipts, repository and dataset pins, prospective registry records, bounded execution transcript, truth-gate report, atomic run-bundle digest, Bulletproof memory ingestion receipt, Hermes publication receipt, statistical/adversarial reviews and final decision episode. Done means the same registered pilot can be reproduced without manual command translation, every artifact and decision replays to its source, failed runs remain searchable, and no component can promote or trade. Rollback disables new bridge submissions while retaining registry, run, memory and dossier evidence. **Parallelism/conflicts:** specification/generation fixtures may proceed alongside BT-004/005; native orchestration must use BT-006; feature contracts use BT-007; publication uses BT-008. **Reviewer:** Senior quantitative research authority, Bulletproof maintainer, independent statistical reviewer, adversarial reviewer, security owner and founder/operator.

### WS-001 — No-capital walking-skeleton demonstration

- **Objective/requirement/citations:** Execute the complete [walking skeleton](WALKING_SKELETON.md).
- **Repository/files:** Control plane, RI, Bulletproof, worker role packages, Mission Control.
- **Prerequisites/scope:** RI-001 through RI-005, OPS-001, BT-002/003/009. **Non-goals:** shadow/live mutation.
- **Data/access:** Immutable small public/synthetic snapshot; no credentials beyond service auth.
- **Steps/interfaces:** Ingest evidence; dossier; question; registered trial; bounded task; run bundle; publication; two reviews; decision; episode.
- **Tests/acceptance:** Valid negative and invalid-causality paths; exact replay from a fresh client.
- **Evidence/rollback/done:** One root dossier linking all object/event/artifact digests; compensation test for partial publication. **Parallelism/conflicts:** demonstration serialized. **Reviewer:** Founder research authority and independent audit reviewer.

## Wave 3 — Discovery, prospective evidence, and ML

### DISC-001 — Evidence-grounded daily research director

- **Objective/requirement/citations:** Replace static mandate rotation as the sole question source with approved RI candidates while retaining deterministic scheduling.
- **Repository/files:** Daily research service, RI Director, trial registry, UI.
- **Prerequisites/scope:** RI-006 and WS-001. **Non-goals:** autonomous approval/execution.
- **Data/access:** Approved surveillance and internal evidence only.
- **Steps/interfaces:** Candidate ranking, duplicate/search-family check, budget gate, proposal, approval, task-ready event.
- **Tests/acceptance:** Static fallback, novelty tie, duplicate, stale corpus, budget exhaustion and race tests.
- **Evidence/rollback/done:** A daily cycle whose question provenance replays to sources and institutional gaps. **Parallelism/conflicts:** owns scheduler selection. **Reviewer:** Senior quantitative research authority.

### SHADOW-001 — Prospective journal and execution replay

- **Objective/requirement/citations:** Implement M5 immutable shadow observations and no-capital replay.
- **Repository/files:** Bulletproof execution runtime, market journal, Hermes/RI publication.
- **Prerequisites/scope:** BT-003 and admitted research candidate. **Non-goals:** venue order submission.
- **Data/access:** Public/read-only feeds; credential isolation.
- **Steps/interfaces:** Candidate pin, event journal, intents, replay fills, reconciliation, incidents.
- **Tests/acceptance:** Disconnect, duplicate/out-of-order event, clock drift, restart, replay parity and cost calibration.
- **Evidence/rollback/done:** Prospective/replay dossier and restored journal. **Parallelism/conflicts:** feed and replay adapters parallel after journal schema. **Reviewer:** Execution and risk reviewers.

### ML-001 — Reproducible model and calibration registry

- **Objective/requirement/citations:** Implement M6 model/feature/fit/calibration lineage without direct alpha or capital authority.
- **Repository/files:** Bulletproof/ML package, RI records, model artifact store.
- **Prerequisites/scope:** BT-002/003 and RI-001. **Non-goals:** live sizing.
- **Data/access:** Point-in-time registered snapshots only.
- **Steps/interfaces:** Feature/fit/model schemas, training run, calibration, uncertainty, inference receipt.
- **Tests/acceptance:** Seed/environment reproduction, leakage, shift, calibration, corrupt model and rollback.
- **Evidence/rollback/done:** Rebuilt model digest and independent evaluation. **Parallelism/conflicts:** feature and evaluation fixtures parallel. **Reviewer:** ML and statistical reviewers.

## Wave 4 — Capital path and resilient operations

### PORT-001 — Portfolio-candidate and deterministic risk service

- **Objective/requirement/citations:** Implement Book VII candidate aggregation, dependency, capacity, constraints and stress without allocation authority.
- **Repository/files:** Portfolio/risk services, Bulletproof integration, RI dossiers.
- **Prerequisites/scope:** SHADOW-001 and optionally ML-001. **Non-goals:** live allocation.
- **Data/access:** Registered candidate/shadow evidence.
- **Steps/interfaces:** Candidate set, covariance/dependency, constraints, stress, explainable rejection.
- **Tests/acceptance:** Concentration, missing data, regime/cost/capacity stress, deterministic repeat and infeasible portfolio.
- **Evidence/rollback/done:** Portfolio-candidate dossier explicitly marked non-allocated. **Parallelism/conflicts:** owns portfolio policy schemas. **Reviewer:** Portfolio and risk authorities.

### LIVE-001 — Demo and micro-live gated canary

- **Objective/requirement/citations:** Execute M7 demo qualification and separately approved micro-live canary.
- **Repository/files:** Execution adapters, risk/kill/reconciliation, secrets and incident systems.
- **Prerequisites/scope:** SHADOW-001, PORT-001, M8 operational gates, explicit human approval. **Non-goals:** scaling.
- **Data/access:** Dedicated least-privilege venue credentials; never in prompts/artifacts.
- **Steps/interfaces:** Certification, demo, approval, hard loss/order limits, canary, kill, reconciliation, review.
- **Tests/acceptance:** Venue sandbox plus forced outage/partial fill/stale data/key rotation/kill drills.
- **Evidence/rollback/done:** Demo dossier and separately signed micro-live dossier; rollback closes orders and revokes allocation. **Parallelism/conflicts:** serialized external mutation. **Reviewer:** Production, risk and founder authority.

### OPS-003 — Disaster recovery and vendor/runtime replacement

- **Objective/requirement/citations:** Prove M8/M9 recovery and replaceability across canonical services, projections, workers, and model runtime.
- **Repository/files:** Infrastructure automation, backups, RI, control plane, deployment docs.
- **Prerequisites/scope:** RI-005 and deployed walking skeleton. **Non-goals:** destructive production test without rehearsal/approval.
- **Data/access:** Encrypted backups and redacted evidence.
- **Steps/interfaces:** Parity rehearsal; restore canonical stores; rebuild projections; rotate secrets; replace one model/runtime; replay tasks.
- **Tests/acceptance:** Measured RPO/RTO, integrity digests, stale lease handling, notification and rollback tests.
- **Evidence/rollback/done:** Recovery dossier and runtime-replacement compatibility report. **Parallelism/conflicts:** rehearsals parallel by service, final integrated drill serialized. **Reviewer:** SRE, security and governance.

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
The dependency order is:

1. `RI-007`, `RI-008`, `RI-009`, `RI-009B`, `RI-010`, `RI-011`; `OPS-001`, `OPS-002`, `OPS-004`, `OPS-005`, `OPS-006`; `CHAN-002`; `UI-007`; `GOV-001`, `GOV-002`, `GOV-003`, `GOV-004`; `AGT-001`, `AGT-002`, `AGT-003`, `AGT-004`, `AGT-005`, `AGT-006`, `AGT-007`, `AGT-008`.
2. `DATA-001`, `DATA-002`, `DATA-003`; `BT-001`, `BT-002`, `BT-003`, `BT-004`, `BT-005`, `BT-006`, `BT-007`, `BT-008`, `BT-009`; `UI-001`, `UI-002`, `UI-003`, `UI-004`; `CHAN-001`; `WS-001`, `WS-002`.
3. `DISC-001`, `DISC-002`, `DISC-003`, `DISC-004`, `DISC-005`, `DISC-006`, `DISC-007`, `DISC-008`, `DISC-009`; `SHADOW-001`, `SHADOW-002`; `ML-001`, `ML-002`, `ML-003`, `ML-004`, `ML-005`, `ML-006`; `RL-001`, `RL-002`, `RL-003`.
4. `PORT-001`, `PORT-002`, `PORT-003`, `PORT-004`; `RISK-001`, `RISK-002`, `RISK-003`, `RISK-004`, `RISK-005`; `EXEC-001`, `EXEC-002`, `EXEC-003`, `EXEC-004`, `EXEC-005`, `EXEC-006`, `EXEC-007`, `EXEC-008`, `EXEC-009`, `EXEC-010`; `DEMO-001`.
5. `PLAT-001`, `PLAT-002`, `PLAT-003`, `PLAT-004`, `PLAT-005`, `PLAT-006`, `PLAT-007`, `PLAT-008`, `PLAT-009`; `SEC-001`, `SEC-002`; `UI-005`, `UI-006`; `CAD-001`, `CAD-002`; `OPS-003`.
6. Separately governed `LIVE-001`, `LIVE-002`, then `EVOLVE-001`, `EVOLVE-002` and deferred `LLM-001`.

Parallel work is allowed only where the coverage dependency graph and the ownership
rules below do not conflict. Capital work cannot become executable merely because its
software prerequisites exist; its independent evidence and human approval gates remain
mandatory.

## Complete capability implementation packets

These packets close the planning gap between the capability map and the executable
backlog. `Status: planned` means that an existing component may be reused, but the
package is not complete until its own tests, evidence and rollback boundary pass.

### DATA-001 — Point-in-time instrument and reference-data service

- **Status/scope/reuse/gap:** Planned. Reuse Bulletproof symbols, venue metadata and dataset manifests; add one canonical, temporal instrument/venue/calendar/clock identity service rather than another symbol map.
- **Contracts/dependencies:** After BASE-002, expose effective-dated instrument, venue, session, corporate-action and reference-data records consumed by DATA-002, BT-004 and EXEC-001/003. Unknown or conflicting identity fails closed.
- **Tests/evidence/rollback/done:** Test relisting, symbol reuse, venue changes, holidays, clock skew and point-in-time replay. Retain snapshot digests and consumer compatibility results. Roll back consumers to the prior versioned snapshot. Done when historical identity reconstructs without present-day leakage.

### DATA-002 — Immutable market-data catalog and availability ledger

- **Status/scope/reuse/gap:** Planned on top of BT-002. Reuse its immutable snapshot and correction lineage; extend coverage to raw/curated partitions, membership and source availability across supported datasets.
- **Contracts/dependencies:** DATA-001 identities plus content-addressed partitions, observation/availability timestamps, correction ancestry and read-only source access; BT-006/007 and ML-002 consume only registered snapshots.
- **Tests/evidence/rollback/done:** Exercise gaps, duplicates, late corrections, membership drift, timezone boundaries and lookahead attempts. Retain manifests and replay receipts. Rollback selects a prior immutable snapshot, never rewrites one. Done when every laboratory input is digest-bound and point-in-time valid.

### DATA-003 — Data quality, lineage, entitlement and lake operations

- **Status/scope/reuse/gap:** Planned. Reuse current lake readers, BT-002 validation and Hermes fleet/backup telemetry; add quality SLOs, entitlement policy, retention and recovery ownership.
- **Contracts/dependencies:** DATA-001/002; publish quality incidents, lineage edges, access decisions, storage budgets and recovery manifests without putting protected data in prompts or evidence.
- **Tests/evidence/rollback/done:** Test corrupt partitions, entitlement denial, stale data, capacity pressure, retention holds and restore. Retain quality/lineage and recovery dossiers. Rollback disables a derived publication and restores its last verified manifest. Done when source immutability, access and recovery are continuously observable.

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

### GOV-001 — Decision rights, delegation and exception policy

- **Status/scope/reuse/gap:** Planned; reuse approvals, role packages and broker gates, adding one versioned authority graph for decisions, vetoes, delegation, exceptions and emergencies.
- **Contracts/dependencies:** BASE-002/003; policy decisions bind actor, role, scope, risk, digest, expiry and separation-of-duty constraints.
- **Tests/evidence/rollback/done:** Test self-approval, conflicting grants, expired delegation, emergency use and revocation. Retain policy/decision replay and exception closure. Roll back by activating a prior signed policy. Done when every consequential action resolves to current accountable authority.

### GOV-002 — Orthogonal lifecycle state machines

- **Status/scope/reuse/gap:** Planned; reuse existing task, mission, evidence and trial states, adding explicit separate machines for research, evidence, operations and capital.
- **Contracts/dependencies:** GOV-001 and BASE-002; typed commands/events define legal transitions and forbid one lifecycle from implying another.
- **Tests/evidence/rollback/done:** Exhaust invalid transitions, races, replay and migration. Retain event histories and state projections. Rollback replays through a compatible projector. Done when no research result can silently become operational or capital authority.

### GOV-003 — Promotion, demotion, quarantine and retirement

- **Status/scope/reuse/gap:** Planned; reuse research decisions, quarantine and approval records, adding consequence-specific promotion, demotion, retirement and reinstatement workflows.
- **Contracts/dependencies:** GOV-001/002 and RI-010; every transition binds evidence, approvers, expiry, rollback and affected descendants.
- **Tests/evidence/rollback/done:** Test stale evidence, revocation, emergency demotion and reinstatement. Retain decision dossiers. Rollback restores the prior bounded state, never deleted history. Done when all lifecycle consequences are explicit and reversible where lawful.

### GOV-004 — Immutable audit and policy evidence export

- **Status/scope/reuse/gap:** Planned; reuse task events, approvals and immutable histories, closing cross-service policy-version and compliance-export gaps.
- **Contracts/dependencies:** GOV-001/002; append-only actor/action/object/policy/evidence events with stable export schema and integrity chain.
- **Tests/evidence/rollback/done:** Test tamper, missing event, clock disorder, redaction and fresh-client reconstruction. Retain signed exports. Rollback changes projectors only. Done when the complete decision/action chain reconstructs without privileged database interpretation.

### CAD-001 — Event-driven institutional operating cadence

- **Status/scope/reuse/gap:** Planned; reuse schedulers, outbox and Mission Supervisor, adding governed daily, weekly, monthly and quarterly review definitions.
- **Contracts/dependencies:** OPS-001 and GOV-002; cadence instances have due windows, dedupe keys, prerequisites, owners and missed-run reconciliation.
- **Tests/evidence/rollback/done:** Test reboot, delay, duplicate ticks, backlog and clock shift. Retain schedule/reconciliation receipts. Rollback pauses future instances. Done when missed reviews catch up once without duplicate action.

### CAD-002 — Scorecards, retrospectives and policy learning

- **Status/scope/reuse/gap:** Planned; reuse operational notes, dossiers and metrics, adding governed scorecards and postmortem-to-proposal lineage.
- **Contracts/dependencies:** CAD-001, GOV-001/004 and EVOLVE-002; metrics produce evidence and proposals, never authority.
- **Tests/evidence/rollback/done:** Test gaming, missing denominators, stale metrics and self-authorization. Retain scorecard and accepted/rejected learning lineage. Rollback retires a metric version. Done when institutional learning is attributable without automating policy consent.

### AGT-001 — Agent charter, capability and grant registry

- **Status/scope/reuse/gap:** Planned; reuse registrations, role packages and deployments, adding canonical charters, responsibilities, conflicts, grants and revocations.
- **Contracts/dependencies:** GOV-001/002 and PLAT-002; every lease resolves machine, role, package, capability, permission and accountable owner.
- **Tests/evidence/rollback/done:** Test excess capability, stale deployment, conflicts, revocation and replacement. Retain effective-permission snapshots. Rollback revokes the package. Done when no task executes outside an active least-privilege grant.

### AGT-002 — Provenance-bearing agent context and working memory

- **Status/scope/reuse/gap:** Planned; reuse RI context packs, task manifests and dossiers, adding minimum-sufficient context assembly and ephemeral working-memory policy.
- **Contracts/dependencies:** RI-003/008/010 and AGT-001; context items bind source, selection reason, sensitivity, expiry and prompt position.
- **Tests/evidence/rollback/done:** Test contamination, stale/contradictory context, protected data and oversized packs. Retain context manifests and citations. Rollback discards working memory, preserving canonical evidence. Done when outputs replay to exactly what the agent was allowed to see.

### AGT-003 — Typed task graphs and bounded deliberation

- **Status/scope/reuse/gap:** Planned; reuse mission steps, dependencies, budgets and leases, adding typed messages, cancellation, termination and deadlock handling.
- **Contracts/dependencies:** AGT-001/002 and OPS-001; graph nodes declare role, inputs, outputs, budgets, stop conditions and compensation.
- **Tests/evidence/rollback/done:** Test dependency failure, cancellation, cycles, runaway loops, correlated failure and lease loss. Retain graph/event replay. Rollback cancels pending nodes and compensates partial publication. Done when every multi-agent run terminates within approved bounds.

### AGT-004 — Prompt, policy and model-output security registry

- **Status/scope/reuse/gap:** Planned; reuse package manifests, input validation and corpus scanning, adding versioned prompts/policies, trust labels and structured-output gates.
- **Contracts/dependencies:** AGT-001/002 and SEC-001; prompts bind model/runtime/version and outputs validate against schemas before becoming data or actions.
- **Tests/evidence/rollback/done:** Adversarially test injection, exfiltration, instruction collision and malformed/confident outputs. Retain evaluation corpus and release report. Rollback restores the prior prompt/policy bundle. Done when no model text bypasses deterministic validation.

### AGT-005 — Agent benchmark, calibration and release scorecard

- **Status/scope/reuse/gap:** Planned; reuse role-package versions and pilot evidence, adding role-specific golden tasks, confidence calibration and shadow release comparison.
- **Contracts/dependencies:** AGT-001/004 and EVOLVE-002; releases bind benchmark set, thresholds, failures, cost/latency and rollback version.
- **Tests/evidence/rollback/done:** Test regressions, distribution shift, abstention and benchmark leakage. Retain comparative scorecards. Rollback reactivates the qualified prior package. Done when each active role meets declared reliability rather than a generic pass rate.

### AGT-006 — Independent evaluator routing and anti-collusion

- **Status/scope/reuse/gap:** Planned; reuse M13 independent roles and reviews, adding enforced producer/evaluator separation and runtime-correlation visibility.
- **Contracts/dependencies:** GOV-001 and AGT-001/003; routing forbids producer selection or impersonation and records provider/model/host correlation.
- **Tests/evidence/rollback/done:** Test same-identity, shared-context leakage, unavailable evaluator and disagreement escalation. Retain routing/review lineage. Rollback blocks promotion pending human review. Done when claimed independence is machine-verifiable.

### AGT-007 — Bounded company role catalog

- **Status/scope/reuse/gap:** Planned; reuse deployed engineering, infrastructure, knowledge, research and stewardship packages, filling production roles only from documented demand.
- **Contracts/dependencies:** AGT-001/005/006; every role declares charter, tasks, workflows, grants, machine, SLO, replacement and prohibited actions.
- **Tests/evidence/rollback/done:** Run per-role golden, denial, outage and replacement drills. Retain catalog/deployment scorecards. Rollback revokes a role package. Done when every deployed agent is inspectable and replaceable without architectural redesign.

### AGT-008 — Evidence-governed agent improvement

- **Status/scope/reuse/gap:** Planned; reuse package registry promotion states and engineering missions, adding bounded improvement proposals derived from failures and evaluations.
- **Contracts/dependencies:** AGT-004/005/006 and GOV-003; agents may propose patches/packages but cannot approve or deploy themselves.
- **Tests/evidence/rollback/done:** Test reward gaming, scope growth, self-promotion and regression. Retain proposal, rehearsal, independent review and promotion evidence. Rollback activates the prior package. Done when improvement is measurable, governed and non-self-authorizing.

### DISC-002 — Observation, anomaly and opportunity mapping

- **Status/scope/reuse/gap:** Planned; reuse RI evidence/search and trial families, adding typed separation of observation, anomaly, mechanism and investable opportunity.
- **Contracts/dependencies:** DISC-001 and RI-004; maps bind population, baseline, effect, uncertainty, costs and null controls.
- **Tests/evidence/rollback/done:** Test noise, duplicated signals, regime confounding and cost-erased effects. Retain maps and null results. Rollback supersedes a map. Done when an anomaly cannot be presented as opportunity without incremental evidence.

### DISC-003 — Representation and factor experiment language

- **Status/scope/reuse/gap:** Planned; reuse hypothesis cards and BT-007 schemas, adding a typed, causal-time-safe DSL for representations, transforms and factor experiments.
- **Contracts/dependencies:** BT-006/007; compile to finite registered trials with units, clocks, domains and constraints.
- **Tests/evidence/rollback/done:** Test invalid expressions, future references, semantic duplicates and deterministic compilation. Retain source/compiled digests. Rollback pins the prior language version. Done when every search space is reproducible and inspectable.

### DISC-004 — Budgeted statistical search services

- **Status/scope/reuse/gap:** Planned; reuse BT-006 grids, adding random, structured, Bayesian and evolutionary planners without changing execution truth.
- **Contracts/dependencies:** DISC-003/007 and BT-006; planners emit registered proposals under fixed budget/stopping contracts.
- **Tests/evidence/rollback/done:** Test seeds, resume, exhausted budgets, failed trials and deterministic audit replay. Retain complete search trajectories. Rollback stops proposing new trials. Done when method comparisons include every evaluation and resource charge.

### DISC-005 — Constrained symbolic and program search

- **Status/scope/reuse/gap:** Planned; reuse DISC-003 compiler and restricted engineering sandbox, adding complexity limits, semantic constraints and safe program generation.
- **Contracts/dependencies:** DISC-003/004 and AGT-004; generated programs have typed inputs, bounded operations and isolated execution.
- **Tests/evidence/rollback/done:** Test path/network escape, nondeterminism, invalid syntax, excessive complexity and duplicate semantics. Retain programs and search lineage. Rollback quarantines the generator. Done when every candidate is safe, reproducible and search-accounted.

### DISC-006 — Mechanism and falsification service

- **Status/scope/reuse/gap:** Planned; reuse dossiers, contradictions and hypothesis registry, adding explicit mechanisms, alternatives and decisive tests before promotion.
- **Contracts/dependencies:** RI-004/008 and DISC-002; each hypothesis declares causal story, competing explanations and falsification outcomes.
- **Tests/evidence/rollback/done:** Test tautologies, unfalsifiable claims, confounders and post-hoc changes. Retain alternative/rejection dossiers. Rollback returns the claim to unresolved. Done when supporting evidence cannot hide failed decisive tests.

### DISC-007 — Selection-bias and research-overfitting auditor

- **Status/scope/reuse/gap:** Planned; reuse trial families and M13 statistical review, adding full-history family-wise/FDR, deflated evidence and researcher-degrees-of-freedom audits.
- **Contracts/dependencies:** BT-006 and DISC-006; audit consumes immutable complete search ledgers only.
- **Tests/evidence/rollback/done:** Test omitted trials, family splitting, metric shopping and optional stopping. Retain adjusted reports and raw lineage. Rollback blocks promotion. Done when evidence strength reflects the complete search process.

### DISC-008 — Bounded autonomous research sessions

- **Status/scope/reuse/gap:** Planned; reuse Mission Supervisor and research roles, adding agenda, budget, termination and escalation for unattended no-capital sessions.
- **Contracts/dependencies:** AGT-003/006, BT-006 and DISC-007; sessions cannot approve, expand scope or promote results.
- **Tests/evidence/rollback/done:** Test loops, no progress, conflicts, worker loss and budget exhaustion. Retain session graph and all negative/invalid outcomes. Rollback cancels remaining tasks. Done when sessions terminate safely and yield replayable dossiers.

### DISC-009 — Discovery portfolio and information-gain scheduler

- **Status/scope/reuse/gap:** Planned; reuse RI gaps, curricula and trial registry, adding diversified inquiry allocation based on expected information value.
- **Contracts/dependencies:** DISC-001/002/007/008; budgets apply to research attention only, never capital.
- **Tests/evidence/rollback/done:** Test duplication, monoculture, stale estimates and gaming. Retain ranked agenda and counterfactual choices. Rollback uses deterministic baseline scheduling. Done when inquiry diversity and allocation rationale are visible.

### SHADOW-002 — Prospective candidate monitoring and re-evaluation

- **Status/scope/reuse/gap:** Planned; reuse SHADOW-001 journal and GOV-003 lifecycle, adding degradation, incident and scheduled re-evaluation rules.
- **Contracts/dependencies:** SHADOW-001, RISK-004 and CAD-001; candidates bind health metrics, thresholds, expiry and demotion action.
- **Tests/evidence/rollback/done:** Test data gaps, drift, outage, false recovery and stale evidence. Retain monitoring/review dossier. Rollback freezes candidate use. Done when deterioration cannot silently continue or promote a candidate.

### ML-002 — Causal feature, label and split pipelines

- **Status/scope/reuse/gap:** Planned; reuse BT-007 contracts and ML-001 registry, adding canonical purge, embargo, overlap and point-in-time dataset construction.
- **Contracts/dependencies:** DATA-002, BT-007 and ML-001; pipeline manifests bind features, labels, universe, splits and fit boundaries.
- **Tests/evidence/rollback/done:** Test leakage, overlapping labels, revised inputs, normalization and missingness. Retain split/lineage reports. Rollback pins prior manifests. Done when training/evaluation data reconstruct without future information.

### ML-003 — Model-family and regime evaluation

- **Status/scope/reuse/gap:** Planned; reuse ML-001/002 and Bulletproof metrics, adding supervised, unsupervised, regime and meta-label baseline ladders.
- **Contracts/dependencies:** ML-002 and DISC-007; evaluations declare baseline, stability slices and incremental conditional value.
- **Tests/evidence/rollback/done:** Test weak baselines, unstable regimes, label permutation and class imbalance. Retain comparative scorecards. Rollback rejects the model version. Done when claimed value is stable and incremental, not merely in-sample fit.

### ML-004 — Calibration, uncertainty and abstention

- **Status/scope/reuse/gap:** Planned; reuse ML-001 registry, adding probability calibration, conformal/uncertainty intervals, interpretability and mandatory abstention/demotion.
- **Contracts/dependencies:** ML-003 and RI-004; inference receipts include calibration version, uncertainty, applicability and abstention reason.
- **Tests/evidence/rollback/done:** Test miscalibration, shift, low support and misleading explanations. Retain reliability diagrams and abstention evidence. Rollback selects a prior calibrated model or baseline. Done when uncertainty reliably reduces authority.

### ML-005 — Conditional cost, slippage and capacity models

- **Status/scope/reuse/gap:** Planned; reuse BT-005 and execution telemetry, adding condition-aware prospective models and uncertainty bands.
- **Contracts/dependencies:** BT-005, SHADOW-001 and EXEC-005; models remain advisory inputs to deterministic constraints.
- **Tests/evidence/rollback/done:** Test regime/size extrapolation, sparse data and adverse-selection shifts. Retain baseline comparisons and calibration lineage. Rollback uses conservative static costs. Done when prospective net estimates outperform declared baselines within uncertainty.

### ML-006 — Model drift, retraining and retirement

- **Status/scope/reuse/gap:** Planned; reuse SHADOW-002 and GOV-003, adding drift diagnosis and governed retraining proposals.
- **Contracts/dependencies:** ML-003/004 and CAD-001; retraining is a new registered trial with new artifacts, never mutation in place.
- **Tests/evidence/rollback/done:** Test drift false positives, concept shift, failed retraining and rollback. Retain comparison and retirement dossiers. Done when degraded models abstain/demote and replacements requalify independently.

### RL-001 — Offline-RL dataset and evaluation contract

- **Status/scope/reuse/gap:** Planned; reuse immutable snapshots and execution journals, adding behavior-policy, action/support, reward and confounding metadata.
- **Contracts/dependencies:** DATA-002, BT-007 and SHADOW-001; dataset versions are point-in-time and no-capital.
- **Tests/evidence/rollback/done:** Test support gaps, leakage, reward errors and policy mismatch. Retain dataset/audit manifests. Rollback quarantines the dataset. Done when offline evaluation limitations are explicit and reproducible.

### RL-002 — Conservative off-policy proposal evaluation

- **Status/scope/reuse/gap:** Planned; reuse RL-001 and statistical review, adding conservative estimators, uncertainty stress and safe proposal gates.
- **Contracts/dependencies:** RL-001, DISC-007 and ML-004; output remains shadow-only and carries support/uncertainty bounds.
- **Tests/evidence/rollback/done:** Test estimator bias, weak overlap, extrapolation and adversarial rewards. Retain estimator comparison. Rollback rejects the proposal. Done when policies cannot pass on unsupported optimistic estimates.

### RL-003 — Learned sizing/allocation/execution sandbox

- **Status/scope/reuse/gap:** Planned; reuse RL-002, portfolio and execution simulators, adding a sandbox beneath immutable deterministic risk controls.
- **Contracts/dependencies:** RL-002, RISK-005 and EXEC-006/007; hard envelopes override every learned action.
- **Tests/evidence/rollback/done:** Test extreme actions, outage, drift and constraint conflicts. Retain override and shadow dossiers. Rollback disables learned policy. Done when the policy is reproducible, shadow-only and incapable of bypassing risk.

### PORT-002 — Dependency, diversification and concentration service

- **Status/scope/reuse/gap:** Planned; reuse PORT-001 candidate schema and Bulletproof portfolio analytics, adding state-dependent dependence, clustering and concentration stress.
- **Contracts/dependencies:** PORT-001 and SHADOW-001; outputs bind data window, regime, uncertainty and stale-input behavior.
- **Tests/evidence/rollback/done:** Test correlation breaks, shared exposures, sparse histories and concentration limits. Retain dependency/stress dossier. Rollback uses conservative concentration bounds. Done when diversification claims survive state and tail dependence tests.

### PORT-003 — Construction benchmark and robust optimizer registry

- **Status/scope/reuse/gap:** Planned; reuse existing allocators where present, adding equal-weight/risk-budget baselines, versioned solvers, feasibility and deterministic fallback.
- **Contracts/dependencies:** PORT-001/002 and RISK-001; optimizer inputs/constraints/objective/rounding bind to a registry record.
- **Tests/evidence/rollback/done:** Test infeasibility, singular matrices, rounding, sensitivity and solver nondeterminism. Retain benchmark ladder. Rollback selects deterministic baseline. Done when optimization adds robust value and never emits an invalid portfolio.

### PORT-004 — Turnover, cost, capacity and liquidity service

- **Status/scope/reuse/gap:** Planned; reuse BT-005, ML-005 and portfolio candidate outputs, adding capacity/turnover constraints with uncertainty.
- **Contracts/dependencies:** PORT-003 and EXEC-005; every capacity claim binds market, horizon, size, cost model and liquidity source.
- **Tests/evidence/rollback/done:** Test illiquidity, shocks, stale volume and scaling. Retain cost/capacity curves. Rollback caps size at conservative prior limits. Done when portfolio feasibility includes executable net capacity.

### RISK-001 — Drawdown, tail and reverse-stress engine

- **Status/scope/reuse/gap:** Planned; reuse Bulletproof risk metrics and PORT-001, adding path-dependent scenarios, tail uncertainty and reverse stress.
- **Contracts/dependencies:** BT-004/005 and PORT-001; scenarios are versioned, attributable and bind portfolio state.
- **Tests/evidence/rollback/done:** Test gap, correlation, liquidity, model and prolonged drawdown failures. Retain scenario/reverse-stress dossier. Rollback restores prior scenario pack while blocking stale admission. Done when loss envelopes include model failure, not only historical variance.

### RISK-002 — Leverage, margin, liquidation and rule engine

- **Status/scope/reuse/gap:** Planned; reuse exchange/prop constraints where present, adding versioned venue/rule state machines and liquidation/funding mechanics.
- **Contracts/dependencies:** DATA-001 and RISK-001; hard rules precede sizing and fail closed when state is unknown.
- **Tests/evidence/rollback/done:** Property-test leverage, margin tiers, liquidation, funding and rule transitions. Retain rule-source and boundary evidence. Rollback disables affected venue/instrument. Done when no order can violate a known hard constraint.

### RISK-003 — Dynamic risk budgets and regime scaling

- **Status/scope/reuse/gap:** Planned; reuse deterministic sizing and regime estimates, adding bounded budgets that decrease under uncertainty and resist procyclicality.
- **Contracts/dependencies:** RISK-001/002 and ML-004; policies declare floors, caps, hysteresis and expiry.
- **Tests/evidence/rollback/done:** Test volatility spikes, regime flip, uncertainty, feedback and stale inputs. Retain budget trajectories. Rollback uses static conservative limits. Done when uncertainty never increases authorized risk.

### RISK-004 — Candidate admission and lifecycle authority

- **Status/scope/reuse/gap:** Planned; reuse GOV-003 and portfolio dossiers, adding separate admission, allocation, scaling, demotion and retirement decisions.
- **Contracts/dependencies:** PORT-001..004, RISK-001..003 and SHADOW-002; approvals bind limits, expiry, kill and evidence epochs.
- **Tests/evidence/rollback/done:** Test stale dossiers, conflicting authority, expiry and emergency demotion. Retain decision chain. Rollback removes allocation and preserves evidence. Done when research success alone cannot allocate capital.

### RISK-005 — Real-time deterministic risk service

- **Status/scope/reuse/gap:** Planned; reuse Bulletproof risk controls, adding a production pre-trade/portfolio service with consistent snapshots and degraded mode.
- **Contracts/dependencies:** RISK-002..004 and EXEC-001/004; deterministic allow/deny responses have latency SLO, state version and independent kill path.
- **Tests/evidence/rollback/done:** Test stale state, partition, overload, restart and limit races. Retain decision/reconciliation logs. Rollback fails closed and cancels authorization. Done when all external orders pass current hard risk checks.

### EXEC-001 — Canonical market/order event and clock service

- **Status/scope/reuse/gap:** Planned; reuse BT-004 events and shadow journals, adding production-grade canonical envelopes, sequence/clock provenance and reconstruction.
- **Contracts/dependencies:** DATA-001/002 and BT-004; events bind source/event/receive time, identity, sequence and correction.
- **Tests/evidence/rollback/done:** Test disorder, duplicates, gaps, drift and restart reconstruction. Retain event/replay digests. Rollback rebuilds projections from the journal. Done when state reconstructs point in time without hidden ordering assumptions.

### EXEC-002 — Market-microstructure state models

- **Status/scope/reuse/gap:** Planned; reuse order-book/trade/funding features, adding typed LOB, trade formation, basis, OI and liquidation reconstructions with limitation metadata.
- **Contracts/dependencies:** EXEC-001 and DATA-003; derived state binds source quality, coverage and uncertainty.
- **Tests/evidence/rollback/done:** Test crossed books, missing levels, venue resets, delayed funding/OI and liquidation proxies. Retain validation dossier. Rollback disables unreliable derived fields. Done when downstream users can distinguish observed from inferred state.

### EXEC-003 — Venue identity and fragmentation service

- **Status/scope/reuse/gap:** Planned; reuse DATA-001 instrument identities, adding cross-venue equivalence, fragmentation and routing constraints.
- **Contracts/dependencies:** DATA-001 and EXEC-001/002; mappings are effective-dated and never assume symbols imply fungibility.
- **Tests/evidence/rollback/done:** Test contract differences, delistings, venue outage and incompatible settlement. Retain mapping/routing evidence. Rollback quarantines a mapping. Done when consolidated views preserve venue-specific risk.

### EXEC-004 — Idempotent order management and reconciliation

- **Status/scope/reuse/gap:** Planned; reuse any existing adapters/order states, adding canonical intent/order/fill lifecycle, idempotency and authoritative reconciliation.
- **Contracts/dependencies:** EXEC-001/003 and RISK-005; commands bind client IDs, approvals and current risk state.
- **Tests/evidence/rollback/done:** Test disconnect, duplicate, partial fill, unknown order, cancel race and restart. Retain command/event reconciliation. Rollback freezes submissions and reconciles before recovery. Done when no ambiguous state permits a second order.

### EXEC-005 — Execution-quality calibration

- **Status/scope/reuse/gap:** Planned; reuse BT-005 and shadow fills, adding queue, latency, impact, slippage and adverse-selection calibration against observations.
- **Contracts/dependencies:** EXEC-001/002/004 and SHADOW-001; calibrations bind venue, order type, size, regime and uncertainty.
- **Tests/evidence/rollback/done:** Test sparse samples, outages, censoring and regime shift. Retain replay-to-observed scorecards. Rollback uses pessimistic bounds. Done when modeled execution meets declared prospective tolerances.

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

### EXEC-009 — Execution degradation feedback

- **Status/scope/reuse/gap:** Planned; reuse EXEC-005 telemetry and SHADOW-002 lifecycle, adding venue/strategy degradation incidents and bounded demotion proposals.
- **Contracts/dependencies:** EXEC-005/008 and CAD-001; alerts cannot self-modify execution or restore eligibility.
- **Tests/evidence/rollback/done:** Test noisy metrics, outage, recovery and alert dedupe. Retain incident/review chain. Rollback keeps conservative execution settings. Done when degradation triggers accountable review before continued use.

### EXEC-010 — Asset-class expansion qualification

- **Status/scope/reuse/gap:** Planned; reuse DATA, BT, risk and execution contracts, adding a mandatory dossier for each new market's mechanics.
- **Contracts/dependencies:** DATA-001..003, BT-004/005 and EXEC-001..009; qualification is asset/venue specific.
- **Tests/evidence/rollback/done:** Cover sessions, settlement, corporate actions, margin, liquidity and adapter behavior. Retain full qualification dossier. Rollback disables the new market. Done when expansion cannot inherit unsupported assumptions from crypto or another asset class.

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

### UI-004 — Digest-safe approval center

- **Status/scope/reuse/gap:** Planned; reuse approvals and durable outbox, adding digest diffs, risk, expiry, prerequisites, clarification and safe links across all domains.
- **Contracts/dependencies:** OPS-001 and GOV-001/002; only executable, current proposals expose approval actions.
- **Tests/evidence/rollback/done:** Test stale/deep-link replay, duplicate notification, changed plan, clarification and rejection. Retain decision receipts. Rollback revokes outstanding links. Done when one current gate yields at most one actionable notification.

### UI-005 — Operations, incident and recovery console

- **Status/scope/reuse/gap:** Planned; reuse fleet, backup and service health surfaces, adding SLOs, deployments, incidents, runbooks and recovery evidence.
- **Contracts/dependencies:** PLAT-001/004..008 and OPS-004/005; read-only by default, mutations become typed approvals and brokered operations.
- **Tests/evidence/rollback/done:** Test stale telemetry, partial outage, rollback and inaccessible service. Retain operator task evidence. Rollback removes mutation controls. Done when service truth and recovery ownership are visible without terminal archaeology.

### UI-006 — Accessible responsive founder experience

- **Status/scope/reuse/gap:** Planned; reuse Mission Control design system, completing keyboard, screen-reader, focus, responsive and long-content behavior on Mac/desktop.
- **Contracts/dependencies:** UI-001..005; shared components preserve status/risk semantics and stable layout.
- **Tests/evidence/rollback/done:** Run accessibility automation, keyboard paths, zoom/mobile widths and founder usability tasks. Retain screenshots/results. Rollback retains prior accessible component. Done when critical workflows remain understandable and operable across supported viewports.

### CHAN-001 — Restricted Telegram founder channel

- **Status/scope/reuse/gap:** Planned toward production qualification; reuse gateway, planner, outbox and safe approvals, closing clarification, dedupe, status and outage behavior.
- **Contracts/dependencies:** OPS-001/002, UI-004 and AGT-004; plain English creates proposals, non-executable requests ask questions, and secrets/sudo are prohibited.
- **Tests/evidence/rollback/done:** Test spoofed user, replay, flood, stale link, outage, clarification and secret input. Retain redacted transcripts. Rollback disables commands while status remains. Done when mobile intake is safe and never bypasses Mission Control authority.

### PLAT-001 — Service catalog and dependency inventory

- **Status/scope/reuse/gap:** Planned; reuse role/deployment and systemd/container inventories, adding owners, SLOs, APIs/events, data classes and recovery plans.
- **Contracts/dependencies:** BASE-002/003; catalog records are versioned and runtime observations reconcile against them.
- **Tests/evidence/rollback/done:** Test orphan service, incompatible API, missing owner and stale dependency. Retain catalog/reconciliation report. Rollback pins prior catalog. Done when every runtime dependency and recovery owner is discoverable.

### PLAT-002 — Workload identity, authorization and secrets lifecycle

- **Status/scope/reuse/gap:** Planned; reuse agent tokens, root-owned environments and package permissions, adding workload identity, RBAC/ABAC, rotation and break-glass lifecycle.
- **Contracts/dependencies:** GOV-001 and AGT-001; credentials bind workload, scope, machine, expiry and audit without entering prompts/logs.
- **Tests/evidence/rollback/done:** Test revocation, rotation, confused deputy, secret leak and emergency access. Retain redacted drills. Rollback revokes new identity and restores scoped prior credential. Done when least privilege and rotation are proven.

### PLAT-003 — Signed artifact and package supply chain

- **Status/scope/reuse/gap:** Planned; reuse role-package signing and promotion states, adding SBOM, provenance, vulnerability/policy gates and artifact verification.
- **Contracts/dependencies:** PLAT-001/002 and AGT-005; build outputs bind source, builder, dependencies, digest and promotion evidence.
- **Tests/evidence/rollback/done:** Test tamper, unsigned artifact, vulnerable dependency and stale attestation. Retain SBOM/signature/rehearsal. Rollback revokes artifact. Done when only verified rehearsed artifacts can deploy.

### PLAT-004 — Deployment controller, canary and rollback

- **Status/scope/reuse/gap:** Planned; reuse deployment architect, runbook packages and manifests, adding a general source-to-environment controller.
- **Contracts/dependencies:** PLAT-001..003 and GOV-003; deployments bind approved artifact, target, preflight, canary, health and rollback.
- **Tests/evidence/rollback/done:** Test interruption, health failure, incompatible migration and stale approval. Retain provenance/canary/rollback dossier. Done when VM1-to-GitHub-to-VM2/Mac deployment and recovery are reproducible.

### PLAT-005 — Unified observability, SLO and alert routing

- **Status/scope/reuse/gap:** Planned; reuse OPS-004 fleet signals and service logs, adding metrics, traces, SLOs, capacity and accountable routing.
- **Contracts/dependencies:** PLAT-001 and SEC-001; telemetry has bounded cardinality, redaction and stable service identity.
- **Tests/evidence/rollback/done:** Test alert precision, silence, overload, secret leakage and missing telemetry. Retain SLO/incident replay. Rollback disables a noisy rule. Done when alerts are actionable, deduplicated and attributable.

### PLAT-006 — Incident command and postmortem system

- **Status/scope/reuse/gap:** Planned; reuse operational notes, alerts and approvals, adding severity, command roles, timeline, evidence capture and recovery actions.
- **Contracts/dependencies:** PLAT-005, GOV-004 and CAD-002; incident actions bind authority and never rewrite history.
- **Tests/evidence/rollback/done:** Simulate service, data, security and agent incidents. Retain timeline/postmortem/action closure. Rollback pauses unsafe automation. Done when incidents close with accountable recovery and governed learning.

### PLAT-007 — Company-wide backup and disaster recovery

- **Status/scope/reuse/gap:** Planned; reuse OPS-005 verified local backups and RI recovery, adding encrypted off-host retention and integrated recovery for every canonical store.
- **Contracts/dependencies:** PLAT-001/002/005 and OPS-005; policies bind RPO/RTO, retention, encryption, owner and restore procedure.
- **Tests/evidence/rollback/done:** Rehearse loss/corruption and restore on intended machines. Retain off-host manifests and measured drills. Rollback never deletes last verified generation. Done when control plane, RI and application recover across a disaster boundary.

### PLAT-008 — VM2 application and infrastructure operations

- **Status/scope/reuse/gap:** Planned; reuse deployment architect, Postgres/app runbooks, TLS, Caddy and backups, generalizing typed Docker, database, Redis, storage, certificate and DNS packages.
- **Contracts/dependencies:** PLAT-003/004/007 and SEC-002; packages declare target profiles, rehearsal, approvals, rollback and ownership.
- **Tests/evidence/rollback/done:** Run VM2-parity rehearsal, cutover, rotation and restore drills. Retain package/promotion dossiers. Rollback restores prior release/network/certificate state. Done when end-to-end operations no longer require ad hoc commands.

### PLAT-009 — Storage, retention and cleanup lifecycle

- **Status/scope/reuse/gap:** Planned; reuse RI lawful deletion, workspace cleanup and backup retention, adding quotas and lifecycle policy across artifacts, logs and caches.
- **Contracts/dependencies:** RI-010, DATA-003 and PLAT-007; canonical evidence, holds and last verified backups are protected.
- **Tests/evidence/rollback/done:** Test disk pressure, interrupted cleanup, retention hold and accidental canonical target. Retain deletion manifests. Rollback restores reversible tiers. Done when storage growth is forecast, bounded and auditable.

### SEC-001 — System threat models and adversarial security suites

- **Status/scope/reuse/gap:** Planned; reuse corpus scanners, sandboxing and approval boundaries, adding maintained threat models for services, agents, research and capital.
- **Contracts/dependencies:** BASE-002/003 and PLAT-001; every high-risk interface owns abuse cases, controls, detection and containment.
- **Tests/evidence/rollback/done:** Exercise injection, exfiltration, privilege escalation, supply-chain and capital mutations. Retain redacted findings and closure. Rollback disables unsafe surface. Done when high-risk paths have current adversarial evidence.

### SEC-002 — Host, container and network hardening

- **Status/scope/reuse/gap:** Planned; reuse systemd sandboxes, private networks, firewall and secret files, adding intended-machine baselines and vulnerability lifecycle.
- **Contracts/dependencies:** PLAT-002/003/005/008; baselines declare ports, users, capabilities, mounts, patches and exceptions.
- **Tests/evidence/rollback/done:** Test drift, exposed port, vulnerable image, permission and recovery. Retain scans and patch drill. Rollback restores known-good configuration. Done when VM1, VM2 and Mac meet versioned least-exposure baselines.

### WS-002 — Degraded-mode and partial-publication compensation

- **Status/scope/reuse/gap:** Planned; reuse WS-001, outbox and BT-008 compensation, adding whole-company behavior under dependency loss.
- **Contracts/dependencies:** WS-001, GOV-002 and PLAT-005/007; each workflow declares authoritative state, retry and compensation.
- **Tests/evidence/rollback/done:** Inject partitions during approval, execution and publication. Retain fault/recovery replay. Rollback reconstructs from canonical events. Done when no outage creates split-brain authority or orphan canonical state.

### DEMO-001 — Production-like venue demo certification

- **Status/scope/reuse/gap:** Planned; reuse EXEC-008 and shadow infrastructure, adding a governed demo environment and certification gate.
- **Contracts/dependencies:** EXEC-004..008, RISK-005 and PLAT-005; demo uses production-like controls without capital.
- **Tests/evidence/rollback/done:** Rehearse order lifecycle, reconciliation, kill, restart, limits and incidents. Retain certification dossier. Rollback revokes adapter/candidate qualification. Done when operational behavior, not simulated PnL alone, passes.

### LIVE-002 — Evidence-gated scaling and multi-candidate production

- **Status/scope/reuse/gap:** Planned and separately governed; reuse LIVE-001 canary, adding expiring scale decisions and multi-candidate limits.
- **Contracts/dependencies:** LIVE-001, PORT-004, RISK-004/005, EXEC-008/009 and PLAT-005/007; no automatic scaling.
- **Tests/evidence/rollback/done:** Test concentration, degradation, outage, loss limit and emergency kill. Retain founder/risk approvals and production dossier. Rollback reduces allocation or exits under deterministic controls. Done when scaling has current independent evidence and bounded loss.

### EVOLVE-001 — Schema, role and model migration/retirement

- **Status/scope/reuse/gap:** Planned; reuse compatibility ADRs, migrations and package registry, adding cross-version evidence replay and retirement.
- **Contracts/dependencies:** BASE-002, GOV-003 and PLAT-003/004; migrations are versioned, reversible where possible and preserve canonical history.
- **Tests/evidence/rollback/done:** Test old evidence, mixed versions, failed migration and replacement. Retain compatibility/replay report. Rollback restores prior reader/runtime. Done when replacement loses neither lineage nor authority semantics.

### EVOLVE-002 — Company reliability and scientific-throughput scorecards

- **Status/scope/reuse/gap:** Planned; reuse fleet, trial, incident and calibration evidence, adding balanced reliability, safety and scientific-quality measures.
- **Contracts/dependencies:** CAD-002, AGT-005 and PLAT-005; metrics cannot reward volume, confidence theater or concealed negatives.
- **Tests/evidence/rollback/done:** Test gaming, missing data and perverse incentives. Retain scorecard lineage and governance decisions. Rollback retires the metric. Done when improvement claims are calibrated to reliability and evidence quality.

## Shared-surface rules

- RI-001 owns canonical evidence schemas; no concurrent task may invent alternatives.
- BT-003 owns the run-bundle producer contract; RI ingestion consumes it.
- OPS-001 owns approval outbox/readiness semantics; domain pilots consume them.
- DISC-001 owns question selection; the Trial Registry owns search accounting.
- PORT-001 owns candidate/risk policy schemas; LIVE-001 may not bypass them.

The precise recommended next task is **OPS-002**, proving four bounded
plain-English proposal paths now that approval/readiness, qualified retrieval,
curriculum breadth, and production-qualified lifecycle-aware memory exist.
