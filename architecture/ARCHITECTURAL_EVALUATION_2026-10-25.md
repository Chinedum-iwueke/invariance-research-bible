# Invariance Research Architectural Evaluation

**Assessment date:** 2026-10-25<br>
**Scope:** Phase 2 of the Agentic Systems Mastery and Evolution Program<br>
**Evidence baseline:** [`ARCHITECTURAL_RECONNAISSANCE_2026-10-25.md`](ARCHITECTURAL_RECONNAISSANCE_2026-10-25.md)<br>
**Change boundary:** Evaluation only. This document does not change a runtime, grant authority, or certify profitability.

## 1. Executive judgment

Invariance Research is a real distributed research platform, not merely a collection
of prompts. Its strongest architectural properties are immutable scientific
receipts, explicit authority boundaries, a durable task model, independently routed
review, and a native backtesting laboratory with causal and reproducibility controls.
Its principal weakness is that those strong local mechanisms do not yet compose into
a uniformly reliable autonomous institution. Several control loops are duplicated,
runtime truth is spread across repositories and hosts, model-driven production often
fails before scientific execution, and operational telemetry can overstate progress
when task completion is confused with terminal experimental evidence.

The near-term architectural objective should therefore be **reliable composition**, not
more agents. The system should make one authoritative answer available for each of the
following questions:

1. What objective is active?
2. What work is runnable now, and why?
3. Which component owns the next transition?
4. What evidence proves the transition occurred?
5. What failed, what state was retained, and what bounded recovery follows?
6. What authority, if any, can the result exercise?

The recommended program begins with canonical state and evidence projections,
contract testing across repository boundaries, and measurable recovery. It then
tests whether model-driven agent specialization actually outperforms simpler
deterministic or single-agent baselines.

## 2. Evidence rubric

This evaluation does not use a maturity score. A numerical score would hide the
difference between code that exists and behavior demonstrated under interruption.
Every capability is instead assigned the strongest supported evidence class.

| Class | Meaning | Required evidence |
|---|---|---|
| `Unknown` | Visibility was absent or conflicting. | No dependable claim is made. |
| `Planned` | A specification, backlog item, or manifest describes the capability. | Documentary evidence only. |
| `Source-verified` | The execution path and contracts were inspected. | Source symbols and configuration. |
| `Test-verified` | Repeatable automated tests exercise the claimed behavior. | Named tests and passing result. |
| `Runtime-evidenced` | A deployed instance produced an attributable observation. | Runtime state, logs, or receipt. |
| `Recovery-evidenced` | The capability survived a controlled failure or restart. | Fault, recovery trace, and reconciled terminal state. |

Evidence classes apply to a claim, not to an entire subsystem. For example, durable
task leasing is source-verified and test-verified; every deployed worker's ability to
recover every task type is not thereby recovery-evidenced.

## 3. Evaluation method

The assessment uses the repository and runtime evidence catalogued in Phase 1. Each
dimension below contains:

- the current architecture and strongest supported evidence;
- strengths and weaknesses;
- realistic failure modes and debt;
- simpler and more elaborate alternatives;
- a recommendation with benefit, difficulty, and prerequisite knowledge; and
- a controlled experiment that could falsify the recommendation.

No backtest result is treated as evidence of trading profitability. No successful
agent task is treated as evidence that its scientific conclusion is valid.

## 4. Agent design and capability boundaries

### Current architecture and evidence

Agent identity, charters, grants, packages, deployments, workload identities, and
reviewer profiles are persisted by the control plane. Runtime behavior enters through
`WorkerDaemon.run`, `WorkerService.run_once`, and typed executors. Specialized role
packages define research, representation, strategy engineering, review, and execution
work. Authority is checked separately in `backend/app/services/authority.py`.

**Evidence class:** Source-verified for the general contract; runtime-evidenced for
the currently registered VM1/VM2 agents; unknown for offline execution hosts.

### Assessment

**Strengths.** Identity and permission are explicit. Typed executors make many agent
boundaries inspectable. Independent review is represented as a different identity and
route instead of an informal second prompt.

**Weaknesses.** The label *agent* covers materially different things: deterministic
daemons, LLM-backed synthesis, coding runtimes, and scheduled reconcilers. Several
roles exist because of organizational naming rather than demonstrated need for an
independent decision-maker. Prompt, model, tools, and context are not always exposed
as one versioned capability contract.

