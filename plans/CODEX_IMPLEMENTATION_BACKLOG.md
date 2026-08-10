<a id="codex-implementation-backlog"></a>
# Codex Implementation Backlog

**Status:** Executable task packets
**Rule:** One task ID per branch and review unless its packet explicitly permits otherwise

All tasks inherit these constraints: preserve unrelated changes; never commit data/secrets; use migrations, compatibility readers, and typed schemas; do not grant an agent promotion or capital authority; retain negative/failed evidence; run repository-native formatting/tests plus the named acceptance commands; publish a redacted evidence report; and obtain the named reviewer before merge.

## Wave 0 — Baseline and identity

### BASE-001 — Machine-verifiable implementation baseline

- **Objective/requirement/citations:** Encode repository pins, runtimes, schema inventory, dirty-state guard, and claim vocabulary required by [Book X Chapter 2](../books/book-10-builders-manual/chapters/02-baseline-audit-and-system-boundaries.md) and [Book V Appendix E](../books/book-05-bulletproof-bt-laboratory/appendices/e-requirement-traceability-and-gap-register.md).
- **Repository/files:** Control plane and Bulletproof; new read-only inventory commands plus CI evidence schema.
- **Prerequisites/scope:** None; record, validate, and diff safe metadata only. **Non-goals:** changing dependencies or tests.
- **Data/access:** No raw lake reads beyond manifest metadata; no credentials.
- **Steps/interfaces:** Define `implementation-baseline-v1`; collect pins/runtime/schema/test command metadata; validate; emit digest.
- **Tests/acceptance:** Fixture repos for clean/dirty/missing lock; run schema validation and secret scan.
- **Evidence/rollback/done:** `implementation-baseline.json` and digest; additive removal is rollback; done when repeat collection is stable. **Parallelism/conflicts:** parallel with OPS-001; owns baseline schema. **Reviewer:** architecture owner.

### BASE-002 — Canonical identity and compatibility ADR

- **Objective/requirement/citations:** Map existing Hermes and Bulletproof IDs to the canonical evidence model in [RI Foundation](RESEARCH_INTELLIGENCE_FOUNDATION.md).
- **Repository/files:** Bible ADR plus control-plane schemas/migrations and Bulletproof producer contract.
- **Prerequisites/scope:** BASE-001; specify aliases, version negotiation, immutability, and deprecation. **Non-goals:** data migration or retrieval.
- **Data/access:** Synthetic fixtures only.
- **Steps/interfaces:** Inventory IDs; choose canonical owners; define JSON Schemas/OpenAPI; add compatibility fixtures.
- **Tests/acceptance:** Round-trip old/new records; reject digest mutation and unknown major versions.
- **Evidence/rollback/done:** ADR and compatibility report; rollback retains readers; complete when both repos consume fixtures. **Parallelism/conflicts:** serialized before RI/BT schema work. **Reviewer:** architecture and knowledge authorities.

## Wave 1 — Research Intelligence foundation

### RI-001 — Evidence object schema kernel

- **Objective/requirement/citations:** Implement source, edition, artifact, scientific object, claim, method, assumption, dataset, run, review, decision, belief, and episode identities from Book III and RI-F1.
- **Repository/files:** Control-plane models/schemas/migrations/services/tests; object-store adapter interface.
- **Prerequisites/scope:** BASE-002; additive schemas and compatibility readers. **Non-goals:** embeddings or UI.
- **Data/access:** Synthetic records and hashes; protected classes represented without payloads.
- **Steps/interfaces:** Migrations; strict schemas; immutable create/read APIs; audit events; access-class hook.
- **Tests/acceptance:** Migration up/down rehearsal, digest/idempotency/authorization/lineage tests, OpenAPI snapshot.
- **Evidence/rollback/done:** Migration and schema-coverage report; rollback only before canonical writes; complete at 100% object contract coverage. **Parallelism/conflicts:** owns canonical tables. **Reviewer:** Knowledge steward and DB reviewer.

### RI-002 — Quarantined scientific ingestion and recovery

- **Objective/requirement/citations:** Implement RI-F2 document recovery with hierarchy, coordinates, tables, figures, equations, citations, confidence, and remediation.
- **Repository/files:** Dedicated ingestion package/worker, object-store adapter, RI APIs.
- **Prerequisites/scope:** RI-001; born-digital plus one scanned fixture. **Non-goals:** broad corpus import.
- **Data/access:** Licensed/public fixtures; sandbox parsers; no network by default.
- **Steps/interfaces:** Quarantine, type/malware scan, extraction, structural/object recovery, validation, atomic publish.
- **Tests/acceptance:** Golden PDF fixtures; corrupted/archive-bomb/active-content/injection cases; coordinate replay.
- **Evidence/rollback/done:** Per-stage ingestion report and retained artifact digests; failed publish leaves quarantine only. **Parallelism/conflicts:** parser adapters parallelize after object schema. **Reviewer:** Librarian and security reviewer.

