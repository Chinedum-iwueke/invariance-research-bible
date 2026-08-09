<a id="b6-c02"></a>
# Chapter 2 — Problem Formulation Before Model Choice

A model is downstream of a decision problem. Formulation fixes what is observed, predicted, acted upon, and evaluated before algorithm choice can exploit accidental structure.

## 2.1 The formulation object

The canonical object records unit of analysis, population, decision and prediction times, information set, target and horizon, action or consumer, loss and utility, costs, constraints, sample construction, censoring, missingness, evaluation environments, uncertainty requirement, and abstention behavior.

For a trade-quality model, the unit might be a registered entry opportunity rather than executed trades. Training only on executed trades conditions on the historical policy and can hide rejected or unobserved opportunities.

## 2.2 Target choice

Return, direction, volatility, fill probability, slippage, drawdown contribution, and survival are different targets. A binary label such as “profitable” discards magnitude and depends on cost, horizon, exit, and path rules. A regression target may have heavy tails and changing scale. Ranking can be more stable than point prediction when only order matters.

The target’s earliest availability time must be later than its full construction horizon. Overlapping horizons create dependent observations and influence split and uncertainty design.

## 2.3 Loss and utility

Training loss approximates the desired statistical property: squared error targets a conditional mean under its assumptions; quantile loss targets a conditional quantile; log loss evaluates predictive distributions; ranking losses emphasize order. Business utility may be asymmetric, state-dependent, and constrained.

The model is selected on registered scientific and decision metrics, not on a convenient default loss alone. Post-hoc threshold selection is another search and belongs to the trial history.

## 2.4 Availability and latency

A feature can be historically present and operationally unavailable. The formulation records source publication, computation time, permissible staleness, failure fallback, and decision deadline. A model that needs data arriving after the order deadline solves the wrong problem.

## 2.5 Sample selection

Sampling defines the estimand. Event-based samples overweight active states differently from clock-based samples. Filtering on future liquidity, complete outcomes, or current universe membership biases the population. Negative examples need a defensible opportunity definition rather than arbitrary timestamps.

## 2.6 Formulation review

Independent review asks whether the prediction changes a real decision, whether a deterministic rule already suffices, whether target leakage is structurally possible, whether the metric rewards the desired behavior, and whether an abstention path exists.

> **ML rule B6-ML02 — The estimand precedes the estimator**  
> Model search may vary estimators within a registered formulation; changing population, target, horizon, or utility creates a new scientific problem.

## Source note

This chapter develops Book I’s question-first doctrine and Book IV’s hypothesis contract for learned estimators. Label execution belongs to Book V; allocation utility belongs to Book VII.
