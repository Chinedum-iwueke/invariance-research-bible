# PORT-004 completion evidence

Date: 2026-09-12

- Authoritative producer: `bt.institutional.capacity.capacity_dossier_receipt`
- Bulletproof source commit: `159a79b7ee1bbf19e6208c8b5216fb0046178d44`
- Bulletproof merge: `ccddacee049dbc97d6bba5912f623a4d8345a8bd` (PR #288)
- Capacity schema digest: `4f2d3384ac29a2aabefd4d79560c4ed2aeda8482157dcdbc1f23177b5c0ee06a`
- Producer receipt: `8c2dc0602e74c76f60c2307e8531817a0aee99b31fcb6db10cb1f3c70758aaf7`
- Capacity dossier: `ef30b343cc3cf241a9519913897d6c61f926ecae910876c00ea3ade94b7dcb4b`
- Native report SHA-256: `d64581d46f170316fd8b534c3676eb15225aacf1223960f1c3214503292a97ca`
- Deterministic fixture: `$100,000` supported notional; `$230,000` base capacity; `$140,000` stressed capacity; `$20,000` turnover
- Stale-liquidity fixture: zero supported notional and `abstain_zero_executable_capacity`
- Bulletproof verification: 14 focused tests and every required CI shard passed
- Supported local suite: 1,408 passed and 28 declared skips; five volatile-panel failures reproduce in the untouched EXEC-004 checkout
- Hermes source commit: `75ed1eb9cbdae2d128e011d83aae3484747b59b7`
- Hermes merge: `6097eb39a02ad1f6ca0849783d3731d4fc29480d` (PR #227)
- Hermes verification: 742 backend tests and all required CI gates passed
- Migration head: `a7c3e9b58f60`
- VM2 image: `sha256:5b9d598d6fa1dbaf3a00673b51ff4f5742d90a168379acf1587750f6876b4183`, healthy
- Live OpenAPI route: `/v1/research/portfolio-capacity-schemas`
- Allocation, capital, order and promotion authority: false
- Live schema registration: `1ceb8bc7-49ff-4627-ba15-0a25d978cbe5`
- Live quantitative receipt: `b4999dba-e29d-44d9-9a27-19c3be0bf0c6`
- Credentialed replay report digest: `de5d0965038cca501fd15477951a0e9af1e6f4d8605dccced8ffcb483c8e9edd`
- Retained report: `/var/lib/invariance-swarm/port004/report.json`, mode `0600`, owner `root:root`
- Exact credentialed cross-repository replay: complete, `success: true`

The fixture proves deterministic point-in-time turnover, cost, capacity, stress,
abstention and receipt-replay mechanics. It does not establish current Bybit/Binance
liquidity, authenticated venue continuity, profitability or permission to trade.
