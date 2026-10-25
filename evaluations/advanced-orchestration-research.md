# Advanced Orchestration Research Agenda

## 1. Scope

This agenda addresses Phase 7 of the program. It separates established engineering
work from open research and selects questions grounded in current Invariance Research
limitations.

## 2. Relevance map

| Question | Current relevance | Classification |
|---|---|---|
| When does multi-agent orchestration outperform one agent? | High; many specialized roles exist without a complete comparative benchmark | Open empirical question |
| How should the orchestrator allocate tasks? | High; capacity and question schedulers exist, but cost/value policy is incomplete | Engineering plus research |
| How should specialized agents be selected? | High; capability routes exist, performance-based selection does not | Engineering plus contextual decision research |
| Sequential versus concurrent execution | High; parallelism, memory, and dependency constraints are operational | Established scheduling plus empirical tuning |
| Efficient communication | High; context and coordination cost are material | Established protocols plus open compression questions |
| Avoiding duplicate work | High; duplicate campaigns/tasks have occurred | Established idempotency and semantic-dedup engineering |
| Resolving contradictory findings | High; independent review and evidence disputes exist | Established provenance plus open adjudication design |
| Adaptive replanning after evidence | High; reconcilers and successors exist | Workflow engineering plus planning research |
| Learning from execution traces | High; rich traces exist but are not yet a validated planning dataset | Open empirical question |
| Memory compression | Medium-high; context limits matter and RI-015 is unqualified | Information-retrieval and summarization research |
| Confidence-aware delegation | Medium-high; routing is capability-based, not well-calibrated | Open empirical question |
| Independent verification in planning | High; reviews occur late and are expensive | Verification engineering plus research |
| Limited-compute operation | High; CPU-only hosts and model cost constrain the loop | Scheduling/optimization |
| Deterministic/model boundary | Very high; this is the central architecture question | Engineering judgment supported by experiments |
| Cascading failure containment | High; failed artifacts can create successors and noise | Established safety/reliability engineering |
| Risk-adjusted autonomy | Very high; mandates, approvals, and capital boundaries exist | Policy engineering and human factors |

## 3. Research program A: Does specialization earn its cost?

**Hypothesis:** Specialist research, representation, and review agents improve
verified completion and reduce scientific false acceptance on heterogeneous tasks
relative to one well-tooled agent under the same total budget.

**Baselines:** deterministic qualification; single agent; current centralized/hybrid
specialists.

**Dataset:** sealed mix of literature questions, duplicate proposals, representation
choices, causal defects, and strategy-intent cases.

**Metrics:** verified completion, false acceptance, evidence recall, abstention,
latency, total tokens, coordination overhead, interventions, and reproducibility.

**Ablations:** remove representation specialist; share versus separate reviewer
context; replace director with deterministic router.

**Failure criteria:** authority violation, unsupported-claim increase, no material
primary-outcome gain, or cost increase beyond the preregistered threshold.

**Reproducibility:** use the comparative benchmark protocol and retain all prompts and
traces.

## 4. Research program B: Independent reviewer value and correlation

**Hypothesis:** Reviewer independence reduces false acceptance only when producer and
reviewer differ materially in context, instructions, and/or model error profile.

**Baselines:** deterministic validator, producer self-review, same-model independent
context, different-model independent context, and expert labels.

**Dataset:** accepted and defective strategy bundles with seeded timing, target,
variant, and logging defects.

**Metrics:** sensitivity, specificity, disagreement, calibration, cost, and earliest
correct rejection stage.

**Failure criteria:** reviewers approve known leakage above the bound, or “independent”
review has error correlation indistinguishable from self-review.

## 5. Research program C: Failure-aware task allocation

**Hypothesis:** A scheduler using capability, failure class, cost, and estimated value
of information produces more verified terminal evidence per constrained resource than
FIFO or utilization maximization.

**Baselines:** FIFO, shortest-job-first, static priority, utilization-maximizing, and
oracle upper bound in simulation.

**Dataset:** immutable historical task descriptors plus synthetic rare failures;
outcomes used for evaluation must be hidden from policy features.

**Metrics:** verified terminals per dollar/CPU-hour, queue latency, diversity, repeated
failure, memory pressure, and interactive-service impact.

**Safety:** offline evaluation only until a deterministic fallback and regret bound or
operational stop condition is established.

## 6. Research program D: Trace-informed recovery planning

**Hypothesis:** Retrieval of structurally similar prior failure traces reduces repeated
repair attempts without causing stale repair transfer.

**Baselines:** static runbook, no retrieval, lexical retrieval, structured failure
signature retrieval, and model-generated repair proposal.

**Dataset:** sanitized incidents labeled by root cause, repair, affected version, and
whether the repair generalizes.

**Metrics:** correct first repair proposal, repeated failure count, time to containment,
stale-repair rejection, unsupported command rate, and human intervention.

**Failure criteria:** any proposed destructive or authority-expanding action outside
the test policy, or higher stale-repair application than baseline.

## 7. Research program E: Context compression without evidence loss

**Hypothesis:** Provenance-aware structured compression reduces context tokens while
preserving material evidence recall better than free-form summaries.

**Baselines:** full context, truncation, extractive selection, free-form summary,
structured claim-evidence summary, and graph-expanded retrieval.

**Dataset:** research questions with gold supporting and opposing evidence, including
tables, equations, deleted/restricted payload states, and negative results.

**Metrics:** evidence recall, unsupported claims, opposing-evidence recall, token count,
latency, and source resolvability.

**Failure criteria:** a compressed context silently changes a quantitative claim or
omits preregistered opposing evidence beyond threshold.

## 8. Research program F: Risk-adjusted autonomy

**Hypothesis:** Effect-based autonomy tiers reduce avoidable approval stalls without
increasing authority ambiguity or unauthorized effects.

**Baselines:** approval for every model task, current policy, and broad time-limited
delegation.

**Dataset:** replayed task/approval histories plus simulated new-code, data-scope,
shadow, demo, and capital actions.

**Metrics:** avoidable wait, approval count, expired approvals, effective-scope
comprehension, policy violations, and time to revoke.

**Hard boundary:** no experiment uses live capital. Policy simulation and staging only.

## 9. Established engineering before research

The following should not be presented as novel AI research:

- database uniqueness and idempotency for duplicate work;
- transactional outbox for reliable publication;
- leases and heartbeat-based work claims;
- schema and consumer contract tests;
- circuit breakers for repeated failures;
- structured logs, traces, and metric definitions;
- least privilege and short-lived credentials;
- deterministic data-timing and strategy semantic checks; and
- release manifests and rollback.

Implementing these well creates the stable platform on which meaningful agentic
experiments can run.

## 10. Selection order

1. Reviewer value and correlation: bounded, directly tied to current failures.
2. Specialization versus one agent: tests the core multi-agent premise.
3. Failure-aware allocation: uses existing traces and addresses cost.
4. Context compression: follows retrieval gold-set construction.
5. Trace-informed recovery: requires sanitized incident labels.
6. Risk-adjusted autonomy: follows a clean canonical authority projection.

No program proceeds to production merely because its offline average improves.
