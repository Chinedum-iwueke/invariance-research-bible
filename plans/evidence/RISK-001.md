# RISK-001 completion evidence

## Delivered

- Immutable risk-stress request, server-derived dossier, API and PostgreSQL registry.
- Drawdown path, tail uncertainty, five mandatory failure mechanisms and five reverse-stress brackets.
- Fail-closed freshness and upper-envelope policy with no allocation, order or capital authority.
- Idempotent registration and exact assessment replay.

## Verification

- Control-plane PRs: #189 and #190.
- Deployed source: `de6839bea5bc2d29d7e78ab879adc29625b50d4b`.
- VM2 migration: `f2b7e1d35a80`.
- Backend: 609 passed, two pre-existing deprecation warnings.
- Focused RISK-001 suite: 13 passed.
- CI: all required suites passed on both PRs.

## Live evidence

- Assessment: `b7713035-e37d-4841-8ecc-acd809409de8`.
- Dossier digest: `1860339b7bded1a112f5579b35a985260919502c4ee4ee1c0a2884f73afeeed4`.
- Report digest: `2aca9632d5bfef72075181196fa8e6b38f973b67e47d899b7c2a970b9a9b1200`.
- Decision: `admissible`; exact replay: true.
- Maximum drawdown: 0.12; tail-loss upper bound: 0.14.
- Reverse-stress first-breach shocks: price gap 1.5, correlation break 1.6, liquidity freeze 1.7, model failure 1.8 and prolonged drawdown 1.9.

The live values are deterministic control-path fixtures. They do not establish portfolio quality or authorize allocation, orders, or capital.
