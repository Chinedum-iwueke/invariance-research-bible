<a id="b10-c10"></a>
# Chapter 10 — Shadow MVP

Shadow provides prospective, zero-mutation evidence using live-arriving data, frozen candidates, and production-like computation.

## 10.1 Components

Live data adapters, point-in-time state builder, strategy and model runner, risk evaluator, simulated execution, event journal, outcome enricher, parity analyzer, monitoring, and immutable artifacts.

## 10.2 Guarantees

No order-mutating credential or network path is available. Decisions and intended orders are timestamped before outcomes. Backfill cannot receive prospective status.

## 10.3 Parity

Compare historical assumptions with live data availability, latency, signal rate, risk rejection, modeled cost, and later outcomes. Missing data and outages remain evidence.

## 10.4 Acceptance

Run continuously, recover from restart, prove zero mutation, produce complete journals, validate clocks, and publish prospective evidence with known gaps.

> **Builder rule B10-BD10 — Shadow is production-shaped and mutation-free**  
> The shadow stack exercises real data and computation paths while architectural controls make market mutation impossible.

## Source note

Environment semantics follow Books II, V, and VIII.
