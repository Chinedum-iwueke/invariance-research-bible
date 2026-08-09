<a id="b7-c05"></a>
# Chapter 5 — Dependency, Diversification, and Concentration

Diversification depends on joint behavior, not labels or strategy count. Two candidates can share return, factor, liquidity, data, venue, model, or operational failure even when their names differ.

## 5.1 Dependency layers

Measure return and residual dependence across horizons and states; shared factor exposure; common instruments and liquidity; joint drawdowns; tail co-movement; mechanism similarity; data and feature lineage; model family; venue and broker; and shared infrastructure. Qualitative mechanism maps complement but do not replace statistical estimates.

## 5.2 Estimation

Sample covariance can be unstable when dimension is large relative to history. [Ledoit and Wolf 2004](../../../bibliography/references.md#ledoit-wolf-2004) develops a well-conditioned linear shrinkage estimator under its asymptotic criterion. Shrinkage improves conditioning under its design; it does not make covariance stationary or capture every tail dependence.

Use horizons and weights aligned with the portfolio, robust estimators where justified, and uncertainty or stress alternatives. Positive-semidefinite repair is recorded because it changes the risk model.

## 5.3 Concentration

Concentration is tracked by position, instrument, issuer, asset class, factor, strategy, mechanism, venue, liquidity bucket, currency, data source, and operational dependency. Net exposure can hide large gross opposing books and shared liquidation risk.

## 5.4 State dependence

Correlations often change during stress. Evaluate rolling, conditional, and scenario dependence without treating estimated regimes as truth. The portfolio keeps slack for dependence uncertainty and common deleveraging.

## 5.5 Diversification credit

Diversification credit is conservative, capped, and revocable. A new strategy with short history receives less credit even if estimated correlation is low. Missing overlap is uncertainty, not independence.

> **Risk rule B7-RK05 — Unknown dependence is not diversification**  
> Capital receives diversification credit only for measured, economically interpretable, stress-tested dependence under adequate overlapping evidence.

## Source note

Covariance-estimation claims link to [Ledoit and Wolf 2004](../../../bibliography/references.md#ledoit-wolf-2004). Knowledge-layer mechanism dependencies originate in Book III.
