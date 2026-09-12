# RISK-003 completion evidence

Date: 2026-09-12

- Authoritative producer: `bt.institutional.risk_budget.dynamic_risk_budget_receipt`
- Bulletproof source: `f5d80f97b318ba14f84863595cc8e0740dca0de6`
- Bulletproof merge: PR #289, `24ea8c5d44a76ed85097a14aacdfdadfb6fc97a6`
- Native tests: 17 focused; 1,430 full-suite passed; 28 declared skips
- Native CI: all collection, lint and contract shards passed
- Native receipt: `e21533c0fa1a2242c16005f4daba206134af5aadb13ea69107789cc4643fde61`
- Policy-schema digest: `bd876f5de05e0a90a06f29ae3db1a29b1e16c736af4dcc5f897afdf31d05b367`
- Budget-trajectory digest: `6c27f2da9713157cc58ad45f9bda4f4519b24703ff68c74201fdb1d5cf752f0b`
- Hermes source: `a987a9f`
- Hermes merge: PR #228, `3d0535787e434837fd8fdcda0049e460401e970d`
- Hermes tests: 18 focused; 746 full backend; Ruff clean
- Migration: `b8d4f0c69a71`, single head
- VM2 migration: `b8d4f0c69a71` at head
- VM2 API image: `sha256:b9dd898a560585c6179217f05175c5a6cb7a5491a77d19291637f3ef392939cc`, healthy
- Registered schema: `e16641dc-8267-4f0f-9610-99433cc66f83`
- Registered quantitative receipt: `261a8c36-2126-4c80-9e52-f8429b15acb1`
- Credentialed replay receipt digest: `e21533c0fa1a2242c16005f4daba206134af5aadb13ea69107789cc4643fde61`
- Credentialed replay report digest: `475d6bcbf40da4a3307c84b0e4f2b88cb01dec6882eea3cc018e208ac4485d9b`
- Credentialed replay result: success; effective risk `0.003` / `$300`; stale input selects `static_conservative_fallback`; uncertainty monotonic
- Retained report: `/var/lib/invariance-swarm/risk003/report.json`, mode `0600`, owner `root:root`
- Allocation, capital, order and promotion authority: false

The deterministic fixture proves causal shock reduction, delayed and bounded recovery,
uncertainty monotonicity, expiry fallback, capacity capping and exact receipt mechanics.
It does not establish a live venue allocation, authorize capital, or permit an order.
