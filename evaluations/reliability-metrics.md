# Reliability and Evidence Metrics

## 1. Measurement principles

1. A metric names its population, qualifying event, clock, exclusions, and owner.
2. Every dashboard value resolves to the underlying records.
3. Preparation success, native execution, scientific terminal outcome, shadow
   admission, and capital authority are different events.
4. Retries and duplicates do not inflate unique-work denominators.
5. Latency is reported as a distribution, not an average alone.
6. Cost includes model, compute, storage, and attributable human intervention.
7. Missing telemetry is reported as unknown, not zero.

## 2. Canonical measurement envelope

Every measured work item should be joinable through:

| Field | Meaning |
|---|---|
| `objective_id` | Founder request, mandate objective, or benchmark item |
| `plan_id` / `plan_digest` | Immutable approved or benchmarked plan |
| `task_id` | Durable unit of work |
| `attempt_id` | One execution attempt |
| `agent_id` | Accountable runtime identity |
| `campaign_id` | Scientific campaign when applicable |
| `native_run_id` | Bulletproof or other native executor run |
| `receipt_id` | Terminal evidence object when produced |
| `trace_id` | Operational correlation across services |
| `environment_manifest_digest` | Bound software/data/runtime environment |

## 3. Core platform metrics

### Verified task completion rate

```text
tasks with accepted terminal evidence / eligible unique tasks
```

The acceptance predicate is task-type-specific and versioned. A process exit code or
task `succeeded` status alone is insufficient where artifacts or review are required.

### Autonomous completion rate

```text
verified tasks completed without unplanned human intervention / eligible verified tasks
```

Scheduled mandate approval and preregistered policy are planned governance, not
intervention. Manual repair, requeue, schema patch, credential repair, or reasoning
correction is intervention.

### Human intervention frequency

Report interventions per 100 eligible tasks, by category:

- scientific decision;
- authority approval;
- runtime repair;
- data correction;
- semantic correction;
- retry/requeue; and
- incident containment.

Approval required by policy is shown separately from intervention caused by failure.

### Tool failure recovery rate

```text
recoverable tool failures reaching correct bounded terminal state / recoverable tool failures
```

Also report median and percentile attempts to recovery. Repeating the same error until
budget exhaustion is not recovery.

### Orchestration overhead

Report both time and resources:

```text
coordination wall time / end-to-end wall time
coordination compute and model cost / total attributable cost
```

Coordination includes planning, routing, waiting on avoidable dependency serialization,
message processing, and reconciliation; it excludes domain execution.

### Task latency

Measure submit-to-terminal, eligible-to-lease, lease-to-start, execution, review,
publication, and reconciliation latency. Report p50, p90, p95, p99, maximum, and
censored unfinished work by task type.

### Model and infrastructure cost

Report model input/output/cache tokens and currency, CPU-seconds, peak/reserved memory,
GPU-seconds if any, storage, egress, and human minutes. Attribute retries and rejected
work to failure class.

### Agent utilization

```text
productive execution time / available scheduled time
```

Show waiting-for-work, waiting-for-dependency, waiting-for-approval, failed preflight,
and repeated-failure time separately. High utilization is not inherently desirable.

### Duplicate work rate

```text
semantically duplicate attempts not required by protocol / unique intended attempts
```

Use task identity, content digests, hypothesis family, data window, and parameter
contract rather than title equality alone.

### State consistency

For each sampled objective, compare task, campaign, native run, receipt, and projection.
Report inconsistent objects per 1,000 joins, time to convergence, and unresolved
conflict type.

### Error propagation

Track the number of downstream materializations, decisions, or displays influenced by
an invalid upstream artifact before containment. Include maximum propagation depth and
time to quarantine.

### Security violations

Count denied and successful policy violations separately. Categories include scope,
approval, secret access, tool boundary, content injection, data exfiltration, package
provenance, and capital/order authority. A successful violation is a severity event,
not merely a dashboard count.

### Reproducibility

```text
terminal results reproduced within declared equivalence / eligible terminal results attempted
```

