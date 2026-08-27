<a id="worker-runtime-and-agent-catalog"></a>
# 3. Worker Runtime and Agent Catalog

## 3.1 Restricted worker architecture

The Python worker is an asynchronous single-task runtime. Its components are:

| Module | Responsibility |
|---|---|
| `api_client.py` | Authenticated typed lifecycle calls and credential-safe error classes |
| `policy.py` / `workflows.py` | Strict task contract and server-local YAML workflow validation |
| `workspace.py` | Direct-child repository resolution and detached per-attempt Git worktrees |
| `executors/` | Named code validation, engineering mission, research experiment and memory-sync execution |
| `service.py` | One identity → heartbeat → lease → validate → prepare → start → execute → terminal cycle |
| `daemon.py` | Serialized polling, idle presence, bounded backoff, signals and shutdown |
| `role_package.py` | Signed package compatibility and active-deployment attestation |
| `supervisor/` | Mission-state reconciliation and bounded autonomous recovery |
| `planner/` | Founder request interpretation into reviewable structured proposals |
| `infrastructure/` | Unprivileged worker, broker client, typed runbooks and root broker implementation |

Workflow subprocesses receive an allowlisted environment, run in their own process
group and never inherit agent credentials. Termination sends SIGTERM, waits a bounded
grace period, then SIGKILLs the process group. Full logs stay in the task workspace;
API results contain bounded summaries and relative log paths.

## 3.2 Repository and command controls

- Repository names cannot contain slash, backslash, traversal or leading dot.
- Repositories must be direct children of the configured root and resolve beneath it.
- Workspaces are deterministic by task, UUID and attempt, mode-restricted, and carry
  ownership metadata before reuse.
- Commands are argument arrays. `shell=True`, shell command strings, `sudo`, `su`,
  shell `-c`, package installation, service management, destructive filesystem tools,
  credential readers and network/firewall tools are rejected in ordinary workflows.
- Git operations are restricted; primary checkout mutation, push, arbitrary fetch,
  remote modification, credential access and global configuration are prohibited.

## 3.3 Declared role-package catalog

The repository currently contains **14 role-package manifests**. A manifest proves a
declared role contract, not that the corresponding agent is active. Live registration,
active package deployment and recent heartbeat must be checked in Mission Control or
the package inventory API.

| Package | Machine | Task types | Risk ceiling | Repository/write authority |
|---|---|---|---:|---|
| `founder-intake-planner` | VM1 | `founder_request` | 1 | No repositories; temporary planning only |
| `restricted-code-validator` | VM1 | `code_validation` | 1 | Three approved repos; isolated workspace; no remote write |
| `vm1-engineering-worker` | VM1 | `code_validation`, `engineering_mission` | 1 | Control plane, Bulletproof and Invariance app; workspace only |
| `vm1-research-runner` | VM1 | `research_experiment` | 1 | Bulletproof; reproducible isolated execution |
| `vm1-research-memory-steward` | VM1 | `research_memory_sync` | 0 | Read-only Bulletproof projection; workspace output |
| `vm1-operational-memory-steward` | VM1 | `operational_memory` | 0 | No repository or execution authority |
| `m14b-research-intelligence-director` | VM1 | `research_intelligence` | 0 | Read-only retrieval/ranking; no repositories |
| `m13-senior-research-specialist` | VM1 | `research_experiment` role stage | 1 | Read-only cited proposal role |
| `m13-experiment-specification` | VM1 | `research_experiment` role stage | 1 | Locks pre-result manifests; no writable roots |
| `m13-research-execution` | VM1 | `research_experiment` role stage | 1 | Executes immutable manifests in workspace |
| `m13-statistical-reviewer` | VM1 | `research_experiment` role stage | 1 | Independent clean-workspace reproduction/review |
| `m13-adversarial-auditor` | VM1 | `research_experiment` role stage | 1 | Leakage, benchmark and falsification attacks |
| `vm2-infrastructure-operator` | VM2 | observation/operation | 3 | Brokered typed infrastructure operations only |
| `vm2-deployment-architect` | VM2 | observation/operation | 3 | Versioned approval-gated runbooks through broker |

## 3.4 Named workflows and runbooks

General worker workflows are `code-validation`, `engineering-mission`,
`research-experiment` and `research-memory-sync`. Infrastructure roles use compiled
observer, restart, PostgreSQL deployment and versioned platform-operation packages.
The presence of a workflow in YAML does not let task input replace its command list.

## 3.5 Agent versus service

The mission supervisor, Telegram gateway, Mission Control web server and root broker
are services, not reasoning agents. They have deterministic operational roles and must
not be counted as autonomous agent identities. Conversely, the five M13 roles are
separate authority identities even when one executable implementation supports them.

## 3.6 Confirmed historical observations

