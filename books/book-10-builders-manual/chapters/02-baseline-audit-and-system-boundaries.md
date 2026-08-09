<a id="b10-c02"></a>
# Chapter 2 — Baseline Audit and System Boundaries

Before building, inventory repositories, services, datasets, schemas, credentials, environments, jobs, vendors, artifacts, and operational practices. Current behavior outranks planned diagrams.

## 2.1 Audit record

Pin versions; map source trees, APIs, databases, queues, storage, tests, documentation, owners, deployments, dependencies, data flows, and incidents. Classify implemented, partial, proposed, deprecated, unknown, and unavailable evidence.

## 2.2 Trust boundaries

Identify humans, services, agents, vendors, venues, networks, data classes, secrets, and mutation paths. Mark canonical writers and readers. Every external input is untrusted until validated.

## 2.3 Gap register

Record missing contracts, stale documentation, duplicate authority, mutable primary evidence, weak identity, absent rollback, unknown operational state, and single points of failure. Rank by consequence and dependency, not visibility.

## 2.4 Freeze

During migration, freeze incompatible schema and authority changes or route them through compatibility review. Preserve existing working behavior and tests.

> **Builder rule B10-BD02 — Audit before abstraction**  
> System boundaries and migration plans derive from pinned implementation and operational evidence, with discrepancies preserved explicitly.

## Source note

Book V’s pinned audit provides the reference method for implementation baselines.
