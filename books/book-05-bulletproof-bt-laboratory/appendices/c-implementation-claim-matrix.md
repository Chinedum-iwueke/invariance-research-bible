<a id="b5-app-c"></a>
# Appendix C — Implementation Claim Matrix

| Surface | Current at audited pin | Target or deferred boundary |
|---|---|---|
| Classic simulation | Bar-driven single-strategy engine with separate feed, strategy, risk, execution, portfolio, audit, and artifacts | Broader event replay and independent differential oracle |
| Data | File and manifest loading, validation, Parquet, streaming, resampling, research panels | Immutable content manifests and universal availability-time coverage |
| Risk and execution | Stop sizing, instrument conversion, margins, costs, delayed orders, modeled fills | Empirically calibrated impact, queue, and complete venue semantics |
| Portfolio | Classic account plus sleeve-based multi-strategy aggregation and coordinator | Unified same-clock portfolio simulation and separately qualified live routing |
| Experiments | Hypothesis contracts, grids, manifests, parallel waves, status, extraction, cleanup | Institution-wide immutable Trial Registry integration |
| Artifacts | Required and conditional run artifacts; several explicit schema versions | Digest-finalized bundles and schemas for every canonical artifact |
| Validation | Layer audits, reconciliation tests, truth validation, focused regression suite | Expanded property, metamorphic, failure-injection, and venue certification evidence |
| APIs | Python/CLI, schemas, research and analysis contract surfaces | Authenticated, authorized, idempotent institutional services |
| Live operation | Execution-runtime code, adapters, safety and recovery tests; portfolio readiness scaffold | Credentialed operational qualification and production evidence |

This matrix is controlled by the [Implementation Reference Register](../../../registers/IMPLEMENTATION_REFERENCES.md). A later commit requires a new audit before any “current” cell is expanded.
