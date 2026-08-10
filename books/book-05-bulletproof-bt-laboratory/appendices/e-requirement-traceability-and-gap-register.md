<a id="b5-app-e"></a>
# Appendix E — Requirement Traceability and Gap Register

**Audit pin:** `ba2a0314817607c5c79d604a0846e008c14379c2`
**Status rule:** `current` requires inspected code; `tested` requires an identified passing test; `observed` requires a controlled run.

| ID | Book V requirement | Current component and evidence | Status | Gap / target component | Milestone |
|---|---|---|---|---|---|
| B5-01 | Baseline identity | Git pin, package metadata, implementation register | current | Dependency lock and supported-runtime matrix | M3 |
| B5-02 | System boundaries and variants | `BacktestEngine`, `portfolio_engine`, execution runtimes | current; tested in focused slices | Publish stable interface/status catalog | M3 |
| B5-03 | Lake relationship | Research-data loaders, manifests, Appendix D profile | partial; observed | Immutable catalog and universal lineage | M3 |
| B5-04 | Instruments, clocks, sessions, point-in-time data | Instrument contracts, UTC events, validators, resampling tests | partial; tested | Availability-time and venue-session proof across all feeds | M3 |
| B5-05 | Strategy/risk/execution/portfolio/accounting ownership | Separate packages and engine composition | current; tested | Same-clock portfolio semantics and ownership ADR | M3, M6 |
| B5-06 | Causality/no lookahead | Higher-timeframe closed-bucket tests and truth checks | partial; tested | Property tests over all enrichments and fitted transforms | M3 |
| B5-07 | Configuration/determinism | Resolved config, deterministic serializers, repeat-output tests | partial; tested | Content-derived run identity and cross-runtime golden matrix | M3 |
| B5-08 | Fills/costs/benchmarks/diagnostics/accounting | Explicit execution config, costs, benchmark and reconciliation surfaces | partial; tested | Empirical calibration and complete venue semantics | M3, M5 |
| B5-09 | Hypothesis/trial/experiment/representation/label contracts | Hypothesis/grid schemas and Hermes immutable registry | partial; tested across repositories | One canonical compatibility contract and fitted-artifact lineage | M1, M3 |
| B5-10 | Search/orchestration/retries/concurrency/identity | Grid expansion, parallel scheduling, status and cleanup | partial | Search accounting, idempotent attempts, durable queue integration | M3-M4 |
| B5-11 | Run bundles/schemas/manifests/lineage | Required artifacts and schema metadata | partial; tested | Atomic digest-finalized bundle with schema for every canonical artifact | M3 |
| B5-12 | Reproducibility/truth | Repeated output and truth validation tests | partial; tested | Full regression closure, differential oracle, environment lock | M3 |
| B5-13 | Research Intelligence publication | Dataset extraction, memory bridge, Hermes research routes | partial; tested | Typed run-bundle ingestion, citation and decision lineage | M1, M3 |
| B5-14 | APIs/institutional boundaries | Python/CLI and public schemas; Hermes authenticated APIs | partial | Versioned, idempotent laboratory service boundary | M3 |
| B5-15 | Portfolio/live-readiness | Sleeve aggregation, adapters, runtime and safety tests | partial | Credentialed certification; separate admission authorities | M5-M7 |
| B5-16 | Shadow/execution replay | Shadow/demo scripts and execution modules | partial | Prospective, immutable replay journal and parity gates | M5 |
| B5-17 | Failures and drift | Implementation register records seven reproduced failures and collection errors | current; observed | Repair contracts/tests/docs without weakening assertions | M3 |
| B5-18 | Target architecture | Chapter 17 and migration diagram | target | Implement through compatibility-preserving slices | M3-M7 |
| B5-19 | Gap register | This appendix and implementation status register | current | Keep synchronized at every release pin | M0 |
| B5-20 | Ordered migration | Company roadmap | target | Execute evidence-gated milestones | M0-M9 |
| B5-21 | Maturity acceptance | System acceptance matrix | target | Bind gates to machine-verifiable evidence | M0-M8 |
| B5-22 | Unsafe-use conditions | Appendix B and below | current doctrine | Enforce in services and release checks | M3-M7 |

## Highest-priority defects and unknowns

1. **Full-suite closure is absent.** The earlier pin audit collected 1,077 tests but recorded dependency collection errors and seven reproduced failures. On 2026-08-10, a new `pytest --collect-only -q` run exceeded its 120-second bound without a completion summary. The focused 50-test slice passed in 2.85 seconds.
2. **The environment is not locked.** The package declares ranges without a committed lock; the audit virtual environment used Python 3.11.15 and pytest 9.0.2.
3. **Dataset identity is incomplete.** Operational manifests exist, but universal content-addressed snapshots, correction lineage, and availability-time evidence do not.
4. **Artifact identity is incomplete.** Several schemas and deterministic serializers exist, but not every canonical artifact is schema-bound and atomic bundle finalization is not universal.
5. **Portfolio semantics are split.** Sleeve aggregation is real and useful, but it is not evidence of a unified event clock or complete live order routing.
6. **Institutional publication is split across systems.** Hermes has immutable research lineage and bounded memory export, while Bulletproof artifacts are not yet universally registered through one producer contract.
7. **Operational qualification is blocked.** Venue credentials, private branches/services, live accounts, and production operating evidence were unavailable and were not requested during this audit.

## Unsafe-use conditions

Bulletproof BT is not safe to use as evidence for capital allocation when the data snapshot is mutable or unidentified; timestamps or fitted-feature availability are unproved; costs or instrument semantics are implicit; artifact validation fails; trial/search history is incomplete; full accounting does not reconcile; the run cannot be reproduced at its supported pin; independent reviews are absent; or a laboratory result is being treated as portfolio, execution, or production authority.

## Source note

Code and tests are evidence only at the pinned commit and named environment. Target rows derive from Books II, III, VII, VIII, IX, and X and do not assert implementation.
