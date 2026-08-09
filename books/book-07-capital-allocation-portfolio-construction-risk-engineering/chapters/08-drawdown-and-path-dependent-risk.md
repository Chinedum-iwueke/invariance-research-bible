<a id="b7-c08"></a>
# Chapter 8 — Drawdown and Path-Dependent Risk

Variance and terminal loss do not describe the sequence of losses, recovery, margin pressure, or mandate breach. Portfolio risk therefore includes path-dependent measures and scenario trajectories.

## 8.1 Drawdown

Define high-water mark, measurement frequency, valuation policy, intra-period treatment, recovery, and cash-flow adjustment. Historical maximum drawdown is one observed path, not a bound on future loss.

Monitor current drawdown, duration, recovery time, speed, strategy contributions, and proximity to action thresholds. Thresholds trigger governed responses rather than forecasts of inevitability.

## 8.2 Tail risk

Value-at-Risk is a quantile under a model and horizon; it does not describe losses beyond the quantile. Conditional Value-at-Risk or expected shortfall summarizes tail loss under its distribution. [Rockafellar and Uryasev 2000](../../../bibliography/references.md#rockafellar-uryasev-2000) provides an optimization formulation for CVaR under the paper’s setup. Estimated tail risk remains sensitive to data, dependence, and regime.

## 8.3 Path simulation

Bootstrap, block resampling, parametric simulation, scenario paths, and historical replay preserve different structures. Simulated paths state what dependence, non-stationarity, cost, liquidity, and feedback they omit. Monte Carlo quantity does not repair model misspecification.

## 8.4 Controls

Drawdown controls can reduce risk budgets, stop new entries, prioritize liquidations, or trigger governance review. Mechanical deleveraging can worsen costs in stress, so actions consider liquidity and margin. Hard loss boundaries remain enforceable.

## 8.5 Recovery

Recovery plans specify minimum evidence and authorization before risk restoration. A rebound does not erase the incident or justify immediate full scaling.

> **Risk rule B7-RK08 — Path risk is operational risk**  
> Drawdown, margin, liquidity, and recovery are evaluated as sequences of states and actions, not only as terminal distribution summaries.

## Source note

The CVaR optimization claim links to [Rockafellar and Uryasev 2000](../../../bibliography/references.md#rockafellar-uryasev-2000).
