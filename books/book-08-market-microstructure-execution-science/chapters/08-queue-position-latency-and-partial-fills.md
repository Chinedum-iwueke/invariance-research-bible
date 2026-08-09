<a id="b8-c08"></a>
# Chapter 8 — Queue Position, Latency, and Partial Fills

Passive execution depends on priority and future order flow. Public market-by-price data rarely reveal exact queue position, so fill models must expose uncertainty.

## 8.1 Queue inference

Estimate initial quantity ahead, priority rule, cancellations ahead or behind, hidden liquidity, self orders, and trade allocation. Conservative and optimistic models define a range. Market-by-order feeds can improve inference when identities and sequence are reliable.

## 8.2 Latency

Measure observation-to-decision, decision-to-send, network, venue acknowledgement, and cancel latency as distributions. Clock error and batching are separated from true latency. Tail latency matters to adverse selection and kill behavior.

## 8.3 Partial fills

Each partial fill updates remaining quantity, average price, fees, risk, position, and parent progress. Strategies and allocators cannot assume atomic fills. Cancel-fill races require reconciliation.

## 8.4 Simulation

Bar simulation cannot establish queue position. Event replay can estimate it only within feed coverage. Fill-model parameters are calibrated prospectively and segmented by venue, state, order type, and size.

> **Execution rule B8-EX08 — Passive fills are interval estimates**  
> When priority and hidden activity are unobserved, fill evidence is reported under explicit queue assumptions rather than as exact counterfactual execution.

## Source note

This chapter defines modeling boundaries; Book V carries them into simulation and Book X into telemetry.
