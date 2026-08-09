<a id="b5-c05"></a>
# Chapter 5 — Strategy, Risk, Execution, and Portfolio Boundaries

A trustworthy simulator prevents strategy logic from silently becoming risk policy, execution policy, or accounting. The same signal should be testable under different admissible downstream assumptions without rewriting its scientific meaning.

## 5.1 Strategy

In the current classic engine, a strategy receives timestamped bars, a tradeable set, and a context containing indicator, state, warmup, and position information. It returns signals. Repository guidance forbids strategies from reaching into portfolio or execution internals.

A signal states direction and strategy metadata. It should not assert that capital is available, that an order will fill, or that a stop is valid. Strategy-specific stop proposals and sizing modifiers may travel as typed metadata, but risk owns their acceptance and canonical interpretation.

## 5.2 Risk

The pinned `RiskEngine` resolves stop contracts, computes stop-distance-based size, applies instrument conversion and quantity rounding, evaluates notional, leverage, free-margin, gross exposure, position caps, and related constraints, and emits stable rejection reasons. It distinguishes exits from entries and carries current position state into order-intent formation.

Pending delayed entries reserve position count, free margin, and gross notional in the audited engine. A second flat-to-entry signal for the same symbol is rejected while an active entry remains pending. This closes a capacity race in bar-delayed execution. It does not prove equivalent reservation across every separate execution-runtime path.

Book VII owns portfolio risk design. Book V’s responsibility is to apply a supplied, versioned risk contract deterministically and preserve every approval, modification, and rejection.

## 5.3 Execution

Execution converts orders into modeled fills using explicit profiles for spread, slippage, fees, commissions, intrabar behavior, and signal delay. A modeled fill is conditional evidence. Bar data cannot identify queue position, hidden liquidity, or the unique price path inside a candle.

The execution layer must never improve a result through a silent fallback. Unsupported order types, invalid stop geometry, missing bars, or ambiguous price rules should reject, fail, or downgrade the evidence class visibly.

## 5.4 Portfolio accounting

The classic `Portfolio` applies fills to a position book, realizes closed trades, marks open positions to market, and recalculates cash, equity, used margin, free margin, and gross notional. Accounting identities should reconcile from fills through positions to equity. Forced liquidation and terminal closeout are policy events, not ordinary strategy exits.

The separate `portfolio_engine` is an aggregation layer over strategy sleeves. It resolves equal, fixed, simple risk-parity, volatility-target, or manual capital allocation; tags artifacts; builds combined curves and summaries; and applies coordinator limits and conflict policies. Its backtest runner executes sleeves through existing single-strategy runs rather than implementing a unified same-clock event loop.

## 5.5 Live-readiness boundary

The portfolio deployment runner persists state, records events, applies coordinator checks, and refuses live mode unless `confirm_live_trading` is true. In the inspected `run_once` path it does not submit an order through its declared adapter protocol. It is therefore current evidence of a guarded readiness scaffold, not complete live portfolio execution.

The repository separately contains `bt.exec` runtime modules and tests for adapters, durability, reconciliation, idempotency, recovery, and live controls. Those surfaces require their own operational qualification. Book VIII owns venue mechanics; Book X owns deployment.

> **Laboratory rule B5-LR05 — Boundaries preserve counterfactuals**  
> Strategy, risk, execution, and accounting decisions remain separately attributable so investigators can identify which layer creates or destroys an observed effect.

## Source note

Current statements derive from the pinned strategy protocol, `RiskEngine`, `ExecutionModel`, classic `Portfolio`, `portfolio_engine`, deployment runner, documentation, and focused tests. Portfolio policy belongs to Book VII and venue execution to Book VIII.
