<a id="b8-c02"></a>
# Chapter 2 — Market Events, Clocks, and State

Execution systems operate across exchange, feed, client, broker, and accounting clocks. Ordering and timestamp quality determine what can be known and reconciled.

## 2.1 Event identities

Canonical events include quote and book updates, trades, auctions, halts, funding and index updates, order submission, acknowledgement, modification, cancellation, rejection, fill, position, balance, liquidation, and reconciliation. Each carries source, sequence where available, instrument identity, event time, receive time, and ingestion time.

## 2.2 Clock domains

Exchange timestamps can be coarse, delayed, corrected, or incomparable across venues. Local receive clocks need synchronization and monotonic capture. Latency is decomposed into observation, decision, serialization, network, venue processing, acknowledgement, and market response.

## 2.3 State reconstruction

Snapshots plus ordered deltas reconstruct books and accounts only when sequence continuity holds. Gaps trigger resnapshot and invalidate affected intervals. Late or duplicate events follow deterministic rules; they are never silently reordered to improve a result.

## 2.4 Point-in-time decisions

The execution policy sees only state received before its decision deadline. Later exchange timestamps do not retroactively make an event available. Replay preserves receive-time ordering as well as exchange time where possible.

> **Execution rule B8-EX02 — Availability is a local event**  
> A market fact enters an execution decision only when an authorized system received and validated it, regardless of the timestamp printed by its source.

## Source note

This chapter extends Books V–VI temporal contracts to venue events. Production time synchronization belongs to Book X.
