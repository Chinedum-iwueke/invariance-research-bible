<a id="b5-c08"></a>
# Chapter 8 — Costs, Fills, Benchmarks, and Diagnostics

Gross return is an incomplete experimental observation. The laboratory must show which prices were used, how quantity was constrained, which costs were applied, what benchmark was available, and where model uncertainty remains.

## 8.1 Current cost model

The pinned execution packages separate spread, slippage, fees, commission, execution profiles, effective configuration, and intrabar handling. Instrument packs can express market-specific assumptions such as FX spread and commission per lot or equity commission conventions. Cost attribution is written into fills, trades, performance extensions, and a machine-readable cost breakdown where configured.

These are explicit models, not guaranteed estimates of realized cost. A fixed basis-point slippage rule can support sensitivity analysis while remaining a poor forecast during stress.

## 8.2 Fill evidence

Every fill should retain order identity, symbol, side, quantity, timestamp, modeled price, cost components, execution rule, and relevant reason or state. Partial fills, rejected fills, and order expiry need their own lifecycle semantics. The classic engine’s open-order processing and audit hooks preserve a separation between order and fill, but bar-level execution cannot recover queue dynamics.

An invalid stop, missing execution bar, non-finite price, or quantity that violates instrument precision should create a rejection or invalid run—not a repaired favorable fill.

## 8.3 Intrabar ambiguity

If both stop and target lie inside one bar, OHLC does not reveal which occurred first. An intrabar mode chooses pessimistic, optimistic, ordered, or other declared policy. Results sensitive to that choice are fragile and must be reported as a range or boundary, not one observed fact.

Tick or lower-frequency replay can reduce ambiguity only when its source quality and clock alignment are adequate. Order-book and impact modeling remain deferred to Book VIII work.

## 8.4 Benchmarks

The repository supports buy-and-hold, flat, and baseline-strategy benchmark concepts, with benchmark equity, metrics, and comparison summaries when enabled. Benchmark alignment and normalization have dedicated modules and tests.

A benchmark must share the evaluation interval, admissible information, currency and valuation basis, and appropriate cost treatment. “Beats buy and hold” is not meaningful when leverage, risk, exposure, or tradable universe differ without normalization.

## 8.5 Diagnostics

Primary diagnostics reconcile counts and money before interpreting performance: signals, approvals, rejections by reason, orders, fills, positions, trades, gross P&L, each cost component, net P&L, cash, margin, and equity. Structural buckets, per-symbol metrics, MFE/MAE, duration, R multiples, and benchmark attribution help locate mechanisms and failures.

The repository includes post-run terminal and dashboard-oriented diagnostic services. They read artifacts after the engine completes. Their visual payloads are derived evidence and must link back to producer artifacts and schema versions.

## 8.6 Sensitivity as default

Cost and fill assumptions should be varied over registered plausible sets. A candidate that survives only zero spread, immediate fills, or one favorable intrabar rule is not robust evidence. Book IV owns the multiplicity of that search; Book V executes and labels each scenario; Book VIII judges empirical plausibility.

> **Laboratory rule B5-LR08 — Modeled execution is a conditional statement**  
> Every net result inherits the scope and uncertainty of the fill, cost, latency, and intrabar policies that produced it.

## Source note

Current statements derive from pinned execution, benchmark, cost-attribution, metric, artifact, and diagnostic modules and their tests. Market-impact and venue realism belong to Book VIII.
