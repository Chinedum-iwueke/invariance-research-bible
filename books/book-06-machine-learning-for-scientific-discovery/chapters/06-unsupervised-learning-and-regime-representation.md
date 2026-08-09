<a id="b6-c06"></a>
# Chapter 6 — Unsupervised Learning and Regime Representation

Unsupervised methods organize observations without a decision label. They can reveal compression, similarity, density, change, or recurring states. Their outputs are representation hypotheses, not discovered market truth.

## 6.1 Objectives define structure

Clustering depends on distance, scaling, number or prior over groups, density assumptions, and initialization. Principal components maximize variance under linear geometry. Autoencoders minimize a reconstruction objective. Change-point models define a transition and noise process. Different objectives produce different “regimes.”

The investigator states which distinctions the objective preserves and why they may matter.

## 6.2 Regime objects

A useful regime representation has identity, features, fit interval, assignment rule, update cadence, transition behavior, uncertainty, and semantic diagnostics. Hard labels are often less honest than membership probabilities or distances. Label names such as “risk-off” are interpretations that require independent evidence.

Future-fitted clusters cannot label past decisions. Online or rolling assignments use only fitted state available at the timestamp. Label switching across refits needs explicit alignment or new regime identities.

## 6.3 Stability

Evaluate resampling stability, seed sensitivity, temporal persistence, feature dependence, outlier influence, and transfer across instruments. A cluster can be stable and economically irrelevant; it can be useful and not stable enough to name as a persistent state.

Downstream performance segmented by clusters is exploratory unless registered independently. Choosing the clustering that best separates returns is supervised search in disguise.

## 6.4 Anomaly detection

An anomaly score describes distance under a reference distribution or model. It may identify data defects, rare market states, or model support failures. These cases need separate dispositions. Anomaly does not imply opportunity.

## 6.5 Use in science

Unsupervised outputs can form stratification variables, retrieval keys, candidate representations, monitoring summaries, or hypotheses about heterogeneity. They never authorize trading, quarantine, or capital changes by themselves.

> **ML rule B6-ML06 — A regime is conditional on its representation**  
> Regime labels remain model-versioned assignments with uncertainty and cannot be treated as observer-independent states of the market.

## Source note

This chapter extends Book IV’s anomaly and representation search. Institutional memory stores regime objects and lineage under Book III; portfolio stress use belongs to Book VII.
