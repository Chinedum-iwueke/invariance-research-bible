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
