<a id="b8-c06"></a>
# Chapter 6 — Venue Fragmentation and Instrument Identity

Nominally similar instruments trade under different participants, collateral, fees, rules, liquidity, outages, and legal relationships. Cross-venue comparison begins with identity and normalization.

## 6.1 Instrument master

The master records venue, product, native symbol, economic underlying, quote and settlement currency, contract type and multiplier, expiry or perpetual status, tick and lot, minimums, margin and fee schedule, sessions, status, and effective intervals.

## 6.2 Price comparability

Normalize FX, inverse contracts, units, timestamps, and reference prices before calculating spreads or basis. A cross-venue price gap may reflect funding, collateral, withdrawal friction, latency, stale feeds, or contract difference rather than arbitrage.

## 6.3 Routing constraints

Capital and inventory are venue-specific in stress. Transfers have delay and custody risk. Routing considers balances, margin, order support, rate limits, reliability, legal permissions, and kill state—not quote alone.

## 6.4 Consolidated state

A consolidated book is a derived representation with receive-time alignment and executable quantity after fees and constraints. It never implies one matching pool.

> **Execution rule B8-EX06 — Consolidation preserves fragmentation**  
> Cross-venue views normalize comparable economics while retaining venue-specific inventory, latency, rules, and failure domains.

## Source note

This chapter interfaces with Book VII concentration and Book X custody and connectivity controls.
