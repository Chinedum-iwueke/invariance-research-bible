<a id="b4-c09"></a>
# Chapter 9 — Random, Structured, Bayesian, and Evolutionary Search

Search algorithms allocate a finite evaluation budget across a registered space. They influence which configurations receive evidence and therefore belong to the experiment. No search method creates independent confirmation merely by finding a high-performing point efficiently.

## 9.1 Random and quasi-random search

Random search samples configurations from a declared distribution. It offers a transparent baseline, exposes the importance of each dimension, and can perform well when only a few dimensions matter. Its evidential interpretation depends on the sampling distribution and stopping rule.

Quasi-random sequences can improve space-filling properties in bounded continuous domains. They are deterministic designs under a seed or sequence specification, not random evidence. Conditional, constrained, and program spaces require valid sampling that does not distort intended weights silently.

## 9.2 Structured search

Grid, coordinate, beam, branch-and-bound, successive-halving, and domain-specific staged searches exploit known structure. Their pruning and ordering rules determine exposure. A candidate surviving several cheap screens has been selected adaptively even if the final evaluation is run once.

Structured search is valuable when operators have natural hierarchies, monotonic constraints, or known incompatibilities. It can be wasteful or misleading when the chosen structure excludes plausible alternatives.

> **Discovery rule B4-DR09 — Search policy is part of the design**  
> The proposal distribution, acquisition or selection rule, fidelity schedule, pruning, parallelism, stopping, and human interventions are versioned components of the registered experiment.

## 9.3 Bayesian optimization

Bayesian optimization maintains a surrogate over an expensive objective and uses an acquisition rule to choose evaluations. In a widely used formulation, a Gaussian-process surrogate represents uncertainty over performance and can account for variable evaluation cost and parallel experiments ([Snoek, Larochelle, and Adams, 2012](../../../bibliography/references.md#snoek-larochelle-adams-2012)).

The method’s effectiveness depends on representation of the space, surrogate assumptions, noise model, acquisition, initialization, and objective stability. Surrogate uncertainty is model uncertainty, not the uncertainty of the scientific claim. Adaptive objective observations remain part of selection.

Multi-objective or constrained variants can represent performance, turnover, robustness, complexity, and resource cost without forcing them into one arbitrary scalar. The resulting Pareto set still requires scientific and governance review.

## 9.4 Evolutionary search

Evolutionary search proposes populations through selection, mutation, recombination, and replacement. It is useful for irregular programs and mixed spaces but can produce extensive hidden multiplicity. Fitness, diversity, lineage, invalid offspring, and every evaluated generation remain recorded.

Elitism can concentrate early noise; mutation and crossover can destroy semantic validity; surrogate fitness can reward artifacts. Grammar and type systems constrain valid programs while independent evaluation protects against the search objective.

## 9.5 Parallel and asynchronous search

Parallel workers receive distinct configuration identities and cannot overwrite duplicates or failures. Asynchronous completion can bias proposal order toward cheap configurations; the scheduler and pending-evaluation treatment remain part of the policy.

Resource-aware acquisition can be appropriate, but a cost-efficient candidate is not scientifically superior by definition. Search value combines information, feasibility, and intended decision.

## 9.6 Comparison and handoff

Search algorithms are compared under common spaces, budgets, seeds or design sets, fidelity rules, and evaluation policies. Aggregate best score is insufficient; coverage, regret under the declared objective, diversity, failure rate, cost, reproducibility, and selection-aware final evidence matter.

The search phase proposes configurations. Confirmatory evaluation uses protected evidence under a separate contract. Book V executes runs; Book IV preserves the proposal process and interprets its consequences.

## Source note

This chapter develops the search-space contract in Chapter 8 and uses primary Bayesian-optimization literature for its technical characterization. Search methods are alternatives conditioned on space and objective, not a canonical algorithm hierarchy.
