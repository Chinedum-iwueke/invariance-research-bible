<a id="b6-c16"></a>
# Chapter 16 — Promotion Evidence and Failure Modes

Promotion asks whether a frozen model package is scientifically useful and operationally safe for a named consumer and environment. It is not a reward for winning validation.

## 16.1 Evidence package

Required evidence includes formulation review; point-in-time dataset and split audit; baseline comparison; search history; protected confirmation; calibration and uncertainty; temporal and subgroup stability; support and abstention; cost-aware utility; sensitivity and adversarial tests; reproducibility; latency and resource behavior; monitoring; rollback; and independent critique.

Policy models additionally require action support, off-policy evaluation limits, simulator validation, hard constraints, and staged prospective evidence.

## 16.2 Failure taxonomy

Common failures include target or feature leakage; selection and survivorship bias; split contamination; unstable features; weak baseline; hyperparameter and seed overfit; miscalibration; unsupported extrapolation; concentration; proxy gaming; cost omission; latency infeasibility; serialization incompatibility; silent missing-value fallback; feedback loops; drift; and monitoring without response authority.

Scientific invalidity, negative evidence, operational failure, and security failure receive separate dispositions.

## 16.3 Challenge tests

Remove suspect features, shift future data, scramble identifiers, test simpler models, perturb costs and latency, exclude dominant periods or symbols, compare seeds, simulate missing inputs, stress support edges, and replay prospective data. A model that cannot explain a sharp collapse under these challenges is not ready.

## 16.4 Demotion and retirement

Promotion expires. Breached calibration, support, latency, data contract, or risk conditions can narrow use, increase abstention, demote, quarantine, or retire the version. Retraining does not erase the old evidence or incidents.

## 16.5 Acceptance

Book VI is complete when the institution can formulate an ML role; construct causal datasets; compare baselines and models; quantify uncertainty honestly; preserve search; detect shift; evaluate policy limits; publish reproducible packages; and prevent model output from bypassing governance, portfolio, or execution authority.

> **ML rule B6-ML16 — Promotion is use-specific and expiring**  
> Evidence authorizes one model version for a named consumer, population, horizon, action envelope, and monitoring contract—not “the model” in general.

## Source note

This chapter operationalizes Book II’s promotion and challenge regimes for ML. Scientific reproducibility follows [NASEM 2019](../../../bibliography/references.md#nasem-2019-reproducibility).
