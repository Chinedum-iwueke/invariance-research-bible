# Two-Year Agentic Systems Mastery Roadmap

**Cadence:** approximately 15 focused hours per week<br>
**Starting point:** a functioning but uneven distributed Invariance Research system<br>
**Method:** the [living systems laboratory](living-systems-laboratory.md)<br>
**Progress rule:** mastery criteria, not elapsed time, unlock the next responsibility.

## Weekly operating rhythm

| Activity | Typical hours | Purpose |
|---|---:|---|
| Theory and source reading | 4 | Build transferable mental models |
| Repository archaeology | 3 | Connect theory to the actual system |
| Implementation or experiment | 5 | Produce independent engineering evidence |
| Testing, measurement, reflection | 2 | Learn from outcomes rather than output volume |
| Oral or written design defense | 1 | Expose shallow understanding |

Incident response can interrupt the rhythm, but the incident becomes a documented
case study afterward. The roadmap does not authorize live trading.

## Year 1: Core architecture and implementation mastery

### Stage 1: Architectural literacy

**Schedule:** Months 1-2, about 120 hours<br>
**Target:** Independently explain the current system, its boundaries, data and control
flow, canonical state, and failure modes.

#### Learning objectives

- Read unfamiliar Python, SQL, configuration, and TypeScript methodically.
- Distinguish source, test, deployment, runtime, and recovery evidence.
- Explain the roles of control plane, Bulletproof, SaaS, Bible, and machine topology.
- Trace one task and one scientific result end to end.
- Identify deterministic workflow, model reasoning, and human authority boundaries.

#### Repository components

- Phase 1 reconnaissance and Book XI workflow maps
- `Task`, `build_task`, `lease_next_task`, and `reap_expired_leases`
- Alpha discovery and campaign reconcilers
- Worker daemon/service and one executor
- Bulletproof registered strategy runner and receipt publication
- Mission Control projection for the same task

#### Required theory

Call graphs, HTTP, relational data models, transactions, finite-state machines,
process supervision, Git, and evidence/provenance basics.

#### Exercises

1. Complete Diagnostics 1 and 8.
2. Recreate the system architecture diagram from memory and reconcile differences.
3. Query an isolated database fixture to reconstruct a task timeline.
4. Explain one systemd service and one Docker service from configuration to health.

#### Improvement opportunity

Draft the canonical transition-ownership table; do not implement it until reviewed.

#### Experiment

Ask two engineers to reconstruct the same task using current telemetry. Measure
agreement, missing links, and time. This establishes an observability baseline.

#### Deliverables

- Annotated end-to-end trace
- State dictionary and transition-ownership draft
- Evidence-bound subsystem briefing
- First learning-journal entries

#### Dependencies

Basic Python and command-line familiarity. Remediate Domain A concurrently if needed.

#### Mastery criteria

Without notes, explain the system for thirty minutes, answer the five diagnostic
architecture questions, locate supporting code, and predict three failure outcomes
with at least four of five predictions confirmed by tests or evidence.

### Stage 2: Individual agent mastery

**Schedule:** Months 3-4, about 120 hours<br>
**Target:** Design, implement, test, and debug one agent execution loop without an
agent framework.

#### Learning objectives

- Understand model inference, context, structured output, tools, state, and budget.
- Separate prompt policy from executable policy and authority.
- Define termination, retry, and recovery.
- Justify agency against a deterministic function.
- Evaluate supported claims, latency, and cost.

#### Repository components

- `WorkerDaemon.run` and `WorkerService.run_once`
- One research role package and executor
- Context-pack construction and evidence retrieval
- Workload identities, charters, and grants
- `EngineeringMissionExecutor` as a high-complexity comparison

#### Required theory

Transformers at inference level, structured outputs, retrieval, tool calling,
statecharts, capability security, and test doubles.

#### Exercises

1. Complete Diagnostics 3 and 4.
2. Implement a framework-free source-question agent with three read-only tools.
3. Add prompt-injection, unavailable-source, malformed-output, and budget tests.
4. Replace the agent with a deterministic baseline for answerable metadata questions.

#### Improvement opportunity

Draft and validate `AgentCapabilityContract` against three actual roles.

#### Experiment

Compare deterministic and agent versions on a preregistered 50-task set. Do not
retain the agent if it fails to add measured value.

#### Deliverables

- Agent loop, typed tools, and test suite
- Capability contracts
- Evaluation report with cost and failure taxonomy
- Design defense

#### Dependencies

Stage 1, software foundations, and AI foundations.

#### Mastery criteria