**Failure modes.** A role can be registered but unable to execute its package; two
agents can repeat the same reasoning; a reviewer can share hidden model or context
correlations with the producer; and a broad grant can outlive the behavior for which
it was issued.

**Debt and missing capability.** There is no single machine-readable inventory that
answers why each role requires agency, its deterministic baseline, model identity,
tool boundary, context budget, and retirement condition.

### Alternatives and recommendation

1. **Simpler baseline:** replace a role with a deterministic function or state
   transition whenever inputs, outputs, and policy are fully enumerable.
2. **Single-agent baseline:** use one bounded reasoning agent with typed tools for a
   complete low-risk research preparation task.
3. **Specialized multi-agent design:** retain multiple agents only where information
   separation, independent judgment, or parallelism is measured to improve outcomes.

Adopt a versioned `AgentCapabilityContract` and require an *agency justification* for
every role. The contract should bind model family, prompt digest, tools, data scopes,
authority, state access, termination, evaluation suite, and deterministic baseline.

**Expected benefit:** fewer ornamental agents, clearer audits, and comparable agent
performance. **Difficulty:** medium. **Prerequisites:** interfaces, capability-based
security, structured model outputs, and experimental controls.

**Validation experiment:** select one research-intake task and compare deterministic,
single-agent, and current specialist paths on the same 50-item corpus. Measure verified
completion, unsupported claims, latency, cost, interventions, and duplicate work.

## 5. Task decomposition and planning

### Current architecture and evidence

`build_task` creates typed tasks with dependencies, plans, approval metadata,
capabilities, and machine constraints. Alpha discovery and campaign reconcilers
deterministically decide the next phase while selected executors perform model-driven
synthesis or engineering.

**Evidence class:** Test-verified for core task creation and transitions;
runtime-evidenced for alpha campaigns; recovery evidence is incomplete across task
families.

### Assessment

**Strengths.** Plans are digest-bound. Dependencies and retry budgets are durable.
Scientific phases are explicit rather than buried inside an opaque conversation.

**Weaknesses.** Planning is distributed across route handlers, reconcilers, task
builders, prompts, and deployment scripts. The same conceptual stage can appear as a
campaign phase, task status, conversation work event, and Mission Control projection.

**Failure modes.** A task is terminal while the campaign remains actionable; an old
approval is mistaken for permission to execute a successor; a model emits an
unmaterializable plan; or a reconciliation loop repeatedly creates semantically
duplicate work.

**Debt and missing capability.** There is no validated intermediate plan language
covering objective, assumptions, dependencies, expected artifacts, evidence gates,
authority, compensation, and termination.

### Alternatives and recommendation

1. Keep hand-coded state transitions for safety-critical and high-volume paths.
2. Introduce a typed declarative task graph for bounded research workflows.
3. Allow model-generated planning only as a proposal compiled into that graph and
   rejected before persistence if it violates invariants.

Adopt option 2 with option 3 at the edge. A deterministic compiler should translate a
typed `ResearchPlan` into tasks. Models may fill unresolved scientific fields but may
not invent state transitions or authority.

**Expected benefit:** fewer schema mismatches and explainable plans. **Difficulty:**
high. **Prerequisites:** graph algorithms, schema evolution, state machines, and
property-based testing.

**Validation experiment:** replay 25 historical campaigns through the compiler and
compare generated graphs with immutable evidence. Failure criteria are omitted gates,
non-idempotent materialization, or any authority expansion.

## 6. Orchestration and coordination

### Current architecture and evidence

Coordination is hybrid: deterministic reconcilers and directors on VM2, workers and
specialists on VM1, database-backed leases, systemd supervision, and native
Bulletproof capacity scheduling. There is no single cognitive orchestration brain.

**Evidence class:** Runtime-evidenced for the hybrid topology; recovery-evidenced for
selected orphan-lock and successor-task cases, not for the whole system.

### Assessment

**Strengths.** The database is a durable coordination point. Leases constrain double
execution. Reconcilers can derive next actions after process loss. Bulletproof
capacity management recognizes memory as a scheduling constraint.

