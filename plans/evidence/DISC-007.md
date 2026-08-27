# DISC-007 Completion Evidence

## Delivered

- Immutable selection audits bound to complete BT-006 family ledgers and DISC-006 evaluations.
- Retention of completed, failed and cancelled trials with exact specification digests.
- Preregistered stopping and declared-versus-observed researcher-degree accounting.
- Family-wise, FDR, selection-adjusted Sharpe and validation-split PBO diagnostics.
- Blocking findings for optional stopping, hidden choices and favorable family truncation.
- Immutable audit supersession without erasing attempts or prior conclusions.

## Verification

- Implementation: control-plane PR #162, merge
  `91e88dfcc879d5d19e68af3decde61b1a82f063f`.
- VM2 pilot compatibility/canonicalization: PRs #163 and #164, ending at
  `0721f1c4d487c7f98dd670c98b268c67bf0958fa`.
- Production evidence: PR #165, merge
  `86c7f4f38e60f5393e6f061ba7e3c7494d41ad9e`.
- VM2 migration: `d7f1a4b63c90`; rebuilt API healthy with the audit route.
- Full backend suite: 475 passed with two warnings; focused suite: 13 passed.
- Audit ID: `45b83a75-8831-4ced-a0f3-93a5d78e981e`.
- Audit digest: `f8bf5a21bf539e0b4e46cf4b54405d0cd4e0fcaa9d0a1c47950d43ec487dd62f`.
- Ledger digest: `2501ebf92252f312d07f6a6da8e24f87717ef52f9bd764105a3e2553727da1e7`.
- Report digest: `bad4c9db76f3aceec9a06cc8652519707c517e5e223e3434f56a9867b71ed8a0`.
- Retained report file SHA-256:
  `b29bd406cf374bd1ca2788963b693643dd809e9865cd717e4378303f07a09dc2`.

The no-capital VM2 replay proved that nominal significance cannot hide complete-family
selection risk: p-value `0.02` became family-wise p-value `0.08`, while failed and
cancelled attempts remained visible. No promotion, execution, order or capital
authority was granted.

## Rollback

Disable new audit registration and retain all ledgers and audits. A corrected policy
or ledger receives a new immutable audit linked through `supersedes_audit_id`; rollback
cannot delete failed trials, shrink a family or rewrite a prior conclusion.
