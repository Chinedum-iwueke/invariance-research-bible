<a id="b8-c04"></a>
# Chapter 4 — Crypto Spot and Perpetual Mechanics

Crypto is the initial model organism because it offers continuous trading, public APIs, multiple venues, and rich derivatives. Its mechanics are not universal market law.

## 4.1 Spot

Spot instruments exchange base and quote assets under venue-specific precision, minimum notional, fee, settlement, custody, and account rules. “BTCUSD” is not identity without venue and contract metadata.

## 4.2 Perpetuals

Perpetual contracts use an index, mark, funding mechanism, contract multiplier, collateral, and liquidation rules to track an underlying reference without fixed maturity. Linear and inverse contracts have different quantity and P&L geometry. Cross and isolated margin create different account coupling.

## 4.3 Continuous does not mean stationary

Trading continues across weekends, but liquidity, participation, maintenance, and venue reliability vary. Session definitions remain useful analytical constructs and can differ by purpose.

## 4.4 Venue rules

Tick and lot sizes, price bands, reduce-only and post-only behavior, self-trade prevention, trigger price, position mode, rate limits, and maintenance tiers are versioned venue facts. Adapters reject unknown or stale rules.

## 4.5 Portability

The canonical contract abstracts instrument, account, order, fee, margin, and event semantics while retaining venue extensions. Expansion to FX, equities, futures, and options requires their own calendars, settlement, corporate actions, rolls, and regulation.

> **Execution rule B8-EX04 — Symbol strings do not identify instruments**  
> Every order binds venue, product, contract, settlement, collateral, multiplier, precision, and effective rule version.

## Source note

This chapter defines general contract requirements and deliberately avoids unstable current venue parameters, which must be verified at execution time.
