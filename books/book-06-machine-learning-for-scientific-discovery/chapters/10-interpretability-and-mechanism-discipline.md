<a id="b6-c10"></a>
# Chapter 10 — Interpretability and Mechanism Discipline

Interpretability helps investigators understand model behavior, debug data and implementation, detect unsupported reliance, and generate hypotheses. It does not automatically explain the market process that produced the data.

## 10.1 Three questions

Distinguish:

1. **model behavior:** which inputs change this fitted model’s output;
2. **data association:** which variables co-vary with target or errors in the sample; and
3. **mechanism:** which intervention or process generates the relationship.

Feature attribution primarily addresses the first under a method-specific reference. It may reflect correlated proxies, representation choices, or extrapolation.

## 10.2 Global and local evidence

Global diagnostics include permutation or ablation effects, partial dependence under support checks, monotonicity, interaction summaries, and surrogate fidelity. Local diagnostics include counterfactual perturbations, neighbor retrieval, gradients, paths, or additive attributions.

Every method states its baseline, perturbation distribution, correlation handling, and stability. Local explanations that vary sharply across seeds or harmless reparameterizations are weak evidence.

## 10.3 Mechanism workflow

An explanation can propose a mechanism. The proposal then receives alternatives, temporal predictions, negative controls, intervention or quasi-experimental design where possible, and out-of-environment tests. Predictive persistence across environments can support—but not prove—mechanistic interpretation.

## 10.4 Debugging

Interpretability is especially valuable for detecting leakage, identifier memorization, stale or revised fields, concentration in one symbol, dependence on missingness, and implausible monotonic response. These findings can invalidate a model before performance is considered.

## 10.5 Human factors

Readable narratives can create unjustified trust. Reviewers see raw diagnostics, counterexamples, support, and uncertainty alongside any generated explanation. Model-generated rationales are not evidence of the computation’s actual causal path.

> **ML rule B6-ML10 — Explanation methods explain models first**  
> A model attribution becomes a market-mechanism claim only through a separate scientific argument and evidence program.

## Source note

This chapter applies Book I’s mechanism discipline and Book IV’s competing-explanation process to learned models. Causal inference remains governed by explicit designs such as those distinguished in [Pearl 2010](../../../bibliography/references.md#pearl-2010-causal-inference).