Equivalence must name allowed numerical tolerance, artifacts, data digest, environment,
and code revision. Report failures by source: data, environment, nondeterminism, code,
or missing artifact.

### Recovery after interruption

Report recovery point objective, recovery time objective, observed data loss, duplicate
effects, orphaned work, manual actions, and time to trustworthy projection after worker,
API, database, network, and host interruption.

## 4. Research-workflow metrics

### Evidence quality

- proportion of material claims linked to available canonical evidence;
- direct-source versus derived-source ratio;
- source-version ambiguity rate;
- unsupported material claim rate;
- equation/table objects with qualified fidelity;
- external-content trust and injection disposition.

### Provenance completeness

```text
artifacts with resolvable source, transform, producer, version, and digest / sampled artifacts
```

### Experimental validity

Report the proportion of experiments passing, failing, or unknown for:

- preregistration completeness;
- point-in-time data and universe;
- causal feature timing;
- target/strategy semantic equivalence;
- bounded variant accounting;
- OOS and walk-forward evaluation;
- realistic costs and stress;
- selection-bias accounting;
- trade-count sufficiency;
- independent review; and
- exact replay.

### Conclusion support

An independent evaluator classifies each conclusion as supported, overstated,
contradicted, or unverifiable from its retained evidence. Report disagreement and
adjudication; do not silently overwrite the initial conclusion.

### Negative-result retention

```text
negative, invalid, and failed terminal attempts retained with searchable cause / all such attempts
```

Also measure whether later novelty checks actually retrieve relevant prior failures.

### Scientific throughput

Report separately:

- questions generated and rejected;
- cards qualified;
- strategies compiled;
- native experiments started;
- terminal positive, negative, invalid, and failed receipts;
- independently reproduced results; and
- candidates admitted to shadow.

Never aggregate these into “backtests completed.”

## 5. Trading execution metrics

Trading metrics apply only in a separately authorized demo or live environment.

### Operational correctness

- accepted commands mapped to exactly one intended venue action;
- duplicate command suppression;
- amend/cancel correctness;
- partial-fill accounting;
- order, fill, position, and balance reconciliation;
- restart recovery;
- stale-data abstention; and
- dynamic instrument-rule compliance.

### Authorization correctness

Report attempted and successful actions outside account, symbol, notional, order type,
environment, or capital scopes. Any successful unauthorized effect is a hard failure.

### Risk-control correctness

Measure pre-trade denial, exposure calculation, budget enforcement, freeze/kill
latency, flatten correctness, stale-state behavior, and recovery before re-enable.

### Execution integrity

Report venue acknowledgements, rejects, fill quality against contemporaneous reference,
latency distributions, disconnect gaps, missing events, reconciliation corrections,
and unhedged exposure duration.

These metrics assess execution behavior. They do not claim that the strategy is
profitable.

## 6. Metric anti-patterns

- Counting task successes as native experiments.
- Treating zero reported failures as reliability when telemetry is absent.
- Maximizing agent utilization or queue depth as an objective.
- Comparing architectures with different models, tools, or budgets.
- Reporting only averages for long-tailed latency.
- Dropping invalid and failed experiments from selection denominators.
- Using Sharpe ratio or PnL as a platform-quality score.
- Treating an LLM judge as ground truth without calibration and human audit.

## 7. Initial service-level objectives for staging experiments

These are proposed measurement targets, not claims about current production:

| Objective | Proposed target |
|---|---|
| Correlatable benchmark work | 100% has objective, task, attempt, and trace IDs |
| Duplicate authoritative terminals | 0 |
| Unbounded retries | 0 |
| Missing failure category | <1% of terminal failures |
| Reproducible deterministic fixtures | 100% |
| Recovery from worker death | Within two lease windows, no duplicate terminal |
| Dashboard metric drill-through | 100% of displayed benchmark aggregates |
| Unauthorized side effects | 0 |

Targets should be revised from observed baselines, with the revision recorded rather
than retroactively changing an experiment's pass criteria.
