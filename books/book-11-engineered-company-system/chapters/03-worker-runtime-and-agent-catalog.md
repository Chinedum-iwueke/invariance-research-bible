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

## 3.7 Prompt, policy and reusable-workflow governance

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

AGT-009 is the planned reusable-workflow layer. It will distill repeated provenance-
bearing task traces into sanitized typed skill candidates, rehearse them against
historical success and failure cases, and promote only the independently reviewed
digest through the existing package lifecycle. Agents may propose these skills but
cannot approve, deploy or use them to expand their grants. Hidden reasoning, secrets,
one-off task state and unreviewed model text are never reusable institutional skills.
