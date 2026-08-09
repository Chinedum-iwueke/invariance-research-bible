<a id="b10-c18"></a>
# Chapter 18 — Migration, Compatibility, and Rollback

Migration moves authority and evidence without losing history or creating ambiguous writers.

## 18.1 Strategy

Use inventory, target contract, compatibility adapter, backfill, validation, dual read, shadow write where safe, cutover, observation, and retirement. Avoid indefinite dual authority.

## 18.2 Data migration

Preserve source identities and digests; map every field; record defaults and unknowns; validate counts, constraints, samples, and semantic reconciliations; and keep reversible snapshots.

## 18.3 Schema change

Expand before contract, support mixed versions for a bounded period, migrate consumers, and remove only after evidence. Event schema corrections append rather than rewrite history.

## 18.4 Rollback

Define triggers, compatible prior version, state and data behavior, irreversible effects, authority, and recovery validation. Forward-fix and rollback are chosen by consequence.

> **Builder rule B10-BD18 — One canonical writer at cutover**  
> Migration may duplicate reads and projections, but canonical mutation authority transfers at an explicit, auditable boundary.

## Source note

This chapter implements the series-wide versioning and lineage doctrine.
