# Comparative Agentic Architecture Benchmark

## 1. Research objective

Determine when, if ever, multi-agent orchestration improves verified completion,
evidence quality, recovery, or cost over simpler designs on tasks representative of
Invariance Research.

The benchmark evaluates software and research workflow quality. It does not evaluate
future market profitability.

## 2. Architecture arms

### A. Deterministic workflow

Typed code, fixed rules, and validators execute the task. No model chooses actions.
Use this arm wherever the task has enumerable transformations or policy.

### B. Single-agent execution

One model-driven agent receives the same admissible context and typed tools. It may
plan and use tools within a fixed budget. Deterministic authority and validation remain
outside the model.

### C. Centralized multi-agent orchestration

One orchestrator decomposes and routes work to specialist agents, receives their
results, and selects the next action. Specialists do not independently change the
global task graph.

### D. Hierarchical orchestration

A director delegates subobjectives to subordinate coordinators or specialists. Each
level has explicit authority, context, and termination contracts.

### E. Event-driven orchestration

Independent components react to typed immutable events and shared durable state.
There is no model with global control; a deterministic lifecycle owner resolves state.

## 3. Task suites

### Suite 1: Evidence retrieval and answer support

Tasks require locating canonical sources, constructing bounded context, answering a
question, and citing support. Gold evidence and acceptable abstentions are curated.

### Suite 2: Research-question qualification

Inputs mix falsifiable predictive questions, vague topics, instructions, duplicates,
unavailable-data questions, and equation-dependent proposals. The output is a typed
qualification and rationale.

### Suite 3: Strategy-intent materialization

Qualified cards are converted into typed `StrategyIntent`, deterministic scaffold,
unresolved signal implementation, tests, and an artifact manifest. Fixtures include
timing and target traps.

### Suite 4: Independent scientific review

Reviewers classify valid and defective artifacts. Defects include leakage, horizon
mismatch, unbounded variants, cost omissions, data unavailability, and incomplete
logging.

### Suite 5: Durable task recovery

Workflows face duplicate delivery, delayed result, worker death, service restart,
unavailable capability, and partial publication.

### Suite 6: Incident diagnosis

Given controlled telemetry and repository evidence, the architecture must identify
root cause, contain effects, and propose a durable corrective action.

### Suite 7: Scheduling under constraint

A mixed queue contains short/long tasks, uncertain value, capability constraints,
memory demands, retry histories, and interactive latency requirements.

## 4. Dataset design

Each suite contains development and sealed evaluation partitions. Items are stratified
by difficulty and independently reviewed. Historical incidents may be included only
after removing secrets and preventing evaluation leakage.

Each item binds:

- input and source digests;
- expected evidence or invariant;
- allowed tools and authority;
- maximum model and compute budget;
- completion and failure criteria;
- adjudication method; and
- known ambiguity.

At least 20% of items should require abstention or rejection so that indiscriminate
action is penalized.

## 5. Controlled variables

Across comparable model-driven arms, hold constant:

- model and exact version;
- prompt-information content, allowing role formatting only when documented;
- total input/output token budget;
- tool implementations and data access;
- wall-clock and retry budget;
- repository and dependency versions;
- CPU, memory, and network envelope;
- evaluation dataset and run order randomization; and
- approval policy and authority.

When an architecture inherently adds calls, report both fixed-total-budget and
architecture-native-budget results.

## 6. Primary outcomes

1. Verified task completion rate.
2. Unsupported material claim or false-acceptance rate.
3. Recovery invariant violations.
4. Total attributable cost per verified terminal.
5. End-to-end latency distribution.

## 7. Secondary outcomes

- human intervention;
- duplicate work;
- message and context volume;
- coordination overhead;
- tool-call errors;
- appropriate abstention;
- evidence and provenance completeness;
- reviewer disagreement;
- reproducibility; and
- operator comprehension of the resulting trace.

## 8. Hypotheses

The null hypothesis for every suite is that the more complex architecture does not
improve the primary outcomes enough to justify its operational cost.

Examples:

- Specialized agents improve evidence coverage on heterogeneous research tasks but
  not deterministic qualification tasks.
- Independent reviewers reduce false acceptance only when their context and model
  errors are sufficiently decorrelated.
- Event-driven orchestration improves interruption recovery but increases diagnosis
  time without a canonical lifecycle projection.
- Hierarchy helps long decomposable tasks but adds harmful overhead to short tasks.

## 9. Execution protocol

1. Preregister dataset, arms, budgets, primary outcomes, exclusions, and stop rules.
2. Validate deterministic evaluators and manually audit a sample.
3. Run a small pilot used only to repair the harness.
4. Freeze prompts, tools, and evaluation code.
5. Randomize item order and execute repeated runs where model variance matters.
6. Retain every attempt, including timeouts and invalid outputs.
7. Blind adjudicators to architecture arm where feasible.
8. Report effect sizes and uncertainty, not only significance.
9. Reproduce a sample on a clean environment.
10. Decide retain, simplify, revise, or reject for each complex architecture.

## 10. Failure criteria

An arm fails regardless of average performance if it:

- crosses an authority boundary;
- produces duplicate authoritative terminal effects;
- conceals or discards invalid/failed work;
- cannot reproduce deterministic fixtures;
- uses prohibited future or unavailable evidence;
- exceeds the preregistered resource budget without stopping; or
- cannot expose an attributable execution trace.

## 11. Analysis

Report results by suite, difficulty, task type, failure class, and architecture. Avoid
pooling tasks whose completion predicates differ. Use paired analysis where every arm
receives the same item. Report confidence intervals and practical effect thresholds.

Model-judge assessments require calibration against blinded expert labels and must
report disagreement. They cannot be the sole evaluator of authority, state
consistency, causal timing, or executable correctness.

## 12. Reproducibility package

- dataset manifest and licensing/provenance;
- architecture and environment manifests;
- prompts, tool schemas, and budgets;
- model identifiers and inference parameters;
- random seeds where effective;
- raw traces and normalized metrics;
- evaluator code and calibration;
- exclusions and anomalies;
- statistical analysis; and
- signed result digest.

## 13. Decision rules

Complexity is adopted only if it yields a preregistered material improvement without
violating hard constraints. A mixed result may justify task-sensitive routing rather
than one universal architecture. A negative result should simplify the system.
