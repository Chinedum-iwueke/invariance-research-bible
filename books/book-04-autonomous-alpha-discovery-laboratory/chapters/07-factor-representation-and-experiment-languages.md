<a id="b4-c07"></a>
# Chapter 7 — Factor, Representation, and Experiment Languages

Search becomes governable when candidate objects are expressed in typed languages with explicit time, units, domains, and complexity. A research language is not a promise that every expressible program is meaningful; it defines what can be generated, validated, executed, and recorded without hidden interpretation.

## 7.1 Language layers

The laboratory separates three languages:

- a **representation language** transforms causally available observations into typed state;
- a **factor or signal language** expresses candidate predictive quantities and decision-time scores;
- an **experiment language** defines populations, comparisons, metrics, uncertainty, costs, and validation procedures.

Separation permits the same representation to support several hypotheses and prevents an experiment specification from smuggling future data into a factor.

## 7.2 Type and time systems

Every expression carries data type, units, instrument and venue domain, sampling basis, event and availability semantics, fit state, missingness behavior, and lookback. Operators declare how they transform each property.

The compiler rejects unit mismatch, undefined alignment, future access, ambiguous universe membership, and unsupported operator composition. Static validation reduces defects but cannot prove scientific validity.

> **Discovery rule B4-DR07 — Expressibility is not admissibility**  
> A syntactically valid research program becomes admissible only after its provenance, causal availability, scientific rationale, search family, and experiment contract satisfy the applicable controls.

## 7.3 Operator governance

Operators have identity, definition, parameters, determinism, fit behavior, numerical properties, cost, tests, and version. A change in semantics creates a new version and invalidates incompatible cached artifacts.

Powerful operators such as cross-sectional ranking, group neutralization, adaptive filtering, learned transforms, and conditional branching receive explicit leakage and selection tests. User-defined functions enter through a reviewed extension contract.

## 7.4 Complexity and canonical form

Complexity budgets can limit tree depth, operator count, parameter precision, lookback, state, and compute. They reduce search and operational risk but do not define truth. A real mechanism can be complex; a simple expression can be spurious.

Canonicalization identifies algebraically or operationally equivalent expressions where rules justify it. Hash equality proves identical canonical representation, not equivalent economic behavior under every environment.

## 7.5 Experiment language

Experiment expressions reference immutable datasets, representations, trial families, split policies, estimands or targets, metrics, diagnostics, cost models, and artifact requirements. Defaults are explicit and versioned. Missing choices cannot be filled silently by a worker after results appear.

The language records cheap screens and full evaluations as different stages. Early-stage metrics cannot be presented as final evidence.

## 7.6 Portability and handoff

Language specifications are market-agnostic where semantics permit; crypto-specific operators declare venue and contract assumptions. Bulletproof BT provides deterministic interpreters or compiled execution under Book V. Book VI supplies learned operators. Book X implements registries and services.

## Source note

This chapter develops the typed-object and representation doctrine of Books I–III into discovery-language requirements. Concrete DSL syntax is an implementation design owned jointly by Books V and X.
