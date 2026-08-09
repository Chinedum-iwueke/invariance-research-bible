<a id="b1-c08"></a>
# Chapter 8 — Evidence, Uncertainty, and Belief

Evidence has force only in relation to a claim. Source prestige, numerical precision, and favorable outcomes cannot substitute for that relationship. A code trace can be decisive about implemented behavior and nearly irrelevant to whether a market mechanism exists. A paper can establish how a method was defined while providing weak support for its transfer to another venue. A profitable month can be operationally real while remaining scientifically ambiguous.

Invariance Research therefore rejects a universal evidence pyramid. It uses contextual authority: the strength and relevance of evidence depend on the claim, design, provenance, scope, independence, uncertainty, and decision consequence.

## 8.1 Evidence is claim-relative

An evidence record identifies the claim it bears on and the relationship by which it bears. It states whether it supports, weakens, contradicts, bounds, or merely contextualizes the claim. It also records source, method, population, time, representation, assumptions, limitations, and review state.

This structure prevents borrowed authority. Documentation is authoritative about an interface only at the documented version and only if implementation and tests do not contradict it. A controlled experiment may support a causal claim in its setting without establishing transport to a changing market. A backtest may support computational and historical propositions without becoming prospective evidence.

Different claims require different evidence. Implementation claims need code, schemas, tests, and observed artifacts. Mathematical claims need valid derivation under stated assumptions. Empirical claims need data and methods adequate to their estimand. Operational readiness needs exercised controls and observed environment behavior. Governance claims require adopted authority, not statistical significance.

> **Principle B1-PR07 — Claim-relative evidence**  
> Evidence is evaluated against the claim it can support, the uncertainty it carries, and the consequence of acting on it; no source type has universal authority.

## 8.2 Provenance and independence

Evidence without provenance cannot be weighed reliably. The institution preserves original sources, transformations, data snapshots or identities, code versions, parameters, environments, and authorship. Derived summaries link to the primary objects and declare where interpretation entered.

Apparent multiplicity is not independence. Ten reports derived from one dataset and one implementation are not ten independent observations. Two studies can share vendors, benchmark constructions, preprocessing code, or publication incentives. Evidence dossiers record dependency so that volume is not mistaken for corroboration.

Contradiction is preserved rather than averaged away. Disagreement may reveal scope, measurement differences, non-stationarity, or error. The task is to explain which conclusions remain warranted, not to force every source into a single score.

## 8.3 Reproducibility, replication, and prospective evidence

Computational reproducibility asks whether the same data, code, methods, and conditions yield consistent computational results. Replicability asks whether new data aimed at the same scientific question produce consistent results. The National Academies distinguishes these concepts and notes that non-replication can have many causes rather than serving as an automatic verdict ([NASEM, 2019](../../../bibliography/references.md#nasem-2019-reproducibility)).

For market research, both matter and neither is sufficient. A perfectly reproducible backtest can reproduce leakage. A replication across instruments can reproduce a shared artifact. Prospective evidence adds temporal separation: the claim and decision rule are fixed before later observations arrive. Execution replay, demo, shadow, micro-live, and production address different scientific or operational questions; their meanings are controlled by the series architecture.

Evidence strength is multidimensional. Useful dimensions include temporal separation, independence, ecological relevance, control of confounding, data integrity, implementation fidelity, sample information, search exposure, and reproducibility. Collapsing them into one rank can hide a decisive weakness.

## 8.4 Uncertainty is typed

Uncertainty is not a decorative interval around a point estimate. It can arise from sampling, measurement, model form, parameter estimation, regime change, implementation, costs, execution, dependency, or ignorance of relevant alternatives. Some uncertainty is expressed probabilistically; some is represented by scenarios, bounds, unresolved assumptions, or an explicit unknown state.

The common distinction between aleatoric and epistemic uncertainty can be useful, but it is model-relative. What appears irreducible under one representation may become explainable under another; what appears reducible may remain inaccessible at the required horizon or cost. The institution records the source and meaning of uncertainty rather than assuming a universal two-bin decomposition.

Unknown is a legitimate result. A design can be unable to distinguish explanations, a dataset can be too weak, or a decision can be underdetermined. Precision in reporting ignorance is more valuable than a confident answer manufactured by an arbitrary model.

## 8.5 Belief is governed and revisable

An institutional belief is a versioned assessment of a scoped claim. It records evidential basis, uncertainty, contradictions, applicable conditions, review state, and revision history. It differs from constitutional doctrine, which changes through governance, and from promotion state, which authorizes operational progression. A candidate may have moderate epistemic support yet remain ineligible for capital because controls are incomplete.

Belief is not necessarily a scalar probability. Some claims admit calibrated probabilities; others require intervals, partial orderings, qualitative states, or sets of plausible models. When probabilities are used, the event, horizon, information set, and calibration population are specified. Confidence language does not borrow the meaning of a frequentist confidence interval, Bayesian credible interval, or predictive coverage statement.

Revision adds an attributable event. It does not overwrite the prior belief. The institution must be able to reconstruct what was believed at a decision time and which later evidence changed it.

## 8.6 Evidence thresholds depend on consequence

The evidence required to continue exploration is lower than the evidence required to expose capital, change a constitutional rule, or make an irreversible operational decision. This is not permission to call weak evidence strong. It is a recognition that decisions have different costs, reversibility, and failure modes.

A cheap reversible experiment may proceed under substantial uncertainty if it protects holdouts and records search. Production promotion requires evidence about net economics, operational controls, risk, monitoring, and failure handling. A safety stop may be justified by asymmetric loss before a complete causal diagnosis exists.

Governance specifies the decision and threshold; evidence supplies the warranted claim. Neither a model score nor a statistical test can assume decision authority.

## 8.7 Updating without false precision

New evidence changes belief according to its relevance and dependence, not merely its direction. A prospective contradiction may outweigh many variants of the same backtest. A software defect may invalidate a family of prior results. A replication failure may narrow scope rather than erase the original observation.

Updates should distinguish three questions: did the observation occur; is the proposed relationship supported; and should the institution act? Conflating them produces familiar errors. Profit proves that profit occurred under an accounting convention, not that the mechanism is correct. Statistical association supports dependence under a design, not causal identification. Scientific support does not by itself establish portfolio suitability.

Research Intelligence preserves evidence and belief lineage. Review bodies evaluate it. Portfolio and risk authorities decide exposure. The separation allows beliefs to change without silently changing authority.

## 8.8 Honest evidence is institutional strength

An evidence system should make the strongest objection easy to find, the primary artifact easier to reach than its summary, and uncertainty harder to omit than to report. It should reward correction without treating perpetual skepticism as rigor. Decisions must still be made, but their premises and residual risks remain visible.

The institution earns confidence through traceability, criticism, replication where meaningful, prospective observation, and calibration over time. It does not claim certainty from ceremony. Evidence remains conditional, beliefs remain revisable, and decisions remain accountable to the knowledge available when they were made.

## Source note

This chapter revises the Founder’s Edition, Chapters 11 and 24 (pp. 112–123 and 290–302), with evidence doctrine from Chapters 2 and 28. Book III owns evidence, belief, provenance, and uncertainty records; Books II and V own decision gates and laboratory evidence production.
