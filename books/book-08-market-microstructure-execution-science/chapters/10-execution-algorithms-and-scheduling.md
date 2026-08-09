<a id="b8-c10"></a>
# Chapter 10 — Execution Algorithms and Scheduling

Execution algorithms schedule quantity across time, venues, prices, and order types under risk and cost. Their output remains subordinate to parent intent and hard controls.

## 10.1 Baselines

Immediate execution, time-weighted schedules, volume-weighted schedules, participation rules, and simple passive-aggressive policies form the baseline ladder. Adaptive and learned policies compete under identical intents and market support.

## 10.2 Cost-risk tradeoff

[Almgren and Chriss 2001](../../../bibliography/references.md#almgren-chriss-2001) formalizes an execution frontier between expected transaction cost and volatility risk under specified impact dynamics. It is a foundational model, not a complete description of fragmented electronic venues.

## 10.3 Scheduling contract

Specify horizon, urgency, maximum participation, price and loss limits, passive tolerance, venue eligibility, cancel cadence, residual policy, and terminal behavior. The algorithm cannot extend horizon or risk without authorization.

## 10.4 Evaluation

Compare cost distribution, completion, opportunity cost, adverse selection, inventory path, tail latency, rejects, market participation, and stability. Selection-aware analysis includes unfilled and cancelled parents.

> **Execution rule B8-EX10 — The parent intent bounds adaptation**  
> An execution algorithm may adapt tactics within a registered envelope but cannot change economic quantity, risk, horizon, or venue authority on its own.

## Source note

The cost-risk frontier claim links to [Almgren and Chriss 2001](../../../bibliography/references.md#almgren-chriss-2001).
