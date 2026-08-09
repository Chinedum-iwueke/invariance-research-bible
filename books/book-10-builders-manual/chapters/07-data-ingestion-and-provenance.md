<a id="b10-c07"></a>
# Chapter 7 — Data Ingestion and Provenance

Ingestion converts external observations into immutable, validated datasets while preserving source and correction history.

## 7.1 Pipeline

Acquire, authenticate, timestamp receipt, store raw bytes, validate transport, parse, normalize, map instruments, validate semantics, quarantine failures, publish versioned partitions, and emit manifests and quality events.

## 7.2 Provenance

Record provider, endpoint, query, terms, retrieval time, source and availability times, raw digest, parser, transformations, repairs, exclusions, and output digest. Revised data create new versions.

## 7.3 Quality

Check schema, sequence, duplicates, gaps, ranges, cross-field consistency, source coverage, clock, corporate actions, contract rolls, and comparison with independent sources where justified.

## 7.4 Access

Classify license, privacy, commercial restrictions, protected periods, and consumers. Derived datasets inherit restrictions unless policy states otherwise.

> **Builder rule B10-BD07 — Raw evidence remains recoverable**  
> Every normalized field can be traced through deterministic transformations to source bytes and acquisition context.

## Source note

Data contracts derive from Books III, V, VI, and VIII.
