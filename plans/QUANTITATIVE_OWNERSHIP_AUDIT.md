# Quantitative ownership audit

Audit date: 2026-08-28. Repositories inspected: `bulletproof_bt` origin main at
`c3f8c0a`, `swarm-control-plane` main at `176c1c744c161f79083aa70afa04781537d864d9`,
and the canonical Research Bible.

## Verdicts

| Milestone | Verdict | Bulletproof producer | Control-plane role | Required action |
|---|---|---|---|---|
| BT-001..009 | Complete | Present | Contract registry/publication where applicable | Preserve split |
| SHADOW-001 | Complete | Present | Evidence publication | Preserve split |
| ML-001 | Complete | Present in `bt.ml.registry` | Model lifecycle projection | Preserve split |
| PORT-001 | Complete | Present in `bt.portfolio_engine.candidate_service` | Candidate evidence projection | Preserve split |
| WS-001 | Complete | Uses native BT-009 publication | No-capital saga and compensation | Preserve split |
| DATA-001 | Complete | Native point-in-time snapshot producer and receipt | Temporal identity registry | Closed by digest-bound live replay |
| DATA-002 | Complete | Native immutable catalog and availability producer | Catalog registry | Closed by digest-bound live replay |
| DATA-003 | Complete | Native lake quality, lineage and entitlement producer | Operations registry | Closed by digest-bound live replay |
| DISC-002 | Complete | Native observation/opportunity effect producer | Map registry/admission | Closed by digest-bound live replay |
| DISC-003 | Complete | Native factor compiler and executable receipt | Independent validator and registry | Closed by digest-bound live replay |
| DISC-004 | Complete | Native budgeted proposal/search-state producer | Budget/lifecycle registry | Closed by digest-bound live replay |
| DISC-005 | Complete | Native constrained symbolic candidate producer | Sandbox policy/registry | Closed by digest-bound live replay |
| DISC-006 | Complete governance capability | No quantitative producer required | Mechanism and falsification registry | Quantitative decisive tests must reference BT receipts |
| DISC-007 | Complete | Native family/selection-bias audit producer | Audit admission registry | Closed by digest-bound live replay |
| DISC-008 | Complete orchestration capability | Uses BT task contracts | Bounded supervision | Preserve split |
| DISC-009 | Complete orchestration capability | Consumes admitted evidence | Attention scheduler | Preserve split; never treat rank as alpha estimate |
| ML-002 | Complete | Native causal feature/label/split materializer | Manifest validator | Closed by digest-bound live replay |
| ML-003 | Complete | Native model-family and regime evaluator | Scorecard validator/gate | Closed by digest-bound live replay |
| ML-004 | Complete | Native calibration, uncertainty and abstention producer | Qualification gate | Closed by digest-bound live replay |
| RL-001 | Complete | Native transition, propensity, reward and support producer | Dataset contract/audit registry | Closed by digest-bound live replay |
| RL-002 | Complete | Native conservative off-policy estimator producer | Conservative admission gate | Closed by digest-bound live replay |
| RISK-001 | Complete | Native drawdown, tail, scenario and reverse-stress producer | Scenario admission registry | Closed by digest-bound live replay |
| RISK-002 | Complete | Native venue-rule margin and liquidation producer | Rule registry and independent validator | Closed by digest-bound live replay |

## Closure evidence

All 15 reopened milestones closed on 2026-08-28. Bulletproof merge `80db509`
contains the native producers and Hermes merge `54c4447` contains the receipt
consumer. The live VM2 replay registered and exactly read back all 15 receipts;
the retained replay SHA-256 is `c77c865342facd8f6b2c15bbe94a6c6243b5b6e88e452920fb21c83c54ec7aff`.

## Other completed milestones

BASE, RI, GOV, AGT, CHAN, UI, OPS, PLAT and SEC milestones primarily own identity,
knowledge infrastructure, governance, communication, operations or security. Their
completed status is not invalidated by this audit because they do not claim to produce
market, statistical, model, portfolio or risk estimates. Their quantitative inputs must
still reference Bulletproof receipts whenever they consume such evidence.

DISC-001, DISC-006, DISC-008 and DISC-009 remain complete only as institutional
director, falsification-structure, supervision and attention-allocation capabilities.
They cannot manufacture performance evidence, fill missing metrics or promote a
hypothesis without native Bulletproof results.
