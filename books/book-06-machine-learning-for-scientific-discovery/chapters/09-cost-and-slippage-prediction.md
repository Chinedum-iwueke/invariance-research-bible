<a id="b6-c09"></a>
# Chapter 9 — Cost and Slippage Prediction

Execution cost is a conditional distribution shaped by order, venue, market state, latency, and the institution’s own behavior. ML can estimate that distribution, but historical fills are selected observations produced by prior routing and risk policies.

## 9.1 Target decomposition

Separate spread paid, price movement during latency, market impact, fee and rebate, missed-fill opportunity, adverse selection, and post-fill drift. Their clocks and causal drivers differ. A single “slippage” target can hide compensation among errors.

Targets use a declared reference price, side convention, horizon, currency, and treatment of partial or cancelled orders. Censoring is explicit when an order does not fill.

## 9.2 Dataset selection

Executed orders are not a random sample of intended orders. Routers select venue and timing; risk rejects some states; large orders may be split; cancelled orders lack ordinary fill outcomes. Training on fills alone estimates cost conditional on historical execution and fill.

The dataset should retain submitted, rejected, cancelled, partially filled, and filled intents with policy version and market context. Counterfactual venue or size labels require causal assumptions or simulation and remain separate from observed outcomes.

## 9.3 Features and latency

Admissible features can include observable spread, depth summaries, volatility, imbalance, recent trade flow, queue proxy, venue state, order type, size relative to liquidity, session, and measured latency. Each is point-in-time and venue-specific. Aggregated bars cannot support claims about order-book features they do not contain.

## 9.4 Evaluation

Evaluate conditional bias, quantile coverage, tail error, fill probability, cost by size and state, temporal transfer, venue transfer, and decision utility. Underprediction in stressed liquidity may matter more than average error. Baselines include fixed spread, historical bucket averages, and transparent monotone models.

## 9.5 Use

Book VIII supplies venue semantics and execution policy. Book VI supplies fitted cost distributions and uncertainty. Book V can inject frozen model versions into simulations. Book VII can use conservative cost evidence in capacity and allocation. None of these consumers should use a point forecast without its uncertainty and support.

> **ML rule B6-ML09 — Cost models inherit routing selection**  
> A learned execution-cost estimate is conditional on the policies and market support that generated its training orders unless transport is independently established.

## Source note

This chapter defines ML responsibilities for cost estimation. Empirical microstructure, routing, and venue mechanics belong to Book VIII.