Implement the loop independently, diagnose injected failures, explain every context
field and permission, and defend or reject the agent using experimental results.

### Stage 3: Orchestration mastery

**Schedule:** Months 5-6, about 120 hours<br>
**Target:** Design task graphs, scheduling, delegation, coordination, and recovery.

#### Learning objectives

- Model workflows as state machines and directed acyclic graphs where appropriate.
- Understand centralized orchestration, choreography, hierarchy, and blackboards.
- Compile proposed plans into deterministic tasks.
- Control concurrency, dependencies, backpressure, and duplicate work.
- Measure coordination overhead and reviewer independence.

#### Repository components

- Task graphs, alpha discovery, alpha campaign, review routing
- Capacity director and Bulletproof capacity scheduler
- Mandates, approvals, and pause/drain state
- Conversation materialization boundary

#### Required theory

Graph algorithms, scheduling, queues, state machines, multi-agent coordination,
transactions, and experiment design.

#### Exercises

1. Complete Diagnostic 9.
2. Specify a typed `ResearchPlan` and deterministic task-graph compiler in a toy
   namespace.
3. Property-test idempotent graph materialization.
4. Measure duplicate work and message volume in a multi-agent fixture.

#### Improvement opportunity

Prototype the transition-ownership table and plan compiler behind no-production
fixtures.

#### Experiment

Run deterministic, single-agent, centralized multi-agent, and current hybrid paths on
the same planning tasks under fixed model and tool budgets.

#### Deliverables

- Orchestration design with sequence/state diagrams
- Compiler prototype and property tests
- Controlled comparison report
- ADR proposed by the founder

#### Dependencies

Stages 1-2 and domains D, E, H, and I.

#### Mastery criteria

Given a new workflow, select and defend an orchestration style, specify state and
failure semantics, implement a bounded prototype, and explain why a simpler design is
or is not sufficient.

### Stage 4: Distributed autonomous systems

**Schedule:** Months 7-9, about 180 hours<br>
**Target:** Implement durable execution, event-driven integration, observability, and
fault recovery across processes.

#### Learning objectives

- Reason about partial failure and at-least-once delivery.
- Implement leases, idempotency, outbox, reconciliation, and backpressure.
- Version cross-repository contracts and release manifests.
- Build end-to-end traces without confusing telemetry with canonical evidence.
- Conduct a safe fault-injection game day.

#### Repository components

- PostgreSQL task and evidence persistence
- Cross-repository alpha publication
- VM1/VM2 service topology and deployment scripts
- Mission Control trace projections
- OMS and reconciliation patterns as a consequential reference

#### Required theory

Distributed systems, databases, networking, Linux, observability, release engineering,
and threat modeling.

#### Exercises

1. Complete Diagnostics 2, 6, and 10.
2. Build a transactional outbox prototype.
3. Publish a versioned compatibility fixture consumed by two repositories.
4. Instrument a staging trace from request through terminal receipt.

#### Improvement opportunity

Create a release-manifest prototype and canonical transition journal in staging.

#### Experiment

Kill workers, restart the API, delay a dependency, and duplicate delivery. Compare
predicted with actual state and measure bounded convergence.

#### Deliverables

- Durable workflow implementation
- Cross-repository compatibility suite
- Game-day report and postmortem
- Release and rollback runbook

#### Dependencies

Stages 1-3 and strong Domains A, E, G, and H.

#### Mastery criteria

Deploy the staging workflow from an immutable manifest, recover it within declared
objectives, preserve invariants, and defend all consistency choices.

### Stage 5: Advanced autonomous intelligence, foundation

**Schedule:** Months 10-12, about 180 hours<br>
**Target:** Reason about uncertainty, feedback, adaptive allocation, and scientific
evaluation without prematurely deploying RL.

#### Learning objectives

- Frame discovery and scheduling as constrained decision problems.
- Use confidence and value of information without turning estimates into truth.
- Design offline bandit and control simulations.
- Separate platform reward from trading return.
- Build reproducible architecture benchmarks.

#### Repository components

- Question and capacity schedulers
- Research mandates and novelty/failure feedback
- Scientific receipt and selection-accounting data
- Planned ML/RL boundaries in Books VI and XI

#### Required theory

Probability, statistics, optimization, control theory, bandits, introductory RL,
causal inference, and benchmark methodology.

#### Exercises

1. Complete Diagnostics 5 and the value-of-information exercise in the knowledge map.
2. Implement FIFO, heuristic, and contextual-bandit schedulers in simulation.
3. Define safe abstention and deterministic fallback.
4. Audit reward proxies for Goodhart's law.

