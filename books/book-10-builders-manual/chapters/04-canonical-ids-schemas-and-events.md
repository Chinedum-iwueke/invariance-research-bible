<a id="b10-c04"></a>
# Chapter 4 — Canonical IDs, Schemas, and Events

Identity and schema discipline allow systems to exchange evidence without guessing semantics.

## 4.1 Identity

Use immutable opaque IDs for institutions, actors, tasks, questions, hypotheses, experiments, trials, attempts, runs, datasets, representations, models, strategies, portfolios, instruments, orders, fills, artifacts, decisions, incidents, and deployments. Human names are attributes.

## 4.2 Schema registry

Register name, version, owner, compatibility, units, nullability, examples, validators, producers, consumers, retention, and deprecation. Breaking semantic change creates a new major version.

## 4.3 Events

Events carry identity, schema, actor, event and ingestion times, aggregate identity, sequence or causation, correlation, payload, provenance, and idempotency. Facts are append-only; corrections reference superseded facts.

## 4.4 Commands and decisions

Commands request mutation and can be rejected. Events report what occurred. Decisions include evidence, policy, authority, conditions, and expiry. The three are never one generic message.

> **Builder rule B10-BD04 — Identity survives transport**  
> Every object retains canonical identity and schema across databases, queues, files, APIs, and derived projections.

## Source note

This chapter implements the series notation and lineage standards.
