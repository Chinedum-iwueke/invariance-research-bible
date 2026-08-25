<a id="system-topology-and-authority"></a>
# 1. System Topology and Authority

## 1.1 Physical and logical placement

```mermaid
flowchart LR
    Founder[Founder] --> MC[Mission Control on Mac]
    Founder --> TG[Telegram gateway on VM2]
    MC --> API[Hermes API on VM2]
    TG --> API
    API --> CPDB[(Control-plane PostgreSQL)]
    API --> Redis[(Redis)]
    API --> ES[(Canonical evidence object store)]
    API --> VM1[Restricted VM1 workers]
    API --> VM2W[Brokered VM2 workers]
    VM1 --> Worktrees[Isolated Git worktrees]
    VM1 --> BT[Bulletproof BT]
    VM2W --> Broker[Root-owned infrastructure broker]
    Broker --> Docker[Approved Docker/system operations]
    Caddy[Caddy] --> Web[Invariance web replicas]
    Web --> PgB[Client-TLS PgBouncer]
    PgB --> IRDB[(Invariance Research PostgreSQL)]
```

### VM1 — engineering and research execution

- Source repositories are direct children of `/home/omenka/Projects`.
- Restricted task workspaces live below the configured workspace root, historically
  `/home/omenka/Projects/swarm-agent-workspaces`.
- Engineering and research workers never execute inside primary checkouts.
- VM1 hosts Codex-authenticated engineering missions, reproducible research execution,
  Bulletproof memory projection, operational-memory recording and research roles.
- VM1 is the only authoring environment in the operating model. Changes flow through
  GitHub before VM2 or the Mac consumes them.

### VM2 — control plane and deployment runtime

- The production control-plane repository is
  `/srv/invariance/swarm/repositories/swarm-control-plane`.
- Its Compose runtime is `/srv/invariance/swarm/control-plane-runtime`.
- The API, control-plane PostgreSQL and Redis run as containers.
- Root-required infrastructure mutations are not granted to agents. An unprivileged
  deployment/infrastructure worker obtains a signed, one-use broker ticket; a
  root-owned broker validates the typed operation and performs only compiled runbook
  actions.
- VM2 also hosts the private Invariance Research database and the on-prem application
  stack described in Chapter 7.

### Mac — founder command center

- Mission Control runs as user `ice`, loopback-only, from
  `~/Library/Application Support/Hermes Mission Control`.
- Its token and environment remain outside Git with mode `0600`.
- The founder research inbox is under Mission Control's protected data directory.
- The Mac submits proposals and approvals; it is not an infrastructure shell or a
  source-of-truth database.

## 1.2 Authority layers

| Layer | May do | May not do |
|---|---|---|
| Founder | Approve bounded plans, risk gates, deployments and research progression | Turn a chat message into an unreviewed privileged command |
| Control plane | Authenticate, validate, lease, record, route and enforce state transitions | Execute arbitrary task-provided shell commands |
| Role package | Declare task types, capabilities, machines, repositories, risk and permissions | Grant itself authority or exceed an active deployment attestation |
| Worker | Execute a named local workflow in an isolated workspace | Write a primary checkout, push, modify remotes, or inherit secrets |
| Infrastructure broker | Execute allowlisted typed operations after ticket validation | Accept free-form commands or reusable tickets |
| Research Intelligence | Store evidence, retrieve, assemble context and retain institutional memory | Approve trials, promote findings or allocate capital |
| Bulletproof BT | Validate strategies and produce research artifacts | Decide production admission or place live orders by research result alone |

## 1.3 End-to-end task lifecycle

```mermaid
sequenceDiagram
    participant F as Founder interface
    participant P as Intake planner
    participant C as Control plane
    participant W as Restricted worker
    participant E as Evidence store
    F->>P: Plain-English objective
    P->>C: Structured proposal
    C-->>F: Scope, risk, role and approval
    F->>C: Approve immutable plan digest
    C->>W: Lease task and token
    W->>C: Start and heartbeats
    W->>W: Validate policy and prepare worktree
    W->>W: Execute named workflow only
    W->>E: Publish bounded artifacts/evidence
    W->>C: Complete or fail exactly once
    C-->>F: Auditable result and event sequence
```

Lease ownership is checked at lifecycle calls. Conflict or lease loss terminates local
execution and forbids stale completion. Policy rejection occurs before start and
releases the lease where the API state machine permits it.

## 1.4 Institutional authority graph

Control-plane PR #117 (`12afe1afa46dda81bfbc35ed14428cb8ee9bed64`) adds the
first machine-enforced institutional authority graph. A policy snapshot binds a
semantic version and canonical SHA-256 manifest digest to:

