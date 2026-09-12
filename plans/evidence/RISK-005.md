# RISK-005 completion evidence

## Ownership and implementation

Bulletproof PR #292 merged as `14596cbab85fb2df7be24985d8dd5f51dbb0e53d`
and owns the deterministic real-time risk producer and broker-boundary enforcement.
Hermes PRs #231-#232 merged through
`f3a6af861297e4b3dd967557f185bf1d31123eb5` and own migration
`e2b7c5f94d10`, immutable schema activation and exact native-receipt custody. Hermes
does not recompute the quantitative decision.

## Contract evidence

- Exact RISK-002/003/004 and EXEC-001/004 producer receipts are mandatory.
- Order fields, candidate, dataset, state version and causal clocks are digest bound.
- Stale, future, raced, partitioned, unreconciled and limit-breaching requests fail closed.
- Degraded authorization is possible only for a verified exposure-reducing order.
- Emergency cancellation and freeze/close remain independent.
- Every receipt has allocation, capital, order and promotion authority set to false.

## Verification

Nineteen focused Bulletproof tests, 203 broader risk/execution tests and the full 1,475
test suite with 28 declared skips passed. The
deterministic native pilot emitted `allow`, `deny`, and `reduce_only_exit`. Twenty focused
and 757 full Hermes tests passed, Ruff and all CI gates passed, and Alembic reports one head. The pilot evidence class
is `deterministic_qualification_fixture`; it is not evidence of candidate admission or a
real exchange submission.

VM2 runs healthy image
`sha256:c9e606135c52856ddccca61be2188cfb5185c6cf0d28409308f28c0d8b6eb6a2`
and active schema `f5b47f51-f0cb-4681-989e-4664db917e9f` with exact specification
digest `665a25ba672e32ee449ca41bf18db2b8bc8ed6dc4fea2db83f4d0a7cba407f0a`.
An activation-time source-hash transcription was corrected only after verifying zero
dependent RISK-005 receipts. The follow-up deployment rejects a same-version source
commit drift probe. The first genuine decision receipt remains contingent on a real
RISK-004-admitted candidate and current upstream state; fabricating it would violate the
truth boundary.
