<a id="b4-c08"></a>
# Chapter 8 — Search Spaces and Search Histories

A reported candidate is selected from a larger set of questions, representations, methods, parameters, samples, and interpretations. The evidential problem depends on that selection process, not just the final trial count. Book IV represents both the intended search space and the realized search history.

## 8.1 Search-space contracts

A search-space contract identifies object type, grammar or parameter domain, conditional dependencies, constraints, priors or proposal weights, fidelity levels, budgets, objectives, stopping, and protected evidence. Continuous, discrete, combinatorial, and program spaces remain distinct.

The declared space can be broader than the realized search. If workers expand it, the amendment and evidence already observed are recorded.

## 8.2 Trials, configurations, and families

A configuration is one point or program in the space. A run executes an experiment for a configuration. A trial is a governed evaluation event. A family groups attempts connected by the question, selection process, shared evidence, or intended inference.

These objects are not interchangeable. Repeated seeds can be several runs of one configuration; many metrics can be several result views of one run; prompt changes can be material selection events without creating independent data.

> **Discovery rule B4-DR08 — Reconstruct selection**  
> Search history preserves enough proposal, execution, observation, adaptation, and selection events to reconstruct why the reported object was chosen from the alternatives that could have been reported.

## 8.3 Event history

The append-only history includes proposed and rejected configurations, scheduling, early stopping, failures, retries, parameter and grammar changes, result views, rankings, human and agent interventions, dataset and holdout exposures, selected candidates, and post-result interpretation.

Events identify causal order and shared dependencies. Aggregated dashboards remain projections over the event record.

## 8.4 Multi-fidelity search

Cheap screens can allocate resources efficiently using smaller samples, lower resolution, surrogate metrics, or simplified costs. Their relationship to final evidence is registered. A candidate selected by a cheap screen carries that selection into later interpretation.

Early stopping is a decision rule whose observations can bias survivors. The rule, checkpoints, censored runs, and resource allocation remain visible.

## 8.5 Deduplication and equivalence

Syntactic canonicalization, semantic metadata, result similarity, and shared lineage can identify redundant candidates. Deduplication reduces waste but does not erase attempts. Near-equivalence thresholds and collision errors are evaluated.

Novelty reports compare the candidate against both explicit prior work and generated alternatives. Search-space absence cannot prove conceptual novelty.

## 8.6 History as evidence

Search histories support selection-aware uncertainty, multiplicity methods, reproducibility, resource analysis, and failure retrieval. Counts alone are insufficient when tests are dependent or adaptively proposed.

Book II governs the Trial Registry and access. Book III stores the history. Book IV defines search semantics and statistical interpretation. Book V executes registered runs.

## Source note

This chapter develops Book I, Chapter 6, Book II, Chapter 8, and Book III, Chapter 13 into the discovery laboratory’s search-space and event-history contract.
