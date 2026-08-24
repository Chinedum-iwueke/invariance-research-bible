<a id="verification-gaps-and-maintenance"></a>
# 9. Verification, Gaps and Maintenance

## 9.1 Current milestone ledger

| Package | Source state | Runtime/evidence state at 2026-08-22 |
|---|---|---|
| BASE-001..003 | Implemented/tested | Completion evidence retained |
| RI-001..006 | Implemented/tested | Isolated/database rehearsals retained; live health must be queried |
| RI-007/012/013 | Implemented/tested/deployed | Incremental inbox, bounded Codex-advised recovery and two-item terminal action register observed |
| RI-008 | Implemented/tested/observed | Live 762,232-node, 1,331,231-edge graph plus replay and tool receipts retained |
| RI-009/009B/011 | Implemented/tested/observed | Twelve-domain portfolio production-qualified; retrieval SLO and graph freshness gates pass |
| RI-010 | Implemented/tested/deployed/observed | Lifecycle, consolidation, supersession, retraction, lawful deletion and projection invalidation pilot passed |
| UI-003A/B/C | Implemented/tested/deployed/observed | Mac Research Workspace, grounded Copilot, graph exploration and canonical replay production-observed |
| OPS-001 | Implemented/tested/deployed/observed | Durable approval outbox and readiness-race closure production-activated |
| OPS-004 | Implemented/tested/deployed/partial | VM1/VM2 probes active; independent correlated-outage watchdog awaits an external always-on host |
| OPS-005 | Implemented/tested/deployed/observed | Two verified generations, isolated 77-table restore drill and persistent VM2 timers retained |
| BT-001 | Implemented/tested/merged | Canonical Python 3.11 contract matrix closes recorded collection and drift defects |
| BT-002 | Implemented/tested/merged | Immutable bounded dataset, availability and correction-lineage contract merged |
| BT-003 | Implemented/tested/merged | Atomic digest-finalized bundle and compatible Hermes producer contract merged; production run not yet claimed |
| Fast-path deprecation | Implemented/tested/merged | Classic event-driven execution is authoritative; legacy accelerated modes fall back explicitly |
| OPS-002, BT-004..009, WS-001 and later packages | Planned or partial as individually recorded | Do not infer completion from historical Hermes M-number pilots or prerequisite completion |

## 9.2 Backlog maintenance rule

Every task heading in `plans/CODEX_IMPLEMENTATION_BACKLOG.md` must acquire an
`Implementation status` paragraph when work begins and be updated at each gate:

1. branch/PR created;
2. source and automated acceptance complete;
3. merged to canonical branch;
4. migration/deployment complete;
5. live or parity evidence captured;
6. known limitations and next dependency recorded.

“Completed” is reserved for the package's stated done condition. If deployment or live
corpus evidence is part of that condition, merged code alone is `implemented`, not
`completed`.

The capability map and executable backlog are now structurally synchronized. All 110
canonical capability IDs in `plans/BIBLE_CAPABILITY_COVERAGE.md` have dedicated backlog
headings. The 80 packages that previously appeared only in compact coverage tables now
have explicit scope, reuse, missing-gap, contract, dependency, test, evidence, rollback
and done boundaries; this includes the full `BT-004` through `BT-008` laboratory chain.
Ledger validation fails if a future capability is added without an executable backlog
heading. This establishes complete planning coverage only: each new packet remains
`planned` until its individual implementation and operating evidence satisfy its done
condition.

## 9.3 Book XI update rule

Every merged feature that changes architecture, data, agents, permissions, workflows,
interfaces, infrastructure or verification must update this book in the same PR or a
linked documentation PR. The author must:

- update the snapshot date only for facts actually rechecked;
- cite repository, commit/PR, migration and validation record;
- classify source, test, rehearsal and deployment separately;
- update the agent table from manifests and the live count from API inventory;
- update diagrams when data flow or authority changes;
- describe migration, rollback, secret and compatibility effects;
- state non-goals and material gaps;
- avoid copying credentials, private payloads or raw corpus data.

## 9.4 Required snapshot commands

The following inventories must be refreshed before a release-level edition:

```text
Control plane: Git SHA, dirty state, Alembic head, OpenAPI routes, test totals
Workers: role-package manifests, workflow digests, systemd units, active deployments
Runtime: agents/heartbeats, tasks, package inventory, migrations, container health
RI: corpus coverage manifest, projection digests, graph manifest, replay samples, SLOs
Bulletproof: Git SHA, dirty state, test/collection matrix, schemas, lake manifest profile
Mac: Mission Control SHA/service status/inbox coverage
VM2: API image/health, broker/worker status, database/app/certificate/backup evidence
```

Runtime snapshots must be redacted and digest-bound. Secrets and authorization headers
must never be stored in this repository.

## 9.5 Immediate next gates

1. Implement `OPS-006`, `CHAN-002` and `UI-007` from the retained 2026-08-23 founder
   transcript so Telegram and Mission Control provide stateful, schema-aware,
   cross-channel conversation with governed defaults and explicit thread control.
2. Implement `BT-004` using the existing Bulletproof engine and tests, adding only the
   causal market-model contracts and evidence still missing from the Bible backlog.
3. Continue `BT-005` through `BT-008` in dependency order so `BT-009` can compose
   qualified engine, orchestration, feature and publication contracts without
   duplicating existing Bulletproof capability.
4. Execute `BT-009` and `WS-001` to prove a founder-approved hypothesis can traverse
   specification, prospective registration, native execution, truth gates, atomic
   bundling, Hermes publication and independent review without capital authority.
5. Provision the deferred external watchdog and rehearse correlated VM1/VM2 outage
   detection before upgrading OPS-004 from partial to production-qualified.
6. Add encrypted off-host control-plane backup replication under PLAT-007; OPS-005's
   local verified lifecycle remains active but is not a substitute for disaster-domain
   separation.
7. Continue the company backlog while maintaining Book XI at every merge, deployment
   and production-evidence gate.

## 9.6 Reconciled merge boundary

The 2026-08-22 laboratory source boundary is:

| Repository | Capability | Canonical merge |
|---|---|---|
| `bulletproof_bt` | BT-001 contract-drift closure | `6a1cbbfbc69bd84281d466316e42e04698c1b3c5` |
| `bulletproof_bt` | BT-002 immutable dataset contract | `54220e21ad1b4b2110c00d243bd4326b7d67c76d` |
| `bulletproof_bt` | BT-003 atomic run bundle | `8f1418415cad4e2327f7e9a6dbb78257609f65e7` |
| `swarm-control-plane` | BT-003 canonical bundle reference producer | `4b7f7d1685c0af5a4cb81b621f49dfeabea5eff8` |

These pins prove merged source, not deployment or a successful production research
cycle. The corresponding runtime claim may be upgraded only after BT-009/WS-001 retain
an end-to-end digest-bound dossier.