### RI-003 — Hybrid retrieval and citation replay

- **Objective/requirement/citations:** Deliver RI-F3 exact, lexical, vector, and graph-assisted retrieval with citation replay and compatibility filtering.
- **Repository/files:** RI query service, projection builders, evaluation fixtures, API client.
- **Prerequisites/scope:** RI-001 and RI-002 fixture corpus. **Non-goals:** model-authored final decisions.
- **Data/access:** Enforce access at canonical fetch and projection query.
- **Steps/interfaces:** Build projections; reciprocal-rank or declared fusion; replay endpoint; stale-index detector.
- **Tests/acceptance:** Golden relevance, exact citation, table/equation/figure, access denial, stale rebuild and deterministic filter tests.
- **Evidence/rollback/done:** Versioned evaluation report meeting declared thresholds; drop/rebuild projections for rollback. **Parallelism/conflicts:** lexical/vector builders parallelize. **Reviewer:** Independent Knowledge Evaluator.

### RI-004 — Contradiction, negative-result, belief and dossier services

- **Objective/requirement/citations:** Implement RI-F4/F5 and Book III memory forms.
- **Repository/files:** RI schemas/services, Mission Control dossier view, worker client.
- **Prerequisites/scope:** RI-001/003; supporting/opposing evidence, supersession, frozen dossiers, episodes. **Non-goals:** automatic approval.
- **Data/access:** Redact protected evidence while preserving existence and access reason.
- **Steps/interfaces:** Belief ledger; contradiction edges; dossier compiler; episode publisher.
- **Tests/acceptance:** Negative-result recall, conflicting-edition, belief supersession, dossier freeze and cross-role access tests.
- **Evidence/rollback/done:** Replayed dossier with exact citations and opposing evidence. **Parallelism/conflicts:** owns belief semantics. **Reviewer:** Canon Curator and governance reviewer.

### RI-005 — Corpus security, observability and recovery

- **Objective/requirement/citations:** Implement RI-F6/F7 security controls, SLOs, projection rebuild and restore proof.
- **Repository/files:** Ingestion/query services, telemetry, backups/runbooks, security fixtures.
- **Prerequisites/scope:** RI-002/003. **Non-goals:** production source surveillance.
- **Data/access:** No protected content in logs/traces; synthetic secrets and poison documents.
- **Steps/interfaces:** Policy enforcement, parser limits, injection labels, metrics, backup, rebuild, restore rehearsal.
- **Tests/acceptance:** OWASP-style indirect injection, exfiltration, denial, corrupt projection, lost queue and restore drills.
- **Evidence/rollback/done:** Security evaluation and recovery report with measured RPO/RTO. **Parallelism/conflicts:** observability and security fixtures parallelize. **Reviewer:** Security and SRE owners.

### RI-006 — Governed scientific surveillance

- **Objective/requirement/citations:** Implement RI-F8 feeds, correction/retraction state, novelty, technique briefs, contradictions, and routing.
- **Repository/files:** RI connectors, scheduler, research-program proposal APIs, Mission Control.
- **Prerequisites/scope:** RI-003/004/005; begin with two approved primary feeds. **Non-goals:** auto-adoption or auto-trial.
- **Data/access:** Respect licenses, rate limits, allowlists, and source access classes.
- **Steps/interfaces:** Source registry, fetch receipt, novelty report, alert, proposed question, approval route.
- **Tests/acceptance:** Duplicate, retraction, poisoned abstract, outage, retry/idempotency and provenance-replay fixtures.
- **Evidence/rollback/done:** One weekly digest with citation-replayable candidates and approval events. **Parallelism/conflicts:** connector work parallel. **Reviewer:** Canon Curator and research authority.

## Wave 1 — Agent reliability in parallel

### OPS-001 — Approval and readiness race closure

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

## Shared-surface rules

- RI-001 owns canonical evidence schemas; no concurrent task may invent alternatives.
- BT-003 owns the run-bundle producer contract; RI ingestion consumes it.
- OPS-001 owns approval outbox/readiness semantics; domain pilots consume them.
- DISC-001 owns question selection; the Trial Registry owns search accounting.
- PORT-001 owns candidate/risk policy schemas; LIVE-001 may not bypass them.

The precise recommended next task is **BASE-001**, followed by the serialized **BASE-002** identity decision. RI fixture design and OPS-001 failure reproduction may begin in parallel without schema ownership.
