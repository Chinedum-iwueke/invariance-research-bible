<a id="b6-c03"></a>
# Chapter 3 — Causal Datasets, Labels, and Splits

An ML dataset is a temporal construction, not a matrix found in storage. Each row needs population membership, feature availability, target availability, lineage, and a split role that respects the decision process.

## 3.1 Row contract

For row (i), record entity or event identity, observation time (t_i), decision time (d_i), feature-source times, label interval ([a_i,b_i]), label availability, universe membership, sampling weight, and group or episode identity. Fitted feature state references its training cutoff.

Rows whose label intervals overlap are statistically dependent even when their timestamps differ. Multiple rows from one episode or instrument can leak shared path information across random folds.

## 3.2 Temporal splits

The default evaluation respects chronology. Training precedes validation; protected test evidence follows model and threshold selection. Rolling or expanding origins reveal sensitivity to history and retraining cadence. Gaps or embargoes separate folds when label horizons or feature construction overlap boundaries.

No split rule is universally correct. The gap must follow the actual information overlap, not a ritual constant. Cross-sectional models may require time-blocked splits that keep all entities at a timestamp together.

## 3.3 Causal availability

Point-in-time joins use what was knowable, not the latest database value. Revisions, publication lags, corporate actions, delistings, and universe changes retain effective and availability times. Feature and label builders emit source-time diagnostics that Book V can validate.

“Causal dataset” here means causally available for prediction. It does not imply that the dataset identifies a causal effect. Causal inference requires explicit assumptions and design.

## 3.4 Protected evidence

Search workers receive training and validation partitions according to charter. Test or holdout access is an attributable event. Once exposed, that evidence cannot be treated as untouched for later variants. Repeated rolling evaluation may be operationally realistic while still accumulating selection information.

## 3.5 Dataset diagnostics

Before fitting, inspect missingness by time and state, target prevalence, label censoring, sample weights, dependence, duplicates, feature availability lag, support changes, and split comparability. Diagnostics are computed without leaking protected outcomes into design choices.

> **ML rule B6-ML03 — Splits follow information, not rows**  
> Two records belong on opposite sides of an evaluation boundary only when the training side cannot acquire outcome or fitted-state information from the evaluation side.

## Source note

This chapter extends Book V’s representation and label contracts and Book III’s lineage rules. It distinguishes temporal availability from causal identification as defined in [Pearl 2010](../../../bibliography/references.md#pearl-2010-causal-inference).