Recorded pilots demonstrate restricted code validation, engineering missions,
research execution, memory synchronization, infrastructure observation/restarts,
deployment runbook phases, mission supervision and a five-role research loop. Present
online state is not inferred from those pilots; it must be checked from current
heartbeats and active deployment attestations.

## 3.7 Effective agent authority

AGT-001 makes the catalog executable rather than descriptive. An agent charter is an
immutable, versioned statement of role, responsibilities, machine and repository
scope, task types, risk ceiling, accountable owner, conflicts and forbidden actions.
A capability grant is separately time bounded and revocable, and is bound to the
exact signed role package it authorizes. Grant and revocation events are digest
chained.

Task leasing now intersects four records: enabled agent registration, active charter,
newest active package deployment and unexpired capability grant. The resolver returns
the charter, package and grant digests plus accountable owner in a permission snapshot
whose digest is retained in the lease event. Missing scope, package replacement,
conflict, expiry or revocation denies the lease before approval consumption. In the
production bootstrap, 14 deployed agents received 41 per-capability grants; a second
run created no records. No record in this registry supplies capital or order authority.

## 3.8 Workload identity and runtime authorization

PLAT-002 binds the credential used by a running service to the exact AGT-001 authority
snapshot that makes that service legitimate. The immutable identity manifest contains
the agent, active charter and role-package digests, machine, control-plane audience,
wildcard-free API scopes, accountable owner and expiry. Authentication rechecks the
enabled agent, active charter, exact active package deployment and complete unexpired
grant set on every request. Revoking or replacing any of those records therefore
invalidates the runtime identity without waiting for credential expiry.

The central authentication dependency maps each agent API path to one explicit scope.
Task lease, task execution, infrastructure brokering, research publication, fleet
observation, operational notes, package inspection and heartbeat are separate rights.
The production bootstrap bound 14 deployed credentials and then activated enforcement
only after the uncovered count reached zero. Its immediate replay created no identity
and rebound no credential.

Credential rotation creates a bounded 30-900 second overlap. Finalization revokes the
prior credential; rollback, while the overlap is still valid, revokes the new credential
and restores the prior identity-bound credential. Logical secret policies contain a
reference, required scope, rotation date, expiry and digest, never a secret value.
Authorization receipts drop secret-, token- and password-like context keys. Emergency
grants require separate founder approval and security review, last at most one hour and
can only halt, isolate or revoke. They cannot read secrets, broaden normal work or grant
capital/order authority.

## 3.9 Provenance-bearing execution context

AGT-002 turns retrieved information into an immutable task-attempt input rather than an
unrecorded prompt side effect. An orchestrator chooses active canonical evidence for the
next unconsumed attempt. Each selected item records canonical object and content digests,
the reason it was selected, access sensitivity, expiry, exact prompt position, replay
coordinates and any contradiction among the selected objects. Positions are unique and
contiguous. Default packs are limited to 32 items and 64 KiB.

Assembly resolves the agent's current AGT-001 charter, exact package and grants itself;
the caller cannot assert an authorization digest. Inactive, cross-project, unapproved
restricted, protected or oversized context fails closed. Protected evidence is never
placed into this path. The complete rendered envelope is stored with a pack digest and
an outer manifest digest, so later replay reconstructs exactly what the agent was
allowed to see rather than re-rendering whichever corpus state happens to be current.

The feature is opt-in per task through `governed_context_required`. Once the agent owns
the lease, the worker fetches the attempt-bound manifest and creates a mode-`0600`
`context-manifest.json` outside the repository checkout before starting execution.
Scratch content stays inside that isolated attempt workspace. The control plane stores
only a digest, safe relative path, kind, sensitivity, expiry and receipt digest. Task
completion, failure or release marks every active scratch receipt discarded while
preserving canonical evidence and the immutable context manifest. The live no-execution
pilot bound real authority and corpus evidence, replayed exactly, discarded its one
scratch receipt and ended cancelled without execution or capital authority.

## 3.10 Typed graphs and bounded multi-agent deliberation

AGT-003 does not introduce a second scheduler. Graph activation materializes normal
Hermes tasks plus existing `task_dependencies`, so every node passes the same approval,
charter, active package, capability grant, machine, risk and lease checks. Its immutable
envelope adds a node ceiling, total-attempt budget, duration/deadline and parallelism
ceiling. Each node declares one role, task contract, typed input/output, stop conditions,
dependencies and an optional compensation task.

Validation rejects cycles, unknown dependencies, duplicate keys and excess attempts.
The lease selector will not cross graph parallelism even when more workers are online.
Task outcomes create typed digest-bound messages; graph events have monotonic sequences
and a predecessor-digest chain, making decisions replayable without hidden chain of
thought. Cancellation reaches running workers in heartbeat responses. Workers terminate
and release; unleased nodes cancel immediately; a late completion is rejected. Failure
or exhausted budget cancels unfinished work and materializes declared compensation for
successful side-effect nodes in reverse graph order. The Mission Supervisor reconciles
deadlines and deadlocks even if no worker emits another event.

