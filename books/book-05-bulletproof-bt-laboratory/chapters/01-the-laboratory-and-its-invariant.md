<a id="b5-c01"></a>
# Chapter 1 — The Laboratory and Its Invariant

Bulletproof BT is the institution’s historical experimental instrument. It converts a registered research question, point-in-time data, configuration, and code version into an inspectable run bundle. Its central obligation is not to make a strategy look attractive. It is to make the path from experimental intent to reported observation explicit enough to reproduce, criticize, and invalidate.

The laboratory sits between discovery and judgment. Book IV proposes hypothesis and search contracts. Book V executes their supported forms. Research Intelligence preserves the resulting primary evidence. Hermes governs promotion. Books VII and VIII determine whether portfolio and execution consequences survive their own evidence burdens.

## 1.1 The laboratory invariant

For a pinned implementation and supported environment, equal canonical inputs should produce equal economic events and equal normalized scientific outputs. The relevant inputs include data bytes and manifest, resolved configuration, strategy and contract versions, instrument rules, random seeds where permitted, and runtime dependencies.

This is narrower than saying every byte in every directory is equal. Creation timestamps, absolute output paths, process diagnostics, and permitted environment metadata can vary. The pinned repository’s own deterministic-artifact tests remove `created_at_utc` and `run_dir` before comparing manifests. Book V therefore distinguishes:

- **semantic determinism:** equal ordered decisions, orders, fills, trades, equity, and normalized metrics;
- **serialization determinism:** stable ordering, numeric normalization, and encoding for designated artifacts;
- **operational repeatability:** execution succeeds under a declared environment and resource envelope; and
- **scientific reproducibility:** another authorized investigator can reconstruct the experiment and its interpretation.

One does not imply all the others.

> **Laboratory rule B5-LR01 — Reproducibility begins with closure**  
> A run is reproducible only when its material inputs, versions, temporal policy, outputs, and exceptions are closed under an explicit contract.

## 1.2 What a backtest observes

A backtest observes behavior inside a model. Historical bars are representations, fills are modeled events, costs are assumptions or estimates, and market impact is absent unless explicitly modeled. The output is evidence about a strategy under those conditions. It is not a counterfactual proof of what production would have earned.

The laboratory must therefore expose the chain:

1. source observations become validated market records;
2. records become time-ordered events and completed representations;
3. strategy logic emits typed signals;
4. risk logic approves, modifies, or rejects intent;
5. execution logic converts orders into modeled fills;
6. portfolio logic updates cash, positions, margin, and equity;
7. validators reconcile events and artifacts; and
8. reporting derives summaries without replacing primary records.

Every broken link limits the claim.

## 1.3 Current implementation boundary

At audited commit `ba2a0314817607c5c79d604a0846e008c14379c2`, the classic engine is a bar-driven, single-strategy event loop with separate data, strategy, risk, execution, portfolio, audit, metric, and logging surfaces. The repository also contains experiment orchestration, research-data extraction, hypothesis contracts, a separate multi-strategy portfolio layer, and paper/live execution-runtime code. Their presence does not make them equally mature or prove production operation.

Current behavior in this volume means behavior supported by inspected code, tests, schemas, and executable audit evidence at that pin. An extension is a plausible next slice compatible with the current system. Target architecture describes the institutional destination. Deferred capability is intentionally outside the present claim.

## 1.4 Failure is an output

Invalid data, impossible stops, rejected orders, missing artifacts, reconciliation differences, and truth-check failures are scientific outputs. A system that suppresses them to preserve a clean summary corrupts evidence. A failed run bundle should remain attributable, diagnosable, and distinct from a valid negative result.

The laboratory succeeds when it makes error legible. Performance comes later.

## Source note

Current implementation statements derive from the pinned Bulletproof BT audit in the [Implementation Reference Register](../../../registers/IMPLEMENTATION_REFERENCES.md). Institutional rules extend Books I–IV; they are not claims that every target control is currently implemented.
