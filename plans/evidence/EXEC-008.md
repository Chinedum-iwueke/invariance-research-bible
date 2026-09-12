# EXEC-008 completion evidence

Completed 2026-09-12.

## Ownership and behavior

- Bulletproof merge `03ec779dd489ddd8498406405cd208f94ba8cd14` owns capability matrices, drill evaluation, evidence class, expiry and admission.
- Hermes merge `f4eec14bbe0b7137c88517dce63b457da4b5186c` owns immutable schema registration and exact receipt custody only.
- Micro-live authorization now requires the exact integrity-verified EXEC-008 receipt for the live venue and environment, still within its validity window.
- Deterministic conformance can never certify a demo or live environment.

## Verification

- Bulletproof focused certification, adapter and live-authorization suite: 19 passed before the final pilot expansion; the native pilot executes the broader Binance/Bybit conformance set and exited zero.
- Hermes: 770 backend tests passed; scoped Ruff passed; Alembic resolves to one head.
- Native report digest: `0f587aa5e43e5df8e67d02ea00baae53d994d0e8b133b2d7b4ff864cd916775f`.
- Deployed cross-repository report digest: `a31f26cec93092ed7547128506c67f11867ecb1ecaab3b0a0a1ba55376211941`.

## Production deployment

- VM2 migration: `b5e1f8d37c40`.
- VM2 image: `sha256:9babb9566d96c43c0cf11c7c53bd39a0094d6310d9fd13877be277ec0dd80d5e`, healthy.
- Schema: `b9bf1690-90c4-41ba-8fe5-3bb818ca5270`, digest `4e9c541bc2b23cc107fac125930d0ec7ed9ee4b0c167941905d3ce7741617cfc`.
- Bybit receipt record: `9dfb51c4-f358-4f69-8ca9-7b18b506b787`, receipt digest `1ecc54bb4425c1418547f6be30c5f49e37e31d153e920ad94923d973160dcb6c`.
- Binance receipt record: `48068d01-3664-4688-b27d-7d8b207889d8`, receipt digest `bf5f507af958f2a5f73404541584c50b095211e07da56832ea99f62d09b97de1`.
- Retained VM2 report: `/home/omenka/.local/state/exec008/report.json`, mode `0600`.

## Claim boundary and rollback

The deployed receipts are `conformance_only`, not venue observations. Both adapters are
currently ineligible for demo execution and micro-live. DEMO-001 must run the same drills
against real demo endpoints and retain current environment evidence. Rollback preserves
all dossiers, withholds or revokes admission, and leaves external submission frozen.
