<a id="bulletproof-bt-as-built"></a>
# 5. Bulletproof BT Laboratory

## 5.1 Engine purpose

Bulletproof BT is a deterministic, event-driven quantitative research engine. Its
declared invariant is same data plus same configuration yields semantically identical
outputs, with closed-bar strategy visibility, no interpolation and no silent cost or
risk assumptions. The latest exhaustive audit pin and dirty-tree boundary remain in the
implementation reference register; this chapter summarizes inspected capability, not
profitability or live certification.

## 5.2 Core engine composition

The classic run loop connects a historical feed, instrument/universe abstraction,
strategy, risk engine, execution model, portfolio accounting, metrics, benchmark and
artifact writers. Strategies receive a read-only context and emit typed `Signal`
objects; they do not mutate portfolio or execution internals.

### Data contracts

- UTC timezone-aware, monotonic timestamps;
- required OHLCV columns and OHLC consistency;
- duplicate detection and explicit missing-bar behavior;
- closed-bucket higher-timeframe resampling;
- market modes for 24/7 crypto, 24x5 FX and equity sessions;
- single-file data or manifest-backed dataset directories;
- no implicit interpolation.

### Execution and cost model

- maker/taker fees, spread, slippage and delayed execution;
- tiered or complete custom execution profiles;
- deterministic intrabar pricing;
- FX commission-per-lot and lot rounding;
- equity commission and cash-account behavior;
- basic futures/contract abstraction;
- explicit margin usage and rejection reasons.

### Risk and portfolio accounting

- stop-intent contract via explicit stop price/specification;
- stop-distance and percentage-equity sizing;
- tick/lot rounding and instrument contract size;
- margin-aware reservation and execution constraints;
- cash, positions, liquidation and R-multiple normalization;
- a separate portfolio engine for isolated strategy sleeves, allocation/coordinator
  checks and aggregated artifacts.

The separate portfolio engine is not yet evidence of a unified, certified same-clock
multi-strategy matching engine or production order router.

## 5.3 Market and indicator capability

The documented V1 surface supports crypto, FX and equities with basic futures
abstraction. Streaming indicators include moving averages; RSI/Stochastic/CCI/ROC and
other oscillators; ATR, Bollinger, Keltner, Donchian and volatility measures; ADX,
MACD/PPO/TRIX and directional indicators; OBV/CMF/MFI and volume flows; Supertrend,
Parabolic SAR, pivots, Heikin-Ashi and candle/range features. Every indicator has an
explicit warmup and bar-by-bar update path.

## 5.4 Research data library

`bt.research_data` contains adapters and workflows for Binance, Bybit and OKX perpetual
futures, backfills, instrument refresh, stable/volatile universe manifests, causal
research panels, validation reports and forward-collected liquidation events.

BT-002 adds an immutable derived contract around explicit bounded Parquet partitions.
It records each partition's SHA-256, size, schema, row count, event and availability
ranges, duplicate count and gap count; binds those records to the BASE-002 canonical
identity; declares UTC/bar-clock semantics and a knowledge cutoff; validates
point-in-time membership; and retains append-only correction lineage. Missing bars
remain missing. Replaying the manifest against the source root detects changed bytes.
The builder writes only a JSON manifest outside source partitions and never repairs or
rewrites the lake.

This is a snapshot qualification boundary, not lake-wide certification. DATA-001
through DATA-003 still own complete venue identity, historical membership population,
vendor correction ingestion, entitlement policy, quality SLOs and recovery.

## 5.5 Experimentation and artifacts

Experiment support includes configuration layering, hypothesis contracts, grid
expansion, parallel hypothesis execution, resume/skip-completed behavior, dataset
extraction, cleanup and truth validation. A normal run emits resolved configuration,
performance, equity, trades, fills, decisions, bucket performance, cost breakdown,
summary, manifest, run status and optional benchmarks.

Truth checks cover missing evidence, duplicate truth fields, source timestamps after
entry, notional/risk consistency and artifact completeness. Selected JSON outputs have
deterministic serialization; timestamps and absolute run paths mean byte-for-byte
identity is not claimed for every file.

BT-003 adds the immutable publication boundary without replacing those artifacts. A
finalizer copies canonical textual artifacts into a same-filesystem staging directory,
assigns source-byte, publishable-byte and semantic SHA-256 digests, records media type
and structural schema identity, binds repository/code, BT-002 dataset, specification,
environment and attempt lineage, validates the bundle, and atomically renames it to a
content-addressed final directory. A failure or interruption leaves no partial bundle
and retains a redacted failed-attempt record.

Supported volatile run IDs, generated timestamps and output paths are excluded from
semantic identity while exact published bytes remain independently digest-bound. The
legacy run manifest is copied with stable runtime/data aliases and retains its original
source digest. Other absolute protected paths, likely secrets, symlinks, corrupt files,
unsupported binaries and unknown schemas fail closed. Repeated semantic publication is
idempotent and returns the existing receipt.

Hermes' canonical run payload now optionally carries the bundle digest, manifest
digest and `bundle://sha256/...` URI as an all-or-none reference. Bulletproof publishes
that record through the existing idempotent canonical-evidence endpoint; it does not
create another registry or store authorization material in artifacts.

## 5.6 Research memory and Hermes bridge

The SQLite research memory stores completed trades, state buckets, verdicts,
recommendations and alpha candidates. Enriched derivative state includes funding, open
interest, basis, premium, crowding and constraint-stress fields. Similar-state queries
can use those dimensions. Recommendations remain proposed-only.

Hermes does not ingest the raw memory database. The VM1 memory steward opens the fixed
source read-only, exports bounded counts/candidates/summary text, binds it to a digest
and registers canonical evidence plus an RI-007 synchronization receipt.

## 5.7 Known engineering gaps

- BT-001 closes the recorded collection/dependency/fixture drift for the locked Python
  3.11 matrix using deterministic shards and restored canonical contracts. The engine
  and strategy catalog remain the existing Bulletproof implementation.
- Atomic run bundles and canonical run-record publication are complete under BT-003;
  broader result/artifact RI publication remains BT-008 work.
- BT-002 point-in-time and correction proofs apply to selected snapshots; universal
  lake population remains DATA-001 through DATA-003 work.
- Shadow, demo and live-looking surfaces do not constitute venue-certified execution.
- Portfolio admission, allocation and capital mutation remain separately governed and
  cannot be inferred from a successful backtest.
