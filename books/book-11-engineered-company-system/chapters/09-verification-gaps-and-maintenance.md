<a id="verification-gaps-and-maintenance"></a>
# 9. Verification, Gaps and Maintenance

## 9.1 Current milestone ledger

| Package | Source state | Runtime/evidence state at 2026-08-13 |
|---|---|---|
| BASE-001..003 | Implemented/tested | Completion evidence retained |
| RI-001..006 | Implemented/tested | Isolated/database rehearsals retained; live health must be queried |
| RI-007 | Implemented/tested with PR 31-33 recovery fixes | Live 122-file inbox reconciliation running; not production-complete |
| RI-008 | Implemented/tested in PR 34 | Awaiting merge, VM2 migration, graph rebuild and live pilot |
| RI-009 | Planned | Blocked at final evaluation by unstable corpus and undeployed RI-008 |
| OPS/BT/WS and later packages | Planned or partial as individually recorded | Do not infer completion from historical Hermes M-number pilots |

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

1. Finish and review the current RI-007 inbox reconciliation.
2. Merge PR 34, migrate VM2 and run the RI-008 graph pilot.
3. Freeze the resulting corpus and graph digests.
4. Execute RI-009 domain curriculum and institutional-brain evaluation.
5. Continue the company backlog while maintaining Book XI at each engineering gate.
