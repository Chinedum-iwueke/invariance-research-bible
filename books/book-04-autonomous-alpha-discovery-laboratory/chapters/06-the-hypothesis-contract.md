<a id="b4-c06"></a>
# Chapter 6 — The Hypothesis Contract

The hypothesis contract is the registration-ready scientific object that binds a question to evidence before privileged evaluation. It makes scope, representation, alternatives, search, and failure conditions explicit enough for deterministic experiment execution and independent review.

## 6.1 Required fields

The contract records:

- question, claim type, and decision relevance;
- population, market, venue, instruments, and effective scope;
- mechanism or predictive rationale and credible alternatives;
- information set and decision time;
- representation, target, horizon, and benchmark;
- expected effect, ordering, dependence, or qualitative implication;
- null or comparison models where applicable;
- data eligibility and point-in-time policy;
- experiment family, metrics, diagnostics, and uncertainty method;
- costs, execution assumptions, and known constraints;
- search budget, selection rule, stopping, and holdout policy;
- falsification, invalidity, amendment, and closeout conditions.

The contract links canonical identities rather than copying mutable descriptions wherever possible.

## 6.2 Claim classes

Predictive contracts state information and outcome distributions. Explanatory contracts state mechanism implications. Causal contracts state intervention, counterfactual, identification assumptions, and estimand. Engineering contracts can test correctness, latency, reliability, or safety without inventing a market hypothesis.

The form adapts to the claim. A universal statistical null is not mandatory, but every contract identifies what evidence would weaken its assertion.

> **Discovery rule B4-DR06 — Commit before privilege**  
> The hypothesis contract and its permitted search are immutable before access to the evidence designated for their independent evaluation; later changes are attributable amendments or new contracts.

## 6.3 Representations and timing

Representation is part of the claim. The contract references its fit and transform state, availability semantics, missingness, universe formation, and version. The target defines prices, costs, censoring, and accounting.

Temporal policy distinguishes event, receive, availability, decision, label start, and label end times as applicable. An experiment cannot infer availability from a historical column’s presence.

## 6.4 Falsification and invalidity

Failure conditions specify effect magnitude, uncertainty, discriminating predictions, stability, cost, or prospective outcomes that would weaken the claim. Invalidity conditions specify leakage, corrupted data, implementation failure, unauthorized evidence access, or contract violation.

The distinction prevents invalid runs from falsifying a hypothesis and prevents unfavorable valid evidence from being dismissed as engineering failure.

## 6.5 Amendments

An amendment states what changed, why, what evidence had been observed, who authorized it, and how interpretation changes. Material changes to target, representation, sample, metric, search, or mechanism create a new contract version or trial family.

Exploratory findings can motivate a confirmatory contract. Their origin remains linked so novelty and selection are assessed honestly.

## 6.6 Execution and review interfaces

Bulletproof BT receives an executable experiment specification derived from the contract and returns primary artifacts. Research Intelligence stores the contract, evidence, and lineage. Hermes enforces registration, access, budgets, and review. The hypothesis contract does not itself grant execution or promotion authority.

## Source note

This chapter operationalizes Book I, Chapter 7 and Book II, Chapter 8. Book V owns executable experiment schemas; this chapter owns the scientific contract from which they are derived.
