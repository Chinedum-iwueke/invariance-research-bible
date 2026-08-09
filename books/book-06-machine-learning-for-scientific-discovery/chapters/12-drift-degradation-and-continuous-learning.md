<a id="b6-c12"></a>
# Chapter 12 — Drift, Degradation, and Continuous Learning

Model behavior can degrade because inputs, targets, relationships, calibration, support, costs, or infrastructure change. “Drift” is a diagnosis class, not one scalar alarm.

## 12.1 Drift taxonomy

Monitor data quality and schema; marginal feature distribution; joint feature support; target prevalence and scale; conditional relationship; residuals; calibration; selective coverage; decision distribution; realized cost; latency; and upstream representation versions. A change in prediction distribution may be correct adaptation rather than failure.

## 12.2 Delayed outcomes

Labels often arrive after decisions and may be censored. Monitoring separates immediate input and support checks from delayed performance and calibration checks. Proxy metrics cannot silently replace outcomes.

## 12.3 Detection

Tests and detectors specify reference window, current window, statistic, dependence handling, multiplicity, threshold, minimum effect, and expected false-alarm behavior. Visual dashboards support diagnosis but do not authorize retraining.

Segment monitoring matters: aggregate stability can hide degradation in a costly state, while small segments can generate noisy alarms.

## 12.4 Response ladder

Responses include observe, investigate, narrow support, increase abstention, recalibrate, shadow a challenger, retrain under a registered contract, demote, quarantine, or retire. Severity reflects decision consequence and uncertainty, not just statistical significance.

Continuous learning means repeated governed model releases. Online updating requires deterministic update order, bounded parameters, rollback, shadow comparison, and preservation of every model state. It is not unrestricted self-modification.

## 12.5 Feedback loops

Predictions and policies change which data are observed. A filter suppresses opportunities; routing changes fills; allocation changes impact. Monitoring records policy versions and exposure so the institution does not interpret policy-induced selection as exogenous market drift.

> **ML rule B6-ML12 — Retraining is a promotion event**  
> A newly fitted model version does not replace an authorized version until its data, search, validation, shadow evidence, and rollback conditions pass the required governance.

## Source note

This chapter specializes Book I’s non-stationarity doctrine and Book II’s promotion state machine. Venue drift belongs to Book VIII and deployment monitoring to Book X.
