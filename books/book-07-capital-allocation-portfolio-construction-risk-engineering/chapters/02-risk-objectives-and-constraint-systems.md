<a id="b7-c02"></a>
# Chapter 2 — Risk Objectives and Constraint Systems

A portfolio objective is a declared trade among reward, uncertainty, loss, turnover, liquidity, complexity, and mandate. It is never “maximize Sharpe” without an estimation and constraint contract.

## 2.1 Objective families

Objectives may target expected utility, mean-risk tradeoffs, risk-adjusted return, expected log growth, tracking error, drawdown-aware utility, tail loss, or robust worst-case performance. Each embeds assumptions about horizon, return distribution, path, and investor preference.

Mean-variance analysis originates in [Markowitz 1952](../../../bibliography/references.md#markowitz-1952), which formalizes portfolios through expected return and variance. It remains a useful framework, not a claim that variance captures every economically relevant risk.

## 2.2 Constraint taxonomy

Constraints include gross and net exposure, leverage, margin, per-position and per-strategy caps, asset and venue concentration, factor exposure, liquidity and participation, turnover, borrow, currency, mandate, daily loss, drawdown, and operational readiness. They have owner, units, scope, priority, effective time, and breach action.

## 2.3 Soft and hard

Soft penalties express preferences and can be traded off. Hard constraints define admissibility. Slack variables can diagnose infeasibility but cannot silently legalize a breach. Emergency liquidation policy may temporarily violate ordinary turnover preferences while respecting higher-order survival controls.

## 2.4 Horizon alignment

Forecast, covariance, cost, and constraint horizons must correspond. Daily covariance does not directly justify intraday liquidation risk; long-horizon expected return may not cover near-term margin calls. Multi-horizon portfolios retain separate state variables.

## 2.5 Feasibility evidence

Before optimization, validate units, sign conventions, positive-semidefinite risk inputs where required, price and FX freshness, capacity, margin, and constraint consistency. An infeasible problem produces a typed failure and fallback, not a relaxed solution chosen by the solver.

> **Risk rule B7-RK02 — Constraint priority is explicit**  
> When objectives and constraints conflict, the system follows a governed priority order and records which rule bound or rejected the portfolio.

## Source note

Mean-variance claims link to [Markowitz 1952](../../../bibliography/references.md#markowitz-1952). Tail-risk objectives are developed in Chapter 8.
