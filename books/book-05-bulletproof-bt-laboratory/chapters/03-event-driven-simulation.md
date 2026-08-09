<a id="b5-c03"></a>
# Chapter 3 — Event-Driven Simulation

An event-driven simulator advances through information in the order declared by its clock and transforms state through explicit boundaries. The value of the form is not realism by itself. Its value is that causal ordering can be stated, tested, and audited.

## 3.1 Current loop

The pinned `BacktestEngine` accepts a historical data feed, universe engine, strategy, risk engine, execution model, portfolio, artifact writers, resolved configuration, and optional audit and sanity components. Its documented loop performs the following sequence for each feed step:

1. receive bars from the feed;
2. update universe state and indicators;
3. construct strategy context, including optional online state;
4. obtain signals from the strategy;
5. convert approved signals to order intent through risk;
6. materialize typed orders;
7. process open orders through execution;
8. apply fills to portfolio accounting;
9. mark positions to market; and
10. write decision, fill, trade, and equity evidence.

Warmup timestamps update state but expose an empty tradeable set and do not pass signals into order formation. Open orders and positions are synchronized back to feeds that expose execution-state hooks. At exhaustion, the engine can write flat equity rows for feed timestamps skipped by optimized paths and then handles residual exposure according to configured closeout behavior.

## 3.2 State machines, not rows

A bar is an observation event. A signal is a strategy statement. An order intent is a risk-conditioned request. An order has lifecycle state. A fill changes cash and position state. A trade is a derived episode formed from fills. Collapsing these into one table erases rejection, delay, partial lifecycle, and causality.

The current core types distinguish `Bar`, `Signal`, `OrderIntent`, `Order`, `Fill`, `Position`, and `Trade`. Their timestamps are checked for UTC awareness. The distinction allows audit layers to inspect alignment, signals, orders, fills, positions, portfolio state, data, and resampling separately.

## 3.3 Ordering is policy

Whether a strategy observes a bar before an order fills, whether stops are evaluated inside a bar, and whether a delayed order reserves risk capacity are scientific choices. The audited commit explicitly reserves capacity for active pending entries and rejects a new entry when the same symbol already has a pending entry. Those controls prevent a delayed-fill model from approving several intents against the same unreserved account snapshot.

This does not settle all ordering questions. A bar simulator cannot infer the unique intrabar path from OHLC alone. Execution profiles and intrabar modes select a policy. The resulting observation is conditional on that policy.

## 3.4 One clock and many clocks

The classic loop groups bars by timestamp. Higher-timeframe contexts are emitted only after their buckets close under the tested strict resampler path. Funding, open interest, benchmarks, and enriched state may have distinct source times. Their values are admissible only if their source timestamps satisfy the experiment’s availability rule.

A target laboratory should represent observation, source publication, decision, submission, acknowledgement, fill, and accounting times explicitly. Current backtest evidence is strongest for its bar and source-time contracts; venue lifecycle timing belongs primarily to Book VIII.

## 3.5 Extending the engine

A new event type requires identity, timestamp semantics, ordering priority, admissible state transitions, failure behavior, serialization, replay behavior, and tests against adjacent events. Adding a callback without those elements creates hidden scheduling policy.

The target engine should support deterministic replay from an event journal and compare reconstructed terminal state with emitted artifacts. That is a target contract, not a claim that every current run can be rebuilt solely from one canonical journal.

> **Laboratory rule B5-LR03 — Ordering is part of the hypothesis**  
> Any change to event order, information availability, fill timing, or state update order creates a different experiment unless equivalence is demonstrated.

## Source note

Current behavior derives from `src/bt/core/engine.py`, core event types, audit modules, feed hooks, and associated tests at the pinned commit. Execution realism and venue clocks are developed in Book VIII.
