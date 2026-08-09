<a id="b7-c06"></a>
# Chapter 6 — Portfolio Construction Families

Portfolio construction maps forecasts and risk inputs into feasible target exposures. No family is assumption-free; comparison emphasizes sensitivity, stability, and decision consequences.

## 6.1 Families

Common families include equal or fixed weights, volatility scaling, risk budgets, minimum variance, mean-variance, maximum diversification, hierarchical or clustered allocation, robust optimization, scenario optimization, and utility or growth-based rules. Each defines what inputs it trusts.

Equal weight avoids return estimation but ignores unequal risk and capacity. Minimum variance depends heavily on covariance and can concentrate. Mean-variance adds fragile expected returns. Risk parity distributes modeled risk, not necessarily economic loss. Hierarchical methods depend on distance and clustering.

## 6.2 Robustness

Use shrinkage, uncertainty sets, regularization, turnover penalties, position bounds, and scenario constraints to reduce sensitivity. Robustness parameters are validated and interpreted; excessive conservatism can create hidden concentration or inactivity.

## 6.3 Benchmark ladder

Every complex allocator competes with fixed weights, inverse volatility, capped risk budgets, and current policy under identical costs and constraints. Compare realized risk, drawdown, turnover, concentration, stability, and forecast utilization—not return alone.

## 6.4 Solver evidence

Record objective, constraints, inputs, scaling, solver and tolerance, status, iterations, residuals, active constraints, and fallback. Equivalent mathematical problems can yield different numerical behavior under poor conditioning.

## 6.5 Rounding and implementation

Continuous weights become executable quantities through prices, contract sizes, lot steps, margin, cash, and minimum notional. Rounding is part of construction and can violate constraints if applied after optimization without repair.

> **Risk rule B7-RK06 — Allocation families compete under one contract**  
> A sophisticated optimizer earns use only through stable improvement over simple feasible baselines after costs, rounding, uncertainty, and stress.

## Source note

Mean-variance lineage begins with [Markowitz 1952](../../../bibliography/references.md#markowitz-1952). This chapter does not claim universal superiority for any portfolio family.
