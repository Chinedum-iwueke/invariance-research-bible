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
