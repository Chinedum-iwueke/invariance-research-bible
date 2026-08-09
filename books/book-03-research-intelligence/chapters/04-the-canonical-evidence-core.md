<a id="b3-c04"></a>
# Chapter 4 — The Canonical Evidence Core

Research Intelligence needs one coherent identity and evidence substrate from which documents, indexes, graphs, dossiers, and memory views can be derived. Without a canonical core, each retrieval system or graph can become an independent truth store whose conflicts cannot be reconciled.

The core is a logical data model, not a mandated database product.

## 4.1 Canonical objects

The core represents sources and editions; structural document objects; concepts and definitions; claims and assumptions; evidence relationships; methods and variables; datasets and representations; hypotheses and trials; experiment specifications and runs; artifacts and reviews; decisions and beliefs; incidents and operational outcomes; people, agents, services, and organizations; policies, access rules, and retention events.

Each object has stable identity, type, version or revision semantics, provenance, authority, validity interval where applicable, access policy, and lifecycle. Content identity and semantic version remain distinct.

## 4.2 Assertions and relationships

Relationships are evidence-bearing assertions. “Source supports claim,” “run instantiates specification,” “result contradicts belief,” and “decision uses dossier” each identify origin, scope, time, and review state.

Observed relationships, deterministic derivations, statistical estimates, and agent-proposed inferences remain different edge types. A graph connection does not become true because it is stored structurally.

> **Knowledge rule B3-KR04 — One core, rebuildable views**  
> Search indexes, embeddings, graphs, caches, dashboards, and dossier assemblies derive from canonical objects and attributable assertions; they may be rebuilt or replaced without rewriting source identity or historical evidence.

## 4.3 Events and current state

Consequential change is append-only. Creation, correction, invalidation, supersession, access change, belief revision, and deletion are events. Current state is a projection over valid events, not a mutable row with erased history.

An event asserts that an identified actor or service emitted a statement under a schema. Authentication proves origin, not objective truth. Review and evidence determine whether the assertion is accepted.

## 4.4 Primary and derived objects

Primary objects preserve authoritative source or producer output: captured documents, dataset versions, laboratory artifacts, signed decisions, and operational records. Derived objects include extracted text, normalized equations, embeddings, rankings, summaries, comparisons, and graph projections.

Derived objects link their producer, inputs, method, version, and quality. A derived object can become a stable cited artifact without being confused with the primary evidence from which it was made.

## 4.5 Corrections and deletion

Corrections add a new version or event and preserve the earlier state. Invalidated objects remain discoverable with warnings so dependent claims and decisions can be reviewed. Supersession does not imply that the old object was erroneous; it may simply no longer be current.

Privacy, legal, license, and security obligations can require deletion or cryptographic erasure. A permitted tombstone preserves identity, relationship, reason, and date without retaining prohibited content. Derived indexes receive the same deletion propagation.

## 4.6 Transactional and analytical use

The authoritative catalog must support consistent identity, transition, and permission decisions. Retrieval and graph systems optimize discovery and reasoning. They can be eventually consistent within defined service levels but must expose freshness and version so a user knows which core state was searched.

Book X selects storage and service topology. Book III fixes the semantics that any implementation must preserve.

## Source note

This chapter consolidates the Founder’s Edition, Chapters 25–31 and 45–47 (pp. 88–108 and 153–161), retaining one evidence core with rebuildable projections while relocating technology choices to Book X.
