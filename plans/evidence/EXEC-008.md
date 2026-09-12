# EXEC-008 completion evidence

Completed 2026-09-12.

## Ownership and behavior

- Bulletproof merges `03ec779dd489ddd8498406405cd208f94ba8cd14` and `bacfcd4f6334cd40f8e36ba9460fcf1ead326cb9` own capability matrices, drill evaluation, evidence class, expiry, admission and corrected Binance reconnect.
- Hermes merge `f4eec14bbe0b7137c88517dce63b457da4b5186c` owns immutable schema registration and exact receipt custody only.
- Micro-live authorization now requires the exact integrity-verified EXEC-008 receipt for the live venue and environment, still within its validity window.
- Deterministic conformance can never certify a demo or live environment.

## Verification

- Bulletproof focused certification, adapter, lifecycle, safety and live-authorization suite: 34 passed. Both private streams were disconnected and re-authenticated deterministically; Binance acquired a fresh listen key.
- Hermes: 770 backend tests passed; scoped Ruff passed; Alembic resolves to one head.
- Corrected native report digest: `262629f3b30f795e9997484e3999635ea74ee10806de569a30a4ebd2ff70dd32`.
- Corrected deployed cross-repository report digest: `f7e0f9105f57299e51d27ee3363909736822a78a0a8d1edadff936afefdfa8b9`.

## Production deployment

- VM2 migration: `b5e1f8d37c40`.
- VM2 image: `sha256:9babb9566d96c43c0cf11c7c53bd39a0094d6310d9fd13877be277ec0dd80d5e`, healthy.
- Schema: `b9bf1690-90c4-41ba-8fe5-3bb818ca5270`, digest `4e9c541bc2b23cc107fac125930d0ec7ed9ee4b0c167941905d3ce7741617cfc`.
- Bybit receipt record: `347d2c37-49c1-48f1-bf2c-43617602d3e8`, receipt digest `d21473fe5d5ae4ffb9463b018b16592b96a3167b0d1cbf82cda338f765c1a4e6`.
- Binance receipt record: `0f98d24c-2245-499e-99a5-019aa8cc961c`, receipt digest `e9c6844820324b292878a0dc0f01af3d7dc5096ac1a6dfa22ffb6c778719b009`.
- Retained VM2 report: `/home/omenka/.local/state/exec008/report-v2.json`, mode `0600`.

## Claim boundary and rollback

The deployed receipts are `conformance_only`, not venue observations. Both adapters are
currently ineligible for demo execution and micro-live. DEMO-001 must run the same drills
against real demo endpoints and retain current environment evidence. Rollback preserves
all dossiers, withholds or revokes admission, and leaves external submission frozen.
