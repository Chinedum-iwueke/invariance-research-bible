<a id="book-11-engineered-company-system"></a>
# Book XI — The Engineered Company System

**Edition:** Living as-built engineering specification
**Snapshot date:** 2026-08-27
**Scope:** Hermes Swarm, Research Intelligence, Bulletproof BT, Mission Control,
founder channels, VM2 operations, and the public Invariance application

This book states what the company has actually engineered. It complements the first
ten books, which define the institution that must exist. It is intentionally stricter
than a product overview: every material claim identifies its source, evidence class,
runtime location, authority boundary, and known gap.

## Claim vocabulary

| Label | Exact meaning |
|---|---|
| `implemented` | Source, schema and migration exist at a named repository revision. |
| `tested` | Declared automated acceptance checks passed in the recorded environment. |
| `rehearsed` | An isolated or parity environment executed the complete bounded operation. |
| `observed` | A dated pilot or runtime response was retained. |
| `deployed` | The named revision and migration were installed on the named machine. |
| `active` | Runtime health was observed at the snapshot time; this is not a future uptime guarantee. |
| `partial` | A useful subset exists, with consequential missing behavior stated. |
| `planned` | The capability appears only in an approved roadmap or backlog. |
| `unknown` | Current runtime state was not rechecked for this edition. |

No chapter may upgrade a claim because prose sounds complete. Source proves
implementation; tests prove bounded behavior; rehearsal proves environment fit; runtime
evidence proves only the observed deployment window.

## Contents

1. [System topology and authority](chapters/01-system-topology-and-authority.md)
2. [Hermes control plane](chapters/02-hermes-control-plane.md)
3. [Worker runtime and agent catalog](chapters/03-worker-runtime-and-agent-catalog.md)
4. [Research Intelligence](chapters/04-research-intelligence.md)
5. [Bulletproof BT laboratory](chapters/05-bulletproof-bt-laboratory.md)
6. [Founder interfaces and operating channels](chapters/06-founder-interfaces.md)
7. [VM2 platform and Invariance application](chapters/07-vm2-and-invariance-application.md)
8. [Security, reliability and recovery](chapters/08-security-reliability-and-recovery.md)
9. [Verification, gaps and maintenance](chapters/09-verification-gaps-and-maintenance.md)

## Source hierarchy

1. Database migrations, strict schemas and executable policy are authoritative for
   stored data and runtime acceptance.
2. Service and worker tests establish bounded behavior at the recorded commit.
3. Role-package manifests define what a role may request, not proof that an agent is
   currently registered, deployed or online.
4. Systemd and launchd units define process sandboxing, not proof of current health.
5. Pilot and validation records establish dated observations.
6. Roadmaps and the Bible define targets and constraints, never current behavior.

The implementation references and exact pins belong in
[`registers/IMPLEMENTATION_REFERENCES.md`](../../registers/IMPLEMENTATION_REFERENCES.md).
