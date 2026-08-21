<a id="codex-implementation-backlog"></a>
# Codex Implementation Backlog

**Status:** Executable task packets
**Rule:** One task ID per branch and review unless its packet explicitly permits otherwise

All tasks inherit these constraints: preserve unrelated changes; never commit data/secrets; use migrations, compatibility readers, and typed schemas; do not grant an agent promotion or capital authority; retain negative/failed evidence; run repository-native formatting/tests plus the named acceptance commands; publish a redacted evidence report; and obtain the named reviewer before merge.

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

**Implementation status:** Production corpus reconciliation completed on 2026-08-14. The retained founder-inbox ledger classifies all 120 files: 117 are canonical or duplicate-backed usable evidence and 3 remain explicitly quarantined. Governed recovery resolved 9 of the final 12 exceptions without weakening content-security policy; one structurally unreadable PDF and two instruction-bearing documents remain quarantined. The continuous Research Ingestion Recovery Steward is implemented and tested, with VM2 service activation still requiring an observed privileged installation. See the control-plane `docs/ri-007-validation.md` and `docs/runbooks/ri-007-pdf-recovery.md` records.

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

### OPS-004 — Fleet observability and founder alerting

- **Objective/requirement/citations:** Continuously and accurately observe VM1 and VM2 resource health and availability, surface actionable incidents in Mission Control, and notify the founder through Telegram without transient-spike noise or duplicate floods.
- **Repository/files:** Control-plane machine-observation, incident and notification schemas/services; bounded local probe; VM1/VM2 systemd units; peer and independent availability watcher; Telegram notification outbox consumer; Mission Control Fleet Health view; operator runbooks and retention policy.
- **Prerequisites/scope:** OPS-001 for durable deduplicated notifications; PLAT-001 service ownership; PLAT-005 owns common telemetry/SLO conventions. Deliver VM1-to-VM2 and VM2-to-VM1 observation first, followed by an independent always-on third observer so simultaneous VM failure remains detectable. **Non-goals:** LLM-decided alert thresholds, automatic privileged remediation, process-environment collection, or treating the sleeping Mac as an availability authority.
- **Data/access:** Probes publish signed, bounded, low-cardinality observations only. Never collect command lines, credentials, process environments or protected payloads. Raw samples have bounded retention; hourly/daily rollups and incident evidence have explicit retention classes.
- **Steps/interfaces:** Collect `MemAvailable`, swap activity, Linux PSI, CPU utilization/load per core, disk/inode capacity, I/O pressure, uptime, OOM events and approved service health every 15–30 seconds; ingest observations idempotently; evaluate sustained multi-signal thresholds; transition incidents through pending, warning, critical, acknowledged, silenced and recovered states; apply hysteresis, cooldowns and maintenance windows; deduplicate Telegram delivery; provide a VM1 fallback notifier when VM2 hosts the primary gateway; expose current state, history and evidence in Mission Control.
- **Tests/acceptance:** Simulated CPU saturation, low available memory, swap thrashing, disk/inode exhaustion, OOM, critical-service failure, packet loss, one missed probe, sustained single-host outage, both-host outage, recovery, restart, clock skew, duplicate delivery, acknowledgement, silence expiry and maintenance-window fixtures. A single spike or isolated missed heartbeat emits no alert; sustained threshold crossings emit exactly one state-change notification; escalation and recovery each emit once; secrets never appear in samples, logs or messages.
- **Evidence/rollback/done:** A retained pilot dossier proves accurate VM1 and VM2 resource readings against operating-system references, single-host outage detection within the declared SLO, independent simultaneous-outage detection, bounded false-positive rate under injected transient faults, durable incident history, Telegram warning/escalation/recovery delivery and Mission Control replay. Rollback disables probes/notifiers without deleting incident evidence. **Parallelism/conflicts:** share telemetry contracts with PLAT-005 and notification semantics with OPS-001; do not create a second alert outbox. **Reviewer:** SRE/operations owner, security owner and founder/operator.

## Wave 2 — Laboratory closure and walking skeleton

### BT-001 — Bulletproof full-suite and contract-drift closure

- **Objective/requirement/citations:** Resolve every recorded collection/failure discrepancy in Book V Appendix E without weakening tests.
- **Repository/files:** Bulletproof dependencies, fixtures, hypotheses/contracts, alert writer, tests/docs.
- **Prerequisites/scope:** BASE-001; diagnose each defect as code/test/config/docs/environment. **Non-goals:** new strategy logic.
- **Data/access:** Synthetic fixtures; no lake mutation.
- **Steps/interfaces:** Commit lock/environment matrix; repair drift; bounded collection shards; publish status.
- **Tests/acceptance:** Full collection and suite by declared shards, lint/type commands, failure reproduction before fix.
- **Evidence/rollback/done:** Test matrix with zero unexplained collection errors/failures. **Parallelism/conflicts:** defect groups parallel except dependency lock. **Reviewer:** Bulletproof maintainer and independent test reviewer.

### BT-002 — Immutable dataset and availability contract

