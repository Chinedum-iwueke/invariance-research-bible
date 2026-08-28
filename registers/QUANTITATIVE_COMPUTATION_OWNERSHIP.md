# Quantitative computation ownership

## Binding rule

`bulletproof_bt` is the sole authoritative producer of scientific and quantitative
calculations used by the systematic-research company. The control plane may validate,
compare, gate, register, route and replay digest-bound receipts, but it may not become
an alternative backtest, feature, model, statistical-search, portfolio or risk engine.

## Repository responsibilities

| Responsibility | Owner | Boundary |
|---|---|---|
| Dataset materialization, point-in-time joins and quality computation | `bulletproof_bt` | Emits immutable manifests and receipts |
| Backtests, features, labels, statistical search and selection adjustment | `bulletproof_bt` | Emits complete native run/search evidence |
| ML training, evaluation, calibration and inference | `bulletproof_bt` | Emits model bundles and evaluation receipts |
| Offline-RL dataset construction and estimators | `bulletproof_bt` | Emits support, estimator and stress receipts |
| Portfolio, drawdown, tail, margin and liquidation mathematics | `bulletproof_bt` | Emits candidate and risk receipts |
| Canonical identity, registry, lifecycle, approvals and policy admission | `swarm-control-plane` | Verifies exact producer digests and derives institutional decisions |
| Worker execution and publication | Swarm workers | Invokes pinned Bulletproof producers and transports receipts without recomputation |
| Requirements and acceptance evidence | Research Bible | Declares ownership and records cross-repository proof |

Deterministic recomputation in the control plane is allowed only for small independent
integrity checks explicitly labelled `validator`, never as the source of a scientific
estimate. A validator disagreement fails closed and creates an incident; it does not
silently replace the Bulletproof result.

## Completion gate

A computational milestone is complete only when all of the following exist:

1. A versioned Bulletproof-native producer on `bulletproof_bt` main.
2. Native tests covering causality, determinism, failure and replay boundaries.
3. An immutable producer receipt with code, configuration, dataset and artifact digests.
4. A control-plane schema that consumes and verifies that receipt without re-implementing the producer.
5. One live no-capital end-to-end replay from Bulletproof through Hermes.
6. Bible evidence naming both repository commits and the live receipt digest.

A schema, fixture, registry, gate or API by itself cannot close a computational
milestone. Until all six conditions pass, status is `reopened: producer missing` or
`planned`, even when its governance slice is deployed.

As of 2026-08-28, all six conditions pass for DATA-001..003,
DISC-002..005/007, ML-002..004, RL-001..002 and RISK-001..002. The qualified
producer is Bulletproof merge `80db509bfdbfc08c2420f1099650c77a22c7fc4d`;
Hermes merge `54c444722d55057a2e8d4b8bdb5845f8dbbb3575` supplies the immutable
consumer registry. The retained live replay registered and read back all 15
receipts without allocation, capital, order or promotion authority.

PORT-002 also satisfies the six-part completion gate. Bulletproof merge
`79caf1d334a5e80d03cf644875dfa022d09c952a` is the authoritative dependency,
diversification and concentration producer. Hermes merge `3a2a38ba15d455263281c42d06881d7aebc601d0`
only admits its immutable receipt. VM2 replayed receipt `70f4ff8045875341e8f324cd2a1f44ff22a309d4dc0362c011b5a51a1c5138be`
exactly and granted no allocation, capital, order or promotion authority.

PORT-003 satisfies the same gate. Bulletproof merge
`866e1c1c0ab23b0bb65fa795030eabf1daedfcb1` owns every benchmark, covariance,
optimization, rounding, sensitivity and fallback calculation. Hermes merge
`ffbb9bc5e39873672d3f260c6fb8a50f07b018c3` registers the exact versioned solver
and verifies its receipt without recomputation. VM2 replayed receipt
`c196ca8f43a1c67c49284b111df44083ba8e076cdb75097b90844ebc5e414825`
exactly and granted no allocation, capital, order or promotion authority.
