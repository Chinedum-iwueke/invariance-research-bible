<a id="b3-c14"></a>
# Chapter 14 — Knowledge and Projection Graphs

Graphs make relationships among scientific objects queryable, but graph structure is not truth. Research Intelligence builds access-controlled projections over the canonical evidence core. A projection answers a class of questions while preserving the provenance and type of every node and edge.

## 14.1 One core, many projections

Useful projections include knowledge, methods, representations, questions, opportunities, confidence, uncertainty, memory, learning, environmental evolution, predictive edges, and mechanisms. They are views, not independently mutable stores.

A source correction, access change, or invalidation propagates through affected projections. Rebuilds can change rankings and neighborhoods while retaining semantic compatibility and version history.

## 14.2 Edge semantics

Edges are typed as:

- **observed** — directly present in a source or primary artifact;
- **deterministically derived** — produced by an explicit reproducible rule;
- **statistically estimated** — accompanied by estimator, data, uncertainty, and scope;
- **reviewed inference** — accepted institutional interpretation linked to premises;
- **agent-proposed inference** — unaccepted candidate relationship.

Visual and query interfaces must not render these as equivalent. Confidence in an edge is typed and scoped, not inherited from the number of connected nodes.

> **Knowledge rule B3-KR14 — Connectivity is not evidence**  
> Centrality, path length, similarity, community membership, and multi-hop plausibility may generate questions; they cannot establish a scientific claim without the underlying evidence relationships and applicable inference.

## 14.3 Scientific projections

The Method projection links problem classes, estimands, assumptions, diagnostics, alternatives, software evidence, and failure modes. The Representation projection links observations, transformations, fit state, invariants, causal availability, information loss, and downstream claims.

Question and Opportunity views distinguish recorded uncertainty from governed priority. Expected information gain, novelty, feasibility, cost, risk, and portfolio relevance are attributable estimates, not objective graph attributes.

Predictive-edge and Mechanism views remain separate. Statistical dependence does not create a causal edge; an execution advantage does not become price prediction; realized return does not become a graph property called alpha.

## 14.4 Graph reasoning

Traversal can surface analogies, missing tests, incompatible assumptions, shared dependencies, and unexplored combinations. Every generated path retains access policy and edge type. A proposed synthesis becomes a claim object before it can enter a dossier.

Unknown unknowns are not nodes waiting to be scored. Gap views represent missing expected evidence or unresolved questions under a defined model of what should exist.

## 14.5 Access and inference leakage

Permissions propagate to nodes, edges, embeddings, counts, neighborhoods, and aggregate statistics. Hiding a protected document while exposing its title, degree, nearest neighbors, or query timing can leak information.

Projection services enforce purpose and return safe omissions. A denied neighborhood cannot be inferred through repeated count queries.

## 14.6 Evaluation

Evaluation tests edge provenance, type accuracy, invalidation propagation, access inheritance, projection rebuilds, query utility, and the rate at which proposed inferences survive review. A visually rich graph is not an acceptance criterion.

## Source note

This chapter consolidates the Founder’s Edition, Chapters 25–31 (pp. 88–108), preserving fourteen graph families as rebuildable projections rather than parallel truth stores. Discovery prioritization belongs to Book IV.
