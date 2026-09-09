# ALPHA-001 Completion Evidence

## Verdict

Source implementation is complete and locally validated as of 2026-09-09. Production
activation is pending and is not inferred by this record.

## Implemented boundary

- Bulletproof owns a deterministic ALPHA-001 real-data admission receipt.
- Hermes requires that receipt plus consistent DATA-002 build/catalog and DATA-003
  governance records before registering a campaign.
- An immutable DISC-009 selection, dataset scope, source commit and finite budgets are
  frozen before founder activation.
- Every answer binds its selected question and retains candidate, negative, invalid or
  failed evidence.
- Candidate state requires complete BT-009 publication and independent no-capital
  gates, and permits only prospective shadow review.
- A continuous director and Mission Control surface expose active and terminal state.

Local verification passed 702 Hermes backend tests, 72 Mission Control tests, 1,336
Bulletproof tests with 27 declared skips, and 7 Bible tests with 11 subtests. Ruff,
JavaScript syntax, Python compilation, Alembic-head, OpenAPI-route, shell-syntax,
systemd-unit and whitespace checks passed.

## Live-data observation

The source producer inspected the canonical local Bybit BTCUSDT perpetual 1-minute
research panel. It observed 2,827,851 strictly ordered rows with no duplicate
timestamps from `2021-01-01T00:00:00Z` through `2026-05-18T18:50:00Z` and bound the
required fields and acquisition manifests. Dataset digest
`9a211d8818c5ab8ec82ad5a7d38957e63eb387ea83d4b00541922a0eeca4aacb`
and receipt digest
`fbc73f7b0896ce7f64f97e677b9e6a19bd530968197ec2f290cab08aeb64f6ff`
are retained outside source control. This observation does not establish exchange attestation, alpha, shadow
fitness, demo readiness or live authority.

## Remaining production proof

Deploy Hermes migration `e3f7a1c94b20` and the rebuilt API on VM2, register the exact
panel through DATA-002/003 if not already present, install the campaign director,
bootstrap and activate the campaign, then retain one terminal BT-009 real-data attempt.
Until that completes, status is `source-complete`, not `production-active`.
