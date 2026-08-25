<a id="hermes-control-plane"></a>
# 2. Hermes Control Plane

## 2.1 Canonical service catalog

PLAT-001 adds a declared-intent layer over the runtime truth already supplied by
Docker, systemd, launchd, role-package deployments, fleet observations and the OPS-007
operation ledger. An immutable `service-catalog-v1.0.0` snapshot identifies every
service by a stable key and records its accountable owner, recovery owner, runtime
kind, intended machines, typed interface versions, required dependencies, handled data
classes, SLO and recovery runbook. Dependency references must resolve inside the same
snapshot. Missing owners, duplicate keys, unknown dependencies and self-dependencies
are rejected before registration.

Registration is idempotent by canonical SHA-256 manifest digest. A semantic version
cannot be reused with different content. Activation is a separate recorded event that
binds the new snapshot, its predecessor, actor and reason. Rollback therefore means
reactivating a retained prior snapshot; neither activation nor rollback changes a
container or service process.

Reconciliation compares bounded observations with the active snapshot and records the
catalog digest, normalized observation digest, ordered findings and report digest. It
fails closed for orphan or missing services, stale evidence, unhealthy state, wrong
machine, runtime-kind drift, interface-version mismatch and unavailable required
dependencies. An observation is evidence about runtime state, never permission to
rewrite declared intent. Recovery routes through the recorded recovery owner and
runbook, after which the native runtime surface must be observed again.

The first source artifact covers 12 known services across VM1, VM2 and the founder Mac.
Its deterministic rehearsal includes both a clean pass and simultaneous orphan,
staleness and interface-drift findings. Production truth requires migration
`a4c7e1f92d60`, explicit activation and a live reconciliation; until that replay is
retained, the implementation is source-complete rather than production-observed.

## 2.2 Runtime stack

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

## 2.3 Implemented service surfaces

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
| Operation ledger | Cross-machine operation identity, owner, phase, honest progress, heartbeat freshness, task reconciliation, exact failure and append-only event replay |

### 2.2.1 OPS-007 operation identity

Migration `b7c3e8a91d40` introduces a canonical operation record that joins work which was
previously visible only through separate task, mission, worker, API and host surfaces.
An operation records its immutable key, kind, project, machine, owner type/identity,
state, phase, progress mode and units, heartbeat, start/completion, retry/cancel
capability, safe error summary, links and input digest. Append-only sequenced events
retain every material transition.

Task reconciliation maps approval waits, queued work, fresh execution, stale execution
and terminal results into this common ledger without replacing the task event source of
truth. Projection reporters commit operation heartbeats through an independent database
session, so disconnecting the initiating browser or terminal cannot erase the running
record. Retrieval reports scientific objects indexed; graph rebuilding reports digest
records processed, active nodes projected and edges projected. Work without a
defensible denominator remains explicitly indeterminate rather than receiving a
fabricated percentage.

The production replay used operation
`c7055a10-0c15-48a5-9faf-367f091a0b54`. It retained `1,080` events before reaching
`succeeded`, projected `784,223` nodes and `1,368,760` edges, and produced fresh graph
manifest `f931765a099aeda5ee3fe8c4dc8225d9843201f8916e64f702a0e5b524f2b277`.
Mission Control replayed the same terminal state and exact units. Final hardening also
timestamps a projection at completion rather than at rebuild start.

## 2.4 Data model evolution

The single Alembic chain includes OPS-007 revision `b7c3e8a91d40` and merge revision
`c9d4f2a71e30`, which reconciles the parallel DISC-001 daily-research revision without
replaying either branch. Major layers are:

1. agent credentials, heartbeat and task execution lifecycle;
2. operational controls, role packages, approvals, artifacts and missions;
3. founder proposals, mission supervision and runbook packages;
4. immutable research registry, knowledge documents, daily programs and intelligence;
5. research-memory exports, operational notes and point-in-time data contracts;
6. canonical identity aliases and canonical evidence objects;
7. quarantined scientific ingestion and hybrid retrieval;
8. institutional memory, corpus operations and governed surveillance;
9. continuous corpus synchronization;
10. typed knowledge graph projections and cognitive tool receipts;
11. fleet-wide operations and append-only progress events.

Canonical tables are append-only or mutation-constrained where identity and evidence
history require it. Search, vector, graph and analytical tables are projections and can
be rebuilt from canonical records.

## 2.5 State-machine invariants

- A task has at most one live lease owner.
- A lease token is never returned in events or completion output.
- Start must precede fail or complete.
- Complete and fail are mutually exclusive terminal paths.
- Approval is bound to a plan digest; changing the plan requires a new approval.
- Role-package attestation must match an active deployment before agent heartbeat and
  execution are accepted.
- Artifact and evidence identities are content-digest bound.
- No model response can directly change task, approval, package or capital authority.

## 2.6 Current verification boundary

The RI-008 branch records 224 passing backend tests and a single Alembic head
`6e8a1c4d9b20`. RI-008 is implemented and tested in PR 34 but is not described here as
deployed until VM2 migration, projection rebuild and live pilot receipts exist.
