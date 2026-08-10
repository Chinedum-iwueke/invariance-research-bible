<a id="b5-c04"></a>
# Chapter 4 — Data and Instrument Contracts

The engine cannot repair an undefined dataset. A laboratory data contract identifies what each row means, when it became knowable, which transformations produced it, and which instrument rules govern its economic interpretation.

## 4.1 Current data forms

The pinned repository supports single-file input and dataset directories described by manifests. Its data packages cover loading, validation, Parquet I/O, streaming feeds, resampling, dataset manifests, symbol sources, market rules, research panels, and a separate research-data library. The repository also contains configuration profiles for different market families.

Core bar validation requires the expected timestamp, symbol, OHLC, and volume structure; checks UTC-aware time, ordering, duplicates, finite values, and coherent price geometry; and can validate expected gaps separately. “No interpolation” means missing observations are not silently synthesized into tradable evidence. It does not mean the source vendor itself is complete or correct.

The read-only local-lake audit found operational `raw`, `canonical`, `manifests`, and `reports` layers and cataloged perpetual-market data across Binance, Bybit, and OKX. It also found material declared gaps in Bybit funding and open-interest coverage. [Appendix D](../appendices/d-research-data-lake-audit.md) records safe aggregate evidence and its proof limits. This observed inventory does not certify every partition or permit raw data to enter the Bible repository.

## 4.2 Dataset identity

A reproducible dataset identity includes:

- source and retrieval interval;
- immutable content hashes or a content-addressed manifest;
- symbol and contract identity;
- timezone and calendar;
- frequency and aggregation convention;
- adjustment and corporate-action policy;
- missingness and duplicate policy;
- source-time and revision policy for enriched fields;
- exclusions and repairs; and
- license and access conditions.

Path plus filename is not identity. File modification metadata can support a cache signature, but it is weaker than content hashing for institutional lineage.

## 4.3 Instrument semantics

Price and quantity do not have stable economic meaning without an instrument specification. Tick size, contract multiplier, quote and settlement currency, lot step, pip value, margin rule, trading calendar, fee basis, and price precision affect risk, cost, and P&L.

The current repository exposes instrument specifications and market packs for crypto, foreign exchange, equities, and basic futures modeling. Risk paths contain instrument-aware notional conversion, FX lot handling, leverage and margin overrides, and deterministic quantity rounding. These are implemented abstractions, not proof of complete coverage for every venue contract or corporate action.

## 4.4 Point-in-time enrichment

Features such as funding, open interest, reference prices, classifications, or universe membership need both value time and availability time. The experiment truth validator checks that selected source timestamps do not occur after entry. This is a valuable guard, but it protects only fields that carry and enter the check. Every new enriched field must join the same policy.

Universe construction deserves equal care. A present-day symbol list applied backward creates survivorship bias. Delistings, listings, contract rolls, and changing eligibility must be reconstructed point in time or declared as limitations.

## 4.5 Resampling

Higher-timeframe bars are derived objects. Their bucket boundary, label, closure, timezone, and session convention belong to the representation contract. The strict resampler’s focused test verifies that an intrabucket spike remains invisible until rollover closes the bucket. That proves the tested path, not every custom strategy transform.

> **Laboratory rule B5-LR04 — Availability travels with value**  
> A material field without a source-time or justified availability rule is inadmissible for causal strategy decisions.

## 4.6 Target controls

The target laboratory validates schemas at ingestion, binds datasets to immutable manifests, records every transformation, prevents protected-date access outside authorization, and emits a data-scope artifact with effective start, end, warmup, symbols, filters, and exclusions. Dataset revisions create new identities and trigger affected-run lineage analysis.

Deferred capabilities include universal tick normalization, complete order-book reconstruction, and authoritative cross-venue symbology. Those require Book VIII semantics and dedicated data operations.

## Source note

Current statements derive from the pinned `bt.data`, `bt.research_data`, `bt.instruments`, risk conversion, resampling, and truth-validation surfaces. The institutional lineage requirements extend Books I and III.
