<a id="b6-c14"></a>
# Chapter 14 — ML for Sizing, Allocation, and Execution

ML can estimate inputs to sizing, allocation, and execution. It does not own the constrained decisions those estimates inform.

## 14.1 Forecast objects

Useful outputs include expected return distributions, calibrated direction probabilities, volatility and covariance forecasts, tail and drawdown risk, fill probability, cost quantiles, capacity proxies, and support or degradation scores. Each object has target, horizon, units, uncertainty, calibration, and version.

Generic confidence is prohibited. A 70% event probability, a narrow return interval, low ensemble disagreement, and high data support describe different properties.

## 14.2 Sizing

A learned trade-quality estimate may alter a proposed risk budget only through a Book VII mapping that is monotone where justified, capped, stress-tested, and robust to calibration error. Hard exposure, leverage, concentration, liquidity, and loss limits remain outside the model.

Backtests compare learned sizing with fixed and simple volatility-scaled baselines. They account for nonlinear costs and selection introduced by abstention.

## 14.3 Allocation

Forecasts feed an allocator alongside dependence, turnover, capacity, constraints, model risk, and uncertainty. Joint training of forecasts and allocations can optimize decision loss, but evaluation must reveal which layer creates improvement and guard against unstable end-to-end policies.

Book VII owns covariance, robust optimization, risk budgets, capacity, and capital admission.

## 14.4 Execution

Models can predict fill, cost, short-horizon movement, venue state, or order duration. Book VIII owns the action space, order lifecycle, venue constraints, routing, and safety. A router cannot choose unsupported actions because a model assigns high value.

## 14.5 Interface contract

The ML service returns a typed forecast plus model and data identity, generation time, valid horizon, support, uncertainty, and reasoned abstention. Consumers validate freshness and compatibility, apply independent constraints, and log the exact forecast used.

> **ML rule B6-ML14 — Models estimate; constrained systems decide**  
> Capital and execution actions remain functions of typed forecasts, uncertainty, costs, constraints, and accountable policy—not raw model scores.

## Source note

This chapter defines interfaces to Books VII–VIII. It does not prescribe an allocation optimizer or live routing policy.
