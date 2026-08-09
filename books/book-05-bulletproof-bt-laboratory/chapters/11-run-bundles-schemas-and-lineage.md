<a id="b5-c11"></a>
# Chapter 11 — Run Bundles, Schemas, and Lineage

A run bundle is the primary evidence package of a historical experiment. Dashboards, verdicts, and comparisons are projections over it. If the bundle cannot support reconstruction and reconciliation, a polished summary cannot rescue it.

## 11.1 Current classic bundle

The pinned artifact manifest defines the following required artifacts: resolved configuration, decisions, fills, equity, trades, performance, performance by bucket, and run status. Benchmark equity and metrics, comparison summaries, cost breakdown, data scope, decision-logging summaries, candidate-event summaries, and human-readable summary are conditional or optional under their policies.

`run_manifest.json` records creation time, run directory, data path, whether the path is a dataset directory, benchmark enablement, artifact filenames, and a compact configuration summary. `artifacts_manifest.json` records definitions, required and conditional status, observed presence, and selected schema versions.

Presence is not validity. A zero-byte ledger, malformed JSON, incompatible schema, or internally inconsistent trade file remains a failed contract.

## 11.2 Canonical and derived evidence

Decisions, orders where emitted, fills, trades, equity, resolved configuration, status, and validated manifests form the run’s canonical evidence core. Performance, bucket tables, figures, terminal cards, and dashboard payloads are derived. Derived objects retain producer, schema version, source artifact digests, and derivation version.

The repository’s research dataset builder extracts run- and trade-level Parquet datasets and records an extraction manifest and log. It can operate after large decision and fill logs are explicitly removed under cleanup policy. Such a dataset supports cross-run analysis but is not automatically equivalent to the deleted primary event history.

## 11.3 Schema versioning

The repository explicitly versions several JSON outputs and publishes 23 JSON schemas for research and integration contracts. Other artifacts rely on stable columns, documentation, and tests. A blanket statement that every artifact is schema-versioned is therefore too broad.

Every consumer declares accepted producer and schema ranges. Additive compatibility is tested; breaking change creates a new major version and migration. CSV requires the same discipline even without an embedded schema field: field order, names, types, units, nullability, and semantic meaning belong to a registered schema.

## 11.4 Lineage closure

Target lineage connects:

`research question → hypothesis version → experiment → trial → attempt → code and environment → dataset and representation → resolved configuration → event artifacts → validation → interpretation → decision`.

Each edge is attributable. Run directory names are locators, not identities. Mutable URLs are locators, not version pins.

## 11.5 Integrity

The target bundle includes a manifest of relative paths, sizes, media types, schema identities, and cryptographic digests. It is finalized atomically after validation. Later derived artifacts form a signed or append-only extension manifest; they do not rewrite the original record.

> **Laboratory rule B5-LR11 — Summaries never outrank events**  
> A derived metric or visualization is admissible only while its source artifacts, producer version, and derivation lineage remain recoverable.

## Source note

Current statements derive from pinned artifact definitions, run manifests, run contracts, deterministic writers, public schemas, research dataset extraction, and documentation. Institutional lineage extends Book III.
