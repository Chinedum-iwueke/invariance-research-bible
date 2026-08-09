<a id="b6-c07"></a>
# Chapter 7 — Meta-Labeling and Trade-Quality Estimation

A meta-model conditions a primary decision process rather than replacing its scientific identity. It may estimate whether to act, rank opportunities, choose among registered variants, or predict outcome distribution under a fixed primary policy.

## 7.1 The conditioning problem

The primary strategy defines opportunity time, direction, horizon, stop, exit, and base size or abstention. The meta-dataset includes all eligible opportunities, not only executed winners and losers. Its target is conditional on the primary policy and downstream execution contract.

If the historical primary policy filtered opportunities, missing counterfactual outcomes create selection bias. Reconstructing rejected opportunities requires replay under a declared model; it does not create observed fills.

## 7.2 Uses

Meta-models can estimate probability of a positive net outcome, conditional R distribution, adverse excursion, time to resolution, expected cost, or confidence that a setup belongs to the primary strategy’s supported region. Each target supports different action rules.

Thresholding a probability is a decision layer. Thresholds, class weights, and top-k policies are tuned inside protected evaluation and assessed after turnover and capacity effects.

## 7.3 Leakage risks

Trade-level features often contain future-enriched fields: realized volatility over the holding period, final stop distance, exit reason, path extrema, or post-trade regime. Field names are insufficient; lineage and source times decide admissibility.

Purging must account for primary-trade overlap. Randomly splitting episodes from the same market path can leak common outcome shocks.

## 7.4 Evaluation

Compare the primary policy alone, meta-policy with fixed threshold, simple transparent filter, and learned alternatives. Report coverage, abstention, calibration, turnover, cost, effect on missed winners and avoided losers, stability, and concentration. Improvement in precision can coexist with lower net utility if coverage collapses.

## 7.5 Authority

A meta-label never becomes a generic confidence score for capital. It is a calibrated estimate for a specific target, population, horizon, policy, and version. Book VII decides whether and how such an object may influence allocation.

> **ML rule B6-ML07 — Meta-models inherit the primary policy**  
> Changing the primary opportunity definition, execution contract, or downstream action invalidates transport of the meta-model unless re-established.

## Source note

This chapter refines Founder’s Edition meta-labeling concepts under Books IV–V’s hypothesis, label, and execution contracts. Capital use is deferred to Book VII.