**Weaknesses.** Multiple directors can have overlapping responsibility. Service
presence is sometimes mistaken for productive work. Host-level scheduling and
scientific-stage scheduling are only loosely coupled.

**Failure modes.** Thundering reconcilers, lease starvation, work stranded behind an
offline capability, duplicate successors, capacity oversubscription, and a queue that
appears full while no native experiment is running.

**Debt and missing capability.** A canonical orchestration projection and formally
defined ownership of every state transition are absent.

### Alternatives and recommendation

1. **Central workflow engine:** one durable orchestrator owns every transition.
2. **Event choreography:** services react to immutable events without a central owner.
3. **Current hybrid, clarified:** a deterministic control plane owns lifecycle state;
   domain schedulers own bounded execution; events are evidence, not competing truth.

Choose option 3 now. Publish a transition-ownership table and enforce single-writer
semantics per lifecycle field. Evaluate a workflow engine only after measuring current
recovery and coordination overhead.

**Expected benefit:** less split-brain state and easier incident diagnosis.
**Difficulty:** high. **Prerequisites:** distributed state machines, leases,
idempotency, and event sourcing.

**Validation experiment:** inject worker death, director restart, duplicate delivery,
and delayed result publication into a two-campaign simulation. Require exactly one
terminal scientific receipt per attempt and bounded convergence.

## 7. Tool integration and execution

### Current architecture and evidence

Executors call repositories, coding agents, native scripts, APIs, and Bulletproof
entry points through typed task contracts. The execution laboratory exposes registered
strategies through `run_alpha_research_assignment.py::execute_registered`.

**Evidence class:** Source-verified and runtime-evidenced for several tool paths;
uneven recovery evidence.

### Assessment

**Strengths.** Native execution is preferred over prose simulation. The backtester,
resampler, receipt builder, risk engine, and router are separable tools.

**Weaknesses.** Tool prerequisites have repeatedly diverged between isolated
engineering workspaces and Bulletproof's real environment. Tool outputs are not all
normalized into one error and artifact envelope.

**Failure modes.** Missing dependencies, wrong repository revision, inaccessible data,
unbounded subprocesses, partial file mutations, and success reported without required
artifacts.

**Debt and missing capability.** There is no universal tool manifest declaring
version, environment, inputs, side effects, artifacts, timeout, resource envelope,
and compensating action.

### Alternatives and recommendation

Keep tools specialized, but wrap them in a common `ToolExecutionReceipt`. Validate
environment and artifact expectations before costly model work. Prefer deterministic
scaffolding and validators before asking a coding model to edit a strategy.

**Expected benefit:** cheaper failures and portable execution. **Difficulty:** medium.
**Prerequisites:** subprocess isolation, content-addressed artifacts, and contract
testing.

**Validation experiment:** run the same strategy-authoring fixture in a clean
workspace, VM1 runtime, and CI container. Require identical preflight decisions and
artifact digests before native numerical execution.

## 8. Memory and context engineering

### Current architecture and evidence

Institutional memory spans PostgreSQL records, evidence objects, retrieval and graph
projections, immutable receipts, repository history, and conversation work events.
Context packs bind selected evidence to reasoning tasks.

**Evidence class:** Source-verified for persistence and context construction;
runtime-evidenced for current retrieval/graph epochs; RI-015 reasoning quality remains
not demonstrated.

### Assessment

**Strengths.** Provenance and digests are first-class. Negative results can be
retained. Canonical evidence is distinguished from derived projections.

**Weaknesses.** “Memory” describes several incompatible layers. Model context quality,
compression loss, novelty use, and the actual effect of prior failures are not yet
measured end to end.

**Failure modes.** Stale projections, missing payload after lawful deletion, context
overflow, irrelevant retrieval, accidental leakage from future evidence, and a model
claiming to remember data that was not in its context.

**Debt and missing capability.** Every reasoning receipt should expose context object
IDs, selection policy, token budget, truncation, and excluded high-ranked evidence.

### Alternatives and recommendation

Use three named layers: canonical evidence, rebuildable retrieval projections, and
ephemeral model context. Introduce context-selection evaluations before adding new
memory mechanisms. Summaries must point to superseded source spans and disclose loss.

