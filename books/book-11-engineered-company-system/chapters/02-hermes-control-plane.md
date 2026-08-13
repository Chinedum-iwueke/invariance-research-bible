<a id="hermes-control-plane"></a>
# 2. Hermes Control Plane

## 2.1 Runtime stack

The control plane is a FastAPI service with SQLAlchemy models, strict Pydantic schemas,
Alembic migrations, PostgreSQL as canonical state, Redis for runtime coordination, and
filesystem-backed content-addressed evidence artifacts. The production Compose image is
named `invariance-swarm-api:0.4.0` in the recorded VM2 deployment.

Authentication uses separated bearer domains:

- orchestrator/founder token for operator APIs;
- hashed agent credentials for `/v1/agent/*`;
- founder-channel credential for Telegram;
- signing secrets for role-package manifests and mission approvals;
- infrastructure-broker secret for single-use execution tickets.

Secrets are read from protected files or Docker secrets. They are not schema fields,
task inputs, event payloads or worker subprocess environment entries.

## 2.2 Implemented service surfaces

| Surface | Engineering behavior |
|---|---|
| Agents | Registration, credential issuance/revocation, identity, enabled state, capabilities, risk ceiling, machine and heartbeat presence |
| Tasks | Creation, priority, approval state, capability/machine matching, leasing, lease expiry, start, heartbeat, complete, fail, release and immutable events |
| Governance | Approval requests/events, plan digests, risk policy, artifact registration, pause/resume control scopes |
| Missions | Immutable approved mission manifests, work-item dependencies, supervision policy, bounded recovery and reconciliation |
| Packages | Signed versioned role manifests, compatibility ranges, deployment inventory and active attestation |
| Runbooks | Versioned package registry, target profiles, promotion records, rehearsal evidence and typed operations |
| Proposals | Founder intake proposal documents, clarification boundary, materialization/rejection and target-role selection |
| Supervisor | Mission reconciliation, readiness recovery, task-state observation and bounded retry policy |
| Research registry | Sources, snapshots, hypotheses, experiments, trials, results, reviews, decisions, programs and daily cycles |
| Research Intelligence | Canonical evidence, ingestion, retrieval, memory, surveillance, corpus operations/synchronization and RI-008 graph services |
| Operations memory | Non-executing notes, assignment/defer/resolve/reopen transitions and proposal requests |
| Metrics/health | Service readiness, aggregate corpus metrics and bounded health state without protected payloads |

## 2.3 Data model evolution

The single Alembic chain currently spans 27 revisions from the initial agent/task
tables through RI-008. Major layers are:

1. agent credentials, heartbeat and task execution lifecycle;
2. operational controls, role packages, approvals, artifacts and missions;
3. founder proposals, mission supervision and runbook packages;
4. immutable research registry, knowledge documents, daily programs and intelligence;
5. research-memory exports, operational notes and point-in-time data contracts;
6. canonical identity aliases and canonical evidence objects;
7. quarantined scientific ingestion and hybrid retrieval;
8. institutional memory, corpus operations and governed surveillance;
9. continuous corpus synchronization;
10. typed knowledge graph projections and cognitive tool receipts.

Canonical tables are append-only or mutation-constrained where identity and evidence
history require it. Search, vector, graph and analytical tables are projections and can
be rebuilt from canonical records.

## 2.4 State-machine invariants

- A task has at most one live lease owner.
- A lease token is never returned in events or completion output.
- Start must precede fail or complete.
- Complete and fail are mutually exclusive terminal paths.
- Approval is bound to a plan digest; changing the plan requires a new approval.
- Role-package attestation must match an active deployment before agent heartbeat and
  execution are accepted.
- Artifact and evidence identities are content-digest bound.
- No model response can directly change task, approval, package or capital authority.

## 2.5 Current verification boundary

The RI-008 branch records 224 passing backend tests and a single Alembic head
`6e8a1c4d9b20`. RI-008 is implemented and tested in PR 34 but is not described here as
deployed until VM2 migration, projection rebuild and live pilot receipts exist.
