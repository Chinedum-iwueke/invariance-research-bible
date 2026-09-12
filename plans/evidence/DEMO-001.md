# DEMO-001 evidence

## Claim

The production-like Bybit demo certification contract is implemented and fails closed. DEMO-001 is not operationally certified because the required venue pass cannot run from the present hosts.

## Implemented boundary

- Bulletproof computes the certification; Hermes stores only its immutable schema and exact receipt.
- Each drill records whether it is venue-observed or an authenticated in-environment replay and binds a content digest.
- Venue observation is mandatory for authentication, clock, current instrument constraints, order/fill/cancel/amend/rejection behavior, private reconnect, restart reconciliation and final flattening.
- The adapter now retains `minOrderQty`, `maxOrderQty` and `minNotionalValue` from current Bybit instrument metadata.
- Qualification expires and requires exact dependency receipts, a PLAT-005 digest, a secret-free credential fingerprint, no withdrawal authority, the demo endpoint and a zero-order/zero-position terminal state.

## External blocker observed on 2026-09-12

Both VM1 and VM2 returned HTTP 403 for unauthenticated `https://api-demo.bybit.com/v5/market/time`. No `BYBIT_DEMO_API_KEY` or `BYBIT_DEMO_API_SECRET` was available to the execution process. The system therefore sent no order, created no venue-observed receipt and grants no demo or micro-live eligibility.

## Source and deployment evidence

- Bulletproof PR #297: merge `41eaaaeb73aa95b8bfec40563a0f6d0f421ee113`; 1,503 tests passed with 28 declared skips and all CI shards passed.
- Hermes PR #237: merge `3f4eb263046f7423fdf5e701560d1cac5bb5185b`; 774 backend tests and all CI gates passed.
- VM2: migration `c6f2a9d48b70`; healthy image `sha256:edc7aac7b4149db86b08d3cc1a227eb8715a4c91cefc532fe63ac6381f383c22`.
- Active immutable schema: `240bfa4c-1f98-48de-80c3-be4297dfd5e8`, digest `64376e2bbeb981f47282218bbc567d2872db455618833f91e9d78dd18fc5ca8d`.
- No DEMO-001 quantitative receipt was registered because no venue run completed.

## Remaining acceptance

Run from a Bybit-permitted always-on execution host with dedicated demo trade credentials. Complete every drill, prove final flat state, register the exact receipt in Hermes and retain the dossier. A failed venue drill is a terminal failed certification, not permission to weaken a threshold.