**Expected benefit:** inspectable reasoning inputs and safer compression.
**Difficulty:** medium. **Prerequisites:** information retrieval, embeddings,
provenance, and evaluation design.

**Validation experiment:** construct 100 answerable research questions with known
evidence. Compare lexical, vector, graph-expanded, and hybrid context builders on
source recall, irrelevant-token ratio, supported-answer rate, latency, and cost.

## 9. Knowledge retrieval and provenance

### Current architecture and evidence

The ingestion and evidence services maintain source identity, payload lifecycle,
retrieval projections, graph state, and source-bound claims. Equation-dependent work
is intended to require independent or deterministic assurance.

**Evidence class:** Runtime-evidenced for current derived-state reconciliation;
source-verified for provenance contracts; corpus-wide mathematical fidelity is not
qualified.

### Assessment

**Strengths.** The design refuses to equate retrieval with truth. Lawful deletion can
retain a lifecycle dossier without pretending payload remains available.

**Weaknesses.** Catalog and payload semantics can surface confusing HTTP behavior to
clients. Mathematical and table fidelity remain a known boundary. External-web
research has less mature provenance than the canonical corpus.

**Failure modes.** Citation drift, deleted bytes presented as retrievable, OCR damage,
equation transcription errors, source/version ambiguity, and prompt injection from
external content.

**Debt and missing capability.** A provenance conformance suite should test every
ingestion route, deletion state, equation path, and external-source adapter.

### Alternatives and recommendation

Retain strict source replay. Add typed content states (`available`, `restricted`,
`deleted`, `metadata_only`) and require clients to render them distinctly. For
equations, combine layout extraction, symbolic parsing, executable dimensional or
property tests, and an independent model only as a disputable reviewer.

**Expected benefit:** fewer false claims of availability and safer mathematical use.
**Difficulty:** high. **Prerequisites:** information retrieval, OCR, symbolic algebra,
and adversarial content handling.

**Validation experiment:** curate a gold set of 200 prose, table, and equation objects;
measure exact source resolution, cell/formula fidelity, deletion behavior, and answer
support under two independent extraction paths.

## 10. State persistence and durable execution

### Current architecture and evidence

PostgreSQL persists tasks, leases, attempts, campaigns, evidence, receipts, authority,
and derived state. Workers heartbeat and leases expire. Reconcilers reconstruct next
actions. Immutable results are content-bound.

**Evidence class:** Test-verified for many transitions; runtime- and selective
recovery-evidence exist.

### Assessment

**Strengths.** Durable records and idempotency are core design concerns. Task attempts
and terminal evidence survive worker processes.

**Weaknesses.** Idempotency rules are not expressed uniformly. Some repair behavior
lives in one-off scripts or migration-specific logic. Cross-repository publication is
not one atomic transaction.

**Failure modes.** Lease expiry during valid long work, double publication, receipt
without campaign transition, transition without artifact availability, and counters
derived from retry events rather than immutable attempts.

**Debt and missing capability.** A formal state-transition specification and a
replayable event ledger for material lifecycle transitions are missing.

### Alternatives and recommendation

Do not rewrite the platform as pure event sourcing. Keep normalized state for command
handling and add an append-only transition journal transactionally written with every
material state mutation. Derive counters from immutable attempts and receipts.

**Expected benefit:** trustworthy recovery and historical reconstruction.
**Difficulty:** high. **Prerequisites:** transactions, outbox patterns, event sourcing,
and temporal queries.

**Validation experiment:** property-test arbitrary sequences of create, lease,
heartbeat, expire, retry, cancel, publish, and reconcile. Assert invariant counters,
single terminal publication, and replay equivalence.

## 11. Distributed-systems reliability

### Current architecture and evidence

The deployed system crosses Mac, VM1, VM2, and intended VPS execution nodes over
Tailscale, HTTP APIs, PostgreSQL, Redis, systemd, and containers. VM1 and VM2 have
demonstrated useful operation; both VPS nodes were offline during the audit.

**Evidence class:** Runtime-evidenced for the reachable core; unknown for current VPS
execution readiness; no system-wide recovery certification.

### Assessment

**Strengths.** Machines have bounded roles. Services are supervised. The system can
continue to retain durable work when a worker is absent.

