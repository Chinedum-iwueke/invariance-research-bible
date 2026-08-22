<a id="b5-app-d"></a>
# Appendix D — Research Data Lake Audit

**Audit date:** 2026-08-10
**Implementation pin:** `ba2a0314817607c5c79d604a0846e008c14379c2`
**Method:** read-only directory and Parquet-metadata inspection; no raw rows were committed, moved, repaired, or published

## D.1 Safe inventory

**Observed.** The ignored lake has `raw`, `canonical`, `manifests`, and `reports` layers. Raw paths are partitioned by exchange, native symbol, dataset (`ohlcv`, `mark`, `index`, `funding`, and `oi`), timeframe, and chunks. Canonical paths are exchange/symbol/timeframe partitions. The following aggregates come from the lake's own Parquet manifests:

| Manifest evidence | Safe aggregate |
|---|---|
| Instrument catalog | 1,678 perpetual-instrument records: Binance 645, Bybit 722, OKX 311 |
| Coverage catalog | 3,448 series records; declared range 2021-01-01 through 2026-08-08 |
| Fetch state | 6,727 records: 6,721 `success`, 5 `failed`, 1 `running`; five non-empty error fields |
| Stable universe | 30 Bybit perpetual records: 26 available, 4 unavailable |
| Volatile-universe membership | 382,861 rows, 628 symbols, 7,003 rebalance identifiers; 2025-01-02 through 2026-08-08 |

**Observed limitation.** Aggregate coverage reports zero missing OHLCV rows for the cataloged Bybit series, while Bybit funding reports 76,106 missing rows and Bybit open interest reports 18,887,057 missing rows with large maximum gaps. Binance and OKX coverage in the manifest is much narrower by series count. These values describe the manifest at inspection time; they are not a claim that every underlying file is readable or causally valid.

## D.2 Schema and identity

The instrument manifest records market, exchange, native and canonical symbols, assets, contract type, status, first/last seen timestamps, and precision. Coverage records dataset/timeframe, expected and actual rows, missing rows, largest gap, and first/last timestamps. Fetch state records attempts, last success, status, row count, and error text.

This is a useful operational catalog, but it does not yet establish all target identities. A target dataset version requires a content manifest over immutable partitions, source request/provenance, vendor/venue semantics, retrieval time, correction lineage, schema identity, timezone/clock contract, availability-time policy, and access classification.

## D.3 Proof limits

| Requirement | Present evidence | Status |
|---|---|---|
| Directory and partition convention | Read-only path inventory | current; observed |
| Instrument and coverage manifests | Parquet schemas and aggregate queries | current; observed |
| Duplicate and gap accounting | Gap fields exist; no exhaustive partition scan was completed | partial |
| Point-in-time membership | Timestamped membership plus BT-002 `known_at`/validity validation for bounded snapshots | bounded contract complete; lake-wide backfill pending |
| Point-in-time feature availability | BT-002 recorded-or-derived `available_at`, clock and cutoff validation | bounded contract complete; lake-wide certification pending |
| Vendor corrections and restatements | BT-002 append-only successor ledger rejects late/identity-preserving mutation | bounded contract complete; vendor history population pending |
| Immutable dataset digest | BT-002 binds canonical identity, partition SHA-256, schema, range, quality and manifest digest | bounded contract complete; universal catalog pending |
| Retention and access policy | Filesystem layout exists; no complete policy evidence was inspected | unknown |
| Recovery | Fetch state and temporary files show resumable operations; restore drill evidence was not established | partial |

## D.4 Safe-use rule

No experiment may infer point-in-time correctness from the existence of a canonical Parquet partition. The registered experiment must bind the exact data snapshot, coverage report, availability policy, universe-membership rule, and validation report. Missing funding or open-interest observations must be modeled as missing evidence, never silently forward-filled into economic knowledge.

## D.5 Required closure

BT-002 now provides immutable dataset manifests, partition digests, correction lineage,
availability-time tests, access classes and point-in-time membership for explicitly
selected partitions. It deliberately does not rewrite the raw lake. DATA-001 through
DATA-003 still own lake-wide identity, vendor-history population, entitlements,
quality SLOs and recovery evidence. The lake therefore supports digest-bound bounded
research, not a blanket certification of every dataset.

## Source note

This appendix publishes only schemas and safe aggregates from ignored local evidence. Absolute protected-data paths, raw records, credentials, and proprietary samples are intentionally omitted.
