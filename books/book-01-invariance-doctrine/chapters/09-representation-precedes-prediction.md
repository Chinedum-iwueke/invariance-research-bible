<a id="b1-c09"></a>
# Chapter 9 — Representation Precedes Prediction

Markets are not delivered to research as neutral tables. They are observed through venue messages, trades, quotes, books, reference data, clocks, identifiers, and transformations. Every dataset is already a representation: a selective construction that preserves some distinctions, suppresses others, and embeds assumptions about time, state, and comparability.

Prediction therefore begins before model fitting. It begins when the institution decides what an observation is.

## 9.1 Observation is constructed

A trade print, order-book update, candle, index level, funding rate, and portfolio return are different observational objects. None is the market itself. Each results from market rules, collection systems, timestamps, filters, aggregation, and conventions. Even a “raw” event stream has boundaries chosen by a venue and collector.

This does not make observation arbitrary. Representations can be evaluated against explicit purposes and invariants. A representation intended to study queue dynamics must preserve ordering and relevant event semantics. One intended for cross-venue comparison must reconcile instruments, units, clocks, and contract specifications. A daily bar may be adequate for one horizon and destructive for another.

The scientific error is to treat the representation as invisible. When a transformation becomes customary, its assumptions can disappear from the hypothesis while continuing to determine the result.

> **Doctrine B1-PR08 — Representation precedes prediction**  
> Every empirical claim identifies the causally available, versioned representation through which its object is observed; representation choice is part of the hypothesis.

## 9.2 A representation reveals and conceals

Aggregation can reduce noise and computation while erasing sequence, extremes, or path. Normalization can improve comparability while introducing future information if its parameters are fitted outside the permitted window. Imputation can support a model while converting absence into an invented value. A rolling statistic can expose local structure while adding delay and dependence.

No representation is universally faithful. Fitness is relative to the question, and losses should be named. A representation record states its source fields, time semantics, transformation, fit population, parameters, missingness policy, update rule, output schema, known invariants, and known distortions.

This applies to labels as strongly as features. “Future return,” “volatility,” “regime,” “fill,” and “drawdown” are constructed targets whose horizons, prices, costs, censoring, and accounting rules alter their meaning.

## 9.3 Causal availability

A field may exist in a historical database without having been knowable at the decision time. Revised reference values, finalized bars, backfilled constituents, corrected trades, and globally normalized features can carry future information backward.

Causal availability asks what the decision system could have observed, through which channel, at which timestamp, with which latency and revision state. The answer is an empirical and implementation property, not an assumption inferred from column names.

Point-in-time lineage therefore accompanies every material field. Laboratory systems enforce fit and transform boundaries; event simulation enforces observation and decision clocks. Book V owns those deterministic contracts, while Book VIII owns venue and execution semantics.

## 9.4 Representation hypotheses

A representation hypothesis states why a transformation should make a phenomenon observable while preserving information relevant to the claim. It identifies the expected benefit, likely loss, alternatives, and tests that can distinguish improvement from artifact.

Learned representations receive the same burden. An embedding or latent state is not exempt because its coordinates lack ordinary names. Its training information, objective, update cadence, stability, and downstream dependence remain part of the scientific object. Book VI develops these methods.

Comparison requires care. If many representations are searched and only the best is reported, representation selection is part of multiplicity. If preprocessing is tuned using the evaluation interval, the nominal holdout is no longer protected. If one representation changes the eligible sample, metric differences may reflect population changes rather than better information.

## 9.5 Invariance as a test, not a presumption

The institution’s name does not imply that useful representations are invariant by decree. Invariance is a question: which transformations preserve the relationship relevant to a decision, and under which changes of units, venue, scale, time, participant mix, or environment?

Some symmetries are definitional. Changing quote currency and units should not alter an economically equivalent calculation when conversions are correct. Other invariances are empirical and may fail. A signal stable across a narrow historical sample may depend on a venue rule or liquidity regime.

Tests of invariance should specify the transformation group, object preserved, tolerance, and scope. Stability across perturbations can strengthen a claim, but indiscriminate invariance can discard genuinely informative structure.

## 9.6 Representation failures

Representation defects often resemble discoveries. Timestamp misalignment creates lead–lag. Survivorship creates persistence. Sparse observations create artificial jumps. Contract rolls create returns that no holder earned. Price discreteness creates thresholds. A benchmark transformation can manufacture residual alpha.

The response is not to distrust every feature. It is to make representation criticism a first-class part of experiment review. Diagnostics trace surprising effects back through lineage, reproduce transformations independently, compare plausible alternatives, and test known invariants. A representation failure invalidates affected evidence; it does not automatically answer the underlying market question.

## 9.7 Representation as institutional property

Reusable representations are versioned scientific assets rather than private notebook fragments. Their definitions, fit state, code, tests, lineage, restrictions, and downstream consumers remain recoverable. A change that affects semantics creates a new version and triggers impact review.

Research Intelligence records the conceptual and evidential lineage. Bulletproof BT produces deterministic artifacts. Hermes governs approval and access. No agent or model runtime becomes the sole keeper of a transformation’s meaning.

Prediction is downstream of observation. When representation is explicit, a result can be criticized at the correct layer: market relationship, measurement, transformation, estimator, or decision rule. Without that separation, the institution may optimize a numerical artifact and call it discovery.

## Source note

This chapter revises the Founder’s Edition, Chapters 3 and 13 (pp. 24–33 and 138–148). Learned representations move to Book VI; deterministic fit, transform, and point-in-time contracts move to Book V; market-data semantics move to Book VIII.
