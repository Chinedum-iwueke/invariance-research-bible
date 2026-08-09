<a id="b5-c06"></a>
# Chapter 6 — Time, Causality, and No-Lookahead Rules

No-lookahead is not a slogan attached to a strategy. It is a system property spanning data retrieval, transformations, fitting, resampling, universe membership, decision order, execution, labels, caches, and post-run selection.

## 6.1 The time tuple

Every material observation should be interpreted through at least four times:

- **event time:** when the represented market event occurred;
- **source time:** when the value became available from its source;
- **decision time:** when the strategy was permitted to use it; and
- **evaluation time:** when the outcome becomes measurable.

Order submission, acknowledgement, fill, cancellation, and reconciliation add operational clocks. Bar backtests often compress them through configured delay and fill policy. That compression must be declared.

## 6.2 Current protections

The pinned core event types reject naive timestamps and expect UTC-aware values. Data validation enforces ordering. The strict higher-timeframe adapter reveals only completed buckets; its focused test withholds a spike until bucket rollover. Warmup observations update state while preventing trading. Truth validation rejects selected enriched source timestamps later than entry.

Hypothesis tests in the repository repeatedly exercise “two-clock” semantics for strategies that compute on a signal timeframe and monitor exits on a lower timeframe. These tests are evidence for their covered families, not a proof over arbitrary user code.

## 6.3 Common leakage channels

Leakage enters through more than indexing mistakes:

- fitting normalization or model parameters on the full sample;
- using revised fundamentals under their period end rather than publication time;
- resampling with an in-progress bucket;
- constructing a universe from future survival;
- filling gaps with future-aware interpolation;
- selecting features or parameters after viewing protected outcomes;
- reusing a cache whose key omits fit window or data version;
- labeling a trade with future path information and feeding that label back into entry logic; or
- reporting only the best branch of an adaptive search.

The last two are scientific leakage even when the engine loop is temporally correct.

## 6.4 Fit and transform

A transformation has a fit interval, fitted state identity, update cadence, transform interval, and permitted information set. Rolling estimates define whether the current observation enters the estimate before or after the decision. Expanding estimates define their origin and minimum history. Cross-sectional transforms define which instruments were knowable and eligible at the timestamp.

Learned models belong to Book VI, but Book V must enforce their temporal envelope. The engine should receive a frozen, versioned estimator or a deterministic update contract. It should never infer training policy from a serialized object alone.

## 6.5 Detecting violations

The target test suite includes perturbation tests: change future observations and verify earlier decisions remain identical; shift source timestamps beyond availability and verify rejection; compare serial and parallel execution; invalidate caches and compare recomputation; and replay resampling boundaries around sessions and daylight changes.

Static scans for negative shifts and full-sample fits are useful but incomplete. Causality tests need behavior.

> **Laboratory rule B5-LR06 — Future perturbations must not rewrite the past**  
> For any experiment prefix, changes confined to unavailable future information must leave prior admissible state and decisions unchanged.

## Source note

Current protections derive from pinned timestamp types, validation, warmup, resampling, hypothesis two-clock tests, and experiment truth validation. The broader causal contract extends Books I and IV.