- canonical principals, role bindings and identity aliases;
- named decision types, allowed actions, environments and maximum risk;
- accountable roles, veto roles and separation-of-duty rules;
- whether a right is delegable or constitutional; and
- constitutional boundaries that no operating exception may waive.

The runtime stores four additive PostgreSQL object families introduced by migration
`e6b1a4d82f90`: policy snapshots, delegations, exceptions and immutable decision
records. A partial unique database index permits only one active policy. Each
resolution binds actor, effective roles, action, object identity and digest, scope,
risk, policy digest, delegation/exception references, outcome, reason and timestamp.
Denied decisions are committed before the API returns `403`, so denial evidence is
not lost with the rejected mutation.

Delegation is a bounded grant rather than a role mutation. It cannot exceed the
grantor's accountable right, decision types, risk or environment and expires within
30 days. More than one applicable grant is ambiguous and therefore fails closed.
Exceptions expire within 24 hours, declare reason, scope, risk and compensating
controls, and require a governance approver distinct from requester and independent
reviewer. Constitutional rules remain unwaivable. Emergency authority admits only
containment verbs: halt, isolate, revoke, quarantine and reduce.

Both `/v1/approvals` and `/v1/founder-channel/approvals` resolve the current authority
policy before approve, reject or revoke changes task state. The Telegram alias maps to
the founder's canonical principal, preventing channel changes from manufacturing
independence. Mission Control's approval surface displays the active policy version,
digest, decision-right count and active delegation/exception counts.

The merged source passed 333 backend and 71 Mission Control tests plus focused policy,
OpenAPI, lint, JavaScript and CI checks. On 2026-08-25 VM2 applied migration
`e6b1a4d82f90`, started the rebuilt healthy API and activated policy version `1.0.0`
with digest `4c3d868fc93d6f33b8d1197cd7b89d303a622a14770c2243ff2f02cb417bfacf`.
Mission Control was reinstalled and independently read that active policy. A live
replay committed authorized decision `83d483cc-d6f6-44ee-b330-4a4bf2eff5ba` and denied
decision `467f5f4a-6534-4c54-9ff1-ba0a6b00aa37`; the latter retained
`action-not-authorized` rather than mutating state. A prior retired snapshot is the
rollback unit, and reactivation itself requires an authorized digest-bound
`policy-activation` decision under the current policy.

## 1.5 Orthogonal institutional lifecycles

Control-plane PRs #118 and #119, ending at
`caa9163af9033df903521858ca534f827c06dc39`, add the GOV-002 lifecycle kernel.
Migration `f7c2a9d41e80` stores four independent projections for every explicitly
registered governed subject:

| Dimension | Initial state | Meaning |
|---|---|---|
| Research | `proposed` | Scientific work and its execution outcome |
| Evidence | `unassessed` | Admissibility, dispute, invalidity, retraction or retirement |
| Operations | `not-considered` | Candidate, approval, shadow, demo or live operating maturity |
| Capital | `no-authority` | Eligibility and bounded allocation authority |

Each transition is an explicit typed command against exactly one projection. It binds
the immutable subject digest, expected projection version, actor, reason, evidence
digests, effective time and a GOV-001 authority-decision record. PostgreSQL row locking
and optimistic versions reject stale concurrent writers. Command IDs are idempotent
only for identical command identity; reuse with changed content fails closed. Events
chain the prior event digest per dimension, and every dossier read replays all four
histories before returning their projections.

Cross-dimension facts are prerequisites, never triggers. Operations progression checks
for succeeded research and admissible evidence but cannot cause either state. Capital
progression checks for live operations and admissible evidence but cannot cause those
states. A research success therefore cannot become deployment or capital authority by
implication. Mission Control displays the four state/version pairs without collapsing
them into a single maturity badge.

The production pilot on 2026-08-25 registered subject
`research-candidate:gov002-orthogonality-pilot-v1` with digest
`2c29d45820e4da3c7b43dc6ec0384eca1c49178adefcd9e257a276fec3f14f51`.
After research reached `succeeded` and evidence `admissible`, operations remained
`not-considered` and capital `no-authority`. A fifth, separately authorized `nominate`
command moved only operations to `candidate`. The replayed dossier digest is
`c8d305c59298b2fb2ef00a502e704a27335a1070f3460c27b434aff1a9a6829c`.
This kernel governs newly registered subjects; it does not silently backfill legacy
status columns, promote an artifact, allocate capital or place an order.
