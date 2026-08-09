<a id="b6-c15"></a>
# Chapter 15 — Reproducible ML Contracts

An ML artifact is reproducible only when data, code, environment, pipeline, fitted state, evaluation, and authorization are bound into a reconstructible package.

## 15.1 Model specification

The specification includes formulation identity; dataset and split manifests; feature and label schemas; representation and transformer versions; estimator family; hyperparameter and seed policy; training procedure; loss; calibration and uncertainty procedures; evaluation metrics; search history; support; operational requirements; and prohibited uses.

## 15.2 Training run bundle

The bundle preserves resolved pipeline configuration, code pin, dependency lock and hardware compatibility class, input digests, fitted transformer and estimator artifacts, logs, checkpoints where relevant, fold predictions, metrics, calibration objects, diagnostics, lineage, and status. Failed trials remain visible.

Model serialization is not a complete environment. Loading is tested in a clean supported runtime. Unsafe executable serialization formats are controlled, signed, scanned, and isolated.

## 15.3 Prediction contract

Inputs have schema, units, availability, null and range policy. Outputs have target, units, horizon, calibration, uncertainty, abstention and error semantics. The contract declares deterministic tolerance, batching behavior, latency envelope, and behavior on unknown categories or support violations.

## 15.4 Model card and evidence dossier

The model card summarizes intended use, population, data, method, performance, calibration, robustness, fairness or mandate considerations where applicable, limitations, monitoring, and ownership. The evidence dossier links primary artifacts and opposition; it is not marketing prose.

## 15.5 Registry states

Models progress through candidate, validated, shadow-authorized, operationally qualified, production-authorized, demoted, quarantined, retired, and superseded states under Book II. Registry version and deployment state remain separate from scientific confidence.

> **ML rule B6-ML15 — The model is the governed package**  
> Weights without their data, transforms, contract, evaluation, environment, and lineage are not an admissible institutional model.

## Source note

This chapter integrates Books II, III, and V into an ML-specific artifact contract. Service construction belongs to Book X.
