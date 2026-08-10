<a id="implementation-status"></a>
# Implementation Status Register

**Status:** Controlled implementation baseline
**As of:** 2026-08-10
**Claim vocabulary:** `current`, `partial`, `documented`, `tested`, `observed`, `target`, `extension`, `deferred`, `unknown`, `blocked`

This register separates the completeness of the Bible from the maturity of the institution it specifies. A written chapter is not implementation evidence. A source file is not operational evidence. A passing unit test is not production qualification.

| Capability | Status | Evidence boundary | Consequential gap | Roadmap destination |
|---|---|---|---|---|
| Constitutional doctrine and authority model | current | Books I-II and controlled ADRs | Runtime policy coverage is incomplete | M0, M2 |
| Machine-verifiable repository baseline | current; tested | Identical `implementation-baseline-v1` collectors, schemas, fixtures, and CI artifact workflows in Hermes and Bulletproof | Clean CI artifacts are commit-specific; declared project suites retain recorded upstream failures | BASE-001 complete; BT-001 and control-plane defect closure remain |
| Canonical identity and compatibility | current; tested | ADR-0005, shared `canonical-identity-v1.0.0` schema/readers, compatibility fixtures, and additive Hermes alias-registry migration | Existing records are not backfilled into the new kernel | BASE-002 and RI-001 complete |
| Canonical evidence object kernel | current; tested | Thirteen strict object contracts, immutable create/read APIs, alias and lineage registries, audit events, access-class hook, object-store interface, OpenAPI snapshot, and PostgreSQL migration rehearsal | Existing research records are not backfilled; retrieval projections and UI remain later work | RI-001 and RI-002 complete; RI-003 may begin |
| Quarantined scientific ingestion and recovery | current; tested | Content-addressed quarantine, strict type and malware gates, offline OCR boundary, structural recovery, confidence/remediation policy, atomic canonical publication, coordinate replay, authenticated API snapshot, adversarial fixtures, and PostgreSQL migration rehearsal | Built-in scanner is signature-based; approved production OCR and external antivirus adapters are not deployed; broad corpus import and retrieval projections remain out of scope | RI-002 complete; RI-003 and RI-005 extend retrieval and corpus defense |
| Canonical hybrid retrieval and citation replay | current; tested | Exact identity/text, lexical, deterministic local vector, and graph-assisted projections; declared RRF fusion; access and schema compatibility filters; canonical re-authorization; stale-index detection; exact coordinate replay; typed client; golden evaluation and PostgreSQL rehearsal | Deterministic hashed vectors are a network-free baseline rather than learned domain embeddings; legacy inbox bundles are not backfilled; no retrieval UI or production scale/SLO evidence | RI-003 complete; RI-004 may begin and RI-005 hardens corpus operations |
| Agent identity, bearer authentication, leases, lifecycle events | tested; observed | Control-plane routes, worker client/service tests, recorded M4-M15 pilots | No complete multi-service SLO or disaster exercise | M2, M8 |
| Restricted named workflows and isolated Git worktrees | tested; observed | Worker policy, executor, workspace tests and engineering pilots | Broader role catalog remains package-specific | M2 |
| Human approvals and mission supervision | tested; observed | Governance models, Telegram/Mission Control flows, M9 evidence | Approval fatigue and notification correctness need durable SLOs | M2, M8 |
| Immutable hypothesis, experiment, trial, result, review, decision lineage | tested; observed | Research registry services/tests and M11-M13 pilots | Bulletproof run bundles are not yet universally bound to these identities | M1, M3 |
| Research document/chunk ingestion | current; tested; observed | Existing inbox bundles plus RI-002 canonical source/edition/artifact/scientific-object recovery with coordinates, tables, figures, equations, citations, confidence, remediation, and access hooks | Existing inbox bundles are not backfilled; broad import, production OCR/antivirus adapters, retrieval projections, and recovery SLOs remain incomplete | M1 |
| Retrieval | current; tested | Legacy lexical search plus RI-003 canonical exact/lexical/vector/graph projections, deterministic RRF, compatibility/access filters, staleness gate, coordinate replay, typed client, and versioned golden evaluation | Learned domain embeddings, broad legacy backfill, production scale/SLOs, and Mission Control retrieval UI remain incomplete | M1 |
| Research Intelligence Director | partial; observed | Domain profiles, intelligence runs, role-gated routes, inbox ingestion | Surveillance, novelty/contradiction routing, belief records, corpus defenses, and recovery SLOs are incomplete | M1, M4 |
| Bulletproof research-memory bridge | partial; tested; observed | Read-only bounded SQLite export and digest registration | Export is a projection; full trade memory remains outside canonical Hermes lineage | M1, M3 |
| Daily research scheduling | partial; tested | Program/cycle service and tests | Questions currently rotate through a static approved mandate; `awaiting_brief` is not automatic experiment execution | M4 |
| Bulletproof classic engine | tested | Pinned source and focused engine/accounting tests | Full regression closure and supported environment matrix are absent | M3 |
| Bulletproof portfolio engine | partial; tested | Sleeve-based aggregation and focused tests | Not a unified same-clock matching engine; live routing is not certified | M3, M6 |
| Bulletproof data lake | partial; observed | Read-only manifest profile in Book V Appendix D | Coverage gaps, incomplete point-in-time proofs, and catalog/security controls | M3 |
| Bulletproof run bundles and truth validation | partial; tested | Artifact schemas, deterministic serialization, truth tests | Universal content-addressed bundle finalization and canonical lineage missing | M3 |
| Shadow, replay, demo, micro-live | partial | Execution surfaces and unit tests exist | No audited prospective sequence establishing environment promotion | M5-M7 |
| Portfolio admission and capital allocation | target | Books VII-VIII | Must remain separate from research success | M6-M7 |
| Production operations | partial; observed | VM2 deployment/runbook foundations | Company-wide backup, restore, telemetry, incident, and recovery evidence incomplete | M8 |

## Current operating conclusion

The current system can run bounded, no-capital research pilots with identity, approval, isolated execution, structured evidence, independent reviews, and attributable decisions. It cannot yet claim the complete Research Intelligence architecture specified by Book III, repository-wide Bulletproof regression closure, point-in-time correctness across the lake, or readiness for autonomous capital mutation.
