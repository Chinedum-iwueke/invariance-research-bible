<a id="b8-c15"></a>
# Chapter 15 — Monitoring Venue and Strategy Degradation

Execution degradation can arise from venue rules, liquidity, participant behavior, strategy footprint, infrastructure, or model drift.

## 15.1 Signals

Monitor spread and depth, fill and cancel behavior, latency, rejects, rate limits, funding and borrow, cost and adverse selection, queue-model error, venue outages, reconciliation, and strategy participation. Segment by venue, instrument, order type, size, and state.

## 15.2 Strategy footprint

Rising impact, declining passive fills, faster post-trade reversal, or concentration can indicate capacity pressure or crowding. Evidence remains conditional and must distinguish market-wide change from the institution’s own policy.

## 15.3 Response

Responses include observation, route restriction, smaller participation, greater abstention, recalibration, shadow fallback, risk reduction, venue quarantine, or kill. Current terms and rule changes are verified.

## 15.4 Feedback

Execution findings update Book VII capacity and costs, Book VI cost models, Book V simulation, and Book III evidence. They do not change strategy or capital automatically.

> **Execution rule B8-EX15 — Degradation is jointly diagnosed**  
> Venue, model, strategy, and infrastructure explanations remain separate until event, cost, and operational evidence distinguishes them.

## Source note

This chapter integrates drift monitoring across Books VI–X.
