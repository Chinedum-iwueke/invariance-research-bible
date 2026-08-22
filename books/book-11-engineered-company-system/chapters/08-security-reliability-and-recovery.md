<a id="security-reliability-and-recovery"></a>
# 8. Security, Reliability and Recovery

## 8.1 Credential separation

- Founder/operator, worker, founder-channel, package-signing, mission-signing,
  supervisor and infrastructure-broker credentials are separate.
- Root-owned environment files are mode `0600`; service users receive only required
  variables/files.
- Tokens, authorization headers and lease tokens are redacted from exceptions/logs.
- Workflow subprocesses receive a minimal environment and never the worker token.
- Telegram does not carry sudo credentials.

## 8.2 Process sandboxing

Worker systemd units run as non-root users with `UMask=0077`, `NoNewPrivileges`,
read-only home/system protections, kernel/control-group protections, restricted address
families and explicit writable paths. Infrastructure privilege is isolated in the
broker rather than widening worker capabilities. Mission Control is local-user and
loopback only.

## 8.3 Filesystem boundaries

Primary repositories are read-only to task execution. Worktrees and audit artifacts
live under bounded roots with metadata ownership checks. Cleanup verifies containment
before removing a worktree and never automatically destroys failed workspaces. Corpus
payloads and credentials are excluded from Git.

## 8.4 Failure behavior

- API clients distinguish authentication, validation, conflict/state, transport and
  server failures.
- Lifecycle mutations are not silently retried.
- Daemons use bounded backoff with jitter for transport/server failures and exit on
  authentication/configuration failures.
- Heartbeat delivery failures are recorded without automatically destroying valid local
  execution; confirmed lease loss terminates it.
- Workflow timeouts terminate process groups.
- Mission recovery is bounded by an immutable supervision policy and approved plan.

## 8.5 Data recovery

Control-plane canonical state is migrated through one Alembic chain. RI backups bind
metadata and digests, require an empty restore target and rebuild disposable projections.
The Invariance application database has separate dump/restore, schema and TLS lifecycle
runbooks. Rehearsals retain rollback receipts; production claims require a dated restore
exercise, not only a successful backup command.

## 8.6 Consequential open risks

- Full off-host backup and disaster recovery are not yet proven company-wide.
- Alerting, tracing and production SLO evidence remain incomplete.
- VM1 and VM2 fleet probes are active, but simultaneous loss of both hosts cannot be
  detected independently until the external watchdog is placed on an always-on VPS
  outside their shared failure domain and its outage/recovery behavior is rehearsed.
- Scientific ingestion uses bounded local scanners, structural repair, independent
  parsing and OCR. A dedicated Codex identity may advise which remaining allowlisted
  method to attempt or recommend a terminal classification, but receives no artifact
  bytes and cannot suppress scanner findings or publish evidence. Stronger
  antivirus/parser process isolation remains future hardening.
- Two founder-inbox artifacts remain terminally quarantined: one needs a replacement
  edition and one requires an approved provenance-preserving redaction decision. Their
  action and attempt history is visible in the blocked-artifact register.
- Role manifests and historical pilots do not guarantee current agent presence.
- No research result has authority to mutate capital.
## 8.7 Fleet observability and founder alerting

### 8.7.1 OPS-004 source architecture

At the 2026-08-22 source boundary, Hermes contains a dedicated fleet-observation
subsystem. Unprivileged VM1 and VM2 probes publish strict, authenticated,
low-cardinality samples to the control plane. Samples contain CPU utilization and load
per core, `MemAvailable`, swap counters, disk and inode capacity, Linux PSI, uptime,
OOM deltas and health for an explicit systemd service allowlist. They never enumerate
process arguments or environments and never carry credentials in their payload.

Migration `b6f2a9c41d80` stores idempotent, digest-bound observations with
`telemetry_raw_30d` retention and introduces incident and incident-event ledgers. The
detector requires three consecutive breaches before warning or critical state and
three consecutive healthy samples before recovery. This hysteresis prevents a single
load spike or one missed sample from notifying the founder. Warning, escalation and
recovery transitions use the OPS-001 founder-notification outbox and therefore inherit
durable deduplication and acknowledgement.

Mission Control reads `/v1/fleet/health` to display current per-machine resource values,
service status and active incidents. Prometheus exposes sample age and incident counts.
Acknowledgement and bounded silence change incident state but grant no remediation
authority.

### 8.7.2 Independent availability boundary

Peer observations allow a surviving VM to detect that the other stopped reporting.
They cannot detect simultaneous VM1/VM2 loss when VM2 also hosts the control plane and
primary Telegram gateway. Hermes therefore includes a separate TCP-only watchdog for
an always-on third host. It persists breach/recovery counters locally and uses a
separate alert-only Telegram credential. The Mac is not accepted as that authority
because it may sleep.

### 8.7.3 Exact claim status

The schemas, migration, services, probes, watchdog, systemd sandboxes, Telegram
rendering, Mission Control view and focused fault tests are `implemented` and locally
`tested`. Migration `b6f2a9c41d80` is deployed, and the hardened VM1 and VM2 probes are
enabled, active and publishing authenticated observations every 20 seconds as
`vm1-developer` and `vm2-deployment`. This establishes operational individual-host
telemetry; it does not yet production-qualify correlated-outage alerting.

The independent watchdog is explicitly deferred until a minimal hardened, always-on
VPS is provisioned outside the VM1/VM2 failure domain. That host must use a dedicated
restricted observer credential and alert-only Telegram fallback, expose no execution
authority, and restrict outbound access to the declared health targets and Telegram.
Production qualification still requires live value comparison with kernel references,
observed Telegram warning/recovery delivery, and digest-bound rehearsals of VM1 loss,
VM2 loss, simultaneous loss, recovery, duplicate suppression and credential rotation.
Rollback disables probes and watchdogs without deleting incident evidence.