#### Improvement opportunity

Propose a scheduler evaluation using immutable historical tasks without activating it
in production.

#### Experiment

Compare schedulers on verified scientific terminals per cost and CPU-hour while
constraining retries, latency, and task diversity.

#### Deliverables

- Decision-problem specification
- Offline simulator and benchmark
- Safety and reward-misspecification analysis
- Year-one architecture defense

#### Dependencies

Stages 1-4 and mathematics prerequisites.

#### Mastery criteria

Independently formulate, implement, and critique an adaptive policy; show when a
deterministic heuristic wins; and refuse online deployment when offline evidence or
safety coverage is insufficient.

## Year 1 capstone

Produce a complete architectural defense of one Invariance Research workflow:

1. reconstruct its current implementation;
2. identify a falsifiable architectural weakness;
3. compare at least two designs and a simple baseline;
4. implement a staging prototype;
5. fault-test and measure it;
6. publish an ADR and reproducible report; and
7. explain the result orally without model assistance.

Passing requires correct boundaries, reproducible evidence, explicit uncertainty, and
no unsupported trading claim.

## Year 2: Advanced research trajectory

### Stage 5 continued: Adaptive systems under constraints

**Schedule:** Months 13-15, about 180 hours

#### Objectives

- Study sequential decision-making, uncertainty calibration, and constrained control.
- Create offline policy-evaluation datasets from immutable execution traces.
- Understand non-stationarity and why historical orchestration policy success may not
  transfer.

#### Work

- Build an offline scheduler policy evaluator.
- Compare calibrated and uncalibrated task-value estimates.
- Investigate safe exploration with hard resource and authority constraints.
- Reproduce one foundational bandit or RL result before using its method.

#### Mastery criteria

Defend estimator assumptions, identify off-policy evaluation failure, and build a
fallback that remains correct when the learned policy is unavailable.

### Stage 6A: Original orchestration architecture

**Schedule:** Months 16-18, about 180 hours

#### Objectives

- Form an original but bounded research question relevant to Invariance Research.
- Derive it from measured platform limitations rather than fashion.
- Design reproducible baselines and ablations.

#### Candidate questions

- Can transition-ownership contracts reduce recovery ambiguity versus current hybrid
  reconciliation?
- Does a capability-aware planner improve verified completion over static routing?
- When does independent multi-agent review reduce false acceptance enough to justify
  its cost?
- Can execution traces improve failure-aware planning without leaking outcome labels?

#### Work and deliverables

- Literature review and problem statement
- Preregistered protocol
- Reference implementation and at least two baselines
- Evaluation dataset with provenance
- Threat and failure analysis

#### Mastery criteria

Survive adversarial design review and show that the question is both novel enough to
matter and narrow enough to test.

### Stage 6B: Experimental implementation

**Schedule:** Months 19-21, about 180 hours

#### Objectives

- Implement the proposed architecture in an isolated environment.
- Measure reliability, quality, latency, cost, and complexity.
- Run ablations and fault injection.

#### Work

- Freeze evaluation protocol before final runs.
- Maintain complete environment and artifact manifests.
- Run deterministic and single-agent baselines.
- Analyze negative and contradictory results.

#### Mastery criteria

Another engineer can reproduce the main result from the repository and report. The
conclusion remains valid if the proposed architecture loses.

### Stage 6C: Defense, integration, and teaching

**Schedule:** Months 22-24, about 180 hours

#### Objectives

- Defend the work as an architecture decision and a research result.
- Decide whether production integration is warranted.
- Teach the design and its limitations.

#### Work and deliverables

- Research report suitable for an engineering venue or master's project
- Reproducibility package
- Production-readiness and rollback assessment
- Public-style technical talk and internal workshop
- Final ADR: adopt, revise, or reject

#### Mastery criteria

Explain and defend the system before critical reviewers; answer counterexamples;
distinguish evidence from inference; and make the correct decision even if that means
not deploying the original design.

## Progress governance

### Monthly review

- Demonstrated concepts and retained artifacts
- Incorrect predictions and revised mental models
- Model assistance used and why
- Reliability or comprehension metrics moved
- Next month's design responsibility

### Quarterly review

- One oral architecture defense
- One reproducible experiment or fault drill
- One source-to-runtime trace
- One simplification candidate
- Assistance-ladder decision from ADR-0006

### Adjustment policy

The roadmap may change after diagnostics. It may not be compressed merely to maximize
feature throughput. Urgent production work can be performed directly, but must receive
a retrospective lesson, state trace, and durable corrective-action review.
