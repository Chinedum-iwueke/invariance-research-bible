# ADR-0004: Orthogonal epistemic, maturity, environment, and operational states

**Status:** Accepted  
**Date:** 2026-08-08

## Context

The Founder’s Editions combine belief strength, scientific maturity, validation environment, and operating health in several linear promotion lists. This creates impossible orderings, including production before portfolio eligibility, and encourages a strategy to inherit scientific confidence merely by entering a new environment.

## Decision

Represent four linked but independent state dimensions:

1. **Epistemic state:** unknown, proposed, disputed, supported, weakened, rejected, retired, or another typed claim state defined by evidence semantics.
2. **Candidate maturity:** registered, screened, replicated, robust, portfolio eligible, production eligible, degraded, quarantined, retired.
3. **Validation environment:** backtest, robustness, shadow, execution replay, demo, micro-live, production.
4. **Operational state:** unavailable, ready, running, paused, degraded, halted, recovering, retired.

A governance transition cites evidence from one or more environments and may change candidate maturity. Merely running in an environment does not confer maturity. Operational health does not establish alpha, and epistemic confidence does not grant capital authority.

## Consequences

Schemas require separate fields and transition records. Dashboards may project a combined view but cannot collapse the underlying states. Book II owns maturity and authority; Book III owns epistemic records; Books V and VIII own environment evidence; Book X implements operational state services.

