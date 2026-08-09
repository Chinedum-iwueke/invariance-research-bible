<a id="b4-c03"></a>
# Chapter 3 — Representation Search

Representation search asks which causally available transformation makes a phenomenon observable for a specified question while preserving the distinctions the decision requires. Because representation can create leakage, change the eligible sample, or manufacture apparent robustness, it is part of the registered search family.

## 3.1 Representation candidates

A candidate representation declares source observations, time semantics, fit population, transformation, parameters, missingness, normalization, state, output schema, known invariants, information loss, computational cost, and intended claim.

Handcrafted and learned representations use the same envelope. Learned representations additionally preserve objective, architecture, training data, fit state, stochastic controls, and stability evidence.

## 3.2 Search spaces

Search may vary aggregation, sampling clock, horizon, normalization, basis, differencing, filtering, state variables, cross-sectional construction, event alignment, or learned encoding. The space is defined before privileged evaluation where confirmation is intended.

Unbounded composition can generate innumerable transforms with hidden dependence. A representation language therefore constrains valid types, time behavior, permissible operators, fit/transform semantics, and complexity budgets.

> **Discovery rule B4-DR03 — Representation search is registered search**  
> Every representation considered after observing result-bearing data is recorded with its family, lineage, exposure, and selection role; preprocessing is not exempt from multiplicity or holdout policy.

## 3.3 Evaluation dimensions

Representation evaluation includes causal availability, integrity, stability, information preservation, invariance appropriate to the mechanism, interpretability where needed, resource cost, downstream compatibility, and incremental predictive value.

Predictive performance alone can reward leakage or sample selection. Reproducing a transformation on point-in-time data and testing known invariants precede model comparison.

## 3.4 Fit and transform

Any transformation that learns parameters has explicit fit, freeze, transform, update, and invalidation boundaries. Normalization statistics, vocabularies, decompositions, clusters, embeddings, and feature selection cannot inspect evaluation data outside policy.

Updating creates a new representation version and triggers downstream impact. A historical dataset transformed using a later fitted state is not point-in-time evidence.

## 3.5 Comparative experiments

Comparisons hold population, target, availability, estimator, and evaluation policy fixed where the question requires. If a representation changes eligible observations, results report both common-sample and intended-sample behavior when meaningful.

Search reports response surfaces and boundaries rather than only the winning representation. A simpler transform can be preferred for stability, cost, or diagnosis, but simplicity is a decision criterion rather than a universal scientific law.

## 3.6 Handoff

Book IV defines and searches representation hypotheses. Book V executes deterministic fit and transform contracts. Book VI owns learned representation methods. Book III records concepts, evidence, lineage, and projections. Promotion follows Book II.

## Source note

This chapter operationalizes Book I, Chapter 9 and Book III’s Representation projection. It establishes search requirements without prescribing a universal transform family.
