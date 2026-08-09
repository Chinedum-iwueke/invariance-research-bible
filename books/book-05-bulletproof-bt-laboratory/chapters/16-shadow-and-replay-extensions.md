<a id="b5-c16"></a>
# Chapter 16 — Shadow and Replay Extensions

Historical simulation, execution replay, and shadow operation answer different questions. A controlled transition preserves those distinctions instead of presenting them as one ascending performance score.

## 16.1 Historical replay

Historical replay reruns a strategy and its modeled downstream layers over fixed observations. It supports determinism, regression, sensitivity, and counterfactual policy tests. It cannot observe how the strategy would have affected the market.

The current classic engine is the principal historical path. Its run bundle and validation tools provide a foundation for replay comparison at a pin.

## 16.2 Execution replay

Execution replay applies order and risk intent to recorded quote, trade, bar, or venue lifecycle data to compare modeled and observed handling. It may test adapter mapping, latency assumptions, partial fills, cancellations, and reconciliation. It is still retrospective and constrained by captured data.

The repository contains execution-runtime contracts, simulated and venue adapters, event schemas, state stores, reconciliation, restart, idempotency, safety controls, and tests. A target replay service should ingest immutable production event journals and generate differences without mutating live state.

## 16.3 Shadow

Shadow is prospective observation on information arriving after registration. It computes decisions and may model orders, but it sends no market-mutating instructions. This makes it stronger than reused historical evaluation for freshness and operational timing, while weaker than demo or live evidence for venue interaction.

Shadow records input arrival, decision latency, intended orders, modeled fills, risk state, missed or stale observations, and comparison with later market outcomes. A shadow result cannot be backfilled after its timestamp and still retain prospective status.

## 16.4 Demo and micro-live

Demo uses a venue’s non-production environment or simulator and can test authentication, mapping, lifecycle, and operational control with uncertain equivalence to production matching. Micro-live mutates a real market under independent authorization and strict loss, notional, symbol, time, and kill controls. Neither state follows automatically from a good backtest.

The audited repository includes Bybit demo/live adapter and safety documentation and tests. The public audit lacks credentials and observed venue sessions, so no operational qualification claim follows.

## 16.5 Parity

The target transition compares signal identity, order intent, risk decision, order mapping, acknowledgement, fill, position, cost, and P&L across historical, shadow, demo, and live environments. Differences receive a taxonomy: expected environment difference, model misspecification, data issue, adapter defect, timing issue, or unknown.

> **Laboratory rule B5-LR16 — Environments do not promote themselves**  
> Historical, replay, shadow, demo, micro-live, and production evidence remain distinct states with separate authorization and acceptance criteria.

## Source note

Current statements derive from pinned classic engine and execution-runtime code, contracts, runbooks, and tests. Environment governance is defined in Book II; venue mechanics in Book VIII; deployment in Book X.
