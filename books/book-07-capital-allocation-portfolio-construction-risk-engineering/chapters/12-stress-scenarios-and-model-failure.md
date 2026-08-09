<a id="b7-c12"></a>
# Chapter 12 — Stress, Scenarios, and Model Failure

Stress testing asks what the portfolio and control system do when estimated relationships fail. It is not a single historical replay or a decorative loss number.

## 12.1 Scenario families

Use historical episodes, hypothetical macro and market shocks, factor shocks, correlation convergence, volatility and gap shocks, liquidity withdrawal, spread and impact expansion, funding and borrow stress, venue outage, data corruption, model failure, and combined operational-market scenarios.

## 12.2 Coherence

Scenario variables should be economically coherent or explicitly adversarial. Shocking prices without FX, volatility, liquidity, margin, and funding responses can understate loss. Conversely, arbitrary simultaneous extremes can be useful as boundary tests but should not be assigned a probability without evidence.

## 12.3 Model failure

Stress forecast sign reversal, calibration collapse, covariance error, false diversification, capacity overestimate, stale data, optimizer failure, duplicated orders, and delayed risk state. Evaluate fallbacks and human response, not only theoretical portfolio loss.

## 12.4 Reverse stress

Begin from breach—margin call, drawdown limit, liquidity shortfall, or operational freeze—and solve for plausible combinations that produce it. Reverse stress reveals hidden concentrations and narrow safety margins.

## 12.5 Outputs

Report path, peak loss, margin and liquidity use, constraint breaches, liquidation sequence, cost, recovery time, strategy and dependency contributions, control actions, and unresolved assumptions. Scenarios inform limits; they do not predict occurrence dates.

> **Risk rule B7-RK12 — Stress the controls with the portfolio**  
> A scenario is incomplete unless it tests data, models, constraints, execution, operational response, and recovery along the loss path.

## Source note

This chapter integrates portfolio risk with Books VIII and X operational failure. It does not attach empirical probabilities to hypothetical scenarios.
