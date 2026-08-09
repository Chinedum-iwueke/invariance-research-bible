<a id="b8-c13"></a>
# Chapter 13 — Execution Risk and Kill Controls

Execution controls prevent data, model, adapter, venue, or human error from creating unbounded market mutation.

## 13.1 Pre-trade controls

Validate authorization, environment, instrument, side, quantity, notional, price, stop geometry, position effect, margin, concentration, duplicate identity, market state, data freshness, rate limit, and parent envelope. Unknown state rejects risk increases.

## 13.2 Runtime controls

Monitor order and fill rates, rejects, latency, private-stream health, reconciliation, slippage, position and balance changes, losses, and venue status. Canary limits bound new live capability.

## 13.3 Freeze and kill

Freeze blocks risk-increasing mutation while permitting safe observation and authorized reduce-only action. Kill can cancel, stop submission, isolate an adapter, or invoke liquidation policy. Scope and priority are explicit; a kill is idempotent.

## 13.4 Human authority

Named roles can freeze and escalate. Restoration requires diagnosis, reconciliation, and approval. Credentials and manual venue actions are incorporated into audit and reconciliation.

> **Execution rule B8-EX13 — Safety controls dominate alpha**  
> No forecast, strategy, model, or operator may override hard execution limits, environment isolation, reconciliation freeze, or kill state.

## Source note

This chapter consumes Book VII limits and Book X security and incident controls.
