<a id="b10-c09"></a>
# Chapter 9 — Trial Registry and Experiment Integration

The Trial Registry connects scientific authorization to deterministic execution without making the backtest engine a governance system.

## 9.1 Flow

Register experiment and search budget; materialize trial identities; authorize evidence access; schedule immutable specifications; create attempt identities; execute Book V; validate bundles; publish lifecycle events; and close every trial.

## 9.2 States

Proposed, registered, queued, running, succeeded, valid-negative, invalid, failed-operational, cancelled, and closed remain distinct. Retries preserve trial identity and failed attempts.

## 9.3 Idempotency

Submission key prevents duplicate trials; worker lease prevents concurrent ownership; finalization uses compare-and-set; artifact manifest proves completion.

## 9.4 Integration

Adapters translate registered specs into engine inputs and validate returned evidence against producer schemas. Engine-specific fields do not leak into institutional contracts without mapping.

> **Builder rule B10-BD09 — Trial truth is registry plus bundle**  
> Authorization and lifecycle come from the Trial Registry; experimental observations come from validated immutable run bundles.

## Source note

Book II owns registry authority, Book IV search, and Book V execution.
