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
| Agent identity, bearer authentication, leases, lifecycle events | tested; observed | Control-plane routes, worker client/service tests, recorded M4-M15 pilots | No complete multi-service SLO or disaster exercise | M2, M8 |
| Restricted named workflows and isolated Git worktrees | tested; observed | Worker policy, executor, workspace tests and engineering pilots | Broader role catalog remains package-specific | M2 |
| Human approvals and mission supervision | tested; observed | Governance models, Telegram/Mission Control flows, M9 evidence | Approval fatigue and notification correctness need durable SLOs | M2, M8 |
| Immutable hypothesis, experiment, trial, result, review, decision lineage | tested; observed | Research registry services/tests and M11-M13 pilots | Bulletproof run bundles are not yet universally bound to these identities | M1, M3 |
| Research document/chunk ingestion | partial; tested; observed | Research document bundle routes, ingestion scripts, M12/M14B records | Scientific-object recovery, editions, coordinates, tables, figures, equations, and protected evidence are incomplete | M1 |
| Retrieval | partial; tested | Lexical knowledge search, similar-hypothesis search, retrieval evaluation | No production hybrid lexical/vector/graph retrieval or citation replay service | M1 |
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
