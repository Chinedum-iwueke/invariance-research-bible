<a id="b8-c11"></a>
# Chapter 11 — OMS, Adapters, and Reconciliation

The order-management system maintains canonical intent and lifecycle. Venue adapters translate and transport; they do not redefine portfolio or risk policy.

## 11.1 OMS authority

The OMS owns client identities, parent-child lineage, desired and known state, deduplication, transitions, and audit journal. Adapter responses are evidence incorporated through validated mappings.

## 11.2 Adapter contract

An adapter implements instrument discovery, authentication, clock and rate handling, submit, amend, cancel, open orders, fills, positions, balances, public and private streams, error taxonomy, and environment isolation. Demo and live credentials and endpoints cannot cross.

## 11.3 Reconciliation

Compare local orders, fills, positions, balances, and sequence checkpoints with authoritative venue surfaces. Differences are classified by timing, mapping, duplication, missing event, external activity, or unknown. Material uncertainty freezes risk increases.

## 11.4 Recovery

On restart, load durable state, resynchronize venue facts, replay unresolved events, reconcile, and apply policy. Safe continuation is proven; it is not assumed from a checkpoint.

> **Execution rule B8-EX11 — Venue truth is reconciled, not trusted blindly**  
> Authoritative external state and canonical internal intent are compared through typed mappings; contradictions trigger a controlled state rather than silent overwrite.

## Source note

This chapter generalizes public execution-runtime patterns audited in Book V. Deployment durability belongs to Book X.