**Weaknesses.** Host identity, service health, network reachability, capability
availability, and productive throughput are not presented as distinct states. Manual
deployment scripts remain important.

**Failure modes.** Network partitions, clock skew, stale service discovery, host disk
pressure, split deployments, database bottlenecks, inaccessible artifacts, and
silent loss of the only worker with a required capability.

**Debt and missing capability.** There is no repeatable multi-host disaster-recovery
exercise with measured recovery point and recovery time objectives.

### Alternatives and recommendation

Avoid adding Kubernetes at current scale. Standardize declarative host manifests,
health contracts, artifact replication, deployment verification, and fault drills on
the existing systemd/container topology.

**Expected benefit:** reliability without an unnecessary orchestration platform.
**Difficulty:** medium-high. **Prerequisites:** networking, Linux service management,
distributed tracing, backups, and consensus fundamentals.

**Validation experiment:** quarterly game day: isolate VM1, restart VM2, delay Redis,
and make one capability unavailable. Measure data loss, time to detection, bounded
degradation, recovery time, duplicates, and operator actions.

## 12. Observability and debugging

### Current architecture and evidence

Structured logs, heartbeats, Mission Control projections, task attempts, fleet
observations, campaign state, conversation work events, and scientific receipts are
available. Mission Control can show workflows, agents, knowledge, and venue replay.

**Evidence class:** Runtime-evidenced, but semantic accuracy varies by view.

### Assessment

**Strengths.** Durable scientific and operational records provide strong raw material.
Recent UI work makes several flows explorable rather than log-only.

**Weaknesses.** Activity counts can classify successful preparation tasks as
backtests. Correlation across conversation, plan, task, attempt, campaign, native run,
receipt, and decision is not uniformly one click. Health and liveness can be stale.

**Failure modes.** Green dashboards with no scientific progress, noisy alerts,
missing causal chain, log retention gaps, and investors or operators drawing the
wrong conclusion from an aggregate count.

**Debt and missing capability.** A canonical trace envelope and semantic metric
dictionary are needed. Every displayed count must link to qualifying records.

### Alternatives and recommendation

Adopt end-to-end correlation IDs and OpenTelemetry-compatible traces, but keep
immutable domain receipts as scientific truth. Mission Control metrics should expose
their inclusion predicate and freshness.

**Expected benefit:** faster diagnosis and honest operational narratives.
**Difficulty:** medium. **Prerequisites:** telemetry semantics, tracing, and product
information design.

**Validation experiment:** give an engineer five injected incidents and only Mission
Control plus documented runbooks. Measure time to root cause, false leads, and whether
the complete causal chain can be recovered.

## 13. Testing and independent verification

### Current architecture and evidence

The repositories contain unit, integration, contract, migration, scientific gate,
and UI tests. Strategy and causality review can be routed to independent reviewer
profiles. Bulletproof validates causal timing, costs, walk-forward behavior,
selection bias, and receipts.

**Evidence class:** Test-verified for many components; independence is structurally
represented but not statistically characterized.

### Assessment

**Strengths.** Verification is a pipeline stage, not an afterthought. Negative and
invalid outcomes are valid terminal research products.

**Weaknesses.** Full suites have been expensive and late. Producer/reviewer semantic
mismatches repeatedly reject work that deterministic preflight could catch. Two model
roles may not be genuinely independent if they share training, prompts, or evidence.

**Failure modes.** Test gaps at repository seams, flaky integration tests, review
rubber-stamping, evaluator drift, and a passing implementation that answers a
different hypothesis than the card.

**Debt and missing capability.** Contract fixtures should be shared across the control
plane and Bulletproof. Reviewer disagreement and calibration should be measured.

### Alternatives and recommendation

Build a verification pyramid: schema/preflight first, focused semantic fixtures
second, native full validation third, independent review fourth, and prospective
shadow evidence last. Reserve expensive model review for artifacts that pass the
deterministic layers.

**Expected benefit:** fewer wasted tokens and more informative failures.
**Difficulty:** medium. **Prerequisites:** test design, mutation testing, causal
inference, and evaluator calibration.

**Validation experiment:** replay 50 accepted and rejected strategies through each
layer. Measure earliest correct rejection, false acceptance, reviewer disagreement,
cost, and time to terminal classification.

## 14. Security and permissions

