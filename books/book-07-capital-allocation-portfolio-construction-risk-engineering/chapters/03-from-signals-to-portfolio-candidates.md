<a id="b7-c03"></a>
# Chapter 3 — From Signals to Portfolio Candidates

A research candidate becomes a portfolio candidate only after its forecast, uncertainty, costs, capacity, dependencies, operational state, and authorization are expressed in a common interface.

## 3.1 Candidate object

The object contains strategy and model version, authorized environment, instrument universe, forecast distribution and horizon, proposed exposure direction, uncertainty, expected turnover and holding time, cost and capacity curves, risk exposures, scenario behavior, data and system dependencies, current support, and expiry.

Historical performance is evidence behind the object, not the object itself.

## 3.2 Normalization

Signals arrive as scores, probabilities, expected returns, ranks, rules, or target positions. They are normalized into comparable forecast or utility units with explicit calibration. A z-score from one strategy is not commensurate with another without a reference distribution and stability evidence.

## 3.3 Eligibility

Eligibility requires scientific admission under Book II, current data and model support, executable instruments, cost and capacity evidence, operational qualification, and no active quarantine. Eligibility does not guarantee allocation.

## 3.4 Netting and conflicts

Strategies can request opposing exposure in one instrument. The portfolio layer distinguishes gross strategy intent from net executable position. Netting may reduce external cost while preserving internal attribution and risk budgets. Conflict policy considers mechanism, horizon, priority, and mandate rather than deleting one signal silently.

## 3.5 Attribution

Every target position retains forecast contributors, allocator version, constraints, cost estimate, and rounding. Later P&L attribution separates forecast, sizing, interaction, execution, and residual effects.

> **Risk rule B7-RK03 — Admission is not allocation**  
> Scientific validity grants eligibility for portfolio consideration; capital is assigned only after comparable forecasts, joint risk, costs, capacity, constraints, and operational state are evaluated.

## Source note

This chapter connects Books II and VI to the portfolio boundary. Execution netting and order semantics belong to Book VIII.
