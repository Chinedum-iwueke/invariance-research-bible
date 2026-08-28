# Quantitative computation ownership closure

Date: 2026-08-28

## Closed milestones

DATA-001, DATA-002, DATA-003, DISC-002, DISC-003, DISC-004, DISC-005,
DISC-007, ML-002, ML-003, ML-004, RL-001, RL-002, RISK-001 and RISK-002.

## Evidence chain

- Bulletproof producer commit: `597a7697226b82f4c28f5e152c7df1067babba09`
- Bulletproof merge: `80db509bfdbfc08c2420f1099650c77a22c7fc4d`
- Native producer report digest: `5fc1b293fcc0e1cebcdc29fa7fe36b36d0f8ee99a081f650651ce3dae054bb2e`
- Bulletproof verification: 1,304 passed and 27 skipped
- Hermes receipt-registry merge: `54c444722d55057a2e8d4b8bdb5845f8dbbb3575`
- Hermes migration: `f4d9b3e57c10`
- Hermes verification: 628 passed
- VM2 deployment: migration at head and rebuilt API healthy
- Cross-repository live replay: 15 registered and 15 exactly replayed
- Replay SHA-256: `c77c865342facd8f6b2c15bbe94a6c6243b5b6e88e452920fb21c83c54ec7aff`
- Capital, allocation, order and promotion authority: false

## Definition-of-done result

The authoritative calculation now runs in `bulletproof_bt`; its source commit,
inputs, dataset, configuration, artifacts and result are digest-bound. Hermes
consumes the receipt, validates the allowlisted producer/milestone contract,
stores the immutable envelope and replays the exact digest. Hermes does not
recalculate or silently reinterpret the scientific result.

The deterministic closure fixtures are engineering evidence, not market
evidence. They close repository ownership and interoperability only. Claims of
alpha, model skill, data completeness, portfolio fitness or trading readiness
remain subject to prospective evaluations and later promotion gates.