### Current architecture and evidence

Workload identities, scopes, charters, grants, approval digests, risk levels, and
capital/order-authority flags constrain action. Demo and live credentials are intended
to be isolated from general research roles.

**Evidence class:** Source- and test-verified for core authority logic;
runtime-evidenced for low-risk approval paths; credential posture on offline VPS hosts
was not inspected.

### Assessment

**Strengths.** Authority is explicit and often fail-closed. Plan digests protect
approval meaning. Scientific success does not itself confer capital authority.

**Weaknesses.** Temporary sudo and founder delegations have been operationally
necessary. Role and host sprawl make revocation and least-privilege review difficult.
External web content introduces model prompt-injection risk.

**Failure modes.** Stale grants, confused deputy behavior, credentials in logs,
approval replay, supply-chain compromise, prompt injection causing tool misuse, and
research infrastructure reaching execution authority.

**Debt and missing capability.** Continuous entitlement review, signed deployment
attestation, secret-use telemetry, and adversarial model-tool testing need stronger
evidence.

### Alternatives and recommendation

Retain capability scopes and add short-lived workload credentials, policy-as-code
tests, deployment provenance, and explicit data-flow isolation between untrusted
content and privileged tools. Human approval remains mandatory for capital changes.

**Expected benefit:** smaller blast radius and auditable delegation.
**Difficulty:** high. **Prerequisites:** threat modeling, PKI, secrets management,
OAuth/workload identity, and LLM security.

**Validation experiment:** run a red-team suite covering approval replay, stale grant,
malicious document, compromised worker, and secret exfiltration attempts. Any capital
or credential boundary crossing is a hard failure.

## 15. Human oversight and autonomy boundaries

### Current architecture and evidence

Risk-zero and bounded research can operate under mandates and delegated authority;
new code, expanded data access, shadow admission, and capital actions require stronger
approval. Mission Control and Telegram expose review paths.

**Evidence class:** Runtime-evidenced for approvals and mandate-driven work; not yet
recovery-evidenced as a uniformly frictionless process.

### Assessment

**Strengths.** Autonomy is conditional rather than absolute. Approval binds a specific
plan. Pause/drain semantics recognize the difference between stopping intake and
aborting in-flight work.

**Weaknesses.** Approval expiry and duplicate notifications have caused stalls.
Founder delegation can become an operational workaround rather than a deliberate
policy. The boundary between authoring a bounded strategy and changing platform code
has historically been unclear.

**Failure modes.** Approval fatigue, silent queue blockage, old consent applied to new
work, emergency bypass becoming normal, and operators unable to tell what will stop
under pause.

**Debt and missing capability.** Authority simulation and plain-language previews of
effective consequences should precede approval.

### Alternatives and recommendation

Use autonomy tiers tied to effect, not component name. Permit deterministic
materialization inside a founder-approved research mandate; require fresh approval for
new executable logic, authority expansion, shadow admission, and capital. Make every
approval renewable from Mission Control without recreating the task.

**Expected benefit:** less friction without weakening consequential gates.
**Difficulty:** medium. **Prerequisites:** authorization models, human factors, and
state-machine design.

**Validation experiment:** run a week-long paper-only campaign and measure approvals,
avoidable stalls, expired links, interventions, and any action whose effective scope
exceeded its displayed preview.

## 16. Resource allocation, latency, and cost

### Current architecture and evidence

Bulletproof has a global capacity scheduler and the control plane has capacity
directors/executors. Backtests use bounded parameter grids and host memory constraints.
LLM use occurs in research synthesis, engineering, review, and conversation.

**Evidence class:** Source-verified and partially runtime-evidenced; complete per-task
model and infrastructure cost attribution is missing.

### Assessment

**Strengths.** Compute limits and eight-variant experiments are explicit. The platform
can separate authoring from native numerical execution.

**Weaknesses.** “Never idle” can maximize waste rather than information gain. Failed
engineering has consumed model tokens before deterministic contradictions were found.
Parallelism goals have sometimes exceeded reliable work supply or memory.

**Failure modes.** RAM exhaustion, duplicate expensive reasoning, starvation of short
high-value tasks, unlimited retry cost, and background work degrading interactive
control.

