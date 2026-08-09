<a id="b3-c09"></a>
# Chapter 9 — Query Planning and Hybrid Retrieval

A single search query rarely expresses the evidence needed for a scientific decision. Research Intelligence begins with the question, claim, and decision consequence, then decomposes them into evidence needs and retrieval paths. Search is an evidence-assembly process, not a contest for the most semantically similar passages.

## 9.1 Evidence-needs models

An evidence-needs model identifies which claims must be established, challenged, or bounded. Useful lanes can include definitions and theory, methodology, external empirical evidence, internal experiments, operational behavior, contradiction, prior failures, and novelty. These are defaults rather than mandatory empty boxes.

Each lane specifies eligible source and claim types, time and scope, authority, quality requirements, protected-access rules, and stopping conditions. Planning records the decision and does not encode its desired conclusion.

## 9.2 Retrieval methods

Hybrid retrieval assigns distinct roles to:

- lexical search for exact terms, identifiers, quotations, and rare notation;
- semantic search for paraphrase and conceptual similarity;
- structured search over source, claim, method, dataset, experiment, and decision fields;
- citation search across reference and support relationships;
- formula and symbol search;
- graph traversal across reviewed relationships;
- experiment and operational search over institutional lineage.

Exact identifiers and source coordinates are never overruled by embedding similarity. Each method reports its index, version, query, filters, and result scores or ranks.

> **Knowledge rule B3-KR09 — Retrieval follows evidence need**  
> Search strategy, source eligibility, ranking, and stopping criteria derive from the claims and decision being supported; relevance alone cannot establish authority, coverage, or evidential strength.

## 9.3 Fusion and reranking

Scores from different retrieval systems do not share a natural scale. Fusion uses calibrated or rank-based methods whose behavior is evaluated on relevant queries. Reranking considers claim scope, authority, source quality, directness of support, temporal applicability, redundancy, diversity, contradiction, and coverage.

Recency matters for mutable implementation, policy, venue, or empirical claims. It is not a universal preference over foundational mathematics or historical decisions. Prestige and citation count likewise remain contextual signals.

## 9.4 Coverage and stopping

Coverage asks whether the retrieved evidence addresses the necessary claims and alternatives, not whether a fixed number of documents was returned. Missing lanes and inaccessible sources remain visible. Redundant sources derived from the same data or publication chain do not create independent coverage.

Stopping can follow saturation of material claims, exhausted eligible sources, budget, deadline, or decision sufficiency. The dossier states the stopping basis and residual gap; it never implies that unobserved evidence does not exist.

## 9.5 Retrieval manifests

A retrieval manifest records the evidence-needs model, queries, indexes and versions, filters, candidate sets where retained, reranking, selected objects, expansions, exclusions, access denials, and timestamps. It enables replay against the recorded version and comparison with later systems.

Replay does not require current indexes to reproduce obsolete ranks. A retained snapshot or candidate manifest reconstructs the historical decision context while new indexes remain free to improve.

## 9.6 Evaluation boundary

Retrieval quality is measured against versioned judgments by source, domain, claim, and decision type. Recall, precision, support, contradiction coverage, diversity, latency, and cost can trade off. A universal recall target has no meaning without query strata and relevance definitions.

Chapter 18 governs formal evaluation. The operational requirement here is honest, reconstructible retrieval whose limitations survive synthesis.

## Source note

This chapter consolidates the Founder’s Edition, Chapters 14–16 (pp. 53–61), replacing one-query retrieval with decision-led evidence planning and versioned hybrid search.
