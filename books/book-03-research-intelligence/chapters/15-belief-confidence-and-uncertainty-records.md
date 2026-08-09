<a id="b3-c15"></a>
# Chapter 15 — Belief, Confidence, and Uncertainty Records

Institutional belief records what the organization currently judges about a scoped claim and why. It is neither constitutional doctrine nor operational permission. A belief can change without promoting a candidate; governance can authorize a reversible action while belief remains uncertain.

## 15.1 Belief records

A belief record contains claim identity and scope, assessment, supporting and opposing evidence, method of synthesis, uncertainty, dependencies, owner, reviewers, effective time, review date, invalidation conditions, and revision history.

Assessment can be qualitative, probabilistic, interval-valued, model-relative, or partially ordered. The type determines its interpretation. A generic confidence number is prohibited when its event, population, horizon, or calibration basis is undefined.

> **Knowledge rule B3-KR15 — Belief is typed judgment**  
> An institutional belief states its claim, scope, evidence, uncertainty semantics, reviewer, and validity interval; it never inherits authority mechanically from source prestige, model confidence, or workflow state.

## 15.2 Evidence updating

New evidence creates a revision event linking prior belief, new evidence, reasoning, resulting assessment, and remaining disagreement. Dependencies matter: ten analyses from one run do not count as ten independent updates.

A valid null may narrow uncertainty without materially changing the central assessment. A software defect can invalidate several earlier updates at once. A prospective contradiction may outweigh many adaptively selected historical variants.

## 15.3 Uncertainty records

Uncertainty records identify source—sampling, measurement, model form, parameter, environment, implementation, cost, dependency, or unresolved alternative—and representation such as distribution, interval, scenario, bound, sensitivity, or unknown state.

Aleatoric and epistemic labels are model-relative. Unknown unknowns cannot be enumerated conveniently; the system records model limits and observed surprise rather than false probabilities.

## 15.4 Confidence and calibration

Calibration applies only when belief records make comparable forecasts about defined events over defined horizons with known censoring and scoring. Brier or logarithmic scores apply to probabilistic forecasts, not qualitative labels.

Calibration is stratified by claim type and context. “Survival” is not a universal outcome: a scientifically supported claim can become economically obsolete, and a weak claim can remain deployed through luck or inertia.

## 15.5 Dissent and review

Minority assessments remain linked with their evidence and revisit conditions. A final institutional belief names the accountable synthesis but does not erase unresolved expert disagreement.

Expiry triggers review where evidence or environment is mutable. Historical belief remains reconstructible for decision audit.

## 15.6 Decision interface

Hermes consumes the belief record and evidence dossier as inputs to consequence-sensitive decisions. Candidate maturity, validation environment, operational state, and risk budget remain separate objects.

This separation permits action under uncertainty without pretending that action establishes truth, and revision of belief without granting action automatically.

## Source note

This chapter consolidates the Founder’s Edition, Chapters 24 and 28–31 (pp. 84–108), replacing universal confidence weights with typed, scoped belief and uncertainty records.
