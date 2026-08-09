<a id="b7-c11"></a>
# Chapter 11 — Dynamic Risk Budgets and Regimes

Risk budgets may change when opportunity, uncertainty, liquidity, dependence, drawdown, or operational state changes. Dynamic control must avoid amplifying noisy estimates and crowding the portfolio into shared responses.

## 11.1 State inputs

Inputs can include forecast strength and uncertainty, realized and forecast volatility, covariance, liquidity, capacity, drawdown, margin, calibration, model support, data health, and operational incidents. Learned regime labels are model-dependent inputs under Book VI, not authoritative switches.

## 11.2 Mapping

The mapping from state to risk budget is versioned, bounded, smooth where possible, and tested for monotonic behavior. Hysteresis and minimum holding periods reduce churn. Hard constraints dominate dynamic budgets.

## 11.3 Procyclicality

Volatility targeting can reduce exposure after losses and increase it in calm periods, which may be useful but can become procyclical. Correlation and liquidity can worsen together. Stress tests shock the whole control rule, not just its inputs.

## 11.4 Uncertainty response

Weak support, degraded calibration, or conflicting models normally reduces or caps risk rather than increasing it. The portfolio distinguishes low forecast magnitude from high uncertainty and from missing data.

## 11.5 Governance

Automatic changes operate inside preauthorized bands. Crossing bands, changing mappings, or restoring risk after breach requires the designated authority. Every budget change records inputs, rule version, binding constraints, and expiry.

> **Risk rule B7-RK11 — Dynamic does not mean discretionary**  
> Risk budgets respond through bounded, testable, versioned mappings whose procyclical and joint-state behavior has been stressed in advance.

## Source note

This chapter consumes model and drift objects from Book VI and preserves Book II’s decision rights.
