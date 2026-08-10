<a id="base-002-completion-evidence"></a>
# BASE-002 Completion Evidence

**Status:** Complete  
**Date:** 2026-08-10  
**Scope:** Identity decision, compatibility readers, schemas, synthetic fixtures, and
an empty additive alias registry. No production data migration or retrieval.

## Decision evidence

[ADR-0005](../../architecture/adrs/0005-canonical-identity-and-compatibility.md)
defines canonical ownership, existing identity mappings, alias uniqueness,
content/object separation, version negotiation, immutability, and deprecation.
Hermes UUIDs and Bulletproof producer identifiers are preserved.

## Implementation evidence

| Repository | Evidence |
|---|---|
| Hermes | `canonical-identity-v1` schema; compatibility reader; canonical/legacy fixtures; additive alias-registry migration |
| Bulletproof | Matching schema semantics; producer compatibility reader; canonical/legacy fixtures |

Both readers consume the canonical fixture without alteration. Hermes maps legacy
`{id, record_digest}` and Bulletproof maps explicit `{run_id, artifact_digest}`
contracts. Neither reader guesses field meaning.

## Acceptance results

| Check | Result |
|---|---|
| Canonical and legacy fixture consumption in both repositories | Passed |
| Same-version digest mutation rejection | Passed |
| Unknown major-version rejection | Passed |
| Python compilation and focused Ruff checks | Passed |
| Alembic migration graph | Single BASE-002 head |
| Hermes identity, research-registry, and data-contract slice | 23 passed |
| Bulletproof identity and experiment-cleanup slice | 7 passed |

The Hermes slice used a mode-0600 audit-only placeholder password file to satisfy
configuration import; it did not connect to a database or contain a credential.
Bulletproof's broader research-spec module was not included because its current
environment lacks the undeclared test dependency `jsonschema`; BASE-002 introduces
no dependency change and its dedicated fixtures passed independently.

The implementation pins are:

- Hermes control plane: `d26484f1da3f73697b4748326912c9879b05fef1`
- Bulletproof BT: `45790daaa62d8c8737317c0a869099b5747781c6`

## Rollback and boundary

Readers remain on application rollback so historical evidence is replayable. The
alias table may be removed only while empty; after RI-001 writes aliases, rollback
requires a reviewed compatibility migration. No production-readiness, migration,
retrieval, or capital-authority claim is made.
