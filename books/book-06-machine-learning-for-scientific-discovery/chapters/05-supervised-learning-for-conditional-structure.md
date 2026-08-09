<a id="b6-c05"></a>
# Chapter 5 — Supervised Learning for Conditional Structure

Supervised learning estimates a target from labeled examples under a chosen loss and hypothesis class. The scientific question is which conditional structure remains useful under realistic time, shift, and cost—not which algorithm wins an unconstrained leaderboard.

## 5.1 Model ladder

Evaluation proceeds through a ladder: constant and empirical baselines; linear or generalized linear models; regularized and monotone variants; trees and ensembles; kernels; sequence or deep architectures; and specialized mixtures only when justified. Each step retains the same dataset and evaluation contract.

The ladder reveals whether value comes from nonlinearity, interactions, memory, representation capacity, or merely changed preprocessing.

## 5.2 Conditional targets

Regression can estimate conditional means, quantiles, scale, hazards, or full distributions. Classification estimates a probability only when its scores are calibrated for the intended population and horizon. Ranking learns order, not cardinal utility.

Metrics match the object: proper scoring rules for distributions, calibration diagnostics for probabilities, pinball loss and coverage for quantiles, rank correlation or top-k utility for rankings, and decision curves for thresholds.

## 5.3 Dependence and weights

Financial observations are dependent, heteroskedastic, and unevenly informative. Sample weights may correct sampling design, emphasize economic exposure, or address class imbalance, but they change the target population. Weight definition and normalization are part of the estimand.

Repeated events from one market episode should not dominate uncertainty as if independent. Evaluation reports effective group counts and block-level variability.

## 5.4 Constraints and priors

Monotonicity, sparsity, symmetry, equivariance, or known bounds can improve sample efficiency and auditability when scientifically justified. They are hypotheses, not free regularization. A wrong invariant can prevent the model from representing real change.

## 5.5 Comparative evidence

Report distribution of performance across temporal folds, instruments, states, seeds, and plausible costs; calibration; error concentration; support coverage; complexity; latency; and failure behavior. A small stable improvement over a credible baseline can be more useful than a large unstable peak.

> **ML rule B6-ML05 — Complexity must identify its contribution**  
> A more expressive model is retained only when controlled comparisons show which decision-relevant property it improves and where that improvement fails.

## Source note

This chapter is a method framework rather than an endorsement of one estimator family. Search multiplicity remains governed by Book IV and execution by Book V.
