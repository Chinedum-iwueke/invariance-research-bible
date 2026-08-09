<a id="b5-c07"></a>
# Chapter 7 — Configuration Resolution and Determinism

Configuration is executable scientific input. Defaults, aliases, environment values, inheritance order, and command-line overrides can change the experiment as surely as source code.

## 7.1 Current resolution surface

The pinned repository contains core configuration resolution, default engine configuration, instrument packs, strategy overrides, research tiers, execution profiles, stop canonicalization, and validators for completeness and legacy duplicates. Tests cover deep merging, alias handling, profile resolution, supported-key completeness, local grid overlays, and configuration used by API entry points.

Every completed classic run is expected to preserve `config_used.yaml`, the fully resolved configuration. That artifact outranks the author’s intended input file when diagnosing what ran.

## 7.2 Canonical resolution

A resolver needs a published precedence order. A suitable order is stable defaults, market and instrument pack, research tier, experiment base, strategy or hypothesis materialization, authorized run overrides, and finally narrowly permitted command-line values. Environment variables may supply secrets or deployment endpoints but should not silently alter scientific parameters.

After merging, aliases are converted to one canonical key, types and ranges are validated, mutually exclusive options are rejected, and unknown keys fail unless the schema explicitly permits extension. The canonical object is serialized with deterministic ordering and becomes part of run identity.

## 7.3 Seeds and concurrency

Stochastic research requires explicit pseudorandom algorithm, seed, stream derivation, and parallel partition policy. A top-level seed is insufficient if worker count changes draw order. Seeds should derive from stable run and component identities, not process scheduling.

The current engine emphasizes deterministic strategy behavior and includes deterministic wave scheduling and serial/parallel parity tests for covered paths. This is scoped evidence. Filesystem iteration, floating-point reductions, third-party numerical kernels, and unordered concurrency can still create variation unless controlled.

## 7.4 Run identity

Target run identity is a digest over canonical scientific inputs: implementation commit, resolved configuration, dataset manifest, hypothesis and strategy versions, schema versions, estimator identity, seed policy, and declared environment compatibility class. Output directory and wall-clock creation time do not belong to scientific identity.

An attempt identity distinguishes retries of the same run identity. This lets infrastructure retries remain visible without pretending they are new scientific trials.

## 7.5 Determinism tests

The pinned tests compare deterministic JSON writes byte for byte, reject non-finite floats, and compare repeated end-to-end outputs while removing known variable manifest fields. The manifest writer itself records current UTC creation time and run directory. Consequently, repository language promising “identical outputs” must be read as normalized scientific equivalence for covered artifacts, not universal directory byte identity.

Target checks run a small golden experiment twice, in different output paths and supported worker configurations; normalize declared operational fields; and compare event, trade, equity, metric, and artifact digests. Differences fail closed.

> **Laboratory rule B5-LR07 — Resolved input is the experiment**  
> Intended configuration has no evidentiary authority once it diverges from the validated, serialized configuration actually executed.

## Source note

Current statements derive from pinned configuration resolvers, config tests, deterministic formatting, run-manifest behavior, artifact determinism tests, and parallel-run documentation.
