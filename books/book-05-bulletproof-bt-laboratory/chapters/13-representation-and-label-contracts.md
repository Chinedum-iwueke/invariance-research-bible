<a id="b5-c13"></a>
# Chapter 13 — Representation and Label Contracts

Representations and labels can leak information or change the scientific question without touching the engine loop. The laboratory therefore executes them as versioned temporal contracts.

## 13.1 Representation contract

A representation contract states source fields, units, transformation graph, fit window, transform window, update cadence, warmup, missingness, clipping, cross-sectional membership, source-time policy, implementation version, and output schema. It declares whether state persists across sessions or instruments.

The pinned repository contains stateful indicators with `update(bar)` interfaces and explicit warmup behavior, online state features, feature schemas and stores, higher-timeframe context, and specialized research-panel loaders. Covered tests exercise streaming indicators, state layers, resampling, and hypothesis-specific feature logic.

Current implementation supports many deterministic handcrafted transforms and selected rolling fitted features. It is not a general proof that arbitrary feature code respects point-in-time boundaries.

## 13.2 Fit artifacts

Any fitted transform emits a fit artifact identifying training data, timestamps, parameters, algorithm, numeric library compatibility, and random policy. Transform execution references that artifact by digest. Refitting creates a new identity.

Precompute caches use keys that include the data and transformation dependencies capable of changing output. Cache hits and misses remain observable. A cache whose key omits fit cutoff can create silent leakage.

## 13.3 Label contract

A label states prediction target, origin time, horizon, event definition, censoring, overlap, path dependence, cost treatment, and earliest availability time. Trade outcome, maximum favorable excursion, barrier touch, future volatility, and regime labels answer different questions.

The repository enriches trades and constructs experiment datasets with identity and outcome fields. Some hypothesis families emit counterfactual or path diagnostics. These are post-event evidence unless a separate causal construction makes them admissible at decision time.

Labels never return to the strategy context for the same event. Dataset builders physically or logically separate feature-time fields from outcome-time fields and validate their clocks.

## 13.4 Learned representations

Book VI owns estimator choice, training, calibration, and model evaluation. Book V owns deterministic loading, admissible update scheduling, input and output schemas, fit lineage, and replay. A model file without its data and temporal contract is an incomplete laboratory input.

## 13.5 Representation equivalence

Changing candle boundaries, price adjustment, missing-value handling, normalization, or universe membership creates a new representation version. “Same indicator name” does not establish equivalence. Comparative experiments vary one representation contract intentionally and preserve the rest.

> **Laboratory rule B5-LR13 — Labels belong to the future they summarize**  
> Outcome-derived fields remain unavailable to decisions until their complete event horizon and publication policy permit use.

## Source note

Current statements derive from pinned indicator, feature-state, resampling, research-panel, hypothesis, trade-enrichment, cache, and dataset-extraction surfaces. Learned-method design belongs to Book VI.
