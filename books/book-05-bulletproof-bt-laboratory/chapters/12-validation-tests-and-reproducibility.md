<a id="b5-c12"></a>
# Chapter 12 — Validation, Tests, and Reproducibility

Tests do not prove a simulator correct. They provide bounded evidence that named properties hold for exercised inputs in a recorded environment. A laboratory quality gate must state that scope precisely.

## 12.1 Validation layers

The pinned repository separates data, resample, alignment, signal, order, fill, position, portfolio, and determinism audits. It also contains sanity counters, artifact-contract checks, accounting and cost reconciliation, metric reconciliation, experiment truth validation, and extensive focused tests.

Truth validation checks completed run roots rather than trusting their summaries. Covered failures include notional-cap breach, future source timestamps, actual stop risk inconsistent with recorded risk, material risk-budget breach, divergent duplicate truth columns, and absent or incomplete evidence. It distinguishes valid zero-trade runs and explicitly logged cleanup from silent missing artifacts.

## 12.2 Test taxonomy

A mature suite includes:

- unit tests for formulas and state transitions;
- property tests for invariants over generated inputs;
- contract tests across modules and adapters;
- golden tests for stable artifacts;
- metamorphic tests such as future perturbation and scale transformations;
- differential tests against independent implementations;
- replay and reconciliation tests;
- failure-injection tests for interruption and retry; and
- credentialed certification in isolated non-production venue environments.

The public snapshot is rich in unit, integration, regression, and contract tests. The audit does not infer that every taxonomy category or production environment is covered.

## 12.3 Reconciliation gates

Before performance interpretation, the run must reconcile:

1. order and fill quantities;
2. fills and position transitions;
3. positions, realized P&L, and trades;
4. gross P&L minus itemized costs to net P&L;
5. cash, unrealized P&L, margin, and equity;
6. trade aggregates to performance outputs; and
7. required artifacts and declared schema versions.

Tolerance is unit-aware, justified, and recorded. A tolerance should absorb numeric representation, not economic discrepancies.

## 12.4 Audit result discipline

The Book V audit uses Python 3.12 because the project requires Python 3.11 or later. Source and tests passed byte-compilation at the pin. A focused 55-test contract set passed. A broader run produced 135 passes before interruption, seven reproducible failures, and dependency-limited collection errors. Two PyArrow downloads failed hash verification after truncation; Ruff was unavailable within the transfer envelope. The implementation register preserves the exact commands, counts, defect categories, and limitations.

The result is not “the suite passes.” It is a bounded behavioral audit with both positive and negative evidence. QG-011 passes only because the pin and claim boundary are faithful to those results.

Failures discovered by audit become evidence. They are not edited out of prose after a narrow fix unless the new commit is pinned and rerun.

## 12.5 Reproduction packet

A target reproduction packet contains exact commands, interpreter and dependency identity, platform class, code pin, dataset manifest, configuration, seeds, environment variables by name but not secret value, resource limits, expected artifact digests or semantic checks, and known variable fields.

> **Laboratory rule B5-LR12 — A quality gate reports what ran**  
> Test evidence names the code pin, environment, command, result counts, skips, failures, and limitations; “tested” without that record has no gate value.

## Source note

Current statements derive from pinned audit, validation, truth, reconciliation, deterministic, and focused test surfaces. The executable audit record is maintained in the [Implementation Reference Register](../../../registers/IMPLEMENTATION_REFERENCES.md).