**Debt and missing capability.** Cost, expected information gain, confidence, queue
age, and failure likelihood are not combined in scheduling policy.

### Alternatives and recommendation

Schedule for **value of information per constrained resource**, not utilization alone.
Reserve host headroom, enforce per-stage budgets, cache content-addressed reasoning,
and stop repeated failure classes with a circuit breaker.

**Expected benefit:** lower spend and higher useful throughput. **Difficulty:**
medium-high. **Prerequisites:** scheduling, queueing theory, Bayesian decision theory,
and cost accounting.

**Validation experiment:** compare FIFO, utilization-maximizing, and information-value
schedulers over a replayed month of tasks. Measure verified terminals per dollar and
CPU-hour, interactive latency, memory pressure, and repeated failure rate.

## 17. Scalability and maintainability

### Current architecture and evidence

Subsystems are separated into control plane, backtesting laboratory, product SaaS,
Bible, and auxiliary deployment/profile repositories. Typed APIs and schemas connect
them, but branches and deployed revisions have drifted.

**Evidence class:** Source-verified for boundaries; runtime-evidenced for version
drift.

### Assessment

**Strengths.** Domain boundaries are meaningful. The Bible provides explicit concept
ownership. Components can evolve independently.

**Weaknesses.** Cross-repository changes require manual coordination. Similar concepts
have multiple schemas. Deployment state is not always reproducible from Git alone.

**Failure modes.** Contract mismatch, incompatible revisions, partial rollout,
orphaned migrations, documentation drift, and an increasing number of repair scripts.

**Debt and missing capability.** A versioned cross-repository compatibility matrix and
release train are absent.

### Alternatives and recommendation

Do not merge all repositories. Publish shared contracts as versioned packages, test
consumer/producer compatibility in CI, and produce a signed release manifest that
binds repository commits, migrations, packages, and host deployments.

**Expected benefit:** independent evolution without guesswork. **Difficulty:** high.
**Prerequisites:** semantic versioning, package design, contract testing, and release
engineering.

**Validation experiment:** deploy a complete test environment only from a release
manifest and run a representative campaign. No manual source copy or unrecorded patch
is allowed.

## 18. Research reproducibility and scientific validity

### Current architecture and evidence

Hypothesis cards, point-in-time data binding, immutable strategy specs, bounded grids,
walk-forward tests, realistic costs, stress, selection-bias review, negative-result
retention, independent review, and BT-009 receipts form the scientific path.

**Evidence class:** Runtime-evidenced for several terminal negative experiments;
scientific coverage across the broader universe remains partial.

### Assessment

**Strengths.** The platform treats falsification and negative outcomes as progress.
The backtester separates native artifacts from institutional publication. Causal
timing and point-in-time validity are explicit gates.

**Weaknesses.** A card and implementation can disagree on target horizon or exit
semantics. Strategy engineering remains a high-failure translation boundary. Repeated
hypothesis generation can create an untracked multiple-testing burden.

**Failure modes.** Leakage, survivorship bias, selection over many uncounted attempts,
cost underestimation, implementation drift, inadequate trade count, and promotion
based on one favorable slice.

**Debt and missing capability.** Experiment-family accounting, preregistration lineage,
and full attempt denominators should be first-class.

### Alternatives and recommendation

Compile a typed `StrategyIntent` into deterministic scaffolding, require semantic
equivalence tests between card and strategy, and track every tested family in an
experiment registry. Models implement only unresolved signal logic.

**Expected benefit:** fewer invalid experiments and honest selection accounting.
**Difficulty:** high. **Prerequisites:** experimental design, causal inference,
statistical testing, and DSL/compiler construction.

**Validation experiment:** take 20 historical cards, independently encode expected
timing and outcomes, compile them, and mutation-test the generated strategies. Any
mutation that changes horizon, information set, or target must be detected before a
full backtest.

## 19. Trading-specific risk isolation and execution safeguards

### Current architecture and evidence

Risk schemas, dynamic budgets, candidate admission, deterministic risk, OMS
idempotency, reconciliation, freeze/kill/recovery, venue adapters, demo certification,
and execution telemetry are represented. Demo receipts do not confer live authority.

**Evidence class:** Runtime-evidenced for bounded pilots and demo publication;
current live readiness and VPS credential posture are unknown.

