<a id="b10-c14"></a>
# Chapter 14 — Testing and Deterministic Acceptance

Testing covers formulas, contracts, workflows, security boundaries, failure, recovery, and scientific invariants.

## 14.1 Pyramid

Use unit and property tests, schema and contract tests, integration, golden artifacts, metamorphic causality, differential implementations, end-to-end vertical slices, load and soak, fault injection, security tests, replay, and game days.

## 14.2 Determinism

Define canonical inputs, environment class, numeric tolerance, variable operational fields, seeds, concurrency, and expected artifact digests. Compare semantic events and normalized outputs.

## 14.3 Acceptance suites

Map every invariant and ADR to tests. Critical paths include evidence lineage, protected access, trial idempotency, no-lookahead, accounting, risk constraints, order lifecycle, capability enforcement, zero-mutation shadow, kill, and recovery.

## 14.4 Evidence

Record code pin, dependencies, command, environment, results, skips, failures, runtime, and artifacts. A gate can pass with known external defects only when scope and limitation are explicit, as Book V demonstrates.

> **Builder rule B10-BD14 — Tests state their proof boundary**  
> Passing evidence authorizes only the version, environment, paths, and properties actually exercised.

## Source note

This chapter consolidates quality requirements across the series.
