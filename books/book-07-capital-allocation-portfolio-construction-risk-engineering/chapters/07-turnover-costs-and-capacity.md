<a id="b7-c07"></a>
# Chapter 7 — Turnover, Costs, and Capacity

Target weights are not portfolio value until they can be traded. Turnover, spreads, slippage, impact, borrow, funding, taxes where applicable, and operational throughput can reverse an allocation’s ranking.

## 7.1 Trade list

The allocator compares current executable positions with target positions, accounts for pending orders, cash, restrictions, and internal netting, then produces desired trades. Cost and risk are evaluated on the transition path, not only the endpoint.

## 7.2 Cost curves

Costs depend on instrument, venue, side, order type, size, participation, volatility, liquidity, latency, and urgency. Use distributions or conservative curves from Book VIII. A fixed basis-point penalty is a scenario, not a universal estimate.

## 7.3 Turnover control

No-trade regions, hysteresis, minimum economic improvement, explicit penalties, rebalance schedules, and trade compression can reduce churn. Their thresholds are selected under the same evidence controls as the allocator.

## 7.4 Capacity

Capacity is the exposure at which expected net contribution, risk, or execution quality ceases to satisfy policy. It is state- and horizon-dependent. Evaluate participation, order duration, crowding, borrow, venue limits, signal decay, impact, and liquidation capacity.

Backtest volume is not guaranteed available liquidity. Capacity estimates carry uncertainty and stress haircuts.

## 7.5 Attribution

Report forecast contribution, diversification benefit, turnover, explicit fees, spread, slippage, impact estimate, missed trades, and residual. Portfolio construction that improves gross results but loses net of transition costs is rejected.

> **Risk rule B7-RK07 — Capacity is a curve, not a badge**  
> Every strategy and portfolio has a versioned, state-dependent relationship among capital, turnover, cost, latency, and net contribution.

## Source note

Execution-cost evidence and market-impact semantics belong to Book VIII. Book VII owns their use in allocation and capacity.