### Assessment

**Strengths.** Research, admission, portfolio, risk, execution, and venue authority are
separate. Idempotency and reconciliation are explicit. Kill and recovery are treated
as workflows, not buttons alone.

**Weaknesses.** Much evidence is pilot-scale. Offline execution nodes prevent current
certification. Master-account usage increases blast radius. Live venue constraints can
change independently of deployed code.

**Failure modes.** Duplicate order, stale instrument rule, incorrect balance scope,
position divergence, partial-fill mishandling, kill that cannot flatten, network
partition, and risk state not restored after restart.

**Debt and missing capability.** Continuous adapter conformance, independent position
reconciliation, and environment-specific live canary evidence remain necessary.

### Alternatives and recommendation

Keep capital disabled. Restore an isolated execution host and dedicated restricted
account before any live canary. Certify every order lifecycle, dynamic venue rule,
restart, disconnect, and kill behavior in demo with external reconciliation.

**Expected benefit:** contained operational risk. **Difficulty:** very high.
**Prerequisites:** market microstructure, OMS design, venue APIs, risk systems,
networking, and incident command.

**Validation experiment:** a fault-injected demo certification covering submit,
amend, partial fill, cancel, rejection, disconnect, stale market data, duplicate
command, restart, reconciliation, freeze, kill, and immediate flatten. Profitability
is explicitly out of scope.

## 20. Prioritized improvement portfolio

Priorities are qualitative and ordered by reliability gain, learning value,
architectural leverage, effort, and operational risk.

| Priority | Improvement | Why now | Difficulty | Operational risk | Learning value | Proof of completion |
|---|---|---|---|---|---|---|
| 1 | Canonical lifecycle projection and transition ownership | Removes misleading state and duplicated control | High | Medium | Very high | Replay and fault tests converge to one lifecycle view |
| 2 | Cross-repository contracts and release manifest | Repeated failures originate at repository/runtime seams | High | Medium | Very high | Clean environment deploys and runs from one manifest |
| 3 | Typed `StrategyIntent` compiler and semantic equivalence tests | Strategy engineering is the dominant scientific bottleneck | High | Low while offline | Very high | Mutations are rejected before full backtest |
| 4 | Verification pyramid and failure circuit breaker | Reduces expensive repeated model failures | Medium | Low | High | Earlier correct rejection and lower terminal cost |
| 5 | Scientific trace and honest Mission Control metrics | Operators need evidence-qualified progress | Medium | Low | High | Every count resolves to qualifying records |
| 6 | Context-selection and provenance evaluation | RI-015 quality cannot be inferred from architecture | Medium | Low | High | Gold-set retrieval and supported-answer benchmark |
| 7 | Agent capability contracts and simplification experiments | Tests whether specialization earns its complexity | Medium | Low | Very high | Multi-agent path beats named baselines or is retired |
| 8 | Distributed recovery game day | Core hosts work, but system-wide recovery is unproved | Medium-high | Medium in staging | Very high | Published RPO/RTO and bounded convergence evidence |
| 9 | Value-of-information scheduler and cost attribution | “Never idle” should not mean “always spending” | Medium-high | Low | High | More verified terminals per constrained resource |
| 10 | Demo execution recertification on isolated host | Required before considering any capital canary | Very high | High | High | Complete environment-specific certification receipt |

## 21. Architectural conclusions

1. The control plane should remain deterministic at authority and lifecycle
   boundaries. Models should propose scientific content, not invent permissions or
   state semantics.
2. Multi-agent design is justified only for measured specialization, independence,
   information separation, or parallelism. Otherwise a function or single bounded
   agent is preferable.
3. The platform already has valuable scientific rigor. Its next advance is to make
   translation between research intent, executable strategy, and terminal evidence
   reliably machine-checkable.
4. Observability must distinguish activity, task success, native execution, terminal
   scientific receipt, shadow admission, and capital authority.
5. Durable autonomy is demonstrated by bounded recovery from failure, not by a daemon
   running continuously.
6. No architectural result in this assessment supports a claim of profitable alpha
   or live-trading readiness.

Phase 3 should use these findings to teach the exact concepts needed to understand,
challenge, and eventually redesign the system rather than offering a generic computer
science curriculum.
