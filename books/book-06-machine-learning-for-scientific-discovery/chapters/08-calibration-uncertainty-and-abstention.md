<a id="b6-c08"></a>
# Chapter 8 — Calibration, Uncertainty, and Abstention

Decision systems need uncertainty objects whose meaning survives contact with the population and action. Raw model scores, ensemble spread, probability, prediction interval, and epistemic uncertainty are not interchangeable.

## 8.1 Calibration

A classifier is calibrated over a reference population when events assigned probability (p) occur at frequency (p) under the stated grouping and conditions. Calibration is evaluated out of sample with reliability curves, proper scores, and subgroup or temporal diagnostics. Small bins and adaptive binning create uncertainty of their own.

Temperature scaling and related post-hoc methods can improve calibration on held-out data, as demonstrated for modern neural networks by [Guo et al. 2017](../../../bibliography/references.md#guo-et-al-2017-calibration). That result is empirical and domain-dependent; a calibrator is another fitted artifact with its own split and drift.

## 8.2 Prediction sets and intervals

Conformal methods can provide finite-sample coverage under their stated exchangeability or related assumptions. [Vovk et al. 2017](../../../bibliography/references.md#vovk-et-al-2017-conformal) establishes validity for the studied predictive distributions under IID observations. Market time series do not automatically satisfy that condition.

Distribution shift can degrade both calibration and conformal coverage. [Podkopaev and Ramdas 2021](../../../bibliography/references.md#podkopaev-ramdas-2021-label-shift) studies classification uncertainty under label shift and develops reweighted procedures when target information is available. The institutional rule is to name the guarantee and its assumptions, never to say merely “distribution-free.”

## 8.3 Aleatoric and epistemic limits

Data noise and unresolved state create aleatoric uncertainty; limited support, parameter ambiguity, and model misspecification contribute epistemic uncertainty. Practical estimators mix them. Ensemble disagreement is a diagnostic, not a complete posterior.

## 8.4 Abstention

Abstention is a registered action with cost. The system can abstain when support is weak, uncertainty is high, inputs are stale, calibration fails, or operational constraints invalidate the prediction. Selective performance is reported against coverage; a model cannot appear excellent by acting only on a tiny favorable subset without accounting for selection.

## 8.5 Typed uncertainty

Every uncertainty object records target, population, horizon, confidence or coverage definition, method, calibration window, assumptions, evaluation, support diagnostics, and expiry. Consumers reject incompatible objects.

> **ML rule B6-ML08 — Uncertainty claims name their guarantee**  
> A probability, interval, or prediction set is communicated with its reference population, assumptions, calibration evidence, and failure under shift.

## Source note

Technical claims link to verified primary papers in the controlled bibliography. Decision and capital consequences belong to Book VII.