PR #133 merged at `283fc415432fa6a124befa2eaad5c9843ed5fd8e`. Its 393 backend
tests and 18 worker service tests passed, and PostgreSQL 16 migrated cleanly through
`b3e7a1c52d90`. VM2 now runs that migration and healthy image
`sha256:598ed40a60b22798e7d1640e396be4c2725b4bf9fb77901cf7db134afc3a11b5`.
The live two-node cancellation replay retained manifest digest
`ef38ec20fddc92080db2a2b85392c92dc4278769a2968ca994f1ed56a3556463`,
event-chain head `d52646f5f0a7f3daade23a9503d261a0490f55b68aa94eb44c20644897fc81a1`
and report digest `3db36e82c88622629381137bf89ce072620489b9027f677609ee1cae8a614295`.
Both nodes cancelled before lease; execution and capital authority were false. The graph
machinery grants no authority itself.

## 3.11 Learning and self-improvement boundary

Hermes improves institutional inputs and future decisions through retained evidence,
negative results, contradictions, retrieval/graph projections, curriculum evaluation,
operational notes, exact context, audit replay and versioned package replacement. That
is a learning company process, not unconstrained recursive self-modification. An agent
cannot rewrite or promote its own charter, prompt, policy, model, package, tools or
authority. Later AGT-004/005 and EVOLVE work must convert failure into a tested proposal,
independent evaluation and authorized release before production behavior changes.

## 3.12 Prompt, policy and reusable-workflow governance

AGT-004 introduces a canonical prompt/policy registry rather than leaving model
instructions embedded anonymously in worker code. An immutable bundle identifies its
semantic version, canonical digest, exact provider/model/runtime/version, prompt
template, instruction-precedence policy, trust labels, allowed tools and data classes,
and fail-closed input/output schemas. Output is explicitly `data_only`: passing the
schema gate does not approve a task, lease a worker, grant a tool, deploy software or
authorize capital.

Every evaluation records a fixture digest, category, violations, evaluator identity
and receipt digest. Valid output and the required prompt-injection, secret-exfiltration,
instruction-collision and malformed-output fixtures must pass before approval or
activation. The producer cannot serve as the only reviewer. Activating a new version
retires the prior active digest while preserving its event chain, so rollback and
historical replay remain possible.

Production replay on 2026-08-27 activated bundle
`12d23600-6ee5-401b-b43e-0f016641e046` at digest
`b00090c9cef72f22eeb56b096854f48bfe81ffefcd4f7b48b2a6ff9a28cf81e3`.
Valid output plus all four adversarial categories passed, its nine-event chain was
retained under report digest
`8fc5f2047ebce3be5d9f204e05eef1aadebc029d1c3e4bafc99f0cba9aa99c99`,
and the report explicitly confirms that action authority remained false.

AGT-009 is the planned reusable-workflow layer. It will distill repeated provenance-
bearing task traces into sanitized typed skill candidates, rehearse them against
historical success and failure cases, and promote only the independently reviewed
digest through the existing package lifecycle. Agents may propose these skills but
cannot approve, deploy or use them to expand their grants. Hidden reasoning, secrets,
one-off task state and unreviewed model text are never reusable institutional skills.

## 3.13 Independent evaluator routing and anti-collusion

AGT-006 replaces reviewer labels with an enforceable routing record. An evaluator
profile is versioned and bound to an enabled agent, declared capabilities and an exact
active role-package digest. A route binds the subject digest, producer identity,
required review kinds and correlation policy before any reviewer is selected. The
selection is deterministic and a route cannot reuse an agent, package or context group
across the producer and evaluators or among evaluators.

The system does not overstate what the current fleet can prove. Host, provider, model
family and runtime are correlation dimensions. Shared dimensions are scored, retained
on each assignment and subject to a pairwise ceiling. A route may permit disclosed
shared infrastructure when its policy allows it, but the receipt says that correlated
risk remains. A stricter policy fails closed when independent capacity is unavailable.
This means two differently named agents running the same package or context do not
become independent merely because the organization chart calls them reviewers.

Only the routed evaluator identity can attach a review ID and digest. After every
required assignment completes, Hermes issues an immutable assertion over the producer,
policy, assignments, review digests and disclosed correlations. Before that point, the
assertion endpoint blocks promotion. The receipt itself provides no execution,
deployment, capital or order authority. Source validation passes all 403 backend tests
with migration `d5a9c3e72f10` as the sole head. Production completion still requires the
migrated VM2 API and the live two-role pilot receipt; this chapter must be updated with
those identities rather than treating source tests as production evidence.
