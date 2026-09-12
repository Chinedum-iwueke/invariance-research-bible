# EXEC-006 completion evidence

## Ownership and contract

Bulletproof is the authoritative scheduler producer. It emits immutable market, limit,
TWAP and causal-profile VWAP schedules and pessimistic cost comparisons derived from
qualified EXEC-005 strata. Hermes registers the active schema and preserves exact
producer receipts; it does not calculate slices, choose an algorithm or release orders.

Schedules bind parent intent, candidate, side, quantity, reference price, urgency,
window, projected interval volume, participation caps, child deadlines and causal
volume-profile digest. Future VWAP profiles, invalid windows, thin-volume conflicts,
undersized children, excessive horizons, aggressive limit prices, unknown child states,
clock drift and schedule tampering fail closed. Partial fills carry toward the next
cumulative target only within that child's participation cap.

Every submit remains a two-step boundary. The scheduler emits `propose_submit` with no
authority. It becomes `submit` only after an exact, fresh RISK-005 receipt matches the
child's symbol, side, quantity, reference price, reduce-only flag and current state
version. Cancellation remains available without an exposure-increasing authorization.

## Verification

The Bulletproof dependency suite passes 57 focused EXEC-004/005, RISK-005 and EXEC-006
tests. The Hermes schema and receipt-custody suite passes 21 tests and Alembic reports
one head at `f3c8d6a15e20`. The native qualification replay deterministically produces a
four-child causal VWAP schedule, retains market/limit/TWAP/VWAP pessimistic cost
comparisons and proves its first action is unauthorized. This fixture grants no capital
or order authority and is not real venue evidence.

Bulletproof PR #293 merged as `abd40ef81d812e9d600de187606766d238b4b638`;
its full suite passed 1,483 tests with 28 declared skips and every CI shard passed.
Hermes PR #233 merged as `21bc3857ed844f1e0f44539180c9d3fdfff1e926`;
761 backend tests and every CI gate passed. VM2 runs migration `f3c8d6a15e20` and
healthy image
`sha256:2d41566521dc9747faa5284ccf34fc004d4085d29dd3eacde4454a3d5f1b01cb`.
The deployed replay registered active schema
`fd9d7e1b-7e14-41e3-ba2d-aa67502dc8da`, exact receipt
`1b7713a7-58f8-49cc-b8e7-86599fb86f7b`, schedule digest
`21426406e40a9f765ac4693ac5a6845868ed623288ab7cd2164b0b1a4d368a6b` and
report digest `44baeec8d21d202c32eb58832d2e66a67167cd2c564c78a1f6d42926d5bcf830`.
The retained report is mode `0600`; it proves scheduler qualification, not a real fill.
