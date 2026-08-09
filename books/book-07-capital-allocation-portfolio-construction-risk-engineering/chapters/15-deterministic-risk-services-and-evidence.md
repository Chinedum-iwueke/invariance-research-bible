<a id="b7-c15"></a>
# Chapter 15 — Deterministic Risk Services and Evidence

Risk services turn governed policy into repeatable decisions. They must be deterministic for equal canonical state, fail closed where state is unsafe, and expose every input and binding rule.

## 15.1 Service boundaries

Separate forecast normalization, risk-state aggregation, covariance and scenario services, allocator, pre-trade risk, margin, capacity, constraint evaluation, post-trade reconciliation, monitoring, and incident response. Each has versioned input and output schemas.

## 15.2 Decision record

Every target and order approval records timestamp; state snapshot; prices and FX; positions, cash, pending orders, collateral, and margin; forecasts and uncertainty; risk model and scenarios; costs and capacity; objective; constraints and active set; solver status; rounding; output; reasons; policy version; and actor or service identity.

## 15.3 State and consistency

Authoritative state is reconciled. Stale or contradictory position, balance, price, or order state blocks risk increases. Idempotency prevents duplicate approvals. Replays from the same snapshot reproduce the decision within declared numeric tolerance.

## 15.4 Fallbacks

Solver, model, or data failure invokes a named fallback: hold, reduce, flatten, use conservative static limits, or escalate. Fallback cannot create greater risk than the failed path was authorized to create.

## 15.5 Acceptance

Book VII is accepted when the institution can normalize candidates, estimate joint and tail risk with uncertainty, construct feasible portfolios, include costs and capacity, survive path and margin stress, stage capital, monitor and demote, and reproduce every risk decision from primary evidence.

> **Risk rule B7-RK15 — Risk decisions are replayable**  
> No capital or order authorization is valid without the canonical state, policy, constraints, computation result, and reason required to reconstruct it.

## Source note

Book V provides deterministic simulation patterns; Book VIII supplies executable venue state; Book X deploys these services.
