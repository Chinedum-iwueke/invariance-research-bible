# ADR-0005: Canonical identity and compatibility

**Status:** Accepted  
**Date:** 2026-08-10  
**Decision owners:** Architecture authority and Knowledge authority

## Context

Hermes already assigns UUIDs and digest-bound records to research and operational
objects. Bulletproof independently identifies hypotheses, manifest rows, runs,
configurations, and artifacts. Replacing either namespace would break historical
evidence; treating hashes or filenames as institutional identity would make
corrections and producer upgrades ambiguous.

## Decision

Adopt `canonical-identity-v1.0.0` as the shared identity envelope.

1. **Hermes owns institutional identity.** `object_id` is a stable UUID assigned or
   adopted when an object enters the canonical core. Existing Hermes UUIDs remain.
2. **Producers own native identity.** Bulletproof run IDs, hypothesis IDs, config
   hashes, artifact digests, and existing Hermes keys remain immutable aliases.
3. **Content and object identity are separate.** `content_digest` is lowercase
   SHA-256 over producer-defined canonical content, not enduring object identity.
4. **Versions are explicit.** `schema_version` governs the envelope;
   `content_version` identifies a revision; `producer.schema_version` identifies the
   native contract. A new version points to the superseded object.
5. **Aliases are append-only.** `(namespace, object_type, value)` is unique
   institution-wide. An alias cannot be reassigned or removed from a live identity.
6. **Major versions negotiate compatibility.** Readers accept supported v1 minor and
   patch versions and reject unknown major versions and fields. Semantic changes or
   required fields require a new major version.
7. **Canonical history is immutable.** Corrections, retractions, invalidations, and
   improved recoveries create events or successors rather than overwrite history.

| Field | Meaning |
|---|---|
| `schema_version` | Envelope contract, currently `canonical-identity-v1.0.0` |
| `object_id` | Stable institutional UUID |
| `object_type` | Scoped canonical type such as `research.trial` |
| `content_version` | Producer-declared edition or revision |
| `content_digest` | SHA-256 of exact identified content |
| `producer` | Native system, type, ID, and schema version |
| `aliases` | Append-only native and historical identifiers |
| `supersedes_object_id` | Prior UUID when this is a new content version |

## Existing identity crosswalk

| Existing record | Canonical ownership | Preserved alias/content field |
|---|---|---|
| Hermes source, snapshot, hypothesis, trial, result, review, decision | Existing Hermes `id` | Keys remain aliases; `record_digest` becomes `content_digest` |
| Hermes experiment | Existing Hermes `id` | `experiment_key` is an alias; `manifest_digest` becomes `content_digest` |
| Hermes document or artifact | Existing Hermes UUID | Document/artifact keys are aliases; digest remains content identity |
| Bulletproof hypothesis/specification | Hermes UUID assigned at canonical registration | Native hypothesis/spec IDs are `bulletproof` aliases |
| Bulletproof trial/run | Hermes trial UUID, or an unclaimed valid UUID run ID | `run_id` is an alias; run-bundle digest is content identity |
| Bulletproof config/manifest/artifact | UUID assigned on publication when independently cited | Native key/hash remains an alias/content identity as applicable |

A valid UUID native ID may be adopted only when no canonical object or alias owns it.
The future registry service is authoritative for collision checks.

## Compatibility and deprecation

- Legacy readers require explicit namespace, object type, ID field, digest field,
  and producer schema version. Guessing identity semantics is forbidden.
- Both repositories retain v1 readers for at least two released successor minor
  versions and until active producer packages declare the successor contract.
- Deprecation requires telemetry, a published replacement, a warning period, and a
  major release. Historical readers required for replay remain available.
- Writers emit the newest supported minor version. Unknown majors are never coerced.
- Digest mismatch, alias reassignment, type change, and producer-identity change are
  hard integrity failures.

## Persistence and rollback

Hermes adds an empty `canonical_identity_aliases` registry with uniqueness over the
producer namespace/type/value tuple. BASE-002 performs no backfill. RI-001 will add
canonical object persistence and transactionally register aliases. Application
rollback retains readers; the empty table is removable only before canonical writes.

## Consequences

Existing records remain replayable, producers can upgrade independently, and RI-001
cannot invent replacement identifiers. This decision does not migrate data,
implement retrieval, publish RI objects, or grant promotion or capital authority.
