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
