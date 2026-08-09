<a id="b9-c13"></a>
# Chapter 13 — Evaluation, Calibration, and Reliability

Agent evaluation measures task completion, evidence quality, safety, efficiency, and recovery in interactive environments. Static answer accuracy is insufficient.

## 13.1 Evaluation unit

Evaluate the full system: model, prompt, context assembly, tools, permissions, workflow, and environment. Record seeds or sampling, retries, budgets, and evaluator.

## 13.2 Metrics

Measure valid completion, factual and citation accuracy, schema compliance, tool correctness, side effects, authorization violations, overreach, abstention, latency, cost, recovery, and human correction burden. Severity-weighted failures accompany averages.

## 13.3 Benchmarks

[AgentBench](../../../bibliography/references.md#liu-et-al-2024-agentbench) demonstrates multi-environment evaluation and reports substantial variation and common failures among tested models. Benchmarks are useful evidence for covered tasks; local workflows require local suites and prospective monitoring.

## 13.4 Calibration

Agent confidence is typed: claim support, task completeness, tool-state certainty, or prediction probability. Self-report is calibrated against outcomes and cannot override deterministic validation.

## 13.5 Release gate

New model, prompt, tool, or workflow versions run regression, adversarial, shadow, and canary suites. Material regressions block or narrow release.

> **Agent rule B9-AG13 — Evaluate the action system**  
> Reliability evidence covers multi-step behavior, tool consequences, permissions, recovery, and evidence quality under the intended environment.

## Source note

The benchmark claim links to the primary [AgentBench paper](../../../bibliography/references.md#liu-et-al-2024-agentbench).
