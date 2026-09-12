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
- Exact credentialed cross-repository replay: staged; pending operator execution

The fixture proves causal observation filtering, split isolation, empirical distribution
construction, holdout scoring, digest replay and pessimistic fallback behavior. It does
not prove authenticated venue continuity, current live-stratum qualification, adapter
certification, profitability or permission to submit an order.
