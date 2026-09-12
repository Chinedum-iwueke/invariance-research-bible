# EXEC-009 evidence

## Ownership

Bulletproof is the authoritative producer for execution-degradation measurement,
diagnosis, incidents and bounded response recommendations. Hermes registers the
versioned contract and retains exact receipts. It performs no market calculation and
has no order, capital, allocation, promotion or restoration authority.

## Implemented contract

- Point-in-time observations with immutable identity and source digests.
- Explicit venue/environment/strategy/instrument/order/size/regime strata.
- Fill, latency, shortfall, adverse-selection, queue-error, rejection,
  reconciliation, service and venue-rule signals.
- Separate venue, model, strategy and infrastructure diagnoses.
- Consecutive-breach confirmation for noncritical degradation.
- Immediate fail-closed review for outage or stale venue rules.
- Immutable incident digests and exact producer receipt.
- Independent-review-only restoration after restriction, fallback, demotion or kill.
- Exact same-dataset, allowlisted-producer EXEC-005, EXEC-008 and SHADOW-002
  receipt binding, with matching candidate and adapter venue/environment identities
  plus immutable GOV-003/PLAT-005 context digests.

## Verification

The native focused suite passes fourteen tests. The Hermes registry and receipt suite
passes twenty-five focused tests. The deterministic native pilot proves healthy,
confirmed strategy degradation, critical outage and false-recovery behavior. The
cross-repository pilot verifies exact immutable replay after migration
`d7a3f1c59e20` is deployed.

Live venue evidence is intentionally absent until EXEC1 is provisioned and DEMO-001
produces current venue-observed evidence. This dossier proves source behavior and
contract integrity, not live exchange availability.
