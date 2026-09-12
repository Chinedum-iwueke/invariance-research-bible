# EXEC-005 completion evidence

Date: 2026-09-12

- Authoritative producer: `bt.institutional.execution_calibration.execution_calibration_receipt`
- Bulletproof source commit: `d6cde7665385732d0f49deafbaac324161da33d9`
- Bulletproof merge: `97d20db19b81054b729c0fb11a2ca1657aa4c632` (PR #287)
- Calibration schema digest: `3f66c4d7b3742e23b47ff32856e4304fe73a475585a33b39092f799679b29049`
- Producer receipt: `fc819372f8cedde7a1e4ad99162eb9d2e5d5a59d4432e8f26c7575d9581be434`
- Calibration digest: `e1aa6787a920c155159c39f0c56746ae96f3f0826034e6bc22b6ebec540687d9`
- Empirical market-model bundle: `e46c1ea0e0a0e826673496cbe1a023022ee7059db62314c04469b5358d26fbdf`
- Native report SHA-256: `6bdfad0635f6a247b16d877dda4d08d11a13128fe26c4a2003baebf133efda35`
- Native result: one future observation excluded; sparse stratum selected the 5 bps pessimistic fallback
- Bulletproof verification: 15 focused tests, all required CI shards and Ruff passed
- Supported local suite: 1,394 passed and 28 declared skips; five volatile-panel failures reproduce unchanged in the untouched EXEC-004 checkout under the same shared environment
- Hermes source commit: `7bd40a980d93c22c800f26ed0d217e00798d3385`
- Hermes merge: `5906127939090b30a114efdf1d9d243d85fdebde` (PR #226)
- Hermes verification: 738 backend tests and all required CI gates passed
- Migration head: `f6b2d8a47e50`
- VM2 image: `sha256:6e2199467f35b38b010d11130d6c2d23f78b674fa5bf2417dad43fd437a39bc7`, healthy
- Live OpenAPI route: `/v1/research/execution-calibration-schemas`
- Allocation, capital, order, promotion, routing and cancellation authority: false
- Live execution-calibration schema: `88d60d24-441c-4019-8c1f-5d3d79cbe761`
- Live quantitative receipt: `a08d562a-09bd-465b-86ed-534255fbcc96`
- Cross-repository report digest: `f061249f89d4823597480491ebf9aa327d70f2dddbba200ce67d617961163fd5`
- Retained report: `/var/lib/invariance-swarm/exec005/report.json`, mode `0600`, owner `root:root`
- Exact credentialed cross-repository replay: complete; `success: true`

The fixture proves causal observation filtering, split isolation, empirical distribution
construction, holdout scoring, digest replay and pessimistic fallback behavior. It does
not prove authenticated venue continuity, current live-stratum qualification, adapter
certification, profitability or permission to submit an order.
