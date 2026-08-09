<a id="b5-c09"></a>
# Chapter 9 — Research Questions, Hypotheses, and Trial Contracts

The engine should not begin with a configuration grid. It should begin with a registered question whose executable consequences can be inspected before outcomes are known.

## 9.1 From question to execution

Book IV owns the scientific hypothesis contract: question, mechanism, alternatives, scope, information set, expected observations, falsification, metrics, evidence access, and search budget. Book V compiles the supported portions into engine configuration, strategy or hypothesis code, data scope, execution assumptions, and artifact requirements.

Compilation must produce a readiness report. Unsupported operators, ambiguous clocks, missing stops, unavailable fields, incompatible instruments, or unimplemented metrics block execution or create an explicit limited-evidence mode. They must not be replaced silently.

## 9.2 Current contract surfaces

The pinned repository contains typed hypothesis contracts, materializers, registries, logging helpers, tier rules, and many family-specific hypothesis modules and tests. It also publishes JSON schemas for hypothesis cards and specifications, strategy specifications, experiment plans, compile readiness, and related research lifecycle objects.

Current hypothesis contracts lock details such as signal timeframe, base frequency, gate model, stop model, update cadence, fit method, holding-time unit, and logging expectations for covered families. Materialization tests establish that declared variants become configurations deterministically for tested cases.

These are repository-specific executable contracts. They do not replace the institution’s broader scientific rationale and alternative-explanation record.

## 9.3 Trial identity

A trial is one fully resolved run identity inside a registered experiment family. Its identity binds hypothesis version, parameter assignment, representation, data scope, code pin, configuration, seed, and evaluation contract. An infrastructure retry is another attempt of the same trial. An amended parameter or metric is a new trial or experiment version.

The Trial Registry in Book II records authorization and exposure. Book V emits attempt and run evidence. Book III preserves lineage. This separation prevents an output directory name from becoming institutional identity.

## 9.4 Research tiers

The repository distinguishes signal-discovery evidence from portfolio-style evidence through research modes and tiers. That distinction is scientifically useful: a relaxed discovery run can study signal episodes without claiming deployable account behavior, while a portfolio-style run applies account constraints and supports different questions.

Tier labels are meaningful only when their required controls are validated. A string in configuration cannot certify that costs, constraints, or artifacts were actually applied. Run status and truth validation must check the claimed tier.

## 9.5 Invalidity and negative evidence

A valid trial with no effect is negative scientific evidence. A trial with missing artifacts, future leakage, inconsistent risk, failed parsing, or unsupported semantics is invalid. A runtime failure is operational evidence. These dispositions must not share one “failed” bucket.

> **Laboratory rule B5-LR09 — Compilation preserves scientific intent**  
> An executable trial is admissible only when every material transformation from hypothesis contract to runtime input is attributable and semantics-preserving.

## Source note

Current statements derive from pinned hypothesis contracts, schemas, registries, materializers, research-tier documentation, and tests. Scientific hypothesis ownership remains in Book IV and trial authority in Book II.
