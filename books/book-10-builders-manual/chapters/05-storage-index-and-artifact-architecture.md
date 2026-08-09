<a id="b10-c05"></a>
# Chapter 5 — Storage, Index, and Artifact Architecture

Storage separates canonical records, immutable large artifacts, mutable workflow state, and rebuildable indexes.

## 5.1 Stores

Use transactional storage for identities, authority, workflow, registries, and decisions; object storage for immutable data and run bundles; event journals for lifecycle; analytical stores for projections; search and vector indexes for retrieval; and caches for disposable acceleration.

## 5.2 Artifact manifest

Every bundle has relative path, media type, schema, size, digest, producer, inputs, created time, access class, and retention. Finalization is atomic. Derived artifacts append lineage.

## 5.3 Indexes

Search, graph, embeddings, and analytics are rebuildable from canonical evidence. Index version and source cutoff are visible. Deletion or access change propagates through projections.

## 5.4 Retention

Policy considers scientific value, legal obligation, cost, incident status, promotion, dispute, and reproducibility. Deletion produces a tombstone and audit; sensitive content uses controlled destruction.

> **Builder rule B10-BD05 — Primary evidence is immutable; views are rebuildable**  
> No index, cache, dashboard, or graph becomes the sole carrier of institutional truth.

## Source note

Storage semantics derive from Book III and run-bundle contracts from Book V.