- **Objective/requirement/citations:** Close Appendix D identity, correction, membership, clock and point-in-time gaps.
- **Repository/files:** `bt.research_data`, manifests/schemas/validators/tests/docs.
- **Prerequisites/scope:** BASE-002 and BT-001; content manifests for a bounded dataset family first. **Non-goals:** rewriting raw lake.
- **Data/access:** Read-only existing lake; write new derived manifests outside source partitions.
- **Steps/interfaces:** Dataset/snapshot schemas, partition digests, provenance/correction ledger, availability policies and validators.
- **Tests/acceptance:** Duplicate/gap/clock/correction/membership/lookahead fixtures and read-only lake smoke.
- **Evidence/rollback/done:** Snapshot validation report and RI registration receipt. **Parallelism/conflicts:** schemas before validators. **Reviewer:** Data steward and statistical reviewer.

### BT-003 — Atomic digest-finalized run bundle

- **Objective/requirement/citations:** Give every canonical artifact a schema, content digest, lineage, atomic finalization and failure state.
- **Repository/files:** Bulletproof artifact writers/schemas/validation; Hermes producer endpoint.
- **Prerequisites/scope:** BASE-002, RI-001, BT-001/002. **Non-goals:** live orders.
- **Data/access:** Bounded public/synthetic fixture.
- **Steps/interfaces:** Bundle manifest; temporary/final states; compatibility; idempotent publish receipt.
- **Tests/acceptance:** Repeat run, interruption, corrupt/missing artifact, incompatible schema, duplicate publish, absolute-path/secret scan.
- **Evidence/rollback/done:** Two semantically identical bundle digests under supported environment policy and one retained failed attempt. **Parallelism/conflicts:** owns producer contract. **Reviewer:** Laboratory and Knowledge stewards.

### WS-001 — No-capital walking-skeleton demonstration

- **Objective/requirement/citations:** Execute the complete [walking skeleton](WALKING_SKELETON.md).
- **Repository/files:** Control plane, RI, Bulletproof, worker role packages, Mission Control.
- **Prerequisites/scope:** RI-001 through RI-005, OPS-001, BT-002/003. **Non-goals:** shadow/live mutation.
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

The compact work-package contracts in
[Bible Capability Coverage](BIBLE_CAPABILITY_COVERAGE.md#4-engineering-work-packages)
are incorporated into this backlog by reference. They are active planned work, not an
ideas list. Before implementation, the selected package must be expanded here to the
same repository/scope/data/interfaces/tests/evidence/reviewer detail used by `RI-*`.
The dependency order is:

1. `RI-007`, `RI-008`, `RI-009`, `RI-009B`, `RI-010`, `RI-011`; `OPS-001`, `OPS-002`, `OPS-004`; `GOV-001`, `GOV-002`, `GOV-003`, `GOV-004`; `AGT-001`, `AGT-002`, `AGT-003`, `AGT-004`, `AGT-005`, `AGT-006`, `AGT-007`, `AGT-008`.
2. `DATA-001`, `DATA-002`, `DATA-003`; `BT-001`, `BT-002`, `BT-003`, `BT-004`, `BT-005`, `BT-006`, `BT-007`, `BT-008`; `UI-001`, `UI-002`, `UI-003`, `UI-004`; `CHAN-001`; `WS-001`, `WS-002`.
3. `DISC-001`, `DISC-002`, `DISC-003`, `DISC-004`, `DISC-005`, `DISC-006`, `DISC-007`, `DISC-008`, `DISC-009`; `SHADOW-001`, `SHADOW-002`; `ML-001`, `ML-002`, `ML-003`, `ML-004`, `ML-005`, `ML-006`; `RL-001`, `RL-002`, `RL-003`.
4. `PORT-001`, `PORT-002`, `PORT-003`, `PORT-004`; `RISK-001`, `RISK-002`, `RISK-003`, `RISK-004`, `RISK-005`; `EXEC-001`, `EXEC-002`, `EXEC-003`, `EXEC-004`, `EXEC-005`, `EXEC-006`, `EXEC-007`, `EXEC-008`, `EXEC-009`, `EXEC-010`; `DEMO-001`.
5. `PLAT-001`, `PLAT-002`, `PLAT-003`, `PLAT-004`, `PLAT-005`, `PLAT-006`, `PLAT-007`, `PLAT-008`, `PLAT-009`; `SEC-001`, `SEC-002`; `UI-005`, `UI-006`; `CAD-001`, `CAD-002`; `OPS-003`.
6. Separately governed `LIVE-001`, `LIVE-002`, then `EVOLVE-001`, `EVOLVE-002` and deferred `LLM-001`.

Parallel work is allowed only where the coverage dependency graph and the ownership
rules below do not conflict. Capital work cannot become executable merely because its
software prerequisites exist; its independent evidence and human approval gates remain
mandatory.

## Shared-surface rules

- RI-001 owns canonical evidence schemas; no concurrent task may invent alternatives.
- BT-003 owns the run-bundle producer contract; RI ingestion consumes it.
- OPS-001 owns approval outbox/readiness semantics; domain pilots consume them.
- DISC-001 owns question selection; the Trial Registry owns search accounting.
- PORT-001 owns candidate/risk policy schemas; LIVE-001 may not bypass them.

The precise recommended next task is **OPS-002**, proving four bounded
plain-English proposal paths now that approval/readiness, qualified retrieval,
curriculum breadth, and production-qualified lifecycle-aware memory exist.
