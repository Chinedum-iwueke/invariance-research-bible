<a id="b4-c10"></a>
# Chapter 10 — Symbolic Regression and Program Search

Symbolic regression searches for explicit expressions that relate observations to outcomes. Program search generalizes the idea to decision rules, transformations, mechanisms, and experiment components. The output can be interpretable and generative, but a concise equation selected from a large search remains a selected empirical model.

## 10.1 Expression spaces

The grammar defines terminals, constants, operators, types, units, time semantics, state, and composition limits. Candidate expressions carry syntax-tree identity, canonical form, lineage, complexity, and execution cost.

Unsafe operations specify behavior for division near zero, logarithms, missing data, overflow, discontinuity, and non-finite output. Protected operators can stabilize execution but change mathematical meaning and must be explicit.

## 10.2 Objectives

Objectives can combine predictive loss, uncertainty, complexity, stability, invariance, novelty, turnover, and computational cost. Combining them into one fitness function encodes preferences; multi-objective search can expose trade-offs instead.

Complexity penalties control search and operational burden. They do not prove that the simplest surviving expression is the true mechanism.

> **Discovery rule B4-DR10 — Formula discovery remains model selection**  
> An equation or program found through search retains its complete search lineage and must earn independent predictive, explanatory, or causal status under the corresponding claim contract.

## 10.3 Symbolic scientific discovery

Schmidt and Lipson demonstrated a symbolic-regression approach that recovered compact relationships from experimental dynamical-system data ([Schmidt and Lipson, 2009](../../../bibliography/references.md#schmidt-lipson-2009)). The result is an important example of search over free-form expressions, not evidence that market mechanisms are recoverable from price data in the same way.

Market observations are partial, adaptive, noisy, selected, and affected by costs and strategic response. A discovered expression can encode a data artifact or regime. Domain assumptions and prospective evidence remain necessary.

## 10.4 Equivalence and simplification

Algebraic simplification and dimensional checks help identify duplicates and invalid expressions. Numerical equivalence on a sample cannot prove symbolic equivalence; symbolic equivalence under assumptions may not imply identical behavior under finite precision, missingness, or operational state.

Simplification creates a derived program version with a proof or tested equivalence record. It cannot silently replace the evaluated implementation.

## 10.5 Program synthesis

Program search can combine typed transforms, conditions, aggregations, and state machines. Each program is sandboxed with resource, determinism, side-effect, and tool restrictions. Search programs cannot access sealed evidence or production interfaces.

Generated code passes static checks, property tests, point-in-time validation, deterministic replay, and independent review before producing admissible evidence. Passing tests establishes covered behavior, not scientific validity.

## 10.6 Interpretation and falsification

Candidate expressions are translated into scoped claims and possible mechanisms. Partial dependence, sensitivity, counterexamples, boundary probes, and simpler baselines help determine what the program uses. Interpretations remain inferences unless the design identifies them.

Independent evaluation compares the selected expression with its family, null simulations, alternative representations, and protected data. Failure remains linked to the grammar and search so later work does not rediscover the same artifact unknowingly.

## Source note

This chapter applies Chapter 7’s typed languages and Chapter 8’s search history to symbolic and program search. It cites Schmidt and Lipson as a bounded scientific example and does not generalize their experimental result to markets.
