<a id="b8-c07"></a>
# Chapter 7 — Order Types and Lifecycle Semantics

An order type is a venue contract, not a portable label. The canonical order model must express intent and map only to verified native semantics.

## 7.1 Intent

Record instrument, side, quantity, order kind, price and trigger, time in force, reduce-only, post-only, client identity, parent identity, expiry, and risk context. Signed quantity and side have one canonical convention.

## 7.2 Lifecycle

States include created, risk-approved, submitted, acknowledged, partially filled, filled, cancellation requested, cancelled, rejected, expired, and unknown pending reconciliation. Acknowledgement is not fill. Cancellation request is not cancellation.

## 7.3 Native differences

Market, limit, stop, stop-limit, immediate-or-cancel, fill-or-kill, good-till-cancelled, post-only, and reduce-only behavior varies. Trigger sources and price protection matter. Unsupported combinations fail closed.

## 7.4 Idempotency

Stable client order identity and deduplication prevent retry from creating another economic order. Amend and cancel operations bind original order and expected state. Late events remain reconcilable.

## 7.5 Evidence

Persist every request, canonical-to-native mapping, signed payload digest, response, event, state transition, and reason. Secrets are excluded.

> **Execution rule B8-EX07 — Acknowledgement is provisional**  
> Only reconciled venue lifecycle events establish order state; transport success or an accepted request does not establish fill or cancellation.

## Source note

This chapter formalizes the execution-runtime boundaries audited in Book V and generalizes them beyond one adapter.
